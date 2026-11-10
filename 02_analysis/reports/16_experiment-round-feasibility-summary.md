# Experiment round 2026-11-10: feasibility summary

Status: coordinator summary for owner review. Levels are provisional and the owner sets scope. Nothing here sets `in` or `out`. Nothing is committed to git.

## How to read this

The owner asked for the planned experiments (E11 to E21) to be run and feasibility determined. Each was run in reduced form by an AI specialist. Read every result with these limits:

- **No real participants.** Every "Part B" and "Part C" that needs people was not run with participants. Where a simulated persona pilot ran, it is labelled simulated and is not evidence about job seekers. No need level can rise from this round.
- **Synthetic data.** The owner has not hand-collected postings. Postings, letters, pastes and profiles are mostly synthetic, and samples are smaller than planned.
- **AI-written gold labels.** Gold labels, rubrics and ratings were written by an AI before each run and frozen by file hash. No human or HR or legal reviewer has checked them.
- **Thresholds.** The owner's instruction to run was treated as confirmation of the proposed thresholds. They are frozen by hash and not committed to git.
- **Daily token limit.** The Groq account allows about 200,000 tokens per model per day. All three models hit it, which cut E12, E13, E15, E17, E18, E19 and E20 short. Incomplete cells are reported as "not run" or inconclusive.

## Result by feature

| Feature | Experiment | Result | Feasibility call (for owner to confirm) | Level |
|---|---|---|---|---|
| FEAT-001 Employer identity check | [E11](../../04_experiments/E11-employer-identity-check/FINDINGS.md) | Part A fails by the written rule (4 and 3 wrong accepts against a limit of 2, all on hidden-employer postings) | Supported at fixture level for named employers with a findable legal name (13 of 13, 6 of 6 lookalikes not confirmed). Not supported for brand to operating entity (0 of 8) or hidden employers. | T3 (earlier X2 run), E11 itself T2 |
| FEAT-002 Single-posting review | [E12](../../04_experiments/E12-single-posting-review/FINDINGS.md) | Part A fails on unknown recall (27.5%) | Supported for source-anchored extraction (261 of 261 claims grounded). Gap-finding and contradiction-keeping are not supported without moving them outside the model. | T2 |
| FEAT-003 Verification questions | E12 | Fail: 38% of 92 questions met all four checks | Not supported as generated. Alternative: fixed per-gap question templates with the official route attached. | T2 |
| FEAT-004 Accept, edit, reject, decision record | E12 | Inconclusive; needs participants | Untested. | T1 |
| FEAT-005 Paste capture | [E13](../../04_experiments/E13-paste-capture/FINDINGS.md) | Inconclusive overall | Supported at fixture level for the snapshot core (storage, restore, stale rule). Field and partial-paste warnings inconclusive; effort untested. | T2 |
| FEAT-006 Official red-flag evidence | [E14](../../04_experiments/E14-official-red-flag-evidence/FINDINGS.md) | Part A narrow pass, Part B fail (recall 20% against 70%) | Narrow to a lookup of named official lists (MOM agency directory, MAS, CASE). The web sweep is not supported. MOM reuse needs permission. | T2 |
| FEAT-007 Harmful signals pack | [E15](../../04_experiments/E15-harmful-signals-fixture-test/FINDINGS.md) | Inconclusive; no fail line reached | Plausible for the two TAFEP-sourced wording categories once pack text is fixed. Other categories not supported until sources are found. | T2 |
| FEAT-008 Employee experience and reviews | [E16](../../04_experiments/E16-employee-experience-sources/FINDINGS.md) | Part A fails: no external source permits reading review text | A build that reads or summarises reviews is not supported. Narrow to link-out cards. | T2 |
| FEAT-009 Pay benchmark | [E17](../../04_experiments/E17-pay-benchmark-occupation-match/FINDINGS.md) | Inconclusive (top-three recall 97.6% on 83 scored postings; stability 83.3% against 85%) | Supported at fixture level for a shortlist-and-confirm step with a careful model; not supported for gpt-oss-20b (no-match handled 5 of 13). Users and basis reading untested. | T2 |
| FEAT-010 Profile comparison | [E18](../../04_experiments/E18-profile-comparison/FINDINGS.md) | Free-text fails (14.1% unsupported, 10.0% hard-fact errors); structured inconclusive | Not supported as free-text comparison. Narrow to a structured check of hard facts, credentials and a right-to-work flag; experience matching inconclusive. | T1 |
| FEAT-011 Resume suggestions | [E19](../../04_experiments/E19-evidence-linked-resume-suggestions/FINDINGS.md) | Inconclusive | Ledger-cited rewording and selection with a human confirming each entry: 0 fabrications in 75 suggestions, but the code check cannot see relevance. Scoped format check supported at fixture level. | T1 |
| FEAT-012 Application tracker | none | Postponed by owner (`later`) | Not assessed. | T0 |
| FEAT-013 Offer and contract checks | [E20](../../04_experiments/E20-offer-completeness-check/FINDINGS.md) | Inconclusive (recall 91 to 95%, but false alarms over budget in every run) | Narrow to a "not stated in this letter" presence check with quote and source, user-confirmed. Not reliable as an automatic check yet. | T1 |
| FEAT-014 Autofill | none | Postponed by owner (`later`) | Not assessed. | T0 |
| FEAT-015 Interview practice | [E21](../../04_experiments/E21-interview-preparation-need/FINDINGS.md) | Part A not run with participants; simulated pilot only | Inconclusive; the pilot's main value was finding problems in the interview guide. | T0 |
| FEAT-016 Candidate profile | none | Not tested (a data-capture feature, no AI experiment planned) | Not assessed here. | T0 |
| FEAT-017 Job preferences setup | none | Not tested | Not assessed here. | T0 |

