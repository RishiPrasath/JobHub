# E15 findings: harmful signals fixture test

Run: `runs/2026-11-10-run-001/`, 2026-11-10. Affects FEAT-007 and ASM-007. Written by the coordinator from the specialist's report, because the specialist could not save report files. Nothing is committed to git.

**Headline:** the deterministic Singapore rule pack caught all 10 clearly concerning cases, but it misses three pass criteria: citation, abstention and legal wording. The AI-assisted method ran only on part of the sample. All methods are **inconclusive**. No fail condition was triggered. Part B was not run with participants, and the simulated pilot did not run because the daily Groq limit was reached.

## Threshold table (Part A)

Thresholds are in `protocol/thresholds.md`, copied verbatim from the README. "Not met" is not a fail. Partial runs use the cases that ran as the denominator.

| Threshold | Deterministic (40 cases) | gpt-oss-20b run 1 (32 of 40) | gpt-oss-20b run 2 (12 of 40) | qwen3.8-27b run 1 (about 20 of 40) |
|---|---|---|---|---|
| Recall of at least 80% on clearly concerning | 10/10 (inflated, see limitations) | 7/7 run; C01, C03, C10 not run | 2/2 | 3/3 |
| False alarms of 10% or less on benign-similar | 0/10, met | 1/7 = 14.3% (B04), not met | 0/3 | 0/5 |
| No legal conclusion | One pack sentence, "discriminatory advertisements breach the Guidelines", appears on nationality flags. Implied, not stated as fact. Not met | 11 hedged hits ("could be discriminatory", "may be unlawful"). Not met | 4 hedged hits | 0 hits, met on cases run |
| 100% of flags carry excerpt and named source | 22/28 = 78.6%, not met. All 6 misses come from four entries with no TAFEP/MOM source | 19/21 = 90.5%, excerpts 21/21 verbatim, not met | 6/7 | 10/11 |
| "No reliable signal" correct on at least 90% of no-signal cases | 17/20 = 85%, not met (false alarms on J02, E1, E5) | 11/15 = 73.3%, not met | 5/6 | 10/10 |
| At least 80% of questions pass the rubric | 28/28, met | 19/21 = 90.5%, met | 6/7 | 11/11 |
| No protected-characteristic inference; no hidden instruction followed | None found; C10 and E6 not followed | None found; injection cases C10 and E6 not run, so untested | not run | not run |
| Stability across two runs | not applicable | 12/12 shared cases gave the same decision and entries, but only 12 overlap | | |

Overall Part A verdict: deterministic **inconclusive**; gpt-oss-20b **inconclusive, partial**; qwen3.8-27b **inconclusive, small sample**; Part B **not run with participants**, so inconclusive.

## Results by group

**Deterministic:**
- Concerning cases: 10/10 matched.
- Benign cases: 0/10 false alarms. B04 ("youth aged 13 to 18") escaped only because the pack suppresses "youth work" nearby.
- Job-related cases: 1/6 false alarm (J02 "women only", where the reason is stated).
- Edge cases: 2/4 false alarms. E1 quotes examples of wording to avoid. E5 "Pay $2000" matched a fee pattern, a pack bug.
- Missed: E2, the Chinese-language case, because the pack has English patterns only.
- Ambiguous cases: 2/8 flagged (A06, A07), both with hedged template text.
- Some excerpts were truncated by the patterns, for example "Earn up to $6".

**gpt-oss-20b run 1:** missed the deposit signal in C06; flagged 6 of 8 ambiguous cases, all with a "not established" sentence; false alarms on B04, J02, J04 and E5; explanations repeatedly used "could be discriminatory" or "may be unlawful".

**qwen3.8-27b:** no false alarms, no legal wording, all questions neutral. The sample is too small and different from the gpt-oss subset to compare.

**Questions:** rated against `protocol/question_rubric.md` (ratings in `outputs/scores/ratings.json`). Three gpt-oss questions failed tone, for example "why younger applicants are preferred".

**Source coverage:** the TAFEP pages (tripartite guidelines, writing job advertisements) and four MOM pages (Fair Consideration Framework, salary deductions, agency fee FAQ, key employment terms) loaded on 2026-11-10. Four entries have no named source because no page covered them: P3-DOCS, P4-UNPAID, P5-RAPID and P5-DEMANDS. TAFEP's wording table lists "Only Singaporeans" as acceptable, against its own general nationality rule; the pack has no pattern for it, and case A01 tests it.

## Part B

Not run with participants. The 6-persona simulated pilot was not run because the daily Groq limit was reached. `harness/pilot.py` is ready. No Part B number exists, and a persona pilot could not satisfy Part B in any case.

## Deviations

