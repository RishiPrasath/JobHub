# E16: employee-experience sources

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-008, ASM-008

## Question

Is there at least one source of first-hand employee and candidate accounts that JobHub may lawfully use for its intended purpose, that covers enough Singapore employers, and can a summary built from it be understood as individual accounts and not as a verdict on the whole company?

FEAT-008 is not treated as feasible until this experiment has run. Earlier evidence is [E09](../E09-openserp-company-research/REPORT.md) and its [agent test](../E09-openserp-company-research/AGENT-TEST.md) (FND-E09-01, FND-E09-02): Glassdoor could not be read in any attempt (21 of 21 in the scripted run, 8 of 8 and 9 of 9 in the agent runs), Reddit returned a bot challenge reported as a success, and Indeed and JobStreet read fine but their terms restrict automated access and the production flow deliberately does not read them. Culture, pay and interview answers were low confidence (culture low in 6 of 8, pay low in 7 of 8, interview low in all). The problem is the source, not the search or the model. The feature's front matter records `result: fail`, and its scope stays unchanged while this survey runs (owner decision 2026-11-10).

## Hypotheses

- **H1 (permitted source):** at least one lived-experience source exists whose terms allow JobHub's intended use.
- **H2 (coverage):** that source has enough first-hand accounts, recent enough, for a useful share of Singapore employers.
- **H3 (reading):** people read a hedged summary from that source as individual accounts, not as the whole company.

## Part A: permitted-source survey

Runnable by the agent team. Needs no participants. No scraping of any site whose terms forbid it.

### Candidate sources

Listed before fetching, and extended during the survey:

| Type | Examples to check |
|---|---|
| Licensed or partner data | Review-site data licences or partner programmes, if any exist for this use |
| Sources whose terms allow the intended use | Public forums or sites with an API or terms that allow reuse |
| Official sources | TAFEP and MOM material, regulator enforcement lists (see [E14](../E14-official-red-flag-evidence/README.md)) |
| Job-seeker contributions | Accounts supplied by JobHub users (cold-start risk noted) |
| Link-out only | Pointing the user to a review site without reading or copying it |

### Method

1. For each source, record the terms of use, any API or licence route, robots rules, cost and what is permitted (read, summarise, quote, store, show) **before** any fetch.
2. Classify each source: permitted for the intended use, permitted for link-out only, or not permitted. Record why.
3. For permitted sources, record the access method, rate limits and cost.
4. Write results to a dated run folder.

### Proposed thresholds (Part A)

Set before running.

- **Pass:** at least one source is permitted for the intended use (read and summarise with attribution).
- **Fail:** none is. The feature narrows to link-out cards or is parked, and the owner decides.

## Part B: coverage

Runs only on sources Part A classed as permitted. Runnable by the agent team.

### Sample

20 Singapore employers, chosen before any run: 6 large, 6 mid-size, 5 small, 3 agencies. Several are the same employers used in E11 and E14 so the work is comparable.

### Measures

- Number of first-hand accounts per employer from the last 24 months (counted, not read for content)
- Share of employers with at least 5 accounts
- Spread across topics (culture, management, workload, pay, interview) where the source allows it
- Share of accounts that name individuals, to size the privacy risk
- Cost and time per employer

### Proposed thresholds (Part B)

- **Pass:** at least 5 first-hand accounts from the last 24 months for at least half of the 20 employers.
- **Fail:** fewer than 25% of employers reach 5 accounts.
- **Inconclusive:** anything between.
- Results are reported by employer size, since coverage is expected to fall for small employers and agencies.

## Part C: reading test (conditional)

Runs only if Part A and Part B pass. Needs 6 to 8 job seekers, recruited by the owner. These can be the same people as [E14](../E14-official-red-flag-evidence/README.md) Part C or [E15](../E15-harmful-signals-fixture-test/README.md) Part B if the sessions are kept separate.

### Design

Each participant reads a hedged summary built from the permitted source for two employers, next to the raw links. The summary states the number of accounts, their dates, what they have in common, what they disagree on, and what the sources cannot show. Participants say what the summary tells them about the employer and what it does not, and what they would do next.

### Measures

- Whether the summary is described as individual accounts and not as "what the company is like"
- Whether the participant states a limit (few accounts, self-selected, dates)
- Whether they say they would use it, and whether it changes a next step
- Whether it changes a decision more than the raw links alone

### Proposed thresholds (Part C)

- **Pass:** at least 75% say the summary reflects individual accounts and not the whole company, and at least half would use it.
- **Fail:** fewer than 50% understand its limits.
- **Inconclusive:** anything between.

Participants consent to notes. They are shown only prepared summaries, so no personal data beyond the findings file is stored. Summaries do not reproduce review text beyond what the source's terms allow.

## Prerequisites

- Time to read terms of use and licence pages, and to ask a provider about access where a licence route exists
- Model access if summaries are generated, with cost recorded
- The employer list, ideally shared with E11 and E14
- Owner time to recruit participants for Part C

## How the result is used

| Outcome | What it does to FEAT-008 |
|---|---|
| Part A, B and C pass | Evidence for the owner to raise the levels and to consider `in`. The gate needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A fails | No permitted source. Narrow to link-out cards or park. |
| Part A passes, Part B fails | A permitted source exists but is too thin. Park, or add job-seeker contributions as a later question. |
| Part C fails | The data is there but misread. Rework the presentation, or keep to link-out. |

## Layout

- `protocol/` source list, sample design and the committed thresholds
- `data/` the source classification, the employer list and coverage counts
- `harness/` counting scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Official and regulator records (see [E14](../E14-official-red-flag-evidence/README.md)), employer identity (see [E11](../E11-employer-identity-check/README.md)), pay benchmarks (FEAT-009), summarising reviews from sources whose terms forbid it, scoring or ranking employers, and any claim that an employer is good or bad.

## Decisions for the owner before the run

1. Confirm or change the sample, the sources to check and the thresholds.
2. Confirm that no site whose terms forbid automated use will be fetched.
3. Decide who contacts providers about licences, if any exist.
4. Choose models and whether paid use is allowed.
5. Decide who recruits Part C participants, and whether they overlap with E14 or E15.

## Deviations

None yet.

## Limitations

- 20 employers and 6 to 8 participants support direction, not statistics.
- Counting accounts does not check whether they are true or typical. Reviews are self-selected.
- Terms of use change; the classification reflects the terms as read at the run date. It is not legal advice.
- Coverage is counted for the employers chosen, not a random sample of the market.
- Part C uses prepared summaries and tests comprehension, not behaviour in a real search.
