# 0007: Fourth build scope (copy-ready application data, no autofill)

Status: accepted
Date: 2026-11-22
Decided by: owner

## Context

[0006](0006-third-build-scope.md) left FEAT-014 undecided. The owner defined its minimum: a place to store form-filling data, filter it, and copy items to paste into the employer's form, for convenience, with no autofill. The owner asked for research first: [R12, application forms and field inventory](../../01_research/rounds/R12-application-forms-and-field-inventory/round-synthesis.md). R12 is desk research at N2 or lower; no live Workday or iCIMS form and no real user was seen.

## Options considered

From the R12 [decision gate](../../01_research/rounds/R12-application-forms-and-field-inventory/decision-gate.md): (1) the minimum as `testing`; (2) the minimum plus extra form fields (start date, referees, language sub-ratings, address and others); (3) keep `later` and fold the questions into the first user test.

## Decision

Option 1. FEAT-014 is in build scope as the **copy-ready store**, scope `testing` (no N3 evidence, so not `in`).

| Item | Condition |
|---|---|
| What it holds | The data in FEAT-016 and FEAT-017 (contact, links, work and education entries, certifications, skills, languages, right to work, notice period, expected pay, relocate, travel) plus per-job saved answers (cover letter, "why this role", screening answers). |
| Filters | By form section, search by field name, per job, recently used. |
| Copy | A copy button per item; repeating entries copy one field per entry. No autofill, no browser extension, no reading the clipboard, no logging in anywhere, JobHub never submits (0002 S12). |
| Sensitive items | Not stored, following FEAT-016 "Not collected" and FEAT-017 "asked each time". A reveal-on-demand option is not added. |
| Per-job answers | Saved with the job and deleted with it, under FEAT-016's tiered retention. |
| Extra form fields | Not added by this decision. Start date, referees, language sub-ratings, full address, awards and nationality detail stay open (option 2 is not chosen). |

## Not in this decision

- Option 2 fields and referees (third-party data).
- A clipboard warning on contact, eligibility and salary items: recommended by the R12 Responsible AI check, not yet confirmed by the owner.
- Renaming the feature to match copy-only scope (the ID stays FEAT-014).
- Reading public Greenhouse, Workable or Recruitee form schemas to suggest fields.
- Autofill, extensions or any form filling.

## Evidence (finding IDs)

FND-R09-04, FND-R12-01, FND-R12-03, FND-R12-04, FND-R12-05.

## Consequences

- FEAT-014 moves to `testing` with `decision: 0007`. Sixteen features are now in build scope.
- Need N1, feasibility T0. It depends on FEAT-016 and FEAT-017 data existing, so it follows them.
- Needs a first user test: do people use a copy panel, which fields they retype most, and how copying works between apps and on a phone.
- Per-job answers need the retention rules from 0006 written into policy before real data is stored.
