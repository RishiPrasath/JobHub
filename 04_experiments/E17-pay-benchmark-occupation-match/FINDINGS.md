# E17 findings: pay benchmark and occupation match (run-001, 2026-11-10)

Affects FEAT-009, ASM-009. Written by the coordinator from the specialist's report, because the specialist could not save report files. Thresholds, postings and gold labels were frozen with sha256 hashes in `protocol/FROZEN.md` before the first Groq call. Nothing is committed to git.

This is a reduced run. All evidence comes from AI labellers, AI matchers and a pilot that did not run. Nothing here comes from real participants.

**Overall verdict: inconclusive.** Recall and no-match bars are met on the scored subset; stability is under its bar on a smaller subset; Parts B and C were not run with participants.

## Threshold table

| Threshold | Observed | Verdict |
|---|---|---|
| A1: gold occupation or correct "no match" in top three for at least 90% (pass); under 70% (fail) | qwen/qwen3.8-27b run 1: 79 of 81 scored (97.5%); postings with a real code 61 of 62 (98.4%); 19 postings not scored | Met on the 81 scored; coverage short of 100, so inconclusive overall |
| A2: at least 85% of true "no match" not given a confident wrong match (pass); under 60% (fail) | 15 of 16 handled (93.8%). The 1 wrong, medium confidence: SYN-33 "Work From Home Part Time Admin (Earn Daily)". High-confidence wrong: 0 of 16. 4 of 20 true no-match not scored | Met on 16 of 20 (small count) |
| A3: at least 85% same top-three set across both runs | Run 2 reached 47 postings, all from the 60 reused X3 postings. Same set 39 of 47 (83.0%); same first choice 91.5%; same verdict 46 of 47 | Under the bar on 47; not tested on the other 34 scored. **Inconclusive** |
| B: users pick gold or correct "none of these" at least 80% | Not run with participants | Inconclusive |
| C: at least 75% restate the basis and do not read the range as a verdict | Not run with participants | Inconclusive |

`openai/gpt-oss-20b` (run 1) was stopped after 51 postings, all X3, and is reported separately; it decides nothing.

## Part A results

**Sample.** 100 postings: 60 from E10 X3 (read only, salary, employer and search term withheld) and 40 synthetic (30 from job families X3 did not cover, 10 failure types: 3 promotional, 3 generic sales and marketing, 4 supervisor-type).

**Gold labels.** Two AI labellers worked separately. Labeller A was the specialist. Labeller B was a fresh sub-agent that saw only title, seniority, type, function and the 523-occupation list, and finished before A's labels existed on disk.
- They agreed on the first-choice code for 93 of 100 postings.
- Six of the seven differences were resolved by accepting both codes (demi chef, two accounts-clerk roles, data business analyst, video editor, social content creator). The seventh, X3-46 "Administrative accounts", accepts clerk codes or "none".
- Gold has 20 true no-match postings, and also accepts "none" for X3-53, X3-55 and X3-46. X3's "good fit" judgement was not used. Details in `data/label_disagreements.json`.

**Scored postings.** 81: all 60 X3 postings plus 21 synthetic (SYN-01 to 12, 14, 15, 17, 19, 20, 32, 33, 36, 39). Not scored: SYN-13, 16, 18, 21 to 31, 35, 37, 38, 40.

| Measure (qwen run 1) | Result |
|---|---|
| Top-three hit | 79 of 81 (97.5%). X3 postings 60 of 60; synthetic 19 of 21 |
| Top-three recall, postings with a real code | 61 of 62 (98.4%) |
| Top-one correct (reported only) | 59 of 62 (95.2%) |
| True no-match flagged "none" | 15 of 16 |
| "None" wrongly given when a gold code existed | 0 of 62 |
| Seniority errors, first choice | 4 of 81: X3-42, X3-46, X3-43 (HR business partner to HR manager), X3-55 (sales executive/manager to sales manager). None for the five warehouse supervisors, which was X3's failure |
| Misses | SYN-04 Aircon technician; SYN-33 (above) |
| By family | 100% everywhere except trades (3 of 4, the SYN-04 miss) and promotional (1 of 2, the SYN-33 miss) |

**Shortlist step.** The 25-candidate lexical shortlist (word and character TF-IDF over occupation titles) lost the gold occupation for 1 of 80 postings with a real code (1.2%): SYN-04, also the one trades miss.

**Second model (gpt-oss-20b, 51 X3 postings).** Top-three hit 41 of 51 (80.4%). It flagged only 5 of 12 true no-match postings as "none"; 7 of 12 got a wrong match at medium or high confidence (5 at high), mostly promotional titles and two warehouse supervisors. It made 7 first-choice seniority errors, mostly HR executives mapped to HR manager. On its own, that no-match rate would sit under the 60% fail bar. One run on a small sample, so not a verdict on the model.

