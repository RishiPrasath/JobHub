# E14 findings: official red-flag evidence (run 001, 2026-11-10)

Written by the coordinator from the specialist's report, because the specialist could not save a findings file. The underlying records are in `protocol/`, `data/`, `harness/` and `runs/2026-11-10-run-001/outputs/`.

Thresholds and ground truth were frozen (file hashes in `protocol/FROZEN.md`) before any model call. Nothing is committed to git.

## Summary against thresholds

| Part | Threshold (proposed, frozen before the run) | Observed | Verdict |
|---|---|---|---|
| A | At least one employment-relevant official source readable and permitted | MOM Employment Agencies Directory (agencies under revocation, suspension or surveillance) and the MOM stop-work-order list are readable for a plain read | **Pass, narrowly** |
| B | Fixed-sweep recall at least 70%; fail under 50% | 1 of 5 = 20% | **Fail** |
| B | Unsupported claims 2% or less | 0 of 29 found, but only 3 cited pages could be opened and checked (2 returned HTTP 403) | Pass, weakly verified |
| B | No more than 10% of controls wrongly flagged | 0 of 5 on the frozen rubric; 1 of 5 if complaint-site posts count | Pass, fragile |
| B | 100% of impersonation warnings labelled as such | 9 of 9 fixed sweep; 10 of 11 free-form | Pass (fixed sweep) |
| C | At least 75% read the warning correctly and do not treat "nothing found" as clean | Simulated pilot only (6 personas) | Not run with participants |

## Part A: source access

Readable and permitted for a plain read:
- **MOM Employment Agencies Directory**, list of agencies under revocation, suspension or surveillance: 26 named agencies (18 revoked, 6 suspended, 2 under surveillance). The plain fetch showed "Content is loading", so a rendering browser was used.
- **MOM stop-work-order PDF:** 143 rows, 1 Jan to 30 Sep 2026.
- **MAS and CASE**, as in E10.

MOM's terms bar commercial reuse, and the PDF asks not to be reproduced.

Not usable:
- **PDPC:** terms clause 20(a) bans robots, so its list was not fetched.
- **SGX:** the page never rendered, even in a browser, and its terms could not be read.
- **ACRA and ScamShield:** terms bar caching or scraping, and neither is an issues list.
- **Courts:** eLitigation is up, but Employment Claims Tribunal decisions are anonymised, so they cannot be searched by employer.

## Part B: harder sweep (10 organisations: 5 agencies with licence actions, 5 controls)

| Measure | Fixed sweep | Free-form | Direct list check |
|---|---|---|---|
| Recall of known problems | 1 of 5 (20%) | 1 of 5 (20%) | 5 of 5, circular: the ground truth came from the same list |
| Unsupported claims | 0 of 29 (weakly verified) | 1 of 46 (2.2%) | n/a |
| Wrong flags on controls | 0 of 5 | not a pass bar | n/a |
| Impersonation labelling | 9 of 9 | 10 of 11 | n/a |

Why recall failed: web search never surfaced the MOM directory, so licence status was invisible to both arms. The only problem found was one agency, through a 2026 MOM prosecution release. The direct list check found all five, but that result is not accepted as evidence, since the ground truth was built from that list.

Cost: the fixed sweep ran 60 searches. The free-form arm ran 67 searches, 17 page reads and 7 failed reads.

## Part C: simulated pilot (6 personas; no threshold satisfied)

Simulated personas, not participants.
- All 6 read the impersonation warning correctly.
- 2 of 6 treated "nothing found" for a resolved company as "legit".
- None treated "nothing found" for an unresolved company as clean.
- None took the non-employment item as an employment flag.

The stimuli state their own meaning and the model echoes it, so this is a wording check only. It shows that a plain-language "nothing found" can still be read as "legit" by a third of simulated readers.

## Deviations

- The sample was cut from 30 to 10 organisations. "Before 2022" could not be verified because the directory shows no action dates.
- Searches used WebSearch through Haiku sub-agents, not OpenSERP.
- `harness/partC_run.py` was patched mid-run after one persona's malformed JSON crashed it, and the run was completed from the cache.
- One fixed-sweep agent made a stray call to an unrelated visualisation tool, with no effect on its output.
- Thresholds and ground truth are frozen by file hash and not committed to git.
- The ground truth for the known problems rests on one list, which makes the direct-check recall circular.

## Limitations

- 10 organisations is a direction, not a statistic.
- The ground truth covers one kind of problem (licensed agencies under action), not employer misconduct generally.
- Most of the cited pages in the fixed sweep could not be opened to verify.
- Persona results show wording problems only.

## Feasibility recommendation for FEAT-006

**Narrow to a lookup of named official lists.** A lookup of a named employer or agency against the MOM agency directory (and MAS and CASE) is readable and was found reliably when the list is checked directly. A web-search sweep for red flags is **not supported**: recall was 20% against a bar of 70%.

Proposed feasibility level: T2 at most, for the narrowed lookup only. ASM-006 ("enough official sources can be read to be useful") is partly supported: two employment-relevant lists are readable, but coverage is mainly licensed agencies, and use is bound by MOM's terms.

## Still needs real participants or a human

- All of Part C.
- A second, independent ground-truth source for the lookup, on general employers and not only agencies.
- Rewording "nothing found" to name what was not checked, then testing it with people.

## Next actions and owner decisions

1. Ask MOM for written permission to use the two lists, or limit the feature to user-run lookups with links.
2. Confirm narrowing FEAT-006 and dropping the web sweep.
3. Keep or remove `data/mom_ea_directory_flagged_2026-11-10.json`, which holds the 26 agency names. The stop-work-order PDF is not stored in the repo.
