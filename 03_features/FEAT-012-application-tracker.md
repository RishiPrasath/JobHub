---
id: FEAT-012
title: Application tracker and reminders
type: feature
scope: testing
need_level: N1
feasibility_level: T0
result: none
opportunity: [OPP-007]
needs: [S-19, S-20, S-21, S-27]
findings: [FND-R09-03, FND-R11-01, FND-R11-02, FND-R11-03]
riskiest_assumption: ASM-012
decision: 0006
updated: 2026-11-22
---

# Application tracker and reminders

Decision 0008 (M11, S7): full job record without reminders; reminders and templates stay later.

Reduced version in build scope ([decision 0006](../06_scope/decisions/0006-third-build-scope.md)): a saved-jobs list with a status the user sets, and a reopenable "No reply" archive that keeps the posting snapshot, source link, review, documents and notes. JobHub never changes a status by itself. The archive default is about 4 weeks, which the user can change (1 to 12 weeks), and JobHub only suggests "Archive?". Reminders, follow-up templates and expected-wait signals stay later. See [R11](../01_research/rounds/R11-application-follow-up-and-silence/round-synthesis.md). Scope is `testing` until the `in` gate is met.

Levels are provisional and await owner review.

## What it does

Tracks applications and prompts follow-ups.

## Evidence for

S-20 is supported.

## Evidence against

Tracking behaviour is unknown.

## Where documents disagree

Deck core job; absent from `reports/13`.

## Next test

No experiment is planned yet (owner decision 2026-11-10; see the reason below).

When this is picked up again, the open question is still ASM-012: people would keep a tracker up to date. Habits are unknown (R09 found no survey on how people track applications). A suitable first step would be interviews about current tracking habits, then a short diary test of a minimal tracker, before any reminders.

## Reason for `later`

Owner decision, 2026-11-10: postpone. There is no clear idea yet of how this feature would work. The review also found that the one supported need (S-20, knowing where an application stands) is about information employers do not give, which a tracker cannot supply. S-19, S-21 and S-27 are rated weak, no tracking-behaviour data exists, and trackers already exist (R07: Teal, Huntr, Simplify, Jobscan). It is also outside the first slice in report 13.
