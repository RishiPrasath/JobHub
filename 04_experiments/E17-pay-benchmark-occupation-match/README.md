# E17: pay benchmark and occupation match

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-009, ASM-009

## Question

Can JobHub suggest a short list of occupations from a posting so that the right one (or a correct "no match") is in the list, can job seekers pick the right one, and do they read the resulting pay range as a stated-basis benchmark and not as a verdict on the pay or on their worth?

FEAT-009 is not treated as feasible until this experiment has run. Earlier evidence is [E10 X3](../E10-market-value-and-red-flag-experiments/FINDINGS.md) (FND-E10X3-01, T3, pre-registered, **inconclusive**): 46 of 60 postings (77%) got a real occupation by majority of three matchers against an 80% bar, and 42 of 60 (70%) were also judged good fits against a 70% bar. Promotional titles, generic sales and marketing titles and warehouse supervisor failed to match. X3 concluded that the user must confirm the occupation, or the tool must say "no benchmark". The research behind the method is [R08](../../01_research/rounds/R08-market-value-and-salary-benchmarking/round-synthesis.md) (FND-R08-01, FND-R08-02). E17 does not edit E10. It is a new experiment.

## Approach (owner decision 2026-11-10)

**The matcher suggests the top three occupations plus "none of these", and the user confirms.** The matcher does not pick one automatically. The experiment tests whether that shortlist is good enough and whether users can use it.

## Hypotheses

- **H1 (shortlist quality):** the right occupation, or a correct "no match", is in the matcher's top three for most postings, including the kinds X3 failed on.
- **H2 (user confirmation):** job seekers pick the right occupation or "none of these" from a three-item list (ASM-009).
- **H3 (basis):** people restate the basis of the range correctly and do not treat it as a verdict.

## Part A: shortlist quality

Runnable by the agent team. Needs no participants.

### Sample

100 postings, collected **by hand** (copy and paste; no crawling or logins) from at least 15 different job families and at least three boards. Include deliberately:

| Stratum | Minimum | Purpose |
|---|---|---|
| Postings in families X3 covered (accountant, software engineer, nurse, supervisor, marketing, customer service, engineer, cook, HR, admin, sales, analyst) | 40 | Comparison with X3 |
| Families X3 did not cover (trades, drivers, retail, education, hospitality, healthcare support, finance operations, creative, others) | 30 | Breadth |
| Promotional-style titles, generic "sales and marketing" titles, roles with no matching table occupation (for example warehouse supervisor) | 20 | The X3 failure types |
| Postings that show no pay | 10 | Benchmark can still be shown without the comparison |

### Gold labels

- Written **before** any run by two humans independently, one of whom is a compensation or HR professional if one can be found. If not, that is recorded as a limitation.
- For each posting: the correct occupation in the official table, or "no match", with a reason. Disagreements between the two are resolved and recorded.
- Labels are committed before results, so the order is visible in git.

### Method

1. Owner collects the postings; the labellers write gold labels; both are committed.
2. Owner confirms the thresholds, and they are committed before any run.
3. Run the matcher, which returns the top three occupations from the current MOM table (the table in `data/mom/` from E10, or a newer release if one is available; record the reference month). Record the model, prompt and version.
4. Run every posting twice, for stability, with at least two models.
5. Score against the gold labels. A prompt or table change means a new dated run folder, never an edit.

### Measures

- **Top-3 recall:** the gold occupation, or a correct "no match", is in the top three
- **Top-1 accuracy** (reported, not a pass condition)
- **Confident wrong match** on postings whose gold label is "no match" (the matcher returned a confident occupation anyway)
- **Seniority errors:** a more senior or junior occupation chosen (X3 mapped supervisors to managers)
- **Stability** across the two runs
- Results by job family and by board

### Proposed thresholds (Part A)

Set before running.

