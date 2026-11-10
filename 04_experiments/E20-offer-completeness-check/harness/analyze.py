"""Extra tables for FINDINGS.md (post-scoring, descriptive only): common-letter comparison across runs, failure listing, token use.
python harness/analyze.py  -> prints markdown; also writes outputs/analysis.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "harness"))
import score as S  # noqa: E402

OUT = ROOT / "runs" / "2026-11-10-run-001" / "outputs"
runs = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted((OUT / "parsed").glob("*.json"))}
common = sorted(set.intersection(*[set(k for k, v in r["results"].items() if isinstance(v.get("parsed"), dict)) for r in runs.values()]))
lines = [f"Letters scored by every run (common set): {', '.join(common)}", "",
         "| run | letters | recall (planted found/planted) | false alarms | strict sourcing | controls flagged |", "|---|---|---|---|---|---|"]
for n, r in runs.items():
    rr = dict(r, results={k: v for k, v in r["results"].items() if k in common})
    s = S.score_run(rr)
    c = s["counts"]
    lines.append(f"| {n} | {len(common)} | {s['found_planted']}/{s['gold_planted']} | {s['false_alarms_total']} | {c['flags_correct']}/{c['flags']} | {s['controls_flagged']} |")
lines += ["", "POST HOC sensitivity (not a verdict; gold labels unchanged). False alarms after removing (a) flags on an item that is part of a planted inconsistency in the same letter and (b) all C14 (leave) flags, where the letters list leave types incompletely in some profiles:", "", "| run | letters | false alarms as scored | after removing (a) | after removing (a) and (b) |", "|---|---|---|---|---|"]
for n, r in runs.items():
    rr = dict(r, results={k: v for k, v in r["results"].items() if isinstance(v.get("parsed"), dict)})
    s = S.score_run(rr)
    fa = s["false_alarms_total"]; a = b = 0
    for lid, L in s["per_letter"].items():
        incitems = {i for g in S.GOLD[lid]["inconsistencies"] for i in g["items"]}
        for it in L["false_alarm_items"]:
            if it in incitems:
                a += 1
            elif it == "C14":
                b += 1
    lines.append(f"| {n} | {len(s['letters_scored'])} | {fa} | {fa - a} | {fa - a - b} |")
lines += ["", "Token use (new calls only, from run logs):"]
tot = 0
for n, r in runs.items():
    u = r.get("usage_new_tokens", {})
    lines.append(f"- {n}: {u}")
    tot += u.get("total", 0)
lines.append(f"- total of the three scored runs: {tot}")
text = "\n".join(lines)
(OUT / "analysis.md").write_text(text + "\n", encoding="utf-8")
print(text)
