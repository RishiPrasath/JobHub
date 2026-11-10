---
id: FEAT-013
title: Offer and contract checks
type: feature
scope: candidate
need_level: N2
feasibility_level: T1
result: inconclusive
opportunity: [OPP-009]
needs: [S-30, S-31, S-40]
findings: [FND-R09-03, FND-E20-01]
riskiest_assumption: ASM-013
decision: null
updated: 2026-11-10
---

# Offer and contract checks

Levels are provisional and await owner review.

## What it does

Compares a written offer with what was agreed. No feature has been proposed yet.

First shape to test (owner decision 2026-11-10): a **completeness check against official guidance only**. It reports which terms that MOM Key Employment Terms and TAFEP guidance say should be stated are present, missing or unclear in an offer letter, and whether the letter is inconsistent with itself, with the official source for each. It gives no legal conclusion. Comparing the offer with a posting snapshot or with a recorded verbal agreement, and suggested questions at offer stage, are later questions.

## Evidence for

Stories S-30, S-31 and S-40 are supported.

## Evidence against

No test yet.

## Where documents disagree

Not yet considered as a feature.

## Next test

Planned in [E20](../04_experiments/E20-offer-completeness-check/README.md), in three parts. Feasibility is not claimed until it has run.

- **Part A (interviews):** 8 to 10 people with an offer in the last 12 months describe what they received, what they checked, what differed, and whether they would have used a check. Proposed pass: at least half found a missing term or a discrepancy and at least half would have used a check. Proposed fail: under a quarter would have used a check.
- **Part B (completeness fixture test):** 20 offer letters (complete controls, planted missing terms, planted inconsistencies, and consented redacted real letters), with gold labels written beforehand. Proposed pass: planted items found at least 90%, no more than 1 false alarm per 10 letters, every rule statement citing a named official source, no legal conclusion. Proposed fail: recall under 70%, or any legal conclusion.
- **Part C (concierge on a real offer):** the Part A people see the check's output on their own redacted offer. Proposed pass: at least half see something new and most read it as what is missing, not a legal judgement. Proposed fail: under a quarter see anything new, or most read it as a verdict.

Riskiest assumption (ASM-013): people would use a check at offer stage. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E20 Part B on 10 synthetic letters: planted items found 91 to 95%, no legal conclusions, but false alarms exceeded the budget in every run and one run mixed up sources. **Inconclusive**; recall and legal wording look workable, reliability does not yet. Parts A and C not run. See [E20 findings](../04_experiments/E20-offer-completeness-check/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
