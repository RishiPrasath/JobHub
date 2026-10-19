# AI-assisted job hunting: initial findings

Date: 2026-10-18. Status: specialist reviews completed; coordinator corrections applied; pending human acceptance. This is the initial approved product-research run, not completion of the entire product or AI-development research backlog.

Source IDs resolve through [sources.md](sources.md). Detailed evidence and caveats live in the linked specialist registers.

## Main conclusion

Test whether JobHub can help someone preserve a role, understand the evidence, return after an interruption, and prepare truthful material with less correction effort. This is a candidate experiment, not validated market positioning or accepted scope. The current evidence supports investigating selective assistance; it does not justify assuming full automation produces better hiring outcomes.

## Claim-level findings

| ID | Finding | Evidence | Type and confidence | Implication |
| --- | --- | --- | --- | --- |
| F01 | Assistance can improve presentation, but outcome effects depend on the intervention and labour market | P01-P02 | Source-reported empirical results; bounded causal/identification claims, limited transfer | Evaluate current workflows directly; do not promise interview or hiring gains |
| F02 | Some job seekers combine AI with manual edits, saved postings, and spreadsheets | P07-P08; compatible with I01-I06 | First-person reports and one documented internal system; low population confidence | Test continuity and repeated context entry with ordinary users |
| F03 | Tracking, AI writing, and some application automation already coexist in career products | T04-T07; local alternatives D03-D04 | Official documentation; high for documented offering, untested performance | Feature aggregation alone is not proven differentiation |
| F04 | Qualitative accounts report checking, editing and selective avoidance; internal documents prescribe review gates | P06-P08, I03-I05 | Reported experience and documentary evidence; adoption impact remains a hypothesis | Measure checking/correction effort and allow disagreement |
| F05 | Singapore statistics describe varied occupations and working/caregiving circumstances | D01-D02 | High confidence in reported population facts within survey coverage | Coordinator implication: recruit across sectors and preserve mandatory licences/requirements |
| F06 | This scan cannot decide mobile versus web | User's stated problem; D02 and I01-I07 do not measure device preference | Explicit evidence gap | Compare the same interrupted task across surfaces before choosing |
| F07 | Interview rehearsal exists as a reported practice and documented service | P08, D04, T04 | Anecdote/service documentation; limited outcome confidence | Evaluate rehearsal separately from live interview assistance |
| F08 | User-visible workflow state needs to be clear | I03-I06, T07 | Documented distinction; coordinator design inference | Saving, preparing, reviewing, and submitting should not be conflated |
| F09 | Internal workflows prescribe separate source-authenticity checks before preparation | I03-I04, I06 | Observed documentation only; no detection-performance evidence | Test comprehension of unverified identity and unsafe-contact signals; do not present a signal as proof of wrongdoing |

## Important empirical qualifications

P01 evaluates nongenerative writing assistance; it is not evidence that today's general assistants deliver the same improvement. P02's callback estimate is statistically weak at conventional thresholds and fades; employment gains remain inconclusive. Human editing is associated with outcomes but was not randomized. Together they support careful task evaluation, not a universal AI benefit or harm claim.

P01 concerns online-labour-market entrants. P02 uses January-September 2023 Freelancer.com bids in PHP and internet marketing. P06 concerns 17 English-speaking blind/low-vision participants interviewed in June-September 2024. Recent publication/access dates do not make these current behavioral observations. P02's version-date discrepancy remains unresolved.

## What real workflows suggest

The public accounts describe a mixture of search, writing, rehearsal, manual changes, and ordinary tracking tools. The internal system documents more explicit gates and durable records. Shared themes are useful hypotheses about continuity and ownership, but neither anonymous professional accounts nor one elaborate personal system represents all job seekers.

Planning, sourcing/networking effectiveness, company-fact verification, follow-up effectiveness, and sustained use are particularly thin evidence areas. A reported integration failure does not establish that competitors generally fail. A job offer following AI use does not establish causation. D04 emphasizes ATS optimization while D05 emphasizes human/contextual judgment; neither establishes a universal screening process.

The internal source-authenticity controls include identity uncertainty and unsafe-contact holds. These show intended safeguards, not adherence, detection accuracy, or scam prevalence. Their package-map tables omit authenticity phases present in YAML/control sections, so even the process documentation has internal inconsistencies. These rules are not automatically adopted as JobHub policy.

## Tool and competitor interpretation

