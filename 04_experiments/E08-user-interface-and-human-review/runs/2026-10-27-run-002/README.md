# Run 002 — Completeness-Gated Single-Posting Review

Status: execution in progress

Date: 2026-10-27

## Objective

Test whether an explicit completeness requirement makes the guarded AI review surface decision-critical gaps instead of silently omitting them.

## Changes from Run 001

- The prompt requires explicit coverage for every review section.
- Coverage may be `covered`, `unknown`, `not_visible` or `conflicting`.
- Each covered section must reference claim IDs where applicable.
- Three postings are run separately; they are never combined into one request.

## Fixtures

- `fixtures/r4-jb-003-input.json` — Class 4 Driver
- `fixtures/r4-jb-006-input.json` — Vehicle Mechanic
- `fixtures/r4-jb-011-input.json` — Part-Time Admin Assistant

## Required review sections

- role identity
- duties
- qualifications
- work conditions
- compensation
- compensation rules and qualifiers
- application process
- employer context
- contradictions
- unknowns
- decision-changing verification questions

## Pass conditions

- Each posting returns valid JSON.
- Each required section is explicitly covered or marked unknown/not visible/conflicting.
- No posting-specific facts are imported from another fixture.
- Compensation qualifiers and platform signals remain separated from employer claims.
- External action remains disabled.

## Limitations

This remains a model and fixture experiment. It is not user validation, production reliability evidence or proof that the completeness gate is sufficient for every occupation.
