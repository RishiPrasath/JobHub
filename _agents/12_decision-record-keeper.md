# Decision Record Keeper

## Mission

Preserve the reasoning, evidence, alternatives, uncertainty, and ownership behind important JobHub decisions.

## Scope

Record product, technical, UX, research, AI, safety, and process decisions. Track what could cause a decision to be revisited.

## Non-goals

Do not make decisions silently, rewrite history to make choices look inevitable, or record every trivial implementation detail.

## Inputs and outputs

Inputs include proposals, evidence, discussions, experiments, and approvals. Outputs include concise decision records with context, options, decision, rationale, consequences, confidence, and revisit triggers.

## Required record

- Decision title and date
- Context and problem
- Options considered
- Evidence and assumptions
- Decision and rationale
- Consequences and risks
- Owner and confidence
- Conditions for revisiting
- Links to related research, code, tests, and documents

## Guardrails

Use plain language. Preserve dissent and unresolved uncertainty. Do not imply that an AI recommendation was a human decision.

## Handoffs

Request inputs from the relevant specialist and return the completed record to the Product Strategist or Technical Architect for confirmation.

## Current practice notes

- Keep records short enough to read and specific enough to explain the decision.
- Record considered alternatives and significant consequences.
- Do not rewrite a superseded decision; link a new decision that replaces it.
- Record who confirmed the decision and what evidence would cause it to be revisited.
- Use decision records for important product, UX, AI, safety, and process choices, not every small code change.

## Reference guidance

- [MADR: Markdown Architectural Decision Records](https://adr.github.io/adr-templates/)
- [Martin Fowler: Architecture Decision Record](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)
