"""POST HOC run-002: run the unchanged snapshot step (v0.1.0) on the held-out set and score it. Usage: python harness/run_heldout.py"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
EXP = HERE.parent
sys.path.insert(0, str(HERE))
import snapshot as S

out = EXP / "runs/2026-11-10-run-002/outputs"
gold = {g["id"]: g for g in json.loads((EXP / "data/heldout/gold_labels.json").read_text(encoding="utf-8"))["items"]}
FIELDS = ["title", "employer", "pay", "duties", "closing"]
an = {}
for i, g in gold.items():
    raw = (EXP / "data/heldout/pastes" / f"{i}.txt").read_bytes().decode("utf-8")
    an[i] = S.analyse(raw, S.parse_dt(g["captured_at"]))
(out / "analysis_deterministic.json").write_text(json.dumps({"version": S.VERSION, "items": an}, indent=1, ensure_ascii=False), encoding="utf-8")

def score(name, an):
    c = [i for i, g in gold.items() if g["set"] == "heldout10"]
    p = [i for i, g in gold.items() if g["set"] == "heldout_partial3"]
    L = [f"## {name}", ""]
    tot = 0
    for f in FIELDS:
        ok = sum(an[i]["fields"][f] == gold[i]["fields"][f] for i in c)
        tot += ok
        L.append(f"- {f}: {ok}/{len(c)}")
    L.append(f"- all five fields right on {sum(all(an[i]['fields'][f]==gold[i]['fields'][f] for f in FIELDS) for i in c)}/{len(c)} pastes")
    L.append(f"- partial pastes flagged: {sum(an[i]['partial_flag'] for i in p)}/{len(p)}  ({[ (i, an[i]['partial_reasons']) for i in p]})")
    L.append(f"- false flags on the 10 full pastes: {sum(an[i]['partial_flag'] for i in c)}/{len(c)}  ({[(i, an[i]['partial_reasons']) for i in c if an[i]['partial_flag']]})")
    L.append("- field errors:")
    for i in c:
        for f in FIELDS:
            if an[i]["fields"][f] != gold[i]["fields"][f]:
                L.append(f"  - {i} {f}: gold {gold[i]['fields'][f]}, got {an[i]['fields'][f]}, value {(an[i].get('values') or {}).get(f)!r}")
    ce = [(i, an[i]["closing_date_iso"], gold[i]["closing_date_iso"]) for i in c if (an[i]["closing_date_iso"] or None) != gold[i]["closing_date_iso"]]
    L.append(f"- closing date value errors (id, got, gold): {ce}")
    return L

L = ["# Run-002 (POST HOC) held-out robustness check", "", f"Snapshot step: {S.VERSION}, unchanged from run-001.", ""] + score("deterministic snapshot step", an)
llm_p = out / "llm_analysis.json"
if llm_p.exists():
    llm = json.loads(llm_p.read_text(encoding="utf-8"))
    L += [""] + score(f"LLM check ({llm['model']})", llm["items"])
(out / "results.md").write_text("\n".join(L), encoding="utf-8")
print("\n".join(L))
