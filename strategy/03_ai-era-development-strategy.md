# AI-Era Development Strategy

## Purpose

JobHub needs a development approach that is technically responsible and explainable without turning early discovery into a slow specification exercise. Detailed specifications should grow with certainty rather than precede learning.

## Working development model

Use a staged, evidence-driven approach:

1. Explore the problem and user flow.
2. State the smallest useful behavior and acceptance conditions.
3. Prototype or implement a narrow slice.
4. Test it with automated checks and realistic examples.
5. Review the result for UX, security, accessibility, and technical coherence.
6. Record material decisions and revise the strategy when evidence changes.

AI may assist at each stage, but the product owner remains responsible for understanding and approving important product and technical decisions.

## Gherkin and Cucumber

Gherkin and Cucumber should be evaluated as selective tools, not adopted as the entire method.

They may be valuable for critical user journeys such as capturing a posting, saving and resuming across devices, distinguishing evidence from interpretation, comparing a job with a profile, preparing an application, and tracking an application.

They should not describe every implementation detail. They do not replace discovery, UX design, architecture, unit tests, integration tests, exploratory prototypes, or decision records.

The research question is: where does executable behavior specification provide enough value to justify its maintenance cost?

## User-proposed development research

- How to remain technically responsible without slowing discovery.
- How specifications should change as requirements change.
- How Gherkin relates to other tests and specifications.
- How AI should create, review, maintain, and execute behavior scenarios.
- How to improve user-flow and UX design while developing with AI.
- How to use AI as a design partner without outsourcing product judgment.
- How to make interfaces intuitive and accessible without formal UI training.
- How to evaluate flows, content, visual hierarchy, error recovery, keyboard use, screen readers, contrast, text scaling, and motion.
- How to test usability with real users or realistic exercises.

## Recommended development research

### AI-assisted development model

Determine which SDLC activities should be AI-assisted, AI-generated, human-led, or human-only, and how much specification is appropriate at different levels of uncertainty.

### Codex and agent workflows

Research bounded specialist roles, parallel versus sequential agents, coordination, handoffs, approval gates, context management, and preventing overlapping edits.

### Context and knowledge management

Define how `AGENTS.md`, strategy documents, prompts, plans, decision records, and project memory should remain concise, portable, and resistant to stale instructions.

### Evaluation-driven AI development

Create representative datasets and evaluate factuality, evidence grounding, uncertainty, usefulness, accessibility, consistency, tool selection, handoffs, and quality drift.

### Secure and responsible AI SDLC

Address prompt injection, sensitive-information disclosure, unsafe output handling, excessive agency, supply-chain risk, permissions, auditability, and approval for consequential actions.

### Software quality and technical debt

Study review, testing, debugging, generated-test quality, architecture coherence, dependency risk, duplication, rollback, repair, and recovery from bad changes.

### UX learning with AI

Use AI to teach and critique UX, while validating flows with heuristics, prototypes, usability testing, and accessibility evaluation.

### Tool and model selection

Compare models and tools using JobHub-specific tasks, cost, latency, reliability, privacy, portability, context limits, vendor lock-in, and deterministic alternatives.

### Delivery and personal skill development

Define branch, worktree, approval, and integration practices. Identify the product owner's learning goals so agents act as tutors and reviewers rather than replacements for understanding.

## Reference sources to review

- [The AI-Native SDLC Playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)
- [AI SDLC Transformation Playbook](https://www.atlassian.com/blog/ai-at-work/ai-sdlc-transformation-playbook)
- [AI-Driven SDLC: How to Build Secure, Governed, and Scalable](https://www.linkedin.com/pulse/ai-driven-sdlc-how-build-secure-governed-scalable-withai-ran-isenberg-99nuf/)

These are research inputs, not automatically accepted practices. Claims should be checked against primary documentation, observed experiments, and JobHub's needs.

