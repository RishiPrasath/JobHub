---
id: FEAT-006
title: Red-flag evidence from official sources
type: feature
scope: candidate
need_level: N2
feasibility_level: T2
result: mixed
opportunity: [OPP-003]
needs: [S-05]
findings: [FND-E10X0-01, FND-E10X1-01, FND-R02-01, FND-R09-02, FND-E14-01]
riskiest_assumption: ASM-006
decision: null
updated: 2026-11-10
---

# Red-flag evidence from official sources

Levels are provisional and await owner review.

## What it does

Checks a company against official lists and records.

## Evidence for

Official verification routes exist.

## Evidence against

Only 2 of 7 sources were readable. X1 failed because the test was too easy.

## Where documents disagree

Source file heading says "Locked direction" while status says "Proposed".

## Next test

Planned in [E14](../04_experiments/E14-official-red-flag-evidence/README.md), in three parts, as a new experiment that leaves the [E10](../04_experiments/E10-market-value-and-red-flag-experiments/FINDINGS.md) raw data untouched. Scope stays as written for now (owner decision 2026-11-10): coverage is tested first, and the feature is narrowed afterwards if no employment source is readable. Feasibility is not claimed until it has run.

- **Part A (source access retry):** retry the five sources X0 could not read, with a rendering fetch and terms of use checked first. Proposed pass: at least one employment-relevant official source is readable within its terms. Proposed fail: none, which would narrow the feature to MAS, CASE and links to official lookups.
- **Part B (harder sweep):** at least 30 organisations, 15 older, smaller or less reported known problems and 15 clean controls, fixed sweep against free-form. Proposed pass: recall at least 70%, unsupported claims 2% or less, at most 10% of controls wrongly flagged, impersonation warnings always labelled as such. Proposed fail: recall under 50%, or any unsupported claim shown without a source.
- **Part C (presentation):** 6 to 8 job seekers read prepared outputs, including a brand-impersonation warning and "nothing found". Proposed pass: at least 75% read the warning correctly and at least 75% do not treat "nothing found" as clean. Proposed fail: under 50% on either.

Riskiest assumption (ASM-006): enough official sources can be read to be useful. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

Open overlap: which feature owns the ACRA, MOM agency directory and ScamShield lookups (FEAT-001 or this one) is not decided.

## Result of the first run (2026-11-10)

E14: MOM's flagged-agency list and stop-work orders are readable within terms (Part A pass, narrow); PDPC, ScamShield and ACRA are not permitted. The open web sweep found 1 of 5 known problems (20%, fail); the direct list check found 5 of 5 by construction. **Narrow to direct lookups of MOM, MAS and CASE lists plus links to official lookups**; the open sweep is not supported; MOM reuse needs permission. Part C not run with participants. See [E14 findings](../04_experiments/E14-official-red-flag-evidence/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
