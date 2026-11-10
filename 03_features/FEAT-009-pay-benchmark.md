---
id: FEAT-009
title: Pay benchmark with stated basis
type: feature
scope: candidate
need_level: N2
feasibility_level: T2
result: inconclusive
opportunity: [OPP-004]
needs: []
findings: [FND-E10X3-01, FND-R08-01, FND-R08-02, FND-R02-02, FND-E17-01]
riskiest_assumption: ASM-009
decision: null
updated: 2026-11-10
---

# Pay benchmark with stated basis

Levels are provisional and await owner review.

## What it does

Shows a pay range with its basis and an official anchor.

## Evidence for

Research gives a clear method.

## Evidence against

X3 reached 77% against an 80% bar.

## Where documents disagree

Deck core job; absent from `reports/13`.

## Next test

Planned in [E17](../04_experiments/E17-pay-benchmark-occupation-match/README.md), in three parts, as a new experiment that leaves the [E10 X3](../04_experiments/E10-market-value-and-red-flag-experiments/FINDINGS.md) data untouched. Approach (owner decision 2026-11-10): the matcher suggests the top three occupations plus "none of these" and the user confirms. Feasibility is not claimed until it has run.

- **Part A (shortlist quality):** 100 hand-collected postings across at least 15 job families, including the kinds X3 failed on. Two humans label the correct occupation or "no match" beforehand. Proposed pass: the gold occupation or a correct "no match" is in the top three for at least 90% of postings, and at least 85% of true no-match postings are not given a confident wrong match. Proposed fail: top-three recall under 70%.
- **Part B (user confirmation):** 6 to 8 job seekers each pick from the top three or "none of these" on 8 postings. Proposed pass: correct at least 80% of the time. Proposed fail: under 60%.
- **Part C (reading the basis):** do people restate the basis correctly and avoid reading the range as a verdict on pay or worth? Proposed pass: at least 75%. Proposed fail: under 50%, or any benchmark shown with no basis.

Riskiest assumption (ASM-009): users can confirm their occupation accurately. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E17: with a lexical shortlist and qwen, the gold occupation was in the top three for 81 of 83 scored postings (97.6%) and 15 of 16 true no-match postings were handled; stability was 83% on 47 (bar 85%); a second model did much worse on no-match. Supported at fixture level for the shortlist step; **narrow to a user-confirmed shortlist**. Parts B and C not run. See [E17 findings](../04_experiments/E17-pay-benchmark-occupation-match/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
