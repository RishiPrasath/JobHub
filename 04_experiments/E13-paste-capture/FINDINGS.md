# E13 findings: paste capture

Date of run: 2026-11-10. Run folders: `runs/2026-11-10-run-001/` (pre-registered plan) and `runs/2026-11-10-run-002/` (post hoc robustness check, labelled as such). Affects FEAT-005 and ASM-005. Run by an AI specialist, not reviewed by a human. Written by the coordinator from the specialist's report, because the specialist could not save report files.

## Headline

- All of Part A used synthetic pastes written by the same AI that built the snapshot step and wrote the labels. It shows the instrument works on that fixture, not how real pastes behave.
- On the fixture, 1 threshold is inconclusive (completeness 19 of 30 = 63%) and 4 pass. Part A overall is inconclusive. Part B was not run, so every Part B threshold is inconclusive.
- The 150 of 150 field score is not trustworthy. On a held-out set written by another model, the same step got all five fields right on 2 of 10 pastes and falsely flagged 3 of 10. A `qwen/qwen3.8-27b` check got 10 of 10.
- Low completeness comes mostly from boards that do not show a closing date or pay. That follows from the definition ("silent absence is a miss") and from how the boards were modelled. It is not evidence that people lose text when pasting.

## 1. Thresholds (frozen; deterministic step v0.1.0; synthetic data)

| # | Threshold | Observed | Verdict |
|---|---|---|---|
| A1 | At least 80% of 30 have all fields (fail under 50%) | 19/30 = 63.3% | Inconclusive |
| A2 | At least 90% of 10 partials flagged (fail under 70%) | 10/10 (cut-off 4/4, no body 3/3, cards or navigation 3/3) | Pass at fixture level |
| A3 | No more than 2 false flags on 30 | 1/30 (P29, a page pasted twice whose second copy ends mid-list) | Pass at fixture level |
| A4 | Stale rule correct on 100% | 153/153 (table 33/33, end to end 120/120); the notice includes the re-paste prompt | Pass |
| A5 | 100% restore to original | 40/40 (including CRLF, non-breaking space and zero-width characters) | Pass |
| Overall Part A | | | Inconclusive |
| B1 to B4 | Median time, unaided completion, effort rating, notice understanding | Not run with participants | Inconclusive (not tested) |

## 2. What ran

- Snapshot step `harness/snapshot.py`, "snapshot-step 0.1.0 (E13, deterministic)": regular expressions and counts, no model. It stores the pasted text unchanged with its capture time, detects five fields on a normalised copy, flags partial pastes (cut off, no role body, or cards or navigation), applies the stale rule, keeps corrections as separate revisions, and restores the original.
- Light model check `harness/llm_check.py` (prompt "llm-check-prompt v1") with `qwen/qwen3.8-27b`, temperature 0, reasoning effort low.
- Persona pilot: personas created by `tools/persona_creator.py` (creator `gpt-oss-120b`, answering agent `gpt-oss-20b`).
- Run-002 held-out pastes were written by `gpt-oss-120b`.
- Tokens in cached calls: about 47,500 of the 300,000 budget. Failed and retried calls are not counted.

## 3. Results

### 3.1 Sample

30 synthetic pastes: MyCareersFuture 9, JobStreet 8, FastJobs 6, company pages 7. Noise includes cookie banners, badges, "similar jobs" cards with other employers' pay, mixed order, a page pasted twice, and head-trimmed and tail-trimmed copies. 10 partials: 4 cut off, 3 with no role body, 3 of search results or navigation.

### 3.2 Completeness by board (gold labels)

| Board | n | All five fields | Missing fields |
|---|---|---|---|
| MyCareersFuture | 9 | 8 (88.9%) | One head-trimmed paste lacks title, employer, pay and closing |
| JobStreet | 8 | 3 (37.5%) | pay 3, closing 4 |
| FastJobs | 6 | 3 (50.0%) | closing 3, employer 1 |
| Company page | 7 | 5 (71.4%) | pay 2, closing 1 |

