# Feature idea: Candidate profile and preferences

## Status

Proposed

## Locked direction — 2026-10-29

The candidate profile should include decision boundaries and working-style preferences, not only skills and job-search targets. Relevant fields include:

- must-haves, strong preferences, acceptable compromises and deal-breakers;
- minimum pay and schedule limits;
- tolerance for overtime, ambiguity and changing responsibilities;
- need for training, structure or predictable hours;
- communication and management preferences; and
- workplace risks or conditions the user wants to avoid.

JobHub should explain why a finding matters to this person. It should not decide that a job is unsuitable on the user’s behalf.

## User problem

A job seeker repeatedly explains the same skills, experience, preferences, constraints and goals while reviewing jobs, tailoring resumes and preparing for interviews. Without a structured profile, JobHub cannot adapt its responses consistently, and the user may receive generic or contradictory guidance.

## Proposed feature

Create a user-controlled candidate profile that stores the information needed to make job reviews, matching, application preparation and AI responses more relevant.

The profile should not be a single opaque “candidate score.” It should separate different types of information and show how each item was obtained:

```text
Verified facts
    ↓
User preferences and constraints
    ↓
Goals and working context
    ↓
Evidence-backed derived insights
    ↓
Personalised but reviewable AI responses
```

The user should be able to inspect, edit, correct, hide, export and delete profile information.

## Example user flow

```text
Create or import a candidate profile
    ↓
Review each extracted item
    ↓
Mark it as confirmed, incorrect, private or unknown
    ↓
Set preferences and priorities
    ↓
Review a job posting
    ↓
See transparent comparisons and personalised questions
    ↓
Correct the profile when circumstances change
```

## Information the profile may contain

### 1. Basic working context

Only collect what is useful for the product:

- preferred name or display name;
- location or commute area, at an appropriate level of precision;
- work authorisation or eligibility information when the user chooses to provide it;
- preferred contact or application details only when needed for a later workflow;
- current job-search stage;
- whether the user is actively searching, exploring or preparing.

The profile should not require sensitive personal details that do not improve the user’s job-search decisions.

### 2. Experience and work history

- previous roles and employers;
- dates or approximate periods of work;
- responsibilities performed;
- achievements and outcomes;
- industries and work environments;
- employment type and working arrangements;
- projects, freelance work, volunteering or caregiving experience the user wants considered.

Each item should retain its source:

```text
Source: User entered
Source: Imported resume
Source: Confirmed from an application record
Source: AI-suggested; user confirmation required
```

### 3. Skills and capabilities

Separate different forms of evidence:

- technical skills;
- tools and software;
- domain knowledge;
- transferable skills;
- communication and language abilities;
- licences, certifications and qualifications;
- proficiency level;
- recency of use;
- evidence or examples demonstrating the skill;
- skills the user wants to develop.

The system should not treat a skill as confirmed merely because it appears in a job posting or an AI-generated draft.

### 4. Preferences and constraints

- preferred industries or sectors;
- roles the user wants to explore;
- roles the user does not want;
- full-time, part-time, contract or temporary preferences;
- on-site, hybrid or remote preferences;
- preferred locations and commute limits;
- minimum salary or hourly rate;
- preferred working hours;
- willingness to work shifts, weekends, public holidays, travel or on-call periods;
- preference for stability, progression, autonomy, training or structured supervision;
- customer-facing, physical, technical or independent-work preferences;
- company-size or workplace-environment preferences.

Preferences should support priority levels:

```text
Must have
Strong preference
Open to
Avoid if possible
Do not want
```

This prevents a minor preference from being treated like a hard exclusion.

### 5. Goals and current situation

- target role or next career direction;
- short-term job-search goal;
- longer-term career goal;
- reason for exploring a role;
- desired learning or development outcomes;
- time available for applications and preparation;
- financial, schedule or location pressures the user chooses to disclose;
- confidence areas and areas where the user wants support.

These details should be optional and changeable. The system should not infer personal circumstances without permission.

### 6. Application and learning history

If the user chooses to store it, the profile may include:

- roles reviewed;
- roles saved, declined or applied to;
- reasons for decisions;
- questions asked during interviews;
- feedback received;
- resume versions used;
- interview preparation topics;
- skills or requirements repeatedly appearing in target roles.

The user should be able to keep job-specific information separate from the canonical profile.

## How the profile improves JobHub

### Matching and comparison

The system can compare:

- posting requirements against verified skills;
- schedule and location against preferences;
- compensation against stated minimums;
- role duties against desired work;
- missing requirements against learnable gaps;
- company signals against the user’s stated priorities.

The output should remain transparent:

```text
Posting requirement: Weekend shifts
Profile preference: Avoid weekend work if possible
Meaning: May conflict with a preference; confirm the actual schedule.
```

### Better AI responses

The profile can help JobHub:

- explain job postings at the user’s level;
- ask more relevant clarification questions;
- tailor resume suggestions without inventing experience;
- identify transferable skills;
- distinguish a real gap from a skill the user already has;
- prepare interview questions based on the role and the user’s evidence;
- maintain consistent terminology across application materials.

The AI should cite the profile item it used and avoid silently using private or stale information.

### Adaptation over time

