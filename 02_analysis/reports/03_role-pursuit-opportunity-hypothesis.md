# Role-pursuit opportunity and hypothesis card

Status: working hypothesis — accepted as the first analysis subject

Date: 2026-10-19

## Selected user episode

A job seeker is considering a job posting and needs to decide whether it is worth pursuing before investing time in tailoring a resume, preparing an application or attending an interview.

## Decision this work should inform

Can a small, reviewable workflow help a job seeker make a clearer continue, pause, investigate or decline decision about a role without creating false confidence?

## Why this episode was selected

This episode connects several evidence-backed concerns without requiring us to commit to a final feature:

- job postings vary in structure, completeness, provenance and accessibility;
- role fit depends on skills, credentials, work conditions, preferences and constraints;
- missing or conflicting information should remain visible;
- people may need to identify red flags and investigate employer claims;
- AI assistance is only defensible when evidence, uncertainty and user control remain visible;
- a decision-support workflow can be tested before resume generation, application tracking or submission automation.

This is a synthesis of the research, not proof that this is the greatest job-search burden.

## User goal

> “Help me decide whether this role deserves more of my limited time and effort, and show me what I still need to verify.”

## Desired outcome

The person can:

- understand the role’s stated responsibilities and requirements;
- distinguish required, preferred, inferred, missing and conflicting information;
- compare the role against their skills, constraints and preferences;
- identify important questions, risks or red flags;
- choose a next action: continue, investigate, save for later, pause or decline;
- explain why they made that decision.

## Current evidence

- [Round 4 integrated findings](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-round4-remaining-objectives/findings.md)
- [Industry profiles and role-fit evidence](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-round4-remaining-objectives/industry-profiles.md)
- [AI-assisted job-seeking and trust](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-round4-remaining-objectives/ai-assisted-job-seeking-and-trust.md)
- [Round 4 job-posting page inventory](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/README.md)

These sources support the problem space and risks. They do not establish prevalence, the best interface, or a successful intervention.

## Competing hypotheses

### Hypothesis A — Information clarity is the main opportunity

Job seekers struggle because important job-posting information is fragmented, inconsistently labelled, missing or difficult to compare.

**Prediction:** A structured, source-linked representation of the posting helps people identify what is known, unknown and worth checking before they decide.

**Disconfirming signal:** People can already make the decision reliably, or the main barrier remains unrelated to posting comprehension.

### Hypothesis B — Personal fit and work conditions are the main opportunity

Job seekers struggle because a posting may look suitable by keywords while conflicting with their schedule, location, pay needs, physical conditions, credentials or life constraints.

**Prediction:** A context-aware comparison of role conditions and personal preferences changes decisions more often than a generic skills match.

**Disconfirming signal:** Users primarily need more employer information or confidence rather than personal-fit comparison.

### Hypothesis C — Trust and verification are the main opportunity

Job seekers struggle because they cannot tell which job-posting claims are credible, current, complete or safe to act on.

**Prediction:** Showing provenance, freshness, contradictions, employer context and verification questions improves decision confidence without requiring a single fit score.

**Disconfirming signal:** Source and employer uncertainty rarely affects the decision, or the additional information creates more confusion than value.

### Hypothesis D — Time and interruption are the main opportunity

Job seekers struggle because deciding whether to pursue a role requires returning to multiple sources and losing context across devices or sessions.

**Prediction:** A resumable decision record reduces repeated work and helps the person continue later.

**Disconfirming signal:** The workflow is rarely interrupted, or the main cost is not retrieval but uncertainty about the role itself.

## Candidate opportunity statement

> Job seekers need a trustworthy way to examine a role’s requirements, conditions, evidence quality and unknowns together, so they can decide what to do next without treating an automated match or summary as a hiring prediction.

## Candidate capability directions

These are intentionally solution-neutral enough to compare:

1. A structured role-understanding worksheet.
2. A source-linked requirement and condition comparison.
3. A question-and-verification checklist.
4. A personal constraints and preferences comparison.
5. A resumable decision record.
6. A reviewable AI-assisted summary with visible evidence and uncertainty.

