---
id: FEAT-001
title: Employer identity check
type: feature
scope: testing
need_level: N2
feasibility_level: T3
result: mixed
opportunity: [OPP-001]
needs: [S-05, S-35]
findings: [FND-E10X2-01, FND-P05-01, FND-E09-02, FND-R09-01, FND-E11-01]
riskiest_assumption: ASM-001
decision: 0002
updated: 2026-11-22
---

# Employer identity check

In build scope ([decision 0002](../06_scope/decisions/0002-first-build-scope.md)), starting from a UEN or company domain; a bare brand is treated as a group of entities. Scope is `testing` until the `in` gate is met.

Levels are provisional and await owner review.

## What it does

Resolves a brand to a legal entity using the registry plus a web step.

## Evidence for

Strongest test result in the repo (X2), and prototype P05 caught a lookalike.

## Evidence against

Only 12 brands; 1 wrong answer; small employers fail discovery. Scam statistics do not show that this would prevent scams.

## Where documents disagree

In the deck plan first slice but absent from `reports/13`.

## Next test

Planned in [E11](../04_experiments/E11-employer-identity-check/README.md), in two parts:

- **Part A (technical):** run the P05 flow on 60 real postings, including small employers, hidden-employer agency postings and lookalikes. Ground truth is set before the run, without registry-mirror sites. Thresholds are proposed in E11 and await owner confirmation.
- **Part B (usefulness):** a concierge test with 6 to 8 job seekers, to test the riskiest assumption: knowing the legal entity changes what a job seeker does next.

See the result below.

Related, from the 2026-11-10 narrowing of [FEAT-003](FEAT-003-verification-questions.md): points that a public record can answer (is the company registered, is the agency licensed, is the number reported) are lookups shown by JobHub, not questions left for the user to ask. They are not yet specified here or tested in E11. The owner decides whether they become part of this feature.

## Result of the first run (2026-11-10)

E11 Part A ran twice on 39 synthetic postings (33 with known truth; truth set by an AI) with the P05 flow unchanged. Named employers with an exact legal name were resolved correctly 13 of 13 times, and 6 of 6 lookalikes were not confirmed. No brand-named employer (0 of 8) resolved to the operating entity. The flow has no "employer not disclosed" state and named a company on 4 of 6 hidden-employer postings in run 1 and 3 of 6 in run 2; under the E11 definition these are wrong accepted answers (4 and 3, against a pass limit of 2 and a fail line of 4). Correct on known truth 21 of 33 (64%) and 22 of 33 (67%) against a 70% bar. **Part A fails by the written rule.** **Narrow to employers named by their registered legal name**; not supported for brand-only or hidden-employer postings without new steps. Part B not run. See [E11 findings](../04_experiments/E11-employer-identity-check/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
