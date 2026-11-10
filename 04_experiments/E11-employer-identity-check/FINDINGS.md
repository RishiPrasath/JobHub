# E11 findings: employer identity check on synthetic postings

Run date 2026-11-10. Part A ran on a reduced synthetic sample (39 postings). Part B was not run (no participants). Affects FEAT-001 and ASM-001.

Written by the coordinator from the specialist's report, because the specialist could not save report files. Thresholds are copied verbatim in `protocol/thresholds.md`, and how they apply to 39 items is in `protocol/interpretation.md`.

## Short answer

When a posting gives an employer's exact registered legal name, the P05 flow named the correct registered entity every time (13 of 13 accepted answers right, 0 wrong). It accepted none of the 6 lookalike or invented employers. It does not resolve brand names (0 of 8 to the operating entity). It has no way to say "employer not disclosed": it named a company on 3 or 4 of the 6 hidden-employer postings. Under the thresholds as written Part A is a **fail** (run 1 reached 4 wrong accepted; run 2 reached 3), and several pass lines are not met. The failures are concentrated in two strata. Part B is inconclusive because it was not run.

## Thresholds against observed values

Absolute caps are applied literally. Rates are applied as proportions, rounded up.

| Threshold (Part A) | Run 1 | Run 2 | Verdict |
|---|---|---|---|
| Pass: correct on at least 70% of postings with known truth (33 known) | 21/33 = 63.6% | 22/33 = 66.7% | Not met; above the 50% fail line |
| Pass: wrong accepted at most 2 | 4 (H03, H04, H05, H06) | 3 (H04, H05, H06) | Not met |
| Fail: wrong accepted 4 or more | 4 | 3 | **Fail line reached in run 1** |
| Pass: lookalikes not confirmed, at least 4 of 5 (applied as 5 of 6) | 6/6 | 6/6 | Met |
| Fail: 2 or more lookalikes confirmed | 0 | 0 | Not reached |
| Pass: same headline in both runs on at least 90% (36 of 39) | 25/39 | | Not met as written; confounded by quota outage |
| Pass: agency and anonymous postings name no company on 90% (6 of 6) | 2/6 | 3/6 | Not met |
| Fail: correct under 50% | no | no | Not reached |
| Small-employer stratum, reported separately | 6/6 known resolved | 6/6 | See below |

**Part A verdict:** fail by the written rule. If only run 2 counted it would be inconclusive. **Part B:** inconclusive, not run. All wrong accepted answers are hidden-employer postings.

## What ran

- **Flow:** P05 `jobhub-company-research-flow:dev`, unchanged, source commit `d580a348ca05b95a48de7fa0973e73dee9f34c00`. Repo HEAD `11259e858794a3ce725e8445b7c412a3e1009493`, tree clean under `05_prototypes`. The image was rebuilt from those files with cached layers.
- **Command:** the flow's own `cases` command in a container, 2 workers, `READER=fetch`, `READ_POLICY=conservative`. Outputs went to this folder, not to P05's `outputs/`.
- **Model:** `openai/gpt-oss-120b` for the written brief only. The headline, registry check and name gate are code.
- **Search and reader:** OpenSERP (E09 build 0.8.18) with Bing and DuckDuckGo, and the P04 fetch service. Bing answered 35 case-runs per run. DuckDuckGo answered 8 in run 1 and 15 in run 2.
- **Registry:** P03 service, ACRA release 2026-10-14, 2,124,508 rows.
- **Runs:** two full runs in `runs/2026-11-10-run-001/outputs/run1/` and `run2/`, raw and unedited. Scoring is `harness/score_final.py`, which writes `analysis_summary.json`.

## Sample

39 synthetic postings, all `synthetic: true` with provenance. Employer names are real public employers or constructed names. Role and text were invented by an AI. The flow takes an employer string plus a role.

| Stratum | Planned | Built | Notes |
|---|---|---|---|
| Large | 15 | 9 | 7 truth set, 2 unknown |
| SME, chain, startup | 20 | 8 | 6 set, 2 unknown; no micro businesses |
| Agency or anonymous | 10 | 6 | 3 anonymous strings, 3 named agencies |
| Brand differs | 10 | 10 | 8 set, 2 unknown |
| Lookalike or fictitious | 5 | 6 | Constructed; absent from raw ACRA |
| Total | 60 | 39 | 33 known, 6 unknown |

Truth came from the employer's own page (footer, privacy or terms) plus the raw ACRA record by name or UEN, read with plain SQL (`harness/truth_sql.py`). No registry-mirror sites were used. The six unknown-truth items are Singapore Airlines, NTUC FairPrice, Koufu, Carousell, Grab and Toast Box.

## Results by stratum

| Stratum | Known truth | Correct | Wrong accepted | Refused or unresolved |
|---|---|---|---|---|
| Large | 7 | 7 | 0 | 0 |
| SME and startups | 6 | 6 | 0 | 0 |
| Brand differs | 8 | 0 | 0 | 5 "brand unconfirmed" (no entity named), 3 refused |
| Hidden or agency | 6 | 2 (run 1), 3 (run 2) | 4 (run 1), 3 (run 2) | none |
| Lookalike | 6 | 6 | 0 | all caught |