**Reading.** The shortlist plus qwen put the right occupation in the top three for 98% of occupation postings and flagged 15 of 16 true no-match postings. That is better than X3's single pick (77% got a real code), but the comparison is not like for like: labels differ, gold accepts several codes for ambiguous roles, and a three-item list is easier than picking one. The result depends on the model, since gpt-oss-20b did much worse on no-match handling.

## Parts B and C

Both need 6 to 8 real job seekers, so they were not run with participants and are inconclusive. The simulated persona pilot (`harness/persona_pilot.py`) produced no output: persona creation hit a malformed-JSON failure, a lock-file error and rate-limit waits, then the daily limit stopped it. Nothing is claimed from it. Even if it had run, it could only have tested screen wording, not whether real people restate the basis or read the range as a verdict.

## Deviations

1. **Sample.** The README planned 100 hand-collected postings from at least 15 families and three boards. No new postings were collected, because crawling is barred and none were supplied. There is no "shows no pay" stratum (the matcher never sees pay anyway). The sample does not represent the market.
2. **Labels.** Two AI labellers, not two humans, and neither an HR or pay professional. B is a different instance of the same model family as A, so the 93% agreement is weak evidence.
3. **Runs cut short.** Planned: qwen two runs plus gpt-oss-20b, all 100 postings. Actual: qwen run 1 on 81 postings, qwen run 2 on 47, gpt-oss-20b run 1 on 51. Postings ran X3 first, so most planned synthetic failure types went unscored. Causes: the shared 8,000 tokens-per-minute limit, two crashes of the rate-limit lock file on Windows (a retry was added and runs resumed from the cache), and the account's daily token limit. The coordinator also directed the cut.
4. **Thresholds judged on a subset.** Recall and no-match used qwen run 1 on the 81 scored postings. Stability used the 47 postings both runs covered.
5. **Descriptors.** The README says to index titles and duty descriptors; the MOM table has titles only, so only titles were indexed and no duty descriptions were shown for Part B.
6. Two smoke-test calls (X3-16, SYN-14, run number 99) checked the output format and were not used.
7. Thresholds not committed to git.

## Limitations

AI labels and AI matchers from related model families, with no human check on gold. Only 81 of 100 postings and 16 of 20 true no-match postings were scored; the no-match result rests mostly on X3 promotional and warehouse-supervisor items. The prompt says "a supervisor is not a manager" and similar, written after seeing X3's failures, which helps those cases and may not carry over. Gold accepts several codes for ambiguous roles, which raises recall; strict first-choice agreement is the reported top-one, 95.2%. Synthetic postings are short and clean. Temperature 0.3, so run-to-run variation is expected. The MOM table is June 2025, full-time residents, excluding bonuses. No prompt-injection text was tested.

## Feasibility recommendation for FEAT-009

**Inconclusive overall. Supported at fixture level for the occupation-shortlist step only, and narrow to a user-confirmed shortlist.** Show three candidates plus "none of these" and a range only after the user confirms; "no benchmark" stays an allowed result. Not supported by this run: stability across runs (83% on 47, under the 85% bar), the second model, and Parts B and C.

Proposed feasibility level: T2 at most (fixture-level, AI labels, partial sample). Users, the basis reading and real postings were not tested.

## Still needs real participants

- Part B: do 6 to 8 job seekers pick correctly from three plus "none of these"?
- Part C: do they restate June 2025, full-time residents, excluding bonuses, and avoid reading the range as a verdict, including a below-range junior posting?
- Human gold labels, ideally including a pay or HR professional.
- Real, hand-collected postings, including noisy and injection-style ones.

## Next actions and owner decisions

1. After the Groq daily limit resets, finish run 1 on the remaining 19 postings and run 2 on the other 53 (cached calls are reused), then re-score. Any prompt or shortlist change goes in a new `run-002` labelled post hoc.
2. Run the second model on all 100, or drop it.
3. Decide on human labellers and recruit participants for Parts B and C.
4. Add duty descriptions per occupation (the table has none) before Part B.

## Update from the specialist's later report (supersedes the figures above where they differ)

The specialist's interim report was received after the figures above were written, with more calls completed before the daily limit. It stopped with background work of its own still running, so these numbers may change again; if a later run adds results, it will be a labelled addition.

| Measure (primary model qwen/qwen3.8-27b) | Earlier snapshot above | Later report |
|---|---|---|
| Scored postings, run 1 | 81 of 100 | 83 of 100 (17 synthetic postings hit the daily limit) |
| Top-three recall (A1) | 79 of 81 (97.5%) | 81 of 83 (97.6%); full-sample range 81% to 98% | 
| True no-match not confidently wrong (A2) | 15 of 16 | 15 of 16 (93.8%); full-sample range 75% to 95% |
| Same top-three set across runs (A3) | 39 of 47 (83.0%) | 40 of 48 (83.3%), X3 postings only; under the 85% bar on the postings tested |
| Top-one (reported only) | 59 of 62 | 61 of 64 (95.3%) |
| Seniority errors, first choice | 4 of 81 | 4 of 83, all too senior (HR business partner to HR manager, Sales Executive / Manager to Sales manager, two accounts-clerk-level roles to Accountant); all 5 X3 warehouse supervisors were flagged "none" |
| Second model gpt-oss-20b | 51 X3 postings; 5 of 12 no-match handled | 58 postings, mostly X3; no-match handled 5 of 13 (38.5%), 8 confident wrong matches; finds the right code about as often (93.2%) but does not say "none" |
| Cross-model agreement | not reported | the two models gave the same top-three set on only 15 of 57 postings |

