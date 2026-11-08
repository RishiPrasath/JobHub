"""X1 Arm A: fixed six-query sweep per company via OpenSERP (DuckDuckGo, Bing fallback). Saves titles/URLs/snippets."""
import json, time, urllib.parse, urllib.request, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATES = ['"{n}" Singapore regulator penalty fine', '"{n}" enforcement action Singapore',
             '"{n}" court judgment Singapore', '"{n}" complaints Singapore',
             '"{n}" retrenchment layoffs Singapore', '"{n}" scam fraud warning Singapore']
d = json.load(open(ROOT / "data/x1_companies.json", encoding="utf-8"))
names = [k["name"] for k in d["known"]] + d["controls"]


def search(q):
    for eng in ("duckduckgo", "bing"):
        url = "http://localhost:7000/%s/search?text=%s&limit=8" % (eng, urllib.parse.quote(q))
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                j = json.load(r)
            res = [x for x in j.get("results", []) if x.get("type") == "organic"][:8]
            if res:
                return eng, [{"title": x["title"], "url": x["url"], "snippet": x.get("snippet", "")} for x in res]
        except Exception as e:
            err = str(e)
    return "none", []


out = {}
for n in names:
    out[n] = []
    for t in TEMPLATES:
        q = t.format(n=n)
        eng, res = search(q)
        out[n].append({"query": q, "engine": eng, "results": res})
        time.sleep(7)
    print(n, [len(x["results"]) for x in out[n]], flush=True)
    json.dump(out, open(ROOT / "outputs/x1/armA_search.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
