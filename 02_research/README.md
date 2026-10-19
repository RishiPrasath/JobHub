# JobHub Research

This folder contains the instructions, active research work, evidence, and results used to inform JobHub strategy and product decisions.

The research folder is separate from [`01_strategy`](../01_strategy/). Research produces evidence and findings; strategy interprets that evidence into product and technical direction.

## Current research status — 2026-10-18

The original topic lists remain in the drafts, indexed by the [research intent register](00_research-intent-register.md). Round 00 is prior desk research; Round 01's bounded public-web pass is completed and reviewed. The owner authorised an [expanded Round 02 evidence pass](03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/README.md) on job-seeker pains, practical guidance, video captions, and a bounded internal process review. Its earlier fictional comparison stays historical. Direct interviews, product/device tests, live tool comparisons and launch clearance are not claimed complete.

## Research-round structure

```text
02_research/
├── README.md
├── 00_research-intent-register.md
├── 00_research-charter.md
├── 01_research-backlog.md
├── 02_instructions/
│   ├── README.md
│   ├── 00_common-research-protocol.md
│   ├── 01_agent-assignment-and-coordination.md
│   ├── 02_product-and-user-research.md
│   ├── 03_ai-job-hunting-and-automation.md
│   ├── 04_competitive-and-market-research.md
│   ├── 05_product-surface-and-ux-research.md
│   ├── 06_ai-era-development-research.md
│   └── 07_technical-and-responsible-ai-research.md
├── 03_research-rounds/
│   ├── README.md
│   ├── 00_orientation-and-baseline/
│   │   ├── README.md
│   │   ├── round-brief.md
│   │   ├── run-index.md
│   │   ├── runs/YYYY-MM-DD-topic-slug/
│   │   ├── round-synthesis.md
│   │   └── decision-gate.md
│   ├── 01_public-web-user-insights/
│   │   ├── README.md
│   │   ├── round-brief.md
│   │   ├── runs/YYYY-MM-DD-topic-slug/
│   │   ├── round-synthesis.md
│   │   └── decision-gate.md
│   ├── 02_synthetic-workflow-selection/  # expanded pain/practice research; prior run historical
│   └── 03+_future-decision-oriented-rounds/
├── 04_results/
│   ├── README.md
│   ├── 00_cross-research-synthesis.md
│   ├── product-and-users/
│   ├── ai-and-job-hunting/
│   ├── market-and-competition/
│   ├── ux-and-product-surface/
│   └── development-and-technology/
├── 05_evidence/
│   ├── README.md
│   ├── external/
│   ├── internal-job-hunt-workspace/
│   └── datasets-and-examples/
├── 06_research-decisions/
│   ├── README.md
│   └── YYYY-MM-DD-decision-slug.md
└── 07_presentations/
    ├── README.md
    ├── 00_research-findings/
    └── 01_job-seeker-research-story/
```

## Responsibilities of each area

### `00_research-charter.md`

Defines the purpose, research principles, evidence standards, scope, and relationship between research and strategy.

### `01_research-backlog.md`

Tracks research questions from the product research and AI-era development strategies. Each item should identify the decision it informs, priority, uncertainty, and recommended method.

### `02_instructions/`

Contains reusable instructions for conducting research. These should explain how to investigate a topic, what evidence to collect, how to handle uncertainty, and what output to produce. They are research procedures, not one-off results.

### `03_research-rounds/`

Contains decision-oriented research rounds. A round groups one or more bounded runs that answer a related decision. Each round has its own brief, run index, synthesis, and decision gate. Individual runs remain dated and preserve their own methods, sources, observations, findings, and limitations.

Rounds are numbered in sequence:

- `00_orientation-and-baseline` — completed desk-research baseline and known uncertainties.
- `01_public-web-user-insights` — next public-web-only evidence round for a solo founder without direct user access.
- `02_synthetic-workflow-selection` — select a bounded workflow to test without claiming user validation.
- `03_cross-industry-job-search` — bounded cross-industry collection conducted on 2026-10-19: 13 profiles, six non-IT deep dives, fake/ghost-posting evidence and explicit gaps; the former UX placeholder is preserved.
- `04_ai-assistance-and-trust` — define useful AI assistance, user approvals, evidence presentation, and uncertainty handling.
- `05_technical-feasibility-and-ai-sdlc` — test technical and development-process assumptions.
- `06_readiness-and-scope-decision` — consolidate evidence for a human-owned scope decision.

Future rounds are optional. A decision gate may stop, repeat, narrow, defer, or advance the work.

Every run should preserve its question, method, sources, observations, findings, and limitations.

### `04_results/`

Contains reviewed and synthesized findings organized by theme. Results should be concise enough to use, but traceable back to research runs and evidence.

### `05_evidence/`

Contains source records and supporting material. External sources, the internal Job Hunt workspace, and datasets/examples should remain distinguishable.

### `06_research-decisions/`

Contains conclusions that directly change product or development direction. These should link back to the relevant result and be reflected in `01_strategy/08_decision-log.md` when they become durable strategy decisions.

## Research lifecycle

```text
Research question
       ↓
Research instruction or protocol
       ↓
Research round brief
       ↓
One or more bounded runs
       ↓
Evidence and observations
       ↓
Round synthesis
       ↓
Decision gate
       ↓
Promoted result or strategy update
```

## Evidence rules

Research records should distinguish:

- Directly observed facts
- Source claims
- Interpretations and inferences
- AI-generated suggestions
- Contradictions
- Missing information
- Confidence and limitations

Research results should not silently turn an assumption into a requirement. When the evidence is weak or mixed, the result should say so and recommend the next useful experiment.

## Naming rules

- Numbered documents start at `00` within each ordered collection.
- Research rounds use `NN_round-purpose`.
- Runs inside a round use `YYYY-MM-DD-topic-slug`.
- Round-level synthesis and gates must link to the runs that support them.
- Results describe conclusions, not just the sources reviewed.
- Evidence records retain source date, access date, location, and relevance.

## Current operating order

For a reading overview before analysis, open the [storytelling research briefing](07_presentations/01_job-seeker-research-story/README.md). It includes an offline browser presentation with readable text, an editable PPTX, sources and limitations. The earlier briefing is preserved. Slides summarise the research and do not approve product decisions.

1. Preserve the full [owner and agent topic lists](00_research-intent-register.md) without turning them all into simultaneous studies.
2. Use the reviewed [Round 01 first pass](03_research-rounds/01_public-web-user-insights/round-synthesis.md) and its [narrow gate](03_research-rounds/01_public-web-user-insights/decision-gate.md) to guide any additional public retrieval.
3. Review the completed [Round 02 expanded evidence run](03_research-rounds/02_synthetic-workflow-selection/README.md) and proposed next task, keeping its historical fictional work distinct from public and internal evidence.
4. Promote a result into strategy only after its evidence and limitations support a human-owned decision.

Research update, 2026-10-19: the owner authorised [Round 03 cross-industry research](03_research-rounds/03_cross-industry-job-search/README.md), industry profiles and updated slides. Bounded collection is complete; integration/review and presentation finalisation are tracked there. Evidence remains partial and does not select scope for `03_analysis/`.

