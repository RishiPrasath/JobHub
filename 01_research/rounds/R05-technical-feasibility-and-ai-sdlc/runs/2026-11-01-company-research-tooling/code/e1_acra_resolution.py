"""E1: resolve employer names against ACRA open data (data.gov.sg), no API key."""
import json, re, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from difflib import SequenceMatcher
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
BASE = "https://data.gov.sg"
SUFFIX = re.compile(r"\b(pte|ltd|limited|private|co-operative|singapore|sg|holdings|international|the)\b\.?", re.I)

def get(url, tries=2):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "JobHub-research/0.1"}), timeout=20) as r:
                return json.load(r)
        except Exception as e:
            code = getattr(e, "code", None)
            time.sleep(3)
    return None

def norm(s):
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", SUFFIX.sub(" ", s)).strip()

def main():
    meta = get(f"https://api-production.data.gov.sg/v2/public/api/collections/2/metadata")
    ids = meta["data"]["collectionMetadata"]["childDatasets"]
    postings = json.loads((RUN / "data/postings.json").read_text(encoding="utf-8"))
    out, t_all = [], time.time()
    for p in postings:
        q = norm(p["employer"])
        t0 = time.time()
        def one(rid):
            u = f"{BASE}/api/action/datastore_search?resource_id={rid}&limit=15&q=" + urllib.parse.quote(q)
            d = get(u)
            return d["result"]["records"] if d and d.get("success") else None
        with ThreadPoolExecutor(3) as ex:
            res = list(ex.map(one, ids))
        failed = sum(r is None for r in res)
        cands = {}
        for recs in res:
            for r in recs or []:
                cands[r["uen"]] = r
        scored = []
        for r in cands.values():
            names = [r["entity_name"]] + [r.get(f"former_entity_name{i}") for i in range(1, 4)]
            s = max(SequenceMatcher(None, q, norm(n)).ratio() for n in names if n)
            scored.append((round(s, 3), r))
        scored.sort(key=lambda x: -x[0])
        top = scored[:5]
        live_top = [x for x in scored if x[1]["entity_status_description"].lower() in ("live", "live company")]
        if not top: state = "unresolved"
        elif top[0][0] >= 0.97 and (len(top) == 1 or top[1][0] < 0.9): state = "exact_match"
        elif top[0][0] >= 0.85 and (len(top) == 1 or top[0][0] - top[1][0] >= 0.1): state = "likely_match"
        else: state = "ambiguous"
        out.append({"id": p["id"], "employer": p["employer"], "query": q, "state": state, "datasets_failed": failed,
                    "seconds": round(time.time() - t0, 1), "candidates_total": len(scored),
                    "top": [{"score": s, "uen": r["uen"], "name": r["entity_name"], "type": r["entity_type_description"],
                             "status": r["entity_status_description"], "incorporated": r["registration_incorporation_date"],
                             "ssic": r["primary_ssic_description"]} for s, r in top]})
        print(p["id"], state, f'{out[-1]["seconds"]}s', top[0][1]["entity_name"] if top else "-", flush=True)
    (RUN / "outputs/e1_acra_resolution.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    print("total s", round(time.time() - t_all))

main()
