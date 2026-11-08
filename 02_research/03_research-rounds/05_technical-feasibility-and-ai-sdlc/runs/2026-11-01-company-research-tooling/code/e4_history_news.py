"""E4: Wayback CDX (site age/continuity) and GDELT DOC 2.0 (recent news mentions). No keys."""
import json, time, urllib.parse, urllib.request
from pathlib import Path
RUN = Path(__file__).resolve().parents[1]
UA = "JobHubResearchBot/0.1 (research experiment; prasath.rishi@gmail.com)"
postings = {p["id"]: p for p in json.loads((RUN / "data/postings.json").read_text(encoding="utf-8"))}
sites = {s["id"]: s["url"] for s in json.loads((RUN / "outputs/e2_plain_fetch.json").read_text(encoding="utf-8")) if s.get("url")}
QUERIES = {"P01": "Moda Paolo", "P02": "Yan Business Group", "P03": "Palo IT", "P04": "Grab", "P05": "Ang Mo Kio-Thye Hua Kwan Hospital",
           "P06": "Singapore General Hospital", "P07": "HRnetGroup", "P08": "DHL Supply Chain Singapore", "P09": "Supreme HR Advisory",
           "P10": "Marina Bay Sands", "P11": "Natureland", "P12": "NTUC FairPrice", "P13": "Curos Learning", "P14": "Little Skool-House", "P15": "Randstad Singapore"}
def get(u, t=45):
    return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=t).read().decode("utf-8", "replace")
out = []
for pid in postings:
    rec = {"id": pid}
    t0 = time.time()
    if pid in sites:
        host = urllib.parse.urlparse(sites[pid]).netloc.removeprefix("www.")
        try:
            rows = json.loads(get("https://web.archive.org/cdx/search/cdx?output=json&fl=timestamp&collapse=timestamp:4&filter=statuscode:200&url=" + urllib.parse.quote(host)))
            yrs = [r[0][:4] for r in rows[1:]]
            rec["wayback"] = {"host": host, "years_with_captures": yrs, "first_year": yrs[0] if yrs else None, "n_years": len(yrs)}
        except Exception as e:
            rec["wayback"] = {"host": host, "error": f"{getattr(e,'code',type(e).__name__)}"}
        time.sleep(4)
    else:
        rec["wayback"] = None
    try:
        q = urllib.parse.quote(f'"{QUERIES[pid]}"')
        d = json.loads(get(f"https://api.gdeltproject.org/api/v2/doc/doc?query={q}%20sourcecountry:SN&mode=artlist&maxrecords=10&format=json&timespan=6months&sort=datedesc"))
        arts = d.get("articles", [])
        rec["gdelt"] = {"query": QUERIES[pid], "articles": len(arts), "titles": [(a["seendate"][:8], a["domain"], a["title"][:90]) for a in arts[:3]]}
    except Exception as e:
        rec["gdelt"] = {"query": QUERIES[pid], "error": f"{getattr(e,'code',type(e).__name__)}:{str(e)[:60]}"}
    time.sleep(12)
    rec["seconds"] = round(time.time() - t0, 1); out.append(rec); print(pid, rec["wayback"] and {k: rec["wayback"].get(k) for k in ("n_years", "first_year", "error")}, rec["gdelt"].get("articles", rec["gdelt"].get("error")), flush=True)
(RUN / "outputs/e4_history_news.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
