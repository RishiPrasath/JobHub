# Feature idea: Fact-based red-flag evidence database

## Status

Proposed

## Locked direction — 2026-10-29

This feature is not limited to wording found in a job posting. It should cover signals across the full opportunity journey:

```text
Job posting → recruiter communication → interview → offer and negotiation
```

The database should include interview and employer-behaviour signals such as poor communication, repeated rescheduling, evasive answers, contradictory answers, boundary-blurring culture language, unclear success criteria, repeated vacancies, pressure to accept and changes to pay or duties.

Every entry must separate the observed signal from its possible meaning, what it does not prove, the question to ask, evidence to collect, personal relevance and confidence. Signals must not become automatic “toxic workplace” or fraud labels.

## User problem

Job seekers may notice warning signs in a job posting but lack a reliable way to interpret them. A single unclear phrase may not mean much on its own, while several source-grounded signals together may justify asking questions or proceeding carefully.

## Proposed feature

Create a fact-based, structured database of job-posting warning signals and related evidence. An agent could retrieve relevant entries and compare them with a particular job posting to identify connected patterns, missing information and questions worth verifying.

The database should describe signals and their context. It must not automatically label an employer or posting as fraudulent, unsafe or dishonest.

## Example user flow

```text
Capture a job posting
    ↓
Extract observable phrases, conditions and inconsistencies
    ↓
Retrieve relevant red-flag evidence entries
    ↓
Connect matching signals to the posting with source excerpts
    ↓
Explain why the signals may matter
    ↓
Suggest questions or verification steps
```

## Possible evidence entry

```text
Signal: Important duties deferred until the interview
Category: Missing role information
Why it matters: The applicant cannot evaluate the actual work before investing more time.
What it does not prove: It does not establish fraud or bad intent.
Suggested verification: Ask for the core duties, schedule and reporting relationship.
Evidence standard: Require a source excerpt and context.
```

## Expected value

- Helps job seekers notice patterns they may otherwise overlook.
- Connects individual posting details instead of treating every signal in isolation.
- Produces practical questions to ask before applying, interviewing or sharing sensitive information.
- Creates a reusable knowledge base for future research and experiments.

## Evidence and assumptions

### Evidence

- JobHub research has identified recurring concerns such as unclear duties, ambiguous pay, deferred details, inconsistent role descriptions and unclear employer identity.
- The prototype already separates missing information and verification questions from unsupported fraud claims.

### Assumptions

- A structured evidence library can improve consistency across job reviews.
- Users will find connected explanations more useful than a single red warning label.
- Reliable entries can be sourced, reviewed and kept current.

## Feasibility review

### Technical feasibility

Likely feasible as a searchable structured dataset with categories, aliases, evidence requirements and retrieval metadata. An agent could retrieve candidate entries and attach them to extracted posting facts.

### Data and integration feasibility

The difficult part is not storing the records; it is sourcing, validating, updating and contextualising them. Entries should retain provenance and distinguish research findings, legal or regulatory guidance, expert advice and product interpretation.

### AI feasibility

An AI agent could help retrieve relevant entries and connect them to posting excerpts. Every connection should show the matching evidence and confidence. The agent should be allowed to say that no reliable connection was found.

### Privacy, security and responsible-use considerations

- Do not infer criminality or employer intent from wording alone.
- Do not expose private or unverified allegations.
- Keep signals separate from conclusions.
- Present multiple explanations when a signal has benign interpretations.
- Make the original posting evidence inspectable.
- Avoid a universal risk score unless it can be meaningfully validated.

### Complexity and maintenance

The database will require review rules, versioning, source expiry checks and a process for correcting weak or outdated entries. Poorly maintained records could create false alarms and reduce user trust.

## Smallest useful prototype

Start with a small curated library of evidence entries and a single-posting comparison:

1. Store 10–20 reviewed signals.
2. Give each signal categories, examples, non-conclusions and suggested questions.
3. Retrieve entries using deterministic keywords first.
4. Show the matched posting excerpt beside each signal.
5. Ask a human to review the connection before treating it as useful.

## Decision

Explore further

## Decision rationale

The idea is potentially valuable, but it should first be tested as an evidence-retrieval and explanation feature—not as an automated scam detector.

## Feasibility assessment and options — 2026-10-29

### Feasibility

- Structured signal storage: High
- Exact phrase and alias retrieval: High
- Source-linked posting excerpts: High
- Semantic retrieval and connected-pattern reasoning: Medium
- Reliable employer or legal conclusions: Low
- Continuous source maintenance: Medium-low

### Implementation options

| Option | Description | Trade-off |
|---|---|---|
| A — Curated prototype | 10–20 reviewed records in JSON or SQLite, deterministic search, source excerpts and human review | Most transparent; limited paraphrase handling |
| B — Balanced system | Versioned records, hybrid retrieval, jurisdiction/industry filters, freshness checks and correction history | More useful; requires curation and evaluation |
| C — Knowledge graph | Multi-jurisdiction ontology, monitoring, relationship reasoning and expert review | Broadest capability; premature and difficult to govern |

Recommended path: implement Option A first while keeping the record model compatible with Option B.

### Smallest useful experiment

Test 20 reviewed entries against job-posting fixtures covering clear, benign, ambiguous, missing-information and contradictory cases. Measure relevant retrieval, false alarms, missed signals, citation completeness, user comprehension and whether suggested questions are useful.

The feature must be able to return “no reliable signal found” and “needs verification.” It must not label an employer fraudulent, toxic or illegal from a phrase alone.

### External feasibility references

- [SQLite FTS5](https://www.sqlite.org/fts5.html) supports transparent full-text retrieval, ranking, highlighting and snippets.
- [W3C PROV](https://www.w3.org/TR/prov-overview/) and [Web Annotation](https://www.w3.org/TR/annotation-model/) provide useful concepts for provenance and source-span linking.
- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) and [OWASP GenAI risks](https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/) support cautious handling of fabricated explanations, prompt injection and sensitive information.

## Open questions

- What qualifies as a reliable red-flag evidence entry?
- Which sources are authoritative enough for different signal categories?
- How should signals be weighted, if at all?
- How should benign explanations be represented?
- How often should entries be reviewed or retired?
- Can users understand the connection without being overwhelmed?
- What evidence is required before an agent may recommend a verification action?

## Related ideas

- Single-posting review prototype
- Job-posting capture and evidence extraction
- Red-flag and missing-information research
