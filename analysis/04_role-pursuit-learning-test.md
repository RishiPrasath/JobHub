# Role-pursuit learning test

Status: draft test plan — not yet executed

## Purpose

Determine whether a structured, source-linked role review helps a person understand a job posting and decide what to do next without introducing unsupported claims or false certainty.

## Learning questions

1. Which information changes the continue, investigate, pause or decline decision?
2. Do users understand the distinction between stated, preferred, inferred, missing and conflicting information?
3. Does a structured review reduce repeated reading and comparison effort?
4. Does AI assistance preserve evidence fidelity and personal control?
5. Which fields differ materially across industries and employment arrangements?
6. Can the workflow recover from interruption, stale information or missing data?

## Test boundaries

- Use synthetic or fully redacted job postings.
- Do not upload personal resumes, identity data, private employer information or application credentials.
- Do not submit applications or message employers.
- Do not claim participant usability evidence from the coordinator’s own walkthrough.
- Treat all AI output as draft material requiring review.
- Keep the manual worksheet as the baseline.

## Test set

Prepare six synthetic postings:

| Case | Context | Deliberate condition |
|---|---|---|
| T01 | Software/office role | Relatively complete posting |
| T02 | Customer/service role | Missing schedule and salary details |
| T03 | Utilities or maintenance | Licence and shift requirements |
| T04 | Maritime or offshore | Credential, medical and deployment constraints |
| T05 | Domestic/household service | Mixed duties and ambiguous care expectations |
| T06 | Agri-food or production | Physical conditions and transferable-skill ambiguity |

At least two cases should include:

- a preferred qualification that is not a hard gate;
- a missing field that must remain unknown;
- an ambiguous or contradictory statement;
- a potentially concerning signal that does not justify a fraud accusation;
- a stale or uncertain source date.

## Three conditions

### Condition A — Raw posting

The reviewer receives only the source posting and records:

- initial decision;
- reasons;
- questions;
- time spent;
- confidence and uncertainty.

### Condition B — Manual structured review

The reviewer uses a worksheet with fields for:

- role and employer identity;
- responsibilities;
- required qualifications;
- preferred qualifications;
- work conditions;
- compensation and benefits;
- application route;
- source date and provenance;
- missing or conflicting information;
- personal fit constraints;
- red flags and verification questions;
- next action.

### Condition C — AI-assisted structured review

The AI produces a draft from the same posting. The reviewer sees:

- source-linked statements;
- explicit unknowns;
- confidence/limitations;
- suggested verification questions;
- editable fields;
- a before/after or accept/reject view;
- a warning that this is not a hiring prediction.

The AI must not browse beyond the approved test materials, invent employer facts, infer missing requirements or produce a single suitability score.

## Procedure

1. Record the case ID, condition and starting assumptions.
2. Review the case and make an initial decision.
3. Complete the assigned review condition.
4. Record what changed in the decision and why.
5. Introduce an interruption: stop midway, remove one data field or mark a source stale.
6. Resume the task and record recovery effort and uncertainty.
7. Inspect the final output against the source.
8. Log unsupported claims, omissions, false certainty, confusing labels and unnecessary effort.
9. Compare conditions without treating the coordinator’s judgment as user research.

## Evaluation measures

### Evidence fidelity

- percentage of material claims traceable to the source;
- unsupported claim count;
- omitted required/preferred distinction;
- incorrect inference count;
- source-locator accuracy.

### Decision quality

- whether the final decision has a stated rationale;
- whether important unknowns are identified;
- whether next actions are specific and safe;
- whether red flags are framed as signals/questions rather than accusations.

### Human control

- can the reviewer edit, reject, annotate and restore content;
- are AI suggestions clearly marked as draft;
- is the original posting preserved;
- are external actions impossible without explicit approval?

### Recovery and accessibility

- can the reviewer resume after interruption;
- is saved/pending/incomplete state understandable;
- are headings, labels, reading order and non-colour cues clear;
- can the review be completed with keyboard and enlarged text;
- does the structure remain understandable without visual grouping?

### Effort and uncertainty

- time to first decision;
- time to final decision;
- number of repeated checks;
- number of corrections;
- unresolved uncertainty count;
- review burden introduced by AI.

## Pass conditions for moving to a prototype

These are provisional learning thresholds, not product requirements:

- no fabricated employer, credential, salary, schedule or eligibility facts;
- every material AI claim either cites source evidence or remains explicitly unknown;
- required, preferred, inferred and missing information remain distinct;
- the reviewer can explain why the decision changed;
- the reviewer can correct or reject every AI suggestion;
- no red-flag conclusion is stronger than its evidence;
- interruption does not erase the review state;
- the workflow identifies at least one meaningful limitation;
- no critical accessibility or control failure remains unexplained.

## Failure interpretation

- If raw and structured review produce the same decision with no meaningful improvement, the opportunity may not justify a product workflow.
- If structured review helps but AI adds unsupported claims or review burden, retain the manual structure and redesign the AI boundary.
- If different industries need materially different fields, avoid a universal role-review template.
- If the workflow is understandable but slow, test a narrower episode before adding automation.
- If the coordinator cannot evaluate the result reliably, improve the evidence model before building an interface.

## Output artefacts after execution

- case set and provenance record;
- completed manual worksheets;
- AI raw outputs and reviewed outputs;
- claim-level error log;
- contradiction and unknown log;
- accessibility/control checklist;
- comparison summary;
- prototype/no-prototype recommendation;
- updated scope decision record.

## Approval boundary

This plan is ready for review. Execution should occur only after the owner accepts the test cases, conditions, evaluation rubric and data boundaries.
