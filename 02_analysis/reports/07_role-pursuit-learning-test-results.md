# Role-Pursuit Learning Test — Results

Status: bounded desk simulation complete — not a user study or usability test

Date: 2026-10-19

## Purpose

This test examined whether a structured, source-linked review helps a job seeker understand a posting, identify uncertainty, and choose a sensible next action without creating false confidence.

The comparison used the three existing Round 4 posting records:

- R4-JB-003 — MyCareersFuture Class 4 Driver
- R4-JB-006 — FastJobs Vehicle Mechanic
- R4-JB-011 — Jobstreet Part-Time Admin Assistant

Sources: [page inventory](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/page-inventory.md), [findings](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/findings.md), and [AI-assisted job-seeking and trust](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-round4-remaining-objectives/ai-assisted-job-seeking-and-trust.md).

## Conditions compared

| Condition | What was reviewed | Resulting decision record |
|---|---|---|
| A. Raw posting | The posting and visible platform context as recorded | Fast to access, but important conditions and unknowns remain scattered |
| B. Manual worksheet | A structured review of identity, duties, gates, conditions, pay, process, unknowns and next checks | More deliberate and trustworthy, but requires effort and careful recording |
| C. Guarded AI worksheet | The same structure with AI-assisted extraction, source references, unknown labels, conflict flags and verification questions | Faster organisation, but every consequential claim still requires review |

## Evaluation results

| Criterion | Result | Confidence | Evidence boundary |
|---|---|---:|---|
| Preserve source facts | Passed in the simulation | Medium | Material claims stayed tied to the recorded posting evidence |
| Preserve unknowns | Passed in the simulation | Medium | Missing guarantee, response, benefits and authenticity details were not filled by inference |
| Preserve contradictions | Passed in the simulation | High | The Jobstreet URL/title/body mismatch remained visible |
| Separate platform signals | Passed in the simulation | High | Match, response and safety signals were not treated as employer facts |
| Explain role conditions | Passed in the simulation | Medium | Shifts, rest days, worksite, pay qualifiers and work pattern were surfaced |
| Support a next action | Passed as a reasoning aid | Low-to-medium | Verification questions and continue/investigate/pause options were clear in the worksheet model |
| Edit or reject AI suggestions | Not executed | None | No working interface exists yet |
| Interrupt and return | Not executed; state requirements defined | None | Persistence was specified, not observed |
| Keyboard, zoom and assistive technology | Desk inspection only | None | No rendered interface or assistive-technology test exists |
| Real time saved | Not measured with participants | None | The comparison supports a directional claim only: less copying, more verification |
| Decision change for a real person | Not tested | None | No user participants were involved |

## Case findings

### R4-JB-003 — Class 4 Driver

The structured review improved visibility of the decision-critical conditions: Class 4 licence, day/night rotation, six-day week, four rest days per month, travel/port context, overtime and allowances. The salary range was retained as displayed and not converted into guaranteed base pay.

The correct next questions are about allowance and overtime calculation, exact schedule, response expectations and how the vacancy should be verified. The review must not conclude that the job is suitable, legitimate or financially worthwhile without the job seeker’s constraints and additional confirmation.

### R4-JB-006 — Vehicle Mechanic

The structured review brought together the 5.5-day week, Changi location, salary range, automotive qualification and licence wording. Employer identity and response indicators were kept separate from the role requirements.

The correct next questions concern detailed duties, benefits, assessment stages, licence expectations and what “normally responds within 24 hours” actually represents. The response indicator is not a guarantee.

### R4-JB-011 — Part-Time Admin Assistant

The structured review made the part-time pattern, Alexandra Hill location, hourly pay and 2–3 weekday expectation easier to compare. It also preserved the URL/title/body mismatch and the unrelated salary teaser rather than silently choosing one interpretation.

The correct next action is to verify the canonical posting, role identity, pay terms, schedule and application route before tailoring a resume or sharing personal information.

## Correction and rejection exercise

The simulated reviewer was given four deliberately unsafe suggestions:

1. “The Class 4 Driver salary is guaranteed base salary.”
2. “The FastJobs employer will respond within 24 hours.”
3. “The Jobstreet posting is definitely a scam because of the URL mismatch.”
4. “The candidate is a strong fit because the platform shows a match signal.”

