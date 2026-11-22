---
id: FEAT-014
title: Autofill without retyping
type: feature
scope: later
need_level: N1
feasibility_level: T0
result: none
opportunity: [OPP-008]
needs: [S-16]
findings: [FND-R09-04]
riskiest_assumption: ASM-014
decision: null
updated: 2026-11-10
---

# Autofill without retyping

Levels are provisional and await owner review.

## What it does

Reuses information across application portals.

Owner direction, 2026-11-20 ([decision 0002](../06_scope/decisions/0002-round-10-must-have-review.md), S12): this is **not autofill**. JobHub does not fill forms itself. It keeps the user's data ready in one copy-ready panel for each job (for example notice period, right to work, contact details, work-history snippets and saved answers), and the user copies and pastes into the employer's form and clicks submit. No automation, no browser extension, no logging in anywhere. Sensitive fields (eligibility, salary expectation, disability, criminal history, demographics) are shown only when the user chooses to reveal them.

## Evidence for

S-16 is supported.

## Evidence against

Friction figures are US snippets only.

## Where documents disagree

Not yet considered as a feature.

## Next test

No experiment is planned yet (owner decision 2026-11-10; see the reason below).

When this is picked up again, the riskiest assumption is still ASM-014: autofill is feasible on real portals. A first step that needs no platform decision is a saved-forms mapping test: the owner saves about 30 real application forms by hand from at least 6 portal types, the system maps each field to a profile field or marks it not covered, and gold labels are written beforehand. It would also check that sensitive fields (eligibility, salary expectation without confirmation, disability, criminal history, demographics) are never proposed for auto-fill, and that hidden instructions in a form are not followed. A live-portal spike needs a platform decision and a terms-of-service review first. The data an autofill would use comes from [FEAT-016](FEAT-016-candidate-profile.md) and the saved answers in [FEAT-017](FEAT-017-initial-setup-job-preferences.md).

## Reason for `later`

Owner decision, 2026-11-10: postpone. No feature has been proposed yet, and a spike on real portals depends on a platform choice (browser extension, web app or helper) that has not been made and is the owner's to make. Job-board logins and crawling are still awaiting owner confirmation, the friction figures are US snippets, R04 sets strict controls on automated form filling, and application actions are outside the first slice in report 13.
