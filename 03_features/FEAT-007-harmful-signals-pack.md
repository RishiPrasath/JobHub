---
id: FEAT-007
title: Discriminatory and harmful signals pack (Singapore)
type: feature
scope: candidate
need_level: N2
feasibility_level: T2
result: inconclusive
opportunity: [OPP-003]
needs: []
findings: [FND-R09-02, FND-E15-01]
riskiest_assumption: ASM-007
decision: null
updated: 2026-11-10
---

# Discriminatory and harmful signals pack (Singapore)

Levels are provisional and await owner review.

## What it does

Flags discriminatory or harmful language using a Singapore rule pack.

First-test scope (owner decision 2026-11-10): posting wording only, in five categories: exclusionary wording, questionable screening requirements, requests for money or sensitive information, unpaid work or unclear compensation, and misleading presentation visible in the text. Interview and hiring-process signals (harassment, retaliation, process behaviour) from the 29 Oct "locked direction" cannot be checked against a source and are not covered yet. That direction stays an open question.

## Evidence for

Official guidance exists to draw on.

## Evidence against

No test yet.

## Where documents disagree

Step 4 in `reports/15`.

## Next test

Planned in [E15](../04_experiments/E15-harmful-signals-fixture-test/README.md), in two parts. Feasibility is not claimed until it has run.

- **Part A (fixture test):** 40 cases (10 clearly concerning, 10 benign but similar, 8 ambiguous, 6 job-related or jurisdiction-sensitive, 6 edge text), three methods compared (deterministic phrase matching, AI-assisted retrieval, human-reviewed reference). Gold labels are written beforehand by the owner from TAFEP and MOM guidance, with an HR or employment-law reviewer if one is found. Proposed pass: recall at least 80% on clearly concerning cases, false alarms 10% or less on benign-similar cases, no legal conclusion on any case, every flag with an excerpt and a named source, correct "no reliable signal" on at least 90% of no-signal cases. Proposed fail: any unlawful-as-fact statement, false alarms over 25%, or recall under 60%.
- **Part B (comprehension):** 6 to 8 job seekers read eight prepared flags. Proposed pass: at least 75% read them as concerning but unproven. Proposed fail: under 50%, or a majority drop a posting because of a planted false alarm.

Riskiest assumption (ASM-007): signals can be flagged without false accusations. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E15 on 40 synthetic cases: the deterministic pack found 10 of 10 concerning cases and flagged 0 of 10 benign ones, but only 79% of flags carried a named source, abstention was 85%, and one pack sentence implied illegality. The AI method ran on part of the sample. **Inconclusive**; plausible for TAFEP-sourced wording categories once pack text is fixed; other categories not supported. Part B not run. See [E15 findings](../04_experiments/E15-harmful-signals-fixture-test/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