Verdicts are unchanged: Part A overall **inconclusive** (recall and no-match bars met on the scored subset, stability just under its bar on the postings tested, coverage short), Parts B and C not run with participants.

Further points from the later report:
- **Labellers.** Two AI labellers (the specialist and a fresh blind sub-agent). Primary codes agreed on 93 of 100; the 7 differences were reconciled by a written rule (6 had two defensible codes, 1 was a real disagreement). 20 postings are true no-match. Both labellers are the same model family, with no HR or compensation reviewer.
- **Persona pilot.** Six personas were created, but the Part B and C answers were never obtained. The prepared screens are in `runs/2026-11-10-run-001/outputs/personas/screens_for_pilot.md`.
- **Instrument problem found without a model call.** The MOM table has no duty text, so the plan to show duties on the choice screen has no official source. The shortlist therefore matches on titles only.
- **Part B posting swap.** The Part B posting set was fixed in advance, then three postings (SYN-24, SYN-10, SYN-31) were swapped for X3-33, SYN-08 and X3-21 because qwen run 1 had not reached them.
- **Process.** Others edited the harness and restarted runs (PermissionError retry, partial-collection script, subset option, persona-pilot edit); the specialist stopped three duplicate gpt-oss processes by hand. None of this changed the prompt, shortlist or parameters. Failed calls are recorded as unscored, not misses.
- **Comparison with X3.** qwen scored 60 of 60 on the X3 postings, but this is not like for like (different design, accepted codes and gold).
- **No-pay stratum** was not tested, because the matcher never sees pay.

**Feasibility call for FEAT-009 (for the owner to confirm):** narrow to a shortlist-and-confirm design where the user confirms the occupation and no benchmark is shown on "none". Supported at fixture level for a model as careful as `qwen3.8-27b`, and **not supported** for `gpt-oss-20b`. ASM-009 (users can confirm their occupation) and the reading of the basis have no evidence. Proposed level T2 for the matching step only.

Owner decisions: confirm the narrowed direction and a minimum model capability; decide how the choice screen describes occupations, since the table has no duties; allow the remaining 17 qwen run 1 postings, the 52 qwen run 2 postings and the persona pilot to run when quota returns (identical settings and cache, so only the missing postings cost tokens).

## Completion run, 2026-11-11

Added runs, same prompt and shortlist (`harness/score_completion.py` reuses the frozen scoring functions and adds the new runs; the older scorer is unchanged). qwen3.8-27b hit its daily limit again, so its run 1 stands at 89 of 100 scored (10 failed on the limit) and run 2 at 48. gpt-oss-20b run 1 now covers all 100. gpt-oss-120b and gpt-oss-20b run 2 could not run (daily limit; stopped without results). A simpler model, `allam-2-7b` (7B), was added as a floor check, with two runs on all 100.

| Run | Postings scored | Gold occupation (or correct "none") in top three | Gold-code postings: top-three recall | True no-match handled | Confident wrong match on no-match |
|---|---|---|---|---|---|
| qwen3.8-27b run 1 | 89 | 97.8% | 68 of 69 (98.6%) | 16 of 17 flagged "none" | 1 of 17 |
| gpt-oss-20b run 1 | 100 | 80.0% | 73 of 77 (94.8%) | 6 of 20 flagged "none" | 14 of 20 |
| allam-2-7b run 1 / run 2 | 100 / 100 | 49% / 50% | 49 of 77 (63.6%) both | 0 of 20 both | 20 of 20 both |

- Stability: qwen run 1 vs run 2, same top-three set on 40 of 48 (83.3%, bar 85%), same verdict 47 of 48. allam run 1 vs run 2: same top-three set only 35%, though it gave the same verdict on 99%.
- Models disagree with each other: qwen and gpt-oss-20b gave the same top-three on 34% of postings; qwen and allam 7%.
- Reading: occupation shortlisting depends heavily on the model. qwen clears the recall and no-match lines; gpt-oss-20b has good recall but fails the no-match line (14 of 20 confident wrong matches, against a limit that was met by qwen); the 7B model fails both and never says "none".
- Verdict unchanged for the supported route: Part A **inconclusive** overall (qwen near the stability bar, coverage 89 of 100), and clearly **not supported** for gpt-oss-20b and allam-2-7b on no-match handling. Parts B and C are still not run with participants. The persona pilot was not run (no model with quota that is able to make personas).
