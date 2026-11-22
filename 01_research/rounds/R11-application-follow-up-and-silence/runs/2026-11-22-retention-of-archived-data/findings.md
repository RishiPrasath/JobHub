# Run F findings: Retention and deletion for JobHub's per-job archive and candidate profile

Run date: 2026-11-22. Added after the main R11 pass at the owner's request. Read-only desk research. **This is research, not legal advice.** Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report. No logins or submissions.

Evidence labels: V-site (primary document read on its publisher's own site), V-3p (third-party verification), 2nd (secondary commentary), I (interpretation). PDPC guidelines are advisory, not binding. Only the Key Concepts and ICT guides were revised in 2026; the Selected Topics (2024) and AI (2024) guidelines are older.

**Inspected:** FEAT-016 (open question 1: retention, deletion and access rules); PDPC Key Concepts (text says Revised 29 April 2026; chapters 15, 17, 18, 20 and consent withdrawal), Selected Topics (Revised 23 May 2024, employment chapter), AI Recommendation and Decision Systems (1 Mar 2024), Guide to Data Protection Practices for ICT Systems (Revised 20 Jul 2026); privacy policies and help pages of LinkedIn, Indeed, JobStreet Singapore, Teal, Huntr, Simplify, Careerflow; MyCareersFuture user FAQ PDF only; TAFEP's 2026 article on record-keeping. Copyright was covered by search results only.

## PDPA findings

**Does the PDPA apply to JobHub?** The Data Protection Provisions bind organisations, not "individuals acting in a personal or domestic capacity" (V-site). Interpretation (I): JobHub is an organisation holding users' data, so it is in scope. A user privately jotting down a recruiter's name is probably in a personal capacity, but JobHub is still the party holding that note: a grey area to flag.

**Retention Limitation (s25; Key Concepts chapter 18, V-site).**
- Cease to retain documents, or anonymise them, once the collection purpose is no longer served and retention is no longer necessary for legal or business purposes (18.1). Judged on reasonableness; no fixed period; no perpetual retention without a legal or business reason (18.2); no "just in case" retention for purposes not notified (18.4(a)(ii)).
- Review data regularly and use different periods per data type (18.5). A written retention policy with the rationale for long retention is good practice (18.8).
- Archived or access-limited electronic data still counts as retained (18.11). Deletion should be "completely irretrievable or inaccessible" as far as possible (18.12). PDPC weighs intent to reuse, effort to restore, third-party access, and whether a reasonable attempt was made (18.13). Anonymisation also counts (18.14).
- Applicant data (Selected Topics 6.8): other applicants' data is "only kept for as long as it is necessary for business or legal purposes". Applicants keep access and correction rights.
- Interpretation (I): for a user-initiated archive the purpose is "keep my application records", lasting while the account is active and the user wants it. It does not clearly cover keeping dormant data indefinitely or reusing it for product improvement unless that purpose was notified (PDPC lists business improvement as a legitimate business purpose, 18.4(b)(iv), so a notified analytics purpose is possible). The wording gives no basis for a fixed number of months.

**ICT systems guide (V-site, Revised 20 Jul 2026).** Have a retention policy with minimum and maximum periods covering "backups and archives". ICT controls can enforce retention periods and flag records at end of life. Delete or anonymise records no longer needed. "The safest data is the data you no longer store." No backup-purge rule; only that backup strategy should include "backup retention".

**Protection (s24, chapter 17).** Reasonable security scaled to sensitivity and harm if exposed. Resumes with contact and employment history justify more than basic controls (I).

**Consent, purpose, withdrawal.** Withdrawal of consent must be allowed (s16); PDPC's rule of thumb is at least 10 business days to give effect, and organisations must say what the consequences are. Consent for a job application is deemed for assessing that application only (Selected Topics 6.2); any other use needs a notified purpose.

**Access and Correction.** On request, the individual gets their personal data and how it was used in the past year, as soon as reasonably possible (default 30 days); correction within 30 days; a copy in documentary form, reasonable fee allowed. If the data has already been deleted, the organisation says it no longer holds it (15.7), which favours genuine deletion over "soft" retention.

**Data breach notification (Part 6A, chapter 20).** Assess expeditiously, generally within 30 calendar days. Notify PDPC and affected individuals if likely to cause significant harm; notify PDPC if 500 or more individuals are affected; notification deadline 3 calendar days after assessment as notifiable (20.23, 20.24 as read). A data intermediary must tell the organisation. Less data held means a smaller breach; deleted archives cannot leak (I).

**Data Portability Obligation.** Legislated in the 2020 amendments as Part 6B; commencement needs regulations (2nd). Secondary sources through October 2026 say it is not in force and no regulations were found; not confirmed on a PDPC page (URL 404) or Singapore Statutes Online (403). Key Concepts mentions portability only in a definition of "derived personal data". Interpretation: treat export as a product and trust feature and a way to answer access requests, not a statutory duty today.

**AI and recommendation systems (1 Mar 2024).** Consent and Notification apply to consumer-facing AI; notify at the point of collection, layered and proportionate to risk; encourages data minimisation, anonymising or pseudonymising training data. No specific retention rule other than service providers being data intermediaries with Protection and Retention duties (1.4). Interpretation: reusing archived text for model improvement needs its own notified purpose.

## What comparable products state

| Product | Retention or inactivity rule | Deletion | Export | Source |
|---|---|---|---|---|
| LinkedIn | Kept while account is open, "even if you only use the Services every few years". No inactivity cutoff. | Closing: hidden within 24 hours, "generally" deleted within 30 days, exceptions for legal, fraud and similar. | Copy on request incl. machine-readable data you provided. | Privacy Policy, effective 3 Nov 2025 (V-site) |
| Indeed | No fixed period ("as necessary"). No inactivity rule. | Closing does not delete. A Personal Data Request deletes data and account about a month after identity verification. Glassdoor is separate. | Copy via the same form, before deleting. | Indeed help page and privacy FAQ (V-site), undated |
| JobStreet / SEEK (Singapore) | "As long as necessary", no fixed period. No inactivity rule. | Profile deletion means deleting the whole account. May keep data for legal, fraud, testing or backups. Copies sent to advertisers stay with them. Public-profile content may stay visible elsewhere. | No general download; portable copy only for EEA/UK and some regions. | sg.jobstreet.com/privacy, updated 14 Aug 2026 (V-site) |
| Teal | Kept while active or as needed. No inactivity rule. | Removed from active systems "within 30 days"; backups "per retention schedule", unpublished. Imported Google data persists until account deletion. | By email request; no self-service. | Privacy Policy, updated 11 Nov 2026 (V-site) |
| Huntr | "As long as necessary". | Deactivate or make private; deletion goes via your "Organization", no direct process described. | Not addressed. | huntr.co/privacy, modified 8 Feb 2024 (V-site) |
| Simplify | Kept while you have an account. | Via settings or contact, no timeframe; backup and log residuals "deleted or expire over time". | "Review, change, export, or delete at any time"; format not described. | simplify.jobs/privacy, updated 19 Aug 2026 (V-site) |
| Careerflow | States a cap: no purpose requires keeping data "longer than 1 year", with exceptions; job-application data may be kept longer. | Email request, no timeframe; backups isolated until deletable. | Copy by email request. | careerflow.ai/privacy, updated 15 Sep 2025 (V-site) |
| MyCareersFuture | Not found. | FAQ shows how to delete or edit an uploaded resume; account deletion not found. | Not found. | MCF user FAQs PDF (V-site, undated) |

Observations (I): no product publishes an inactivity-based auto-deletion rule; all are "keep while account exists". Deletion windows cluster at 30 days, with backups handled vaguely. Self-service export is rare. Careerflow's 1-year purpose statement is the only stated cap.

## Design patterns and trade-offs (interpretation)

- **Keep until the user deletes, with one-tap delete and export.** Fits the purpose test (the user asked for the archive). Risk: indefinite retention of dormant accounts, which PDPC warns against. Needs a written rationale and regular review.
- **Inactivity prompts.** Email a reminder at, say, 12 months with keep, export or delete choices, then delete after a grace period if no reply. No competitor does it. Strongest answer to "no longer necessary". Trade-off: users returning after a long break lose records; mitigate with a grace period and export in the reminder.
- **Separate account data from archived documents.** Account data is needed to run the service; archives are optional and can have different lifetimes. The user can delete archives without closing the account. Matches "varying retention periods for each type" (18.5).
- **Third-party personal data in notes.** Notes can name recruiters or contacts. Options: a warning on the notes field, a per-job "delete notes" action, excluding notes from any reuse (analytics, model training).
- **Deletion lag and backups.** Promise clearly, for example "gone from the app immediately, from backups within N days". Archived or access-limited data still counts as retained, and PDPC weighs "reasonable attempt" at permanent deletion. Keep backup windows short and documented.
- **Account deletion.** Remove everything, with an option to export first. Keep only what law requires; say what remains and why.
- **Export.** A readable format with documents, notes and metadata, supporting access requests and trust.

## Risks specific to JobHub's data types

- **The resume.** May contain more than the profile form intends to collect: date of birth, NRIC/FIN, photo, marital status, nationality, health or disability, salary history. FEAT-016 lists these as "not collected" but an uploaded file can contain them. Parsing should drop them, and the stored original is itself a retention item. No PDPA "special category" label; sensitivity and harm scale the required security (17.2). NRIC-type data carries separate PDPC rules not re-read.
- **Archived posting text is third-party content.** May contain recruiter names and emails, which are personal data. Business contact information is excluded from the Data Protection Provisions, but not safe to rely on for arbitrary text. Copyright flag (I, 2nd): Singapore's Copyright Act 2021 has a computational data analysis exception (ss243 and 244) and s187 may void contract terms that restrict it; commentary says it is untested in court and applies only to acts in Singapore. It addresses analysis copies, not a personal archive of postings. Counsel should look at storing full posting text and at scraping against site terms.
- **Notes may name other people** (colleagues, referrers, interviewers, sometimes negative opinions). JobHub holds the third party's data without their knowledge; access requests from those people are possible. The evaluative-opinion exception for job applicants (Selected Topics 6.10) should not be assumed to cover a user's own notes about a recruiter.
- **Tailored resume and cover letter** contain the user's own data plus the employer's name, derived from the profile. Deleting the profile should say whether derived documents go too.
- **Account deletion edge cases.** Parsed resume fields, cached model prompts and logs, backups and analytics copies are all "retention". If an LLM provider processes the text, it becomes a data intermediary and its retention terms matter; none reviewed.
- **User population.** Lower-wage and early-career users may be less able to use email or form-based deletion, which argues for in-app deletion (I).

## What could NOT be found or read

- MyCareersFuture privacy statement and account-deletion rules (site privacy page is JavaScript-rendered; WSG/SWDA statement says nothing on retention).
- A PDPC primary page or Singapore Statutes Online text on portability status (404 and 403).
- Indeed's own retention wording (privacy policy page 404; only help pages and FAQ read).
- LinkedIn backup practice and Huntr deletion process: not stated.
- Independent confirmation of the late-2026 dates on the Teal and SWDA pages.
- Singapore-specific PDPC guidance on recruitment apps or aggregator products; only employer-facing applicant guidance found.
- Any TAFEP or MOM rule on how long a job seeker's own copy should be kept; none exists. The one-year figure is for employers.
- Workplace Fairness Act record-keeping rules; the Data Breach Notification Regulations' full prescribed-data list; court decisions on retention or copyright.

## Limitations

- Several pages were read through a summarising fetch tool and PDFs through text extraction; product policy summaries are not verbatim legal text.
- Singapore guidance changes; the 2024 guidelines predate the 2026 Key Concepts revision.
- The PDPA, the Data Breach Notification Regulations and the Workplace Fairness Act were not read. No signed-in settings screens were read, so self-service claims rest on policy text.
- Not legal advice.

## Retention options for the owner (options, not decisions)

All assume JobHub documents a retention policy with its rationale (Key Concepts 18.8).

**A. Keep until the user deletes.** Pros: simplest, matches competitor norms, clear user control. Cons: weak against "no perpetuity" (18.2); dormant accounts keep sensitive data indefinitely; larger breach surface. Needs: one-tap delete per record and for the account, export, a stated deletion lag including backups, a regular internal review.

**B. Keep with an annual prompt (inactivity-based).** Pros: best fit to the purpose test; users can opt in to keeping archives; reduces dormant data. Cons: no competitor does it; needs email deliverability and a grace period; risk of surprise loss if the prompt is missed. Needs: reminder emails with export, a grace window (for example 30 to 60 days), logs of prompts sent.

**C. Fixed period, then delete.** Pros: strongest minimisation and a simple story; Careerflow states a 1-year cap. Cons: conflicts with an archive's value, since users revisit records for months or years; may drive churn. Needs: a rationale for the period, automatic deletion jobs, an extend-by-user option.

**D. Tiered by data type.** Pros: maps to 18.5 (varying periods per type). Example: profile and account kept while active; archived postings, notes and tailored documents tied to the account; uploaded resume original deleted after parsing or after a short period; notes flagged for review; a prompt on inactivity. Cons: more rules to build, explain and test; risk of inconsistent behaviour (for example a tailored resume outliving its profile). Needs: a data inventory by type, a per-type lifetime table, UI showing each one's status, tests that deletion cascades to derived copies, logs and backups.

A combination (D with B's prompt) is plausible; that is for the owner to decide. Two items need owner input regardless of option: whether the stored original resume file is kept at all, and whether any archived text is reused for model improvement.