JobHub could learn from explicit user actions:

- repeated acceptance or rejection of suggestions;
- corrected skills or preferences;
- decisions to pursue or decline certain roles;
- feedback about whether a report was useful;
- changes in target industries or availability.

Adaptation should be visible and reversible. The system should not silently redefine the user’s identity or career direction.

## Profile data states

Every important item should have a clear state:

```text
Confirmed by user
Imported; awaiting review
Evidence-backed
AI suggestion; not confirmed
Outdated
Private or excluded from AI use
Unknown
Rejected or corrected
```

This prevents unverified AI output from becoming permanent candidate truth.

## Privacy and control requirements

- The profile must be optional for basic job-posting review.
- Use data minimisation: collect only what improves the user’s stated goals.
- Clearly explain why each category is requested.
- Allow field-level visibility controls.
- Let the user exclude information from AI prompts or comparisons.
- Keep sensitive attributes out of matching unless the user explicitly chooses to use them for a legitimate purpose.
- Do not infer protected characteristics or health information.
- Support export, correction and deletion.
- Record when information was last confirmed.
- Keep job-specific drafts and application history separate from the canonical profile.
- Never share profile data with employers or external services without explicit user action.

## Smallest useful prototype

Start with a temporary, session-based profile containing only:

1. Skills and evidence.
2. Desired role types.
3. Work arrangement preferences.
4. Location or commute preference.
5. Compensation preference.
6. Schedule constraints.
7. A short “avoid” list.

Let the user review one job and see transparent comparisons. Do not begin with permanent accounts, sensitive data, automated learning or a full application history.

## Feasibility review

### Technical feasibility

Feasible as a structured profile document with versioned fields, provenance, visibility settings and a comparison layer. The core model should remain provider- and platform-agnostic.

### AI feasibility

AI can help extract profile items from resumes and conversations, suggest transferable skills and personalise explanations. Human confirmation is required before extracted information becomes a verified profile fact.

### Complexity and maintenance

The main complexity is not storing fields; it is keeping information current, preventing contradictions and ensuring that stale or unverified data does not affect important recommendations.

## Risks and trade-offs

- A richer profile can improve relevance but increase privacy exposure.
- Automatic extraction reduces effort but can introduce inaccurate candidate facts.
- Strong preference matching can reduce useful discovery if preferences are treated as rigid rules.
- Learning from user behaviour can improve adaptation but may reinforce temporary decisions or biases.
- Storing application history can improve continuity but increases the impact of a data breach or accidental disclosure.

## Decision

Explore further

## Decision rationale

A candidate profile could become a central product capability, but it should begin as a transparent, user-controlled preference and evidence layer rather than a permanent AI-generated identity.

## Feasibility assessment and options — 2026-10-29

### Feasibility

- Structured profile storage: High
- Manual editing, provenance and deterministic comparison: High
- Resume import and AI extraction: Medium to medium-high
- Field-level privacy and optional persistence: Medium-high
- Semantic skill matching: Medium
- Continuous preference learning or autonomous matching: Low for the first release

### Implementation options

| Option | Description | Trade-off |
|---|---|---|
| A — Session profile | Skills with evidence, desired roles, work arrangement, location, pay, schedule and avoid list | Fast and private; limited continuity |
| B — Versioned profile | Provider-neutral schema, provenance, confirmation states, privacy controls, export and optional persistence | Better foundation; more data responsibility |
| C — Adaptive career profile | Learns from applications, infers preferences, maintains variants and continuously ranks jobs | Highest convenience; high privacy, fairness and explainability risk |

Recommended path: implement Option A first while designing the data shape for Option B. Do not build Option C yet.

### Smallest useful experiment

Use synthetic or anonymised profiles across administration, hospitality, technical support, logistics/operations and healthcare support. Compare manual review with AI-assisted extraction, require confirmation for every imported item, and test the profile against several postings.

Measure extraction completeness, incorrect fields, unsupported skills, correction time, preference-conflict accuracy, missed hard constraints, comprehension, export/re-import fidelity and privacy comprehension.

Deterministic rules should control schema validation, confirmation states, privacy, staleness, salary, schedule, location, export, deletion and preference conflicts. AI may suggest fields and explanations but must not silently create verified candidate facts.

### External feasibility references

- [Singapore PDPC guidance](https://www.pdpc.gov.sg/)
- [IMDA Model AI Governance Framework](https://www.imda.gov.sg/)
- [JSON Schema](https://json-schema.org/docs)
- [WCAG 2.2 input guidance](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose)
- [OWASP sensitive-information disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)

## Open questions

- Which profile fields are genuinely necessary for the first useful workflow?
- Should the first profile be session-based, local-only or account-backed?
- How should profile information be imported from a resume?
- How should conflicting or outdated facts be resolved?
- Which data should never be used for matching?
- How should the user see exactly what information the AI used in a response?
- How should profile data be exported in a portable format?
- What should happen when a user changes career direction?

## Related ideas

- [Company and role research service](01_company-and-role-research-service.md)
- [Fact-based red-flag evidence database](00_red-flag-evidence-database.md)
- [Discriminatory and harmful signals knowledge base](02_discriminatory-and-harmful-signals-knowledge-base.md)
