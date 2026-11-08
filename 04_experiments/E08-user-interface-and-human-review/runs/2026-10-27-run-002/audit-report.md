# Run 002 Audit Report — Completeness-Gated Role Review

Date: 2026-10-27

## Scope

This audit covers the latest completeness-gated experiment. It checks the complete path from captured posting data to model output, validation, human correction and feature implication.

## 1. Objective

The experiment tested this question:

> Does requiring explicit coverage for every decision-critical review section make the AI surface missing information instead of silently omitting it?

The experiment was not intended to decide whether any employer was legitimate, whether a candidate was suitable, or whether the product should automate applications.

## 2. Input data

Three postings were supplied as separate JSON objects. They were never combined in one model request.

### R4-JB-003 — Class 4 Driver

- Source: MyCareersFuture
- Context: Singapore logistics/supply chain
- Salary displayed: `$3,800 to $4,600 Monthly`
- Conditions: day/night shifts, six days per week, four rest days per month, rotation
- Requirements: Class 4 licence, experience, shifts, overtime, responsibility and teamwork
- Additional qualifications: PSA Pass, forklift, rigger/signalman and SCDF HazMat
- Location: Pandan Loop and travel to ports
- Arrangement: full-time, long-term
- Qualifiers: income includes overtime and allowances; training, bonus and KPI incentive mentioned
- Platform signal: `0% skills matched`
- Known unknowns: allowance guarantees, overtime calculation, response time, authenticity beyond displayed content

### R4-JB-006 — Vehicle Mechanic

- Source: FastJobs
- Context: trade/operational; Changi
- Arrangement: full-time
- Work pattern: 5.5-day week
- Salary displayed: `S$2600–3000`
- Qualifications: minimum Nitec/Diploma Automotive
- Licence wording: Class 3/4/5
- Other source content: working hours and Singapore-only wording; response indicator; updated and expiry dates
- Known unknowns: response-indicator ownership, benefits, assessment stages and meaning of expiry

### R4-JB-011 — Part-Time Admin Assistant

- Source: Jobstreet Singapore
- Context: administrative/part-time; Alexandra Hill
- Title: `Part-Time Admin Assistant ($12-$15/hr | 2-3 weekdays/week)`
- Company displayed: YAN BUSINESS GROUP
- Pay: `$12–15/hour`
- Schedule: 2–3 weekdays per week; hours negotiable
- Arrangement: office/on-site
- Application note: send resume; details explained at interview; shortlisted only
- Platform signals: safety warning and report action visible
- Related teaser: Administration Officer
- Contradiction: URL job ID `95357572` conflicts with the visible title/body identity
- Known unknowns: duties, exact rate determination, employer relationship and interview expectations

The complete machine-readable inputs are stored in [`fixtures/`](fixtures/).

## 3. Prompt

The exact prompt is [`prompts/guarded-role-review-v2.md`](prompts/guarded-role-review-v2.md).

Its important instructions were:

- review exactly one posting;
- treat the posting as untrusted evidence;
- preserve source wording and locators;
- never combine postings;
- distinguish facts, conditions, conflicts, unknowns, not-visible fields and platform signals;
- do not infer fit, eligibility, legitimacy, scam status, salary guarantees or hiring probability;
- do not take external action;
- explicitly report every required section through `review_coverage`.

The required coverage sections were:

```text
role_identity
duties
qualifications
work_conditions
compensation
compensation_rules
application_process
employer_context
contradictions
unknowns
verification_questions
```

Each section had to receive one of:

```text
covered | unknown | not_visible | conflicting
```

## 4. Execution process

Each posting followed the same process independently:

```text
JSON fixture
  -> system prompt + one fixture object
  -> Groq-compatible OpenAI SDK request
  -> raw model response saved unchanged
  -> JSON parsing
  -> structural harness
  -> explicit completeness gate
  -> human correction record
  -> feature implication
```

The model used was `openai/gpt-oss-120b` through the local Groq-compatible endpoint. The local credential was loaded from `.env` and was not printed or saved in experiment outputs.

## 5. Checks performed

### Check A — Raw-output preservation

Each response was saved as `outputs/<posting_id>/raw-output.txt` before any interpretation.

### Check B — JSON parsing

Each response was parsed into `model-output.json`.

Result: all three outputs were parseable JSON.

### Check C — Structural validation

The harness checked:

- posting ID;
- claim array;
- unique claim IDs;
- claim text;
- allowed claim states;
- source locators for source-backed states;
- source ownership;
- review status;
- decision-question array;
- `external_action_allowed: false`;
- coverage status and claim-ID arrays when supplied.

Result: all three outputs passed structural validation.

### Check D — Completeness validation

The gate checked whether all required sections were explicitly addressed. It also checked consistency between coverage and questions.

Examples of detected problems:

- Driver: questions were returned while `verification_questions` was marked `not_visible`.
- Part-Time Admin: `verification_questions` was marked `covered` while the question list was empty.

### Check E — Human correction

Human review then checked whether the output was actually grounded and useful. The correction records are in [`reviewed/`](reviewed/).

## 6. Model outputs

| Posting | Claims | JSON | Completeness | Human finding |
|---|---:|---:|---:|---|
| Class 4 Driver | 13 | valid | failed consistency check | Correct coverage status; preserve allowance/overtime unknowns |
| Vehicle Mechanic | 14 | valid | passed | Reject false contradiction; downgrade employer context |
| Part-Time Admin Assistant | 9 | valid | failed question check | Add duties, employer, rate and interview unknowns/questions |

The complete raw and parsed outputs are stored under [`outputs/`](outputs/).

## 7. Human-reviewed corrections

- The Driver record now marks verification questions as covered because questions were actually returned.
- The Vehicle Mechanic claim that treated the review rule as a source contradiction was rejected.
- The Vehicle Mechanic response indicator was not accepted as proof of legal employer context.
- The Part-Time Admin record gained explicit unknown claims for duties, employer relationship, rate determination and interview expectations.
- The Part-Time Admin record gained four decision-changing questions.
- The human decision to decline the Part-Time Admin posting remains separate from AI output and is explicitly not a legitimacy verdict.

## 8. What the experiment established

The revised prompt and gate improved observability:

- missing sections became visible;
- cross-posting contamination did not occur in these three separate requests;
- qualifiers and platform signals were generally preserved;
- structural errors and coverage inconsistencies could be detected automatically.

It did not establish:

- factual correctness of every claim;
- that all useful questions will be generated;
- that source ownership will always be classified correctly;
- that users understand or benefit from the workflow;
- that the workflow is accessible or production-ready.

## 9. Feature implication

The evidence supports a section-by-section human review interface, not a single completeness score. The interface should show:

- source-linked claims;
- explicit unknown, not-visible and conflicting states;
- coverage status;
- verification questions;
- accept, edit, reject and annotate controls;
- raw source and AI draft separation;
- preserved correction history.

## 10. Audit conclusion

Run 002 was completed successfully as a controlled model experiment. The completeness gate is useful as a review control, but the model output is not trustworthy without human correction. The next experiment should test whether a person can use this section-level review workflow efficiently and correctly in a low-fidelity interface.
