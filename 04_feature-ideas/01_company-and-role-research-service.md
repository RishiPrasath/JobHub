# Feature idea: Company and role research service

## Status

Proposed

## Locked direction — 2026-10-29

This service should include hiring-process and workplace due diligence, not only a static company summary. It should investigate, where public evidence allows:

- whether the vacancy appears active and serious;
- how long the role has been open or repeatedly reposted;
- whether similar roles suggest turnover or role instability;
- whether the posting matches the company’s actual work;
- whether duties, pay and expectations remain consistent; and
- whether the employer communicates clearly and provides enough information before asking for commitment.

The output should provide evidence, possible explanations and questions to verify. It should not produce a universal company-risk score.

## User problem

A job seeker may understand the text of a job posting but still lack important context about the company, the role and the working conditions. Researching that context manually can take significant time, especially when the job seeker is trying to determine whether the opportunity fits their preferences, likes and dislikes.

## Proposed feature

Create a public-source research service that investigates a company and a specific role, then presents evidence-backed answers to important questions for the job seeker.

The service could collect and organise information about:

- what the company does;
- who appears to be hiring;
- how the role relates to the company’s work;
- what the company publicly says about its culture and working style;
- whether the role, location, schedule and compensation match the user’s stated preferences;
- what information is missing, inconsistent or worth verifying;
- whether observable signals are meaningful for this particular job seeker.

The service should distinguish public-source observations from interpretation. A signal may matter to one person and not another.

## Research dimensions

The service should research the company and role through a question-led checklist rather than produce a generic company summary.

### 1. Company identity and operating context

- What is the legal or publicly stated company name?
- Do the employer name, application contact and company website appear consistent?
- What does the company say it does, sells or supports?
- Which markets, customers or locations does it publicly serve?
- Does the company appear to be active, dormant, recently established or changing direction?
- Are the job posting and company sources describing the same organisation?
- Is the role posted by the direct employer, a recruitment agency, a staffing intermediary or an unclear party?

### 2. Company activity and role relevance

- Does the advertised role connect clearly to the company’s stated business?
- Can the role’s likely team, product, service or operational area be identified?
- Does the company appear to have similar roles or an established function for this position?
- Is the role a new position, a replacement, an expansion role or unknown?
- Are the responsibilities consistent with the company’s size and operating context?

### 3. Culture and working practices

Research the difference between what the company claims and what can be supported by attributable evidence.

- What working values does the company publicly describe?
- What do public employee or candidate accounts repeatedly mention about management, workload, communication, training and psychological safety?
- Are working hours, flexibility, remote or on-site expectations clear?
- Does the role appear to involve high autonomy, close supervision, shift work, travel, on-call work or unpredictable hours?
- Are there signs of a learning environment, structured progression or limited support?
- Are culture claims specific and evidenced, or only generic employer-branding language?

The service should label culture findings carefully. A small number of reviews or promotional statements cannot establish the complete culture of an organisation.

### 4. Role context and day-to-day reality

- What work is likely to occupy most of the person’s time?
- Who might the person report to or work with?
- What outputs, targets, customers, equipment or systems are involved?
- Which duties are explicit, implied or missing?
- What qualifications, licences, tools or experience are genuinely required?
- Are the title, seniority, pay and responsibilities consistent with one another?
- Does the role look like one job or a combination of several jobs?
- What is likely to be difficult, stressful, physical, repetitive or unpredictable?

The system must distinguish a source-backed description from an inference about daily work.

### 5. Hiring seriousness and vacancy intent

The service should investigate whether the company appears to be actively hiring, without claiming that it can prove intent from public data alone.

Possible signals include:

- how recently the posting was published and whether it remains open;
- whether the closing date is repeatedly extended;
- whether the same role appears across several boards for a long period;
- whether the company has a coherent application route;
- whether the role appears on the company’s official careers page;
- whether the company has recently posted related openings;
- whether the posting contains specific duties, a real location and a named hiring process;
- whether the role appears to be continuously reposted with little change;
- whether the employer responds to applicants or provides meaningful next steps, where public evidence exists;
- whether the role may be an evergreen listing, talent-pool listing, pipeline role or genuine immediate vacancy.

Possible interpretations must remain separate:

```text
Observed: The same role appears with similar wording across several dates.
Possible meanings: Ongoing hiring, reposting, high turnover, or an evergreen listing.
What to verify: Ask whether there is an active vacancy and what the expected start date is.
```

### 6. Workforce stability, layoffs and organisational change

Where reliable public evidence exists, the service could research:

- announced layoffs or workforce reductions;
- repeated restructuring, acquisitions or business closures;
- changes in leadership or operating model;
- hiring freezes or rapid hiring expansions;
- repeated reports of high turnover or short tenures;
- whether layoffs affected the team, location or function relevant to the role;
- whether the role may be connected to a replacement, cost reduction or business transition.

