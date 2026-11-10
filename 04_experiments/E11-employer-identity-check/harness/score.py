"""Score runs against data/ground_truth.json. Usage: python harness/score.py run1 [run2]. Writes runs/.../score_<run>.json and prints a table."""
import json, sys, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "runs/2026-11-10-run-001/outputs"
gold = {x["id"]: x for x in json.load(open(ROOT / "data/ground_truth.json", encoding="utf-8"))["items"]}
ACCEPT = {"exists_and_consistent", "exists_limited_evidence", "web_evidence_only"}   # names a registered entity as the employer
BRAND = {"brand_legal_entity_unconfirmed"}                                            # says it is a real company but names no registered entity

def load(run):
    res = {}
    for i in gold:
        p = OUT / run / (i + ".json")
        if p.exists():
            res[i] = json.load(open(p, encoding="utf-8"))
    return res

def classify(g, r):
    h = r["headline"]; ent = ((r.get("registry") or {}).get("entity") or {})
    uen = ent.get("uen"); t = g["truth_type"]
    named = h in ACCEPT or h in BRAND
    if t == "entity":
        if h in ACCEPT and uen == g["truth_uen"]: return "correct"
        if h in ACCEPT: return "wrong_accepted"
        if h in BRAND: return "brand_unresolved"
        return "wrong_refusal"
    if t == "unknown":
        return "unknown_accepted" if named else "unknown_refused"
    if t == "not_disclosed":
        return "named_company" if named else "no_company_named"
    if t == "not_real":
        return "lookalike_confirmed_real" if named else "lookalike_caught"

def main():
    runs = sys.argv[1:]
    allr = {}
    for run in runs:
        res = load(run); allr[run] = res
        cls = {i: classify(gold[i], r) for i, r in res.items()}
        by = collections.Counter(cls.values())
        bystratum = collections.defaultdict(collections.Counter)
        for i, c in cls.items(): bystratum[gold[i]["stratum"]][c] += 1
        secs = [r["seconds"] for r in res.values()]
        out = {"run": run, "n": len(res), "classes": by, "by_stratum": {k: dict(v) for k, v in bystratum.items()},
               "seconds_total_sum": round(sum(secs), 1), "seconds_mean": round(sum(secs) / max(1, len(secs)), 1),
               "rows": {i: {"stratum": gold[i]["stratum"], "employer": gold[i]["employer"], "truth": gold[i]["truth_type"], "truth_uen": gold[i]["truth_uen"],
                            "headline": res[i]["headline"], "got_uen": ((res[i].get("registry") or {}).get("entity") or {}).get("uen"),
                            "class": cls[i], "degraded": res[i].get("degraded"), "seconds": res[i]["seconds"]} for i in res}}
        json.dump(out, open(OUT / ("score_%s.json" % run), "w"), indent=1, default=dict)
        print("==", run, "n=%d" % len(res), dict(by)); [print("  ", k, dict(v)) for k, v in bystratum.items()]
        for i, row in out["rows"].items():
            if row["class"] not in ("correct", "lookalike_caught", "no_company_named", "unknown_refused"):
                print("   !", i, row["employer"][:40], "|", row["headline"], row["got_uen"], "->", row["class"])
    if len(runs) == 2:
        a, b = allr[runs[0]], allr[runs[1]]
        common = [i for i in a if i in b]
        same = [i for i in common if a[i]["headline"] == b[i]["headline"] and ((a[i].get("registry") or {}).get("entity") or {}).get("uen") == ((b[i].get("registry") or {}).get("entity") or {}).get("uen")]
        print("stability: %d/%d same headline+UEN" % (len(same), len(common)), [i for i in common if i not in same])

main()
