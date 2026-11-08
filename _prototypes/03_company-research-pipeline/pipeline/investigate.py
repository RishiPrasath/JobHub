"""End-to-end company investigation for a list of employers:
registry match -> official site (cache, then local SearXNG, verified) -> page capture -> Wayback -> cited Groq answers.
Everything is reported with its status; a missing or blocked source is never reported as absence of evidence."""
import json, time, urllib.parse
from pathlib import Path

from . import acra, extract, pagefetch, sitecache, wayback, websearch

OK_STATES = ("exact", "exact_by_uen", "likely")


NOISE_PATHS = ("/news", "/watch", "/article", "/company-details", "/company/", "/shop/", "/tools/", "/partner-profile", "/blog", "/capital/",
               "/item/", "/job", "/career", "/listing", "/directory", "/profile", "/stories", "/press")


def homepage_shaped(url, words):
    """True when the URL looks like a company's own site rather than an article or listing about it:
    no news/listing path segment, and either a distinctive name word sits in the domain or the path is the root or one segment deep."""
    u = urllib.parse.urlparse(url)
    host = u.netloc.lower().removeprefix("www.").replace("-", "").replace(".", "")
    path = u.path.lower()
    depth = len([s for s in path.split("/") if s])
    if any(n in path for n in NOISE_PATHS):
        return False
    return any(w in host for w in words if len(w) >= 4) or depth <= 1


def find_site(db, cache, employer, uen=None, hint=None, replay=None):
    reg = acra.resolve(db, employer, uen, hint)
    chosen = reg["chosen"] or {}
    legal, c_uen = chosen.get("name", employer), chosen.get("uen")
    out = {"registry": {k: reg[k] for k in ("state", "why")} | {"chosen": reg["chosen"], "alternatives": [c["name"] for c in reg["candidates"][1:4]]},
           "legal_name": legal, "site": None, "text": ""}
    if c_uen and reg["state"] in OK_STATES:
        hit = sitecache.get(cache, c_uen)
        if hit:
            p = pagefetch.fetch(hit["url"])
            out.update(site={"url": hit["url"], "title": hit["title"], "match": hit["verified"], "found_by": "cache:" + hit["found_by"]},
                       text=p["text"], page={k: v for k, v in p.items() if k != "text"}, search=None)
            return out
    words = [t for t in acra.toks(legal) if t not in ("singapore", "holdings", "group", "international") and len(t) > 2]
    if replay is not None:   # saved results from an earlier search: lets rules be re-tested without querying the engines again
        found = {"source": "replayed_searxng_results", "status": "ok", "results": replay}
    else:
        found = websearch.search(legal.replace(".", " ") + " Singapore")
    out["search"] = {"source": found["source"], "status": found["status"], "note": found.get("note"),
                     "unresponsive_engines": found.get("unresponsive_engines"),
                     "top_results": [{"url": r["url"], "title": r["title"], "description": r["description"]} for r in found["results"][:5]]}
    tried = []
    for url in websearch.official_site_candidates(found["results"])[:3]:
        p = pagefetch.fetch(url)
        head = (p.get("title", "") + " " + p["text"][:3000]).lower()
        frac = (sum(w in head for w in words) / len(words)) if words else 0
        level = "unreadable" if p["status"] not in ("ok", "thin") else "verified" if frac == 1 else "probable" if frac >= 0.6 else "unverified"
        res = next(r for r in found["results"] if r["url"] == url)
        if level in ("verified", "probable") and not homepage_shaped(url, words):
            level = "article_or_listing"   # mentions the company but is not its own site
        tried.append({"url": url, "page_status": p["status"], "match": level})
        if level in ("verified", "probable"):
            out.update(site={"url": url, "title": res["title"], "description": res["description"], "match": level, "found_by": found["source"]},
                       text=p["text"], page={k: v for k, v in p.items() if k != "text"})
            if level == "verified" and c_uen and reg["state"] in OK_STATES:
                sitecache.put(cache, c_uen, legal, url, res["title"], res["description"], level, found["source"])
            break
    if not out["site"]:
        # A page we could not read (429, block) may still be clearly the company's own site: accept it only when the
        # search result's title carries every distinctive word of the legal name, and say the page was not read.
        for t in tried:
            if t["match"] == "unreadable":
                res = next(r for r in found["results"] if r["url"] == t["url"])
                head = (res["title"] + " " + res["description"]).lower()
                host = urllib.parse.urlparse(t["url"]).netloc.lower().replace("-", "").replace(".", "")
                # stricter than a readable page: the domain itself must carry a distinctive name word
                if words and all(w in head for w in words) and any(w in host for w in words if len(w) >= 4):
                    out["site"] = {"url": t["url"], "title": res["title"], "description": res["description"], "match": "found_unreadable",
                                   "found_by": found["source"]}
                    out["page"] = {"status": t["page_status"]}
                    break
    out["candidates_tried"] = tried
    return out


def investigate(db, cache, items, pause=8):
    results = []
    for it in items:
        t0 = time.time()
        r = {"id": it["id"], "employer": it["employer"], "job_title": it.get("job_title"), "job_url": it.get("job_url")}
        try:
            f = find_site(db, cache, it["employer"], it.get("uen"), it.get("hint"), it.get("replay_search"))
        except Exception as e:
            r["error"] = type(e).__name__ + ": " + str(e)[:120]; results.append(r); continue
        r.update(registry=f["registry"], search=f.get("search"), candidates_tried=f.get("candidates_tried"))
        if f["site"]:
            r["site"] = f["site"]; r["page"] = f.get("page")
            r["history"] = wayback.years(urllib.parse.urlparse(f["site"]["url"]).netloc)
            if f["text"]:
                time.sleep(pause)   # stay under Groq's free tokens-per-minute limit
                r["answers"] = extract.extract(f["text"])
            else:
                r["answers"] = {"note": "site found but page unreadable (blocked or empty); not evidence of absence"}
        else:
            r["site"] = None
            r["answers"] = {"note": "no verified official site found; registry record only"}
        r["seconds"] = round(time.time() - t0, 1)
        results.append(r)
        print(it["id"], "|", it["employer"][:34], "| registry:", f["registry"]["state"], "| site:", (f["site"] or {}).get("url", "none"), flush=True)
    return results
