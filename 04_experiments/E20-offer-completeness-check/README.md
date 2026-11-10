# E20: offer completeness check

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-013, ASM-013

## Question

Do people who receive a job offer find missing or unclear terms, would they have used a check, and can a completeness check against official guidance find what an offer letter does not state, with sources, without giving legal conclusions?

FEAT-013 is not treated as feasible until this experiment has run. Nothing about this feature has been tested (T0), and the feature file records that no feature has been proposed yet. The need is supported (S-30, S-31, S-40, N2) by MOM and TAFEP material: Key Employment Terms must be given in writing within 14 days of the first day, notice tiers apply when a contract is silent, probation notice is addressed in MOM answers, and offers should state pay, benefits, duties and start date and allow time to consider ([R09 gap-fill](../../01_research/rounds/R09-job-seeker-processes-as-is/runs/2026-11-07-gap-fill/findings.md), FND-R09-03). Not verified in that work: the Employment Act text, any probation cap, CPF pro-rating for a mid-month start, the Workplace Fairness Act's recruitment duties and exemptions, and coverage by employee category.

## What is tested first (owner decision 2026-11-10)

**A completeness check against official guidance only.** The check takes an offer letter and reports which of the terms that MOM and TAFEP guidance say should be stated are present, missing or unclear, and whether the letter is inconsistent with itself (for example two different pay figures). It does not compare the offer with a posting snapshot or with what the user says was agreed verbally. Those comparisons are not in this test.

The checklist is compiled from MOM's Key Employment Terms page and the TAFEP guidance before the run, and reviewed by the owner. This README does not fix its contents.

The check does not say that a term is unfair, unlawful or non-compliant. It says what is stated, what is not, and what the guidance says, with the source.

## Hypotheses

- **H1 (need):** a meaningful share of offer recipients found a missing term or a discrepancy in an offer, and would have used a check (ASM-013).
- **H2 (finding):** a completeness check finds missing and inconsistent terms in offer letters, with the official source, without false alarms or legal conclusions.
- **H3 (value):** on their own offer, people see something they had not noticed.

## Part A: interviews

Needs 8 to 10 job seekers who received an offer in the last 12 months, recruited by the owner.

### Design

A structured interview about the most recent offer:

- What they received (verbal, email, letter, contract, handbook) and when, and the response deadline they were given
- What they checked, how, and with whose help
- Whether anything differed from what was advertised or agreed, or was missing, and what they did
- What they wish they had known or asked
- Whether they would have used a check at offer stage, and what would have stopped them
- What they are willing to share (a redacted letter, the terms only, nothing)

### Measures

- Share who found a missing term or a discrepancy
- Which terms were missing or differed (pay, bonus, notice, probation, hours, duties, start date, deadline)
- Share who would have used a check, and the reasons given
- Share willing to share a redacted letter for Part C

### Proposed thresholds (Part A)

Set before running.

- **Pass:** at least half found a missing term or a discrepancy in an offer they received, and at least half say they would have used a check.
- **Fail:** fewer than a quarter would have used a check.
- **Inconclusive:** anything between.

Participants consent to notes. Interview notes avoid names and employer identities, and no offer details beyond the term categories are stored.

## Part B: completeness fixture test

Runnable by the agent team. Needs no participants.

### Sample

20 offer letters:

| Source | Count | Purpose |
|---|---|---|
| Synthetic letters written from common templates, complete | 4 | Control: nothing should be flagged |
| Synthetic letters with planted missing terms (for example no notice, no probation, no pay date, no start date, no response deadline) | 8 | Recall on missing terms |
| Synthetic letters with planted internal inconsistencies (two pay figures, two start dates, notice in the letter differing from the handbook text) | 4 | Inconsistency detection |
| Real letters shared and redacted with consent from Part A, if available | 4 | Realism |

### Gold labels

- Written **before** any run by the owner from the compiled checklist, and checked by an HR or employment-law reviewer if one is found. If not, that is recorded as a limitation.
- For each letter: which checklist terms are stated, missing or unclear, which inconsistencies exist, and which official source each checklist item rests on.
- Labels are committed before results, so the order is visible in git.

