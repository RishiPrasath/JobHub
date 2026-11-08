# Manual-versus-AI Comparison — R4-JB-011

## Run metadata

- Model: `openai/gpt-oss-120b` through the local Groq-compatible endpoint
- Model request: completed
- Raw response: `raw-model-output.txt`
- Parsed response: `model-output.json`
- Harness result: valid
- Claims returned: 13
- External action allowed: false

## What the model captured well

- Role title and employer name.
- Displayed hourly pay and part-time schedule.
- Office/on-site arrangement.
- The limited application note.
- Platform safety and reporting signals as platform-owned signals.
- The URL/title/body identity conflict.
- External actions remained disabled.

## Important omissions

The manual review identified several decision-changing unknowns that the model did not represent clearly enough:

- The actual day-to-day duties are not stated.
- The posting does not establish who the legal employer is or whether the named company is the hiring organisation or a recruiter/client reference.
- The exact method for determining the rate within the S$12–S$15 range is not stated.
- The posting does not explain what information or commitment is requested during or after the interview.

## Unsupported or weakly grounded questions

The model proposed questions about:

- whether the displayed rate includes overtime, bonuses or allowances;
- whether the platform warning indicates specific concerns;
- whether the Administration Officer teaser implies additional compensation expectations.

These are not necessarily bad questions, but the captured source does not establish overtime, bonuses, allowances, specific safety concerns or a compensation relationship with the Administration Officer teaser. They require human editing before use.

## Comparison with the human decision

The human reviewer chose `decline` because the posting withholds the duties, leaves compensation and working hours unclear, does not sufficiently establish the employer context, and requests a resume before providing meaningful details.

The AI output did not independently reproduce that rationale. It is therefore useful as a draft evidence organiser, but not as a decision-maker or complete review substitute.

## Assessment

### Structure

Pass. The output was valid JSON and passed the deterministic harness.

### Evidence organisation

Partial pass. The basic facts and contradiction were organised, but important unknowns were omitted.

### Decision support

Fail for this run. The model did not surface the key missing duties and employer-context questions that drove the human decline decision.

### Product implication

The first JobHub capability should remain human-reviewed source organisation. The output needs an explicit completeness check for missing decision-critical fields before it can be considered useful for a role decision.

## Corrections required before treating the output as reviewed

1. Add an `unknown` claim stating that actual duties are not established in the captured record.
2. Add an `unknown` claim stating that the legal employer or recruiter relationship is not established.
3. Add a verification question asking how the exact hourly rate is determined.
4. Retain the contradiction between the URL job ID and page title/body.
5. Remove or qualify questions that imply facts not present in the source.
6. Keep the human `decline` decision separate from the AI draft.
