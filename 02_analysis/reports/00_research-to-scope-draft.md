# From research to product scope — working draft

Status: revised after web research and specialist review — 2026-10-19

## Purpose

This document proposes a disciplined way to turn JobHub’s research into meaningful product scope without treating every observation as a feature request. It is a working method, not a product decision.

## Decision this analysis should support

Which user problem, workflow and smallest coherent capability should JobHub test first, given the evidence already collected, the remaining uncertainty, and the risks of misleading or over-automating job preparation?

## Current evidence base

- Research rounds 1–4 under `02_research/`.
- The Round 4 job-posting page inventory.
- Round 4 remaining-objectives evidence on industry fit, truthful tailoring, ATS/accessibility, market value, AI-assisted job seeking and trust.
- The user’s original product ideas and strategy drafts.

The analysis must distinguish source observations, interpretations, hypotheses, product opportunities, decisions and unresolved questions.

## Proposed evidence-to-scope pipeline

```text
Owner decision to support
    ↓
Context and whole-journey episode
    ↓
Source register, evidence ledger and claim map
    ↓
Needs, pains, constraints and desired outcomes
    ↓
Opportunity statements and competing interpretations
    ↓
Riskiest assumptions and evidence gaps
    ↓
Smallest coherent learning slice
    ↓
Prototype / manual baseline / controlled experiment
    ↓
Evaluation: usefulness, grounding, recovery, accessibility and harm
    ↓
Human-owned scope decision, non-goals and revisit trigger
    ↓
Implementation slice and regression checks
```

## Rules for translating research

1. **Do not turn a topic into a feature.** “People use AI for resumes” is an observation. It is not automatically a resume generator.
2. **Preserve the chain of reasoning.** Every proposed capability should link to evidence, the user problem it addresses, the assumption it tests and the risk it introduces.
3. **Separate need from solution.** Record what the person is trying to accomplish before naming a screen, automation or technical component.
4. **Represent uncertainty explicitly.** Mark claims as observed, reported, interpreted, hypothesised, contradicted or unknown.
5. **Prefer reversible learning.** Prototype or test an uncertain workflow before committing to a large build or irreversible data model.
6. **Scope a complete slice.** A small slice must include the user goal, necessary inputs, output, review/control, failure state and evaluation method.
7. **Keep human decisions visible.** Product scope, non-goals, privacy boundaries, automation level and architecture remain owner decisions.

8. **Treat a feature as a hypothesis, not a conclusion.** A capability is only a candidate response until the underlying opportunity, assumption and test are explicit.

9. **Make the smallest slice a complete user episode.** It must include the relevant context, input, output, uncertainty, interruption, recovery, user control and evaluation—not merely the fewest screens.

10. **Use an experiment before an implementation commitment.** Desk research can establish context and plausible need; it cannot establish that a workflow is useful, understandable or effective for JobHub.

## Proposed analysis artefacts

### 1. Evidence ledger

| Field | Meaning |
|---|---|
| Claim ID | Stable reference |
| Source and date | Where and when the claim came from |
| Evidence type | Observed fact, reported claim, research result, guidance, interpretation or unknown |
| Population/context | Who, where, role, industry, seniority and arrangement |
| Confidence | High, medium or low with rationale |
| Contradictions | Supporting and disconfirming evidence |
| Implication | What it may change in the product conversation |

### 1a. Source register and lineage

The source register precedes the claim ledger. It prevents multiple articles, reposts, job-board syndications or vendor summaries from being counted as independent evidence.

```text
Source ID:
Canonical source/study/dataset:
Report/page/post ID:
Source type and owner:
Publication and access dates:
Population and context:
Method:
Parent study/project:
Duplicate/syndication relationship:
Locator or excerpt:
Captured version:
```

### 1b. Context-and-journey episode

Before translating a finding into a need, describe the complete episode:

```text
Episode and user/context:
Trigger and goal:
Current workaround:
Online, offline and human-support steps:
Device and environment:
Interruption points:
Missing, changing or conflicting information:
Desired outcome:
Consequence of misunderstanding or failure:
Evidence references:
Unknowns:
```

### 2. Problem and opportunity map

For each recurring problem:

