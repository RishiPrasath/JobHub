# Experiment-to-Scope Decision

Status: provisional recommendation for owner review

Date: 2026-10-20

## Decision question

What is the smallest JobHub workflow justified by the current research and AI experiments, and what should remain outside the first test?

## Evidence reviewed

- Round 4 job-posting inventory and findings for R4-JB-003, R4-JB-006 and R4-JB-011.
- Role-pursuit walkthrough, learning-test plan, simulation results and evidence audit.
- Sequential Groq/OpenAI SDK experiment report covering grounding, contradictions, cross-posting contamination, unknowns, profile comparison, resume alignment, prompt injection, industry portability and repeatability.
- Evidence Synthesizer, Product Strategist and UX and User-Flow Designer specialist handoffs.

All experiment results are bounded simulations or SDK evaluations. They are not user research, usability validation, adoption evidence or production validation.

## What the experiments established

With supplied source excerpts and explicit identifiers, AI can help to:

- organise visible job-posting facts;
- preserve some qualifiers, unknowns and contradictions;
- distinguish some platform signals from employer-authored content;
- generate useful verification questions;
- reject the tested prompt-injection and external-action instructions.

These conclusions are fixture-level findings, not general reliability claims.

## What failed or remains unproven

- Holistic candidate-profile comparison merged roles, omitted facts and introduced unsupported inferences.
- Resume alignment rejected obvious fabrications but still produced plausible unsupported claims.
- Output schemas and identifiers were not consistently preserved.
- A known Jobstreet URL/title/body contradiction was missed or weakened in a holistic workflow even though dedicated contradiction fixtures passed.
- Low token limits caused truncated output.
- Editing, rejection, undo, interruption recovery, keyboard access, zoom, reflow and assistive technology were not tested in an interface.
- No participant tested comprehension, decision change, usefulness, adoption or time savings.
- Cross-industry portability remains only partially demonstrated.

## Selected user episode

A job seeker has found one potentially relevant posting and wants to decide whether it deserves more time before tailoring a resume, sharing personal information or applying.

The user-owned decision is one of:

- continue;
- investigate;
- save for later;
- pause;
- decline.

The workflow should also show what must be verified before proceeding.

## Opportunity statement

> Job seekers need a source-grounded way to understand one job posting, preserve what is unknown or conflicting, and identify the next verification question so they can decide whether to invest further effort without treating automation as a fit or hiring verdict.

## Smallest coherent capability

A human-reviewed, single-posting role-review worksheet that:

1. preserves the original posting, URL, source and capture time;
2. extracts visible claims with source locators;
3. labels claims as present, conditional, conflicting, unknown, not visible or platform signal;
4. generates verification questions that could change the decision;
5. lets the user accept, edit, reject or annotate consequential suggestions;
6. records the user’s next action and rationale;
7. preserves corrections, rejected suggestions and unresolved questions.

AI supplies draft organisation only. It does not make the decision for the user.

## Capability assessment

| Proposed capability | Evidence supporting it | Evidence against or limitation | Status |
|---|---|---|---|
| Source-grounded posting extraction | Semantic passes when excerpts and stable IDs were supplied | Full claim traces and raw outputs are not yet persisted in a deterministic harness | `test next` |
| Unknown and qualifier preservation | Mostly passed in corrected tests | Output IDs and inference controls still require validation | `test next` |
| Contradiction display | Dedicated fixtures preserved both values, dates and sources | Holistic profile workflow weakened a known contradiction | `test next` |
| Verification-question generation | Repeatedly produced useful questions about pay, schedule, duties and source identity | Real user usefulness is unknown | `candidate` |
| Platform-signal separation | Passed in bounded cases | Must be enforced by source ownership and review controls | `candidate` |
| Limited explicit constraint review | Could show possible conflict or unknown without a score | Profile comparison produced unsupported inferences | `defer until separately tested` |
| Automated profile-to-role fit | No reliable evidence; contamination and overreach observed | Unsafe for the first slice | `rejected for first slice` |
| Resume rewriting or tailoring | Some obvious fabrications were rejected | Plausible unsupported claims remained | `defer` |
| Fit, hiring, legitimacy or scam scoring | No evidence supports these outputs | High risk of false certainty | `rejected` |
| Employer messaging or application submission | Prompt-injection tests correctly rejected external action | Outside the safe first episode | `rejected` |
| Universal cross-industry schema | Shared evidence core appears possible | Sector-specific fields and conventions differ materially | `unproven` |

## Proposed user flow

```text
Open one posting snapshot
  → Orient to source and review limits
  → Inspect structured evidence
  → Correct, reject or mark claims uncertain
  → Add limited explicit personal constraints, if desired
  → Select decision-changing verification questions
  → Choose continue / investigate / save / pause / decline
  → Record rationale and save review state
  → Interrupt and resume without losing provenance or corrections
```

