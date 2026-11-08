"""The three outside services this flow uses: the company registry, OpenSERP (search only), and the page reader."""
import re
import urllib.parse

from . import config
from .http import Unavailable, call

# ---------------------------------------------------------------- registry (existence and identity)


def registry_check(name, uen=None, url=None):
    """GET /check on the registry service. Raises Unavailable when the registry cannot answer."""
    q = {"name": name}
    if uen:
        q["uen"] = uen
    if url:
        q["url"] = url
    code, j = call("GET", config.REGISTRY_URL + "/check?" + urllib.parse.urlencode(q), timeout=15)
    if code == 503:
        raise Unavailable("registry is still being provisioned")
    if code != 200:
        raise Unavailable("registry answered HTTP %s: %s" % (code, str(j.get("error") or j)[:100]))
    return j


# ---------------------------------------------------------------- search (OpenSERP, search only)


def web_search(q, limit=8):
    """One query. Returns {'ok', 'unavailable', 'results', 'engine', 'error'}; an unreachable service is not an empty result."""
    out = {"query": q, "ok": False, "unavailable": False, "results": [], "engine": None, "error": None}
    path = "/mega/search?" + urllib.parse.urlencode({"text": q, "mode": "any", "engines": config.SEARCH_ENGINES, "limit": limit})
    try:
        code, j = call("GET", config.OPENSERP_URL + path, timeout=150)
    except Unavailable as e:
        out.update(unavailable=True, error=str(e))
        return out
    if code != 200:
        out["error"] = "%s: %s" % (j.get("error") or code, j.get("message") or "")
        return out
    out["results"] = [{k: r.get(k) for k in ("rank", "engine", "title", "url", "domain", "snippet")}
                      for r in j.get("results", []) if r.get("type") == "organic"]
    out["engine"] = sorted({r["engine"] for r in out["results"]}) or None
    out["ok"] = True
    return out


def build_queries(names, role=""):
    """Entity-aware queries: the exact name in quotes, plus the registered legal name when it differs."""
    n = names[0]
    qs = ['"%s" Singapore employee reviews' % n,
          '"%s" scam OR fraud OR complaints' % n,
          '"%s" layoffs OR retrenchment OR restructuring' % n,
          '"%s" %s interview process salary' % (n, role) if role else '"%s" interview process salary' % n]
    qs.append('"%s" company profile UEN' % (names[1] if len(names) > 1 else n))
    return [re.sub(r"\s+", " ", q).strip() for q in qs][:config.MAX_QUERIES]


# ---------------------------------------------------------------- reading pages

# Sites we do not read: login-walled, or terms that restrict automated access, or unreadable in testing (Glassdoor 21/21 failed,
# Reddit returned a bot challenge). Their search snippets may still be used, labelled as snippet only.
LINK_OUT = ["linkedin.com", "glassdoor.", "reddit.com", "facebook.com", "instagram.com", "x.com", "twitter.com", "tiktok.com"]
LINK_OUT_CONSERVATIVE = LINK_OUT + ["indeed.com", "jobstreet.com"]
BLOCK = re.compile(r"captcha|verify you are human|prove your humanity|not for bots|complete the challenge|access denied|just a moment|"
                   r"enable javascript|unusual traffic|sign in to continue|join now to see|log in to (see|continue)|checking your browser|"
                   r"are you a robot|403 forbidden", re.I)
DATA_URI = re.compile(r"\(data:[^)]{40,}\)")
GENERIC = {"pte", "ltd", "limited", "singapore", "holdings", "group", "the", "and", "of", "company", "inc", "llc", "bank"}


# Sites that republish company-registry records. They show the registry says what it says; they are not independent evidence
# about the company, so they never count toward "several sources agree". (Found in run 2: Avanguarde's four 'agreeing' pages were
# three of these plus one job posting.)
REGISTRY_MIRRORS = ["sgpbusiness.com", "recordowl.com", "companies.sg", "opencorporates.com", "scam.sg", "ltddir.com"]


def is_registry_mirror(url):
    host = (urllib.parse.urlparse(url).hostname or "").lower().removeprefix("www.")
    return any(host == m or host.endswith("." + m) for m in REGISTRY_MIRRORS)


def name_tokens(*names):
    return sorted({w for n in names for w in re.findall(r"[a-z0-9]{3,}", n.lower()) if w not in GENERIC})


def link_out_reason(url):
    host = (urllib.parse.urlparse(url).hostname or "").lower().removeprefix("www.")
    for s in (LINK_OUT_CONSERVATIVE if config.READ_POLICY == "conservative" else LINK_OUT):
        if (s.endswith(".") and s[:-1] in host.split(".")) or host == s or host.endswith("." + s):
            return "link out only (%s): restricted or login-walled site" % s.strip(".")
    return None


def read_page(url, tokens):
    """Read one page and judge it. status: ok, thin, blocked, blocked_by_robots, irrelevant, error, skipped_by_policy, unavailable."""
    rec = {"url": url, "status": "error", "chars": 0, "text": "", "note": None, "tier": None}
    why = link_out_reason(url)
    if why:
        rec.update(status="skipped_by_policy", note=why)
        return rec
    try:
        if config.READER == "openserp":
            code, j = call("GET", config.OPENSERP_URL + "/extract?" + urllib.parse.urlencode({"url": url, "mode": "auto"}), timeout=120)
            if code != 200:
                msg = str(j.get("message") or j.get("error") or code)
                rec.update(status="blocked" if re.search(r"blocked|rate limited|40[13]|429", msg, re.I) else "error", note=msg[:140])
                return rec
            text, title, rec["tier"] = j.get("markdown") or j.get("text") or "", j.get("title") or "", (j.get("meta") or {}).get("mode_used")
        else:
            code, j = call("POST", config.FETCH_URL + "/fetch", {"Authorization": "Bearer " + config.FETCH_TOKEN}, {"url": url, "mode": "auto"}, timeout=120)
            if code != 200:
                rec.update(status="error", note="reader HTTP %s: %s" % (code, str(j.get("detail") or j.get("error") or "")[:100]))
                return rec
            if j.get("status") == "blocked_by_robots":
                rec.update(status="blocked_by_robots", note="the site's robots.txt does not allow this page")
                return rec
            if j.get("status") == "error":
                rec.update(status="error", note=str(j.get("error") or "")[:140])
                return rec
            text, title, rec["tier"] = j.get("text") or "", "", j.get("tier")
    except Unavailable as e:
        rec.update(status="unavailable", note=str(e))
        return rec
    text = DATA_URI.sub("(data:…)", text).strip()
    rec["chars"] = len(text)
    if (BLOCK.search(text[:800]) or BLOCK.search(title)) and len(text) < 2500:
        rec.update(status="blocked", note="challenge or login-wall text")
    elif len(text) < 400:
        rec.update(status="thin", note="fewer than 400 characters of real content")
    elif tokens and not any(t in text.lower() for t in tokens):
        rec.update(status="irrelevant", note="the page never mentions the company name")
    else:
        rec.update(status="ok", text=text)
    return rec
