# 0006: Third build scope (comparison, profile, preferences, review step, saved jobs with a No reply archive)

Status: accepted
Date: 2026-11-22
Decided by: owner

## Context

[0004](0004-first-build-scope.md) and [0005](0005-second-build-scope.md) put ten features in build scope and left FEAT-004, FEAT-010, FEAT-015, FEAT-016, FEAT-017, FEAT-012 and FEAT-014 undecided. On 2026-11-22 the owner reviewed FEAT-004, FEAT-010, FEAT-015, FEAT-016, FEAT-017 and FEAT-012 one by one. For FEAT-012 the owner asked for a new research round first: [R11, application follow-up and silence](../../01_research/rounds/R11-application-follow-up-and-silence/round-synthesis.md), with two follow-up runs on the archive wait time and on retention.

As in 0004 and 0005, none of these features has N3 evidence, so their `scope` is `testing`, not `in`. Moving any to `in` needs N3 evidence or a change to the gate in [03_features/README.md](../../03_features/README.md), and is the owner's call.

## Options considered

Each candidate: add to build scope, or leave. For the archive wait time: a fixed value, a user-chosen value, a changeable default, or a default that varies by role type (R11 run E). For retention: keep until the user deletes, an annual prompt only, a fixed period then delete, or tiered by data type with an inactivity prompt (R11 run F, research and not legal advice).

## Decision

Five features are in build scope, with these conditions.

| Feature | Condition |
|---|---|
| [FEAT-004 Accept, edit, reject and decision record](../../03_features/FEAT-004-review-and-decision-record.md) | The concept is accepted. How it is presented is left to design; the owner's first idea is that the user types a proposed edit and gets suggested edits back. The decision record stays minimal until people are shown to return to it. |
| [FEAT-010 Profile and preference comparison](../../03_features/FEAT-010-profile-comparison.md) | Compare a posting with the candidate's preferences and profile or resume, find the issues and notify the user. Each issue is checked in code and quotes the posting line and the profile entry it clashes with. No free-text model comparison, which failed (FND-E18-01). Experience and skills are shown as items for the user to confirm, with no pass or fail and no score. Follows FEAT-016 and FEAT-017 (0001 still applies). |
| [FEAT-016 Candidate profile](../../03_features/FEAT-016-candidate-profile.md) | As written, with all sections and the required sign-up fields, because matching, decisions, resume refinement and applying all need it. Retention is tiered by data type, with a yearly prompt to keep, export or delete and a grace period. The original resume file is deleted after parsing and only confirmed fields are kept. Archived text is not reused for model improvement without a new notified purpose. |
| [FEAT-017 Initial setup of job preferences](../../03_features/FEAT-017-initial-setup-job-preferences.md) | As written. Deal-breakers follow 0002 M6 (built-in list plus custom); matching free-text deal-breakers by meaning is untested. |
| [FEAT-012 Application tracker and reminders](../../03_features/FEAT-012-application-tracker.md), reduced | A saved-jobs list with a status the user sets, and a reopenable archive for applications with no reply. This settles the simple form of 0002 M11 and S7. Details below. Reminders, follow-up templates, expected-wait signals and pooled employer data stay later. |

### FEAT-012 reduced: the saved-jobs list and the No reply archive

- Statuses are set only by the user. JobHub never changes a status, never infers one, and never sends anything to an employer.
- The visible label is **No reply**. Wording such as "ghosted", "rejected", "closed by employer" or "overdue" is not used. Users may write their own words in notes.
- The user moves a job into the archive. After the waiting time the user chose, JobHub may only suggest "Archive?" and the user confirms.
- Waiting time: a changeable default of about 4 weeks, which the user can set from 1 to 12 weeks. The label reads "No reply after N weeks". R11 run E found no evidence for one number, so the default is a starting point and the reopen path is the safeguard.
- The archive keeps the dated posting snapshot and source link, the posting review and employer identity check, the tailored resume and cover letter, the date applied, any follow-ups the user sent, notes and the reason for moving on.
- On reopening the user can: change the status with a dated note, keeping the history; view the saved source and review; compare a late message to the saved details (an idea so far, untested); and reuse the documents.
- Retention follows FEAT-016: the user can delete any archived job or the account, and can export. Notes carry a notice not to store other people's personal details, and a delete-notes action per job is in scope.

## Not in this decision

- **FEAT-015 Interview practice:** not added, by owner decision. It stays a `candidate`.
- **FEAT-014 Autofill without retyping:** not yet decided; still `later`.
- **0002 M11 and S7 beyond the simple list:** richer saved-jobs views and any reminder design are not settled.
- Pooling users' recorded reply times into an expected wait is not in scope; the R11 Responsible AI review treats it as a separate question needing a data-protection review first.

## Evidence (finding IDs)

FEAT-004: FND-R04-01, FND-E08-01, FND-E12-01. FEAT-010: FND-E03-01, FND-R03-02, FND-E18-01. FEAT-016: FND-R09-04, FND-R11-04. FEAT-017: FND-E18-01. FEAT-012: FND-R09-03, FND-R11-01, FND-R11-02, FND-R11-03.

## Consequences

- FEAT-004, FEAT-010, FEAT-012, FEAT-016 and FEAT-017 move to `testing` with `decision: 0006`. Fifteen features are now in build scope in total.
- FEAT-011 now has its profile source (FEAT-016), which 0005 flagged as a gap.
- FEAT-016 and FEAT-017 have N0 need evidence and T0 feasibility, so they need a first user test early; the [R11 interview and diary guide](../../01_research/rounds/R11-application-follow-up-and-silence/interview-and-diary-guide.md) can be folded into it.
- FEAT-016's retention and deletion rules are chosen but still need a written policy and, because R11 run F is research and not legal advice, a data-protection review before real resume upload ([0003](0003-v1-scope-answers.md) already requires a privacy notice).
- FEAT-012's `testing` scope covers only the reduced version; its reminders, templates and wait signals remain `later`.
- FEAT-010's comparison of experience and skills, and FEAT-017's free-text deal-breakers, have no passing test yet.