By job type, pastes with all five fields: professional 4 of 8, clerical 2 of 6, manual 5 of 6, contract 3 of 3, part-time 2 of 4, gig 3 of 3.

- Missing by field (of 30): closing date 9, pay 6, employer 2, title 1, duties 0. Duties are never missing by construction, because a missing role body counts as a partial paste.
- If closing date were not required, 23 of 30 (77%) would be complete. If neither closing date nor pay were required, 28 of 30 (93%).
- Only 17 of 30 pastes have a closing date. For the other 13 the stale rule can act only on snapshot age.

### 3.3 Field detection (run 001)

30 of 30 on every field, including the relative date "Closing in 9 days". This is circular, because the author wrote the data, the labels and the rules.

### 3.4 Partials and false flags

All 10 partials were flagged with the right reason. P29 was falsely flagged as cut off. A realistic two-pane full-page dump (five job cards on the left, the selected job on the right) was flagged as cards or navigation even though the selected posting was complete. That is a likely source of false flags.

### 3.5 Stale rule

- The rule: show the notice if the closing date is before today in Singapore time, or the snapshot is more than 7 days old. Exactly 7 days is not old, and closing today has not passed.
- The 33 hand-written cases cover the 7-day boundary, closing day, midnight in Singapore versus UTC, month and year ends, and no closing date. All 33 pass.
- The end-to-end test used closing dates the step extracted itself, at four "now" times. All 120 pass.
- The "closing passed only" branch is covered by the table but not by the end-to-end set.
- The age rule alone gives a notice on 14 of 30 pastes after six days and on all 30 after nine days. Whether that is too eager is not tested.

### 3.6 Integrity

40 of 40 stored texts equal the original, and 40 of 40 restore to the original after a correction.

### 3.7 Run 002 (post hoc; 10 pastes plus 3 partials; step unchanged)

The pastes were written by `gpt-oss-120b` to specified field states, with prose descriptions and messier pages. The labels were written by the specialist after reading the pastes and before the step ran on them. Two labels are ambiguous: H03 (title only in a sentence) and H05 ("Posted by a verified employer", counted as no employer name). Thresholds are not applied to this run.

| System | Title | Employer | Pay | Duties | Closing | All five right | Partials flagged | False flags on 10 |
|---|---|---|---|---|---|---|---|---|
| Deterministic v0.1.0 | 7 | 8 | 9 | 8 | 8 | 2/10 | 2/3 | 3/10 (H02, H07, H10) |
| qwen check | 10 | 10 | 10 | 10 | 10 | 10/10 | 3/3 | 1/10 (H01) |

The deterministic step failed on titles that sit inside a sentence or contain "$", "Private Advertiser" written as a company line, "Apply anytime, no deadline", "applications will be reviewed until 28 November 2026", prose descriptions with no headings (judged to have no role body: H07, H10), pay from other jobs' cards counted for the selected job (H01), and a cards-only page cut before the job (HP3), which was not flagged.

### 3.8 Model check on run 001

It ran on 18 of 40 pastes (P01 to P13 and P31 to P35) before a daily token limit. Result: 13 of 13 complete pastes right on all five fields, 5 of 5 partials flagged, 0 false flags. This is a subset and not a threshold score.

### 3.9 Part B

Not run with participants. A **simulated pilot** ran (not evidence about job seekers). It stopped at the `gpt-oss-20b` daily limit, leaving 4 personas who answered the paste question and 3 who answered the notice question.
- The set clustered: personas 01 and 05 were near duplicates, as were 02 and 06. Personas 05 and 06 were not run.
- Three of four said they would select everything and paste the whole page; one would select from the job title to the end of the description.
- Effort ratings were 1, 2, 3 and 4. Expected time was 5 to 45 seconds.
- All named the noise (menu, cookie banner, footer, other jobs). Two said they would not do this for every job; two said sometimes.
- All 3 who saw the notice read the generic wording as "my saved copy may be old" and would paste again. All 3 found wording that gives the reason (closing date passed) clearer.
- The paste question was badly worded and needs fixing before any real session.
- A simulation cannot show real phone copying, time, abandonment, effort tolerance, or whether people understand the notice.

