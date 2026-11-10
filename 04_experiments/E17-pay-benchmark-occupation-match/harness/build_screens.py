"""Build the Part B and Part C screens for the persona pilot / a future participant session. No model call.
Writes runs/.../outputs/personas/screens_for_pilot.md."""
import csv, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent)); sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import persona_pilot as pp
E = pp.E
rd = pp.rundir
posts = {p["id"]: p for p in json.loads((E / "data/postings.json").read_text(encoding="utf-8"))}
gold = {g["id"]: g for g in json.loads((E / "data/gold.json").read_text(encoding="utf-8"))}
sl = json.loads((rd / "outputs/shortlists.json").read_text(encoding="utf-8"))
titles = {c["code"]: c["title"] for v in sl.values() for c in v}
m1 = {r["id"]: r for r in json.loads((rd / "outputs/matcher__qwen-qwen3-8-27b__run1__partial.json").read_text(encoding="utf-8"))["results"]}
x3 = {f"X3-{p['id']:02d}": p for p in json.loads((E.parent / "E10-market-value-and-red-flag-experiments/outputs/x3/postings_ids.json").read_text(encoding="utf-8"))}
mom = {r["ssoc2024"]: r for r in csv.DictReader(open(E.parent / "E10-market-value-and-red-flag-experiments/data/mom/occupations_all_industries.csv", encoding="utf-8"))}
L = ["# Prepared screens (SIMULATED pilot instrument; no participants)", "", "## Part B: confirm the occupation", ""]
for pid in pp.B_IDS:
    p = posts[pid]
    L.append(f"- **{pid}** {p['title']} | {p['seniority']} | {p['employment_type']} | {p['function']}")
    L.append(f"  - matcher top three (qwen run 1): " + "; ".join(titles[c] for c in m1[pid]["top3"]) + f"; verdict: {m1[pid]['verdict']}")
    acc = [titles.get(c, c) for c in gold[pid]["accept"]]
    L.append(f"  - gold (accepted): {', '.join(acc)}")
L += ["", "## Part C: read the range and its basis", "", pp.BASIS, ""]
for pid, kind in pp.C_SCREENS:
    g = gold[pid]; m = mom[g["primary"]]; p = x3[pid]
    L.append(f"- **{pid}** {p['title']} ({p['seniority']}), occupation {m['occupation']}. Advertised ${p['salary_min']:,}-${p['salary_max']:,}. Official gross monthly P25 ${int(m['gross_p25']):,}, median ${int(m['gross_median']):,}, P75 ${int(m['gross_p75']):,}. Position: {kind}.")
out = rd / "outputs/personas/screens_for_pilot.md"
out.write_text("\n".join(L), encoding="utf-8")
print(out)
