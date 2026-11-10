"""Rebuild outputs/results/*.json from the raw cache files (so partial runs can be scored). Raw files are only read."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import OUTPUTS
groups = {}
for p in sorted((OUTPUTS / "raw").glob("*.json")):
    r = json.loads(p.read_text(encoding="utf-8"))
    m = re.match(r"(M\d)-(P\d+-[AB])-r(\d+)", r["tag"])
    if not m: continue
    meth, sid, run = m.group(1), m.group(2), int(m.group(3))
    groups.setdefault((r["model"], meth, run), {})[sid] = {"content": r["content"], "usage": r["usage"], "latency_s": r["latency_s"],
        "finish_reason": r.get("finish_reason"), "created_utc": r.get("created_utc")}
rd = OUTPUTS / "results"; rd.mkdir(exist_ok=True)
for old in rd.glob("*.json"): old.unlink()
for (model, meth, run), sets in groups.items():
    out = {"meta": {"model": model, "method": meth, "run": run, "prompt_version": "e19-prompts-v1", "sets_completed": len(sets),
                    "params": {"temperature": 0.2, "reasoning_effort": "low (gpt-oss only)", "max_tokens": 1000 if meth != "M3" else 900, "json_mode": True}},
           "method": meth, "sets": sets}
    (rd / (model.replace("/", "-") + f"__{meth}__run{run}.json")).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(model, meth, run, len(sets))