This area requires especially careful handling. A company having layoffs does not automatically mean that a job is unsafe or unsuitable. The meaning depends on timing, business area, location, role type and the user’s preferences.

For example:

```text
User preference: Stable employer and predictable long-term work.
Observed: Public reports describe recent restructuring in the relevant business unit.
Meaning: Worth asking about team stability, funding and the reason for the vacancy.
Not established: That the individual role will be eliminated.
```

### 7. Compensation and employment conditions

- Is the salary range clear and consistent across sources?
- Is the stated amount hourly, monthly, annual, commission-based or conditional?
- Are overtime, allowances, bonuses, commissions or deductions explained?
- Does the compensation appear consistent with the responsibilities and seniority?
- Are employment type, probation, benefits, leave and working hours stated?
- Are pay details deferred to the interview?
- Does the user have a minimum pay or stability preference that changes the importance of an unknown?

The service should preserve ranges and conditions rather than reduce them to a single estimated number.

### 8. Hiring process and candidate treatment

- Is the application process clear and proportionate to the role?
- Are candidates asked for unusual personal information or payment?
- Are there excessive unpaid tasks, unexplained trial work or unclear interview stages?
- Does the process involve a recruiter, agency or direct employer?
- Are interview expectations, decision timelines and communication channels clear?
- Does the process respect the user’s time, privacy and boundaries?

These findings should produce questions and caution, not a definitive employer label.

### 9. Fit with the individual job seeker

The research becomes meaningful only when the findings are compared with explicit preferences, likes, dislikes and constraints.

Examples include:

- preferred work schedule and availability;
- minimum compensation;
- commute and location limits;
- tolerance for shift work, weekends, travel or on-call work;
- preference for stability or rapid-growth environments;
- preference for direct employers over agencies;
- tolerance for ambiguity or changing responsibilities;
- desired management style and level of supervision;
- preference for customer-facing, physical, technical or independent work;
- willingness to work in a company experiencing restructuring;
- need for training, progression or formal support.

The output should say:

```text
This finding may matter because you said predictable weekday hours are important.
```

It should not say:

```text
This company is not suitable for you.
```

### 10. Evidence quality and research gaps

For every research area, the service should record:

- source type;
- source URL;
- publication or update date where available;
- date accessed;
- whether the source is official, attributable reporting, self-reported, anonymous or unverified;
- whether the finding is direct evidence, a repeated pattern, an interpretation or an unknown;
- contradictory evidence;
- what could not be researched because the page was blocked, unavailable or too vague.

The final report should make research limits visible. No public evidence should not be presented as evidence that nothing happened.

## Example user flow

```text
Capture a job posting
    ↓
Identify the employer, role and important unknowns
    ↓
Research relevant public company and role sources
    ↓
Answer a defined set of job-seeker questions
    ↓
Compare findings with the user’s preferences and constraints
    ↓
Show meaningful signals, uncertainty and verification questions
```

## Questions the service might answer

### About the company

- What does the company appear to do?
- Is the employer identity clear and consistent across sources?
- What products, services or customers are publicly described?
- Are there signs that the company is active in the relevant area?
- Does the company provide clear contact and location information?

### About the role

- Does the role appear connected to the company’s stated work?
- Are the duties consistent across the posting and company sources?
- Is the role full-time, part-time, temporary, contract or unclear?
- Are the location, schedule, pay and reporting relationship clear?
- Are important details only revealed during the interview?

### About the job seeker’s preferences

- Does the schedule match the user’s availability?
- Does the compensation meet the user’s stated minimum or expectations?
- Does the location fit the user’s travel limits?
- Does the work environment match stated likes and dislikes?
- Does the role require conditions the user has said they want to avoid?
- Which unknowns could materially change the user’s decision?

## Evidence output

Each finding should show:

```text
Question: Is the employer identity clear?
Finding: The job posting names Company A, while the application email uses Company B.
Evidence: <posting excerpt> + <public source link>
Meaning for this user: Worth verifying because the user prefers direct-employer roles.
Confidence: Needs verification
```

The system should not convert this into an automatic fraud, safety or suitability verdict.

## Expected value

- Reduces the time required for basic company and role research.
- Helps job seekers focus on questions that matter to their own circumstances.
- Connects company context, job-posting evidence and personal preferences.
- Makes hidden or unclear decision factors more visible before the user invests in an application or interview.

## Evidence and assumptions

### Evidence

- JobHub research identified recurring concerns involving unclear duties, ambiguous compensation, unclear employer identity and role details deferred to interviews.
- The current prototype already extracts posting facts, missing information and verification questions.
- The red-flag evidence-database idea would provide a reusable signal library for this service.

### Assumptions

