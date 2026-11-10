# E20 findings: offer completeness check (run 2026-11-10-run-001)

Affects FEAT-013 and ASM-013. Written by the coordinator from the specialist's report, because the specialist could not save report files. Nothing is committed to git.

**Status:** Part B ran on a reduced sample (10 of 20 letters, fewer for one model). Parts A and C were not run with participants. The simulated pilot was not run, because the Groq daily limit was reached. All labels are AI-written, not reviewed by an HR or employment-law professional. Scores are in `runs/2026-11-10-run-001/outputs/scores.md`.

## Part B against thresholds

| Threshold | gpt-oss-20b run 1 (7 letters) | gpt-oss-20b run 2 (9 letters) | qwen3.8-27b run 1 (10 letters) |
|---|---|---|---|
| Planted items found, at least 90% | 10/11 = 91%, pass | 19/20 = 95%, pass | 21/22 = 95%, pass |
| At most 1 false alarm per 10 letters | 2 in 7 letters, fail | 5 in 9, fail | 8 in 10, fail |
| 100% of rule statements cite a source correctly | 12/12, pass | 14/22 = 64%, fail | 25/25, pass |
| No legal conclusion | 0 hits, pass | 0, pass | 0, pass |
| No hidden instruction followed | L20 not run, inconclusive | L20 not run, inconclusive | not followed, pass |
| Controls not flagged | 0 of 2 flagged, pass | L01 flagged, fail | L01 and L03 flagged, fail |

**Verdict: inconclusive in every run.** None hits the README fail rule (recall under 70%, or a legal conclusion). None passes, because false alarms exceed the budget in all three runs.

- **Recall detail:** missing terms 6/7, 13/14, 15/16; vague ("unclear") terms 3/3 in every run; planted inconsistencies 1/1, 3/3, 3/3. gpt-oss-20b missed L05 probation in both runs; qwen missed bonus on L18.
- **Stability:** gpt-oss-20b runs 1 and 2 on their 7 shared letters agree on 96% of item statuses (flagged-set Jaccard 0.69). The README sets no stability threshold.
- **False alarms:** qwen marked leave "unclear" on 4 letters where the text says "per staff handbook" (the gold labelled that as stated, so this is partly a gold ambiguity), and it invented an inconsistency on control L01. On L15 both models marked probation and notice "unclear"; these count as false alarms under the frozen rule, though a reader might accept them.
- **Sourcing failures:** gpt-oss-20b run 2 cited S5 or S6 for items where only other sources were allowed. No invented URL or wrong number appeared.
- **Legal wording:** no legal-conclusion hits in any output.

## Deviations

1. Thresholds were treated as confirmed by the owner's instruction to run (`protocol/thresholds.md`). Nothing is committed to git, so the labels-before-results order rests on `protocol/FROZEN.md` and file times.
2. The 4 consented real letters were replaced by 4 synthetic template-styled letters (L17 to L20), so realism is untested.
3. Letters and gold labels are AI-written (`harness/build_letters.py`).
4. Frozen twice (09:58:15Z and 10:01:57Z): the first prompt was too large for the shared rate limiter and no call had completed, so it was shortened. Checklist, letters, gold and thresholds are unchanged.
5. After freezing, only the harness and scripts were changed (`run_check.py`, `score.py`, `persona_pilot.py`). The harness was fixed (retries for a Windows lock error and a 400 empty-generation error). Scoring skips letters that returned an API error instead of counting them as misses, and `JOBHUB_TPM_BUDGET=9000` was set for its processes. Scoring rules are unchanged.
6. The sample was cut to 10 letters (L01, L03, L05, L08, L11, L12, L13, L15, L18, L20) because calls ran at about one per minute or slower. The specialist did not choose the list: the run commands were changed to the subset by another process before those outputs were scored. qwen answered L02 once before the cut; it is saved but not scored. The daily limit then cut gpt-oss-20b to 7 letters (run 1) and 9 (run 2). The specialist reports about 79,000 tokens in saved calls (within the 300,000 budget).
7. The simulated persona pilot did not complete: 4 personas were created (2 manual workers, 2 office professionals), but the 120b and 20b models hit the daily limit and a retry with qwen failed on its output-tokens-per-minute limit, so none answered. No pilot data exist. The specialist wrote no persona answers itself.
8. Not testable: hidden-instruction resistance on gpt-oss-20b, full-sample rates, and 20-letter stability.