None is accepted into scope yet.

## Smallest coherent learning slice

### Scenario

Use one realistic but fully redacted or synthetic job posting from a non-IT context and one from an office/technology context. Include:

- clear requirements;
- missing salary or schedule information;
- at least one preferred qualification;
- at least one ambiguous or potentially conflicting statement;
- a source date and employer identity;
- enough candidate context to reason about fit without using personal data.

### Test flow

1. Present the raw posting and ask for an initial continue/pause/decline decision.
2. Present a structured, source-linked analysis with explicit unknowns.
3. Ask the reviewer to identify what is known, inferred, missing and worth verifying.
4. Ask for a revised decision and written rationale.
5. Introduce an interruption or missing-information state.
6. Ask the reviewer to resume and identify the next safe action.

### Comparators

- raw posting only;
- manually structured worksheet;
- AI-assisted structured draft with human verification.

The comparison is about reasoning quality and control, not about proving that AI is better.

## Evaluation rubric

| Dimension | Question |
|---|---|
| Comprehension | Can the reviewer explain the role and the decision in their own words? |
| Evidence fidelity | Does every material statement trace to the posting or approved context? |
| Unknown handling | Are missing, conflicting and inferred fields kept distinct? |
| Fit reasoning | Are skills, credentials, work conditions and preferences kept separate? |
| Red-flag discipline | Are concerns framed as signals/questions rather than unsupported accusations? |
| Decision usefulness | Does the output support a clear next action? |
| Trust calibration | Does the reviewer understand what the analysis cannot establish? |
| Correction | Can the reviewer edit, reject or annotate the analysis? |
| Recovery | Can the reviewer resume after interruption or missing data? |
| Accessibility | Can the material be inspected with readable structure, keyboard access and non-colour cues? |
| AI comparison | Does AI reduce effort without increasing unsupported claims or false certainty? |

## Safety and responsible-AI constraints

- No hiring-probability score.
- No claim that an employer or posting is fraudulent based on one signal.
- No silent inference of salary, eligibility, shift, licence, location or work conditions.
- No personal resumes, identifiable candidate data or private employer information in the first test.
- No autonomous browsing, application submission or external messaging.
- Preserve the original posting and analysis version.
- Mark every AI suggestion as draft until human-reviewed.
- Fail closed when source evidence is missing or contradictory.

## What this test can and cannot tell us

### It can tell us

- whether the proposed information structure is understandable;
- whether the evidence/unknown distinction is visible;
- whether the workflow exposes useful questions;
- whether different contexts require different fields;
- whether AI introduces unsupported claims or extra review burden;
- which parts are suitable for a future prototype.

### It cannot tell us

- whether this is the most important job-search problem;
- whether real job seekers would adopt it;
- whether it improves application or employment outcomes;
- whether a specific platform or technology is correct;
- whether a single role-fit method works across industries.

## Stop, revise and continue conditions

### Stop or change direction if

- reviewers cannot distinguish source fact from inference;
- the structure creates false confidence or encourages a single score;
- the workflow adds more work than the decision value it provides;
- different industries require incompatible assumptions;
- red-flag guidance becomes accusatory or unsupported;
- the AI version cannot maintain evidence fidelity.

### Continue to prototype if

- reviewers can explain the role and uncertainty more clearly;
- the analysis changes decisions for understandable reasons;
- a manual baseline is useful but burdensome;
- the workflow remains correctable and accessible;
- the next uncertainty is interaction or workflow performance.

### Continue desk research if

- a critical target context is missing;
- a key requirement is legally or materially uncertain;
- the source inventory is too narrow to support the test;
- a major contradictory evidence branch has not been investigated.

## Owner decision after the test

The owner should decide whether to:

- stop this opportunity;
- continue research;
- run a manual/concierge workflow;
- build a low-fidelity prototype;
- define a narrow implementation slice.

The result must be recorded in a scope decision record with accepted scope, non-goals, evidence, risks and revisit triggers.
