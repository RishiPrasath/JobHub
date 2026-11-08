# Feature idea: Discriminatory and harmful job-signal knowledge base

## Status

Proposed

## Locked direction — 2026-10-29

The knowledge base should cover harmful signals throughout hiring, not only discriminatory wording in job advertisements. Add interview and process concerns such as invasive questions, discriminatory screening, excessive or unpaid work trials, pressure to disclose sensitive information, harassment, humiliation, retaliation, coercive acceptance pressure and unexplained changes to pay or responsibilities.

Legal guidance, general warning signs and personal concerns must remain separate. The system should support awareness and safer questions without making automatic legal conclusions.

## User problem

Job seekers may encounter job postings or hiring processes that contain discriminatory, exploitative, coercive or otherwise harmful signals. They may not recognise the significance of the wording, may be unsure whether a concern is meaningful, or may not know what to ask before proceeding.

## Proposed feature

Create a curated knowledge base focused on discriminatory and harmful employment signals. An agent could use it to review a job posting, company research result or hiring-process description and identify evidence that may deserve attention.

The knowledge base should cover:

- discriminatory or exclusionary language;
- requirements that may unfairly screen people out;
- invasive or irrelevant personal questions;
- harassment, humiliation or abusive workplace signals;
- coercive, exploitative or unsafe conditions;
- unpaid labour, unclear pay or unlawful-looking deductions;
- requests for money, sensitive information or inappropriate commitments;
- misleading, degrading or dehumanising descriptions of workers;
- retaliation, intimidation or pressure during the hiring process.

This feature should support awareness and verification. It should not provide legal advice or make a definitive finding of unlawful discrimination without appropriate jurisdiction-specific evidence and human review.

## Example user flow

```text
Review a job posting or hiring-process note
    ↓
Identify potentially harmful wording or conditions
    ↓
Retrieve the relevant knowledge-base entries
    ↓
Show the source excerpt and context
    ↓
Explain why it may matter
    ↓
Suggest a question, boundary or safer next step
```

## Possible knowledge-base categories

### Discriminatory wording

- Explicit exclusion based on protected characteristics.
- Age-coded, gender-coded, racialised or nationality-based language.
- Requirements that appear unrelated to the actual work.
- “Ideal candidate” wording that may discourage otherwise qualified applicants.
- Different conditions or expectations for different groups.

### Questionable screening requirements

- Requests for photographs or personal details unrelated to the role.
- Questions about family plans, pregnancy, religion, health or other sensitive matters without a clear job-related reason.
- Requirements for a specific demographic when the job duties do not establish a legitimate need.
- Unclear background, financial or social-media checks.

### Exploitative or coercive conditions

- Unpaid work presented as a condition of being considered.
- Requests to pay fees, deposits or training costs to obtain a job.
- Unclear wages, deductions, commissions or overtime expectations.
- Pressure to accept conditions immediately without time to review them.
- Retention of identity documents or unusual financial demands.

### Harmful workplace signals

- Publicly described harassment, threats, humiliation or retaliation.
- Repeated reports of unsafe conditions or ignored safety complaints.
- Normalisation of excessive hours, abuse or degrading treatment.
- Job descriptions that openly expect workers to tolerate mistreatment.

### Misleading or dehumanising presentation

- Language that treats workers as disposable or interchangeable.
- Contradictions between the advertised role and the actual duties.
- Promises of rapid progression that are unsupported by the role or company context.
- Vague duties combined with high personal demands or unusual obligations.

## Evidence output

Each finding should be presented with context:

```text
Signal: Potentially discriminatory requirement
Observed wording: <short source excerpt>
Why it may matter: The requirement does not appear connected to the stated duties.
Possible explanations: The wording may be poorly written, role-specific or genuinely exclusionary.
What is not established: The excerpt alone does not prove unlawful discrimination.
Suggested next step: Ask how the requirement relates to the actual work or seek appropriate advice.
Confidence: Needs human review
Source: <URL and access date>
```

## Expected value

- Helps job seekers recognise harmful patterns earlier.
- Gives users language for asking questions and setting boundaries.
- Makes vulnerable job seekers less dependent on guesswork.
- Provides a structured foundation for responsible red-flag explanations.
- Separates evidence, context and uncertainty instead of producing an alarming label.

