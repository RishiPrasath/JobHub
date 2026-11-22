---
id: FEAT-004
title: Accept, edit, reject and decision record
type: feature
scope: testing
need_level: N1
feasibility_level: T1
result: inconclusive
opportunity: [OPP-002]
needs: []
findings: [FND-R04-01, FND-E08-01, FND-E12-01]
riskiest_assumption: ASM-004
decision: 0006
updated: 2026-11-22
---

# Accept, edit, reject and decision record

In build scope ([decision 0006](../06_scope/decisions/0006-third-build-scope.md)): the concept is accepted, and how it is presented is left to design. The owner's first idea is that the user types a proposed edit and gets suggested edits back. The decision record stays minimal until people are shown to return to it. Scope is `testing` until the `in` gate is met.

Levels are provisional and await owner review.

## What it does

Lets a person correct AI output and record a decision with a rationale.

## Evidence for

Research favours explainable assistance with approval.

## Evidence against

Walkthrough only; keyboard, focus, zoom and screen-reader use are untested.

## Where documents disagree

None significant.

## Next test

Tested inside [E12](../04_experiments/E12-single-posting-review/README.md) Part B, not in a separate experiment. Feasibility is not claimed until it has run.

- **Planted wrong item:** each AI worksheet contains one wrong item the participant is not told about. Proposed pass: caught at least 75% of the time. Proposed fail: under 50%.
- **Skim indicators:** record accept, edit or reject for every item, and time per item. Proposed pass: fewer than 90% of reviewable items accepted untouched. Proposed fail: more than 90% accepted untouched.

Riskiest assumption (ASM-004): people review claims rather than skim or ignore them. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

Not tested in E12, by owner decision on 2026-11-10:
- **Accessibility and interruption recovery** (keyboard, focus, zoom, screen reader). Deferred to a later test on a rendered prototype.
- **Whether people return to their recorded decision and reason.** Not measured for now. The decision record stays an untested part of this feature.

## Result of the first run (2026-11-10)

The planted-error catch rate and skim indicators need real participants; the simulated pilot did not run. Inconclusive. See [E12 findings](../04_experiments/E12-single-posting-review/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.

## Completion run (E12, 2026-11-11)

A simulated pilot (6 persona-posting pairs, not participants) ran on 2026-11-11: the planted wrong item was caught in 6 of 6, and 74% of 96 worksheet items were accepted untouched. These figures are from a language model and cannot satisfy or fail a threshold. Real participants are still needed. See the addendum in [E12 FINDINGS](../04_experiments/E12-single-posting-review/FINDINGS.md).

## Completion run (E12, 2026-11-11)

A simulated pilot (6 persona-posting pairs, not participants) ran on 2026-11-11: the planted wrong item was caught in 6 of 6, and 74% of 96 worksheet items were accepted untouched. These figures are from a language model and cannot satisfy or fail a threshold. Real participants are still needed. See the addendum in [E12 FINDINGS](../04_experiments/E12-single-posting-review/FINDINGS.md).
