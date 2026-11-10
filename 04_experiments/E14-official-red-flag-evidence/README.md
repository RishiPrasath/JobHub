# E14: official red-flag evidence

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-006, ASM-006

## Question

Can enough official sources be read, within their terms of use, to give a job seeker useful evidence about an employer, and is that evidence found reliably and shown in a way that is not misread?

FEAT-006 is not treated as feasible until this experiment has run. Earlier evidence is [E10](../E10-market-value-and-red-flag-experiments/FINDINGS.md): X0 found only 2 of 7 official sources machine-readable (MAS and CASE), none about employment (FND-E10X0-01). X1 found all 12 known problems with both a fixed sweep and free-form research, so it could not separate them; its test set was recent, heavily reported and taken from the newest list entries (FND-E10X1-01). E14 does not edit or replace E10. It is a new experiment with its own sources and company list.

## Hypotheses

- **H1 (coverage):** at least one official source about employment (MOM, PDPC, courts or similar) can be read within its terms of use, where X0 could not.
- **H2 (finding):** on a harder set, older, smaller and less reported cases, a fixed sweep still finds most known problems with sources, without unsupported claims and without wrongly flagging clean companies.
- **H3 (presentation):** people do not misread a brand-impersonation warning as employer misconduct, and do not treat "nothing found" as proof the employer is clean.

## Part A: source access retry

Runnable by the agent team. Needs no participants.

### Sample

The five sources X0 could not read: PDPC, SGX, the judiciary pages, the MOM directories, and eLitigation (down for maintenance during X0). Add any other official employment-related route found during the retry, such as the MOM agency directory and the MOM enforcement pages, and the ACRA and ScamShield routes named in R09.

### Method

1. For each source, record the terms of use and any robots or rate limits **before** fetching.
2. Retry with a rendering fetch for sources that failed to load a list. Respect the rate limits and any ban on reproduction (MAS, for example, asks for no more than one request per 2 seconds and bars reproduction). No logins, no job-board crawling.
3. Classify each source as readable and permitted, readable but not permitted, or not readable. Record what a readable source can answer (list of entities, individual records, dates).
4. Write results to a new dated run folder. Do not edit the X0 outputs.

### Proposed thresholds (Part A)

Set before running.

- **Pass:** at least one employment-relevant official source is readable and permitted by its terms.
- **Fail:** none is. In that case the feature narrows to MAS enforcement actions, CASE alerts and links to the official lookups the user runs themselves, and the owner decides whether to keep it.
- Sources that are readable but not permitted count as not readable.

## Part B: harder sweep

Runnable by the agent team. Needs no participants. Runs on whichever sources Part A and X0 show to be readable and permitted.

### Sample

At least 30 organisations:

| Stratum | Count | Purpose |
|---|---|---|
| Known problems that are older (before 2022), smaller or less reported | 15 | Test recall where search does not trivially succeed |
| Clean controls, checked by hand against the readable official lists and a search of news | 15 | Test false flags |

Ground truth for the 15 known problems is taken from the official record **before** any run. Control companies are chosen before any run and are not proven clean, only not found on the readable lists (see Limitations).

### Arms

1. **Fixed sweep:** the six-query pack from X1 plus a direct check of each readable official list.
2. **Free-form:** an agent with up to 8 searches per organisation, as in X1.

The fixed sweep is the arm the product would use. The free-form arm is the comparison.

### Measures

- **Recall:** share of the 15 known problems found, with a source.
- **Unsupported claims:** claims shown without a supporting source, or whose source does not support them.
- **Wrong employer-level flags on controls:** a control shown as having a red flag about the employer that it does not have.
- **Impersonation handling:** every brand-impersonation warning (a warning about the brand being imitated) is labelled as such and not shown as misconduct by the employer.
- **Cost and time** per organisation, and the number of failed page reads.

### Proposed thresholds (Part B)

Applied to the fixed sweep. The difference between the arms is reported, not part of the pass bar, because X1's hypothesis that the sweep beats free-form was not supported.

- **Pass:**
  - recall at least 70% on the harder set
  - unsupported claims 2% or less
  - no more than 10% of controls (at most 1 of 15) given a wrong employer-level flag
  - 100% of impersonation warnings labelled as brand impersonation
- **Fail:** recall under 50%, or any unsupported claim shown without a source.
- **Inconclusive:** anything between.

Results are reported by source and by organisation size.

## Part C: do people misread it

Needs 6 to 8 job seekers, recruited by the owner. These can be the same people as [E11](../E11-employer-identity-check/README.md) Part B if sessions are kept separate.

### Design

Each participant is shown six short outputs, in a rotated order:

1. A confirmed regulator action against the employer.
2. A brand-impersonation warning (the employer is the one being imitated).
3. A consumer-complaint alert.
4. A "nothing found" result for a clean employer.
5. A "nothing found" result for an employer whose entity could not be resolved.
6. A non-employment item (for example a police probe of an app).

For each, the participant says what it means about the employer and what they would do next.

### Measures

- Whether the impersonation warning is read as being about the brand being imitated, not as misconduct
- Whether "nothing found" is described as "safe", "clean" or "verified", rather than as "nothing in the sources checked"
- Whether a non-employment item is taken as an employment red flag
- What the participant says they would do next

### Proposed thresholds (Part C)

- **Pass:**
  - at least 75% read the impersonation warning correctly
  - at least 75% do not treat "nothing found" as clean
- **Fail:** fewer than 50% on either measure.
- **Inconclusive:** anything between.

Participants consent to notes. They are shown only prepared examples, so no personal data beyond the findings file is stored.

## Prerequisites

- The [E10 X1 search pack](../E10-market-value-and-red-flag-experiments/protocols/X1-red-flag-sweep.md) and company list format
- Model and search access (OpenSERP, as in E09), with cost recorded
- A human reviewer for the ground truth, who is not running the arms
- Owner time to recruit participants for Part C

## How the result is used

| Outcome | What it does to FEAT-006 |
|---|---|
| Part A pass, Part B pass, Part C pass | Evidence for the owner to raise the levels and to consider `in`. The gate needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A fail | Narrow the feature to MAS, CASE and links to official lookups, or park it. Part B then runs only on those sources. |
| Part B fail or inconclusive | Do not build the sweep. Record which kind of organisation or source failed. |
| Part C fail | The evidence is found but misread. Rework the presentation before any build. |

## Layout

- `protocol/` sample design and the committed thresholds
- `data/` the organisations, the ground truth and the stimuli for Part C
- `harness/` scoring scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Employer identity resolution (see [E11](../E11-employer-identity-check/README.md)), review of a single posting (see [E12](../E12-single-posting-review/README.md)), employee-experience and opinion sources (FEAT-008), job-board crawling, and scam or legitimacy verdicts.

## Decisions for the owner before the run

1. Confirm or change the sample size, strata and thresholds.
2. Confirm which sources are in scope for the retry, and that terms of use are checked before fetching.
3. Decide who picks the organisations and who verifies the ground truth.
4. Choose models and whether paid use is allowed.
5. Decide who recruits Part C participants, and whether they overlap with E11.

## Deviations

None yet.

## Limitations

- 30 organisations and 6 to 8 participants support direction, not statistics.
- Clean controls are not proven clean. They are not found on readable lists or in news.
- Ground truth comes from official records that cover only the readable sources, so recall is measured against what those sources show.
- Model and agent output is non-deterministic.
- Prepared stimuli in Part C test comprehension, not behaviour in a real search.