### Method

1. The checklist is compiled and reviewed; letters and labels are written and committed.
2. The owner confirms the thresholds, and they are committed before any run.
3. Run the check on all 20 letters, twice, with at least two models, treating the letter as untrusted data. Record the model, prompt and harness version.
4. Score against gold labels. A prompt or checklist change means a new dated run folder, never an edit.
5. Write `FINDINGS.md`, add a finding to [findings.md](../../02_analysis/findings.md), and update FEAT-013.

### Measures

- **Recall of planted missing terms** and of planted inconsistencies
- **False alarms:** a term flagged as missing when the letter states it, or an inconsistency that is not there
- **Sourcing:** share of rule statements that name an official source and use it correctly
- **Legal conclusions:** any statement that a term is unfair, unlawful or non-compliant, or that the user should take action in law
- **Control letters:** complete letters that are flagged
- **Injection resistance:** a hidden instruction inside a letter that is followed
- **Stability** across two runs

### Proposed thresholds (Part B)

- **Pass:**
  - planted items found at least 90%
  - no more than 1 false alarm per 10 letters
  - 100% of rule statements cite a named official source, correctly
  - no legal conclusion on any letter
  - no hidden instruction followed
  - complete control letters not flagged
- **Fail:** recall under 70%, or any legal conclusion stated.
- **Inconclusive:** anything between.

## Part C: concierge on a real offer

Needs the Part A participants willing to share a redacted letter. A concierge test: the researcher runs the check and prepares the output.

### Design

Each participant sees the check's output on their own redacted offer and says what they notice, what they did not know, and what they would do next.

### Measures

- Whether the output showed something they had not noticed
- Whether it was understood as "what the letter does not state", not as a legal judgement
- Whether they would use it again at the next offer

### Proposed thresholds (Part C)

- **Pass:** at least half say it showed something they had not noticed, and most read it as a statement of what is missing, not a legal judgement.
- **Fail:** fewer than a quarter see anything new, or most read it as a legal verdict.
- **Inconclusive:** anything between.

Letters are redacted before they reach the researcher, used only for the session and not stored beyond the findings file. Retention and any model use are stated before the participant shares anything.

## Prerequisites

- The checklist, compiled from MOM and TAFEP pages and reviewed
- A human to write letters and gold labels who is not running the model
- Model access for at least two models, with cost recorded
- Owner time to recruit participants

## How the result is used

| Outcome | What it does to FEAT-013 |
|---|---|
| Parts A, B and C pass | Evidence for the owner to define the feature and to raise the levels. The gate for `in` needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A fails | People do not find problems or would not use a check. Park the feature. |
| Part A passes, Part B fails | The need exists but the check is unreliable. Rework the checklist or method, or park. |
| Part C fails | The check works but is misread. Rework the presentation. |

Comparing an offer with a posting snapshot or a recorded verbal agreement is a later question that this test does not answer.

## Layout

- `protocol/` the checklist, sample design and committed thresholds
- `data/` the letters and frozen gold labels
- `harness/` scoring scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Legal advice or any finding that a term is unlawful or unfair, negotiation advice (see FEAT-009 for pay), comparing an offer with a posting or an agreed verbal offer, handbook review, work-pass eligibility, and employer verification.

## Decisions for the owner before the run

1. Confirm or change the sample, parts and thresholds.
2. Approve the checklist and its sources.
3. Decide who writes the letters and gold labels, and whether an HR or employment-law reviewer is available.
4. Choose models and whether paid use is allowed.
5. Decide who recruits participants and how redacted letters are handled.

## Deviations

None yet.

## Limitations

- 8 to 10 interviews, 20 letters and a few concierge sessions support direction, not statistics.
- Interview participants are self-selected, and recall of an old offer is imperfect.
- Synthetic letters are cleaner than real ones.
- The checklist reflects guidance as read at the run date; the Workplace Fairness Act and other rules are changing.
- Employee categories and coverage differ; the checklist does not decide whether a given person is covered.
- If the same model family writes labels and runs the check, agreement is not independent. Use a human for labels.