1. No git commits. Order of events is shown by `protocol/FROZEN.md` (hashes, 09:58 UTC) and file times.
2. All 40 cases are synthetic; no hand-collected postings were available and no crawling was done. The README asked for at least 10 real ones, so the sample is not representative. Group sizes are 10/10/8/6/6, with two hidden-instruction cases (C10, E6).
3. Gold labels and the pack were written by an AI, not an HR or employment-law reviewer.
4. The run was interrupted and restarted: the first attempt (one posting per call) was aborted and moved to `outputs/aborted_single_call_attempt/`; the harness was changed to batch four postings per call (C10 and E6 alone); qwen was restarted with `--max-tokens 1200`. None was tuned to scored results.
5. The daily Groq limit was reached. gpt-oss-20b run 1 covers 32 of 40 cases (not run: B02, B05, B07, C01, C03, C10, E1, E6); run 2 covers 12 and qwen about 20. No further calls were made and gpt-oss-120b was not used. Full recall, injection resistance, full-group false alarms and stability are inconclusive.
6. A post hoc pack v0.2 was prepared but not run (`data/pack_v0.2_posthoc.json`: removes the "breach" sentence, fixes the `pay $` and truncation patterns). It plays no part in any verdict.
7. The shared rate-limit lock raised a PermissionError once on Windows; the run was restarted using the cache.
8. WebFetch returns model-written summaries, so pack wording may be incomplete.

## Run record

- Date: 2026-11-10. Frozen files were re-hashed after the runs and still match `protocol/FROZEN.md` (pack, cases, gold, thresholds, rubric).
- Models and settings: `openai/gpt-oss-20b` (runs 1 and 2) and `qwen/qwen3.8-27b` (run 1), temperature 0.2, JSON mode, `reasoning_effort="low"` on gpt-oss, four postings per call (C10 and E6 alone). `max_tokens` was 1800 for gpt-oss and 1200 for qwen batches 0 to 4. A retry of qwen batches 5 to 11 at 1000 hit the daily limit before any call succeeded. The first qwen attempt at 1200 failed on batch 5 with a per-minute output-token limit error (`results_qwen27b-run1.first-pass.json` is kept).
- Groq tokens used: about 35,000 in total (gpt-oss-20b scored runs 16,000, qwen scored run 7,200, two format probes 1,900, the aborted one-posting-per-call attempt 10,200). Well inside the 300,000 budget; the limit that stopped the work was the shared daily cap, not this experiment's budget.
- Daily limit: gpt-oss-20b, gpt-oss-120b and qwen3.8-27b all returned the daily token limit error. No further calls were made. The persona pilot was not run.
- Tool issue to report (not edited): `tools/llm_client.py` can raise `PermissionError` on its Windows lock file when several processes share it, which ended the first gpt-oss run after batch 6; `harness/runloop.sh` retries from the cache.

## Limitations

40 synthetic cases and partial runs support direction only. Author overlap inflates deterministic recall: the pack and the cases both draw on the TAFEP wording lists. An AI wrote the gold labels and rated the questions and legal wording. The pack is English only. Model output is non-deterministic and the stability result rests on 12 cases. Batching four postings per call could let one posting influence another (injection cases were isolated).

## Feasibility recommendation for FEAT-007

**Inconclusive.** At fixture level the deterministic pack finds clear wording and is quiet on most benign wording, but it does not meet the citation, abstention and legal-wording criteria, and AI-assisted retrieval is untested in full. Narrowing to categories 1 and 2 (wording with TAFEP sources) is plausible once the pack text and patterns are fixed. Categories 3 to 5 have weak or no named source and are **not supported** until sources are found.

Proposed level: T2 at most, only for the deterministic method on categories 1 and 2. No need-level change. ASM-007 (flagging without false accusations) is not shown. The only legal-sounding text in the deterministic output was in the pack's own wording, so the risk is in how entries are written.

## Needs real participants or a human

Part B (6 to 8 job seekers reading prepared flags); an HR or employment-law reviewer for the pack and gold labels; real postings to measure false-alarm rates.

## Next actions and owner decisions

1. When the Groq limit resets, run the missing cases and the full second run and qwen run, then score. The cache avoids repeat spend.
2. Run `harness/pilot.py` (6 personas), labelled simulated.
3. Score pack v0.2 against the same frozen gold as a labelled post hoc `run-002`.
4. Find sources for unpaid trials, document retention and progression claims, or drop those categories.
5. Add Chinese, Malay and Tamil patterns if translated postings are in scope.
6. Decide whether to rewrite the pack wording to remove legal-sounding language, whether entries with no named source may display at all, and whether to spend the next day's Groq budget on completing the AI runs or on the pilot first.
