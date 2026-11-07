# Company Research Service Plan

Status: Draft

## 1. Purpose

The Company Research Service will help a job seeker understand an employer before investing significant time in an application, interview, or offer decision.

The service should focus especially on lived experiences from current employees, former employees, contractors, and candidates. Official records are useful for identifying the legal entity, but they cannot describe the complete experience of working for or interviewing with a company.

The service must gather evidence from the internet. An LLM may help organize or summarize retrieved evidence, but it must not invent company information or act as the source of truth.

## 2. Core direction

The service will use a fixed source catalog, not a permanent list of URLs for every company.

At research time, it will:

1. Resolve the company identity.
2. Generate source-specific search queries.
3. Discover relevant company pages dynamically.
4. Retrieve permitted public pages or record that retrieval was blocked.
5. Extract reviews, discussions, facts, and metadata.
6. Group the evidence into meaningful themes.
7. Show recurring patterns, disagreements, and unknowns to the job seeker.

Company-specific URLs are outputs of a research run. They are not hard-coded into the service configuration.

## 3. Source catalog

The initial source catalog should include the following source classes.

### 3.1 Identity and registration sources

- ACRA and data.gov.sg: legal entity name, UEN, status, registration date, entity type, address, and business activity.
- BizFile: optional deeper business information when the user authorizes a paid lookup.
- SGX: listed-company announcements, corporate actions, and issuer disclosures.

