# JobHub Analysis Experiment-to-Feature Roadmap

Status: working roadmap for owner review

Date: 2026-10-21

## Purpose

This roadmap defines how JobHub will move from research evidence to a deliberately small, testable product scope.

The process is:

```text
research evidence
  -> bounded experiment
  -> observed behaviour
  -> user problem or risk
  -> smallest capability hypothesis
  -> low-fidelity test
  -> feature candidate
  -> scope decision
```

The roadmap does not assume a final platform, technology stack, AI provider or architecture.

## Current position

The current evidence supports one provisional product direction:

> A human-reviewed, source-grounded worksheet that helps a job seeker understand one posting, preserve unknowns and contradictions, and choose whether to spend more effort on it.

The first live model run showed why this must remain a review aid rather than an autonomous decision-maker. The model organised many visible facts and preserved a posting contradiction, but it missed decision-critical unknowns about duties, employer context and rate determination. The human reviewer made a more complete decision to decline.

Therefore, the next experiments must measure completeness, correction burden and decision usefulness before broader automation is considered.

## Evidence levels

Use these levels when interpreting results:

| Level | Evidence | What it can justify |
|---|---|---|
| E0 | Prompt or synthetic fixture test | A bounded model behaviour hypothesis |
| E1 | Repeated redacted/captured fixtures | A stronger workflow or guardrail hypothesis |
| E2 | Concierge or low-fidelity human test | Evidence about comprehension, effort and decision usefulness |
| E3 | Small real-world pilot with explicit consent | Evidence about repeated use and operational friction |
| E4 | Production monitoring | Evidence about reliability and real outcomes |

No feature should be treated as validated merely because an E0 model response is plausible.

## Experiment families and roadmap

### Phase 0 — Establish the evidence baseline

#### Experiment 0.1: Manual review baseline

**Question:** Can a person identify the information needed to decide whether a posting deserves more time?

**Inputs:** R4-JB-003, R4-JB-006 and R4-JB-011, reviewed one at a time.

**Record:** First impression, structured worksheet, unknowns, contradictions, decision-changing questions, initial decision, time and review burden.

**Success condition:** The reviewer can explain the decision using stated facts, unknowns or conflicts without inventing missing information.

**Feature translation:** Establishes the minimum fields the product must preserve. It is not itself evidence that AI is needed.

**Assigned roles:** Product Strategist, Evidence Synthesizer.

### Phase 1 — Source-grounded evidence organisation

#### Experiment 1.1: Claim extraction and provenance

**Question:** Can AI organise one posting into claims that remain traceable to the source?

**Test:** Compare manual worksheet, guarded AI output and reviewed output.

**Measure:** Claim coverage, source-locator accuracy, qualifier preservation, correction rate, omission rate and unsupported-claim rate.

**Pass:** Every consequential claim has a source locator or explicit unknown state; original wording remains available.

**Fail:** Unsupported claims, lost qualifiers or source-free conclusions are accepted.

**Feature candidate:** Source-grounded claim cards or worksheet sections with source excerpts, ownership and review status.

**Guardrail:** AI output remains draft until human review.

#### Experiment 1.2: Completeness gate

**Question:** Does the review cover the fields that can change a job seeker’s decision?

**Required review areas:**

- role identity and employer context;
- duties and responsibilities;
- qualifications and hard requirements;
- employment type and work conditions;
- pay, rate rules and qualifiers;
- application process and commitments;
- contradictions and platform signals;
- unknowns and verification questions.

**Pass:** Missing decision-critical fields are explicitly surfaced as unknown or not visible.

**Feature candidate:** A completeness panel that shows reviewed, missing, conflicting and not-visible sections.

**Do not build yet:** A percentage completeness score presented as an overall quality or fit score.

**Assigned roles:** Evidence Synthesizer, Quality and Evaluation Engineer.

### Phase 2 — Contradiction, freshness and source ownership

#### Experiment 2.1: Contradiction preservation

**Question:** Does the workflow preserve conflicting title, URL, salary, date and employer values instead of silently selecting one?

**Fixtures:** URL/title/body mismatch, card/detail mismatch, stale/current versions and platform/employer disagreements.

**Pass:** Both values, their source owners, timestamps and locators remain visible.

**Feature candidate:** Conflict panel with side-by-side values and a “needs verification” state.

**Guardrail:** The product must not label a conflict as a scam or legitimacy verdict.

#### Experiment 2.2: Source freshness and resume recovery

**Question:** Can a person tell what was captured when and recover safely after the source changes or becomes unavailable?

**Pass:** Original snapshot, capture time, source version, corrections and unresolved items remain recoverable.

**Feature candidate:** Immutable posting snapshot plus stale-source notice and restore-original action.

**Assigned roles:** Evidence Synthesizer, Quality and Evaluation Engineer, Responsible AI Reviewer.

### Phase 3 — Human review and decision usefulness

#### Experiment 3.1: Manual-versus-AI review burden

**Question:** Does AI reduce organisation effort without creating more checking work than it saves?

