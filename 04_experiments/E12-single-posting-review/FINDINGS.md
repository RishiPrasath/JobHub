# E12 findings: single-posting review (Part A, reduced; Part B not run)

Run folder `runs/2026-11-10-run-001/`, 2026-11-10. Affects FEAT-002, FEAT-003 and FEAT-004 (ASM-002, ASM-003, ASM-004). Written by the coordinator from the specialist's reports and corrected against its final report (the specialist could not save report files). Setup, thresholds, rubric and gold labels are frozen in `protocol/FROZEN.md`. Scoring and question ratings are in `runs/2026-11-10-run-001/scoring/` and `harness/aggregate.py`. Nothing is committed to git.

**Overall Part A verdict: fail on several thresholds for the system as run, on a reduced sample.** Several results are small-n; see the limitations.

## What ran

- **Sample and outputs:** 24 postings were written and frozen (3 real E08 fixtures plus 21 synthetic; 124 gold gaps). Of 72 planned model outputs, 20 were obtained, covering 14 distinct postings. 5 postings have both models complete (P01, P06, P07, P09, P15).
- **Models:** `openai/gpt-oss-120b` run 1 on 8 postings and `qwen/qwen3.8-27b` run 1 on 7. gpt-oss-120b run 2 produced 5 outputs, and only P01 overlaps run 1, so stability rests on one posting.
- **Stopped by the daily limit:** the account's daily token limit (about 200,000 tokens) was hit on gpt-oss-120b and gpt-oss-20b. No further calls were made. Everything uncached is "not run".
- **Part B:** the simulated persona pilot did not run. Every Part B threshold is inconclusive (not run with participants).
- The E08 prompt and completeness gate were used unchanged. The real fixtures were fed as numbered lines without E08's answer-leaking notes, and E08's original inputs were not re-run.

## Thresholds against observed values

| Measure | gpt-oss-120b | qwen3.8-27b | Verdict |
|---|---|---|---|
| Grounding: at least 95% grounded, at most 2% fabricated | 100% grounded, 0 fabricated (261 source-bound claims across both models; the specialist read 14 flagged and 45 random passing claims, all faithful) | same sample | Pass on this sample |
| Unknown recall: at least 80% (fail under 60%) | 13% (run 1), 11% (run 2) | 57% | **Fail** (30 of 109 gold gaps flagged = 27.5% overall; both models under 60%). Six of gpt-oss-120b's 13 outputs raised no unknown or question at all, and the gate did not notice. |
| False conflicts: at most 1 per 10 postings | 0 in 8 postings | 2 in 7 (2.9 per 10) | gpt pass, qwen fail |
| Planted contradictions preserved: at least 3 of 4 | 1 of 4 (pre-registered rule) | 1 of 3 | Not met. The models usually kept both values as two separate claims; reading them together gives 3 of 4 and 2 of 3 (post hoc, labelled). |
| Platform signals mislabelled as employer facts: at most 5% | 14.3% (run 1) | 0% | Pooled 1 of 20 signals = 5.0%. The reverse error is larger: 35 employer-written claims were labelled platform. |
| At least one decision-relevant question on at least 90% of gap postings | 50% | 100% | gpt fail, qwen pass |
| Hidden instructions resisted (3 of 3) | none followed; gpt-oss-120b was tested only on P15 | none followed; resisted 3 of 3 | Pass for qwen; inconclusive for gpt-oss-120b |
| Stability: at least 85% | 72.7% on one posting only | not run | Inconclusive |
| FEAT-003: at least 80% of questions meet all four checks (fail under 50%) | 38% of 92 questions | | **Fail** |

- **Completeness gate:** the gate's completeness logic raised on 0 of 20 outputs. The structural validator caught 1 of the 2 internally inconsistent outputs.
- **Question checks (FEAT-003):** none of the 11 questions where an official route applied named it. About half did not target a decision-critical gap.
- Gold labels and question ratings were written by an AI and are not independent of each other. The rubric was written down before rating.

## Part B

Not run with participants. The simulated pilot did not complete: 6 personas were created and only one persona call ran. Three worksheets with a planted wrong item were built; a rule-based grounding check flagged all three planted items and also 3 of 42 genuine items. All Part B thresholds (gap finding, planted-error catch for FEAT-004, effort, skim indicators, one-week follow-up for FEAT-003) are inconclusive.

## Deviations

- Sample: 24 postings written instead of 30; the owner collected none, and 21 are synthetic. Only 14 have outputs.
- The gpt-oss-120b second run is incomplete (5 outputs, one overlapping posting).
- Every gold-gap hit was read by the specialist as well as every miss, because the keyword matcher over-matched.
- A scorer normalisation fix ("7 pm" versus "7pm") changed the P09 contradiction result.
- Processes the specialist did not start ran this harness against the shared cache; no output was edited.
- About 65,400 tokens used.
- The daily token limit stopped all further calls; uncached cells are not run.
- Gold labels and ratings are AI-written.
- Thresholds frozen by hash, not committed to git.

## Limitations

Small n per model (7 to 8 postings each) and 5 postings with both models. The postings are largely synthetic. Model output is non-deterministic and was not repeated. Unknown recall depends on gold labels written by an AI. The planted-contradiction and injection results rest on 3 to 4 postings.

## Feasibility recommendations

- **FEAT-002:** narrow to **source-anchored extraction**, which is what the grounding result supports. Gap-finding and contradiction-keeping are **not supported** for gpt-oss-120b and inconclusive for qwen. Proposed level: T2 at most.
- **FEAT-003:** **not supported as generated**: only 38% of questions met all four checks and none named the official route. Narrow to fixed per-gap question templates with the official route attached. T2 at most.
- **FEAT-004:** **inconclusive**, because the planted-error catch rate and the skim indicators need real participants. T2 at most.

## Needs real participants

All of Part B for FEAT-002, FEAT-003 and FEAT-004.

## Next actions and owner decisions

1. Decide whether to finish the missing cells and the second run as a labelled `run-002` after the limit resets (or allow paid Groq use).
2. Consider fixed question templates with the official route attached in place of free-generated questions (FEAT-003).
3. Recruit participants for Part B.
