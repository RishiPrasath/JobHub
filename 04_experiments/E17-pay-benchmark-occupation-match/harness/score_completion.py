"""E17 completion-run scoring (2026-11-11). Reuses the frozen scoring functions in score.py unchanged (run as written up to the
point where it builds its run table), then scores the added runs: gpt-oss-20b run 1 (all 100), allam-2-7b runs 1 and 2, and stability.
Usage: python harness/score_completion.py   Writes outputs/score_completion.json"""
import json
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
src = (H / "score.py").read_text(encoding="utf-8").split("runs = {")[0]
sys.argv = [sys.argv[0]]
ns = {"__file__": str(H / "score.py")}
exec(compile(src, "score.py", "exec"), ns)
load, score, ALL, rundir, pct = ns["load"], ns["score"], ns["ALL"], ns["rundir"], ns["pct"]

runs = {"qwen_r1": load("qwen/qwen3.8-27b", 1), "qwen_r2": load("qwen/qwen3.8-27b", 2),
        "gptoss20b_r1": load("openai/gpt-oss-20b", 1), "gptoss20b_r2": load("openai/gpt-oss-20b", 2),
        "gptoss120b_r1": load("openai/gpt-oss-120b", 1),
        "allam_r1": load("allam-2-7b", 1), "allam_r2": load("allam-2-7b", 2)}
R = {"coverage": {k: len(v) for k, v in runs.items()}}
KEEP = ["n_scored", "top3_hit_overall", "top3_recall_gold_code_postings", "top1_gold_code_postings", "no_match_flagged_none",
        "confident_wrong_match_medium_or_high", "no_match_handled_correctly", "false_none_on_gold_code_postings", "seniority_errors_top1"]
for k, v in runs.items():
    if v:
        s = score(v)
        R[k] = {x: s[x] for x in KEEP}


def stab(a, b):
    ids = [i for i in ALL if i in a and i in b]
    if not ids:
        return None
    ss = sum(set(a[i]["top3"]) == set(b[i]["top3"]) for i in ids)
    sv = sum(a[i]["verdict"] == b[i]["verdict"] for i in ids)
    return {"n_overlap": len(ids), "same_top3_set": [ss, pct(ss, len(ids))], "same_verdict": [sv, pct(sv, len(ids))]}


for x, y in (("qwen_r1", "qwen_r2"), ("gptoss20b_r1", "gptoss20b_r2"), ("allam_r1", "allam_r2"),
             ("qwen_r1", "gptoss20b_r1"), ("qwen_r1", "allam_r1"), ("gptoss20b_r1", "allam_r1")):
    s = stab(runs[x], runs[y])
    if s:
        R[f"agreement_{x}_vs_{y}"] = s
(rundir / "outputs/score_completion.json").write_text(json.dumps(R, ensure_ascii=False, indent=1, default=list), encoding="utf-8")
print(json.dumps(R, ensure_ascii=False, indent=1, default=list)[:6000])
