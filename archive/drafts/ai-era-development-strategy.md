# AI-Era Development Strategy

## Purpose

This draft explores how JobHub should be designed and developed in an era where AI can assist with research, design, implementation, testing, documentation, and review.

The goal is to find an approach that is:

- Technically responsible
- Flexible when product and technical decisions change
- Fast enough to support learning through implementation
- Understandable and explainable by the product owner
- Deliberate about quality, testing, privacy, security, and maintainability

Spec-driven development is one approach to evaluate. It may provide useful clarity, but applying detailed specifications too early or too broadly may slow down discovery and development.

## Development Practices Under Consideration

### Gherkin Syntax and Cucumber

Gherkin syntax and Cucumber should be evaluated as one technique within the development approach, not as the complete development method.

Gherkin describes expected behavior in readable scenarios:

```gherkin
Feature: Save a job posting

  Scenario: Save a posting for later
    Given I am viewing a job posting
    When I choose to save it
    Then the posting is added to my saved jobs
    And its source URL is preserved
```

Cucumber can connect these scenarios to automated acceptance tests.

#### Potential value for JobHub

- Keeps requirements focused on user behavior
- Creates a shared language between product, design, AI, and development
- Defines acceptance criteria before implementation
- Tests important end-to-end workflows
- Reduces ambiguity in AI-generated code
- Preserves the reason a feature exists

#### Limitations and risks

Gherkin should not be used to describe every implementation detail or every small behavior. Excessive use can make development slow and create a large suite of difficult-to-maintain scenarios.

Gherkin and Cucumber do not replace:

- Product discovery
- Technical architecture
- UX design
- Unit and integration tests
- Technical decision records
- Exploratory prototypes

#### Candidate workflows for selective use

Gherkin may be particularly useful for critical JobHub user journeys, such as:

- Capturing a job posting
- Saving and resuming a job across devices
- Analysing a posting while distinguishing evidence from interpretation
- Comparing a job with a user profile
- Preparing an application
- Tracking an application

#### Research question

The question is not whether Cucumber should be used everywhere. The question is:

> Where does executable behavior specification provide enough value to justify the effort?

The eventual development approach should determine when Gherkin scenarios are appropriate, how they relate to other tests and specifications, and how AI tools should help create, review, maintain, and execute them.

## Reference Sources to Review

