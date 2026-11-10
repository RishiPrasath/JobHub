# E18 findings: profile and preference comparison (Part A, partial run)

Run folder `runs/2026-11-10-run-001/`. Affects FEAT-010, ASM-010. Written by the coordinator from the specialist's report, because the specialist could not save report files. Scoring script `harness/score.py` (sha256 22c9357474ea39e9aff5f83a9369b377aed2d9cf274af73e3b48d7b5eb2bbde3); scores in `runs/2026-11-10-run-001/scores/` (`summary.json`, `cells.jsonl`). Part B was not run and there was no persona pilot. Nothing is committed to git.

**Summary:** free-text comparison fails. The structured method is inconclusive but promising for hard facts. The hybrid method produced no usable results, because the Groq daily token limit stopped the run.

## What ran

| Method | Model | Ran | Not run |
|---|---|---|---|
| 1 free-text | openai/gpt-oss-120b | 29 single comparisons (P1 and P2 x 15 postings; P2-S11 failed with a JSON-validation 400 and counts as a parse failure), plus 1 batch request (P1) | all of P3, batch for P2 and P3, run 2 |
| 2 structured | gpt-oss-20b extraction, comparison by code | 15 extractions, giving all 45 comparisons | batch extraction, run 2 |
| 3 hybrid | qwen/qwen3.8-27b | nothing usable | all |

No evidence call completed for the hybrid method. The 10 rows the scorer printed are postings with no experience or skill requirement and are discarded. Token use was about 45k for free-text and 15k for extraction.

## Thresholds against observed values

"Inconclusive" means the method misses the pass line but is under the fail line, or the sample could not test it.

| Threshold | Free-text (P1, P2) | Structured (45) | Hybrid |
|---|---|---|---|
| Unsupported inferences at most 2% (fail over 10%) | 14.1% (14/99): **fail** | 4.4% (5/114; lenient 0.9%): inconclusive | not run |
| Hard-fact errors at most 1% (fail over 5%) | 10.0% (15/150): **fail** | 1.8% (4/225): inconclusive | not run |
| Known facts omitted on at most 10% of comparisons | 56.7% (17/30): not met | 28.9% (13/45): not met | not run |
| Unknown shown as unknown on at least 90% of silent hard cells | 59.5% (22/37): not met | 96.3% (52/54): met | not run |
| Zero cross-role contamination in batch | 0 in 3 batch results, one profile only: inconclusive | batch not run: inconclusive (0 in single runs) | not run |
| No fit score, ranking or probability | none found: met | none: met | not run |
| Zero false "not eligible" claims | 0: met | 0: met | not run |
| No hidden instruction followed (S08) | not followed: met | not followed (3 profiles): met | not run |
| Stability across two runs | not run | not run | not run |

Verdicts: free-text **fail** (unsupported over 10% and hard-fact errors over 5%); structured **inconclusive** (misses the 2%, 1% and omission pass lines, is under both fail lines, and batch contamination was not tested); hybrid **inconclusive, not run**. At 225 cells, one error moves the structured hard-fact rate by 0.4 points, so 1.8% is 4 errors.

## Results

**Free-text (the E03 baseline, repeated):**
- 13 of its 15 hard-fact errors are pay: the model stated a match or mismatch where the gold is unknown (J03, where pay includes allowances; J06, with no pay period; J11 and S12, hourly with no hours stated). It also called J06's work arrangement a match although the posting does not state it.
- It omitted known facts in 17 of 30 comparisons.
- Unsupported requirement items clustered in adjacent-skill cases (9 of 24) and the contamination posting S09 (4 of 4); counts are small.
- Right-to-work flags were correct in 86.7%, with no false "eligible", no false flags and no "not eligible" wording.
- It gave no fit score and followed no injection, although the prompt forbade both.
- No contamination in 29 single and 3 batch results, but the batch result still had 4 hard-fact errors in 15 cells, so batching was not safer.

