"""Build pilot_results.json from the cached persona answers (gpt-oss-20b only). The pilot stopped at the daily token limit."""
import glob, json, re, sys
from pathlib import Path
EXP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXP.parents[1] / "tools"))
from llm_client import parse_json
out = EXP / "runs/2026-11-10-run-001/outputs/personas"
P = json.loads((out / "personas.json").read_text(encoding="utf-8"))["personas"]
rows = []
for p in P:
    row = {"persona_id": p["persona_id"], "label": p["label"], "digital_comfort": p.get("digital_comfort"), "simulated": True, "task_a": None, "task_b": None}
    for t, key in (("A", "task_a"), ("B", "task_b")):
        fs = glob.glob(str(out / ("raw/" + re.sub(r"[^A-Za-z0-9_.-]", "_", f"{t}-{p['persona_id']}") + "__openaigptoss20__*.json")))
        if fs:
            r = json.loads(Path(fs[0]).read_text(encoding="utf-8"))
            row[key] = parse_json(r["content"])
    rows.append(row)
(out / "pilot_results.json").write_text(json.dumps({"SIMULATED": True, "agent_model": "openai/gpt-oss-20b", "complete_personas": sum(1 for r in rows if r["task_a"] and r["task_b"]),
    "note": "Language-model simulations, not participants. Stopped at the gpt-oss-20b daily token limit; personas without answers were not run.", "rows": rows}, indent=1, ensure_ascii=False), encoding="utf-8")
for r in rows:
    print(r["persona_id"], bool(r["task_a"]), bool(r["task_b"]))
