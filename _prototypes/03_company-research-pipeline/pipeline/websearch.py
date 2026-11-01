"""Optional keyless web search via DuckDuckGo's HTML endpoint.

ON by default at the project owner's request (set JOBHUB_ENABLE_DDG=0 to turn it off). DuckDuckGo's robots.txt disallows /html and /lite for automated clients,
so this is an unsanctioned source: the owner of the project chose to enable it. Guardrails:
  - honest User-Agent, no header spoofing, no proxies, no retries after a block
  - at least MIN_INTERVAL seconds between requests
  - the first block signal (403/429/202/anti-bot page) trips a breaker; no further requests this process
  - results are labelled source="duckduckgo_html_unsanctioned"; every hit must still be verified against the registry name
"""
import html, os, re, time, urllib.error, urllib.parse, urllib.request

UA = "JobHubResearchBot/0.1 (research prototype)"
ENDPOINT = "https://html.duckduckgo.com/html/"
MIN_INTERVAL = float(os.environ.get("JOBHUB_DDG_MIN_INTERVAL", "2"))
SKIP_DOMAINS = ("linkedin.com", "glassdoor.", "indeed.", "jobstreet.", "mycareersfuture.gov.sg", "facebook.com", "instagram.com",
                "acrawatch.sg", "sgpbusiness.com", "companieshouse.sg", "recordowl.com", "sgpgrid.com", "straitsdata.com", "wikipedia.org",
                "jooble.", "fastjobs.", "carousell.", "youtube.com", "bebee.", "foundit.", "glints.", "jobleads.", "cultjobs.", "ltddir.",
                "scam.sg", "companies.sg", "threebestrated", "streetdirectory", "bloomberg.com", "opengovsg", "cbinsights", "zoominfo",
                "dnb.com", "tiktok.com", "yelp.", "tripadvisor.", "lazada.", "shopee.",
                # news, finance, directories and booking widgets that mention a company but are not its site (found by hand review, run 2026-11-01)
                "businesstimes.", "yahoo.com", "reuters.com", "healthcare.com.sg", "timesbusinessdirectory", "ihrp.sg", "picktime.",
                "edb.gov.sg", "nea.gov.sg", "thebigjobsite", "wikipedia.", "crunchbase.", "pitchbook.", "marketscreener.")
_state = {"last": 0.0, "tripped": None}


def enabled():
    return os.environ.get("JOBHUB_ENABLE_DDG", "1") != "0"


def searxng(query, max_results=10):
    """Local SearXNG container (JSON). Returns url, title (heading), description, and which engines answered."""
    base_url = os.environ.get("SEARXNG_URL", "http://127.0.0.1:8888").rstrip("/")
    wait = float(os.environ.get("SEARCH_MIN_INTERVAL", "3")) - (time.time() - _state["last"])
    if wait > 0:
        time.sleep(wait)
    _state["last"] = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(base_url + "/search?format=json&q=" + urllib.parse.quote(query),
                                                           headers={"User-Agent": UA}), timeout=40) as r:
            d = __import__("json").load(r)
    except Exception as e:
        return {"query": query, "source": "searxng_local", "status": "unavailable", "note": type(e).__name__, "results": []}
    res = [{"url": x["url"], "title": (x.get("title") or "").strip(), "description": (x.get("content") or "").strip()[:300],
            "engines": x.get("engines")} for x in d.get("results", [])[:max_results]]
    return {"query": query, "source": "searxng_local", "status": "ok" if res else "no_results",
            "unresponsive_engines": d.get("unresponsive_engines"), "results": res}


def search(query, max_results=8):
    """SearXNG first; direct DuckDuckGo only if SearXNG is not reachable."""
    s = searxng(query, max_results)
    if s["status"] != "unavailable":
        return s
    return ddg_search(query, max_results)


def ddg_search(query, max_results=8):
    base = {"query": query, "source": "duckduckgo_html_unsanctioned", "results": []}
    if not enabled():
        return {**base, "status": "disabled", "note": "JOBHUB_ENABLE_DDG=0 disables it; unset or 1 enables it"}
    if _state["tripped"]:
        return {**base, "status": "blocked", "note": "breaker tripped earlier: " + _state["tripped"]}
    wait = MIN_INTERVAL - (time.time() - _state["last"])
    if wait > 0:
        time.sleep(wait)
    _state["last"] = time.time()
    req = urllib.request.Request(ENDPOINT, urllib.parse.urlencode({"q": query}).encode(),
                                 {"User-Agent": UA, "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            code, body = r.status, r.read(500_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        _state["tripped"] = "HTTP %s" % e.code
        return {**base, "status": "blocked", "note": "HTTP %s; no retry" % e.code}
    except Exception as e:
        return {**base, "status": "failed", "note": type(e).__name__}
    if code != 200 or "anomaly" in body.lower() or "captcha" in body.lower():
        _state["tripped"] = "HTTP %s or anti-bot page" % code
        return {**base, "status": "blocked", "note": "anti-bot response; no retry"}
    out = []
    for m in re.finditer(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', body, re.S):
        href = html.unescape(m.group(1))
        q = urllib.parse.parse_qs(urllib.parse.urlparse(href).query).get("uddg")
        url = q[0] if q else href
        out.append({"url": url, "title": html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()})
        if len(out) >= max_results:
            break
    return {**base, "status": "ok" if out else "no_results_or_markup_changed", "results": out}


def official_site_candidates(results):
    """Drop job boards, directories and social pages; keep one URL per host."""
    seen, out = set(), []
    for r in results:
        host = urllib.parse.urlparse(r["url"]).netloc.lower().removeprefix("www.")
        if host and host not in seen and not any(s in host for s in SKIP_DOMAINS):
            seen.add(host)
            out.append(r["url"])
    return out
