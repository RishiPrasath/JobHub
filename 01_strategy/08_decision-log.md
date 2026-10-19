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
- **Decision:** `_drafts/` remains exploratory; `01_strategy/` contains curated working strategy.
- **Reason:** Preserve exploration without making unfinished notes the source of truth.

### Product surface remains open

- **Status:** Accepted working assumption
- **Decision:** Do not lock mobile, web, desktop, browser extension, or multi-surface delivery before research.
- **Revisit trigger:** Product-surface research and prototype evidence.

### Specifications should scale with certainty

- **Status:** Proposed
- **Decision:** Use lightweight behavior descriptions during discovery and more formal specifications for stable, critical workflows.
- **Revisit trigger:** Prototype and maintenance experience.

