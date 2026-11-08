# Run Findings: Low-Fidelity Human-Review Instrument

## Status

The test instrument is prepared and the first guarded live model run has now been completed. The deterministic claim-review harness passed on both the sample output and the parsed live model output.

This run has not yet included:

- a rendered interface;
- a real participant or user session;
- an application submission or other external action.

## Validation performed

Command:

```text
python 04_experiments/E08-user-interface-and-human-review/runs/2026-10-20-run-001/code/claim_review_harness.py 04_experiments/E08-user-interface-and-human-review/runs/2026-10-20-run-001/fixtures/sample-ai-output.json
```

Observed result:

- `valid: true`
- `posting_id: R4-JB-011`
- `claim_count: 4`
- `errors: []`
- next step: human provenance review required

## Live model validation

The live model response was saved without editing in `raw-model-output.txt`, parsed into `model-output.json`, and validated with the harness. The model returned 13 structurally valid claims. A manual comparison found that it captured the basic facts and posting contradiction but omitted important unknowns about duties, employer context and rate determination. See [`comparison-findings.md`](comparison-findings.md).

## Completeness-gate result

The updated harness reported:

```json
{
  "valid": true,
  "complete": false,
  "missing_sections": [
    "duties",
    "qualifications",
    "compensation_rules",
    "employer_context",
    "unknowns"
  ]
}
```

This is the expected distinction: the model output is valid JSON, but it is not complete enough for a decision review. The gate is a conservative lexical coverage check; it can identify missing explicit coverage but cannot determine whether a covered claim is factually correct. Human provenance review remains mandatory.

## Interpretation

The validator can detect basic provenance and safety-structure violations before a reviewer relies on an AI-generated worksheet. The completeness gate now also flags decision-critical areas that were not explicitly addressed. The validator does not establish that a claim is factually correct, or that the worksheet is useful, understandable, accessible or accurate in practice. Those questions require the manual-versus-AI comparison in the run README and a later rendered-interface or participant test.

## Next action

Run the comparison using one fixture at a time, record the raw decision, manual worksheet, guarded AI output, corrections, unresolved questions, recovery behavior, and accessibility observations. Keep the result as a dated run record; do not convert it into a product requirement without human review.
