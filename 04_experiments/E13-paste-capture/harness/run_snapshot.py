"""Run the snapshot step on the 40 frozen pastes and the stale/integrity tests. Writes raw outputs only.

Usage: python harness/run_snapshot.py [run_dir]
Default run_dir: runs/2026-11-10-run-001
"""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
sys.path.insert(0, str(HERE))
import snapshot as S  # noqa: E402

run_dir = EXP / (sys.argv[1] if len(sys.argv) > 1 else "runs/2026-11-10-run-001")
out = run_dir / "outputs"
out.mkdir(parents=True, exist_ok=True)

gold = json.loads((EXP / "data/gold_labels.json").read_text(encoding="utf-8"))["items"]
store = S.SnapshotStore(out / "snapshots")

analysis, integrity = {}, []
for g in gold:
    pid = g["id"]
    raw = (EXP / "data/pastes" / f"{pid}.txt").read_bytes()
    cap = S.parse_dt(g["captured_at"])
    rec = store.capture(pid, raw, cap)
    analysis[pid] = rec["analysis"]
    # integrity: reload from disk, compare with the original bytes
    again = store.load(pid)
    same_store = again["original_text"].encode("utf-8") == raw and again["original_sha256"] == hashlib.sha256(raw).hexdigest()
    # a correction, then restore the original
    store.correct(pid, again["original_text"] + "\nCORRECTION: employer name added by the user", cap)
    changed = store.current_text(pid) != again["original_text"]
    restored = store.restore_original(pid).encode("utf-8") == raw
    integrity.append({"id": pid, "stored_equals_original": same_store, "correction_applied": changed, "restore_equals_original": restored,
                      "bytes": len(raw), "has_crlf": b"\r\n" in raw, "has_nbsp": " ".encode() in raw, "has_zero_width": "​".encode() in raw})
(out / "analysis.json").write_text(json.dumps({"version": S.VERSION, "items": analysis}, indent=1, ensure_ascii=False), encoding="utf-8")
(out / "integrity.json").write_text(json.dumps(integrity, indent=1), encoding="utf-8")

# stale rule table
cases = json.loads((EXP / "data/stale_rule_cases.json").read_text(encoding="utf-8"))["cases"]
res = []
for c in cases:
    cd = date.fromisoformat(c["closing_date"]) if c["closing_date"] else None
    r = S.stale_check(S.parse_dt(c["captured_at"]), cd, S.parse_dt(c["now"]))
    res.append({"id": c["id"], "expected": c["expected_notice"], "got": r["notice"], "expected_reasons": c["expected_reasons"],
                "got_reasons": r["reasons"], "ok": r["notice"] == c["expected_notice"] and sorted(r["reasons"]) == sorted(c["expected_reasons"]),
                "message_has_repaste_prompt": (r["message"] is None) or ("Paste the posting again" in r["message"])})
(out / "stale_rule_results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")

# end to end: closing date extracted by the snapshot step, compared with gold
NOWS = ["2026-11-10T12:00:00+08:00", "2026-11-16T12:00:00+08:00", "2026-11-19T12:00:00+08:00", "2026-12-10T12:00:00+08:00"]
e2e = []
for g in gold:
    if g["set"] != "complete30":
        continue
    cap = S.parse_dt(g["captured_at"])
    gcd = date.fromisoformat(g["closing_date_iso"]) if g["closing_date_iso"] else None
    ecd_s = analysis[g["id"]]["closing_date_iso"]
    ecd = date.fromisoformat(ecd_s) if ecd_s else None
    for n in NOWS:
        now = S.parse_dt(n)
        exp = S.stale_check(cap, gcd, now)
        got = S.stale_check(cap, ecd, now)
        e2e.append({"id": g["id"], "board": g["board"], "now": n, "gold_closing": g["closing_date_iso"], "extracted_closing": ecd_s,
                    "expected": exp["notice"], "got": got["notice"], "expected_reasons": exp["reasons"], "got_reasons": got["reasons"],
                    "ok": exp["notice"] == got["notice"] and exp["reasons"] == got["reasons"]})
(out / "stale_e2e_results.json").write_text(json.dumps(e2e, indent=1), encoding="utf-8")
print("done", S.VERSION, len(analysis), "snapshots,", len(res), "rule cases,", len(e2e), "e2e cases")