- [The AI-Native SDLC Playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) — Claude resource to review for AI-native software-development lifecycle practices, workflow changes, human responsibilities, and recommendations that may be relevant to JobHub.
- [AI SDLC Transformation Playbook](https://www.atlassian.com/blog/ai-at-work/ai-sdlc-transformation-playbook) — Atlassian resource to review for AI-related changes to software-development lifecycle practices, team workflows, delivery processes, and organisational adoption.
- [AI-Driven SDLC: How to Build Secure, Governed, and Scalable](https://www.linkedin.com/pulse/ai-driven-sdlc-how-build-secure-governed-scalable-withai-ran-isenberg-99nuf/) — LinkedIn article to review for security, governance, scalability, and control considerations in AI-driven software development.

## Research Topics for Further Investigation

### Your Research Topics

Topics you identify will be recorded here as they arise.

#### Topics raised so far

- Whether Gherkin and Cucumber should be used for selected JobHub workflows
- How executable behavior specifications should relate to other tests and specifications
- How AI tools should help create, review, maintain, and execute Gherkin scenarios
- How to remain technically responsible without allowing detailed specifications to slow discovery and development
- How to improve user-flow design and UX decision-making while developing with AI
- How to use AI as a design partner without outsourcing product judgment
- How to identify user goals, context, friction, uncertainty, and failure states
- How to turn research and product ideas into clear user flows before implementation
- How to evaluate whether a proposed flow is understandable, accessible, and useful
- Which UX and product-design practices are essential to learn personally versus delegate to AI tools
- How someone without formal UI experience can learn the principles needed to make interfaces intuitive
- How to design clear information architecture, navigation, labels, and page structure
- How to use visual hierarchy, spacing, grouping, contrast, and consistency to guide attention
- How to make controls understandable through familiar patterns, affordances, and feedback
- How to design useful loading states, empty states, confirmations, undo actions, and error recovery
- How to write clear, humane, and accessible interface text
- How to reduce cognitive load when users are reviewing complex job and career information
- How to design for users with different abilities, devices, screen sizes, languages, and levels of digital confidence
- How to research and apply accessibility standards without treating accessibility as a final checklist
- How to evaluate keyboard navigation, screen-reader use, focus order, colour contrast, text scaling, and motion
- How to test whether an interface is intuitive with real users or realistic usability exercises
- How AI can critique interfaces, generate alternative flows, identify accessibility risks, and explain the reasoning behind design choices
- How to recognise when AI-generated UI patterns are attractive but confusing, inaccessible, or unsuitable for the product context

### Recommended Research Topics

### AI-Assisted Development Model

- Which parts of the SDLC should be AI-assisted, AI-generated, human-led, or explicitly human-only
- How to choose between exploratory work, lightweight specifications, test-driven development, behaviour-driven development, and hybrid approaches
- How much specification is useful at each stage of uncertainty
- How to measure production-qualified value rather than generated code volume

### Codex and Agent Workflow Design

- How to define bounded specialist roles without creating unnecessary agent sprawl
- When to use one agent, parallel subagents, sequential handoffs, or ordinary conversation
- How coordinators should allocate work, reconcile disagreement, and preserve human approval
- How agent context, repository instructions, prompts, skills, and plans should be organised
- How to prevent multiple agents from editing overlapping files or creating semantic conflicts

### Context Engineering and Knowledge Management

- What repository context agents actually need for reliable work
- How to keep `AGENTS.md`, strategy documents, prompts, plans, and decision records concise and non-duplicative
- How to provide progressive disclosure instead of loading every instruction into every task
- How to preserve project memory while preventing stale instructions from controlling new work
- How to make prompts, role definitions, and decisions portable across AI tools

### Evaluation-Driven AI Development

- How to build representative datasets for JobHub’s research, UX, coding, and analysis workflows
- How to evaluate factuality, evidence grounding, uncertainty, usefulness, accessibility, and consistency
- How to evaluate tool selection, handoffs, permissions, and coordinator decisions
- When to use human review, automated checks, model graders, traces, or end-to-end tests
- How to detect quality drift after model, prompt, data, tool, or workflow changes

### Secure and Responsible AI SDLC

- How to protect source code, personal data, credentials, and research materials when using AI tools
- How to address prompt injection, sensitive-information disclosure, improper output handling, excessive agency, and supply-chain risks
- How to assign permissions according to action risk, reversibility, and impact
- Where approval gates are required for external writes, migrations, deployments, or consequential recommendations
- How to monitor, audit, and respond to unsafe or unexpected agent behaviour

### Software Quality and Technical Debt

- How AI-generated code changes review, testing, debugging, and maintenance effort
- How to prevent generated tests from merely describing the implementation instead of the intended behaviour
- How to preserve architecture coherence while implementing small AI-generated changes
- How to detect duplication, accidental complexity, dependency risk, and undocumented decisions
- How to handle rollback, repair, and recovery when an agent produces a bad change

### UX and Design Learning with AI

- How to use AI to learn UX principles without replacing real user research
- How to evaluate AI-generated flows, wireframes, content, and interfaces for usability and accessibility
- How to combine heuristic review, prototypes, usability testing, and accessibility evaluation
- Which UX and UI skills should be developed personally to retain design ownership
- How AI affects the quality of product decisions when the owner has limited design experience

### Tool and Model Selection

- How to compare AI tools and models using JobHub-specific tasks rather than general benchmarks alone
- How to evaluate cost, latency, context limits, reliability, privacy, portability, and vendor lock-in
- When a deterministic workflow is safer than an agentic workflow
- How to design model and provider substitution without premature abstraction
- How to keep tool-specific details at the runtime boundary while preserving portable role definitions

### Delivery and Collaboration

- How to organise branches, worktrees, approvals, and integration when agents work in parallel
- How to design human-gated phases with clear acceptance and verification criteria
- How to keep research, planning, implementation, review, and deployment responsibilities distinct
- How to maintain an auditable record of prompts, agent outputs, decisions, tests, and changes
- How to determine when a workflow is mature enough to automate further

### Personal Skill Development

- Which software-engineering, product, UX, architecture, and AI concepts the owner should learn directly
- How to use agents as tutors, reviewers, and collaborators rather than replacements for understanding
- How to explain and defend technical decisions made with AI assistance
- How to identify skill gaps from repeated agent handoffs, review findings, or misunderstood outputs
