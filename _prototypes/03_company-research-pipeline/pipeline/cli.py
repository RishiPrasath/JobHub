"""python -m pipeline.cli <command>. Data lives in $JOBHUB_DATA (default ./data)."""
import argparse, json, os, urllib.parse
from pathlib import Path

from . import acra, extract, pagefetch, sitecache, wayback, websearch

DATA = Path(os.environ.get("JOBHUB_DATA", "data"))
DB = DATA / "acra.sqlite"


def main():
    ap = argparse.ArgumentParser(prog="pipeline")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("acra-update", help="download ACRA CSVs and rebuild the index")
    sub.add_parser("acra-index", help="rebuild the index from CSVs already in $JOBHUB_DATA/acra_csv")
    r = sub.add_parser("resolve")
    r.add_argument("employer")
    r.add_argument("--uen")
    r.add_argument("--hint")
    b = sub.add_parser("batch-resolve")
    b.add_argument("postings_json")
    b.add_argument("out_json")
    s = sub.add_parser("research")
    s.add_argument("employer")
    s.add_argument("--site", required=True)
    s.add_argument("--uen")
    s.add_argument("--hint")
    q = sub.add_parser("search", help="optional keyless DuckDuckGo search (needs JOBHUB_ENABLE_DDG=1)")
    q.add_argument("query")
    f = sub.add_parser("find-site", help="registry match, optional search, then verify each candidate homepage")
    f.add_argument("employer")
    f.add_argument("--uen")
    f.add_argument("--hint")
    a = ap.parse_args()
    if a.cmd == "search":
        print(json.dumps(websearch.search(a.query), indent=1))
    elif a.cmd == "find-site":
        reg = acra.resolve(DB, a.employer, a.uen, a.hint)
        chosen = reg["chosen"] or {}
        legal, uen = chosen.get("name", a.employer), chosen.get("uen")
        cache = DATA / "sites.sqlite"
        if uen and reg["state"] in ("exact", "exact_by_uen", "likely"):
            hit = sitecache.get(cache, uen)
            if hit:
                print(json.dumps({"registry_state": reg["state"], "legal_name": legal, "from_cache": True, "site": hit}, indent=1))
                return
        words = [t for t in acra.toks(legal) if t not in ("singapore", "holdings", "group", "international") and len(t) > 2]
        found = websearch.search(legal.replace(".", " ") + " Singapore")
        by_url = {r["url"]: r for r in found["results"]}
        checked = []
        for url in websearch.official_site_candidates(found["results"])[:4]:
            p = pagefetch.fetch(url)
            head = (p.get("title", "") + " " + p["text"][:3000]).lower()
            hit = [w for w in words if w in head]
            frac = len(hit) / len(words) if words else 0
            level = "verified" if frac == 1 else "probable" if frac >= 0.6 else "unverified"
            if p["status"] not in ("ok", "thin"):
                level = "page_unreadable"
            checked.append({"url": url, "page_status": p["status"], "name_words_found": "%d/%d" % (len(hit), len(words)), "match": level,
                            "search_title": by_url[url]["title"], "search_description": by_url[url]["description"]})
        best = next((c for c in checked if c["match"] == "verified"), None)
        if best and uen and reg["state"] in ("exact", "exact_by_uen", "likely"):
            sitecache.put(cache, uen, legal, best["url"], best["search_title"], best["search_description"], best["match"], found["source"])
        print(json.dumps({"registry_state": reg["state"], "legal_name": legal, "search_source": found["source"], "search_status": found["status"],
                          "search_note": found.get("note"), "unresponsive_engines": found.get("unresponsive_engines"), "candidates": checked}, indent=1))
        return
    if a.cmd == "acra-update":
        print("csv files:", acra.download(DATA / "acra_csv"))
        print("rows indexed:", acra.build_index(DATA / "acra_csv", DB))
    elif a.cmd == "acra-index":
        print("rows indexed:", acra.build_index(DATA / "acra_csv", DB))
    elif a.cmd == "resolve":
        print(json.dumps(acra.resolve(DB, a.employer, a.uen, a.hint), indent=1))
    elif a.cmd == "batch-resolve":
        out = []
        for p in json.loads(Path(a.postings_json).read_text(encoding="utf-8")):
            res = acra.resolve(DB, p["employer"], p.get("uen"), p.get("hint"))
            out.append({"id": p["id"], "employer": p["employer"], **res})
            print(p["id"], res["state"], "|", (res["chosen"] or {}).get("name", "-"), "|", res["why"])
        Path(a.out_json).write_text(json.dumps(out, indent=1), encoding="utf-8")
    elif a.cmd == "research":
        report = {"employer": a.employer, "registry": acra.resolve(DB, a.employer, a.uen, a.hint)}
        page = pagefetch.fetch(a.site)
        report["page"] = {k: v for k, v in page.items() if k != "text"}
        report["history"] = wayback.years(urllib.parse.urlparse(a.site).netloc)
        if page["status"] in ("ok", "thin") and page["text"]:
            report["answers"] = extract.extract(page["text"])
        else:
            report["answers"] = {"note": "page not read; reported as blocked/unavailable, not as absence of evidence"}
        print(json.dumps(report, indent=1))


main()