- user and context;
- trigger and current workaround;
- desired outcome;
- friction, cost or harm;
- evidence references;
- affected segments and exclusions;
- unresolved assumptions;
- opportunity statement without prescribing a solution.

The map must distinguish:

```text
Observation → interpretation → need → desired outcome
→ opportunity → competing hypotheses → capability
```

Each opportunity should have at least two plausible interpretations before a feature is proposed. This protects against converting “people use AI for resumes” directly into “build a resume generator.”

### 3. Hypothesis card

```text
We believe [user/context] struggles with [problem]
because [evidence-backed cause].
If we provide [bounded capability],
then [observable behaviour or outcome] should improve.
We will test this by [method] using [measure].
We will not claim [outcome beyond the test].
```

### 4. Capability card

| Field | Required content |
|---|---|
| Capability | Plain-language description |
| Problem addressed | Linked problem IDs |
| Evidence | Claim/source IDs |
| User value | What becomes easier, clearer or safer |
| Inputs | What the user or system must provide |
| Outputs | What the user receives |
| Human control | Review, edit, reject, undo, export and approval points |
| Failure states | Missing, stale, conflicting, unsafe or inaccessible cases |
| Privacy/risk | Sensitive data, inference, bias, prompt injection or lock-in risk |
| Evaluation | Success, harm and learning measures |
| Scope | Now, next, later, experiment or out-of-scope |

### 5. Smallest coherent learning slice

The smallest slice is the smallest end-to-end episode capable of producing credible learning. It should state:

- target user and context;
- user goal and decision supported;
- realistic inputs and deliberately fake/incomplete inputs;
- output and explanation;
- missing, conflicting, stale, loading and failure states;
- review, edit, reject, annotate and undo controls;
- interruption and return behaviour;
- privacy, accessibility and safety checks;
- baseline/comparator;
- success, harm, stop and revise conditions;
- explicit non-goals.

### 6. AI-analysis record

AI may extract, cluster, compare, flag possible contradictions and draft candidate interpretations. It must not silently assign final confidence, resolve contradictions, invent prevalence, rank user needs, decide scope or promote a hypothesis to a requirement.

```text
AI run ID:
Input source IDs:
Prompt/version:
Model/tool/version:
Retrieval/tools used:
Raw output:
Suggested extraction/cluster/contradiction:
Human verification and disagreements:
Evidence status:
Downstream claim/opportunity/scope IDs:
Reviewer and date:
```

### 5. Scope decision record

Every material scope decision should record:

- decision and date;
- options considered;
- evidence supporting each option;
- assumptions and confidence;
- trade-offs and risks;
- what is explicitly not included;
- what would cause the decision to change;
- owner acceptance.

Use explicit statuses: `proposed`, `tested`, `accepted`, `rejected`, `deferred`, `out-of-scope`, and `unknown`.

## Prioritisation approach to research

Prioritise candidate problems and capabilities using a transparent conversation, not an unexplained score. Consider:

- importance of the user outcome;
- evidence strength and recurrence;
- harm if wrong;
- number and diversity of affected contexts;
- learning value;
- implementation and operational cost;
- reversibility;
- privacy, accessibility and responsible-AI risk;
- dependence on unresolved platform or data decisions.

Use categories before ordering:

- **Must learn:** uncertainty that could invalidate the direction.
- **Must test:** a risky or consequential workflow claim.
- **Smallest coherent build:** the narrow slice that creates and measures value.
- **Useful later:** valuable but dependent or not yet validated.
- **Out of scope:** intentionally excluded for this stage.

## Proposed first-pass analysis sequence

1. Build the evidence ledger from the completed research, without adding new features.
2. Cluster evidence into user needs, pains, constraints, workarounds and desired outcomes.
3. Identify contradictions and missing evidence before prioritising.
4. Create opportunity statements for the highest-consequence problems.
5. Convert opportunities into competing hypotheses, not a single assumed solution.
6. Define the smallest test for each high-risk hypothesis.
7. Draft scope options with explicit non-goals and human decision gates.
8. Review the options with UX, responsible-AI, quality and technical perspectives.
9. Select a candidate slice only after the owner accepts the evidence, trade-offs and test plan.

