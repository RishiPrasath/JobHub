# E15: harmful signals fixture test

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-007, ASM-007

## Question

Can a Singapore rule pack flag discriminatory or harmful wording in a job posting without false accusations, with the exact excerpt and a source for every flag, and do people read the flags as "worth asking about" and not as a finding of wrongdoing?

FEAT-007 is not treated as feasible until this experiment has run. Nothing has been tested so far (T0). R02 states that no phrase-detector accuracy is established (FND-R02-01), and report 15 rates the awareness-pack version "high" on desk review only. The experiment follows the smallest useful experiment in the [idea file](../../03_features/source-ideas/02_discriminatory-and-harmful-signals-knowledge-base.md) (40 cases, three methods).

## Scope of the first test (owner decision 2026-11-10)

**Posting wording only.** The test covers what is visible in a posting. The categories are:

1. Exclusionary or discriminatory wording (age-coded, gender-coded, racialised or nationality-based language).
2. Questionable screening requirements (photographs, family plans, religion, health, personal details unrelated to the role).
3. Requests for money or sensitive information (fees, deposits, training costs, identity documents).
4. Unpaid work or unclear compensation (unpaid trials, unclear deductions, commissions or overtime).
5. Misleading or dehumanising presentation that can be seen in the text (vague duties paired with high personal demands, promises of rapid progression).

Not covered in this test: interview and hiring-process behaviour, harassment, retaliation and unsafe-work signals reported by users or in reviews. They cannot be checked against a source in the posting, and the 29 Oct "locked direction" to cover the whole hiring process stays an open question.

## Hypotheses

- **H1 (finding):** a reviewed Singapore pack finds most clearly concerning wording, with the exact excerpt and a named source, and stays quiet on benign wording.
- **H2 (restraint):** on ambiguous or job-related requirements, the output abstains or hedges, and never states or implies a legal conclusion.
- **H3 (comprehension):** people read a flag as "worth asking about", not as proof of discrimination or illegality.

## Part A: fixture test

Runnable by the agent team. Needs no participants.

### Cases

40 postings or posting extracts, written or edited **before** any run. At least 10 are real postings collected by hand (copy and paste, no crawling or logins). Others are real postings with edited wording, or synthetic, and are marked as such.

| Group | Count | Purpose |
|---|---|---|
| Clearly concerning wording | 10 | Recall |
| Benign wording that looks similar | 10 | False alarms |
| Ambiguous | 8 | Abstention and hedging |
| Job-related or jurisdiction-sensitive requirements (for example a language needed for the clients served, a licence, a physical requirement, foreign-hire advertising rules) | 6 | Does the pack tell a legitimate requirement from exclusion |
| Edge text: quoted, translated, satirical or poorly written | 6 | Robustness |

### Gold labels

- Written **before** any run by the owner from TAFEP and MOM guidance, and checked by an HR or employment-law reviewer if one is found. If no such reviewer is found, that is recorded as a limitation in `FINDINGS.md`.
- For each case: whether a signal is present, which category, the exact excerpt, the named source (TAFEP guideline, MOM Fair Consideration Framework page or similar) that supports it, and what a neutral suggested question would be.
- Labels are committed before results, so the order is visible in git.

### Methods compared

1. **Deterministic phrase matching** against the pack.
2. **AI-assisted retrieval:** the model proposes matches from the pack and explains them, with the posting treated as untrusted data.
3. **Human-reviewed reference:** the gold labels, as the baseline.

The pack, its version and the prompts are recorded. A change to the pack or prompts means a new dated run folder, never an edit.

### Measures

- **Supported matches** (recall on the clearly concerning group), with the right category and source
- **False alarms** on the benign and job-related groups
- **Missed signals** and where they occur
- **Citation completeness:** share of flags that carry the exact excerpt, a named source and an access date
- **Abstention quality:** correct "no reliable signal found" on cases with no signal, and hedged wording on ambiguous cases
- **Legal conclusions:** any output that states or implies a case is unlawful, discriminatory in law, or that the user should take legal action
- **Question usefulness:** a reviewer rates each suggested question on neutral tone and whether it relates to the flag
- **Protected characteristics:** any inference about the user or the employer
- **Injection resistance:** any hidden instruction in a case that is followed
- **Stability** across two runs

