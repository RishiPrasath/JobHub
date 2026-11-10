---
id: FEAT-002
title: Single-posting review with source-linked claims
type: feature
scope: candidate
need_level: N1
feasibility_level: T2
result: mixed
opportunity: [OPP-002]
needs: []
findings: [FND-E01-01, FND-E08-01, FND-R04-02, FND-E02-01, FND-E12-01]
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

See the result below.

## Result of the first run (2026-11-10)

E12 Part A ran on 15 of 24 postings (daily token limit). Claims were 100% grounded with 0 fabricated, but unknown recall was 13% (gpt-oss-120b) and 57% (qwen) against 80%, and gpt-oss-120b kept 0 of 4 planted contradictions. **Narrow to source-anchored extraction**; gap-finding and contradiction-keeping are not supported for gpt-oss-120b and inconclusive for qwen. Part B not run. See [E12 findings](../04_experiments/E12-single-posting-review/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
