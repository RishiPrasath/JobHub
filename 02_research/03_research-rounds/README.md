# Research Rounds

Research rounds group related research runs around one decision or transition. A round is larger than an individual evidence-collection run but smaller than the entire product strategy.

## Round sequence

| Round | Purpose | Status |
|---|---|---|
| [00 — Orientation and baseline](00_orientation-and-baseline/README.md) | Consolidate the completed desk research and make remaining uncertainty explicit | Complete enough to proceed |
| [01 — Public web user insights](01_public-web-user-insights/README.md) | Collect public evidence about job-search problems, workflows, AI use, and workarounds | Bounded first pass closed with targeted gap stop check; no priority decision |
| [02 — Job-seeker pains, practices, and guidance](02_synthetic-workflow-selection/README.md) | Public experiences, practical guidance, video captions, and authorised internal process review; prior fictional run retained | Bounded pass complete and independently reviewed; product recommendations await owner acceptance |
| [03 — Cross-industry job search and vacancy credibility](03_cross-industry-job-search/README.md) | Compare sector/occupation hiring experiences beyond IT; investigate fake/ghost postings with careful intent evidence | Bounded pass reviewed; 13 profiles, six non-IT deep dives and updated slides; partial evidence, owner acceptance outstanding |
| [04 — AI assistance and trust](04_ai-assistance-and-trust/README.md) | Define useful AI assistance, approval points, evidence presentation, and uncertainty handling | Planned |
| [05 — Technical feasibility and AI SDLC](05_technical-feasibility-and-ai-sdlc/README.md) | Test technical and development-process assumptions | Planned |
| [06 — Readiness and scope decision](06_readiness-and-scope-decision/README.md) | Consolidate evidence for a human-owned initial scope decision | Planned |

Rounds are a sequence of gates, not a promise to complete every folder. A gate may stop, repeat, narrow, defer, or advance the work.

Round 03's unused UX placeholder was replaced at the owner's request with cross-industry research. Its [original note](03_cross-industry-job-search/prior-ux-plan.md) is preserved. Access/device context remains in the new comparison; a broader UX/platform study is deferred. Rounds 04–06 are not renumbered, and dated audit inventories retain their historical paths.

## Standard round structure

```text
NN_round-purpose/
├── README.md
├── round-brief.md
├── run-index.md
├── runs/
│   └── YYYY-MM-DD-topic-slug/
│       ├── README.md
│       ├── brief.md
│       ├── query-plan.md       # when public or broad retrieval is used
│       ├── query-log.md        # when public or broad retrieval is used
│       ├── sources.md
│       ├── observations.md     # when direct observations are collected
│       ├── findings.md
│       └── limitations.md
├── round-synthesis.md
└── decision-gate.md
```

## Responsibilities

- `round-brief.md` defines the decision, questions, scope, exclusions, assigned agents, evidence standard, budget, and stopping rule.
- `run-index.md` lists each run, its status, and the questions it covers.
- `runs/` preserves the detailed method and evidence record for each bounded activity.
- `round-synthesis.md` compares the runs and records what the round established, contradicted, or left unresolved.
- `decision-gate.md` proposes the next action. It is not a human acceptance record; accepted decisions belong in `06_research-decisions/` and, when durable, `01_strategy/08_decision-log.md`.

## Current operating rule

Round 01 is public-web-only because the owner currently has no direct user access. It must not be expanded into interviews, private-group research, author contact, profiling, purchases, live applications, or claims of representative prevalence. The Research Query Strategist works immediately after the Research Planner and before evidence-collection specialists.

