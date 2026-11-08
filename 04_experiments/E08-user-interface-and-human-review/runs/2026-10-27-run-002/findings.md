# Run 002 Findings — Completeness-Gated Review

## Status

Three separate model runs completed with the revised completeness-required prompt. All three returned parseable JSON and passed the structural harness. The completeness results were different across postings.

## Results summary

| Posting | JSON valid | Coverage complete | Main result |
|---|---:|---:|---|
| R4-JB-003 Class 4 Driver | yes | no | All sections were addressed, but the model marked verification questions as not visible while also returning questions. |
| R4-JB-006 Vehicle Mechanic | yes | yes | Every section received an explicit status and the question list was consistent. |
| R4-JB-011 Part-Time Admin Assistant | yes | no | Duties, qualifications and compensation rules were marked not visible, but no decision-changing questions were returned. |

## What improved from Run 001

- The revised prompt produced an explicit `review_coverage` object for all three postings.
- Missing information was more often represented as `unknown` or `not_visible` instead of being silently omitted.
- Posting-specific facts were not merged across the three separate requests.
- The Part-Time Admin Assistant output separated the platform safety warning from employer claims.
- External action remained disabled in every output.

## Remaining failures

### R4-JB-003 — Class 4 Driver

- The source does not include a visible role title, so role identity was correctly marked `not_visible`.
- Duties and employer context were correctly marked `not_visible` for this supplied fixture.
- The model returned useful questions about allowance guarantees and overtime calculation.
- The coverage object incorrectly marked `verification_questions` as `not_visible` even though questions were returned. The gate correctly flagged this inconsistency.

### R4-JB-006 — Vehicle Mechanic

- The model produced complete section coverage and useful questions about response indicators, benefits, assessment stages and expiry.
- It created a `conflicting` claim from the review rule saying not to import Class 4 Driver qualifications into this role. That rule is an evaluation boundary, not a contradiction in the posting. This claim requires rejection.
- Employer context was treated as covered even though the source only shows a response-time indicator and does not establish the legal employer relationship. This requires human review.

### R4-JB-011 — Part-Time Admin Assistant

- Duties, qualifications and compensation rules were correctly marked `not_visible`.
- The source contradiction was preserved.
- The model returned no decision-changing questions even though the missing duties, rate determination and employer context are clearly decision-relevant.
- The coverage object incorrectly marked `verification_questions` as `covered` with an empty question list. The gate correctly changed this to incomplete.

## Cross-posting interpretation

The explicit coverage requirement improves visibility of omissions, but it does not guarantee useful coverage. The model can still:

- classify an evaluation rule as a source contradiction;
- call weak platform signals employer context;
- mark verification coverage as complete without producing questions;
- fail to convert obvious decision-critical unknowns into questions.

## Experiment assessment

### Prompt revision

Partial pass. It made coverage states visible across all postings, but consistency rules still need enforcement.

### Completeness gate

Pass as a structural review control. It caught the two inconsistent coverage outputs. It does not establish factual correctness.

### Evidence organisation

Partial pass. The model generally preserved source fields, qualifiers and unknowns, but human review is still required for ownership, conflict classification and question usefulness.

### Feature implication

The feature should not be a simple completeness percentage. A safer design is a section-by-section review state with:

- source-linked claims;
- explicit `unknown`, `not_visible` and `conflicting` states;
- validation that `covered` sections have supporting claims;
- validation that covered verification questions actually exist;
- separate treatment of source evidence and system review rules;
- human accept/edit/reject controls.

## Reviewed correction records

Human correction records were added under `reviewed/` without modifying any raw model output. They reject the Vehicle Mechanic false conflict, correct the Driver question-coverage status, add the missing Part-Time Admin questions and preserve the human `decline` decision separately.

## Next action

Use these corrected records to design the low-fidelity interface test. The interface should expose section-level coverage, source-linked claims, unknowns, conflicts, questions and human correction controls rather than an overall completeness score.
