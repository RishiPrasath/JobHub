# Low-Fidelity Role-Review Test Instrument

Status: model-assisted runs executed; not yet tested with participants or a rendered interface

Date: 2026-10-20

## Purpose

This instrument tests the approved JobHub hypothesis:

> A human-reviewed, source-grounded single-posting worksheet can improve clarity about unknowns, contradictions and verification steps.

It compares a raw posting, a manual worksheet and a guarded AI-assisted worksheet. It does not test fit scoring, resume generation or application automation.

## Run package

The executable test package is located at:

[`04_experiments/E08-user-interface-and-human-review/runs/2026-10-20-run-001/`](../../04_experiments/E08-user-interface-and-human-review/runs/2026-10-20-run-001/)

The completeness-gated follow-up run is documented at [`04_experiments/E08-user-interface-and-human-review/runs/2026-10-27-run-002/`](../../04_experiments/E08-user-interface-and-human-review/runs/2026-10-27-run-002/).

It contains:

- three separate captured posting fixtures;
- the manual worksheet;
- the guarded AI prompt;
- a deterministic claim-review harness;
- a sample structured output;
- accessibility and recovery checks;
- run instructions and limitations.

## Conditions

| Condition | Purpose |
|---|---|
| Raw posting | Baseline for scattered information and first impression |
| Manual worksheet | Human-created structured baseline |
| Guarded AI worksheet | AI draft extraction with source links and explicit uncertainty |

## Required comparison questions

- Can the reviewer identify hard requirements?
- Can the reviewer explain what the salary does and does not establish?
- Can the reviewer identify missing, conditional and conflicting information?
- Can the reviewer choose a sensible next verification question?
- Can the reviewer correct or reject an unsafe suggestion?
- Can the reviewer resume after interruption without losing provenance or corrections?
- Does the AI version reduce organisation effort without creating more review effort than value?

## Execution boundary

The package is ready for a low-fidelity or concierge test. It is not evidence of user validation, accessibility compliance, production readiness or a final product scope.