- **Named employers work.** The UEN equalled the truth in 13 of 13 accepted answers, including legal-form wording differences (Ya Kun "Private Limited" versus registered "PTE LTD").
- **Brand names do not resolve.** OCBC, NTUC Income, McDonald's, Mr Bean and Swensen's returned `brand_legal_entity_unconfirmed`. The flow never names the operating entity (Oversea-Chinese Banking Corporation, Income Insurance, Hanbaobao, Super Bean International, ABR Holdings).
- **Name collisions give misleading refusals.** SingPost returned `not_active` on a struck-off namesake (202439966W). Aspire returned `not_active` on 200407197M. Singtel returned `ambiguous_entity`. Grab (truth unknown) returned `not_active` on a sole proprietorship (53355133A). A job seeker would read "not active" for a live, well-known employer.
- **Hidden employers are not handled.** All 3 named agencies were confirmed as real companies. That is true of the agency but it is not the hiring employer, so 0 of 3 passed. Of 3 anonymous strings, run 1 returned a "brand" answer for "A Leading MNC" and called "Confidential Employer" a `likely_lookalike`. Run 2 returned `could_not_confirm_company` for all three.
- **A real employer was called a lookalike.** NTUC FairPrice Co-operative Ltd returned `likely_lookalike` in both runs. ACRA has no entity of that name, so this is a registry coverage gap.
- **Small employers:** 6 of 6 known resolved. These are startups, small chains and mid-size firms whose own site names the legal entity. None are micro businesses, so the claim is limited to employers with a findable legal name.

## Stability

- Same headline text: 25 of 39.
- Same accepted UEN or same refusal: 39 of 39.
- Same scored class: 38 of 39.

The 12 flips from `exists_and_consistent` to `exists_limited_evidence` follow the model quota. The shared Groq quota was exhausted for 15 summaries in run 1 and 32 in run 2, so run 2 wrote only 1 brief. Without a brief the flow cannot reach `exists_and_consistent`. The literal number therefore measures the outage, not the flow's variance, and cannot count as a pass.

## Cost

- **Time:** run 1 averaged 88 s per posting (3,448 s total on 2 workers). Run 2 averaged 57 s because the model step failed fast. Postings the registry settles took under a second.
- **Searches:** 175 per run. About 254 pages read per run.
- **Groq tokens:** not metered by the flow; about 210,000 in total estimated using the flow's own sizing rule.
- **Paid services:** none.

## Deviations

1. 39 synthetic postings instead of 60 hand-collected ones. Strata counts differ. The sample does not represent the market.
2. An AI set the ground truth, before the runs. It is not independent of the model family that drafted the inputs.
3. Registry truth is the same ACRA data the P03 service holds, read directly. Independence is from the flow's matching and web logic, not from the data.
4. Thresholds and the freeze are not committed to git. The record is `protocol/FROZEN.md`.
5. **Two processes worked in this folder at once.** The specialist froze a first version at 10:10:19 UTC. Eleven seconds later another process rewrote `ground_truth.json` (new field names, F-prefixed lookalikes, no `plausible_uens`), `run_input.json`, `thresholds.md` and `FROZEN.md`, and added `build_gold.py`, `run_set.sh` and `score.py`, and ran run 1 and run 2 with them. That freeze (10:10:30) predates its first model call (10:10:37). The specialist's `postings.json` and `interpretation.md` are unchanged since its freeze, and its own attempted run was stopped before producing output. Unknown-truth accepts are reported as unscored; their UENs match the gold notes. The source of the second process is not established, so the independence of the gold from the run harness should be re-checked by a human.
6. The shared Groq quota ran out during run 1 and for nearly all of run 2. Headlines and sources are unaffected, but briefs are missing. No rerun was done, because it would be a new run folder on a shared quota.
7. **Docker repair on the host machine.** Docker Desktop failed on stale socket files that could not be deleted. The specialist renamed their parent folders to `%LOCALAPPDATA%\Docker\run.stale-20261110` and `run.stale2-20261110`, and `%LOCALAPPDATA%\docker-secrets-engine.stale-20261110`. They can be deleted after a reboot.
8. Hidden-employer inputs are employer strings only, because the flow has no extraction step.

## Limitations

- 39 items support direction, not statistics. One item moves a rate by about 3 points.
- Truth quotes came from a plain HTTP fetch of each page.
- Results are tied to the 2026-10-14 ACRA release.
- The lookalikes were built by an AI around names it knew were absent. Real scam employers often use a real registered shell company, so 6 of 6 does not generalise.
- Part B was not run, so ASM-001 is untested.

## Feasibility recommendation for FEAT-001

**Narrow to "named employers with a findable registered legal name", supported at fixture level.** It is **not supported** for brand to operating entity, and **not supported** for hidden-employer postings in its current form. The gaps that need an owner decision are:
- what the product says for a brand it cannot map;
- an explicit "employer not disclosed" state, which needs an extraction step;
- handling of struck-off namesakes and of entities outside ACRA, such as co-operatives.

ASM-001 is inconclusive and needs real participants.

Proposed feasibility level: T2. There are saved outputs from two runs and the thresholds were fixed beforehand. It is not T3 because the data are synthetic.

## Still needs real participants or a human

- All of Part B: whether the result changes a next step; whether the refusal wording ("could not confirm company", "brand legal entity unconfirmed", "not active") is understood; whether a false "not active" or "likely lookalike" on a real employer harms trust.
- Real postings, including real agency and scam postings, collected by the owner, with truth set by a human or independent reviewer.

## Next actions and owner decisions

1. Decide whether the first slice is "named employer, exact legal name", or whether brand to entity is required. If it is required, a new approach is needed; reading the legal name from the employer's own footer or privacy page is one candidate to test.
2. Decide whether the product should add an "employer not disclosed" state.
3. Collect real postings; a human or independent reviewer sets truth.
4. Add an extraction and "not disclosed" test as a new, labelled run folder.
5. Rerun stability as `run-002` when the model quota allows.
6. Run Part B with 6 to 8 job seekers, using the SingPost, Aspire and Singtel wrong refusals as stimuli.
7. Delete the stale Docker folders after a reboot.