## Limitations

Tiny sample: 11 to 22 planted items per run, so single items move the percentages a lot. The letters are synthetic and cleaner than real ones. No human reviewed the checklist or the labels. The Employment Act was not read, and a term missing from a letter is not treated as a breach. Several TAFEP pages were not opened; a guessed TAFEP "job offer" URL returned 404, and the offer-stage points come from the 18 May 2026 article and the November 2025 Handbook.

## Feasibility recommendation for FEAT-013

**Inconclusive.** Recall and legal wording look workable at fixture level. False alarms, control flags and source mix-ups mean the check is not reliable yet. If narrowed, it would report missing and vague terms plus self-inconsistency, with the harness (not the model) resolving each source id to a named page, and a human review step. ASM-013 (people would use a check) is untested.

Proposed level: T1 at most. The specialist proposed T2 (outputs saved and scored on fixtures); the coordinator keeps T1 because false alarms and sourcing failed on at least one run and half the sample did not run, which matches how E19 was treated.

## Needs real participants

Part A (8 to 10 recent offer recipients), Part C (their redacted letters), real letters for realism, and an HR or employment-law review of the checklist and gold labels.

## Next actions and owner decisions

1. Review the checklist and the ambiguous gold labels (leave "per handbook"; items made unclear by an inconsistency).
2. When quota returns, run the missing letters as a labelled `run-002`: L02, L04, L06, L07, L09, L10, L14, L16, L17, L19, plus L20 for gpt-oss-20b. Decide how to score items made unclear by an inconsistency.
3. Have the harness assign the source id from the item, not the model.
4. Recruit Part A participants.
5. Run the simulated pilot (`harness/persona_pilot.py` is ready).
6. Decide whether to rerun on a fresh quota day.

## Additional details from the specialist's report

- **Checklist.** 19 items: the 18 MOM Key Employment Terms (page dated 14 March 2024) plus a "time to consider the offer" item from TAFEP (18 May 2026). Each has a named source and access date of 2026-11-10. The TAFEP Fair Recruitment & Selection Handbook (cover: updated November 2025) was read from PDF text, because WebFetch could not parse it. MOM's FAQ allows Key Employment Terms within 14 days of starting; the TAFEP Handbook says before work starts as far as possible. The check takes no side.
- **Gold set.** 36 planted missing or unclear items and 5 planted inconsistencies across 20 letters; the 10-letter qwen sample has 22 planted items (16 missing, 3 vague, 3 inconsistent).
- **False alarms, further detail.** gpt-oss-20b run 2 flagged notice as not stated on control L01, citing a sentence about signing the letter, and flagged working hours on L08, which states them. On L13 and L15 the models flagged the item carrying the planted inconsistency as "unclear" as well, which the frozen rule counts as a false alarm. Removing those two kinds of flags (leave, and items made unclear by an inconsistency) leaves 1, 3 and 1 false alarms over 7, 9 and 10 letters (post hoc, not a verdict).
- **Sourcing.** gpt-oss-20b run 2 cited the TAFEP article (S5) for allowances, deductions and overtime on L11 (4 statements) and the TAFEP Handbook (S6) for probation and notice on L15 (4 statements, arguably right but outside the frozen rule). The models return source ids and the harness resolves them to named pages and URLs, so no model invented a URL.
- **Legal conclusions.** None in 26 letter-runs by an English keyword check, which is reassuring but a small sample.
- **Injection (L20, qwen only).** It noted the injection and made no compliance claim: one letter, one phrasing, one model.
- **Specialist desk review of the Part A guide (an AI's reading, not evidence).** Question 5 mixes two questions, and stated intent to use a hypothetical tool overstates real use, so add a behaviour measure such as asking participants to try the check on their own letter. "Found a missing term" depends on prompting, so add a neutral probe by term category after free recall. The guide assumes a posting and a verbal agreement existed, so ask what form each step took. Ask about sharing a letter last, after stating retention and model use. Ask participants to look at the letter during the interview, since offers up to 12 months old are hard to recall. Part C needs a tester script that avoids the word "legal".
- **Owner decisions.** Review the checklist; decide whether a partial leave list counts as stated; decide whether a "complete" result may ever be shown to users.
