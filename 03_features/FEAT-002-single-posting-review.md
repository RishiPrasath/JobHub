---
id: FEAT-002
title: Single-posting review with source-linked claims
type: feature
scope: candidate
need_level: N1
feasibility_level: T2
result: pass-small-sample
opportunity: [OPP-002]
needs: []
findings: [FND-E01-01, FND-E08-01, FND-R04-02, FND-E02-01]
riskiest_assumption: ASM-002
decision: null
updated: 2026-11-10
---

# Single-posting review with source-linked claims

Levels are provisional and await owner review.

## What it does

Breaks one posting into sourced claims, unknowns and conflicts.

## Evidence for

Completeness gate passed in two model runs.

## Evidence against

No interface or participant test. Holistic runs weakened a contradiction.

## Where documents disagree

Core of `reports/13`.

## Next test

Planned in [E12](../04_experiments/E12-single-posting-review/README.md), in two parts. Feasibility is not claimed until it has run.

- **Part A (draft quality):** run the guarded review on 30 postings with gold labels written beforehand, including planted contradictions and hidden-instruction postings. Thresholds are proposed in E12 and await owner confirmation.
- **Part B (usefulness):** a concierge test with 6 to 8 job seekers comparing the raw posting, a manual worksheet and the AI worksheet (following `reports/10`), with a planted wrong item to see whether people catch it. This tests the riskiest assumption: people find a structured evidence view more useful than reading the posting.

E12 is a plan only. Nothing has been run.