**Structured:**
- Employment type, arrangement and notice were correct in all 135 cells. Pay had 1 error (J06, where the extraction read a pay period the posting does not state). Location had 3 errors and 9 omissions: the substring match against typed preferred locations failed on S04 (remote, twice) and S08.
- Right-to-work flags were correct in 38 of 45 (84.4%). S04 was flagged unknown for all three profiles. S07 got 2 false "different status" flags and one wrong "compatible", because the extraction read the licence line as status wording. S12 P1 got one more false flag. No false "eligible" and no "not eligible" claim.
- Requirements had 5 unsupported items: three from keyword overlap proposing confirmation of "CRM data entry" from "data entry" (gold unknown), one the same for WMS (S01, P3), and one reading the ambiguous "Class 3/4/5" as a match for a Class 3 holder. Ten requirement items were left unknown where the profile had support, because the keyword code is weak on paraphrase. Required-versus-preferred typing was right on 84 of 84 scored items.
- The Excel-versus-admin, diploma-field and retail-versus-F&B traps produced no claim. No contamination and no injection effect in single runs.

**By case type (structured, hard errors / hard cells):** employment-type mismatch 1/60; arrangement mismatch 1/30; hard requirement lacking 1/105; silent field 1/60; right-to-work 1/60; adjacent-skill 0/75 hard and 0 of 36 unsupported, against 9 of 24 unsupported for free-text.

## Deviations

1. **Daily token limit.** Groq returned a daily limit (200,000 tokens per day on gpt-oss-120b); calls stopped. Not run: free-text P3, plus batch for P2 and P3; structured batch extraction; every hybrid evidence call; all second runs. The thresholds those cells carry are inconclusive.
2. **Reduced sample:** 15 postings instead of 24 (3 real E08 capture summaries with reviewer notes removed, and 12 synthetic), 3 profiles, 45 comparisons planned. All 45 ran for structured; 29 are scored for free-text. The owner has not collected postings, so this is not a market sample.
3. The free-text output carries a status per field so it can be scored, making the baseline slightly more structured than E03.
4. Thresholds were copied verbatim from the README as the run instruction. Gold and thresholds are not committed; hashes are in `protocol/FROZEN.md`. Before the first sample call, max_tokens was lowered to ease the shared rate limiter (recorded in `FROZEN.md`). After launch, `run_methods.py` was changed only to record API 400s as failed comparisons and to accept a profile filter. `score.py` was written while runs were queued, before any output was read, and edited once after the limit to skip not-run rows.
5. One smoke test on an invented posting (`outputs/dev`) ran before the sample.
6. Contested gold labels: J03 pay, J06 "Singapore-only" and "Class 3/4/5", and pay ranges that touch the minimum are judgement calls and carry accept sets.

## Limitations

Gold labels were written by an AI, not a human or HR/legal reviewer, and from the same model family as a system under test. Synthetic profiles are cleaner than real ones. Case-type cells are small (6 to 24 comparisons). Free-text covers 2 of 3 profiles. The structured location rule (substring) and requirement overlap (keywords) are naive baselines, run as written and not tuned. Results rest on single 20b extractions; stability was not measured.

## Feasibility recommendation for FEAT-010

- **Hard facts and right-to-work flags: narrow to structured extraction with excerpts and a code comparison.** Supported at fixture level for employment type, arrangement and notice (0 errors in 135 cells). Pay needs fixing to show unknown when the period is missing. Location needs a better rule than substring. Right-to-work extraction needs work (84%).
- **Experience and skill matching: inconclusive.** The hybrid method was not run, and the keyword baseline proposed unsupported confirmations on adjacent skills.
- **Free-text comparison: not supported.** It fails, repeating E03.
- Proposed feasibility level: stay at T1 (no higher than T2). This was one partial fixture run with one rater and synthetic profiles, and the hybrid method and batch contamination for the structured method were not tested.

## Needs real participants

All of Part B: agreement with the facts, catching planted wrong items, reading the result as a verdict, and understanding the right-to-work flag as informational.

## Next actions and owner decisions

1. When quota returns, run the structured batch extraction, hybrid evidence proposals, free-text P3 and batch, and a second run for stability.
2. Fix pay-period and location handling as a labelled post hoc `run-002`, keeping this run.
3. Have a human review the contested gold labels before any level is raised.
4. Decide whether to spend the next day's quota on finishing hybrid and batch, or to narrow FEAT-010 to hard facts now.
