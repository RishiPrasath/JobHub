# E17 thresholds (copied verbatim from README.md, Parts A, B and C; frozen 2026-11-10 before any model call)

The owner's instruction to run E17 is treated as confirmation of these thresholds.

## Part A: shortlist quality

- **Pass:**
  - gold occupation or a correct "no match" in the top three for at least 90% of postings
  - at least 85% of true "no match" postings are not given a confident wrong match
  - at least 85% of postings give the same top-three set across both runs
- **Fail:** top-three recall under 70%, or fewer than 60% of true "no match" postings handled correctly.
- **Inconclusive:** anything between.

## Part B: can users confirm

- **Pass:** users pick the gold occupation, or "none of these" when it is correct, at least 80% of the time.
- **Fail:** under 60%.
- **Inconclusive:** anything between.

## Part C: reading the basis

- **Pass:** at least 75% restate the basis correctly and do not treat the range as a verdict on pay or on their worth.
- **Fail:** fewer than 50%, or any version of the output shown without a stated basis.
- **Inconclusive:** anything between.

# Operational definitions added before the run (they implement the thresholds above; they do not change them)

1. Sample: 100 postings (60 reused from E10 X3 with salary withheld, 40 synthetic). Gold = frozen reconciled labels in `data/gold.json`.
2. A posting has a *gold code* if its accepted set contains a real occupation code, and a *true no-match* if both labellers said NONE.
3. The matcher returns three ranked candidate codes from a 25-item lexical shortlist, a `verdict` ("match" or "none"), and a confidence (high, medium, low) for its first choice. The product would always show the three candidates plus "none of these".
4. **Top-three hit:** for a posting with a gold code, any accepted code is among the three candidates. For a posting whose gold is NONE (true no-match, or a resolved ambiguity where NONE is accepted), a hit means the matcher said verdict "none" (or, for an ambiguity with an accepted alternative code, also if that code is in the three). "Correct no match" is therefore the matcher flagging no match; the user-facing "none of these" option is always shown and is not credited.
5. **Confident wrong match** (on true no-match postings only): verdict "match" with first-choice confidence high or medium. The high-only count is reported as well. "Handled correctly" = not a confident wrong match.
6. **Seniority error:** the first choice (when verdict is "match") is in the posting's gold `too_senior` or `too_junior` list.
7. **Stability:** the unordered set of three candidate codes is identical across run 1 and run 2 of the primary model.
8. **Verdict rule:** thresholds are judged on the primary model (qwen/qwen3.8-27b) using the lower of its two runs for each measure. The second model (openai/gpt-oss-20b, one run) is reported beside it and does not decide the verdict.
9. Part B and Part C cannot be run with participants. They are reported "Not run with participants" (inconclusive, no verdict). A simulated persona pilot is reported separately and does not count towards these thresholds.
