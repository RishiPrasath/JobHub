# First Scope Decision Brief

Status: ready for owner decision; recommendation is provisional

Date: 2026-10-27

## Decision to make

Should JobHub proceed with a first product slice focused on a human-reviewed, source-grounded review of one job posting?

## Evidence now available

- Research established repeated job-search uncertainty around duties, compensation, employer context, conditions and application effort.
- Controlled model experiments showed useful evidence organisation but recurring omissions and unsafe classifications.
- Completeness-gated Run 002 made missing sections visible but still required human correction.
- Three different job types were reviewed without cross-posting contamination.
- The user's Admin Assistant walkthrough resulted in a clear decline based on missing information.
- Recovery and accessibility are defined at the data level but not yet tested in a rendered interface.

## Provisional v0.1 scope candidate

### Include

1. Capture or paste one job posting.
2. Preserve source, URL/reference and capture date.
3. Organise evidence into review sections.
4. Link consequential claims to source locations.
5. Show unknown, not-visible, conditional and conflicting states.
6. Separate employer facts from platform signals.
7. Generate a small list of decision-changing verification questions.
8. Allow human accept, edit, reject, annotate, undo and restore actions.
9. Record continue, investigate, save, pause or decline with user rationale.
10. Preserve raw source, raw AI output and reviewed corrections.

### Exclude

- Fit scores or candidate rankings
- Hiring-probability predictions
- Scam, legitimacy or employer-quality verdicts
- Automatic resume or cover-letter rewriting
- Profile-to-role matching as an autonomous decision
- Employer messaging or application submission
- Automatic answers to sensitive eligibility questions
- Full job-board crawling or login integrations
- Final platform or provider commitment

## Proposed acceptance gates

Proceed to implementation planning only if a low-fidelity interface test shows that the reviewer can:

- understand the role evidence;
- identify important unknowns and contradictions;
- trace consequential claims to source;
- distinguish platform signals from employer facts;
- correct and reject AI suggestions;
- select a verification question;
- record a decision and rationale;
- resume without losing review state.

## Risks that remain

- No rendered-interface or participant test has yet been completed.
- The completeness gate can identify coverage problems but cannot prove factual accuracy.
- Source ownership can still be misclassified.
- Model output can still produce plausible but unsupported questions.
- Industry portability beyond the three fixtures remains limited evidence.

## Owner decision options

### Option A — Proceed with the narrow prototype

Approve the v0.1 scope candidate and build only the single-posting review workflow with the listed safety boundaries.

### Option B — Continue low-fidelity testing first

Do not build yet. Test the workflow with a rendered or concierge interface and use the results to revise the scope.

### Option C — Reject or reshape the slice

Choose a different first user episode if the evidence does not justify this workflow.

## Recommendation

Option B is the safest immediate decision: run one low-fidelity interface or concierge test before implementation. The evidence is strong enough to justify the narrow workflow as a prototype hypothesis, but not strong enough to justify building the broader JobHub vision.
