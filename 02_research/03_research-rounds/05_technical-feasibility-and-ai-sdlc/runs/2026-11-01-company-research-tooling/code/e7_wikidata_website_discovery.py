"""E7: find official websites with Wikidata (wbsearchentities + P856). Free, official API, no key."""
import json, time, urllib.parse, urllib.request
from pathlib import Path
RUN = Path(__file__).resolve().parents[1]
UA = "JobHubResearchBot/0.1 (research experiment; prasath.rishi@gmail.com)"
def get(params):
    u = "https://www.wikidata.org/w/api.php?format=json&" + urllib.parse.urlencode(params)
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30))
NAMES = {"P01": "Moda Paolo", "P02": "Yan Business Group", "P03": "Palo IT", "P04": "Grab", "P05": "Ang Mo Kio - Thye Hua Kwan Hospital",
         "P06": "Singapore General Hospital", "P07": "HRnetGroup", "P08": "DHL Supply Chain", "P09": "Supreme HR Advisory", "P10": "Marina Bay Sands",
         "P11": "Natureland", "P12": "NTUC FairPrice", "P13": "Curos Learning", "P14": "Little Skool-House", "P15": "Randstad"}
out = []
for pid, n in NAMES.items():
    r = get({"action": "wbsearchentities", "search": n, "language": "en", "limit": 3, "type": "item"})
    hits = []
    for h in r.get("search", []):
        c = get({"action": "wbgetclaims", "entity": h["id"], "property": "P856"})
        sites = [x["mainsnak"]["datavalue"]["value"] for x in c.get("claims", {}).get("P856", []) if "datavalue" in x["mainsnak"]]
        hits.append({"id": h["id"], "label": h.get("label"), "desc": h.get("description"), "websites": sites})
    out.append({"id": pid, "query": n, "hits": hits}); print(pid, n, "->", [(h["label"], h["websites"][:1]) for h in hits][:2], flush=True)
    time.sleep(1)
(RUN / "outputs/e7_wikidata_websites.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