**Conditions:** Raw posting, manual worksheet and guarded AI worksheet.

**Measure:** Time to first decision, time to completed review, number of corrections, rejected claims, unresolved questions and perceived confidence in the record.

**Pass:** The AI condition reduces effort while preserving or improving understanding of uncertainty.

**Fail:** Reviewers accept unsupported claims, cannot distinguish AI suggestions from source facts, or spend more effort repairing output than organising manually.

**Feature candidate:** Review queue with accept, edit, reject, annotate, undo and source-open actions.

#### Experiment 3.2: Decision-changing question usefulness

**Question:** Do generated questions help a person decide what to verify next?

**Pass:** Questions are grounded in actual gaps and reviewers can identify which questions could change their action.

**Feature candidate:** A short, prioritised verification-question list linked to the unresolved claim.

**Non-goal:** Automated employer contact or question answering.

#### Experiment 3.3: Interruption and recovery

**Question:** Can a reviewer stop and resume without losing source context, corrections or decision rationale?

**Pass:** The restored state shows the source snapshot, reviewed claims, rejected suggestions, unresolved questions and current decision.

**Feature candidate:** Saved review state with explicit draft and reviewed statuses.

**Assigned roles:** UX Expert, UX and User-Flow Designer, Quality and Evaluation Engineer.

### Phase 4 — Safety, privacy and responsible boundaries

#### Experiment 4.1: Untrusted posting content

**Question:** Does the workflow treat instruction-like text in a job posting as evidence rather than instructions to the system?

**Pass:** The system extracts or flags the text without revealing data, changing policy or taking action.

**Feature translation:** System-level boundary and audit event, not a user-facing autonomous feature.

#### Experiment 4.2: Sensitive-information handling

**Question:** Can the workflow avoid soliciting or auto-answering sensitive questions about work rights, health, demographics, criminal history or other protected information?

**Pass:** The workflow pauses, explains the boundary and keeps the decision with the user.

**Feature translation:** Clear consent, privacy controls, redaction and review warnings.

#### Experiment 4.3: Overclaim and verdict resistance

**Question:** Does the system avoid turning signals into fit, scam, employer-quality, salary-guarantee or hiring-probability verdicts?

**Pass:** The output uses bounded states such as present, conditional, conflicting, unknown, not visible and platform signal.

**Feature translation:** State vocabulary, source ownership and claim review controls.

**Assigned roles:** Responsible AI Reviewer, Quality and Evaluation Engineer, AI Tools Expert.

### Phase 5 — Industry portability

#### Experiment 5.1: Shared evidence core across sectors

**Question:** Which review fields remain useful across IT, administration, logistics, healthcare, retail, hospitality, finance, construction, education and other sectors?

**Method:** Run the single-posting review across deliberately different industry fixtures.

**Measure:** Shared-field coverage, sector-specific omissions, terminology errors and correction burden.

**Pass:** A stable evidence core works without forcing misleading universal fields.

**Feature candidate:** Core review schema plus optional sector-specific sections.

**Do not assume:** One universal occupation schema or one universal fit model.

#### Experiment 5.2: Industry-specific risk and condition fields

**Question:** Which sector-specific conditions materially affect a person’s decision?

**Examples:** Licences and shifts in logistics; rostering and physical demands in hospitality; regulated qualifications in healthcare; portfolio or tool expectations in creative work; site/travel and safety conditions in construction.

**Feature candidate:** Contextual prompts that appear only when the source contains relevant evidence.

**Assigned roles:** Job Domain Researcher, Evidence Synthesizer, Product Strategist.

### Phase 6 — Explicit personal constraints, without fit scoring

#### Experiment 6.1: Constraint review

**Question:** Can a person record explicit preferences and compare them with stated role facts without the system inventing fit?

**Inputs:** User-provided schedule, location, pay floor, employment type, licences or other constraints; explicit role evidence only.

**Pass:** The system reports stated match, possible conflict or unknown, with source links.

**Fail:** It produces a holistic fit score, ranking or eligibility conclusion.

**Feature candidate:** User-owned constraint checklist with `matches stated`, `may conflict`, `not stated` and `not reviewed` states.

**Decision gate:** Do not proceed until profile comparison errors are materially reduced and the human meaning of each constraint is clear.

**Assigned roles:** Product Strategist, Responsible AI Reviewer, Quality and Evaluation Engineer.

### Phase 7 — Truthful application preparation

#### Experiment 7.1: Evidence-backed resume alignment

**Question:** Can the system suggest truthful alignment without inventing skills, metrics, qualifications, intent or experience?

**Inputs:** Canonical user profile, explicit role claims and source locators.

**Pass:** Suggestions are traceable to verified user evidence and clearly labelled as edits or optional phrasing.

**Fail:** Plausible but unsupported claims, credential inflation or automatic rewriting are accepted.

**Feature candidate:** Evidence-linked suggestion review, not automatic resume replacement.

**Decision gate:** This remains deferred until the single-posting review and constraint workflow are reliable.

#### Experiment 7.2: Interview-preparation grounding