Expected handling:

| Suggestion | Safe disposition | Why |
|---|---|---|
| Guaranteed base salary | Reject and restore source wording | Allowances and overtime were included or not fully established |
| Guaranteed response | Reject and label as a platform/employer signal | “Normally responds” is not a promise |
| Definitely a scam | Reject and retain as an unresolved source inconsistency | A mismatch warrants verification, not a fraud verdict |
| Strong fit | Reject | Personal fit requires user-provided context and cannot be inferred from a platform signal |

This demonstrates that the review model can define correction rules. It does not demonstrate that a real interface will make those corrections easy.

## Interruption and return requirement

The review should preserve, at minimum:

- source URL and access time;
- original wording for material claims;
- claim status: present, conditional, contradictory, not visible or unknown;
- user corrections and rejected suggestions;
- unresolved verification questions;
- current decision state: continue, investigate, save, pause or decline;
- the exact source version used for the review.

This is a design requirement derived from the analysis, not a tested product behaviour.

## Accessibility and comprehension requirement

A future low-fidelity prototype must be checked for:

- logical heading order;
- selectable text and readable contrast;
- keyboard navigation and visible focus;
- zoom/reflow without losing evidence or controls;
- plain-language distinction between fact, inference and unknown;
- an accessible way to inspect each source reference;
- no colour-only meaning for warnings or status;
- a clear review-and-correct path before any sharing or export.

No pass claim is made for these items until a rendered prototype is available.

## Findings

1. A structured review is more useful than a raw posting when conditions, pay qualifiers, source ownership and unknowns are scattered across a page.
2. Manual review is slower but easier to trust because the transformation is visible.
3. Guarded AI can reduce copying and help surface missing information, conflicts and verification questions.
4. The AI boundary must be evidence organisation and question generation, not hiring prediction, scam detection, personal-fit scoring or automatic application action.
5. The value is likely to come from better next questions and decision clarity, not from a polished summary alone.
6. The remaining uncertainty is interactional and behavioural: whether people can correct, resume, understand and act on the review.

## Independent review of the analysis

Three read-only specialist reviews checked the UX/recovery, evidence-safety and product-decision conclusions. They agreed that the simulation is directionally sound but identified an auditability gap: the repository does not yet contain the raw AI output, claim-level source locators, human correction log or reproducible error ledger.

Before treating the workflow as prototype-ready, the next test package must add:

- a claim ledger for every material output claim;
- at least three contradiction fixtures: URL/title/body mismatch, card/detail disagreement, and stale/current or platform/source disagreement;
- a correction and rejection log;
- an interruption, stale-source and restore checklist;
- one prompt-injection fixture to confirm that posting text is treated as untrusted content;
- a second-reviewer comprehension check for hard gates, unknowns and contradictions.

The completed claim audit is recorded in [role-pursuit evidence and claim audit](08_role-pursuit-evidence-audit.md). These are evaluation gates, not production requirements. They prevent a well-written simulation from being mistaken for auditable behavioural evidence.

## Decision recommendation

The opportunity survives as a **candidate for preparing a low-fidelity test**, not as an accepted prototype or implementation commitment.

Recommended next slice:

> A low-fidelity, source-grounded role-review worksheet that helps a person inspect a posting, mark facts and unknowns, record personal constraints, and choose what to verify next.

Keep these out of the next slice:

- resume generation or tailoring;
- universal fit scores;
- hiring-probability or legitimacy scores;
- automatic scam verdicts;
- automatic answers to sensitive questions;
- automatic application submission;
- cross-industry claims that have not been tested.

## What remains unproven

- whether job seekers would use the workflow repeatedly;
- whether it saves time after verification effort is included;
- whether it improves decisions or application quality;
- whether the same review structure works across industries;
- whether the interface is accessible in practice;
- whether the AI version is better than a carefully designed manual worksheet.

## Scope gate

This result is sufficient to justify preparing a disposable low-fidelity test instrument after the audit gates above are added. It is not sufficient to accept a production feature, declare the prototype validated, choose a platform or stack, or claim user validation.
