# E17 run design (2026-11-10, run-001)

Written before the first model call. Plan: [README.md](../README.md). Run brief: `agents/prompts/03_experiment-run-brief.md`.

## Sample (data/postings.json)

100 postings. No crawling, no logins, no fetching.

| Stratum | N | Source |
|---|---|---|
| `x3_reuse` | 60 | The 60 postings from [E10 X3](../../E10-market-value-and-red-flag-experiments/outputs/x3/postings_ids.json), read only. Title, seniority, employment type and function kept. **Salary, employer, location and search term are not passed to any labeller or matcher.** |
| `new_family` | 30 | Synthetic (`synthetic: true`): trades, drivers, retail, education, hospitality, healthcare support, finance operations, creative, security, cleaning, fitness, social work. Modelled on real Singapore posting titles, with plausible seniority, type and function tags. |
| `failure_type` | 10 | Synthetic: promotional titles (3), generic sales and marketing titles (3), and supervisor-type roles where the table has no clear entry or a trap (4). |

Of the 60 X3 postings, many are themselves X3 failure types (9 promotional, 5 warehouse supervisor, 3 generic sales). The planned strata (40 X3-family, 30 new families, 20 failure types, 10 postings with no pay) are only partly met; see Deviations in FINDINGS.md.

## Gold labels

- Labeller A: the specialist (an AI), `data/labels_A.json`. Written after the sample was fixed and without any matcher output. The labeller saw the 523-entry list.
- Labeller B: a fresh sub-agent given only the blind posting file (title, seniority, type, function) and the occupation list. No access to A's labels, X3's matcher outputs or X3's judgement. `data/labels_B.json`. The B labels were on disk before A's labels were written.
- Reconciliation: `harness/make_gold.py` (rule and every case recorded in `data/label_disagreements.json`). Output `data/gold.json`: primary code, accepted set (which may include NONE), `true_no_match` (both said NONE), `too_senior` and `too_junior` neighbour lists (written by A).
- X3's "good fit" judgement is not used anywhere.

## Matcher

1. **Shortlist** (`harness/shortlist.py`): 25 candidates from the 523 occupations by TF-IDF over occupation titles (word 1-2-grams and character 3-5-grams, plus a small function term). The MOM table has titles only, so there are no descriptors to index.
2. **LLM choice** (`harness/run_matcher.py`): the model sees title, seniority, type, function and the 25 candidates in code order and returns three ranked codes, a verdict (match or none), a confidence and a short reason.
3. **Models:** `qwen/qwen3.8-27b` (primary, two runs, temperature 0.3) and `openai/gpt-oss-20b` (second, one run, temperature 0.3, reasoning effort low).
4. **Table:** MOM Occupational Wages Table 4, all industries, SSOC 2024, reference month June 2025 (the E10 copy `data/mom/occupations_all_industries.csv`).

## Scoring

`harness/score.py`, definitions in `protocol/thresholds.md`.

## Part B and C (simulated pilot only)

`harness/persona_pilot.py`: six simulated job-seeker personas. Part B: 8 postings fixed in advance (6 with a gold code, 2 true no-match). Part C: 3 pay-range screens with the basis statement (one within the range, one below the range for a junior role, one above). Simulated; not participants.