**Question:** Can interview preparation use only verified role facts and the user’s real experience?

**Feature candidate:** Practice questions linked to role evidence and user-provided experience, with unknowns clearly separated.

**Non-goal:** Predicted interview questions presented as certain, fabricated experience, or automatic answers to sensitive questions.

**Assigned roles:** Product Strategist, Responsible AI Reviewer, Quality and Evaluation Engineer.

### Phase 8 — Model, provider and operational comparison

#### Experiment 8.1: Model comparison

**Question:** Which available model offers the best bounded behaviour for evidence organisation?

**Measure:** Grounding, omission, unsupported inference, contradiction preservation, JSON validity, latency, token usage, correction burden and cost proxy.

**Pass:** A model is selected for a narrow experimental role, not declared universally reliable.

**Feature translation:** Provider/model abstraction, retry and failure handling, not model-specific product assumptions.

#### Experiment 8.2: Failure and recovery behaviour

**Question:** What happens when output is truncated, malformed, slow, unavailable or contradictory?

**Pass:** The workflow fails closed, preserves the source, reports the failure and allows manual continuation.

**Feature candidate:** Invalid-output state, retry boundary, raw-output preservation and manual fallback.

**Assigned roles:** AI Tools Expert, Technical Architect, Quality and Evaluation Engineer.

## Translating an experiment into a feature

Every candidate feature must complete this record:

```text
Experiment ID:
Observed evidence:
Evidence level: E0 / E1 / E2 / E3 / E4
User problem demonstrated:
Risk if ignored:
Smallest capability that could help:
What the user controls:
What the system must never infer or do:
Acceptance criteria:
Failure and stop conditions:
Open questions:
Decision: build / prototype / investigate / defer / reject
Owner:
```

### Translation rules

1. Convert repeated observed pain into a problem statement, not immediately into an AI feature.
2. Prefer the smallest capability that addresses the pain.
3. Separate source facts, platform signals, AI suggestions, user-provided facts and decisions.
4. Turn omissions and unsafe inferences into guardrails or evaluation tests, not hidden assumptions.
5. Do not translate one plausible model response into a product requirement.
6. Require a manual baseline for any claim that AI saves time or improves decisions.
7. Preserve uncertainty as a product state rather than forcing a binary answer.
8. Keep user decisions and external actions under explicit human control.
9. Defer broad automation until the narrower workflow passes its gates.
10. Record rejected ideas and non-goals so they are not accidentally reintroduced.

## Feature decision categories

| Category | Meaning | Example |
|---|---|---|
| Build candidate | Evidence supports a narrow capability and safety boundary | Source-linked claim review |
| Prototype | Promising but needs human-flow testing | Completeness panel |
| Guardrail | A constraint needed to prevent harm or overclaim | Preserve conflicting values |
| Evaluation requirement | A behaviour that must be repeatedly tested | No unsupported salary guarantee |
| Investigate | Evidence is incomplete or mixed | Industry-specific extensions |
| Defer | Valuable but dependent on earlier reliability | Resume tailoring |
| Reject for now | Evidence or risk argues against inclusion | Fit score or scam verdict |

## Recommended execution order

### Now

1. Finish the R4-JB-011 human-reviewed comparison.
2. Add and test the completeness gate.
3. Repeat the same guarded review with R4-JB-003 and R4-JB-006.
4. Record correction burden, omissions and unsupported questions.

### Next

5. Build a low-fidelity worksheet or concierge flow around the proven evidence core.
6. Test interruption, recovery, accessibility and comprehension.
7. Test contradiction and stale-source handling explicitly.
8. Decide whether the worksheet provides enough value to justify a first prototype.

### Later

9. Expand across industries and identify optional sector fields.
10. Test explicit user constraints without fit scoring.
11. Compare models and provider failure behaviour.
12. Revisit resume alignment and interview preparation only after the core review workflow passes.

## What not to do yet

- Do not build a complete job-search platform.
- Do not lock mobile, web or another platform from these experiments.
- Do not select an AI provider as a product decision from one model run.
- Do not add fit scores, candidate ranking, hiring prediction or scam verdicts.
- Do not automate applications, employer messaging or sensitive-question responses.
- Do not start resume rewriting before source-grounded review is reliable.
- Do not treat industry coverage as evidence that one universal schema works.

## Analysis exit criteria

The 02_analysis/reports phase is ready to produce a first scoped product brief only when:

- the smallest user episode is clearly stated;
- the manual baseline and AI-assisted workflow have been compared across multiple roles;
- omissions, corrections and unsafe inferences are measured;
- the core evidence schema and its limits are documented;
- at least one low-fidelity human-flow test is complete;
- accessibility, interruption and recovery risks have been examined;
- responsible-AI boundaries and non-goals are explicit;
- build candidates are separated from hypotheses and deferred ideas;
- the owner approves the resulting scope and non-goals.

## Owner decision

The next owner decision is whether to continue testing the source-grounded single-posting review as JobHub’s first product slice. This roadmap does not make that decision on the owner’s behalf.
