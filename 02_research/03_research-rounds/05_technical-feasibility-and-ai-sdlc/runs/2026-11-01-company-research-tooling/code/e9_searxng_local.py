"""E9: query a local SearXNG container (http://127.0.0.1:8888) for each employer; report URLs, titles, descriptions, engines."""
import json, sys, time, urllib.parse, urllib.request
from collections import Counter
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
BASE = "http://127.0.0.1:8888/search?format=json&q="
SKIP = ("linkedin.com", "glassdoor.", "indeed.", "jobstreet.", "mycareersfuture", "facebook.com", "instagram.com", "acrawatch", "sgpbusiness",
        "companieshouse", "recordowl", "sgpgrid", "straitsdata", "wikipedia.org", "jooble", "fastjobs", "carousell", "youtube.com", "tiktok",
        "yelp.", "tripadvisor", "mothership", "straitstimes", "lazada", "shopee", "opengovsg", "cbinsights", "zoominfo", "dnb.com", "sg.jobsdb")
EXPECT = {"P03": "palo-it.com", "P04": "grab.com", "P05": "amkh.org.sg", "P06": "sgh.com.sg", "P07": "hrnetgroup.com", "P08": "dhl.com",
          "P10": "marinabaysands.com", "P11": "natureland", "P12": "fairprice.com.sg", "P14": "littleskoolhouse", "P15": "randstad.com"}


def host(u):
    return urllib.parse.urlparse(u).netloc.lower().removeprefix("www.")


def main():
    acra = {r["id"]: r for r in json.loads((RUN / "outputs/e1c_acra_rules_v2.json").read_text(encoding="utf-8"))}
    out, engines = [], Counter()
    for pid, r in acra.items():
        legal = (r["chosen"] or {}).get("name") or r["employer"]
        q = legal.replace(".", " ").strip() + " Singapore"
        t0 = time.time()
        try:
            d = json.load(urllib.request.urlopen(BASE + urllib.parse.quote(q), timeout=40))
        except Exception as e:
            out.append({"id": pid, "query": q, "error": type(e).__name__}); print(pid, "ERROR", type(e).__name__); continue
        res = d.get("results", [])
        for x in res:
            engines.update(x.get("engines", [x.get("engine")]))
        cand = []
        seen = set()
        for x in res:
            h = host(x["url"])
            if h in seen or any(s in h for s in SKIP):
                continue
            seen.add(h); cand.append({"url": x["url"], "title": (x.get("title") or "")[:100], "description": (x.get("content") or "")[:160], "engines": x.get("engines")})
        exp = EXPECT.get(pid)
        rank = next((i + 1 for i, c in enumerate(cand) if exp and exp in c["url"]), None)
        out.append({"id": pid, "query": q, "n_results": len(res), "unresponsive": d.get("unresponsive_engines"), "expected_domain": exp,
                    "expected_rank_among_non_directory": rank, "top_candidates": cand[:4], "seconds": round(time.time() - t0, 1)})
        print(pid, f"{len(res)} results | expected {exp} rank {rank} | top:", [host(c["url"]) for c in cand[:3]], "| unresp:", d.get("unresponsive_engines"), flush=True)
        time.sleep(3)
    (RUN / "outputs/e9_searxng_local.json").write_text(json.dumps({"engines_seen": engines.most_common(), "rows": out}, indent=1), encoding="utf-8")
    print("engines:", engines.most_common())


main()
