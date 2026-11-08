# Manual versus AI-assisted role review

Status: bounded simulation complete — not a user study

Date: 2026-10-19

## Comparison performed

The same three existing job-posting records were reviewed:

- R4-JB-003 — MyCareersFuture Class 4 Driver
- R4-JB-006 — FastJobs Vehicle Mechanic
- R4-JB-011 — Jobstreet Part-Time Admin Assistant

Two approaches were compared:

1. Manual structured worksheet.
2. Guarded AI-assisted structured review.

The source material was the existing Round 4 page inventory. No personal data, live applications or external contact were used.

## What the manual worksheet did well

The manual review made several important distinctions visible:

- source/employer content versus platform signals;
- base pay versus income that includes overtime or allowances;
- required versus additional qualifications;
- stated, conditional, missing and conflicting information;
- useful verification questions;
- a provisional next action without a fit score or legitimacy verdict.

It also exposed different problems in each posting:

- **Class 4 Driver:** compensation composition, shift pattern and additional qualification status.
- **Vehicle Mechanic:** pay frequency, exact hours, licence meaning and expiry interpretation.
- **Part-Time Admin Assistant:** URL/title/body inconsistency and deferred role details.

## What guarded AI assistance added

AI was useful for:

- extracting common fields from differently structured pages;
- preserving original section labels;
- separating platform signals from source wording;
- surfacing unknown and not-visible fields;
- detecting the URL/title conflict;
- generating source-specific verification questions;
- reducing repetitive copying and initial organisation.

## What AI could not safely decide

AI must not determine:

- whether the candidate is suitable;
- whether the employer is legitimate or unreliable;
- whether a posting is fake, a ghost job or a scam;
- whether a salary is guaranteed base pay;
- whether a platform match score is meaningful;
- whether “Singapore-only” implies nationality or work-rights status;
- whether a vacancy will produce an interview;
- whether the user should apply without considering personal constraints.

## Comparison result

| Dimension | Manual worksheet | Guarded AI review |
|---|---|---|
| Initial extraction | More effort | Faster and more consistent in structure |
| Provenance | Depends on careful human recording | Can attach source references, but still needs checking |
| Unknown handling | Human must notice gaps | Can surface gaps, but may still over-infer without controls |
| Contradictions | Human can notice and document them | Can flag conflicts but must not resolve them silently |
| Candidate fit | Requires user-provided context | Cannot infer personal fit safely |
| Verification questions | Human-generated | AI can propose targeted questions |
| Review burden | Higher upfront | Lower copying effort, but consequential claims still need review |
| Safety | Manual by default | Safe only when suggestions are editable/rejectable and actions are disabled |

## Test result

### Passed in the simulation

- No fabricated salary, employer, credential, schedule or eligibility facts.
- Material claims were source-grounded or explicitly marked unknown.
- Platform signals remained separate from employer/source facts.
- No unsupported scam, fraud, safety or hiring prediction was made.
- The URL/title conflict was preserved rather than silently corrected.

### Not tested

- Whether a reviewer can edit or reject every AI suggestion.
- Whether the workflow survives interruption and return.
- Whether the review is accessible with keyboard, zoom or assistive technology.
- Whether the review changes a real person’s decision.
- Whether AI actually saves time after verification effort is included.

## Conclusion

The guarded AI review is promising as an organisation and uncertainty-surfacing aid. It is not proven better than the manual worksheet, and it does not replace human judgment.

The full test therefore remains **incomplete**, not a product success or failure. The missing evidence is interaction evidence: correction, recovery, accessibility and decision usefulness.

## Practical finding for JobHub

The first useful capability is not “AI tells you whether to apply.” It is closer to:

> “AI helps organise what the posting says, what it does not say, what may conflict, and what you should verify next.”

That is still a candidate direction, not an accepted feature.

## Next step

Create a simple low-fidelity worksheet or prototype and test the correction, interruption and accessibility states using the same three postings. Do not add resume generation, fit scoring or application automation yet.

Sources: [Round 4 page inventory](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/page-inventory.md), [role-pursuit walkthrough](05_role-pursuit-walkthrough.md), [role-pursuit learning test](04_role-pursuit-learning-test.md).
