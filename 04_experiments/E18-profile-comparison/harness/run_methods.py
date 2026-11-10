"""Runs the systems under test. Rerunnable: every call is cached under runs/2026-11-10-run-001/outputs/raw.

Usage (from repo root): python -I 04_experiments/E18-profile-comparison/harness/run_methods.py <stage> [run]
stages: free (single + batch), extract (single + batch), evid (hybrid evidence proposals), free_subset
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

stage = sys.argv[1]
run = int(sys.argv[2]) if len(sys.argv) > 2 else 1
subset = sys.argv[3].split(",") if len(sys.argv) > 3 else None  # optional list of profile ids
t0 = time.time()
n = 0


def safe(fn, *a, label=""):
    """API 400s (for example json_validate_failed) are recorded as failed comparisons, not crashes."""
    try:
        return fn(*a)
    except Exception as e:  # noqa: BLE001
        if "DAILY LIMIT" in str(e):
            raise
        print(f"FAILED {label}: {str(e)[:160]}", flush=True)
        import json as _j
        from pathlib import Path as _P
        d = C.RUN_DIR / "outputs" / "raw" / "_failures"
        d.mkdir(parents=True, exist_ok=True)
        (d / (label.replace(" ", "_") + ".txt")).write_text(str(e), encoding="utf-8")
        return None


def tick(msg):
    global n
    n += 1
    print(f"[{time.time()-t0:6.0f}s] {n:3d} {msg}", flush=True)


if stage == "free":
    profs = subset or [p["id"] for p in C.PROFILES]
    for prof in profs:
        for p in C.POSTINGS:
            r_ = safe(C.free_results, prof, [p["id"]], run, label=f"free {prof} {p['id']} run{run}")
            if r_ is None:
                continue
            res, rec = r_
            tick(f"free run{run} {prof} {p['id']} tokens={rec['usage'].get('total_tokens')} cached={rec['cached']} ok={res[p['id']] is not None}")
        if run == 1:
            r_ = safe(C.free_results, prof, C.BATCH_IDS, run, label=f"free BATCH {prof} run{run}")
            if r_ is None:
                continue
            res, rec = r_
            tick(f"free BATCH run{run} {prof} tokens={rec['usage'].get('total_tokens')} cached={rec['cached']} ok={[k for k,v in res.items() if v]}")
elif stage == "extract":
    for p in C.POSTINGS:
        r_ = safe(C.extraction, [p["id"]], run, label=f"extract {p['id']} run{run}")
        if r_ is None:
            continue
        res, rec = r_
        tick(f"extract run{run} {p['id']} tokens={rec['usage'].get('total_tokens')} cached={rec['cached']} ok={res[p['id']] is not None}")
    if run == 1:
        r_ = safe(C.extraction, C.BATCH_IDS, run, label="extract BATCH")
        if r_ is not None:
            res, rec = r_
            tick(f"extract BATCH tokens={rec['usage'].get('total_tokens')} cached={rec['cached']} ok={[k for k,v in res.items() if v]}")
elif stage == "evid":
    ex1 = {p["id"]: ((safe(C.extraction, [p["id"]], 1, label="x") or ({p["id"]: None},))[0])[p["id"]] for p in C.POSTINGS}
    exb = (safe(C.extraction, C.BATCH_IDS, 1, label="xb") or ({k: None for k in C.BATCH_IDS},))[0]
    for prof in [q for q in C.PROFILES if (subset is None or q["id"] in subset)]:
        for p in C.POSTINGS:
            r_ = safe(C.hybrid_results, [p["id"]], prof["id"], ex1, 1, label=f"evid {prof['id']} {p['id']}")
            if r_ is None:
                continue
            out, rec = r_
            tick(f"evid {prof['id']} {p['id']} tokens={rec and rec['usage'].get('total_tokens')} cached={rec and rec['cached']}")
        r_ = safe(C.hybrid_results, C.BATCH_IDS, prof["id"], exb, 1, label=f"evid BATCH {prof['id']}")
        if r_ is None:
            continue
        out, rec = r_
        tick(f"evid BATCH {prof['id']} tokens={rec and rec['usage'].get('total_tokens')} cached={rec and rec['cached']}")
elif stage == "evid_single":
    # added after the gpt-oss-20b daily limit stopped the batch extraction: single-posting evidence proposals only
    ex1 = {p["id"]: C.extraction([p["id"]], 1)[0][p["id"]] for p in C.POSTINGS}
    for prof in C.PROFILES:
        for p in C.POSTINGS:
            r_ = safe(C.hybrid_results, [p["id"]], prof["id"], ex1, 1, label=f"evid {prof['id']} {p['id']}")
            if r_ is None:
                continue
            out, rec = r_
            tick(f"evid {prof['id']} {p['id']} tokens={rec and rec['usage'].get('total_tokens')} cached={rec and rec['cached']}")
else:
    raise SystemExit("unknown stage")
