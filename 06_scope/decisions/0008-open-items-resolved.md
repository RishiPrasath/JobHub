# 0008: Open items resolved (identity card, rules pack, questions, claims, company research, job record, test plan, privacy)

Status: accepted
Date: 2026-11-22
Decided by: owner

## Context

After [0007](0007-fourth-build-scope.md) the owner went through the remaining open items from [0002](0002-round-10-must-have-review.md), [0006](0006-third-build-scope.md) and [0007](0007-fourth-build-scope.md) as multiple-choice questions. For the last four questions (FEAT-014 clipboard note, extra fields, rename, and the inconclusive tests) the owner asked for an explanation and then said "add this to scope"; the recommended options were applied, with the extra fields limited to the low-risk set. This decision records all of it. As before, no feature has N3 evidence, so scopes stay `testing`.

## Decision

| Item | Decision |
|---|---|
| **S3** employer identity card (FEAT-001) | When checks disagree the card shows each check with its result and a "doesn't prove" line, says "checks disagree, verify yourself", links each source, and gives no verdict or score. |
| **S4** rules pack (FEAT-006, FEAT-007) | The owner signs off each new or changed rule. Monthly check of SPF, TAFEP, MOM and ScamShield. Visible change log with dates. |
| **S5** questions to ask the employer (FEAT-003) | Fixed templates per gap type, shown only when the gap is found, quoting the posting line. No AI-written questions. Adding labelled AI questions needs a retest that passes the E12 bar. |
| **S6** claims linked to profile facts (FEAT-011) | Numbers, dates, titles and employers must link to a profile fact or export is blocked. Reworded framing only warns. Optional quick "can you explain this?" check on reworded lines. |
| **S9** company research (FEAT-008, FEAT-001) | Official facts plus link-out cards with freshness and ownership labels. The owner's final decision: attempt scraping of public pages, no login, no accounts. Guardrails: stop at a CAPTCHA, block page or 403 and fall back to a link-out for that source; keep a short terms-of-use note per source with the findings. This replaces the 0005 rule of no review text from sites that bar automation, only for public pages and only within these guardrails. No summarising of review themes (E16). |
| **M11 and S7** job record (FEAT-004, FEAT-012) | Full record without reminders: posting snapshot, review, decision and reason, approved documents, exact files sent, notes and key dates. Reminders, contacts and follow-up templates stay later. |
| **Failed tests** (FEAT-003, FEAT-008) | Redesign and retest before build. FEAT-003 ships templates only; FEAT-008 ships official facts, link-outs and the S9 scraping attempt. Neither ships AI-written output until a retest passes the bar. |
| **N3 gate** | Kept. Features stay `testing`. A first user test, including lower-wage, shift and gig workers and the R11 interview guide, collects N3 evidence before any feature goes `in`. |
| **Privacy** (FEAT-016) | Solo-project scale. The retention and deletion rules from 0006 and R11 run F are written as a one-page plain-language notice ([draft](../privacy-notice-draft.md)). Before any real user uploads anything: the notice, a consent step and a delete button. A professional data-protection check is a gate only before public launch. |
| **Inconclusive tests** (FEAT-007, FEAT-009, FEAT-013, FEAT-004, FEAT-010) | One retest per feature with a stated pass bar, run before build. A fail means reducing that feature's scope. |
| **FEAT-014 clipboard** | A one-time note the first time a user copies a personal item, with a setting to hide it later. No promise to clear the clipboard. |
| **FEAT-014 extra fields** | Added to the FEAT-016 profile as optional: earliest start date, language sub-ratings with a native flag, full postal address. Not added: awards and memberships, referees, nationality and citizenship detail. |
| **FEAT-014 title** | Renamed "Copy-ready application data". The ID stays FEAT-014. |
| **Decision #5** | Logged as not formally decided: no approval of the `reports/10` hypothesis was recorded; 0003 to 0008 are the first logged decisions. |
| **Decision #6** | Third-party text is not tracked in git. Keep findings and source links; reruns fetch again. |

## Not in this decision

- Referees, awards and memberships, nationality detail: left out of the store.
- Pooled reply times: still out of scope.
- The content of the retests and the first user test plan: to be written.

## Risks the owner accepted

- Scraping may breach a site's terms of use even on public pages; the guardrails limit but do not remove this. Per-source terms notes are the record.
- Link-out fallbacks mean some company cards will be thin.

## Consequences

- FEAT-001, 003, 004, 006, 007, 008, 011, 012, 014 and 016 gain notes pointing here. The N3 gate is unchanged.
- Decisions needed #5 and #6 and the 0002 open items S3 to S6, S9 and M11/S7 are closed in `SCOPE.md`.
