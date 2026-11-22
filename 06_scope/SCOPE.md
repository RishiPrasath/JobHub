# JobHub scope

Status: **ten features are in build scope** ([0002](decisions/0002-first-build-scope.md), [0003](decisions/0003-second-build-scope.md), 2026-11-22). They show as `testing` on the board because none meets the N3 need level that the `in` gate requires yet. The other seven remain candidates or later. Levels are provisional.

## Accepted so far

- The four proposed feature ideas should work across the full job journey. This is a direction, "not a final MVP, platform, architecture or implementation commitment" ([decision log](../strategy/08_decision-log.md)).
- The standalone interview feature is deferred.
- The product surface stays open.
- Profile comparison follows the candidate profile ([0001](decisions/0001-profile-comparison-after-profile.md)).

## Build scope

Decided 2026-11-22 in [0002](decisions/0002-first-build-scope.md) and [0003](decisions/0003-second-build-scope.md).

| Feature | Condition |
|---|---|
| FEAT-001 Employer identity check | Start from a UEN or company domain. A bare brand is treated as a group of entities. |
| FEAT-002 Posting review | Thin version that reuses FEAT-001's output. |
| FEAT-003 Verification questions | Needs a reworked approach; the last result was fail. |
| FEAT-005 Paste capture | As narrowed by E13: snapshot, partial-paste check, field-gap notice and the stale rule (0003). |
| FEAT-006 Red flags | Gazette notices plus ACRA status. Link-outs for restricted sources. |
| FEAT-007 Harmful signals (Singapore) | Allowed free sources only. |
| FEAT-008 Employee reviews | Link-outs to Glassdoor, Indeed, JobStreet and Google Maps; TAFEP Tripartite Standards list by UEN; NodeFlair attempted but not shown without a licence (0003). |
| FEAT-009 Pay benchmark | Occupation level: MOM wage tables on data.gov.sg (Singapore Open Data Licence) plus pay text the user pastes. MyCareersFuture data only with SWDA written permission. |
| FEAT-011 Resume suggestions | The user's own text only: cites the user's profile entries, code check blocks new facts, gaps stay gaps, user confirms each entry (0003). |
| FEAT-013 Offer and contract checks | Entity verification plus a checklist. No legal judgement on clauses. |

Not yet decided, in review order: FEAT-004, FEAT-010, FEAT-015, FEAT-016, FEAT-017, FEAT-012, FEAT-014.

## Board

Generated from `03_features/` by `tools/validate.py`. Do not edit between the markers.

<!-- BOARD:BEGIN -->
| Feature | Scope | Need | Feasibility | Result | Next |
|---|---|---|---|---|---|
| [FEAT-001 Employer identity check](../03_features/FEAT-001-employer-identity-check.md) | testing | N2 | T3 | mixed | ASM-001 |
| [FEAT-003 Verification questions](../03_features/FEAT-003-verification-questions.md) | testing | N2 | T2 | fail | ASM-003 |
| [FEAT-006 Red-flag evidence from official sources](../03_features/FEAT-006-official-red-flag-evidence.md) | testing | N2 | T2 | mixed | ASM-006 |
| [FEAT-007 Discriminatory and harmful signals pack (Singapore)](../03_features/FEAT-007-harmful-signals-pack.md) | testing | N2 | T2 | inconclusive | ASM-007 |
| [FEAT-009 Pay benchmark with stated basis](../03_features/FEAT-009-pay-benchmark.md) | testing | N2 | T2 | inconclusive | ASM-009 |
| [FEAT-013 Offer and contract checks](../03_features/FEAT-013-offer-and-contract-check.md) | testing | N2 | T1 | inconclusive | ASM-013 |
| [FEAT-002 Single-posting review with source-linked claims](../03_features/FEAT-002-single-posting-review.md) | testing | N1 | T2 | mixed | ASM-002 |
| [FEAT-005 Paste capture with snapshot and stale notice](../03_features/FEAT-005-paste-capture.md) | testing | N1 | T2 | mixed | ASM-005 |
| [FEAT-008 Employee experience and reviews](../03_features/FEAT-008-employee-experience.md) | testing | N1 | T2 | fail | ASM-008 |
| [FEAT-011 Evidence-linked resume suggestions](../03_features/FEAT-011-resume-suggestions.md) | testing | N1 | T2 | mixed | ASM-011 |
| [FEAT-004 Accept, edit, reject and decision record](../03_features/FEAT-004-review-and-decision-record.md) | candidate | N1 | T1 | inconclusive | ASM-004 |
| [FEAT-010 Profile and preference comparison](../03_features/FEAT-010-profile-comparison.md) | candidate | N1 | T1 | mixed | ASM-010 |
| [FEAT-015 Interview practice](../03_features/FEAT-015-interview-practice.md) | candidate | N0 | T0 | none | ASM-015 |
| [FEAT-016 Candidate profile](../03_features/FEAT-016-candidate-profile.md) | candidate | N0 | T0 | none | ASM-016 |
| [FEAT-017 Initial setup of job preferences](../03_features/FEAT-017-initial-setup-job-preferences.md) | candidate | N0 | T0 | none | ASM-017 |
| [FEAT-012 Application tracker and reminders](../03_features/FEAT-012-application-tracker.md) | later | N1 | T0 | none | ASM-012 |
| [FEAT-014 Autofill without retyping](../03_features/FEAT-014-portal-autofill.md) | later | N1 | T0 | none | ASM-014 |
<!-- BOARD:END -->

## Decisions needed

1. **First slice:** decided 2026-11-22, posting review with the employer identity check and the other build-scope features ([0002](decisions/0002-first-build-scope.md)).
2. **Profile comparison:** decided 2026-11-10, later, after the profile is built ([0001](decisions/0001-profile-comparison-after-profile.md)).
3. **Company research sources:** decided 2026-11-22. Official sources are in build scope (FEAT-006, FEAT-007). Lived-experience reviews (FEAT-008) are link-outs plus the TAFEP Tripartite Standards list; no review text from sites that bar automation ([0003](decisions/0003-second-build-scope.md)).
4. **First user and target outcome:** not chosen.
5. **Earlier approvals:** `reports/10` calls the hypothesis "approved", but no decision is logged. What actually happened?
6. **Third-party text in git:** ignored in E09, tracked in E10. Which policy applies?

## Rejected in documents, awaiting confirmation

Fit scores and hiring prediction, scam or legitimacy verdicts, auto-apply and employer messaging, automatic resume and cover letter generation, job-board crawling and logins, continuous employer monitoring. Sources: `reports/09` and `reports/13`.

## Next step

Review the remaining candidates in the order above, rework the FEAT-003 approach, and plan the first user test, which is also what the build-scope features need to reach N3. No participant test has been run; start from P1-P3 in [E10](../04_experiments/E10-market-value-and-red-flag-experiments/README.md) and `reports/10`.
