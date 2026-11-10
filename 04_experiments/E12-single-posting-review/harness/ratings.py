"""Turn the rater's compact ratings (scoring/question-ratings.txt) into scoring/question-ratings.json.

Rater: Claude (an AI). Rubric: protocol/question-rubric.md (written before rating).
Line format (one per question; '#' starts a comment):
    <tag>|Q<n> <gap|-> <tone T/F> <route T/F/-> [U]
  gap   = the gold gap ID the question targets, or '-' if it targets no gold gap
  tone  = check 3 (neutral tone)
  route = check 4: T if the question names the official route, F if a route exists and is not named, '-' if no route applies
  U     = optional: not a gold gap but the rater judges it plainly decision-critical (sensitivity only)
From the gap ID the script derives: check 1 (gap is critical), check 2 (gap has no public lookup), and whether check 4 applies
(gap has a route). The rater supplies only the gap, tone and route judgements, so the gold file decides the rest.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

SC = c.RUN_DIR / "scoring"
gold = c.load_gold()
questions = {q["qid"]: q for q in json.loads((SC / "questions.json").read_text(encoding="utf-8"))}
out, errs = {}, []
src = SC / "question-ratings.txt"
for ln, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
    line = line.split("#", 1)[0].strip()
    if not line:
        continue
    qid, rest = line.split(" ", 1)
    parts = rest.split()
    if qid not in questions:
        errs.append(f"line {ln}: unknown qid {qid}")
        continue
    gap, tone, route = parts[0], parts[1], parts[2]
    unl = "U" in parts[3:]
    pid = questions[qid]["pid"]
    gd = {g["id"]: g for g in gold[pid]["gaps"]}
    if gap != "-" and gap not in gd:
        errs.append(f"line {ln}: gap {gap} not in gold for {pid}")
        continue
    g = gd.get(gap)
    c1 = bool(g and g["critical"])
    c2 = (g["lookup"] == "none") if g else None  # None = not scored (question targets no gold gap)
    na4 = not (g and g["route"])
    if g and g["route"] and route == "-":
        errs.append(f"line {ln}: gap has a route, give T or F")
        continue
    c4 = None if not g else (True if na4 else (route == "T"))
    out[qid] = {"gap": None if gap == "-" else gap, "c1": c1, "c2": c2, "c3": tone == "T", "c4": c4, "na4": na4, "unlisted_critical": unl}
missing = [q for q in questions if q not in out]
(SC / "question-ratings.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"rated {len(out)} of {len(questions)}; missing {len(missing)}; errors {len(errs)}")
for e in errs:
    print(" ", e)
