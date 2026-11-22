# Round 11 decision gate

Status: **proposal for the owner.** Nothing here sets a scope value. Scope decisions belong in `06_scope/decisions/`, and only the owner sets `in` or `out`.

## The question

FEAT-012 (application tracker and reminders) is `later`, at N1 and T0. Does R11 change that, and what form, if any, should be built?

## What the round shows

See [round-synthesis.md](round-synthesis.md). In one line: the need to remember and close applications is plausible, but silence itself cannot be fixed by a user-side tool, no Singapore data shows how long a normal wait is, and nobody has shown that people would keep a list up to date. Everything is desk evidence at N2 or lower.

## Options for the owner

| Option | What it means | What the evidence says | What it needs |
|---|---|---|---|
| 1. Keep `later`, fold the questions into the first user test | No build. Run the [interview and diary guide](interview-and-diary-guide.md) alongside the first user test | Fits the evidence: the central assumption (ASM-012) is untested and R11 found no behaviour data | A recruitment plan that includes lower-wage, shift and gig workers |
| 2. Settle only the saved-jobs list (0002 M11) now | A plain status list with the user's decision and reason, status changed only by the user. No reminders, no expected-wait, no give-up rule | Approach 1 is the best supported by the findings (A F2, B F1) and is already in your v1 direction as a pending item | Decision on M11 and S7 (decision record), which are already open |
| 3. Add a closure step to that list | Option 2 plus the "No reply by [date], I'm moving on" record feeding FEAT-004 | Plausible (B F1, F10; A F11) but unproven that people want or use it; no tool does it | Neutral wording rules; FEAT-004 decision; a user test of the wording |
| 4. Add user-set reminders and follow-up templates | Option 2 or 3 plus user-chosen reminders and editable follow-up templates the user sends | Templates are published by Singapore career sites (C); no evidence follow-up works; WhatsApp and phone unserved | Reminder design; a decision on whether templates cover WhatsApp and phone |
| 5. Add an expected-wait signal | Quote MCF, LinkedIn or Indeed figures on the user's job | The pattern exists, but all are employer-level, methods undocumented, and conflicting advice shows no norm | Source rules; wording that never says overdue; PDPA and defamation thinking if ever pooled |

A reading, not a decision: Options 1 and 2 are consistent with each other (settle the plain list, test the rest). Options 3 to 5 each add something the evidence has not tested. Pooled employer responsiveness from user data is not in any option; the Responsible AI review treats it as a separate owner question.

## Questions for the owner (from the Responsible AI review)

1. Is a visible, JobHub-derived employer responsiveness figure in scope at all, given MCF, LinkedIn and Indeed already publish theirs?
2. If user data were pooled later, what minimum cohort, anonymisation and notice would be required, and should a PDPA review be scheduled?
3. May JobHub ever set a status, or only the user? Is a fixed ban on "ghosted", "dead" and "rejected" wording acceptable?
4. Should templates cover WhatsApp and phone, given the lower-wage group is otherwise unserved?
5. Should lower-wage, shift and gig workers be in the first user test before any silence feature is decided?
6. Is SkillsFuture Jobseeker Support proof of activity a use case, and what privacy handling would it need?

## Open gaps from the round

Singapore days-to-reply and drop-off; MCF label method and MOM's filter status; whether following up helps or harms; how people decide to stop; lower-wage, shift and gig practices; SkillsFuture Jobseeker Support proof requirements. See the synthesis.

## Outcome (added 2026-11-22)

The owner chose a reduced FEAT-012 (saved-jobs list with user-set status and a reopenable "No reply" archive, about 4-week changeable default) and set retention for the archive and profile. Recorded in [decision 0006](../../../06_scope/decisions/0006-third-build-scope.md). Reminders, templates and expected-wait signals stay later; the pooled-data and data-protection questions above remain open. Runs E and F were added at the owner's request to settle the wait time and retention.

## Not done (as of the first pass, before the outcome above)

No scope value, feature file, board or decision record was changed by this round. If the owner chooses an option, the decision would be recorded as a new numbered decision, and FEAT-012's reason for `later` updated, by the owner or on the owner's instruction.