- **Pass:**
  - gold occupation or a correct "no match" in the top three for at least 90% of postings
  - at least 85% of true "no match" postings are not given a confident wrong match
  - at least 85% of postings give the same top-three set across both runs
- **Fail:** top-three recall under 70%, or fewer than 60% of true "no match" postings handled correctly.
- **Inconclusive:** anything between.

## Part B: can users confirm

Needs 6 to 8 job seekers, recruited by the owner. A concierge test: the researcher prepares each screen from the Part A output.

### Design

Each participant sees 8 postings drawn from Part A (including 2 whose gold label is "no match"). For each, they see the matcher's top three occupations with a short description of the duties of each, plus "none of these", and pick. They are not told which postings have no match.

### Measures

- Agreement with the gold label (including choosing "none of these" correctly)
- Confident wrong picks, including picking a more senior or junior occupation
- Time per posting
- Whether wrong picks follow a wrong shortlist (a Part A failure) or a user error
- What the participant says they would do if none looks right

### Proposed thresholds (Part B)

- **Pass:** users pick the gold occupation, or "none of these" when it is correct, at least 80% of the time.
- **Fail:** under 60%.
- **Inconclusive:** anything between.

## Part C: reading the basis

Needs the same 6 to 8 participants.

### Design

After confirming an occupation, the participant sees the pay range with its basis (the official table's reference month, full-time residents, excluding bonuses, all industries), where the advertised pay sits against it, and that advertised, offered and paid pay are different. Postings include one below the range because the role is junior. Participants say what the range tells them and does not, and what they would do next.

### Measures

- Whether the participant restates the basis correctly (reference month, who it covers, what it leaves out)
- Whether a below-range posting is read as "underpaid" or "paid less than typical, possibly because the role is junior"
- Whether the range is treated as what they are worth
- Whether the participant would use it in a negotiation, and how

### Proposed thresholds (Part C)

- **Pass:** at least 75% restate the basis correctly and do not treat the range as a verdict on pay or on their worth.
- **Fail:** fewer than 50%, or any version of the output shown without a stated basis.
- **Inconclusive:** anything between.

Participants consent to notes. They are shown only prepared postings, so no personal data beyond the findings file is stored.

## Prerequisites

- The MOM occupational wage table (the E10 copy or a newer release)
- The E10 matcher prompts as a starting point
- Model access for at least two models, with cost recorded
- Two labellers, ideally one with compensation or HR knowledge
- Owner time to collect postings and recruit participants

## How the result is used

| Outcome | What it does to FEAT-009 |
|---|---|
| Part A, B and C pass | Evidence for the owner to raise the levels and to consider `in`. The gate needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A fails | The shortlist is not good enough. Record which families failed and decide whether to narrow to the families that work, change the table or park. |
| Part A passes, Part B fails | The shortlist is sound but users cannot confirm. Rework the choice screen or require a search over the list. |
| Part C fails | Users misread the range. Rework the presentation before any build. |

## Layout

- `protocol/` sample design and the committed thresholds
- `data/` the postings, the table version and frozen gold labels
- `harness/` scoring scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Personal market value or "what you are worth", salary negotiation advice, offer comparison, other benchmark sources (private salary guides, review-site pay), and employer identity (see [E11](../E11-employer-identity-check/README.md)).

## Decisions for the owner before the run

1. Confirm or change the sample, strata and thresholds.
2. Confirm postings are collected by hand only.
3. Decide who labels the occupations and whether a compensation or HR professional is available.
4. Choose models and whether paid use is allowed.
5. Decide who recruits the participants, and whether they overlap with other experiments.

## Deviations

None yet.

## Limitations

- 100 postings and 6 to 8 participants support direction, not statistics.
- The postings are chosen by hand and are not a random sample of the market.
- The MOM table covers full-time residents, excludes bonuses and is about a year old on release.
- Model output is non-deterministic.
- If the same model family labels and matches, agreement is not independent. Use humans for labels.
- Prepared screens test comprehension, not behaviour in a real negotiation.