## 4. Surprises and issues

1. The perfect run-001 score is circular.
2. The deterministic rules are brittle on prose and unusual layouts. A model check was far more robust on small samples, but has cost and privacy implications.
3. Two-pane page dumps are a likely false-flag source for the "cards or navigation" check.
4. The definition counts silent absence as a miss.
5. `tools/llm_client.py` `_Lock` raised `PermissionError` on Windows under contention. The coordinator has fixed this.
6. **`gpt-oss-120b`, `gpt-oss-20b` and `qwen` all hit the 200,000 tokens-per-day limit during the wider work.** This affects every experiment that is still running.

## 5. Deviations

1. Own 30 synthetic pastes instead of the E12 postings, because E12 ran concurrently. Layouts come from the author's recollection and were not checked against live pages. The sample does not represent the market.
2. Labels and partial pastes were made by the AI author, not a human reviewer. The step was built by the same author.
3. Thresholds were treated as confirmed by the instruction to run, then frozen. They are not committed to git.
4. The model check was added as a secondary variant, declared in advance.
5. The model check covers 18 of 40 pastes in run 001 and all 13 in run 002.
6. After a limiter crash the specialist added retry-on-`PermissionError` and an optional id subset to `llm_check.py`, and made `score.py` tolerate subsets. No prompt, label or threshold changed.
7. Pilot: one persona was briefly run on `gpt-oss-120b` before its daily limit stopped it, and that attempt was abandoned. The pilot then stopped at the `gpt-oss-20b` daily limit.
8. Run 002 is post hoc and small.
9. Part B was not run with participants.
10. `results.json` and `results.md` in run 001 were regenerated by `score.py` after the model check finished. Raw outputs were not edited.

## 6. Limitations

- Synthetic, author-written data, labels and rules, with no independence between them.
- Samples are small, and two labels are judgement calls.
- Board layouts are from memory. If real JobStreet or FastJobs pages show closing dates, completeness would be higher.
- The 7-day rule is an untested starting guess.
- The model check does not cover the whole sample.
- Part B and all human questions are untested, and the persona results are simulated.
- The snapshot step is a minimal test version, not the product.

## 7. Feasibility recommendation for FEAT-005

**Narrow to the snapshot core.**
- **Supported at fixture level:** unchanged storage with capture time, restore of the original, and the stale rule with a re-paste prompt.
- **Inconclusive:** missing-field and partial-paste warnings. The deterministic step is perfect on its own fixture and weak on the held-out set. The model check did well on small samples. Neither has seen a real paste.
- **Inconclusive (not tested):** whether people accept the paste effort (ASM-005).
- **Not supported:** nothing here argues against FEAT-005.

Proposed feasibility level: **T2, unchanged.** Saved fixture outputs now exist. T3 needs a pre-registered test on real data, and these data are synthetic and author-labelled. The need level stays N1.

## 8. Still needs real participants or a human

- Part B in full: 6 to 8 job seekers, three real postings each, one from a phone.
- At least 30 real pastes from at least 3 boards, labelled by someone who did not build the step.
- Whether people understand the stale notice and which wording works.

## 9. Next actions and owner decisions

1. Is silent absence (a board that does not show a closing date or pay) a paste defect, or an acceptable "not shown on this board" state?
2. Is a model check acceptable for field and partial-paste warnings, given cost and privacy?
3. Collect real pastes by hand, have a human label them, and rerun Part A unchanged as a new run folder.
4. Recruit Part B participants. Rewrite the pilot paste question and add a two-pane dump to the inputs.
5. Add the reason to the stale notice (closing date passed versus older than 7 days) and test it with people.