The [six-tool matrix](specialists/ai-tools.md) distinguishes reusable context from career-specific records, generation, practice, and autofill. Existing offerings overlap with the original JobHub idea. Their documented features do not establish usability, factuality, privacy implementation, or Singapore compatibility. No universal winner can be ranked from these records.

The inspected Copilot instructions retain final user submission; the separate Autopilot offering must not inherit that characterization. The recorded T08 policy review describes permitted own-system AI development and selected recruiter disclosures with source-specific exclusions. Third-party training restrictions do not imply exclusion from all AI use or sharing. This was policy inspection, not an implementation audit.

## Automation boundaries to test

| Activity | Candidate AI contribution | User judgment to preserve | Evaluate |
| --- | --- | --- | --- |
| Capture | Extract posting text and structured fields | Correct fields and choose whether to save | Missing/changed data, source fidelity, and comprehension of unverified source identity |
| Understand a role | Explain requirements, unknowns, and transferable experience | Decide whether the opportunity fits personal circumstances | Misstated requirements and comprehension |
| Prepare materials | Suggest wording using confirmed experience | Accept/reject factual claims and final wording | Unsupported assertions and correction time |
| Interview practice | Generate practice questions and feedback | Supply truthful examples and assess advice | Grounding, feedback quality, accessibility |
| Tracking | Suggest status updates from available evidence | Confirm consequential events such as submission | False status changes and recovery |
| External application | Prepare a reviewable package | Explicitly choose what and where to submit | No submission experiments in this run |

These are proposed product boundaries for validation, not approved privacy/security architecture.

Screening must distinguish information not evidenced from experience known to be absent, and employer-stated requirements from independently verified credential obligations. The proposed test should allow correction and retaining an opportunity; it should not automatically reject users, infer sensitive characteristics, or present hiring probabilities. One negative company review or model interpretation cannot establish misconduct or employer suitability.

Interview-feedback experiments should assess answer content against explicit criteria, offer text participation, and allow correction. They should not infer honesty, personality, or employability from accent, disability-related presentation, fluency, or one answer. Persistent learning records should be optional, correctable, and deletable.

## Candidate first experiments

1. **Save, understand, and resume one job.** Preserve source/version and uncertainty; let the user return and explain the next action. Best small starting experiment because it exercises evidence and continuity without implementing the entire application lifecycle. Evidence for broad demand remains limited.
2. **Prepare one truthful application section.** Use confirmed experience, make gaps visible, and compare checking effort with the user's existing process. Writing is crowded; differentiation must be demonstrated.
3. **Rehearse one interview answer.** Reuse truthful evidence and test whether feedback helps the user improve. Requires separate evaluation of realism, accessibility, and feedback quality.

The UX specialist recommends testing role screening first. The tools specialist recommends matched synthetic tasks measuring corrections, recovery, export completeness and control. The practices specialist recommends interviews/diaries and realistic tasks. The coordinator proposes prioritizing a small screening/return test alongside interviews. These are different emphases, not a documented disagreement about sequencing.

## Next validation and decision criteria

Use the [synthetic comparison fixture](../../../../05_evidence/datasets-and-examples/2026-10-18-synthetic-workflow-check.md) and [UX experiment proposals](specialists/ux-workflows.md). Record task completion, unsupported claims, correction effort, source understanding, state recovery, and user willingness to return. Include frontline/shift workers, career changers/returners, and varied digital confidence and accessibility needs. Small pilots reveal problems; they do not estimate national rates.

Choose a scope only after comparing these options against observed user needs. Reconsider the proposed first experiment if users mainly need sourcing, networking, or interview support, or if existing tools already solve continuity adequately.

Before recruiting participants, specify consent, optional recording, access/recipients, retention/deletion, withdrawal limits, and removal of third-party details. Identifiable diaries/transcripts stay out of Git. Real personal-data uploads require a separate decision; the prepared tool fixture remains synthetic. Report each participant's failures and accommodation needs; aggregate completion and speed must not conceal exclusion. Proposed pilot timings are descriptive, not gates that penalize accessibility needs.

## Review trail

Read the [Evidence Synthesizer corrections](specialists/evidence-synthesis.md) and [Responsible AI review](specialists/responsible-ai-review.md). Both reviewed the draft; the coordinator applied the recorded corrections. This is not a runtime safety audit, a legal assessment, or human acceptance of the recommendations.
