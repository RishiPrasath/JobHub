---
id: FEAT-008
title: Employee experience and reviews
type: feature
scope: testing
need_level: N1
feasibility_level: T2
result: fail
opportunity: [OPP-001]
needs: []
findings: [FND-E09-01, FND-E09-02, FND-P05-01, FND-E16-01]
riskiest_assumption: ASM-008
decision: 0005
updated: 2026-11-22
---

# Employee experience and reviews

Decision 0008 (S9): official facts plus link-outs; attempt scraping of public pages with no login, stopping at bot checks, with a terms note per source; no review-theme summaries. Redesign and retest before build.

In build scope ([decision 0005](../06_scope/decisions/0005-second-build-scope.md)) as link-outs to Glassdoor, Indeed, JobStreet and Google Maps, plus the TAFEP Tripartite Standards list by UEN. NodeFlair is attempted but not shown (licence needed). No review text is fetched from sites that bar automation. Scope is `testing` until the `in` gate is met.

Levels are provisional and await owner review.

## What it does

Summarizes lived-experience evidence about an employer.

## Evidence for

It is a real user interest in the service plan.

## Evidence against

Search was weak for culture, pay and interviews; Glassdoor failed 21 of 21.

## Where documents disagree

The service plan prioritizes it; experiments do not support that.

## Next test

Planned in [E16](../04_experiments/E16-employee-experience-sources/README.md), in three parts, as a source survey before any build. Scope stays `candidate` and the result stays `fail` until it reports (owner decision 2026-11-10). Feasibility is not claimed until it has run.

- **Part A (permitted sources):** list candidate sources (licensed data, sources whose terms allow the intended use, official sources, job-seeker contributions, link-out only), and record terms, cost and permitted uses before any fetch. Proposed pass: at least one source is permitted for the intended use. Proposed fail: none, which narrows the feature to link-out cards or parks it.
- **Part B (coverage):** on permitted sources only, count first-hand accounts from the last 24 months for 20 Singapore employers (large, mid-size, small, agency). Proposed pass: at least 5 accounts for at least half of the employers. Proposed fail: under 25% reach 5.
- **Part C (reading, only if A and B pass):** 6 to 8 job seekers read a hedged summary. Proposed pass: at least 75% say it reflects individual accounts and not the whole company, and at least half would use it. Proposed fail: under 50% understand its limits.

Riskiest assumption (ASM-008): review content can be obtained reliably and lawfully. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E16 Part A failed: no external review source permits reading and summarising reviews. **Narrow to link-out cards** or park. Parts B and C not run. See [E16 findings](../04_experiments/E16-employee-experience-sources/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.

## Build (P06, 2026-11-22)

[P06](../05_prototypes/P06-employee-reviews/README.md) builds the card from decision 0005: four link-outs, the TAFEP Tripartite Standards lookup by UEN (21,116 employers on the live list, updated to 20 Nov 2026), and a NodeFlair probe that keeps aggregates only and is never shown. 14 offline tests pass. Not yet checked: the Glassdoor, Indeed and JobStreet link patterns (a person should click them once) and the live TAFEP download from Python. The riskiest assumption (ASM-008) stays failed for review text; the card holds no reviews.