The current public ACRA dataset provides fields such as UEN, entity name, entity status, entity type, UEN issue date, and registered address. It is updated monthly and available under the Singapore Open Data Licence. [ACRA entities dataset](https://data.gov.sg/datasets/d_3f960c10fed6145404ca7b821f263b87/view)

ACRA should be used to resolve and validate the legal entity, not to discover or represent the whole employer experience. ACRA's free search provides basic information such as status and registered address; more detailed Business Profiles and compliance products may require payment. [ACRA information products](https://www.acra.gov.sg/resources/buying-business-information/types-of-acra-information-products/)

### 3.2 Dedicated employer-review sources

- Glassdoor: culture, management, compensation, work-life balance, interview experiences, and employee reviews.
- Indeed Company Reviews: employee reviews, salary information, workplace dimensions, and company Q&A.
- JobStreet Singapore: local company profiles, culture, benefits, and employee reviews.
- Comparably: culture ratings, compensation information, employee reviews, and prospective-employee Q&A.

Glassdoor provides company ratings and review filters such as location, job type, job function, language, and workplace topic. [Glassdoor review filters](https://help.glassdoor.com/s/article/How-to-filter-reviews-on-Glassdoor?language=en_US)

Indeed describes its company pages as supporting reviews, ratings, Q&A, and salary information. [Indeed Company Pages](https://www.indeed.com/help/employers/articles/204747960)

JobStreet Singapore provides company profiles that combine employer information, culture, perks, benefits, and employee reviews. [JobStreet company profiles](https://help.sg.jobstreet.com/article/What-is-a-Company-Profile-JS)

Comparably states that company-page data includes anonymous culture ratings and reviews from employees, as well as company Q&A. [Comparably FAQ](https://www.comparably.com/faq/)

### 3.3 Workplace and professional discussion sources

- Blind: anonymous professional discussions, company discussions, salary, layoffs, management, and interview experiences.
- Fishbowl: industry and company discussions about salaries, culture, and interviews.
- Reddit: employee, candidate, and industry discussions, including company-specific communities.

Blind describes its company discussions as being supported by workplace verification while retaining anonymity. [Blind FAQ](https://us.teamblind.com/faq)

Fishbowl provides company-specific discussions and professional conversations about salary, culture, and interviews. [Fishbowl company discussions](https://www.fishbowlapp.com/companies)

These sources are not interchangeable with formal records. Their value is that they may reveal experiences that do not appear in company-controlled or structured review systems.

### 3.4 Specialist sources

Use specialist sources when relevant to the company, industry, or user preference:

- Fairygodboss and InHerSight: workplace experiences involving women, inclusion, parental leave, and advancement.
- Levels.fyi: technology-sector compensation and career information.
- Industry-specific communities and professional forums.
- YouTube, podcasts, and long-form blogs where employees or candidates describe their experiences.

These sources should be activated by relevance rather than queried for every company.

### 3.5 Context and corroboration sources

- Official company announcements and careers pages.
- Job boards and repeated job postings.
- CNA, The Straits Times, The Business Times, Reuters, and other reputable news sources.
- Government, regulator, court, licensing, and enforcement sources where publicly available.

These sources help corroborate major events such as layoffs, restructuring, acquisitions, disputes, closures, investigations, or changes in business activity.

## 4. Company identity and dynamic discovery

For Singapore entities, the preferred identity anchor is:

```text
UEN + jurisdiction
```

If a job posting contains only a brand name, trading name, subsidiary, or recruitment-agency name, the service should create a candidate identity and attempt to resolve it using:

1. Exact UEN match.
2. Exact legal name plus matching location.
3. Legal name plus a matching job-board or company-page profile.
4. Brand name plus evidence connecting it to a legal entity.
5. Name-only match, which must remain unresolved until corroborated.

The service should maintain aliases, former names, brands, subsidiaries, domains discovered during the run, addresses, industry identifiers, and parent-company relationships.

The service should never assume that a company name is unique. A name is a search clue; a UEN or equivalent jurisdictional registration number is the identity anchor.

## 5. Query-driven source discovery

The service should generate a bounded set of queries for each source. For a company named `Example Pte. Ltd.`, examples include:

```text
"Example Pte. Ltd." Glassdoor reviews
"Example Pte. Ltd." Indeed reviews
"Example Pte. Ltd." JobStreet reviews
"Example Pte. Ltd." interview experience
"Example Pte. Ltd." management culture
"Example Pte. Ltd." workload
"Example Pte. Ltd." salary
"Example Pte. Ltd." layoffs
"Example Pte. Ltd." Reddit
"Example Pte. Ltd." Blind
"Example Pte. Ltd." Fishbowl
```

The query planner should also use the company’s aliases, job title, department, location, and relevant user preferences.

The service should record the query, search provider, result rank, result title, result URL, snippet, retrieval time, and whether the result was subsequently fetched.

## 6. Making lived experience meaningful

Employee and candidate experiences are important evidence. They should not be dismissed merely because they are anonymous or subjective. They should be analysed with context.

For each review or discussion, capture where available:

- Experience type: employee, former employee, contractor, candidate, interviewer, or hearsay.
- Role, department, seniority, and location.
- Employment status and approximate tenure.
- Date of the experience and date of publication.
- Topic: management, workload, pay, culture, promotion, interview, discrimination, job security, or another theme.
- Specificity: whether the account gives concrete examples.
- Sentiment and reported impact, without treating sentiment as fact.
- Whether the experience is repeated by other people.
- Whether it appears in multiple independent sources.
- Whether other evidence contradicts or supports it.
- Retrieval status and source URL.

Example evidence record:

```json
{
  "theme": "unclear_role_scope",
  "experience_type": "candidate_interview",
  "source": "glassdoor",
  "role": "administration officer",
  "location": "Singapore",
  "specificity": "high",
  "recency": "recent",
  "recurrence": "appears_in_6_reviews",
  "corroboration": ["indeed", "reddit"],
  "status": "reported_pattern_not_verified_fact"
}
```

The service should prefer a pattern statement such as:

> Several recent candidates independently described unclear duties during the interview stage. This is a recurring reported experience, not proof of employer intent.

It should avoid unsupported conclusions such as:

> This company is toxic.

## 7. Evidence interpretation rules

The service should distinguish:

- Verified fact: supported by an official or directly observable source.
- First-hand report: a person describes their own experience.
- Repeated pattern: similar reports recur across people or sources.
- Corroborated signal: a report aligns with independent evidence.
- Contradiction: sources disagree.
- Hypothesis: a possible explanation requiring further checking.
- Unknown: evidence was not found or could not be retrieved.

The service should not produce a single unexplained employer score. It should show the underlying themes, relevant evidence, date range, source coverage, and uncertainty so that the job seeker can decide what matters to them.

## 8. Initial source priorities

The first implementation should prioritize:

1. ACRA/data.gov.sg for Singapore identity resolution.
2. Glassdoor for structured employer and interview reviews.
3. Indeed for a second structured review source.
4. JobStreet Singapore for local coverage.
5. Reddit for candid employee and candidate discussions.
6. Blind and Fishbowl for relevant professional or industry coverage.
7. News, SGX, and regulator sources for corroboration.

Comparably, Fairygodboss, InHerSight, Levels.fyi, YouTube, podcasts, and industry forums should be added when the company, role, industry, or candidate preferences make them relevant.

The priority order is an execution order, not a ranking of whose experiences are most truthful. Different source types answer different questions.

## 9. Product principle

JobHub should help a job seeker investigate an employer’s reported reality, not merely read the employer’s presentation of itself.

The service should preserve employee and candidate experiences, identify meaningful recurring themes, surface contradictions, and keep the final decision under the job seeker’s control.
