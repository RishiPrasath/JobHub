# JobHub scope

Status: **no feature is in build scope.** Every candidate awaits owner review. Levels are provisional.

## Accepted so far

- The four proposed feature ideas should work across the full job journey. This is a direction, "not a final MVP, platform, architecture or implementation commitment" ([decision log](../strategy/08_decision-log.md)).
- The standalone interview feature is deferred.
- The product surface stays open.

## Board

Generated from `03_features/` by `tools/validate.py`. Do not edit between the markers.

<!-- BOARD:BEGIN -->
| Feature | Scope | Need | Feasibility | Result | Next |
|---|---|---|---|---|---|
| [FEAT-001 Employer identity check](../03_features/FEAT-001-employer-identity-check.md) | candidate | N2 | T3 | pass-small-sample | ASM-001 |
| [FEAT-003 Verification questions](../03_features/FEAT-003-verification-questions.md) | candidate | N2 | T2 | none | ASM-003 |
| [FEAT-006 Red-flag evidence from official sources](../03_features/FEAT-006-official-red-flag-evidence.md) | candidate | N2 | T2 | mixed | ASM-006 |
| [FEAT-009 Pay benchmark with stated basis](../03_features/FEAT-009-pay-benchmark.md) | candidate | N2 | T2 | inconclusive | ASM-009 |
| [FEAT-007 Discriminatory and harmful signals pack (Singapore)](../03_features/FEAT-007-harmful-signals-pack.md) | candidate | N2 | T0 | none | ASM-007 |
| [FEAT-013 Offer and contract checks](../03_features/FEAT-013-offer-and-contract-check.md) | candidate | N2 | T0 | none | ASM-013 |
| [FEAT-002 Single-posting review with source-linked claims](../03_features/FEAT-002-single-posting-review.md) | candidate | N1 | T2 | pass-small-sample | ASM-002 |
| [FEAT-005 Paste capture with snapshot and stale notice](../03_features/FEAT-005-paste-capture.md) | candidate | N1 | T2 | mixed | ASM-005 |
| [FEAT-008 Employee experience and reviews](../03_features/FEAT-008-employee-experience.md) | candidate | N1 | T2 | fail | ASM-008 |
| [FEAT-004 Accept, edit, reject and decision record](../03_features/FEAT-004-review-and-decision-record.md) | candidate | N1 | T1 | none | ASM-004 |
| [FEAT-010 Profile and preference comparison](../03_features/FEAT-010-profile-comparison.md) | candidate | N1 | T1 | fail | ASM-010 |
| [FEAT-011 Evidence-linked resume suggestions](../03_features/FEAT-011-resume-suggestions.md) | candidate | N1 | T1 | fail | ASM-011 |
| [FEAT-012 Application tracker and reminders](../03_features/FEAT-012-application-tracker.md) | candidate | N1 | T0 | none | ASM-012 |
| [FEAT-014 Autofill without retyping](../03_features/FEAT-014-portal-autofill.md) | candidate | N1 | T0 | none | ASM-014 |
| [FEAT-015 Interview practice](../03_features/FEAT-015-interview-practice.md) | candidate | N0 | T0 | none | ASM-015 |
| [FEAT-016 Candidate profile](../03_features/FEAT-016-candidate-profile.md) | candidate | N0 | T0 | none | ASM-016 |
| [FEAT-017 Initial setup of job preferences](../03_features/FEAT-017-initial-setup-job-preferences.md) | candidate | N0 | T0 | none | ASM-017 |
<!-- BOARD:END -->

## Decisions needed

1. **First slice:** posting review only (`reports/13`), or with an employer identity check (deck plan)?
2. **Profile comparison:** first (`reports/15`), or later?
3. **Company research sources:** official first, or lived-experience reviews first?
4. **First user and target outcome:** not chosen.
5. **Earlier approvals:** `reports/10` calls the hypothesis "approved", but no decision is logged. What actually happened?
6. **Third-party text in git:** ignored in E09, tracked in E10. Which policy applies?

## Rejected in documents, awaiting confirmation

Fit scores and hiring prediction, scam or legitimacy verdicts, auto-apply and employer messaging, automatic resume and cover letter generation, job-board crawling and logins, continuous employer monitoring. Sources: `reports/09` and `reports/13`.

## Next step

Settle the decisions above, then plan the first user test. No participant test has been run; start from P1-P3 in [E10](../04_experiments/E10-market-value-and-red-flag-experiments/README.md) and `reports/10`.
