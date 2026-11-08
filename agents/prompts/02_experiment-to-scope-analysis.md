# Prompt: Convert AI Experiment Findings into JobHub Scope

## Objective

Use the completed AI experiments and existing JobHub 02_analysis/reports to define the first narrow, testable product workflow for JobHub.

The goal is not to design the entire application. The goal is to decide what one user episode should be tested next, what capability supports it, and what must remain out of scope.

## Working context

JobHub is an exploratory Singapore-first, cross-industry job-search intelligence and application-preparation concept. The product scope, platform, technology stack and architecture are not final.

The current experiment evidence suggests that AI is promising for:

- organising job-posting evidence;
- preserving unknowns and contradictions;
- generating verification questions;
- supporting human review.

The experiments also found important failures in:

- holistic candidate-profile comparison;
- truthful resume alignment;
- output-schema consistency;
- cross-role contamination in broader workflows.

Treat these findings as bounded evidence, not universal claims about AI or job seekers.

## Required inputs

Read these files before making recommendations:

- `AGENTS.md`
- `02_analysis/reports/README.md`
- `02_analysis/reports/02_first-scope-decision-brief.md`
- `02_analysis/reports/03_role-pursuit-opportunity-hypothesis.md`
- `02_analysis/reports/05_role-pursuit-walkthrough.md`
- `02_analysis/reports/06_manual-vs-ai-review-comparison.md`
- `02_analysis/reports/07_role-pursuit-learning-test-results.md`
- `02_analysis/reports/08_role-pursuit-evidence-audit.md`
- `04_experiments/E01-07-sequential-sdk-run/findings.md`
- `04_experiments/README.md`
- `tools/openai-sdk/briefing.md`
- `04_experiments/E01-07-sequential-sdk-run/draft-report.md`

Also inspect the Round 4 source records referenced by those files, especially the three captured postings:

- R4-JB-003 — Class 4 Driver
- R4-JB-006 — Vehicle Mechanic
- R4-JB-011 — Part-Time Admin Assistant

## Specialist coordination

Use no more than three bounded specialists if parallel subagents are available:

1. **Evidence Synthesizer** — reconcile experiment findings, confidence and limitations.
2. **Product Strategist** — turn the evidence into one opportunity statement, capability boundary and scope decision.
3. **UX Expert** — define the smallest coherent user flow and identify usability, accessibility and correction risks.

The coordinator must reconcile their reports. Specialists should not edit the same files. Every report must distinguish evidence, inference, uncertainty, risk and recommendation.

## Required 02_analysis/reports tasks

1. Summarise what the experiments actually established.
2. Separate demonstrated capabilities from failed or untested capabilities.
3. Identify the most defensible first user episode.
4. Write one concise opportunity statement.
5. Define the smallest coherent capability that could be tested.
6. Define explicit non-goals for the first slice.
7. Map the required user flow from input to next action.
8. Identify where human review and correction are mandatory.
9. Define success, harm, stop and revisit conditions.
10. Identify the highest-risk assumptions that remain untested.
11. Recommend whether the next step is more research, a manual workflow, a low-fidelity prototype or implementation planning.

## Proposed direction to evaluate

Evaluate this as a hypothesis, not a predetermined decision:

> Help a job seeker understand what a job posting says, what is missing or conflicting, and what they should verify before spending more time on the role.

The 02_analysis/reports must be willing to reject or revise this direction if the evidence does not support it.

## Scope boundaries to preserve

Do not turn the first scope into any of the following:

- a universal job-fit score;
- a hiring-probability prediction;
- an automatic scam or legitimacy verdict;
- autonomous candidate ranking;
- automatic resume rewriting;
- automatic answers to sensitive eligibility questions;
- employer messaging or application submission;
- a final platform, stack or architecture decision.

## Required output

Create or update one 02_analysis/reports document:

`02_analysis/reports/09_experiment-to-scope-decision.md`

Use this structure:

1. Status and date
2. Decision question
3. Evidence reviewed
4. What the experiments established
5. What failed or remains unproven
6. Selected user episode
7. Opportunity statement
8. Smallest coherent capability
9. Proposed user flow
10. Human-control and safety boundaries
11. Explicit non-goals
12. Success criteria
13. Harm and stop conditions
14. Highest-risk assumptions
15. Recommended next action
16. Owner decision required

Include a table with these columns:

| Proposed capability | Evidence supporting it | Evidence against or limitation | Status |
|---|---|---|---|

Use status values such as `candidate`, `test next`, `defer`, `rejected` or `unproven`.

## Decision standard

The output must not claim that a feature is validated merely because a model produced a plausible response. A capability may be recommended for prototype testing only when:

- the user episode is clear;
- the evidence and limitations are visible;
- the workflow is small enough to test;
- the AI boundary is explicit;
- human correction is possible;
- success and failure conditions are defined.

## Approval boundary

The coordinator may update the 02_analysis/reports document and create the recommendation. The following remain under owner control:

- final product scope;
- product non-goals;
- privacy and responsible-AI decisions;
- platform, architecture and provider choices;
- acceptance of the first prototype or implementation slice.

Do not implement application code, choose a technology stack, contact users or external parties, send applications, commit, push or deploy anything as part of this prompt.

## Verification requirements

Before reporting completion:

- confirm every major recommendation links to supporting evidence;
- preserve disagreements between specialists;
- label desk simulation results as simulations, not user research;
- run `git diff --check` if files were changed;
- report files changed and unresolved owner decisions;
- do not claim user validation, accessibility validation or production readiness.
