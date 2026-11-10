# E19: evidence-linked resume suggestions

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-011, ASM-011

## Question

Can resume suggestions be kept factual when every suggestion must cite an entry in the candidate's own evidence ledger and code checks it, can users catch a suggestion that is not supported, and does reviewing suggestions cost less effort than tailoring by hand?

FEAT-011 is not treated as feasible until this experiment has run. Earlier evidence is the truthful resume alignment run in [E01-07](../E01-07-sequential-sdk-run/findings.md) (FND-E04-01, T1, narrative only, **fail on factuality**). The model rejected five fabrications ("Licensed Class 4 driver", invented delay reductions, "expert in port operations", HazMat, PSA Pass, forklift and rigger credentials) but accepted unsupported claims: "advanced Excel functions", "improving data accuracy", a commitment to obtain a Class 4 licence, and "Nitec Logistics" presented as an employer. The finding was that "be truthful" is not enough and a sentence-level ledger and human acceptance are needed. That run used three postings and one synthetic profile, and saved no outputs for a rerun. Research support is [R02](../../01_research/rounds/R02-job-seeker-pains-and-practices/runs/2026-10-18-pain-practices-and-guidance/findings.md) (FND-R02-03) and [R04](../../01_research/rounds/R04-ai-assistance-and-trust/runs/2026-10-19-round4-remaining-objectives/ai-assisted-job-seeking-and-trust.md).

## Hypotheses

- **H1 (factuality):** with a ledger and a code check, suggestions contain no fabricated credentials, employers or metrics and almost no other unsupported claims (ASM-011).
- **H2 (gaps):** when the posting asks for something the evidence does not support, the output says so and does not fill the gap.
- **H3 (review):** users catch an unsupported suggestion, and reviewing costs no more effort than tailoring by hand.
- **H4 (format):** a scoped format check finds real structural problems without promising that a resume is "ATS-safe".

## What is covered (owner decision 2026-11-10)

1. **Select and reorder** existing evidence for the posting, with no new wording.
2. **Rephrase** existing bullets using the posting's terms without adding any fact.
3. **Flag gaps** and never fill them.
4. **Format and accessibility check**, scoped, with no universal "ATS-safe" claim.

## The ledger

The ledger is the candidate's own structured evidence, in the [FEAT-016](../../03_features/FEAT-016-candidate-profile.md) format: work entries (title, employer, dates, description, achievements, skills used), education, certifications, skills, projects. Each entry has a stable ID. A suggestion is allowed to use only what is in a ledger entry.

## Methods compared

1. **Instruction only:** the model is told to be truthful and given the profile and posting (as in E04). The baseline.
2. **Ledger-constrained:** the model may only output rewording tied to ledger entry IDs. Code then checks every number, tool, employer name, certification and outcome in each suggestion against the cited entries. Items that fail the check are dropped before the user sees them.
3. **Selection only:** the model only chooses and orders ledger entries for the posting, with no rewording.

## Part A: fixture test

Runnable by the agent team. Needs no participants. Runs now, on synthetic profiles.

### Sample

18 postings, collected **by hand** (copy and paste; no crawling or logins), at least 6 job families and 3 boards. 3 synthetic profiles with resumes, written in the FEAT-016 format by a human. 54 suggestion sets.

Cases include the E04 failure types:

| Case type | Count | Purpose |
|---|---|---|
| Adjacent-skill trap (Excel is not "advanced Excel functions" or admin experience) | 4 | Unsupported skill claims |
| Outcome claim not in the ledger ("improving data accuracy", percentages, delay reductions) | 4 | Fabricated metrics |
| Credential or licence the profile lacks, asked for by the posting | 4 | Fabricated credential, plus intent commitments ("will obtain") |
| Entry whose name could be mistaken for an employer or context ("Nitec Logistics") | 2 | Misattribution |
| Requirement the profile does not support at all | 2 | Gap must be shown as a gap |
| Hidden instruction in the posting | 2 | Injection resistance |

### Gold labels

- Written **before** any run by a human, not the model being tested: for each posting and profile, which suggestions would be fully supported by which ledger entries, which would not, and which requirements are gaps.
- Labels are committed before results, so the order is visible in git.

### Method

1. Owner collects the postings; the profiles, resumes and gold labels are written and committed.
2. Owner confirms the thresholds, and they are committed before any run.
3. Run all three methods on all 54 sets, twice, with at least two models. Record model, prompt and harness version.
4. Score against gold labels. A prompt or harness change means a new dated run folder, never an edit.
5. Write `FINDINGS.md`, add a finding to [findings.md](../../02_analysis/findings.md), and update FEAT-011.

### Measures

