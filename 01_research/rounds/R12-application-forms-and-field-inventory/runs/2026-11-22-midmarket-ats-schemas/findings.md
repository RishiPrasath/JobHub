# Run B findings: Mid-market and startup ATS application forms

Run date: 2026-11-22. Role: Technical Architect (#08). Read-only: GET requests to public endpoints and viewing public apply pages. Nothing typed, submitted, signed in or created. The subagent could not write files, so the round lead saved this from its returned report.

Evidence labels as in the [round brief](../../round-brief.md). Capped at N2. Snapshot of 2026-11-22.

**Inspected:** Greenhouse board API (`?questions=true`) for 8 boards (airbnb, stripe, anthropic, gitlab, figma, databricks, coinbase, dropbox; 48 postings; Airbnb and Stripe Singapore read in full) plus one hosted page DOM; Lever public postings and `/apply` pages (Palantir Singapore, Spotify US, Lever demo); Ashby rendered `/application` pages (Ramp, Notion, Linear, Airwallex Singapore); SmartRecruiters Bosch Singapore Easy Apply step 1; Workable public `/api/v1/jobs/{shortcode}/form` JSON (YouTrip, Fuku, Secure IQ, Keywords Studios, Royal Ocean, all Singapore, plus one more); Recruitee (bunq 23 offers); Teamtailor and vendor docs.

**Not touched:** Ashby GraphQL form endpoint (a POST). SmartRecruiters configuration endpoint (401, no token). BambooHR (non-JSON). Several guessed board names returned 404.

**Prompt-injection note:** the Ramp apply page contains an in-form "decode this secret / prove you are not a bot" question; it was treated as a form field and not acted on.

## Standard field set per system

| System | Standard fields | Evidence |
|---|---|---|
| Greenhouse | First name, last name, email (text, required), phone (usually required), resume (file plus paste-text `resume_text`), cover letter (file plus `cover_letter_text`, usually optional), location group (text plus hidden latitude and longitude) only if enabled | API (V-site) |
| Greenhouse employer extras | LinkedIn (36 of 48 postings), Website, Pronouns (optional), Preferred First Name, "How did you hear" (16 of 48), "Additional Information", "Authorised to work" (18 of 48) | API (V-site) |
| Lever | Resume (auto-parsed on upload), full name, email, phone (admin-set), current location (autocomplete, 100 characters), current company, LinkedIn, GitHub, Portfolio, other links; pronouns checkbox and "Additional information" on some forms | HTML (V-site) |
| Ashby | "Autofill from resume" upload, name (single "Legal Name" or "Full Name", or First/Middle/Last at Airwallex), email, phone, location (some), resume, LinkedIn and links, cover letter (file or text, per form) | rendered pages (V-site) |
| SmartRecruiters | Easy Apply step 1: first name, last name, email, confirm email, city, country code plus phone, optional photo, LinkedIn, Facebook, X, Website, Experience and Education (repeating "Add"), Resume, "Message to the Hiring Team" | DOM (V-site) |
| Workable | Per-job Mandatory, Optional or Off: first name (127), last name (127), email (255), phone (255; +65 selector), address, headline (255), resume (12 MB; pdf/doc/docx/odt/rtf), cover letter (200,000 characters), summary, Education group (school, field_of_study, degree, start_date, end_date), Experience group (title, company, industry, summary, start_date, end_date, current) | `/form` JSON (V-site) |
| Recruitee | Name and email always on; per-offer switches for CV, cover letter, phone, photo, salutation (off, optional, required); preferred-work-location question. bunq: phone required, everything else off | API (V-site) |
| Teamtailor | Documented as 8 question types; standard fields not captured | help doc (V-site) |
| BambooHR, Jobvite, Breezy | Not obtained | none |

## Field inventory

Sensitivity: low, personal, sensitive, special. GH = Greenhouse, LV = Lever, AS = Ashby, SR = SmartRecruiters, WK = Workable, RC = Recruitee.

| Field label | Section | Input type | Required | Repeats | Seen in | Sensitivity | Notes |
|---|---|---|---|---|---|---|---|
| First name / Last name | Personal | text (255 GH, 127 WK) | req | no | GH all 48; WK all | personal | GH rejects URLs in name and phone fields. Ashby sometimes one "Legal Name"; Airwallex splits First/Middle/Last |
| Full name | Personal | text | req | no | LV Palantir, Spotify; AS Notion, Linear | personal | |
| Preferred first name | Personal | text | opt | no | GH Figma (15 of 48); LV Palantir ("Preferred Name", "Name Pronunciation") | low | |
| Email | Personal | email | req | no | all | personal | SR adds "Confirm your email" |
| Phone | Personal | tel plus country-code selector | req or opt | no | all | personal | SR separate country dropdown; WK +65 preselected |
| Location (city, country) | Personal | text (LV max 100, autocomplete with hidden lat/long); WK address prefilled from IP | req or opt | no | GH Airbnb, Stripe; LV; AS; WK | personal | Autocomplete needs a picked suggestion (LV, GH) |
| Current residential area | Personal | text (127) | req | no | WK Royal Ocean | personal | Singapore wording |
| Current company / employer | Work | text | req or opt | no | LV, GH Stripe, Figma | low | |
| Current or previous job title | Work | text | req | no | GH Stripe | low | |
| Resume/CV | Documents | file (GH pdf/doc/docx/txt/rtf; WK 12 MB) | req or opt | no | all | personal | GH and WK also allow paste-text or "Enter manually"; file must be non-empty (GH) |
| Cover letter | Documents | file or textarea (WK up to 200,000) | opt (GH 35 of 48) | no | GH, WK, AS Linear | personal | Per job |
| LinkedIn URL | Links | text (255) | opt | no | GH 36 of 48; LV; AS; SR; WK | personal | |
| GitHub / Portfolio / X / Facebook / other website | Links | text | opt | no | LV, GH, AS, SR | low | Linear requires a GitHub username |
| Pronouns | Personal | single-select or checkbox | opt | no | GH (8 of 48), AS Notion, LV Spotify | personal | |
| Experience (title, company, industry, summary, start/end date, current) | Profile | repeating group with dates | opt | yes | WK Keywords, Royal Ocean; SR "Add" | personal | |
| Education (school, field, degree, start/end date) | Profile | repeating group | opt | yes | WK Keywords; SR "Add" | personal | |
| University currently or last attended | Profile | dropdown (about 3,300 options) | req | no | LV Palantir | personal | Exact match ("Other" fallback) |
| Headline / Summary | Profile | text (255) / paragraph | opt | no | WK | low | |
| Authorised to work in country? | Eligibility | yes/no single-select | req | no | GH (18 of 48); AS; LV | personal | Wording varies |
| Require visa sponsorship? | Eligibility | single-select | req | no | GH Stripe, Anthropic, Airbnb; AS Notion | personal | |
| Singapore citizen / PR / other (EP, PEP, ONE Pass) | Eligibility | radio or dropdown | req | no | LV Palantir SG; AS Airwallex SG; WK YouTrip "Work Authorization Status" | sensitive | Singapore pattern; options vary per employer |
| Nationality / Country of citizenship | Eligibility | dropdown or text | req | no | WK YouTrip, Royal Ocean | sensitive | Exact option list |
| Notice period | Preferences | text (WK 127), textarea or dropdown | req | no | WK YouTrip, Royal Ocean, Keywords; AS Airwallex, Linear | low | Free format; units differ |
| Expected salary | Preferences | text or number | req | no | WK YouTrip (monthly/annually), Keywords (SGD per month), Royal Ocean; AS Airwallex ("include currency") | personal | Same value, different format each time |
| Last drawn base salary; bonuses | Preferences | text | req | no | WK YouTrip; Royal Ocean | sensitive | FEAT-016 "not collected" item that employers still ask |
| Willing to relocate / travel | Preferences | yes/no | req | no | GH Anthropic, Stripe; WK Royal Ocean | low | |
| Earliest start date | Preferences | text (255) | opt | no | GH Anthropic | low | Free text |
| Work-from-office or hybrid acceptance | Preferences | yes/no | req | no | GH Stripe, Anthropic; AS Notion | low | |
| Languages you can communicate in | Profile | multi-select | req | no | WK Royal Ocean; LV Palantir | low | |
| Why this company / role | Screening | textarea | req | no | GH Anthropic, Airbnb, Figma; LV Palantir (optional) | low | Per job |
| Proudest accomplishment | Screening | textarea | opt | no | LV Palantir | low | Per job |
| Describe a piece of work using AI tools | Screening | paragraph | req | no | WK YouTrip | low | Per job |
| Open-ended motivation ("500 words or less") | Screening | long text | req | no | AS Linear (3) | low | Word limit in question text |
| Code or puzzle anti-bot question | Screening | long text | req | no | AS Ramp | low | Deliberate automation obstacle |
| How did you hear about us? | Screening | dropdown (21 options Palantir; 9 bunq) or multi-select | req or opt | no | GH (16 of 48), LV, AS, RC | low | Employer-specific list |
| Worked here before / relatives employed here | Screening | yes/no plus conditional name | req | no | GH Airbnb, Figma, Anthropic; AS Airwallex; WK YouTrip | personal | Fits FEAT-017 "not stored, asked each time" |
| Non-compete / non-solicit | Screening | yes/no | req | no | GH Airbnb | personal | |
| AI-use / process policy acknowledgement | Consent | yes/no or checkbox | req | no | GH Anthropic, Airbnb; LV Palantir; AS Airwallex | low | |
| Arbitration / terms acknowledgement | Consent | single-select (one option) | req | no | GH Anthropic | low | |
| Privacy-notice consent (SG PDPA) | Consent | yes/no | req | no | GH Airbnb; WK YouTrip (four consent items: data, sensitive data, truthfulness, talent pool 24 months) | personal | Per employer, not reusable |
| SMS and WhatsApp consent | Consent | yes/no x 2 | req | no | AS Ramp | personal | |
| Gender | Demographic | single-select (Stripe SG: Male/Female/Decline) | opt (Stripe), req (Airbnb SG) | no | GH Stripe SG, Airbnb SG; AS Notion; LV | special | Airbnb SG pairs it with a consent question |
| Race / ethnicity | Demographic | single or multi-select, 7 options plus decline | opt | no | GH Figma US, AS Notion, LV Spotify | special | Not seen on any Singapore form |
| Veteran status | Demographic | single-select | opt | no | GH US-targeted postings; AS Notion; LV Spotify | special | US only |
| Disability / age range | Demographic | single-select | opt | no | LV demo ("age range") | special | Not seen live elsewhere |
| Classified by the Singapore Government as a (5 options) | Eligibility | single-select | req | no | GH Airbnb SG | sensitive | Likely citizenship or PR category; labels not recorded |

## Custom question types and how much of a form is custom

- **Greenhouse** (schema authoritative): `input_text`, `input_hidden`, `input_file`, `textarea`, `multi_value_single_select`, `multi_value_multi_select`. No date or number types, so numbers and dates arrive as text. Across 48 postings: 365 text fields, 341 single-selects, 112 textareas, 85 file fields, 34 multi-selects. Questions per posting: Anthropic 17 to 22, GitLab 13 to 22, Airbnb 19 to 30, Stripe 17 to 30, Figma 17, Databricks 14 to 18, Coinbase 21 to 24, Dropbox 18 to 21. Typical total about 17 to 22; 4 to 6 are fixed core, so roughly 70 to 80% are employer-chosen, with a recurring core of LinkedIn, work authorisation, sponsorship, "worked here before", "how did you hear".
- **Lever:** text, textarea, radio, checkbox groups, dropdowns (including 3,300 options). Palantir SG: about 12 custom items after 9 standard. Spotify and demo: 3 to 7 custom plus a 4 to 6 item survey block.
- **Ashby:** free text, long text, yes/no, single-select, multi-select, URL, file, conditional follow-ups. About 8 (Notion, before EEO) to 17 (Ramp) to 15 (Airwallex). `isRequired` default true; beta conditional visibility. Full type list unread.
- **SmartRecruiters** (documented): `INPUT_TEXT`, `SINGLE_SELECT`, `MULTI_SELECT`, `RADIO`, `CHECKBOX`, `TEXTAREA`, `INFORMATION`. Repeatable questions; `complianceType: DIVERSITY`; conditional questions one level, SINGLE_SELECT parents only.
- **Workable:** docs list `free_text`, `multiple_choice`, `boolean`, `dropdown`, `numeric`, `date`, `file`; live JSON showed `text`, `paragraph`, `boolean`, `dropdown`, `number`, `multiple`, `group`. Field counts on six Singapore forms: 5, 6, 17, 26, 27. Custom questions are all mandatory.
- **Recruitee** (bunq, about 400 questions): `single_choice` 207, `infobox` 114 (display only), `string` 45, `boolean` 30, `text` 4, `multi_choice` 1. 16 to 21 question objects per offer; required defaults to true.
- **Teamtailor:** Choice, Date, File, Number, Range, Text, Video, Yes/No; Range and Yes/No always mandatory.

## Per-job versus reusable

- **Stable across jobs:** name, email, phone, location, LinkedIn, GitHub, portfolio, website, resume file, pronouns, preferred name, current employer and title, Experience and Education groups, languages, authorisation and sponsorship status, notice period, relocation or travel willingness.
- **Reusable but format-sensitive:** expected salary (currency, unit), last drawn salary, notice period (weeks, months, text), earliest start date, "how did you hear" (option list varies).
- **Per job or employer:** cover letter, "why this role", accomplishment prompts, AI-use or policy acknowledgements, privacy and PDPA consents, arbitration or terms acknowledgements, talent-pool opt-ins, role-specific yes/no experience questions, "worked here before", "relatives here".
- **Question libraries:** Workable keeps forms per job (cloning copies custom questions); Greenhouse per job post; Teamtailor has a company question library; Recruitee and Lever not documented here.
- **Demographic:** employer decides whether to show it; applicant decides each time whether to answer. GH `demographic_answers` documented as always optional.

## Copy-and-paste obstacles

- **Exact-option dropdowns:** Lever university (3,300, "Other" fallback), nationality lists (Workable, about 200), country lists (Stripe 31), work-authorisation lists. Stored text rarely matches an option label exactly.
- **Yes/no single-selects:** GH 341 single-selects, Lever radios, Workable booleans.
- **Combobox widgets:** Greenhouse hosted page renders 12 comboboxes without native select; a pasted value does not select an option.
- **Phone:** separate country-code selector plus number (GH, SR, WK); a stored international number needs splitting.
- **Location autocomplete:** LV and GH need a clicked suggestion (hidden lat/long); pasted text alone does not satisfy the field.
- **Character limits:** GH short text 255; WK name 127, email and phone 255, notice and salary 127, cover letter 200,000; LV location 100; Linear "500 words or less" only in question text; GH textarea no limit on the page inspected.
- **File-only fields:** GH pdf/doc/docx/txt/rtf (also Dropbox, Google Drive); WK also odt, 12 MB. GH and WK offer paste-text alternative.
- **Resume parse:** Ashby, Workable, SmartRecruiters (Easy Apply with Indeed and SEEK), Lever all pre-populate after upload; the user still reviews.
- **Anti-bot controls:** Lever hCaptcha slot; Ramp code-puzzle question; Greenhouse API doc recommends `country_short_name` for fraud detection.
- **Dates:** Workable structured date fields with "I currently work here"; Greenhouse has no date type.
- **Conditional fields:** Airwallex "If Yes, please state their name"; SR conditional questions. A flat store gives no sign a field appears only after another answer.
- **Rich text:** none on the Greenhouse hosted page (0 contenteditable); plain textareas. Others not checked.

## What could NOT be found

- BambooHR, Jobvite, Breezy forms or schemas (BambooHR lists custom question types from one marketing page only).
- Lever Help Center text (page failed to load); Lever's public API does not expose custom questions.
- Ashby's full type list and EEO docs (read first 100,000 of 167,696 characters).
- SmartRecruiters screening step and diversity questions on a live form.
- Greenhouse demographic blocks beyond API output (US: EEOC blocks of veteran status, race, gender; no disability seen; Singapore: Stripe gender only).
- Workable demographic or EEO fields on Singapore forms: none seen. Singapore age or race questions: none seen other than gender.
- Teamtailor and Recruitee live applicant forms.
- Lever required flags inferred from HTML attributes and asterisks.
- Sample sizes: 3 Lever, 4 Ashby, 1 SmartRecruiters, 6 Workable, 1 Recruitee tenant; not representative.

## Limitations

- N2 cap. Snapshot of 2026-11-22; employers change forms.
- Samples skew to well-known tech employers and a few Singapore employers; lower-wage, shift and gig employers largely absent.
- Counts describe those 8 Greenhouse boards only.
- Workable live JSON type names differ from reference docs; live JSON treated as better evidence. The `/form` endpoint is undocumented in the vendor reference; stability unknown.
- Sensitivity labels are judgement against FEAT-016 and FEAT-017 lists, not legal classification.
- Required or optional is "as seen" and may change per employer.
- No data was entered, so validation rules, conditional logic after answering and per-field errors were not seen.

## Implications for a store-filter-copy tool (observations, not decisions)

1. A stable core covers most fields on most forms (name, email, phone, location, LinkedIn, resume, current employer, authorisation, sponsorship, notice period), each with format variants.
2. The same fact is asked in many shapes. Work authorisation appears as yes/no, citizen/PR/other, a 5-option government classification, a dropdown with "Work Visa", and a separate sponsorship question. A store would need several phrasings per fact or a short and long value with an option-label hint.
3. Exact-option dropdowns cannot take pasted text; copying helps only when the user picks from a list. The store could show the option label to select, not a string to paste. Large lists (3,300 universities, about 200 nationalities) are worst.
4. Free-text fields have employer-specific limits and units (notice in weeks, salary monthly or annual with currency, 255 caps). Unit-tagged values and a character count beside each snippet may help.
5. Repeating groups with dates (Workable, SmartRecruiters) match FEAT-016 work and education entries; one copy action per field per entry.
6. Per-job answers are a minority but the hardest part (cover letter, "why this company", accomplishment, AI-use). They need a per-job saved answer, matching the owner's "per job" filter.
7. Consent and policy items (PDPA, arbitration, talent pool, SMS) are per employer and not reusable; YouTrip alone has four. Storing them has little value and some risk.
8. Sensitive items appear: last drawn salary and bonus (FEAT-016 "not collected"), nationality, citizenship, gender, race, veteran status, "relatives here", "worked here before". Singapore demographic blocks were gender-only (Stripe) or gender paired with consent (Airbnb); race and veteran blocks were US-targeted. This lines up with the "not stored by default" list.
9. Phone behaviour of selectors and autocompletes was not tested.
10. Greenhouse `?questions=true`, Workable `/form` and Recruitee `/api/offers` are machine-readable and public; Lever, Ashby and SmartRecruiters expose forms only on rendered pages. Reading these at scale is outside this round's manual read-only scope and is a decision for the owner and Responsible AI Reviewer.
