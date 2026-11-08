"""Phase 2b: does page-to-Markdown extraction leave the main text, and how are blocked pages reported?
Eight page types, one company (Randstad Singapore). Pages for some types are chosen from a search so the
search-then-read path is exercised too. Nothing here logs in, solves a challenge or retries a blocked page."""
import json, os, re, time, urllib.error, urllib.parse, urllib.request

BASE = os.environ.get("OPENSERP_URL", "http://openserp:7000")
OUT = "/outputs/phase2/extract"
os.makedirs(OUT, exist_ok=True)

FIXED = [
    ("company_website", "https://www.randstad.com.sg/"),
    ("glassdoor_reviews", "https://www.glassdoor.sg/Reviews/Randstad-Singapore-Reviews-EI_IE302306.0,8_IL.9,18_IM1123.htm"),
    ("indeed_reviews", "https://sg.indeed.com/cmp/Randstad/reviews"),
    ("linkedin_company", "https://www.linkedin.com/company/randstad/"),
    ("gov_data_portal", "https://data.gov.sg/collections/2/view"),
    ("wikipedia_control", "https://en.wikipedia.org/wiki/Randstad_Holding"),
]
SEARCHED = [
    ("news_article", "Randstad Singapore", "channelnewsasia.com"),
    ("reddit_thread", "Randstad Singapore", "reddit.com"),
    ("forum_post", "Randstad", "forums.hardwarezone.com.sg"),
    ("blog_post", "my experience working at Randstad Singapore blog", None),
    ("registry_aggregator", "Randstad Pte Ltd UEN 199304055W company profile", None),
]
BOILER = re.compile(r"cookie|accept all|sign in|log in|subscribe|newsletter|privacy policy|terms of use|skip to (main )?content|©|all rights reserved", re.I)
BLOCK = re.compile(r"captcha|verify you are human|access denied|just a moment|enable javascript|unusual traffic|sign in to continue|join now|log in to (see|continue)|please wait|checking your browser|are you a robot", re.I)


def get(path, timeout=120):
    t = time.time()
    try:
        with urllib.request.urlopen(BASE + path, timeout=timeout) as r:
            return r.status, r.read(), time.time() - t
    except urllib.error.HTTPError as e:
        return e.code, e.read(), time.time() - t
    except Exception as e:
        return type(e).__name__, str(e).encode(), time.time() - t


def pick(text, site):
    q = urllib.parse.urlencode({"text": text, "limit": 8, **({"site": site} if site else {})})
    code, body, _ = get("/duckduckgo/search?" + q)
    time.sleep(8)
    try:
        res = [r for r in json.loads(body).get("results", []) if r.get("type") == "organic"]
    except Exception:
        return None
    skip = ("glassdoor", "indeed", "linkedin", "randstad.com")
    for r in res:
        if not any(s in r["url"] for s in skip) or site:
            return r["url"]
    return res[0]["url"] if res else None


def analyse(md):
    lines = [l for l in md.splitlines() if l.strip()]
    link_lines = sum(1 for l in lines if re.match(r"^\s*[-*]?\s*\[[^\]]+\]\(", l))
    words = len(md.split())
    return {"chars": len(md), "words": words, "lines": len(lines),
            "link_line_share": round(link_lines / max(len(lines), 1), 2),
            "boilerplate_hits": len(BOILER.findall(md)), "block_markers": sorted(set(m.lower() for m in BLOCK.findall(md)) if False else {m.group(0).lower() for m in BLOCK.finditer(md)}),
            "mentions_randstad": "randstad" in md.lower()}


def extract(label, url, mode="auto", clean=True):
    q = urllib.parse.urlencode({"url": url, "mode": mode, "clean": "true" if clean else "false"})
    code, body, secs = get("/extract?" + q)
    rec = {"label": label, "url": url, "mode_requested": mode, "clean": clean, "http": code, "seconds": round(secs, 2)}
    try:
        j = json.loads(body)
    except Exception:
        rec["raw_body"] = body[:300].decode("utf-8", "replace")
        return rec, ""
    if code != 200:
        rec["error"] = {k: j.get(k) for k in ("error", "code", "message", "reason") if k in j} or str(j)[:300]
        return rec, ""
    md = j.get("markdown") or j.get("text") or ""
    rec.update(title=(j.get("title") or "")[:90], mode_used=j.get("meta", {}).get("mode_used"), bytes_fetched=j.get("meta", {}).get("bytes"),
               took_ms=j.get("meta", {}).get("took_ms"), **analyse(md))
    return rec, md


targets = list(FIXED)
for label, text, site in SEARCHED:
    u = pick(text, site)
    print(f"picked {label}: {u}", flush=True)
    if u:
        targets.append((label, u))

rows = []
for label, url in targets:
    for mode in ("auto",):
        rec, md = extract(label, url, mode)
        rows.append(rec)
        open(f"{OUT}/{label}.md", "w", encoding="utf-8").write(md)
        print(f"{label:20} http={str(rec['http']):4} {rec['seconds']:6.1f}s mode_used={rec.get('mode_used')} chars={rec.get('chars')} boiler={rec.get('boilerplate_hits')} links%={rec.get('link_line_share')} block={rec.get('block_markers')} err={rec.get('error')}", flush=True)
        # one retry in rendered mode only when the first answer was empty or thin; never for a blocked status
        if rec["http"] == 200 and rec.get("chars", 0) < 500:
            rec2, md2 = extract(label, url, "rendered")
            rows.append(rec2)
            open(f"{OUT}/{label}_rendered.md", "w", encoding="utf-8").write(md2)
            print(f"{label:20} rendered retry http={rec2['http']} chars={rec2.get('chars')} block={rec2.get('block_markers')}", flush=True)
        time.sleep(4)

# whole-page vs article-only on the company site
for clean in (False,):
    rec, md = extract("company_website_full", FIXED[0][1], "auto", clean=clean)
    rows.append(rec)
    open(f"{OUT}/company_website_full.md", "w", encoding="utf-8").write(md)
    print(f"company_website clean=false chars={rec.get('chars')} boiler={rec.get('boilerplate_hits')} links%={rec.get('link_line_share')}", flush=True)

json.dump(rows, open("/outputs/phase2/extract_summary.json", "w", encoding="utf-8"), indent=1)
