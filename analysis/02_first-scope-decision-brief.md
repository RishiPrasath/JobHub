# First-scope decision brief

Status: draft for owner review

Date: 2026-10-19

## Decision to support

Which job-seeker episode is important enough and uncertain enough for JobHub to test first before committing to a feature, platform or architecture?

## Decision owner

JobHub product owner.

## What this decision is not

This is not yet a decision about:

- the final product scope;
- mobile, web or another platform;
- technology stack or architecture;
- an AI provider;
- autonomous application submission;
- the complete JobHub feature list.

## Current evidence base

Relevant research includes:

- [Round 1–4 research](../02_research/README.md)
- [Round 4 integrated findings](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-round4-remaining-objectives/findings.md)
- [Round 4 job-posting inventory](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/README.md)
- [Research-to-scope method](00_research-to-scope-draft.md)

The existing evidence is public-web, internal and desk research. It does not yet establish a greatest-burden ranking, representative user behaviour, willingness to use, or the best first workflow.

## Candidate user episodes

These are candidate episodes, not accepted priorities.

### Episode A — Capture and resume later

**Context:** A person discovers a potentially suitable job on a phone or another constrained device but cannot complete the research and preparation immediately.

**Possible desired outcome:** Preserve enough trustworthy context to resume later without losing the posting, source, requirements or next action.

**Open uncertainty:** Is interruption and context loss a sufficiently important problem, and what minimum information must be preserved?

**Possible test:** Compare a lightweight manual capture-and-resume flow with an unstructured bookmark/note workflow.

### Episode B — Decide whether a role is worth pursuing

**Context:** A person is considering a job posting and needs to understand requirements, work conditions, fit, unknowns, red flags and trade-offs.

**Possible desired outcome:** Make a better-informed continue, pause or decline decision.

**Open uncertainty:** Which information actually changes the decision, and can it be presented without false confidence or a misleading fit score?

**Possible test:** Give people realistic postings with incomplete or conflicting information and observe what they check, misunderstand or ignore.

### Episode C — Tailor evidence truthfully

**Context:** A person wants to align their resume or application to a role without inventing experience, metrics, credentials or ownership.

**Possible desired outcome:** Produce a clearer, role-relevant application that the person can explain and defend.

**Open uncertainty:** What assistance saves effort while preserving factuality, personal voice and user ownership?

**Possible test:** Compare manual editing, AI-suggested edits and unreviewed AI drafting using redacted or synthetic cases.

### Episode D — Prepare for an interview

**Context:** A person needs to turn their real experience into relevant interview stories and practise likely questions.

**Possible desired outcome:** Enter the interview better prepared without memorising invented answers or relying on hidden live assistance.

**Open uncertainty:** Which feedback is useful, understandable and trusted enough to change preparation behaviour?

**Possible test:** Compare a source-grounded practice flow with an unconstrained question-and-answer assistant.

### Episode E — Track an application journey

**Context:** A person applies across multiple sources and needs to remember roles, versions, dates, answers, status and follow-ups.

**Possible desired outcome:** Maintain an accurate, low-effort record without creating more administration than value.

**Open uncertainty:** Which tracking fields are essential, and when does tracking become burdensome or abandoned?

**Possible test:** Compare a minimal tracker with a spreadsheet/manual baseline over a small synthetic application set.

## Comparison questions

For each episode, assess:

- Is the user outcome important?
- Is the problem supported by more than one independent evidence family?
- Is the current workaround visible?
- Is the uncertainty behavioural or product-performance based?
- Can it be tested without participant recruitment or personal data?
- Can a manual baseline be created?
- Can the test include incomplete, conflicting and failure cases?
- Can usefulness and harm be measured separately?
- Is the result reversible if the hypothesis is wrong?
- Does the episode avoid prematurely selecting the platform or stack?

## Current evidence and unknowns

| Area | What the research suggests | Still unknown |
|---|---|---|
| Job-posting understanding | Job postings vary in structure, completeness and provenance. | Which missing or conflicting fields most affect decisions? |
| Mobile/interrupted work | Context switching and delayed access may create friction. | How severe is this compared with other job-search burdens? |
| Truthful tailoring | Evidence supports reviewable, source-grounded editing over free-form generation. | Which review interaction is understandable and useful? |
| Role fit | Fit depends on skills, credentials, conditions, preferences and constraints. | Which factors should be surfaced first for different contexts? |
| Interview preparation | Practice grounded in real evidence appears safer than hidden live assistance. | What feedback changes preparation quality without creating overconfidence? |
| Tracking | People use trackers and also abandon them when manual work is high. | What is the minimum valuable record? |

## Proposed decision criteria

Do not calculate a single “winner” score. Use a written rationale across:

1. user importance;
2. evidence strength;
3. consequence if wrong;
4. learning value;
5. testability;
6. privacy and responsible-AI risk;
7. accessibility and interruption relevance;
8. reversibility;
9. ability to create a complete but small user episode.

## Options after review

### Option 1 — Continue desk research

Choose this only if a decision-critical population, context or contradiction is still missing.

### Option 2 — Run a manual or concierge experiment

Use a human-supported workflow to learn what information, transformations or checks are valuable before building automation.

### Option 3 — Build a low-fidelity prototype

Use a disposable prototype to test comprehension, flow, correction, interruption and trust.

### Option 4 — Commit to an implementation slice

Choose this only after the highest-risk assumptions have been tested sufficiently and the owner accepts the scope, non-goals, risks and revisit trigger.

## Provisional recommendation

Begin with one low-fidelity test, not implementation. The test should compare at least two plausible approaches and include:

- realistic job-posting inputs;
- incomplete or conflicting information;
- an explicit unknown state;
- a user decision or action;
- review and correction;
- interruption and return;
- an accessibility and comprehension check;
- a manual baseline;
- success, harm and stop conditions.

## Owner decision required

Select one candidate episode, or state that another episode should be added.

The selected episode becomes the subject of the next artefact: an opportunity-and-hypothesis card.

## Decision record

Decision: provisional recommendation — prepare a disposable low-fidelity test instrument after adding the audit and interaction gates; owner acceptance still required.

Accepted episode: provisionally, “decide whether a role is worth pursuing and what must be verified first.”

Rejected or deferred episodes: resume generation, fit scoring, hiring-probability prediction, legitimacy/scam verdicts and automatic application submission are deferred.

Reasoning: The bounded manual-versus-AI simulation preserved source facts, unknowns and contradictions, and showed plausible value in organising role conditions and verification questions. Independent review also found that raw AI output, claim-level locators, correction logs and reproducible contradiction fixtures are still missing. Real users, a rendered interface, accessibility, interruption recovery and actual time savings remain untested. See [learning-test results](07_role-pursuit-learning-test-results.md).

Revisit trigger: Stop or revise if the prototype adds more review burden than decision value, encourages unsupported certainty, cannot be corrected, fails accessibility checks, or requires materially different workflows across industries.
