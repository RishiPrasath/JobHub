# Round 03 agents and ownership

Status: execution design only. Three native subagents helped plan the round: sector/occupation coverage, query strategy, and vacancy-credibility evidence review. This does not mean substantive research has run, nor does a Markdown role definition create a new native runtime agent type.

## Sequence and bounded concurrency

1. **Research Planner/coordinator** adopts the brief, confirms the evidence-only boundary and assigns a single dated run when execution is authorised.
2. **Research Query Strategist** reads the brief, sector map and previous gaps, then finalises the query portfolio and shared log before collectors browse. Menu variants are alternatives, not extra query allowance.
3. **Job Domain + Practices specialists** perform the breadth pass; the coordinator selects six contrasting baskets with written rationale.
4. **Three collection workers** cover two selected baskets each. They apply Job Domain Researcher and Job-Seeker Practices Researcher role definitions, not a generic software-developer lens. A fourth bounded worker may own the shared vacancy-credibility strand.
5. **Evidence Synthesizer** consolidates source families, comparison and limitations after collection. This is reconciliation, not a fresh unbounded search sweep.
6. **Independent Responsible AI / Quality reviewer** checks status/intent inferences, survey methods, source independence, sector attribution, completeness and privacy. UX Expert adds access/comprehension review only where needed.
7. The **Product Strategist** proposes evidence-linked questions or candidate comparisons for `03_analysis/`; the **Decision Record Keeper** records only decisions actually accepted by the owner.

Keep no more than four simultaneous collectors and no more than five specialists active overall. Planning/query and synthesis/review stages need not all run concurrently. A collector must not review its own consequential employer-intent claim as independent validation.

## Responsibilities and write boundaries

| Assignment | Primary role | Bounded responsibility | Own files in a future dated run |
| --- | --- | --- | --- |
| Coordination and shared registers | Research Planner | Question, allocation, run status, budgets and merge | `brief.md`, `query-log.md`, `sources.md`, `observations.md`, `coverage.md`, `README.md` |
| Retrieval design | Research Query Strategist | Vocabulary, official/experience/contrary routes, logging and fallback allocations | Adopted `query-plan.md`; no silent edits to brief or findings |
| Sector worker A | Job Domain + Practices | First two chosen baskets, labelled after breadth selection | `sectors/<Sxx>.md` and `contributions/worker-a.md` |
| Sector worker B | Job Domain + Practices | Next two chosen baskets | `sectors/<Sxx>.md` and `contributions/worker-b.md` |
| Sector worker C | Job Domain + Practices | Last two chosen baskets | `sectors/<Sxx>.md` and `contributions/worker-c.md` |
| Shared credibility strand | Job Domain, with Responsible AI lens | Definitions, intent evidence, methods and contrary cases | `vacancy-credibility.md`, `contributions/credibility.md` |
| Integration | Evidence Synthesizer | One comparison, contradictions, claim confidence and limits | `comparison.md`, `findings.md`, `limitations.md` |
| Independent review | Responsible AI Reviewer + Quality and Evaluation Engineer | Evidence and boundaries, not product acceptance | `review.md`; corrections returned to owners |

Sector workers return query/source/observation contributions to the coordinator. Only the coordinator merges shared ledgers, with qualified source and family IDs. Do not let three workers edit a common spreadsheet/Markdown register simultaneously. Sources reused across baskets keep one origin/family identity; add routes rather than duplicate evidence votes.

## Required handoff

Every specialist reports task/scope, exact files and original sources inspected, performed versus planned searches, findings/observations separated from interpretations, source IDs, confidence and limits, contrary evidence, assumptions, gaps, risks, next action, files changed and validation performed. Return actual executed query strings and any remaining budget to the coordinator.

For every proposed claim about hiring intent, hand off the requisition/time scope, original observation or statement, source dependence, plausible alternatives, what remains unknown and whether independent corroboration exists. Ambiguous cases and any proposed deception finding need separate review; disagreement stays visible.

The [presentation specialist](../../../_agents/18_research-presentation-strategist.md) may brief accepted/reviewed research later, but slide creation is not part of this planning task. Full-Stack Developer, architecture work and AI-provider benchmarking are not default assignments for this round.
