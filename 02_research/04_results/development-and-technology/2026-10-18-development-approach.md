# Development approach and owner control

Date: 2026-10-18. Reviewed recommendation, not adopted method or completed experiment.

The [development report](../../03_research-rounds/00_orientation-and-baseline/runs/2026-10-18-remaining-research/development-method.md) evaluates all three supplied playbooks, independent/observational productivity evidence and specification/TDD/BDD alternatives. Vendor outcomes and older controlled results do not establish the fastest method for this project.

Propose a hybrid: one user outcome, explicit exclusions, a few behavior examples, a prototype for uncertainty, a narrow implementation and verification against independently agreed expectations. Expand the specification for costly reversals or repeated ambiguity. The report supplies a minimal slice template, quality gates, debt/rollback guidance and owner-learning exercises.

Use Gherkin selectively; adding Cucumber is justified only if executable examples improve shared understanding and regression detection enough to pay for maintenance. A Markdown example table linked to ordinary tests is a valid alternative. Generated tests must not simply copy the implementation's current output.

The [Codex/delivery report](../../03_research-rounds/00_orientation-and-baseline/runs/2026-10-18-remaining-research/codex-and-delivery.md) recommends native delegation with bounded ownership, concise context and integrated review. Local inspection found portable roles but no project `.codex` configuration; no setup changes were made. Tool availability does not prove web research occurred—retain actual search/open evidence.

Measure accepted quality, total effort, review/rework, maintenance and owner understanding, not output volume. The owner should explain data flow, failure handling, test rationale and recovery. [V05](../../03_research-rounds/00_orientation-and-baseline/runs/2026-10-18-remaining-research/validation-next.md) defines the canonical method comparison, conditional configuration smoke test and separate parallelism comparison.

[Review corrections](../../03_research-rounds/00_orientation-and-baseline/runs/2026-10-18-remaining-research/review.md) reconcile those experiments. No productivity benchmark, implementation test or native custom-agent load test ran here.
