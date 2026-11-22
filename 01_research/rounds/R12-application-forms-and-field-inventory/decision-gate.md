# Round 12 decision gate

Status: **proposal for the owner.** Nothing here sets a scope value. Scope decisions belong in `06_scope/decisions/`, and only the owner sets `in` or `out`.

## The question

FEAT-014 is `later`, at N1 and T0. Your proposed minimum: a place to store form-filling data, filter it (form section, search by field name, per job, recently used) and copy items to paste into the employer's form, with no autofill. Does R12 support adding it, and in what shape?

## What the round shows

See [round-synthesis.md](round-synthesis.md). In short: forms share a stable core that FEAT-016 already holds, most of each form is employer-chosen, pasting often needs an option picked or a unit fixed, and employers still ask items the guidance says to drop. Friction is reported but not measured for Singapore, and no tool reviewed offers a browse and filter screen for saved answers. All N2 or lower, and no real user has been asked.

## Options for the owner

| Option | What it means | What the evidence says | What it needs |
|---|---|---|---|
| 1. Add the minimum as `testing` | A panel of FEAT-016 and FEAT-017 data plus per-job saved answers, filters as you listed, copy buttons. No autofill, no extension, no clipboard reading | Supported as a need (retyping is a consistent complaint) but N1 and T0; the stable core makes it feasible | Decision record (0007); a first user test of whether people use it; Responsible AI guardrails below |
| 2. Option 1 plus the missing form fields | As option 1, and extend FEAT-016 with earliest start date, referees, language sub-ratings, full address, awards, nationality detail, source and referrer | Forms ask all of these (synthesis coverage map); each adds data to hold and retain | Owner choice per field; referees need third-party data rules |
| 3. Keep `later`, fold the questions into the first user test | No build; ask which fields people retype and how they copy | Matches the evidence level; delays a feature you want | A recruitment plan that includes lower-wage and shift workers |

A reading, not a decision: Option 1 fits what you asked for and the evidence, and Option 2 can be added field by field after the first test. Option 3 is the cautious choice.

## Questions for the owner

1. Sensitive items forms still ask (NRIC, last-drawn salary, gender, medical, criminal record): keep them out of the store entirely, as FEAT-016 does, or allow a reveal-on-demand, device-only option?
2. Per-job saved answers (cover letter, "why this role"): saved with the job and deleted with it, under FEAT-016's retention?
3. Referees: store at all? If so, name and contact only, with a consent reminder.
4. Copy warnings: show a note on contact, eligibility and salary items that the clipboard may keep them?
5. Keep the title "Autofill without retyping", or rename to match the copy-only scope? (IDs never change; titles can.)
6. Should reading public Greenhouse, Workable or Recruitee form schemas to suggest fields ever be considered? It is outside this round.

## Open gaps

Live Workday, iCIMS and login-gated Singapore forms; phone behaviour; Singapore friction figures; lower-wage and gig routes; real-user use of a copy panel. See the synthesis.

## Not done

No scope value, feature file, board or decision record was changed by this round. If the owner chooses an option, it would be recorded as a new numbered decision and FEAT-014's file updated.
