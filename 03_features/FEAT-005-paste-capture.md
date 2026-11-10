---
id: FEAT-005
title: Paste capture with snapshot and stale notice
type: feature
scope: candidate
need_level: N1
feasibility_level: T2
result: mixed
opportunity: [OPP-002]
needs: []
findings: [FND-P01-01, FND-R01-01, FND-E13-01]
riskiest_assumption: ASM-005
decision: null
updated: 2026-11-10
---

# Paste capture with snapshot and stale notice

Levels are provisional and await owner review.

## What it does

Captures a posting by paste, with a dated snapshot.

Stale notice rule (owner decision 2026-11-10): the notice shows when the posting's closing date has passed, or when the snapshot is more than 7 days old, and it prompts the user to paste the posting again. The rule is a starting point and is tested in E13.

## Evidence for

Paste is a reliable fallback.

## Evidence against

Phone-to-laptop loss is unproved, so capture should not lead.

## Where documents disagree

Original idea wanted adaptive browser capture.

## Next test

Planned in [E13](../04_experiments/E13-paste-capture/README.md), in two parts. It is separate from E12 because E12's participants are given postings and so never choose to paste. Feasibility is not claimed until it has run.

- **Part A (paste quality):** run the snapshot step on the 30 E12 postings plus 10 deliberately partial pastes. Proposed pass: at least 80% of pastes contain the minimum fields (title, employer, pay, duties, closing date, or an explicit absence), at least 90% of partial pastes flagged, and the stale rule correct on all test snapshots.
- **Part B (user effort):** 6 to 8 job seekers paste three real postings each, one from a phone, and are asked what a stale notice means. Proposed pass: median time 2 minutes or less, at least 75% finish unaided, effort rated acceptable, and at least 75% understand the notice. Proposed fail: most rate the effort not worth it, or under 50% finish unaided.

Riskiest assumption (ASM-005): pasting is acceptable effort for real users. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E13 Part A on synthetic pastes: stale rule 153 of 153 and snapshot restore 40 of 40 correct, partials flagged 10 of 10, completeness 63% (inconclusive; most misses are fields the board never shows). On harder pastes the simple detector got 2 of 10 right and a model check 10 of 10 (post hoc). **Narrow to snapshot, partial-paste check, field-gap notice and the stale rule**; the notice should state its reason. Part B not run. See [E13 findings](../04_experiments/E13-paste-capture/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
