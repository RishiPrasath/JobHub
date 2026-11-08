# Proposed feature feasibility review

Date: 2026-10-29  
Status: specialist-reviewed feasibility assessment; implementation and final MVP acceptance remain open.

## Features reviewed

1. [Fact-based red-flag evidence database](../../03_features/source-ideas/00_red-flag-evidence-database.md)
2. [Company and role research service](../../03_features/source-ideas/01_company-and-role-research-service.md)
3. [Discriminatory and harmful signals knowledge base](../../03_features/source-ideas/02_discriminatory-and-harmful-signals-knowledge-base.md)
4. [Candidate profile and preferences](../../03_features/source-ideas/03_candidate-profile-and-preferences.md)

Four bounded specialists inspected the repository and performed read-only web research. No specialist edited files. The coordinator reconciled their findings here and in the feature documents.

## Overall conclusion

All four ideas are technically feasible in a bounded form. None is justified as a fully autonomous system yet.

The feasible product boundary is:

> JobHub helps a person inspect evidence, compare it with their own preferences, ask better questions and decide what to do next.

The following are not currently justified:

- universal employer-quality or toxicity scores;
- autonomous fraud or discrimination decisions;
- legal conclusions from wording alone;
- continuous internet-wide employer monitoring;
- autonomous candidate ranking or adaptive career identity;
- automatic acceptance or rejection of a job.

## Feasibility matrix

| Feature | Bounded feasibility | Main difficult area | Recommended starting point |
|---|---|---|---|
| Red-flag evidence database | High for structured storage, keyword retrieval and source-linked explanations | Maintaining trustworthy entries and avoiding false alarms | 10–20 curated records with deterministic retrieval and human review |
| Company and role research service | High for one posting and a small approved source set | Dynamic/blocked sites, entity resolution, freshness and interpretation | Posting + official company site + one attributable secondary source |
| Discriminatory/harmful signals knowledge base | High for awareness and evidence retrieval | Jurisdiction, fairness, sensitive data and legal boundaries | Small Singapore-focused, reviewed knowledge pack |
| Candidate profile and preferences | High for session data, manual editing and deterministic comparison | Accuracy, privacy, staleness, import quality and lifecycle management | Session profile compared with one posting |

## Options by feature

### 1. Red-flag evidence database

| Option | What it does | Feasibility | Trade-off |
|---|---|---:|---|
| A — Curated prototype | JSON/SQLite records, aliases, full-text retrieval, exact posting excerpts and human review | High | Transparent but limited paraphrase coverage |
| B — Balanced system | Versioning, source freshness, hybrid retrieval, metadata filters, correction logs and review queue | Medium-high | More value and maintenance |
| C — Knowledge graph | Multi-jurisdiction ontology, monitoring, semantic reasoning and expert review | Medium-low | Powerful but premature and difficult to evaluate |

Recommendation: start with A and shape the records so they can grow into B. Use AI for candidate matches and explanations, not verdicts.

### 2. Company and role research service

| Option | What it does | Feasibility | Trade-off |
|---|---|---:|---|
| A — Constrained research pass | User supplies one posting; JobHub checks the posting, official company site and one secondary source | High | Limited coverage but easy to validate |
| B — Source-aware service | Adds structured job extraction, entity resolution, snapshots, freshness and approved source adapters | Medium-high | Stronger continuity with engineering cost |
| C — Continuous employer intelligence | Monitors many sources for layoffs, turnover, reposting, reviews and company changes | Medium-low | High cost, legal, privacy, quality and maintenance risk |

Recommendation: implement A first, with data structures that support B. Treat blocked, partial and ambiguous retrieval as visible outcomes.

### 3. Discriminatory and harmful signals knowledge base

| Option | What it does | Feasibility | Trade-off |
|---|---|---:|---|
| A — Singapore-reviewed awareness pack | Curated entries, evidence excerpts, jurisdiction tags, questions and abstention | High | Safe starting coverage but narrow |
| B — Governed hybrid retrieval | Semantic retrieval, review queue, versioned policy packs and correction/appeal paths | Medium | Better recall, more governance |
| C — Multi-jurisdiction classifier | Multilingual legal and discrimination classification with expert network | Low for current stage | Large legal and operational burden |

Recommendation: use A first and only expand after testing false positives, user comprehension and source maintenance.

### 4. Candidate profile and preferences

| Option | What it does | Feasibility | Trade-off |
|---|---|---:|---|
| A — Session profile | Skills with evidence, role goals, location, work arrangement, pay, schedule and avoid list | High | Low privacy risk, limited continuity |
| B — Versioned profile | Provider-neutral schema, provenance, confirmation states, privacy controls, export and optional persistence | Medium-high | Better continuity, more data responsibility |
| C — Adaptive career profile | Learns from applications, infers preferences, maintains variants and continuously ranks jobs | Low for current stage | High privacy, fairness, explainability and evaluation risk |

Recommendation: implement A as the first experiment and design the data shape for B. Do not build C yet.

## Shared technical pattern

The four features should share a common evidence model:

```text
Source or user input
    ↓
Captured item and timestamp
    ↓
Extracted fact or signal
    ↓
Provenance and confidence
    ↓
User correction or confirmation
    ↓
Personal relevance
    ↓
Question or next action
```

The system should preserve the difference between:

- directly observed fact;
- source-reported claim;
- AI suggestion;
- user observation;
- interpretation;
- unknown;
- contradiction;
- confirmed user decision.

## Recommended execution order

1. Build a session-based candidate profile and preference comparison.
2. Add a small curated red-flag library with deterministic retrieval.
3. Add constrained company and role research with visible source status.
4. Add the harmful-signals pack with Singapore-specific governance and human review.
5. Test the combined workflow against synthetic, cross-industry postings.
6. Only then decide whether persistence, semantic retrieval or broader research is justified.

## Shared evaluation requirements

Every feature should measure:

- evidence completeness;
- unsupported-claim rate;
- false positives and false negatives;
- correction effort;
- user comprehension;
- usefulness of suggested questions;
- handling of missing, blocked and contradictory sources;
- privacy and consent comprehension;
- accessibility of the review flow;
- whether the result changes or improves the next action.

Passing a technical test will not prove that the feature is valuable. The product decision still requires a human-reviewed workflow experiment.

## Research sources used

Specialists consulted official or authoritative material including:

- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [OWASP GenAI risks](https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/)
- [W3C PROV](https://www.w3.org/TR/prov-overview/) and [Web Annotation](https://www.w3.org/TR/annotation-model/)
- [SQLite FTS5](https://www.sqlite.org/fts5.html)
- [Google JobPosting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting)
- [IETF Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Singapore ScamShield job guidance](https://ask.gov.sg/scamshield/questions/cmdcv46bt017g36wpmgi0mc2t)
- [Singapore TAFEP fair-employment guidance](https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines)
- [Singapore PDPC guidance](https://www.pdpc.gov.sg/)
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [JSON Schema documentation](https://json-schema.org/docs)

## Decision boundary

This review establishes feasibility options and recommended experiments. It does not select the final feature set, platform, architecture, pricing model or production launch scope.

