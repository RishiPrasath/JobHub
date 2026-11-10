# E11: employer identity check on real postings

Status: planned (thresholds below are proposed and not yet pre-registered; the owner confirms them before any run)
Affects: FEAT-001, ASM-001

## Question

Does the employer identity check work on realistic job postings, not hand-picked brands, and does it change what a job seeker does next?

[E10 X2](../E10-market-value-and-red-flag-experiments/protocols/X2-brand-to-legal-entity.md) resolved 9 of 12 brands, but ground truth could be set for only 12 of 36 brands, the brands were chosen from well-known names, and no user saw the result. [P05](../../05_prototypes/P05-company-research-flow/README.md) passed its 14 cases, but they were the builder's own and a fix followed one failure. This experiment closes those gaps.

## Hypotheses

- **H1 (works):** on a sample of real postings, the registry plus web step names the correct registered employer when it can be known, refuses safely when it cannot, and does not accept a wrong or lookalike company.
- **H2 (useful):** seeing the result changes or confirms a concrete next step for real job seekers (ASM-001).

## Part A: technical feasibility

Runnable by the agent team. Needs no participants.

### Sample

60 postings, collected **by hand** by the owner (copy and paste, no crawling or logins; job-board crawling is still awaiting owner confirmation in [SCOPE.md](../../06_scope/SCOPE.md)).

| Stratum | Count | What the right answer is |
|---|---|---|
| Large or well-known employers | 15 | The registered operating entity |
| Small and mid-size employers (SMEs, small chains, startups) | 20 | The registered operating entity, if findable |
| Agency or anonymous postings (employer hidden) | 10 | "Employer not disclosed". Naming a company is a wrong answer. |
| Brand differs from the registered name (trading names, franchises, parent versus operating company) | 10 | The operating entity |
| Lookalike or fictitious employers (built from public scam advisories or constructed) | 5 | Not confirmed real |

Fewer than 5 small employers resolved would mean the sample did not test small employers. Report this rather than fill the gap with easier cases.

### Ground truth

- Set **before** any run, by someone who does not run the flow (the owner or a separate reviewer).
- Source: the posting's own company details, the employer's own website footer or privacy policy, and the registry record by UEN.
- Registry-mirror sites (sgpbusiness, companies.sg and similar) must not be used to set truth. E10 X2 used them for both truth and acceptance, which weakened the result.
- A posting whose truth cannot be set is **kept** and labelled "truth unknown". It is excluded from the correct-rate but counted in the refusal and wrong-accepted measures. E10 dropped such brands, which hid how common they are.

### Method

1. Owner collects the 60 postings. Ground truth is recorded and committed.
2. Owner confirms the thresholds below. They are committed before any run, so the order is visible in git.
3. Run the P05 flow unchanged. Record the commit, model and search engines. No fixes between runs; a fix means a new run folder (`runs/YYYY-MM-DD-run-001/`).
4. Run the full set twice, to measure stability.
5. Score each posting: correct, wrong accepted, correctly refused, wrongly refused, lookalike caught, real company called a lookalike.
6. Record searches, time and cost per posting.
7. Write `FINDINGS.md`, add a finding to [findings.md](../../02_analysis/findings.md), and update FEAT-001.

### Measures

- Correct top-1 (accepted entity equals ground truth by UEN)
- **Wrong accepted** (a confident answer that is not the truth). This is the dangerous error.
- Correct refusals and wrong refusals
- Lookalikes caught, and real employers falsely called lookalikes
- Stability: same headline across the two runs
- Searches, seconds and cost per posting

### Proposed thresholds

Set before running.

- **Pass:**
  - Correct on at least 70% of postings where truth is known
  - Wrong accepted on at most 2 of 60
  - At least 4 of 5 lookalike or fictitious employers not confirmed as real
  - Same headline across both runs on at least 90% of postings
  - Agency and anonymous postings: no company named on at least 9 of 10
- **Fail:** correct under 50%, or wrong accepted on 4 or more, or 2 or more lookalikes confirmed as real.
- **Inconclusive:** anything between.
- The small-employer stratum is reported separately. A weak result there does not fail the experiment, but it limits the claim to "known employers".

## Part B: does it change what people do

Needs 6 to 8 job seekers recruited by the owner. Concierge test: a person runs the check by hand, so the experiment tests value, not software.

1. Each participant brings 2 to 3 postings they are really considering.
2. Before showing anything, the observer records what the participant plans to do and how sure they are the employer is genuine.
3. The participant sees the employer identity result for each posting.
4. The observer records, before asking any questions, whether the next step changed (apply, skip, ask the recruiter, verify elsewhere) or was confirmed.
5. Short interview: what was new, what was confusing, what they did not trust, and what the refusal outputs ("could not confirm company") meant to them.

Participants consent to notes, and only the posting text they share is used. No personal data is stored beyond what the findings file needs.

### Proposed thresholds

- **Pass:** for at least half of participants, the result changes a next step or removes a stated doubt in at least one posting, and most participants understand the refusal outputs.
- **Fail:** for fewer than a quarter of participants.
- **Inconclusive:** anything between.

## Prerequisites

- The P05 Docker stack and its pinned network names (see [AGENTS.md](../../AGENTS.md)): registry service, OpenSERP, fetch service and flow.
- A model key that is not rate limited. The free tier hit limits in P05, which removes the written brief. If that recurs, record it, and score the headline and sources only.
- Owner time to collect the postings, set or review ground truth, and recruit participants for Part B.
- Estimated run time from P05: 1 to 2 minutes per posting. Two full runs of 60 postings take about 2 to 4 hours.

## How the result is used

| Outcome | What it does to FEAT-001 |
|---|---|
| Part A pass, Part B pass | Evidence for the owner to move FEAT-001 toward `in`. The gate needs N3 and a recorded owner decision. The owner sets the levels. |
| Part A pass, Part B fail | Technically sound but not valued. Reconsider the framing or the first slice. |
| Part A fail or inconclusive | Do not build. Record which stratum failed and decide between narrowing (known employers only) and `later`. |

## Layout

- `protocol/` sample design and the committed thresholds
- `data/` the 60 postings and frozen ground truth
- `harness/` scoring script
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Red flags, employee reviews, pay benchmarks, and any statement about whether an employer is safe. This experiment tests who the employer is.

## Decisions for the owner before the run

1. Confirm or change the sample size, strata and thresholds.
2. Confirm the postings are collected by hand only.
3. Choose the model for the run and whether paid use is allowed.
4. Decide who recruits the Part B participants, and when.

## Deviations

None yet.

## Limitations

- Sample size: 60 postings and 6 to 8 participants support direction, not statistics.
- The postings are chosen by hand and are not a random sample of the market.
- A single flow version, and the model step is non-deterministic.
- Ground-truth setters and flow runners are the same model family if agents set truth; use a human or a different model where possible.
