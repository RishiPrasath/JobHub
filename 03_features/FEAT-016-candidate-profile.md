---
id: FEAT-016
title: Candidate profile
type: feature
scope: candidate
need_level: N0
feasibility_level: T0
result: none
opportunity: [OPP-005, OPP-006, OPP-008]
needs: [S-16]
findings: []
riskiest_assumption: ASM-016
decision: null
updated: 2026-11-10
---

# Candidate profile

Levels are provisional and await owner review. **The field list is a proposal for the owner to confirm.**

## What it does

When a user creates an account, JobHub captures their candidate details once: personal particulars, a short description of themselves, work experience, qualifications and skills. Reviews, comparison, resume work and application answers then use this profile instead of asking again.

Origin: [source idea](source-ideas/03_candidate-profile-and-preferences.md).

## Fields captured at account creation

**Required at sign-up (owner decision, 2026-11-10):** the minimal personal details, at least one work experience entry and at least one education entry. Everything else is optional. "Required" in the tables below means required within an entry that the user adds, or required in section 1.

**Resume upload (owner decision):** a resume can pre-fill the profile. The user reviews and confirms every parsed field before it is saved.

**Job preferences are not part of this feature.** The owner has deferred them to a separate initial-setup feature, where the user selects preferences such as remote or office-based, part-time or full-time, and seniority. That feature is not yet written.

### 1. Personal particulars

| Field | Type | Required |
|---|---|---|
| Full name | text | Required |
| Preferred name | text | Optional |
| Email | text | Required |
| Phone (with country code) | text | Optional |
| Current city and country | text | Required |
| Right to work (citizen, permanent resident, pass type, or needs sponsorship). Captured now; how it is used is to be decided. | choice | Optional |
| LinkedIn URL | url | Optional |
| Portfolio or website URL | url | Optional |
| Other links (GitHub, publications) | list of url | Optional |

### 2. About me

| Field | Type | Required |
|---|---|---|
| Headline (current or target role) | text | Optional |
| Summary (a few sentences about background and goals) | text | Optional |

### 3. Work experience (one entry per job, any number)

| Field | Type | Required |
|---|---|---|
| Job title | text | Required |
| Employer | text | Required |
| Employment type (full-time, part-time, contract, internship, freelance) | choice | Optional |
| Location | text | Optional |
| Start date (month and year) | date | Required |
| End date, or "I currently work here" | date or yes/no | Required |
| Description of the role | text | Optional |
| Key achievements | list of text | Optional |
| Skills used | list | Optional |

### 4. Education and qualifications (one entry each)

| Field | Type | Required |
|---|---|---|
| Institution | text | Required |
| Qualification (degree, diploma, certificate) | text | Required |
| Field of study | text | Optional |
| Start date and end date (or expected) | date | Optional |
| Grade or GPA | text | Optional |

### 5. Certifications and licences (one entry each)

| Field | Type | Required |
|---|---|---|
| Name | text | Required |
| Issuing body | text | Optional |
| Date issued and expiry date | date | Optional |
| Credential ID or URL | text | Optional |

### 6. Skills and languages

| Field | Type | Required |
|---|---|---|
| Skills (list of names) | list | Optional |
| Skill level (basic, working, advanced) | choice | Optional |
| Languages and proficiency | list | Optional |

### 7. Projects (one entry each)

| Field | Type | Required |
|---|---|---|
| Title | text | Required |
| Role | text | Optional |
| Dates | date | Optional |
| Description and outcome | text | Optional |
| URL | url | Optional |
| Skills used | list | Optional |

### 8. Resume

| Field | Type | Required |
|---|---|---|
| Resume file (PDF or DOC); pre-fills sections 2 to 6 after user review | file | Optional |

## Not collected

These are left out by default. Singapore guidance (TAFEP, PDPC) says application forms should not ask for them, and no JobHub feature needs them.

Date of birth or age, NRIC / FIN / passport number, gender, race, religion, marital or family status, disability or health, photograph, National Service status, salary history, criminal record, CPF or bank details.

## Evidence for

- Every job portal researched (LinkedIn, Indeed, Glassdoor, ZipRecruiter, Wellfound, Welcome to the Jungle, JobStreet, MyCareersFuture) captures contact details, work history, education and skills.
- Employer application forms (Greenhouse, Lever, SmartRecruiters, Workable, Workday, Taleo) ask for the same items, as repeating work and education entries. A saved profile addresses re-typing (S-16).

## Evidence against

- No user has been asked what they will enter at sign-up, so this is N0.
- Required versus optional is almost never documented by portals, so the tolerable minimum is unknown.
- FEAT-010 (profile comparison) failed its fixture test (FND-E03-01).

## Open questions for the owner

1. Requiring a work experience entry would block first-time job seekers and fresh graduates. Should there be a "no work experience yet" option?
2. How will right to work be used? It is captured now, but nationality questions are a grey area in TAFEP guidance, so the use needs deciding before it affects any review.
3. Where is the profile stored, and for how long? This is a privacy and architecture decision.

Decided 2026-11-10: required fields (minimal details, work experience, education), resume pre-fill with full user review, capture right to work, and defer job preferences to a separate feature.

## Research basis

Desk research on 2026-11-10 by four read-only specialists, using public pages only. Sources include [LinkedIn](https://www.linkedin.com/help/linkedin/answer/67405), [Indeed](https://www.indeed.com/help/job-seekers/articles/32603395892109-adding-or-editing-job-search-preferences) and [Wellfound](https://help.wellfound.com/article/773-how-do-i-edit-my-candidate-profile) help pages, the MyCareersFuture FAQ, [TAFEP form guidance](https://www.tal.sg/tafep/employment-practices/recruitment/preparing-job-application-forms), the [PDPC NRIC guidelines](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/Advisory-Guidelines-for-NRIC-Numbers---310818.pdf), ATS developer docs, and the JSON Resume schema.

Gaps: Glints, FastJobs, Carousell, agency registration forms, iCIMS and BambooHR could not be verified. Sign-up screens behind logins were not seen. The raw research notes are not saved in the repository.

## Next test

Riskiest assumption: people will fill in this profile at sign-up. Test: have participants complete it, time it, and note which fields they skip or refuse.
