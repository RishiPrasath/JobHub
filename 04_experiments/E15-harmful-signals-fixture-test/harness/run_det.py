"""Method 1 runner: deterministic phrase matching (no model). Writes outputs/results_deterministic.json."""
import json, time
from pathlib import Path
import matcher
EXP = Path(__file__).resolve().parent.parent
OUT = EXP / "runs" / "2026-11-10-run-001" / "outputs"
pack = matcher.load_pack(EXP / "data" / "pack.json")
cases = json.loads((EXP / "data" / "cases.json").read_text(encoding="utf-8"))["cases"]
res = matcher.run(pack, cases)
for r in res:
    for f in r["flags"]:
        f["valid_entry"] = True; f["excerpt_verbatim"] = True
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "results_deterministic.json").write_text(json.dumps({"label": "deterministic", "model": None, "run": 1,
    "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "results": res}, ensure_ascii=False, indent=1), encoding="utf-8")
for r in res:
    print(r["case_id"], [(f["entry_id"], f["excerpt"]) for f in r["flags"]])
