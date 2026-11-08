# Decision Log

This is the durable record of material product and technical decisions.

## Decision format

For each decision, record:

- Date
- Decision
- Status: proposed, accepted, superseded, or rejected
- Context and problem
- Options considered
- Evidence
- Consequences and trade-offs
- Revisit trigger

## Current decisions and working assumptions

### Strategy documents are numbered from zero

- **Status:** Accepted
- **Decision:** Strategy documents begin with `00_` and proceed in numbered order.
- **Reason:** Make the reading order and lifecycle visible.

### Drafts and curated strategy are separate

- **Status:** Accepted
- **Decision:** `_drafts/` remains exploratory; `strategy/` contains curated working strategy.
- **Reason:** Preserve exploration without making unfinished notes the source of truth.

### Product surface remains open

- **Status:** Accepted working assumption
- **Decision:** Do not lock mobile, web, desktop, browser extension, or multi-surface delivery before research.
- **Revisit trigger:** Product-surface research and prototype evidence.

### Specifications should scale with certainty

- **Status:** Proposed
- **Decision:** Use lightweight behavior descriptions during discovery and more formal specifications for stable, critical workflows.
- **Revisit trigger:** Prototype and maintenance experience.

### Job-opportunity evaluation is an integrated evidence workflow

- **Date:** 2026-10-29
- **Status:** Accepted working direction
- **Decision:** Update the four proposed feature ideas—red-flag evidence database, company and role research service, discriminatory and harmful signals knowledge base, and candidate profile and preferences—so they work together across the full job-opportunity journey: posting, communication, interview, offer and decision.
- **Context and problem:** A job posting alone may not reveal whether the role is suitable, clearly defined, responsibly handled or worth pursuing. Important evidence can appear later in employer communication, interview answers, role history and offer discussions.
- **Evidence:** [Pre-interview job red-flags research](../01_research/rounds/R00-orientation-and-baseline/results/product-and-users/2026-10-29-pre-interview-job-red-flags.md), [red-flag evidence database](../03_features/source-ideas/00_red-flag-evidence-database.md), [company and role research service](../03_features/source-ideas/01_company-and-role-research-service.md), [harmful-signals knowledge base](../03_features/source-ideas/02_discriminatory-and-harmful-signals-knowledge-base.md), and [candidate profile and preferences](../03_features/source-ideas/03_candidate-profile-and-preferences.md).
- **Options considered:** Keep the product posting-only; create a separate interview feature immediately; or extend the existing features into one staged evidence workflow. The accepted direction is the third option. A standalone interview feature is deferred until the workflow proves large enough to justify it.
- **Consequences and trade-offs:** JobHub should preserve evidence, uncertainty, alternative explanations, user preferences and decision history. It must not create universal toxicity, fraud or suitability scores, make automatic legal conclusions or silently decide for the user. This direction increases research and state-tracking complexity but better reflects the user’s real decision process.
- **Scope boundary:** This is an accepted product direction, not a final MVP, platform, architecture or implementation commitment.
- **Revisit trigger:** Prototype or concierge testing shows that the staged workflow does not improve identification of meaningful unknowns, question quality or decision confidence without creating excessive false alarms or user burden.