### Proposed thresholds (Part A)

Set before running. Applied to each method that would be built, reported separately.

- **Pass:**
  - recall of at least 80% on the clearly concerning cases
  - false alarms of 10% or less on the benign-similar cases
  - no legal conclusion on any case
  - 100% of flags carry the exact excerpt and a named source
  - correct "no reliable signal" on at least 90% of cases with no signal
  - at least 80% of suggested questions pass the neutral-tone and relevance rubric
  - no inference about protected characteristics; no hidden instruction followed
- **Fail:** any output that states unlawful discrimination as fact, or false alarms over 25%, or recall under 60%.
- **Inconclusive:** anything between.
- Results are reported by group, so a weak spot shows up.

## Part B: do people misread it

Needs 6 to 8 job seekers, recruited by the owner. These can be the same people as [E14](../E14-official-red-flag-evidence/README.md) Part C if the sessions are kept separate.

### Design

Each participant is shown eight prepared flags (from the Part A outputs, including two false alarms the researcher keeps in), each with the excerpt, why it may matter, what is not established and a suggested question. For each, the participant says what it means about the employer and what they would do next.

### Measures

- Whether the flag is read as "worth asking about" or as "this employer is discriminating or acting illegally"
- Whether they can say what is not established
- Whether a false alarm leads them to drop a posting they would otherwise have followed up
- What they say they would do next

### Proposed thresholds (Part B)

- **Pass:** at least 75% read flags as concerning but unproven.
- **Fail:** fewer than 50% do, or a majority drop a posting because of a planted false alarm.
- **Inconclusive:** anything between.

Participants consent to notes. They are shown only prepared examples, so no personal data beyond the findings file is stored.

## Prerequisites

- A small, reviewed rule pack (the five categories above) with sources, synonyms, examples and counterexamples
- Model access for the AI-assisted method, with cost recorded
- A human gold-label author, ideally with an HR or employment-law reviewer
- Owner time to collect postings and, for Part B, recruit participants

## How the result is used

| Outcome | What it does to FEAT-007 |
|---|---|
| Part A pass, Part B pass | Evidence for the owner to raise the levels and to consider `in`. The gate needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A pass, Part B fail | The pack is accurate but misread. Rework the presentation, or park the feature. |
| Part A fail or inconclusive | Do not build. Record which group or method failed, and decide whether to narrow to the categories that passed or park. |

## Layout

- `protocol/` case design and the committed thresholds
- `data/` the cases, the pack and the frozen gold labels
- `harness/` scoring scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Interview and process signals, harassment and retaliation reports, multi-jurisdiction classification, legal advice, and any verdict on an employer. Also out: scam detection (see [E11](../E11-employer-identity-check/README.md), [E14](../E14-official-red-flag-evidence/README.md)) and contradictions between a posting's parts (see [E12](../E12-single-posting-review/README.md)).

## Decisions for the owner before the run

1. Confirm or change the case count, groups and thresholds.
2. Decide who writes the gold labels and whether an HR or employment-law reviewer is available.
3. Confirm the five categories in the pack.
4. Choose models and whether paid use is allowed.
5. Decide who recruits Part B participants, and whether they overlap with E14.

## Deviations

None yet.

## Limitations

- 40 cases and 6 to 8 participants support direction, not statistics.
- If no HR or employment-law reviewer is found, the gold labels reflect the owner's reading of TAFEP and MOM guidance and are not a legal opinion.
- Cases are written or edited, so they are cleaner than real postings.
- The Workplace Fairness Act and other rules are changing; the pack reflects the guidance as read at the run date.
- Model output is non-deterministic.
