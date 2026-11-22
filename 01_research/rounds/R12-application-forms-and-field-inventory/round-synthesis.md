# Round 12 synthesis: Application forms and field inventory

Status: **draft, owner review pending.** Written by the round lead from runs A to D. It changes no scope and decides nothing. Evidence is AI-gathered desk research, capped at N2. Run letters: A enterprise systems, B mid-market systems, C Singapore, D friction and autofill.

## Answer in brief

1. **Forms share a stable core, and it matches FEAT-016.** Name, email, phone with country code, location, links, resume, repeating work and education entries, skills and languages appear on nearly every system (A, B, C).
2. **Most of a form is not the core.** On 48 sampled Greenhouse postings, 17 to 22 questions each, roughly 70 to 80% employer-chosen. Workable's six Singapore forms ranged from 5 to 27 fields (B).
3. **Reusable and per-job fields split cleanly.** Reusable: contact, work and education entries, languages, links, right to work, notice period, salary expectation. Per job: cover letter, "why this role", accomplishment prompts, screening answers, source, referrer, consents and declarations (A, B, C).
4. **The same fact is asked in many shapes.** Work authorisation appeared as yes/no, citizen/PR/other, a five-option government classification, a dropdown with "Work Visa", and a separate sponsorship question (B). Salary appears monthly or annual, with or without currency (B, C).
5. **Pasting often will not work as typed.** Exact-option dropdowns (universities about 3,300 options, nationalities about 200), comboboxes, location autocomplete that needs a clicked suggestion, split phone fields, plain-text boxes, character limits (127, 255, 100) (A, B). So a copy tool should show the option to select, not only a string.
6. **Entries repeat one at a time**, with dates and "I currently work here" checkboxes. Per-entry, per-field copy fits (A, B, C).
7. **Employers still ask what Singapore guidance says to drop.** NRIC at application (public-service form, CSIT), last-drawn salary and bonus, a required gender question (Airbnb Singapore), a medical declaration (public-service form), and, on the public-service form, date of birth, race, religion and marital status for shortlisted candidates only (B, C, D).
8. **Friction is real but not measured for Singapore.** US vendor surveys put abandonment and "too tedious" figures high; none is Singapore, and several are old or from tool vendors (D).
9. **No reviewed tool shows a browse, search and filter screen for saved answers.** Simplify reuses answers by matching the question text, browser-local. This may be a gap or may simply not have been seen (D).
10. **Session loss is a real risk.** Workday and SuccessFactors do not resume timed-out sessions; one source says Workday times out within about ten minutes (2nd) (A, D). Quick, one-click copy helps more than a whole-form paste.

## Merged field inventory (summary)

Full rows with sources are in each run's findings. Sensitivity: low, personal, sensitive, special.

| Group | Fields | Reusable or per job | Sensitivity | Seen in |
|---|---|---|---|---|
| Identity and contact | Full name, preferred name, email, phone (with country code), city and country, current residential area, full address (Workday) | Reusable | personal | A, B, C |
| Links | LinkedIn, GitHub, portfolio, other websites | Reusable | low to personal | A, B, C |
| Resume and documents | Resume file, cover letter file or text, combined resume plus cover letter (iCIMS Guelph) | Resume reusable; cover letter per job | personal | A, B, C |
| Work history entries | Title, employer, location, from, to, current, description, part-time percentage | Reusable, repeating | personal | A, B, C |
| Education entries | Institution, qualification, field, dates, grade, country, course structure | Reusable, repeating | low | A, B, C |
| Certifications, languages, skills | Name, issuer, dates; language proficiency (five sub-ratings plus "native"; CEFR); skills | Reusable, repeating | low | A, B, C |
| Eligibility | Right to work, sponsorship, citizenship, PR, NRIC colour, nationality, age 18+, Singapore government classification | Reusable, wording varies per form | sensitive | A, B, C |
| Preferences | Expected salary, notice period, earliest start date, relocate, travel, hybrid or office, years-of-experience band | Reusable, format varies per form | low to personal | A, B, C |
| Source and affiliation | How did you hear, referrer, worked here before, relatives here, ex-staff, bonded scholarship | Per job or per employer | low to sensitive | A, B, C |
| Per-job answers | Why this role, proudest accomplishment, AI-use description, motivation (word limits in text), posts ranked, other posts | Per job | low | A, B, C |
| Referees | Name, relationship, company, years known, email, phone (two on the public-service form) | Reusable, repeating; third-party data | personal | A, C |
| Consents and declarations | PDPA, truthfulness, talent pool, arbitration, AI policy, SMS and WhatsApp, typed signature and date | Per employer | personal | A, B, C |
| Demographic and compliance | Gender, race, veteran, disability, date of birth, religion, marital status, National Service, criminal record, bankruptcy, medical, NRIC number, last-drawn salary, bonus | Asked per form | special or sensitive | A, B, C |

## Coverage map against FEAT-016 and FEAT-017

**Covered:** full name, preferred name, email, phone, city and country, right to work, LinkedIn, portfolio and other links, headline, summary, work entries (title, employer, location, dates, current, description), education (institution, qualification, field, dates, grade), certifications, skills, languages, resume file. FEAT-017 covers expected pay, notice period, relocate, travel and work arrangement.

**Asked by forms, not held today:**

