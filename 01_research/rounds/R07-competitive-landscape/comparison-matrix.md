# Round 07 comparison matrix

Research date: 2026-10-28

This matrix normalises public product documentation. “Observed” means documented on an official page, not authenticated hands-on testing. Prices are public USD figures unless otherwise noted and may vary by region, promotion, app store or checkout.

## Market comparison

| Product | Profile capture | Matching signals | User process | Automation and control | Public candidate pricing | Strengths | Weaknesses / limits |
|---|---|---|---|---|---|---|---|
| LinkedIn | Profile fields, resume upload, titles, locations, work setting and employment preferences | Profile, preferences, network/recruiter signals and some engagement | Profile → search/alerts → recommendations → Easy Apply or external ATS → partial tracking | Easy Apply and drafting; user submits; some applications leave LinkedIn | Free core; Premium Career publicly starts around US$39.99/month or US$239.88/year; Singapore price not verified | Rich professional identity and recruiter graph | Opaque ranking, profile completeness dependence, external ATS fragmentation, limited post-submit correction |
| Indeed | Resume upload/build/import, work history, education, skills, licences, pay, schedule, location and work-setting preferences | Profile, preferences, searches, opens, saves, dismissals and applications | Resume/profile → preferences → recommendations/alerts → native or external apply | Personalised discovery; user applies; native status is better than external | Core job-seeker access free; no current consumer subscription verified | Broad job distribution, explicit preferences, resume parsing | External applications lose status visibility; searchable data may be copied; stale parsing/preferences |
| MyCareersFuture / CareersFinder | Profile, resume, user-entered skills, competencies, work experience and career quiz/profile analysis | Job description skill extraction compared with profile/resume; local occupation and course context | Browse → Singpass/profile → search → screening questions → apply → Applied Jobs | Transparent-ish job-fit percentage; user applies; employer download drives “Under Review” | No consumer subscription identified; free for eligible Singapore Citizens/PRs | Singapore-specific, salary ranges, government support, local skills context | Singpass/eligibility boundary, format limits, portability unclear, score can reflect incomplete profile |
| Jobstreet by SEEK | Resume parsing, history, education, skills, licences, languages, salary expectations, locations, work type, availability and visibility | Profile, search/save/apply activity and reported application outcomes | Profile → visibility → recommendations → apply/contact → partial tracking | Employer discovery and credential signals; user controls visibility | Candidate subscription not found in reviewed pages | Singapore/APAC schema, credential verification, granular visibility | Public visibility exposure, external ATS status gaps, algorithm and employer-activity opacity |
| Jobright | Resume/profile, target role/preferences, skills, seniority, industry, location, salary and remote preference | Resume/profile to job matching, fit scores, role sources, possibly network/referral signals | Resume → personalised feed → fit explanation → tailored documents → autofill/possible agent submit | Public pages conflict: manual review in one workspace, autonomous agent claims elsewhere | Consumer pricing not verified; employer pricing was surfaced instead | Integrated discovery, fit explanation, tailoring, referrals and automation | Conflicting product/privacy claims, unclear price and Singapore coverage, outcome claims unverified |
| Teal | Resume import, multiple versions, saved jobs, descriptions, statuses, notes, contacts, documents | Keywords and skills in job description versus selected resume | Save job → tracker → matcher → tailor resume/cover letter → manual apply → follow up/interview | Strongly user-reviewed; no auto-submit documented | Free core; Teal+ US$13/week, US$29/month or US$79/quarter | Traceable job/resume tracker, clear review boundary, export | Keyword optimisation can become superficial; Singapore coverage unconfirmed; web/extension orientation |
| Careerflow | PDF/Word resume, LinkedIn import, profile, contacts, tasks, notes | Resume/job keywords, ATS score, LinkedIn sections, skill gaps and newer job-portal matching | Import → optimise LinkedIn/resume → save/search → autofill → external apply → track/network/interview | Assistive autofill; user reviews and submits | Free; public pages show figures such as US$23.99/month Premium and US$44.99/month Premium Plus, but pricing pages conflict | Broad toolkit across profile, networking, tracking and interviews | US-only job portal evidence, inconsistent pricing/features, advertising/session-replay privacy signals |
| Jobscan | Resume upload/paste, LinkedIn import, preferences and AI Coach questions | Job-specific keywords, skills, titles, experience and ATS-style score | Resume → paste job → scan → edit/tailor → tracker → apply | Review-before-submit documented for Auto Apply; runtime not independently tested | Free limited use; official content reports about US$49.95/month or US$89.95/quarter; checkout not verified | Strong job-specific ATS comparison and tailoring | Score is a proxy, pricing/checkout uncertainty, non-US support unclear, outcome claims unverified |
| Rezi | Manual entry, PDF/DOCX import, LinkedIn Chrome import and resume versions | Rezi Score, job keywords and ATS-oriented suggestions | Import/create → tailor → export → AI interview practice | User edits/downloads; no general auto-submit found | Free; Pro US$29/month; Lifetime US$149 | Clear document workflow, versioning and interview bridge | Job discovery/tracking less mature; score can encourage number optimisation; AI-provider details limited |
| Kickresume | Manual creation, PDF/DOCX import, LinkedIn import and templates | ATS checker, keywords, AI writing and career-map signals | Import/create → resume/cover letter/site → ATS check → interview questions | Primarily document creation and review | Free; Premium US$24/month, US$54/quarter or US$96/year | Strong presentation/document tools, career map, interview support | More document-centric; application tracking evidence limited; AI data handling requires review |
| Huntr | Resume/profile/documents, LinkedIn import, job clipper, contacts and preferences | Basic/advanced matching, keyword finder, job-description terms | Clip job → board/status → tailor docs → autofill/contact → track/follow up | Autofill and editing; no auto-submit documented | Free; Pro US$40/month, US$90/quarter or US$160/6 months | Strong tracker, contacts, job/document linkage, export | High paid price, free limits, older privacy documentation, LinkedIn freshness/cache issues |
| Simplify | One reusable profile from manual entry or resume upload; experience, education, skills, work authorisation, answers and documents | Profile, preferences, activity and postings from 50+ boards/company pages | Profile → matches → tailor docs → Copilot/Autopilot → tracker → follow up | Copilot requires review; Autopilot submits supported applications without per-app review | Free core; Simplify+ US$19.99/week, US$39.99/month or US$89.99/quarter | Clearest assisted-versus-autonomous split, integrated profile/documents/tracking | Singapore absent from public matching-country list, no-review risk, unsupported-form and stale-answer risk |
| Sonara | Signup plus resume, work history, preferences, salary and target roles | Preferences and salary/location/role filters; detailed ranking evidence not public | Profile → curated queue → delete/modify unwanted jobs → service applies | Highest apparent automation; per-application review requirement unclear | Current consumer price not publicly clear; terms describe paid subscriptions | Reduces search effort and applies on user’s behalf | U.S.-focused, opaque pricing, limited evidence on tailoring/quality/failure recovery, brand continuity uncertainty |