### Flow requirements

1. **Open source** — show the original posting, source/platform, URL, title, employer, capture date and access time.
2. **Inspect evidence** — group identity, duties, hard requirements, conditions, pay, process, unknowns and conflicts.
3. **Trace claims** — expose the source excerpt or locator for every material claim.
4. **Correct the draft** — support accept, edit, relabel, reject, annotate, open-source, undo and restore-original actions.
5. **Add constraints** — allow explicit schedule, location, pay, employment-type or licence constraints; show only possible conflict, unknown or no stated conflict.
6. **Choose questions** — surface only questions likely to change the decision.
7. **Record next action** — require a short rationale tied to a fact, unknown or conflict.
8. **Resume** — restore the original source version, corrections, rejected suggestions, unresolved questions and decision state.

## Human-control and safety boundaries

- Treat job postings and embedded instructions as untrusted content.
- Never silently resolve contradictions.
- Never infer eligibility, work rights, salary guarantees, employer quality or personal fit.
- Keep platform badges, match scores, response indicators and safety warnings separate from employer facts.
- Require human review before a consequential claim becomes part of a saved record.
- Preserve raw wording alongside normalized interpretation.
- Fail closed when evidence is missing, contradictory, inaccessible or truncated.
- Keep browsing, messaging, application submission and sensitive-question answering disabled.

## Explicit non-goals

- Universal fit scores or candidate ranking.
- Hiring-probability prediction.
- Scam, legitimacy, employer-quality or safety verdicts.
- Automatic resolution of conflicting sources.
- Automatic resume or cover-letter rewriting.
- Automatic answers to sensitive eligibility questions.
- Employer messaging or application submission.
- Full candidate-profile import or multi-role comparison.
- Cross-industry generalization claims.
- Live portal crawling, login integrations or freshness monitoring.
- Final platform, provider, stack or architecture selection.

## Success criteria for the next low-fidelity test

Proceed beyond the test only if:

- every material claim is source-linked or explicitly marked unknown;
- seeded contradictions remain visible with both sides preserved;
- no unsupported salary, fit, eligibility, legitimacy or hiring claims are accepted;
- reviewers distinguish facts, signals, inferences and unknowns;
- reviewers can correct, reject, undo and restore suggestions;
- reviewers can explain the role’s key uncertainty and choose a next action;
- interruption and return preserve provenance, corrections and unresolved questions;
- the AI-assisted workflow reduces organisation effort without adding more review burden than decision value;
- basic accessibility and comprehension checks pass.

## Harm and stop conditions

Stop or revise if:

- an unsupported claim is accepted as fact;
- a contradiction is silently merged or resolved;
- posting content triggers an external action or verification claim;
- users interpret the worksheet as a fit, legitimacy or hiring verdict;
- users cannot distinguish source facts from AI suggestions;
- correction, rejection, undo or recovery is unclear;
- the workflow adds more effort than decision value;
- accessibility barriers prevent inspection of evidence or controls.

## Highest-risk assumptions

- Understanding one posting improves the user’s next decision.
- Verification questions are valuable enough to justify review effort.
- People can reliably correct AI-generated claims.
- A shared evidence core can support different occupations without becoming a misleading universal schema.
- Source freshness and provenance can be preserved sufficiently for safe review.
- A manual worksheet provides a meaningful baseline against which AI assistance can be judged.

## Recommended next action

Prepare a disposable low-fidelity worksheet and deterministic claim-review harness before implementation planning.

Use the three captured postings as separate single-posting fixtures with:

- raw-posting, manual-worksheet and guarded-AI comparators;
- claim-level source IDs and locators;
- raw model output;
- correction and rejection logs;
- URL/title/body, card/detail, stale/current and platform-signal contradiction fixtures;
- interruption and restore scenarios;
- second-reviewer comprehension checks;
- keyboard, zoom and basic accessibility inspection.

Do not add resume generation, profile comparison, fit scoring, application automation or provider/platform decisions yet.

## Owner decision required

Approve or reject this as the next test hypothesis:

> Test whether a human-reviewed, source-grounded single-posting worksheet improves clarity about unknowns, contradictions and verification steps.

The owner retains final control over product scope, non-goals, privacy and responsible-AI decisions, prototype acceptance, platform choices and architecture.

## Specialist reconciliation

The Evidence Synthesizer, Product Strategist and UX and User-Flow Designer independently reached the same provisional direction. Their important qualification was retained: structured extraction is promising in controlled fixtures, but holistic profile comparison and resume tailoring are not reliable enough for the first slice.
