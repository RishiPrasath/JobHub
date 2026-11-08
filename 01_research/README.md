# JobHub Research

Research produces evidence and findings. [Strategy](../strategy/README.md) interprets them into product and technical direction. Nothing here selects product scope, platform or architecture by itself.

## What is here

- [method/](method/00_research-charter.md): research charter, intent register, backlog and reusable instructions.
- [rounds/](rounds/README.md): decision-oriented research rounds, each holding dated runs with their own methods, sources and limitations.
- [sources/](sources/README.md): source material and provenance.
- [decks/](decks/README.md): presentations that summarise the research and approve nothing. Start with the [research briefing](decks/01_job-seeker-research-story/README.md).

## Rounds

| Round | Question | Status |
|---|---|---|
| [R00](rounds/R00-orientation-and-baseline/README.md) | What does existing desk research establish, and what stays uncertain? | Complete enough to proceed |
| [R01](rounds/R01-public-web-user-insights/README.md) | What public evidence exists on job-search problems, workflows, AI use and workarounds? | Bounded first pass closed; no priority decision |
| [R02](rounds/R02-job-seeker-pains-and-practices/README.md) | What pains, practices and guidance do job seekers report? | Bounded pass reviewed; owner acceptance outstanding |
| [R03](rounds/R03-cross-industry-job-search/README.md) | How does job search differ across industries, and how credible are vacancies? | Bounded pass reviewed; evidence partial; owner acceptance outstanding |
| [R04](rounds/R04-ai-assistance-and-trust/README.md) | How can AI assistance stay truthful, reviewable and under the job seeker's control? | Complete; draft synthesis, owner review pending |
| [R05](rounds/R05-technical-feasibility-and-ai-sdlc/README.md) | Which technical and tooling assumptions hold up? | Complete for three tooling runs; AI SDLC not examined; draft synthesis, owner review pending |
| [R06](../archive/research-rounds/R06-readiness-and-scope-decision/README.md) | What evidence supports an initial scope decision? | Retired to archive; never run |
| [R07](rounds/R07-competitive-landscape/README.md) | How do competing products work, and what do they charge? | First pass complete on public sources; owner decisions pending |
| [R08](rounds/R08-market-value-and-salary-benchmarking/README.md) | How are market value and salary benchmarks determined, and how reliable are they? | First pass complete; draft synthesis, owner review pending |
| [R09](rounds/R09-job-seeker-processes-as-is/README.md) | What processes do job seekers actually follow from search to first day? | First pass and gap-fill complete; draft synthesis, owner review pending |

The [rounds index](rounds/README.md) has links to each synthesis and gate.

## Where conclusions live

- Each round's conclusions are in its `round-synthesis.md`, and its proposed next action is in `decision-gate.md` where one exists. R00's promoted synthesis is the [cross-research synthesis](rounds/R00-orientation-and-baseline/results/00_cross-research-synthesis.md).
- Run-level detail is in `rounds/<round>/runs/<date-topic>/`, usually with `findings.md` and `limitations.md`.
- Completing a round accepts nothing. Accepted product and technical decisions are recorded in the [decision log](../strategy/08_decision-log.md).