- Public sources can provide useful context for at least some employers and roles.
- Users value targeted research more than a large undifferentiated company profile.
- Preference-aware explanations are more useful than generic company-risk labels.

## Feasibility review

### Technical feasibility

Feasible as a staged research pipeline:

```text
Posting capture
    ↓
Employer and role identification
    ↓
Source discovery
    ↓
Public-page capture
    ↓
Question-specific extraction
    ↓
Evidence and preference comparison
```

The service should preserve raw captures, source URLs, timestamps and extraction status.

### Data and integration feasibility

Source access will vary. Company websites may be public, dynamic, incomplete or blocked. Third-party reviews and social posts may be difficult to verify and may represent individual experiences rather than general facts. The initial version should prioritise official and directly attributable public sources.

### AI feasibility

An agent could help:

- generate targeted research questions;
- discover relevant public sources;
- extract answers into a schema;
- connect evidence to the job posting;
- compare findings with explicit preferences;
- identify contradictions and unresolved questions.

The agent must not present an inaccessible source as researched, treat search snippets as complete evidence, or infer company intent from weak signals.

### Privacy, security and responsible-use considerations

- Research public company information, not private individuals.
- Do not collect unnecessary personal data about employees or applicants.
- Separate employer/source concerns from candidate fit.
- Do not treat negative reviews, layoffs, legal references or online comments as definitive without context.
- Do not produce a universal employer-risk score without strong validation.
- Show the source and date for consequential findings.
- Make it clear when the system could not verify a claim.
- Respect website terms, access controls and robots or anti-bot boundaries.

### Complexity and maintenance

This is significantly more complex than single-posting extraction because it requires source discovery, entity resolution, source ranking, freshness handling, contradiction management and potentially long-running research tasks.

## Smallest useful prototype

Start with one job posting and a constrained question set:

1. Identify the employer and role from the posting.
2. Research only the official company website and one additional attributable public source.
3. Answer five predefined questions.
4. Link every answer to its source.
5. Compare the results with three user preferences.
6. Show unknowns and questions to verify.

Do not begin with broad internet-wide scraping or an employer legitimacy score.

## Decision

Explore further

## Decision rationale

The feature could provide meaningful value beyond extracting the posting itself, but its usefulness depends on source quality, research boundaries and careful separation between observable facts and interpretation.

## Feasibility assessment and options — 2026-10-29

### Feasibility

- One-posting, small-source research: High
- HTML, visible-text and JSON-LD extraction: High
- Dynamic or blocked pages: Partial; fallback states required
- Company/entity resolution: Medium-high
- Source freshness and snapshots: High
- Internet-wide employer evaluation: Medium-low and not appropriate initially

### Implementation options

| Option | Description | Trade-off |
|---|---|---|
| A — Constrained research pass | Posting + official company site + one attributable secondary source | High feasibility; limited coverage |
| B — Source-aware service | Source adapters, entity resolution, snapshots, freshness checks and approved research routes | Stronger continuity; meaningful maintenance cost |
| C — Continuous employer intelligence | Monitoring layoffs, turnover, reposting, reviews and company changes | Broadest coverage; high cost, legal, privacy and quality risk |

Recommended path: implement Option A first and shape the data model for Option B. Never silently treat blocked or partial retrieval as evidence of employer silence.

### Smallest useful experiment

Use 15 postings across five industries. For each, resolve the employer, check the official site and one attributable source, answer five fixed questions, and compare the result with a human review. Measure employer-resolution accuracy, source coverage, unsupported claims, contradictions, latency, blocked-source handling and question usefulness.

The service should report exact match, likely match, ambiguous, unresolved or user-confirmation-required employer identity states.

### External feasibility references

- [Google JobPosting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting) supports deterministic extraction of common job fields when available.
- [Google JavaScript crawling guidance](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) explains why some pages require rendering and why retrieval can fail.
- [IETF Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html) and [HTTP caching guidance](https://www.rfc-editor.org/rfc/rfc9110.html) support bounded, traceable retrieval rather than unrestricted crawling.
- [Singapore ScamShield guidance](https://ask.gov.sg/scamshield/questions/cmdcv46bt017g36wpmgi0mc2t) supports local checks around identity, vague descriptions, sensitive information and suspicious offers.

## Open questions

- Which public sources should be allowed in the first version?
- What are the minimum questions every job seeker should be able to answer?
- How should the service handle multiple companies with similar names?
- How should it handle staffing agencies and third-party recruiters?
- What makes a company source authoritative enough for a finding?
- How fresh must company research be?
- How should personal preferences be represented without becoming an intrusive profile system?
- Which findings are meaningful enough to change a job seeker’s next action?
- How should the service report blocked, missing or contradictory sources?

## Related ideas

- [Fact-based red-flag evidence database](00_red-flag-evidence-database.md)
- Single-posting review prototype
- Job-posting capture and evidence extraction
