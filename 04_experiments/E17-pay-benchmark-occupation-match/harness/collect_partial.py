"""Rebuild matcher result files from the raw cache for runs that were stopped early (no model call is made).
Usage: python collect_partial.py MODEL RUN  -> outputs/matcher__<slug>__run<N>__partial.json"""
import json, re, sys
from pathlib import Path
E = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(E.parents[1] / "tools"))
from llm_client import parse_json
rd = E / "runs/2026-11-10-run-001"
model, run = sys.argv[1], int(sys.argv[2])
sl = json.loads((rd / "outputs/shortlists.json").read_text(encoding="utf-8"))
mk = re.sub(r"[^A-Za-z0-9]", "", model)[:14]
res = []
for f in sorted((rd / "outputs/raw").glob(f"*-r{run}__{mk}__*.json")):
    rec = json.loads(f.read_text(encoding="utf-8"))
    pid = rec["tag"].rsplit("-r", 1)[0]
    d = parse_json(rec["content"]) or {}
    valid = {c["code"] for c in sl[pid]}
    res.append({"id": pid, "top3": [str(c) for c in (d.get("top3") or []) if str(c) in valid][:3], "verdict": d.get("verdict"),
                "confidence": d.get("confidence"), "why": d.get("why"), "parse_ok": bool(d),
                "tokens": (rec.get("usage") or {}).get("total_tokens")})
slug = re.sub(r"[^A-Za-z0-9]+", "-", model).strip("-")
(rd / f"outputs/matcher__{slug}__run{run}__partial.json").write_text(json.dumps({"model": model, "run": run, "n": len(res), "partial": True, "results": res}, indent=1), encoding="utf-8")
print(model, run, len(res))
