# Run C findings: Singapore application forms

Run date: 2026-11-22. Role: Job-Seeker Practices Researcher (#04). Read-only desk research. No accounts, sign-ins, typing or submissions. The subagent could not write files, so the round lead saved this from its returned report.

Evidence labels as in the [round brief](../../round-brief.md). AI-gathered research is capped at N2. Where only a search snippet was seen, the label is 2nd.

## What was inspected

**Read directly (V-site or V-3p):** MyCareersFuture (MCF) user FAQ PDF (undated, mentions September 2026); Public Service Job Application Form PDF (hosted by MLAW and MOE, undated); CSIT's public Lever apply page (viewed only); Careers@Gov privacy statement; MOE SEN Officer application page; SBS Transit "Data Protection for Job Applicants"; Singtel group careers landing page; FairPrice careers FAQ; TAFEP "Preparing Job Application Forms" and the 18 May 2026 Workplace Fairness Act article; PDPC NRIC Advisory Guidelines (31 Aug 2018); LinkedIn Help a512353; Indeed "Applying for a job" help article (US edition).

**Search snippets only (2nd):** JobStreet Singapore "Employer questions" blocks; Singapore Independent articles; FastJobs app-store descriptions; GrabJobs vendor blog; SMRT walk-in snippet.

**Could not see:** every login-gated step (Singpass, MCF, Careers@Gov, JobStreet, LinkedIn, Indeed, Workday, SuccessFactors). Blocked or failed: sg.jobstreet.com job pages, GrabJobs, sg.indeed.com search, theindependent.sg, ask.gov.sg (403); careers.dbs.com (DNS failure); sbstransit.com.sg/careers (404). No form fields were reached for banks, telcos, retail, healthcare or hotels, so CSIT is the only live Singapore-employer form read.

## Form anatomy per site

**MyCareersFuture (V-site).** Browsing needs no login. Singpass login is mandatory to apply; Singapore Citizens and PRs only. Flow: log in, complete Profile, upload a resume (pdf or doc, up to 2MB), click Apply and follow the steps. Employers can add up to 3 screening questions, Yes/No only, mandatory to submit, not editable after publishing. The profile has work-experience entries each with "Key Skills Practised", and Profile Preferences including "Not seeking opportunities". The Careers & Skills Passport holds government-verified records and, from September 2026, will be shareable with employers through applications, with a visibility switch. Status shows under "Applied Jobs". Not seen: apply-step screens and what Singpass pre-fills.

**JobStreet Singapore (2nd).** Job ads show an "Employer questions" block. Snippets quote: right to work in Singapore; expected monthly basic salary; types of qualifications held; notice period required. Widgets not seen. Quick Apply, profile apply and cover-letter steps not seen.

**LinkedIn Easy Apply (V-3p).** Apply without leaving LinkedIn. LinkedIn may offer to save resume and answers for reuse and pre-fill; saved data can be reviewed, updated or deleted in Job applications settings. Unpublished daily and speed limits. No field labels listed. Typical extra questions (2nd, unverified): work authorisation, visa, years of experience, notice period, salary.

**Indeed Apply (V-3p, US edition).** Steps: apply (sometimes phone verification); choose or upload resume; Indeed scans it for experience, education and qualifications, editable, once per resume file; employer questions (blocking); review, optional cover letter, submit; drafts can be saved; submitted applications cannot be edited. Employer side (2nd): up to 100 screener questions per job.

**Careers@Gov and the public-service form (V-site).** MOE pages say to submit through Careers@Gov in a fixed window. The privacy statement says the portal collects names, NRIC, email, contact, addresses, CV information and optionally Google profile data. Portal screens not seen. The paper-style Public Service Job Application Form is the best documented schema: (A) posts applied for, up to 3; (B) personal particulars; (C) career aspirations; (D) work experience, 4 repeating blocks; (E) tertiary qualifications; (F) non-tertiary; (G) memberships; (H) two character referees; (I) seven Yes/No "Other information" questions; (J) declaration and signature; optional professional registration, languages, certifications, awards, scholarships and bonds, CCA. An "Annex A" is for shortlisted candidates only: title, gender, date of birth, country of birth, marital status, race, religion, place of worship, residential address.

**CSIT on Lever (V-site).** Resume upload, basic fields, optional links, a "Recruitment Application Form" with Singapore-specific fields (below), a required declaration checkbox. No National Service, work-pass or EEO fields appeared.

**SBS Transit (V-site).** The Job Listing link goes to a Microsoft Forms page (not opened). The policy lists data collected from applicants. Incomplete data "will not process". Consent must be written. Agents may submit on a candidate's behalf.

**SMRT (2nd).** Weekly walk-in interviews for buses (2025). Bus captain licence (ODVL) via GoBusiness needs photo, driving licence, NRIC, employment letter (2nd).

**Singtel (V-site).** Appears to use SAP SuccessFactors with Sign In / Create Account (inference). Fields not seen.

**FairPrice (V-site, FAQ).** Most roles through the careers site; cashier and retail assistant roles advertised on notices outside outlets; part-timers can walk in; shortlisted candidates contacted within 1 to 2 weeks. Fields not seen.

**Shift and gig platforms (2nd or inference).** FastJobs: app-based; WhatsApp, in-app chat, call or SMS (WhatsApp flow documented for Malaysia; Singapore unconfirmed). GrabJobs: "1-click" apply and a pre-screening chatbot (vendor blog, not fetched). Some Indeed Singapore shift listings say "email your resume".

## Field inventory

Sensitivity scale: low, personal, sensitive, special. Seen in: PSAF = Public Service Job Application Form; CSIT = CSIT/Lever; MCF; JS = JobStreet; SBS; CAG = Careers@Gov.

| Field label | Section | Type | Required | Repeats | Seen in | Sensitivity | Notes |
|---|---|---|---|---|---|---|---|
| Resume/CV | Submit application | file upload | required (CSIT, MCF) | no | CSIT, MCF (pdf/doc, 2MB), Indeed | personal | MCF stores on profile |
| Full name | Personal | text | required | no | CSIT, PSAF ("Full name in NRIC/Passport", surname underlined) | personal | PSAF wants ID-matching name |
| Email | Personal | text | required | no | CSIT, PSAF, CAG | personal | |
| Phone / contact number | Personal | text | required (CSIT); PSAF "with country code" | no | CSIT, PSAF, SBS | personal | |
| Current location | Personal | location lookup | optional | no | CSIT | low | |
| Current company | Personal | text | optional | no | CSIT | low | |
| LinkedIn, GitHub, portfolio, website | Links | text | optional | no | CSIT | low | |
| Total years of working experience | Application form | dropdown (fresh grad, 0-5, 5-10, 10-15, 15-20, 20+) | required | no | CSIT | low | Exact-option |
| Years of relevant experience | Application form | dropdown | required | no | CSIT | low | Varies per job |
| ID Type (NRIC colour) | Personal | radio (NRIC Pink, NRIC Blue, Passport) | required | no | CSIT, PSAF | sensitive | Used to infer PR status |
| Full NRIC | Personal | text | required | no | CSIT, PSAF, CAG | special | PDPC and TAFEP say not at application |
| Present citizenship | Personal | dropdown (CSIT); text/radio with "Held since" (PSAF) | required | no | CSIT, PSAF | sensitive | |
| Previous citizenship | Personal | text | as seen | no | PSAF | sensitive | |
| Permanent Resident (country, since) | Personal | dropdown | required | no | CSIT, PSAF | sensitive | |
| Last drawn / current gross salary | Personal | monthly and annual S$ | as seen | no | PSAF | sensitive | Varies over time |
| Expected gross salary | Personal | monthly and annual S$ | as seen | no | PSAF, JS (2nd) | personal | Per job |
| Earliest date of starting work | Personal | text | as seen | no | PSAF | low | Free text |
| Notice period to current employer | Employer question | likely choice or number | per employer | no | JS (2nd) | low | |
| Right to work in Singapore | Employer question | multiple choice | per employer | no | JS (2nd) | sensitive | Options not seen |
| Which qualification types do you have | Employer question | multiple choice | per employer | no | JS (2nd) | low | |
| Screening questions (up to 3) | Apply step | Yes/No | required if present | up to 3 | MCF | varies | Employer-authored |
| Employer screener questions (up to 100) | Employer questions | not specified | blocking | many | Indeed (2nd) | varies | |
| Posts applied for (1st to 3rd) | Posts | text or dropdown | as seen | up to 3 | PSAF, CSIT | low | |
| Willing to consider other posts | Posts | Yes/No | as seen (required CSIT) | no | PSAF, CSIT | low | |
| Source ("how did you hear") | Application form | dropdown | required | no | CSIT | low | Per job |
| Referrer's name | Application form | text ("NA" allowed) | required | no | CSIT | personal | Per job |
| Existing bonded scholarships | Application form | radio plus text | required | no | CSIT, PSAF | sensitive | |
| Ex-staff | Application form | Yes/No | required | no | CSIT | low | |
| Highest education level | Education | dropdown | required | no | CSIT | low | Fixed list, PhD to NITEC |
| Course of study | Education | text ("NA" allowed) | required | no | CSIT | low | |
| Institution | Education | dropdown (NUS, NTU, SIM-UOW, SIT, SMU, SUSS, SUTD, Overseas, Others) | required | no | CSIT | low | Exact-option |
| Issuing institution if different | Education | text | optional | no | CSIT, PSAF | low | |
| Qualification level, certificate type, year, institution, country, structure, duration | Academic | mixed | as seen | one block per qualification | PSAF | low | |
| Subjects and grades | Academic | table | optional | many rows | PSAF | low | |
| Work experience: organisation, designation, dates joined/left, duties and achievements, employment type | Work experience | text, dates, long text | as seen | 4 blocks | PSAF | personal | |
| Key Skills Practised (per work entry) | Profile | skill tags | profile field | per entry | MCF | low | |
| Career aspirations and why join | Additional | long text | as seen | no | PSAF | low | Per job |
| Memberships and CCA | Optional | text | optional | yes | PSAF | low | |
| Awards and prizes | Optional | text | optional | yes | PSAF | low | |
| Professional registration (board, year) | Optional | text | optional | no | PSAF | low | |
| Language proficiency | Optional | text plus radio | optional | yes | PSAF | low | |
| Other certifications (title, issuer, country, grade, year) | Optional | text | optional | yes | PSAF | low | |
| Character referees (name, relationship, company/designation, years known, email, contact), two, unrelated | Referees | text | as seen | 2 | PSAF | personal (third-party data) | |
| Medical condition, impairment, substance dependence (Y/N, details) | Other information | Yes/No plus text | as seen | no | PSAF | special | TAFEP says remove |
| Criminal record, pending charges, investigation | Other information | Yes/No | as seen | no | PSAF | special | |
| Undischarged bankrupt or unsecured debts | Other information | Yes/No | as seen | no | PSAF | special | |
| Intention to apply for foreign citizenship or PR within a year | Other information | Yes/No | as seen | no | PSAF | sensitive | |
| Broken bond or obligatory service | Other information | Yes/No | as seen | no | PSAF | sensitive | |
| Declaration and consent | Declaration | checkbox (CSIT); signature and date (PSAF) | required | no | CSIT, PSAF | personal | |
| Date of birth, country of birth | Annex A (shortlisted only) | date, text | as seen | no | PSAF | special | |
| Gender, marital status, race, religion, denomination, place of worship, title | Annex A (shortlisted only) | radio or text | as seen | no | PSAF | special | |
| Residential address | Annex A (shortlisted only) | text | as seen | no | PSAF | personal | |
| Nationality, health conditions, family members' data | Applicant data collected | policy text, not a form | policy says collected | no | SBS | special | Not a seen form |

## Singapore-specific fields and the TAFEP / PDPC position

- **NRIC or FIN.** PDPC guidelines (31 Aug 2018): a job application form need not ask for NRIC; the Employment Act records duty covers employees, not applicants. Partial NRIC (last 3 digits plus checksum) is a less intrusive option for identity checks. A 2024 note says the guidelines will be updated and stay valid meanwhile. TAFEP: NRIC reveals age; request at offer or state reasons; accept a passport number. Public service forms and CSIT still ask at application. Whether the public sector has an exemption was not verified (open question).
- **Date of birth and age.** TAFEP says remove. The 18 May 2026 TAFEP article says NRIC and date of birth should generally be collected at offer. The public service form asks date of birth only in the shortlisted annex.
- **Race, religion, gender, marital status, family responsibilities.** TAFEP says remove. The public service form asks only in the shortlisted annex.
- **Disability, mental health, health.** TAFEP says remove; mental-health declarations only if job-related. The public service form still has a medical or impairment question. SBS's policy lists health conditions that may affect the contracted service.
- **National Service.** TAFEP says remove, or ask at offer with reasons. CSIT shows no NS field. No Careers@Gov NS field found; one search summary mentioned an optional NS section on an employer form that was not opened.
- **Photograph.** TAFEP says remove; request at offer if needed.
- **Salary.** TAFEP sources did not cover salary. An MCF article (2nd, snippet) says last-drawn salary is not required by law and an employer cannot insist. Both appear on the public service form and in JobStreet questions.
- **Citizenship, PR, right to work.** Used for work-pass and Fair Consideration reasons. MCF is open to Citizens and PRs only. No TAFEP or PDPC wording found on it.
- **Referees.** Documented on the public service form. TAFEP articles read did not mention referees.
- **Workplace Fairness Act.** TAFEP: expected to take effect by end 2027; employers told to review forms ahead of it (18 May 2026). Inference: it will push protected fields off forms.

## Lower-wage, shift and gig applicants (thin evidence)

- Phone-first and message-first routes: WhatsApp, in-app chat, call, SMS, chatbot pre-screen (2nd). Walk-ins exist (FairPrice V-site; SMRT 2nd; SBS roadshows V-site). Notices outside shops advertise cashier and retail roles.
- Some employers use a plain Microsoft Form (SBS Transit) or ask for a resume by email.
- Job-tied documents: bus roles need a Class 3, 3A, 3C or 3CA driving licence; ODVL needs photo, NRIC, employment letter (2nd). Other licences (food hygiene, security) not confirmed.
- Shifts are stated in ad text (for example "11pm to 8.30am (Sun-Fri)"); no availability or shift-preference field seen. Transport and distance: no source.

## Per-job versus reusable

- **Reusable:** name, phone, email, location, links, resume, work history, education blocks, certifications, languages, referees' details, citizenship and PR answers (if the user chooses to store them), years of experience.
- **Per job:** screening and employer-question answers (right to work, qualifications, notice period, expected salary, which also change over time), "why join" text, ranking of posts, source and referrer, ex-staff answer, declaration.
- **Per stage:** annex fields (date of birth, race, religion, marital status, address) asked only of shortlisted candidates on the public service form.

## Copy-and-paste obstacles

- Exact-option dropdowns with fixed lists (CSIT experience bands, institution list, source list) and Yes/No-only MCF questions.
- Fixed repeating blocks (up to 4 work entries on the public service form; education, certification, referee blocks).
- Placeholder conventions: "NA" required where not applicable (CSIT). Date wording varies (YYYY/MM/DD in the annex; free text for start date).
- MCF resume limited to 2MB, pdf or doc.
- Singpass login and one-time phone verification (Indeed) happen before any form.
- Underlined surname on the public service form cannot be pasted as plain text.
- Paper-style PDF forms need signature and date.
- Character limits, rich-text handling and whether any field blocks paste were not tested.

## What could not be found

- MCF apply-step screens and Singpass pre-fill; live Careers@Gov form fields and FAQ (403).
- JobStreet help articles and Quick Apply flow.
- Fields from real employer sites for banks, telcos, retail, healthcare or hotels (six to eight employers not reached).
- GrabJobs apply screens (403); confirmed WhatsApp apply path for Singapore.
- Detailed public complaints (two Independent headlines could not be opened; a 57% abandonment figure came from a headline only).
- Whether TAFEP says anything on referees, expected salary or languages; PDPC position on referees' personal data.

## Limitations

- Several relevant sites refused automated readers. Findings on JobStreet, LinkedIn, Indeed, GrabJobs and FastJobs rest on help pages and snippets.
- The public service form is a template; agencies can add or drop sections.
- CSIT is the only live Singapore-employer form read, and is not representative of banks, telcos or retailers.
- Most pages have no publication date. Required or optional status for some fields comes from the template.
- Lower-wage and gig routes have almost no first-hand evidence.
- Overall: N2 at best for the public-service and CSIT schemas; N1 or lower for everything else.

## Implications for a store-filter-copy tool (observations, not decisions)

- The reusable core is stable across sources. Singapore forms add NRIC colour, citizenship or PR, bonded scholarship, source and referrer as recurring items.
- Sensitive items conflict: TAFEP and PDPC say NRIC, date of birth, race, religion, marital status, National Service, disability and photographs should not be asked, yet the public service form and CSIT still ask NRIC and the annex asks the rest. A tool storing these would hold data the guidance says employers should not request. A default-off stance is consistent with FEAT-016's "Not collected" list.
- Screening answers and "why this role" text are per job and fit a per-job view with "recently used".
- Exact-option dropdowns and Yes/No questions mean a stored answer may need to match the option string. Date formats and "NA" differ.
- Repeating blocks imply list storage and one-entry-at-a-time copy.
- Referees are third-party personal data and touch the Responsible AI review.
- Singpass and login steps mean copying from a phone or second window into an open form. Phone-first routes for lower-wage jobs may need short copy-ready text (availability, transport, licence), untested.
