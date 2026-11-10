"""Runs the completeness check on all 20 letters with one model and one run number.

python harness/run_check.py --model openai/gpt-oss-20b --run 1
Raw responses are cached (and never edited) under runs/2026-11-10-run-001/outputs/raw. Parsed results go to
outputs/parsed/<model>__run<N>.json.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(ROOT / "harness"))
from llm_client import chat, parse_json  # noqa: E402
import prompt as P  # noqa: E402

RUN = ROOT / "runs" / "2026-11-10-run-001" / "outputs"


def strip_think(t: str) -> str:
    return re.sub(r"<think>.*?</think>", "", t or "", flags=re.S).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--run", type=int, default=1)
    ap.add_argument("--max-tokens", type=int, default=2200)
    ap.add_argument("--only", default=None, help="comma-separated letter ids")
    a = ap.parse_args()
    meta = json.loads((ROOT / "data" / "letters.json").read_text(encoding="utf-8"))
    ids = [m["id"] for m in meta]
    if a.only:
        ids = [i for i in ids if i in a.only.split(",")]
    sysmsg = P.system_prompt()
    out = {"model": a.model, "run": a.run, "harness": P.HARNESS_VERSION, "results": {}}
    usage = {"prompt": 0, "completion": 0, "total": 0}
    for lid in ids:
        text = (ROOT / "data" / "letters" / f"{lid}.txt").read_text(encoding="utf-8")
        msgs = [{"role": "system", "content": sysmsg}, {"role": "user", "content": P.user_prompt(text)}]
        try:
            r = None
            for _try in range(40):  # the shared limiter's lock file can raise a transient PermissionError on Windows
                try:
                    r = chat(a.model, msgs, json_mode=True, max_tokens=a.max_tokens, temperature=0.2,
                             reasoning_effort="low", cache_dir=str(RUN / "raw"), tag=f"{lid}-run{a.run}", run=a.run)
                    break
                except (PermissionError, FileNotFoundError, TimeoutError):
                    time.sleep(2)
                except Exception as e:  # noqa: BLE001  (e.g. API 400 json_validate_failed with an empty generation)
                    if "DAILY LIMIT" in str(e):
                        raise
                    api_errors = locals().get("api_errors", 0) + 1
                    print(lid, "API error, attempt", api_errors, str(e)[:160], flush=True)
                    if api_errors >= 3:
                        break
                    time.sleep(5)
                except Exception as ex:  # e.g. 400 json_validate_failed with empty generation; retry twice then record
                    if 'DAILY LIMIT' in str(ex) or _try >= 2:
                        raise RuntimeError('API error: ' + str(ex)[:250])
                    time.sleep(3)
            if r is None:
                raise RuntimeError("no response after retries (limiter lock or API error)")
        except RuntimeError as e:
            print("STOP:", str(e)[:200])
            out["results"][lid] = {"error": str(e)[:300]}
            if "DAILY LIMIT" in str(e):
                break
            continue
        content = strip_think(r["content"])
        parsed = parse_json(content)
        u = r.get("usage", {})
        for k, kk in (("prompt", "prompt_tokens"), ("completion", "completion_tokens"), ("total", "total_tokens")):
            if not r.get("cached"):
                usage[k] += u.get(kk, 0)
        out["results"][lid] = {"parsed": parsed, "raw_content": content, "finish_reason": r.get("finish_reason"),
                               "usage": u, "cached": r.get("cached", False), "created_utc": r.get("created_utc")}
        print(lid, "ok" if parsed else "PARSE-FAIL", r.get("finish_reason"), u.get("total_tokens"), flush=True)
    out["usage_new_tokens"] = usage
    d = RUN / "parsed"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{re.sub(r'[^A-Za-z0-9]', '_', a.model)}__run{a.run}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print("tokens", usage)


if __name__ == "__main__":
    main()
