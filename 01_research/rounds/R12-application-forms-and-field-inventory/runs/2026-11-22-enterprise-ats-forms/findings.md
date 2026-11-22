# Run A findings: Enterprise applicant tracking system application forms

Run date: 2026-11-22. Role: Job Domain Researcher (#03). Read-only desk research on Workday, Oracle (Taleo Enterprise and Oracle Recruiting Cloud), SAP SuccessFactors and iCIMS, from vendor admin docs, employer HR candidate guides (PDFs read as text) and a few help or community pages. No account created, nothing typed, no live application form opened. The subagent could not write files, so the round lead saved this from its returned report.

Evidence labels as in the [round brief](../../round-brief.md). Capped at N2. Candidate guides come from universities, cities and agencies, so each shows one employer's configuration, not the vendor default.

**Could not see:** any live employer form on the four systems; everything behind sign-in; several SAP knowledge-base articles (login needed, previews only); iCIMS "Understanding Field Types" (401); the Edmonton Taleo guide (502). Not covered: Cornerstone, Phenom, Avature.

## Form anatomy per system

### Workday (McGill, Penn State, Oregon guides; vendor admin docs)

1. **Entry.** Click Apply on the posting.
2. **Start choice.** Oregon (revised 2026-05-14): Autofill with Resume, Apply Manually, Use My Last Application. Penn State: "Use my last application" or "Upload a new Resume or CV". McGill: resume-select screen.
3. **Account wall.** Sign In or Create Account. Penn State: non-institutional email, password with upper, lower, number and symbol, a privacy-consent checkbox, then email verification. Workday docs: external candidates typically must create a Candidate Home account on first application (tenant setting). Social sign-in optional, shares only the email. Questionnaires need a registered account.
4. **Resume parse screen.** Drag-and-drop or "Select files". McGill: parsing fills name, location, education and work experience; do not parse academic CVs "due to their size and complexity". Oregon: with no resume, later steps "will not pre-populate".
5. **My Information.** Name, address, email (pre-filled), phone with country code, "How did you hear about us?". Employers add "previously affiliated?" follow-ups (Penn State: prior email, 9-digit ID, manager; McGill: McGill ID). McGill required: Country, First name, Last name, Phone number, How did you hear. Oregon: red asterisk marks required; warns to enter County and not Country in the address field.
6. **My Experience.** Repeating Work Experience (Job Title, Company, Location, From, "I currently work here" or To, Role Description), Education, Skills, Languages, Websites. Penn State Education: School, Degree, "Field of Study or Overall Result (GPA)". Languages: proficiency in listening, overall, reading, speaking, writing plus a "native" flag. Resume/CV upload, cover letter and other documents at the bottom. McGill: all files under 5 MB combined; otherwise link a shared drive in Websites.
7. **Application Questions.** Vary by job. McGill: Microsoft Office self-rating, Canadian work-entitlement question. Penn State: age 18+, work authorisation, sponsorship, state-retirement-system question with conditional sub-question.
8. **Voluntary Disclosures.** Gender, Race/Ethnicity (checkboxes), Veteran Status, terms checkbox. Penn State: "not required". Oregon marks some with an asterisk, so required status differs by employer.
9. **Self Identify.** Disability form (Yes / No / I don't wish to answer), ending with a typed name and a date picker (Penn State).
10. **Review and Submit.** Oregon: "Save and Continue" at each step. McGill: submitted applications cannot be edited and you cannot reapply to the same position. Oregon: after submit, extra tasks in Candidate Home may remain (veteran status, questionnaire). Oregon: if the employer un-posts and reposts the job while a draft is open, the draft cannot be submitted; start again.

**Later stages (not the form, but data-relevant).** References requested by task. On offer: National ID (SIN or SSN/ITIN), date of birth, gender, citizenship (McGill, Penn State).

### Oracle Taleo Enterprise

Configurable from a block list. Documented default: Profile Upload, Candidate Personal Information, Education, Work Experience, E-Signature, Review and Submit, Thank You.

- **Vanderbilt (2010 PDF metadata, old):** privacy agreement; new user or login; optional upload; plain text resume paste box, cover letter paste box, attachments; Personal Information, Education, Certifications; Work Preferences (job-family preferences need an "Add to list" click), Work Location Preferences, Organizational Preferences; Public Records Questionnaire; job-specific prescreening plus source tracking; diversity questions; references; eSign; review. "If you do not hit the Submit button, your application will not be entered".
- **City of Richmond:** five steps: register; Your Information (resume upload, "How did you hear", Additional Information); Resume and Documentation (attachments, screening questions); Work and Education History pre-filled from the resume with Edit, Remove, Add Work History, Add Education; Review and Submit (eSignature and date). "Just want to submit your resume?" general profile route.
- **TCNJ:** separate Taleo-only login. Only highest education and the most recent job are needed; certifications can be skipped; diversity survey; Review.
- **Edmonton (snippet only, 2nd):** sign-in via Gmail, Yahoo or Taleo accounts; external applicants can deactivate their account to delete their profile.
- **Parse:** Oracle says the resume is "parsed into the available fields in the following pages", with optional LinkedIn and Indeed import; fields not listed. The Resume Upload block must be alone on its page and precede Personal Information, Education and Work Experience. Candidates can edit or remove parsed entries.

### Oracle Recruiting Cloud (Fusion)

Admin-defined application flows with sections and blocks. Contact Information is the only required block (25A guide); the Easy Apply guide also names Review as required, so it depends on flow type and release. Easy Apply is a chat-bot flow: terms, name and email, resume upload, optional AI-generated "work summary" used as the cover letter, an emailed verification code before final submit. Express Apply imports profile information; field mapping not described. Diversity fields are chosen by administrators per country via Transaction Design Studio. The full sections-and-blocks list was not read. Older PeopleSoft Candidate Gateway (Fluid) "does not allow applicants to copy and paste resume text" (snippet only, 2nd).

### SAP SuccessFactors Recruiting

- **Account wall.** Apply Now, Sign In, Create an Account; one-time-password email. Accounts can be created without applying.
- **Profile versus application.** Reusable profile (Profile Information, Work Experience, Education, Languages; EASA): "The information requested in the candidate profile is the same for all vacancies", and pre-fills later applications. A separate "Job specific information" section must be filled every time.
- **Upload and parse.** Toronto: a resume is mandatory ("no Build a Resume option"); DOCX, PDF, image, text accepted; MSG, PPT, XLS not; uploads from device, Dropbox or Google Drive; auto-populates Profile Information, Employment History and Formal Education. EASA: auto-populates "some fields"; optional at application. SAP KBA 2951470 (preview): parsed Supervisor Name, Supervisor Phone, Salary, Reason for Leaving have no standard field and are merged into the Job Description field. Other KBAs (snippets): parsing fills only empty fields; Apply with LinkedIn plus parsing can overwrite.
- **Mandatory fields.** EASA: cannot save a section unless all mandatory fields are filled; its workaround is dummy data to modify later.
- **Job-specific information.** Multiple choice, short and long text, equal-opportunity block; declaration required. Toronto: typed-name "Statement of Agreement" plus date.
- **Save and submit.** Toronto: "Save" makes a draft hidden from hiring managers; "Apply" submits and cannot be edited. EASA: submitted applications can be edited under "Jobs applied" (employer setting).
- **Quick Apply / mobile.** A SAP article says a candidate not logged in cannot see attachment fields. Mobile Apply consolidates profile and application onto one page.

### iCIMS (Guelph, vendor community article, search)

- **Entry and account.** "Apply For This Job Online"; the email-entry page decides new or returning. Name, email, login, password, or social sign-in (Facebook, Google, LinkedIn, Microsoft) that transfers first name, last name, email.
- **Upload.** From computer, Google Drive, Dropbox or OneDrive. Upload first because parsing can fill profile fields. A resume may not be needed to start but "may be required before you finish".
- **Guelph configuration.** Cover letter and resume must be one file. Steps: Upload, Create a profile, Add other information, Job questionnaire, Confirmation. Returning users click "replace".
- **Typical steps (vendor article).** Candidate Profile ("Update Profile"), screening questions, EEO information, job-specific questions, confirmation.
- **Save later.** "Finish Later" at some steps; "Continue Application" under Past Job Submittals.
- **Not seen.** Required-field lists, file size or format limits, session timeout.

## Field inventory

R = required as documented or seen, O = optional, V = varies by employer or job, N/D = not documented.

| Field label | Section | Input type | Required | Repeats | Seen in | Sensitivity | Notes |
|---|---|---|---|---|---|---|---|
| Country | My Information | dropdown | R (McGill) | no | Workday, McGill | low | Oregon: enter County, not Country, in address |
| First name, Last name | My Information | text | R | no | Workday McGill; Taleo Richmond | personal | Parsed from resume where used |
| Middle name or initial | My Information | text | N/D | no | Workday Penn State | personal | |
| Address Line 1, City, State, Postal Code, County | My Information | text | V | no | Workday Penn State, Oregon | personal | |
| Email | My Information | text | R, auto-filled from account | no | Workday Penn State | personal | Institutional emails rejected for external accounts |
| Phone country code | My Information | dropdown or typeahead | V | no | Workday Penn State | personal | Pre-set to +1; type the country, pick the radio |
| Phone number | My Information | text | R (McGill) | no | Workday McGill; SuccessFactors EASA | personal | EASA: with international code |
| How did you hear about us? | My Information | typeahead or multilevel dropdown | R (McGill) | no | Workday McGill, Penn State; Taleo Richmond | low | Source then sub-category (Penn State) |
| Previously affiliated (yes/no) | My Information | radio or dropdown | V | no | Workday Penn State, McGill | personal | Follow-ups: prior email, ID, manager |
| Employee or student ID | My Information | text | R if affiliated | no | Workday McGill, Penn State | personal | Employer-specific ID |
| Resume file | Resume upload or My Experience | file | V | multiple files | All four | personal | Limits below |
| Cover letter file | My Experience | file | V | multiple files | Workday McGill; SuccessFactors Toronto; iCIMS Guelph (combined with resume) | low | |
| Plain-text resume | Resume and Documentation | text area | V | no | Taleo Vanderbilt | low | Configurable rows, columns, minimum characters |
| Cover letter (plain text) | Resume and Documentation | text area | V | no | Taleo | low | |
| Job Title | Work Experience | text | R within entry | yes | Workday Penn State; Taleo Richmond; SuccessFactors EASA | low | |
| Company or Employer | Work Experience | text | R | yes | same | low | |
| Location | Work Experience | text | V | yes | Workday Penn State | low | "City and state" |
| From and To dates | Work Experience | date picker or typed | R within entry | yes | Workday Penn State; Taleo | low | Format not confirmed; MM/YYYY is an assumption |
| I currently work here | Work Experience | checkbox | V | yes | Workday Penn State; Taleo | low | |
| Role Description | Work Experience | text area | V | yes | Workday Penn State | low | No documented limit; an anecdote (Blind) says special characters caused an error |
| Part-time percentage | Work Experience | numeric | V | yes | SuccessFactors EASA | low | |
| School or University | Education | typeahead | R within entry | yes | Workday Penn State; Taleo | low | Must pick from list |
| Degree | Education | dropdown | V | yes | Workday Penn State | low | |
| Field of Study | Education | typeahead | V | yes | Workday, Intel guide | low | Intel: type "Other" and press Enter |
| Overall Result (GPA) | Education | text | V | yes | Workday Penn State | personal | |
| Education level, Institution, Program, dates | Education | text and dropdown | V | yes (min 0-10) | Taleo, Oracle docs | low | |
| Certifications | Certifications | text | V (TCNJ: skip) | yes (min 0-10) | Taleo | low | Standard fields only |
| Skills | My Experience | typeahead with checkbox | V | yes | Workday Penn State | low | |
| Languages and proficiency | My Experience | dropdown per skill | V | yes | Workday Penn State; SuccessFactors EASA | low | Five sub-ratings plus "native" (Workday); CEFR self-assessment (EASA) |
| Websites or links | My Experience | text (URL) | O | yes | Workday | low | McGill: link a drive when files exceed 5 MB |
| Legally authorised to work | Application Questions | dropdown or radio | V | no | Workday | personal | Employer and job specific |
| Require sponsorship | Application Questions | dropdown | V | no | Workday Penn State | personal | |
| Age 18 or over | Application Questions | dropdown | V | no | Workday Penn State | personal | |
| Screening or job-specific questions | Application Questions | text, number, date, multiple choice, file | V | varies | all four | low or personal | Workday: five types, up to 50 per questionnaire |
| Office-suite self-rating | Application Questions | dropdown | V | no | Workday McGill | low | |
| Retirement-system membership | Application Questions | dropdown with conditional follow-up | R (Penn State) | no | Workday Penn State | personal | |
| Gender | Voluntary Disclosures | dropdown | O (Penn State) | no | Workday; Oracle docs | sensitive | Oregon marks some as required |
| Race/Ethnicity | Voluntary Disclosures | checkboxes | O; Oracle US "must not be required" | no | Workday; Oracle docs | special | |
| Veteran Status | Voluntary Disclosures | dropdown | O | no | Workday; Oracle docs | sensitive | US only |
| Disability status | Self Identify | radio | O; Oracle US "can't be required" | no | Workday; Oracle docs | special | Typed name and date |
| Equity and diversity survey | Application Questions | multiple | O (McGill) | no | Workday McGill | special | |
| Other diversity fields (date of birth, marital status, religion, sexual orientation, pronouns, national ID, birth place) | Candidate personal info | various | N/D | no | Workday and Oracle admin docs | special | Offered fields depend on requisition country |
| National ID, government IDs, date of birth, citizenship | Post-offer task | text, dropdown | R on offer | no | Workday McGill, Penn State | special | After offer, not on the application |
| Terms and conditions or consent | Voluntary Disclosures; sign-off | checkbox | R | no | Workday, Taleo, SuccessFactors | low | |
| Typed signature and date | Self Identify, Review, Statement of Agreement | text and date | R | no | Workday Penn State; Taleo Richmond; SuccessFactors Toronto | low | |
| Work, location, organisational preferences | Work Preferences | multi-select | V | yes | Taleo Vanderbilt | low | "Add to list" click needed |
| Public Records Questionnaire, source tracking, diversity | Application | various | V | no | Taleo Vanderbilt | low to special | |
| References | References | text | V | yes (min 0-10) | Taleo Vanderbilt; Workday later task | personal | |
| Background check consent, address history, military experience | Compliance | checkbox, text | V | yes (address history) | Taleo block list | sensitive | Oracle recommends early consent |
| Shift availability grid | Availability | grid | V (hourly roles) | no | Taleo block list | low | Five shift periods, fixed days, profile level |
| Social sign-in profile | Account | OAuth | O | no | Workday docs, iCIMS | personal | |

## Per-job versus reusable

- **Reusable:** name, contact, address, phone with country code, work history, education, languages, skills, certifications, websites, the resume file. Workday "Use my last application", SuccessFactors saved profile and iCIMS profile carry these forward. EASA: the profile is "the same for all vacancies".
- **Per job:** screening questions, work authorisation and sponsorship (wording and country change), per-job cover letter, free-text answers, declarations and typed signature plus date (Penn State: some fields "required for EVERY NEW application"), "how did you hear", "previously affiliated", tailored Role Description.
- **Reusable but not stored by default:** sensitive and special rows above (demographic, disability, veteran, national ID): "asked each time", per FEAT-017.

## Copy-and-paste obstacles

- **Typeaheads needing an exact pick:** Workday School, Field of Study, Skills, "How did you hear". Intel guide fallback: "Other" then Enter. An NVIDIA forum thread (weak) reports an applicant unable to change Field of Study after a wrong pick. A pasted string may not be accepted.
- **Chained dropdowns:** source then sub-category; phone code list with radio buttons.
- **Repeating entries are added one at a time** (Add, Edit, Remove). No bulk paste.
- **Parse overrides:** parsed work and education need correction. McGill: do not parse academic CVs. Oregon: adjust inaccuracies. SuccessFactors merges salary, supervisor and reason for leaving into the description. A browser-extension vendor suggests "Apply manually" (marketing source). Not verified: a Blind post says people re-enter experience after parsing.
- **Paste bans:** PeopleSoft Fluid blocks pasting resume text (snippet, 2nd). No documentation found for Workday blocking paste. Oregon's guide recommends drafting long answers elsewhere and pasting.
- **Plain text only:** Taleo cover letter and Plain Text Resume lose formatting. Special characters anecdotally error on Workday work history.
- **Dates:** month-and-year pickers or typed fields; formats not specified in any source read.
- **File limits:** McGill 5 MB combined; Toronto DOCX, PDF, image, text only (no MSG, PPT, XLS); Guelph resume and cover letter as one file; iCIMS limits undocumented.
- **Character limits:** none documented. Oracle allows minimum characters on Plain Text Resume and Cover Letter blocks; maxima unconfirmed.
- **Session timeouts:** Workday docs: "Workday doesn't preserve the status of your session or resume a timed-out session"; length is tenant-set; University of Nevada page describes internal worker sessions, not candidates. EASA (SuccessFactors) warns information "cannot be saved" after timeout; an SAP KBA preview mentions 25 minutes inactivity. Oregon: "Save and Continue early and often". Third-party claim (unverified): a stale session can submit silently and lose data.
- **Forced re-entry:** repost while a draft is open (Oregon); Taleo "Add to list" or the entry is not kept, and nothing is entered until Submit; Workday submitted applications cannot be edited or reapplied (McGill); Taleo accounts are per employer.
- **Mandatory-field traps:** EASA's workaround is dummy data.
- **Account walls:** every system wants an account before submit; Oracle Easy Apply uses an emailed one-time code.
- **Mobile:** SuccessFactors Mobile Apply only; nothing found on Workday or Taleo phones.
- **Bot and CAPTCHA:** not seen (no live forms opened).

## What could NOT be found

- Any live employer form on the four systems.
- Candidate-side session timeout lengths for Workday and iCIMS.
- Character limits for any field; exact Workday date format; Workday paste behaviour.
- iCIMS required-field lists, file limits, field types.
- Oracle Recruiting Cloud's full sections-and-blocks list and what Express Apply and resume parse fill.
- Whether Taleo parsing uses a third-party service (blog claim, unconfirmed).
- SAP standard application-template field list (login required).
- Singapore-specific variants (NRIC, nationality, race on these systems). Nothing from a Singapore employer read.
- Cornerstone, Phenom, Avature; phone behaviour except SuccessFactors Mobile Apply.

## Limitations

- No live-form access; every field list comes from HR job aids and vendor docs, so "required" status reflects one employer's template.
- Many PDFs undated; some old (Vanderbilt 2010, Toronto 2019). Screens have since changed.
- Vendor docs are admin-facing: what can be configured, not what a candidate sees.
- SAP knowledge-base articles were preview-only.
- Some search claims could not be confirmed on a fetched page (Taleo third-party parsing, 30 to 60 minute Workday timeouts, silent session-expiry submits) and are reported as unverified or left out.
- Some pages were read as summarised by the fetch tool; label wording may differ slightly.
- Nothing here is Singapore-specific: guides come from the US, Canada and EU. Capped at N2.

## Implications for a store-filter-copy tool (observations, not decisions)

1. The stable block is small and matches FEAT-016 closely: name, contact, address, phone with country code, work entries, education entries, languages, skills, websites, resume file. Gap: forms do not ask for FEAT-016's "Employment type", "Key achievements" or "Skills used", while they do ask for "How did you hear", language sub-ratings, part-time percentage and a "native language" flag that FEAT-016 does not model.
2. Work and education repeat as separate entries with fields copied one at a time; a per-entry, per-field copy matches what employers ask.
3. Per-job text is where retyping costs most (screening answers, work-authorisation wording, cover letters, "why this role"). A per-job store plus "recently used" maps to Workday's "Use my last application".
4. Exact-option fields are the likely failure (School, Field of Study, Skills, Degree, "How did you hear"). A store could keep the typeahead search text, not only the display value.
5. Dates need a month-year form and a free-text form; "I currently work here" is a checkbox, not a copyable value.
6. Resume and cover letter are files, not text; size and type limits matter for the stored file; a "resume plus cover letter" combined variant may be needed.
7. Role Description, cover letter and plain-text resume are plain text; stripping formatting and special characters may avoid known problems.
8. Timeouts and no-resume-after-timeout mean the copy source must stay open and the user may re-copy; short fields with one click each suit this better than a whole-form paste.
9. Sensitive fields (gender, race, veteran, disability, national ID) are mostly optional but sometimes required; offer stage asks national ID and date of birth. Supports "asked each time, not stored" and implies a rule for the post-offer stage.
10. Singapore fit unknown from this run.
11. Phone copy between a tool and an employer form (two apps or tabs) is untested.

**Gaps for the decision gate:** a live-form check on at least one Workday and one iCIMS employer form (ideally Singapore-based); exact Workday date format and character limits; session timeout lengths; paste behaviour on Workday and SuccessFactors.