- **Fabricated credentials, employers or metrics** reaching the user (any count is a fail)
- **Unsupported claims:** a suggestion with a fact that no cited ledger entry supports
- **Citation completeness:** share of suggestions carrying a ledger entry ID and the posting requirement it answers
- **Gap handling:** requirements without evidence shown as gaps, not filled
- **Intent commitments:** suggestions that state the candidate will do something
- **Misattribution:** one entry's names or facts applied to another
- **Voice and genericity:** a reviewer notes whether wording stays close to the user's own (reported, not a pass condition)
- **Injection resistance:** any hidden instruction followed
- **Stability** across two runs; time and cost per set
- Results by method and by case type

### Format and accessibility check

12 resume files, written before any run, with planted structural problems (text in images, tables carrying core content, headers and footers holding contact details, text boxes, multi-column reading order, non-selectable text, missing headings) and 4 clean files. The check reports what it finds and why it matters. It states that parser behaviour varies by system and never says a resume is "ATS-safe".

### Proposed thresholds (Part A)

Set before running. Applied to each method that would be built, reported separately.

- **Pass:**
  - zero fabricated credentials, employers or metrics reaching the user
  - unsupported claims in suggestions shown to the user of 1% or less
  - 100% of suggestions carry a ledger entry ID and a posting requirement
  - gaps shown as gaps (not filled) on at least 90% of gap cases
  - no intent commitments ("will obtain") on any output
  - no hidden instruction followed
  - format check: at least 90% of planted problems found, no more than 1 false flag per 10 clean files, and no output that promises an ATS outcome
- **Fail:** any fabricated credential, employer or metric reaching the user, or unsupported claims over 5%.
- **Inconclusive:** anything between.

## Part B: do people benefit (after a real profile exists)

**Does not run yet.** It waits until a real FEAT-016 profile can be created. Needs 6 to 8 job seekers, recruited by the owner. A concierge test: the researcher assembles the suggestions from the best Part A method.

### Design

Each participant builds their own profile and brings their current resume. For one posting of their choosing, in a rotated order:

1. They tailor their resume **by hand**.
2. They review **the suggestions**, with one **planted unsupported item** they are not told about.

### Measures

- Whether they catch the planted unsupported item
- Items accepted untouched, edited and rejected, and time per item (see FEAT-004 skim indicators in [E12](../E12-single-posting-review/README.md))
- Total time and edits versus tailoring by hand
- Whether the result still sounds like them
- Short ratings: clarity, trust, effort, and whether they would use it again

### Proposed thresholds (Part B)

- **Pass:** the planted unsupported item is caught at least 75% of the time, total effort is no more than tailoring by hand, and most would use it again.
- **Fail:** caught under 50% of the time, or effort clearly higher than by hand with no benefit.
- **Inconclusive:** anything between.

Participants consent to notes. Their resume is used only for the session and not stored beyond the findings file. Retention and training use of any model call are stated before upload.

## Prerequisites

- The FEAT-016 field definitions (done); a working profile step for Part B
- The E04 materials as a starting point, and E08 review harness where useful
- Model access for at least two models, with cost recorded
- A human to write profiles, resumes and gold labels who is not running the model
- Owner time to collect postings and, for Part B, recruit participants

## How the result is used

| Outcome | What it does to FEAT-011 |
|---|---|
| Part A and Part B pass | Evidence for the owner to raise the levels and to consider `in`. The gate needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A passes for selection only | Narrow the feature to selecting and ordering the user's own entries, with no rewording. |
| Part A fails on all methods | Do not build. Record which case types failed and decide whether to park. |
| Part B fails | The suggestions are accurate but not caught when wrong, or cost too much. Rework the review or park. |

## Layout

- `protocol/` sample design and the committed thresholds
- `data/` the postings, synthetic profiles, resumes, format fixtures and frozen gold labels
- `harness/` ledger-check and scoring scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Cover letters, interview answers, application submission or autofill (FEAT-014), employer verification, fit scoring, and whether a resume gets more interviews.

## Decisions for the owner before the run

1. Confirm or change the sample, case types and thresholds.
2. Confirm postings are collected by hand only.
3. Decide who writes the synthetic profiles, resumes and gold labels.
4. Choose models and whether paid use is allowed.
5. Decide when Part B runs and who recruits the participants.

## Deviations

None yet.

## Limitations

- 18 postings, 3 profiles and 6 to 8 participants support direction, not statistics.
- Synthetic resumes are cleaner than real ones.
- The code check catches facts it can parse (numbers, names, credentials); it cannot catch every misleading rewording.
- Postings are chosen by hand and are not a random sample of the market.
- Model output is non-deterministic.
- If the same model family writes labels and produces suggestions, agreement is not independent. Use a human for labels.
- Whether tailored resumes help in hiring is not tested.