## What the round says overall

1. **No feature is supported as originally described.** Every tested feature narrowed, failed or stayed inconclusive.
2. **What held up:** grounded extraction from a posting (FEAT-002), unchanged snapshot, restore and stale rule (FEAT-005), exact-name employer lookup (FEAT-001), a careful model's occupation shortlist (FEAT-009), and a ledger-cited method that avoided fabrication (FEAT-011).
3. **What did not hold up:** free-generated verification questions (FEAT-003), a web sweep for red flags (FEAT-006), reading review text (FEAT-008), free-text profile comparison (FEAT-010), brand to entity and hidden-employer handling (FEAT-001).
4. **Pattern across features:** models are good at quoting and extracting, and weak at deciding what is missing or relevant. Code checks catch wording but not relevance. Anything shown to users probably needs user confirmation and a source.
5. **A second model mattered.** In E17 and E20, `qwen/qwen3.8-27b` and `gpt-oss-20b` behaved very differently on the same cases, so a result for one model does not carry to another.

## Open owner decisions (collected from the findings)

- Whether brand to entity is required in the first slice, and whether to add an "employer not disclosed" state (FEAT-001).
- Whether to narrow FEAT-002, FEAT-003, FEAT-005, FEAT-006, FEAT-008, FEAT-010, FEAT-011 and FEAT-013 as proposed, or park them.
- Whether to seek MOM's written permission to use its two lists (FEAT-006), and whether to ask Glassdoor or SEEK about a licence (FEAT-008).
- Whether AI-written gold labels are acceptable or a human or HR reviewer is needed, and who recruits participants for the Part B and C sessions.
- Whether to spend the next day's Groq quota on the missing cells (run-002 folders), or allow paid use.

## Housekeeping

- Parallel writers: a side fork of this session and some specialists wrote into the same experiment folders, causing some collisions (E11 gold, E19 and E21 files). Findings files were checked against the specialists' reports afterwards.
- Docker: E11's specialist renamed stale Docker socket folders under `%LOCALAPPDATA%` to start Docker Desktop. Delete them after a reboot (paths are in the E11 findings).
- Tool fix: `tools/llm_client.py` now catches the Windows `PermissionError` on its lock file.