## Feasibility review

### Technical feasibility

Feasible as a curated, versioned knowledge base with categories, synonyms, examples, counterexamples, jurisdiction tags and evidence requirements. Retrieval could begin with deterministic phrase matching and later use an AI-assisted classifier for candidate entries.

### AI feasibility

An agent could identify possible matches and explain them, but every finding should retain the exact source excerpt. The agent should be conservative when language is ambiguous and should be able to return “no reliable signal found.”

### Legal and jurisdictional considerations

Discrimination rules differ by country, employment category and context. The knowledge base should distinguish:

- potentially concerning wording;
- established employer policy or public evidence;
- jurisdiction-specific legal guidance;
- user-protection or safety advice;
- unresolved interpretation.

JobHub should not make definitive legal conclusions or advise a user to take legal action without appropriate authoritative sources and human review.

### Privacy and safety considerations

- Do not expose private allegations about identifiable individuals.
- Avoid collecting sensitive personal information unless essential and explicitly requested.
- Do not infer protected characteristics about the user or employer.
- Provide safer alternatives when a user appears to face coercion or immediate risk.
- Preserve source provenance and avoid repeating unverified accusations as fact.

### Maintenance complexity

The knowledge base would require expert review, jurisdiction updates, source expiry checks, counterexamples and a correction process. Poorly maintained entries could create unnecessary fear or reproduce biased assumptions.

## Smallest useful prototype

Begin with a small, reviewed set of entries covering:

1. Explicitly exclusionary wording.
2. Unclear or discriminatory personal requirements.
3. Requests for money or sensitive information.
4. Unpaid work or unclear compensation.
5. Retaliation, harassment or unsafe-work signals.

Test the prototype against both clear positive examples and benign examples so that it measures false alarms as well as missed signals.

## Decision

Explore further

## Decision rationale

This could become an important safety and awareness feature, but it requires careful evidence standards, legal boundaries, jurisdiction support and protection against over-warning users.

## Feasibility assessment and options — 2026-10-29

### Feasibility

- Structured awareness entries and source retrieval: High
- Evidence-linked explanations: Medium-high
- AI-assisted paraphrase matching: Medium
- Jurisdiction-aware guidance: Medium, with reviewed content
- Autonomous legal or discrimination classification: Low

### Implementation options

| Option | Description | Trade-off |
|---|---|---|
| A — Singapore-reviewed awareness pack | Curated entries, evidence excerpts, jurisdiction tags, questions and abstention | Safest starting point; narrow coverage |
| B — Governed hybrid retrieval | Semantic retrieval, review queue, versioned policy packs and correction/appeal paths | Better recall; higher governance burden |
| C — Multi-jurisdiction classifier | Multilingual legal and discrimination classification with expert review | Large legal and operational burden; not suitable now |

Recommended path: implement Option A first and expand only after measuring false positives, user comprehension, source maintenance and the distinction between “concerning” and “illegal.”

### Smallest useful experiment

Create 40 cases: clearly concerning, benign but similar, ambiguous and jurisdiction-sensitive. Compare deterministic retrieval, AI-assisted retrieval and human-reviewed references. Measure supported matches, false alarms, missed signals, citation completeness, abstention quality and usefulness of suggested questions.

The system must not infer protected characteristics, declare discrimination, advise legal action automatically or convert an anonymous allegation into an established fact.

### External feasibility references

- [Singapore TAFEP fair-employment guidance](https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines)
- [Singapore MOM Fair Consideration Framework](https://www.mom.gov.sg/employment-practices/fair-consideration-framework)
- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [OWASP GenAI risks](https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Open questions

- Which jurisdictions should be supported first?
- Which categories require legal or domain-expert review?
- How should discriminatory language be distinguished from legitimate role requirements?
- How should the system handle satire, translation, quoted text or poor wording?
- What is the safest response when the user reports immediate harassment or coercion?
- How should users challenge or correct a knowledge-base finding?
- Which findings should remain private to the user rather than be retained?

## Related ideas

- [Fact-based red-flag evidence database](00_red-flag-evidence-database.md)
- [Company and role research service](01_company-and-role-research-service.md)
