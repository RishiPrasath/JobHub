---
id: FEAT-003
title: Verification questions
type: feature
scope: testing
need_level: N2
feasibility_level: T2
result: fail
opportunity: [OPP-003]
needs: []
findings: [FND-R02-01, FND-R09-02, FND-E12-02]
riskiest_assumption: ASM-003
decision: 0002
updated: 2026-11-22
---

# Verification questions

In build scope ([decision 0002](../06_scope/decisions/0002-first-build-scope.md)), with a reworked approach, since the last result was fail. Scope is `testing` until the `in` gate is met.

Levels are provisional and await owner review.

## What it does

Produces questions the job seeker can put to the employer about unknowns that only the employer can resolve, for example whether an allowance is guaranteed, how overtime is calculated, or what the assessment stages are.

Scope narrowed on 2026-11-10 (owner): questions that a public record can answer are not written for the user to ask. They are lookups, handled by [FEAT-001](FEAT-001-employer-identity-check.md) and the official routes (ACRA, MOM agency directory, ScamShield 1799). Examples: is the company registered, is the agency licensed, is this number reported.

The user decides whether to ask. JobHub does not contact the employer.

## Evidence for

Repeatedly useful model output; research supports proportionate verification.

## Evidence against

Real-world usefulness has not been measured.

## Where documents disagree

None significant.

## Next test

Tested inside [E12](../04_experiments/E12-single-posting-review/README.md), not in a separate experiment. Feasibility is not claimed until it has run.

- **Part A (question quality):** a reviewer rates every generated question on four checks: it targets a decision-critical gap, it needs the employer (a public lookup could not answer it), the tone is neutral, and the right official route is named where one exists. Proposed pass: at least 80% of questions meet all four. Proposed fail: under 50%.
- **Part B (follow-up):** one week later, ask each participant whether they asked any suggested question or checked an official source, what came back, and whether it changed their decision. Proposed pass: at least a third of participants act. Proposed fail: nobody acts.

Riskiest assumption (ASM-003): people ask or act on the suggested questions. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E12 question rubric: 38% of 92 generated questions met all four checks (bar 80%, fail under 50%), and none of the 11 where an official route applied named it. **Not supported as generated**; narrow to fixed per-gap question templates with the official route attached. The one-week follow-up was not run. See [E12 findings](../04_experiments/E12-single-posting-review/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.

## Completion run (E12, 2026-11-11)

With all 24 postings run on both models, 230 questions were rated: 34.8% met all four checks (bar 80%, fail under 50%); 45.7% targeted a decision-critical gap; neutral tone 96.5%; the official route was named in 0 of 25 cases where one exists. See the addendum in [E12 FINDINGS](../04_experiments/E12-single-posting-review/FINDINGS.md). qwen asked 206 questions (32% usable) and gpt-oss-120b only 16. The one-week follow-up was not run.

**Feasibility call (for the owner to confirm):** not supported as generated. Test fixed per-gap question templates with the official route attached.

## Completion run (E12, 2026-11-11)

With all 24 postings run on both models, 230 questions were rated: 34.8% met all four checks (bar 80%, fail under 50%); 45.7% targeted a decision-critical gap; neutral tone 96.5%; the official route was named in 0 of 25 cases where one exists. See the addendum in [E12 FINDINGS](../04_experiments/E12-single-posting-review/FINDINGS.md). qwen asked 206 questions (32% usable) and gpt-oss-120b only 16. The one-week follow-up was not run.

**Feasibility call (for the owner to confirm):** not supported as generated. Test fixed per-gap question templates with the official route attached.
