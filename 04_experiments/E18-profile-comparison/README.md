# E18: profile and preference comparison

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-010, ASM-010

## Question

Can a candidate profile (FEAT-016) and job preferences (FEAT-017) be compared with a posting without unsupported inferences, wrong hard facts, role mixing, or any fit score, and can the user correct and trust the result?

FEAT-010 is not treated as feasible until this experiment has run. Earlier evidence is the profile-comparison run in [E01-07](../E01-07-sequential-sdk-run/findings.md) (FND-E03-01, T1, narrative only, **fail**). On three postings and one synthetic profile, with explicit prohibitions in the prompt, the model merged three roles into one, treated Excel experience as administrative experience, stated all three roles were full-time when one was part-time, imported a Class 4 requirement into another role, omitted known location and employment-type facts, and found no matches for a logistics role the profile supported. That run saved no outputs for a rerun.

Per [decision 0001](../../06_scope/decisions/0001-profile-comparison-after-profile.md), FEAT-010 follows the candidate profile and the preferences setup. It is not part of the first slice, and its scope stays `candidate`.

## Hypotheses

- **H1 (hard facts):** employment type, work arrangement, location, pay against the stated minimum and notice period can be compared correctly when the profile is structured and the posting facts are extracted with excerpts.
- **H2 (experience and skills):** a comparison that only proposes quoted profile evidence for the user to confirm avoids the unsupported inferences that E03 produced (ASM-010).
- **H3 (eligibility):** right-to-work wording in a posting is flagged without false "not eligible" claims.
- **H4 (use):** with real profiles, users agree with the facts, correct wrong items, and do not read the result as a fit verdict.

## What is compared (owner decision 2026-11-10)

1. **Hard facts:** employment type, work arrangement, location, pay against the stated minimum, notice period.
2. **Experience and skills against requirements:** does the profile support a stated requirement? The user confirms.
3. **Right-to-work flags:** postings that need a different status, using the right-to-work field in FEAT-016 (informational; the flag does not decide anything).

No fit score, ranking, hiring probability or "good match" label, in any method.

## Methods compared

1. **Free-text model comparison**, as in E03: the profile and the posting go to a model that returns the comparison. This is the baseline.
2. **Structured comparison:** the model extracts posting facts with excerpts and stable IDs; the profile and preference fields are compared with those facts by code. The model does not compare.
3. **Hybrid:** structured comparison for hard facts and right to work, and for experience and skills the model proposes quoted profile evidence for each requirement. The user accepts, edits or rejects each item. Nothing is stated as a match until the user confirms.

## Part A: fixture test

Runnable by the agent team. Needs no participants. Runs now, on synthetic profiles.

### Sample

24 postings, collected **by hand** (copy and paste; no crawling or logins), at least 6 job families, at least 3 boards. 3 synthetic candidate profiles, written in the FEAT-016 and FEAT-017 formats by a human: one close to a logistics background, one administrative, one early-career with adjacent skills. 72 comparisons.

Postings include the E03 failure types:

| Case type | Count | Purpose |
|---|---|---|
| Employment type or arrangement mismatch (for example part-time posting, full-time seeker) | 4 | Hard-fact errors |
| Adjacent-skill traps (Excel is not admin experience) | 4 | Unsupported inference |
| Hard requirement the profile lacks (a licence, a certification) | 4 | Mismatch correctly stated |
| Posting silent on a field the profile or preferences ask about | 4 | Unknown shown as unknown |
| Preferred versus required wording | 2 | Requirement type |
| Right-to-work wording ("Singaporeans only", "Employment Pass holders", none) | 3 | Eligibility flags |
| Role mixing and contamination: three postings run together in one request, and one posting with another role's requirements in an instruction fixture | 3 | Cross-role contamination |

### Gold labels

- Written **before** any run by a human, not the model being tested: for each posting and profile, the correct status per field (match, mismatch, unknown, needs user confirmation), the supporting profile field and posting excerpt, and the correct right-to-work flag.
- Labels are committed before results, so the order is visible in git.

### Method

1. Owner collects the postings; the profiles and gold labels are written and committed.
2. Owner confirms the thresholds, and they are committed before any run.
3. Run all three methods on all 72 comparisons, twice, with at least two models. Record model, prompt and harness version.
4. Run each posting separately, and again in the batch condition, to test contamination.
5. Score against gold labels. A prompt or harness change means a new dated run folder, never an edit.
6. Write `FINDINGS.md`, add a finding to [findings.md](../../02_analysis/findings.md), and update FEAT-010.

