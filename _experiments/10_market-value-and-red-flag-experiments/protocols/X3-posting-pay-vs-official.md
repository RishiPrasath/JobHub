# X3: posting pay versus the official wage table

**Question.** Can a job posting be matched reliably to an occupation in MOM's wage table, and where does its advertised pay sit against the official range?

**Why.** The research round found MOM's table is the best official anchor, but it is keyed on occupation, so everything depends on the matching step. It excludes bonuses, covers full-time residents only, and is about a year old (reference month June 2025, released June 2026).

## Data (frozen now)
- **Official table:** `data/mom/occupations_all_industries.csv`, 523 occupations from MOM Table 4 (all industries, SSOC 2024): basic and gross wage at the 25th percentile, median and 75th percentile.
- **Postings:** 60 current MyCareersFuture postings that show a monthly salary range, 5 for each of 12 fixed search terms: `accountant`, `software engineer`, `staff nurse`, `warehouse supervisor`, `marketing executive`, `customer service officer`, `mechanical engineer`, `cook`, `human resource executive`, `administrative assistant`, `sales executive`, `data analyst`. Collection rule: search results sorted by newest, take the first 5 postings per term, scanning pages 0 and 1, that show a "Monthly" salary range (skip hourly, daily and unlisted). Recorded: employer, title, seniority, employment type, job function, location, salary minimum and maximum, posted date. Read through the local fetch service (the listing page, robots.txt permitting).

## Matching
Three independent matchers each get, for every posting, the title, seniority, employment type and job function (salary withheld) plus the 523-occupation list, and return the best occupation code, a confidence (high, medium, low), or "no good fit".
- **M1:** Haiku-model agent, a structured prompt.
- **M2:** default-model agent, a prompt that reasons about the likely duties first.
- **M3:** the lead researcher, labelling before seeing M1, M2 or any salary comparison.

## Measures
- **Agreement:** share of postings where at least 2 of 3 matchers give the same code (majority); share where all 3 agree; pairwise agreement; agreement at the first 3 digits of the code as a lenient measure.
- **Matchable:** a posting is matchable if a majority code exists and the lead researcher judges, from the title and function, that the code is a good fit (not just the nearest). The judgement is recorded with a reason.
- **Comparison (for matchable postings):** advertised minimum and maximum against the official gross 25th percentile, median and 75th percentile. Classify the advertised midpoint as below the 25th, between the 25th and 75th, or above the 75th. For postings outside the middle band, record plausible reasons (seniority above or below the benchmark job, the official figure excludes bonus, the posting is for a recruiter's client, and so on).
- **Range width:** top divided by bottom of each advertised range; the share wider than 2 to 1 (the limit MOM sets for Employment Pass advertisements).

## Pass/fail (set before running)
- **Pass for automatic benchmarking:** a majority code exists for at least 80% of postings, and at least 70% of all postings are matchable.
- **Fail:** below 60% matchable. The finding would then be that a benchmark must be shown only after the user confirms the occupation.
- Between those, inconclusive and reported with the reasons.
- The comparison with official pay is descriptive. No pass/fail, and no claim that any advertised pay is right or wrong.

## Limits stated in advance
Sample of convenience (newest postings that show pay); about 60 items; one table (all industries), so industry effects are not controlled; advertised monthly range, not paid wage; the official figure is June 2025 and excludes bonuses.