| Item | Where seen | Per job or reusable | Note |
|---|---|---|---|
| How did you hear, referrer | A, B, C | Per job | Small; per-job note |
| Earliest start date | B, C | Reusable | Not in FEAT-016 or FEAT-017 |
| Language sub-ratings and "native" flag | A | Reusable | FEAT-016 has one proficiency level |
| Part-time percentage | A | Per entry | |
| Referees (two) | C, A | Reusable, third-party data | Not in FEAT-016 |
| Years of experience bands | C | Derivable from work entries | Option string matters |
| Nationality, citizenship, PR detail, NRIC colour | B, C | Reusable, sensitive | FEAT-016 right to work is one choice; forms split it |
| Awards, memberships, CCA, professional registration | C | Reusable, repeating | Optional on the public-service form |
| Full postal address | A, C | Reusable, personal | FEAT-016 has city and country only |
| Cover letter text, "why this role" answers, screening answers | A, B, C | Per job | The core of a per-job answer store |
| Notice period in other units, expected salary in other formats | B, C | Reusable | Needs unit-tagged variants |

**Asked by forms and on the "Not collected" list (never stored by default):** NRIC, date of birth, gender, race, religion, marital status, disability, photograph, National Service, last-drawn salary and bonus, criminal record, bankruptcy, medical declaration. Employers still ask these (see answer 7). The store has no field for them; the user types them each time. That is a position, and the decision gate asks whether to keep it.

**Not stored, asked each time (FEAT-017):** background-check consent, demographic surveys, worked here before, relatives here. R12 confirms all appear, plus privacy, talent-pool, arbitration and SMS consents, which are per employer.

## What the store has to handle (design observations, not decisions)

- Show each item as a labelled copy chip with the item's variants (for example "Notice period: 1 month / 4 weeks / 30 days") rather than one string.
- For list-pick fields, show the exact option label to choose and note that pasting may not work (nationality, university, source).
- Show a character count beside long text, with the common limits (127, 255).
- Split phone into country code and number; keep dates as month and year plus a free-text form.
- Repeating entries: one copy action per field per entry, grouped by entry.
- Per-job answers saved against a job, with a "recently used" filter.
- Filters wanted by the owner: form section, search by field name, per job, recently used. The sections seen in forms (Personal, Experience, Education, Eligibility, Preferences, Screening, Consent, Demographic) give a natural section list.
- Phone use is untested. Copying between two apps while a session times out is the likely worst case.

## Responsible AI check of a copy-ready store

Done by the round lead against the role's checklist; Responsible AI Reviewer (#11) has not reviewed. Each concern is a question for the owner.

| Concern | What the evidence shows | Suggested guardrail |
|---|---|---|
| Clipboard history keeps copied personal data | Windows keeps 25 items and can sync them across devices; some Android keyboards keep previews and history (D, 2nd) | Warn on copying contact, eligibility and salary items; one-click "clear clipboard" is not reliable, so say so; do not copy sensitive items by default |
| Sensitive fields | Forms still ask NRIC, last-drawn salary, gender, medical, criminal record (B, C, D) | Keep them out of the store by default (FEAT-016 "Not collected"); owner decides whether a reveal-on-demand, device-only option exists, as 0002 S12 once described |
| Referees | Third-party personal data (C) | Notice not to store other people's data beyond name and contact; consent reminder; per-entry delete |
| Retention | Archived and stored data still counts as retained (R11 run F) | Follows FEAT-016's tiered retention and yearly prompt; per-job answers deleted with the job |
| Employer or form content shown back | A saved question can quote an employer's wording | Treat as user data; no sharing; no pooling across users |
| JobHub never fills or submits | Copy is user-initiated; no page access | Keep the copy-only boundary; no extension; no reading the clipboard |
| Wording to the user | "Pasting may not work" is a limit, not a failure | Neutral wording; no "autofill" claims |
| Terms and bot detection | A tool that never touches the page does not match the bot pattern (inference, no terms read) (D) | Confirm only if the owner ever considers an extension |
| Public-API field reading | Greenhouse, Workable and Recruitee publish form schemas | Reading these at scale to prefill suggestions is outside this round and a separate owner and review decision |

## Conflicts and gaps

- **Required or optional.** Guides say demographic items are optional; some tenants mark them required (Oregon asterisk; Airbnb Singapore gender required). Required status is employer configuration, not a fixed rule (A, B).
- **Sources disagree on NRIC.** Guidance says do not ask at application; the public-service form and CSIT ask. Whether the public sector has an exemption was not verified (C).
- **Not seen:** any live Workday or iCIMS form; MyCareersFuture, JobStreet and Careers@Gov apply screens; employer forms for banks, telcos, retail, healthcare or hotels; BambooHR, Jobvite, Breezy; phone behaviour; character limits for most fields; Workday date format and paste behaviour; Workday and iCIMS timeout lengths; any Singapore friction figure; lower-wage and gig routes (WhatsApp, chat) beyond snippets.
- **Real users not asked.** Nothing here shows people would use a store-and-copy panel, how they handle it between apps, or which fields they retype most.

## Evidence level

Need: N1 (friction reported in US vendor surveys, consistent complaints about retyping). Feasibility: T0 (no prototype; copy-only is technically simple, no test). Nothing in R12 reaches N3.