### Measures

- **Unsupported inferences:** a match, mismatch or requirement not supported by a profile field and a posting excerpt
- **Hard-fact errors:** a wrong value for employment type, arrangement, location, pay or notice period
- **Omitted known facts:** facts available in the profile and posting but not compared
- **Unknown handling:** posting silent on a field shown as unknown, not as a mismatch
- **Cross-role contamination:** any requirement, qualification or fact from one role appearing in another's comparison
- **Right-to-work flags:** correct flag, and any false "not eligible" or false "eligible"
- **Forbidden outputs:** any fit score, ranking, hiring probability or "good match" label
- **Injection resistance:** any hidden instruction in a posting that is followed
- **Stability** across two runs; time and cost per comparison
- Results by case type and by method

### Proposed thresholds (Part A)

Set before running. Applied to each method that would be built, reported separately.

- **Pass:**
  - unsupported inferences of 2% or less
  - hard-fact errors of 1% or less
  - known facts omitted on no more than 10% of comparisons
  - unknown shown as unknown on at least 90% of cases where the posting is silent
  - zero cross-role contamination across the batch condition
  - no fit score, ranking or hiring probability on any output
  - zero false "not eligible" claims
  - no hidden instruction followed
- **Fail:** unsupported inferences over 10%, or hard-fact errors over 5%, or any fit score output.
- **Inconclusive:** anything between.

## Part B: do people use it (after a real profile exists)

**Does not run yet.** Per decision 0001, it waits until a real FEAT-016 profile and FEAT-017 preferences setup can be created. Needs 6 to 8 job seekers, recruited by the owner. A concierge test: the researcher assembles the comparison from the best Part A method.

### Design

Each participant builds their own profile and preferences in the FEAT-016 and FEAT-017 formats, then sees the comparison against three postings of their own choosing. For each item they accept, edit or reject, and say what they would do next.

### Measures

- Agreement with the facts, and corrections made
- Whether wrong items are caught (a wrong item is planted in one comparison)
- Whether the result is read as a verdict on their chances, despite having no score
- Whether the right-to-work flag is understood as informational
- Whether it changes which posting they would pursue

### Proposed thresholds (Part B)

- **Pass:** at least 75% of planted wrong items are caught, at least 75% do not read the result as a verdict, and most say they would use it again.
- **Fail:** fewer than 50% of planted errors caught, or most read it as a fit verdict.
- **Inconclusive:** anything between.

Participants consent to notes. Their profile is used only for the session and not stored beyond the findings file.

## Prerequisites

- FEAT-016 and FEAT-017 field definitions (done); a working profile step for Part B
- The E08 claim-review harness and E12 extraction approach, where useful
- Model access for at least two models, with cost recorded
- A human to write profiles and gold labels who is not running the model
- Owner time to collect postings and, for Part B, recruit participants

## How the result is used

| Outcome | What it does to FEAT-010 |
|---|---|
| Part A and Part B pass | Evidence for the owner to raise the levels and to consider `in`. The gate needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A passes for hard facts but fails for experience matching | Narrow the feature to hard facts and right-to-work flags. Keep experience matching out. |
| Part A fails on all methods | Do not build. Record which case types failed and decide whether to park. |
| Part B fails | The comparison is accurate but misread or not valued. Rework presentation or park. |

## Layout

- `protocol/` sample design and the committed thresholds
- `data/` the postings, synthetic profiles and frozen gold labels
- `harness/` scoring scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Fit scores, ranking, hiring probability, resume changes (FEAT-011), application actions, employer verification, and any inference about protected characteristics.

## Decisions for the owner before the run

1. Confirm or change the sample, case types and thresholds.
2. Confirm postings are collected by hand only.
3. Decide who writes the synthetic profiles and gold labels.
4. Choose models and whether paid use is allowed.
5. Decide when Part B runs and who recruits the participants.

## Deviations

None yet.

## Limitations

- 24 postings, 3 profiles and 6 to 8 participants support direction, not statistics.
- Synthetic profiles are cleaner than real ones.
- Postings are chosen by hand and are not a random sample of the market.
- Model output is non-deterministic.
- If the same model family writes labels and produces comparisons, agreement is not independent. Use a human for labels.
- A concierge comparison is not a rendered interface.