## Initial quality bar

No capability should enter proposed scope unless we can answer:

- Which user and context is it for?
- What evidence says the problem exists?
- What is the current workaround?
- What is the smallest useful outcome?
- What could go wrong?
- How does the user inspect, correct, reject or undo the result?
- What information must remain unknown rather than inferred?
- How will we evaluate usefulness, factuality, accessibility and harm?
- What would change our mind?

For AI-assisted analysis, also ask:

- Can every material claim be traced to source evidence or marked `unknown`?
- Were supporting, failure, contradiction and alternative-explanation searches performed?
- Did a human inspect the original evidence rather than only the AI summary?
- Are rejected interpretations and negative cases retained for future evaluation?
- Can the workflow fail closed when sources are missing, conflicts are unresolved or review is inaccessible?

## Explicit non-goals for this draft

- No final feature list.
- No platform, stack, architecture or AI-provider selection.
- No universal role-fit score, market-value score or ATS guarantee.
- No assumption that participant access exists.
- No autonomous application submission.
- No treating research volume, competitor presence or AI capability as proof of user value.

## Research questions for this method

- Which discovery-to-scope frameworks best preserve evidence while remaining practical for a solo product owner?
- How should qualitative, desk, market, competitive and technical evidence be combined without false precision?
- What is the right balance between a traceable evidence ledger and the speed needed to learn?
- How should AI assist analysis without becoming an unreviewed source of product decisions?
- What artefacts help explain scope decisions months later when research and assumptions change?

## Web research review — revised operating approach

This draft was tested against current public guidance and four parallel specialist reviews covering evidence synthesis, product strategy, UX/research, and AI evaluation. The sources consistently support the following approach:

### Recommended operating sequence

1. State one owner decision and the deadline/checkpoint that makes it relevant.
2. Describe the user’s whole journey episode, including offline steps, support, device, interruption and failure context.
3. Build the source register and claim-centred evidence ledger before proposing features.
4. Separate observations, interpretations, needs, opportunities, hypotheses and unknowns.
5. Search for supporting evidence, failures, contradictions and alternative explanations.
6. Map assumptions across desirability, feasibility, viability, accessibility, privacy, fairness, factuality and user control.
7. Select the riskiest consequential assumption, not the most exciting feature.
8. Design a disposable prototype, manual/concierge baseline or controlled experiment.
9. Evaluate the complete episode for comprehension, evidence grounding, correction, recovery, accessibility, trust calibration and harm.
10. Prepare two or three scope options with non-goals, risks, learning value and revisit triggers.
11. Keep the product owner responsible for the final scope decision.
12. Convert the chosen slice into implementation work only after the test and decision record are accepted.

### Evidence sufficiency gate

Stop expanding desk research and run an experiment when:

- the decision-critical branches have evidence or explicit gaps;
- each important claim has support plus contradiction/failure review;
- duplicate and syndicated evidence has been linked to a common provenance root;
- remaining uncertainty is behavioural, causal, usability or product-performance uncertainty;
- a smallest coherent learning slice and comparator exist;
- success, harm, stop and revise conditions are written;
- the human owner can state what would change the decision.

Continue research when a major population, geography, context, source family or disconfirmation branch remains uncovered. This is a practical operating rule, not a universal saturation law.

### AI-era operating contract

AI agents are evidence workers and reviewers, not product authorities. Use them for bounded extraction, clustering, source comparison, contradiction flags, draft opportunity statements and test preparation. Retain prompts, model/tool versions, source IDs, raw outputs, human changes and evaluation results. Require human adjudication before a claim becomes a finding, before a finding becomes an opportunity, and before an opportunity becomes scope.

Use exploratory traces while the workflow is unstable. Once expected behaviour is understood, turn representative successes and failures into a versioned evaluation set with held-out cases. Re-run it when prompts, models, retrieval, tools, source data or rubrics change.

### What this means for JobHub now

The current evidence does not justify choosing a final feature list, first segment, platform or architecture. The next analysis activity should produce a small set of traceable opportunity statements and competing hypotheses from the existing research, then select one high-consequence user episode for a low-fidelity test. The decision should be about what to learn next, not what to build forever.
