"""Smoke test of model formats on a toy ledger (not one of the 20 sets). Records outputs in outputs/smoke."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from common import OUTPUTS
from llm_client import chat
import run_suggestions as rs
ledger = "[T-W1] WORK: Cleaner at Sparkle Services (part-time, 2020 to 2022). Role: Cleaned offices at night. Achievements: Cleaned 10 offices a week. Skills used: floor care.\n[T-SK1] SKILL: Forklift, level basic."
posting = "Office Cleaner at ToyCo.\nRequirements:\n[R1] Office cleaning experience.\n[R2] Valid HazMat certificate.\n[R3] Night shifts."
for model in sys.argv[1:]:
    rs.set_model["m"] = model
    user = rs.M2_USER.format(ledger=ledger, posting=posting) + ("\n/no_think" if "qwen" in model else "")
    r = chat(model, [{"role": "system", "content": rs.SYSTEM}, {"role": "user", "content": user}], json_mode=True, max_tokens=1400,
             reasoning_effort="low", cache_dir=str(OUTPUTS / "smoke"), tag="toy-M2")
    print(model, r["usage"], r["finish_reason"], r["latency_s"]); print(r["content"][:700]); print("-----")
