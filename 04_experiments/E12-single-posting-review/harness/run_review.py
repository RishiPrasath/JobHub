"""Run the unchanged E08 guarded review prompt (v2) once per posting per (model, run).

Usage: python harness/run_review.py gpt120 1        # model key, run number
       python harness/run_review.py gpt120 1 E12-P04 E12-P05   # subset
Rerunnable: llm_client caches every call under runs/<run>/outputs/raw, so a rerun spends no tokens.
Raw outputs are never edited after the run.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402
from llm_client import chat  # noqa: E402


def main() -> None:
    mkey, run = sys.argv[1], int(sys.argv[2])
    only = set(sys.argv[3:])
    model = c.MODELS[mkey]
    posts = c.load_postings()
    sysmsg = c.system_prompt()
    ledger = c.RUN_DIR / "outputs" / "usage.jsonl"
    marker = c.RUN_DIR / "outputs" / f"DAILY_LIMIT_{mkey}.txt"
    if marker.exists():
        print(f"{mkey}: daily limit recorded earlier ({marker.name}); not calling.")
        return
    ledger.parent.mkdir(parents=True, exist_ok=True)
    for pid, p in posts.items():
        if only and pid not in only:
            continue
        tag = f"{pid}__{mkey}__r{run}"
        t0 = time.time()
        try:
            r = chat(model, [{"role": "system", "content": sysmsg}, {"role": "user", "content": c.user_message(p)}],
                     json_mode=False, max_tokens=c.MAX_TOKENS, temperature=c.TEMPERATURE,
                     reasoning_effort=c.REASONING, cache_dir=str(c.RAW_DIR), tag=tag, run=run)
        except RuntimeError as e:
            print("STOP:", str(e)[:200])
            if "DAILY LIMIT" in str(e):
                (c.RUN_DIR / "outputs" / "DAILY_LIMIT.txt").write_text(f"{tag}: {str(e)[:300]}\n", encoding="utf-8")
            raise
        u = r.get("usage", {})
        rec = {"tag": tag, "model": model, "cached": r.get("cached"), "latency_s": r.get("latency_s"),
               "finish": r.get("finish_reason"), "prompt_tokens": u.get("prompt_tokens"),
               "completion_tokens": u.get("completion_tokens"), "total_tokens": u.get("total_tokens"),
               "created_utc": r.get("created_utc")}
        if not r.get("cached"):
            with ledger.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec) + "\n")
        print(tag, rec["total_tokens"], rec["finish"], round(time.time() - t0, 1), "s", "cached" if r.get("cached") else "")


if __name__ == "__main__":
    main()
