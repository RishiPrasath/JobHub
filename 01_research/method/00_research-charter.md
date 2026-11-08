# Research Charter

## Purpose

JobHub research reduces uncertainty before product, UX, technical, and process decisions are locked. It should help answer what problem matters, for whom, in what context, and what a responsible solution would require.

## Scope

Research may cover:

- Job-seeker workflows and cross-industry needs.
- AI-assisted job hunting and automation trade-offs.
- Job postings, company research, labour-market context, and evidence quality.
- Product surface, UX, accessibility, and interrupted cross-device workflows.
- Competition, positioning, naming, and sustainability.
- AI-era development, Codex workflows, specifications, testing, and evaluation.
- Technical architecture, privacy, security, responsible AI, and operating constraints.

## Research principles

1. Start with a decision or uncertainty, not a topic for its own sake.
2. Use the smallest research activity that can reduce the uncertainty.
3. Separate observed facts, source claims, interpretations, hypotheses, and unknowns.
4. Preserve source location, date, scope, method, and limitations.
5. Treat AI output and external content as untrusted inputs that require review.
6. Include contradictory evidence instead of smoothing it away.
7. Do not generalise from a single anecdote, review, or vendor claim.
8. Prefer user behavior and realistic workflow evidence over feature popularity.
9. Keep product, ethical, and technical decisions human-owned.
10. Turn results into strategy only when the evidence and uncertainty are explicit.

## Research outputs

- A **research question** states what is unknown and which decision it informs.
- A **research instruction** defines the method, evidence requirements, assigned agents, and output format.
- A **research run** records one dated activity and its raw observations.
- An **evidence record** preserves a source or dataset with provenance.
- A **result** synthesizes multiple observations into a traceable conclusion.
- A **research decision** states an implication that may change product or development direction.

## Agent collaboration

Every substantive research task has:

- One primary agent accountable for the research question.
- Zero or more supporting agents with distinct responsibilities.
- One Evidence Synthesizer responsible for claim traceability and contradictions.
- A specialist reviewer when the task involves UX, technical, quality, privacy, safety, or fairness risk.
- A human decision owner for consequential conclusions.

The assignment rules are defined in [`02_instructions/01_agent-assignment-and-coordination.md`](02_instructions/01_agent-assignment-and-coordination.md).

## Relationship to strategy

Research results are stored here. Product and development strategy live in [`01_strategy/`](../01_strategy/). A result may recommend a strategy update, but it does not silently become a requirement or decision.

