---
id: FEAT-010
title: Profile and preference comparison
type: feature
scope: candidate
need_level: N1
feasibility_level: T1
result: mixed
opportunity: [OPP-005]
needs: []
findings: [FND-E03-01, FND-R03-02, FND-E18-01]
riskiest_assumption: ASM-010
decision: null
updated: 2026-11-10
---

# Profile and preference comparison

Levels are provisional and await owner review.

## What it does

Compares explicit candidate facts with role requirements.

## Evidence for

Practical fit comes before preparation.

## Evidence against

The clearest failure in the 10-19 run.

## Where documents disagree

Step 1 in `reports/15`; out or later elsewhere.

## Next test

Planned in [E18](../04_experiments/E18-profile-comparison/README.md), in two parts. Per [decision 0001](../06_scope/decisions/0001-profile-comparison-after-profile.md) this feature follows the candidate profile and the preferences setup. Feasibility is not claimed until it has run.

What is compared (owner decision 2026-11-10): hard facts (employment type, work arrangement, location, pay against the stated minimum, notice period), experience and skills against requirements (the user confirms), and right-to-work flags (informational). No fit score, ranking or hiring probability.

- **Part A (fixture test, runs now):** 24 hand-collected postings against 3 synthetic profiles in the FEAT-016 and FEAT-017 formats (72 comparisons), with gold labels written beforehand. Three methods are compared: free-text model comparison as in E03, structured field comparison against extracted posting facts, and a hybrid where the model proposes quoted evidence and the user confirms. Proposed pass: unsupported inferences 2% or less, hard-fact errors 1% or less, known facts omitted on no more than 10%, unknown shown as unknown at least 90%, zero cross-role contamination, no fit score, zero false "not eligible" claims. Proposed fail: unsupported inferences over 10%, hard-fact errors over 5%, or any fit score.
- **Part B (with people, waits for a real profile):** 6 to 8 job seekers compare their own profile against three postings. Proposed pass: at least 75% of planted wrong items caught and at least 75% do not read the result as a verdict. Proposed fail: under 50% caught, or most read it as a fit verdict.

Riskiest assumption (ASM-010): comparison can avoid unsupported inferences. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E18 Part A (partial): free-text comparison fails (14% unsupported, 10% hard-fact errors). Structured comparison by code had 0 errors on employment type, arrangement and notice in 135 cells and 1.8% hard-fact errors overall (inconclusive). The hybrid method did not run. **Narrow to structured hard-fact and right-to-work comparison**; experience matching inconclusive. Part B not run. See [E18 findings](../04_experiments/E18-profile-comparison/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