## Process archetypes

### 1. Job-board recommendation loop

```text
Create profile/resume
    → set preferences
    → search, click, save, dismiss or apply
    → recommendations and alerts adapt
    → apply natively or leave for an external ATS
```

Examples: LinkedIn, Indeed, MyCareersFuture, Jobstreet.

### 2. Resume-to-posting optimisation loop

```text
Import resume
    → paste or capture job posting
    → calculate keywords/skills/ATS proxy
    → tailor documents
    → user reviews and applies
```

Examples: Jobscan, Rezi, Kickresume, Teal.

### 3. Application workspace loop

```text
Capture job
    → keep role, source, status and contacts together
    → attach a role-specific resume
    → track follow-ups and interviews
```

Examples: Huntr, Teal, Careerflow.

### 4. Application automation loop

```text
Build reusable profile
    → find supported roles
    → generate answers/documents
    → autofill or submit automatically
    → track outcome
```

Examples: Simplify, Sonara and Jobright’s advertised agent experience.

## Cross-cutting observations

- Candidate profiles and resumes are related but not identical objects.
- Preferences commonly include role, location, schedule, compensation and work arrangement.
- Behavioural signals—searches, clicks, saves, dismissals and applications—are commonly used, but ranking weights are opaque.
- Matching is usually a keyword, skills, ATS or fit score rather than a validated hiring prediction.
- Free access is common; paid tiers monetise higher limits, AI generation, advanced matching, interview support, visibility or automated application volume.
- User-control boundaries vary more than feature lists: recommendation, drafting, autofill, reviewed submit and autonomous submit are materially different products.
- External ATS handoffs create a recurring status and provenance gap.
- Export and deletion exist in some products, but re-import fidelity, employer copies and third-party retention are often unknown.
- No product reviewed publicly established verified Singapore job-matching coverage across the AI-first category.
