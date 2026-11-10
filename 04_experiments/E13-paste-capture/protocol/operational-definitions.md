# E13 operational definitions (written 2026-11-10, before data and before any run)

These make the README definitions precise enough to label and score. They add no new thresholds.

## Sample

- 30 synthetic "pasted" postings (`data/pastes/P01..P30.txt`), `synthetic: true`. They are modelled on how text looks when a person selects a whole page on MyCareersFuture, JobStreet, FastJobs or a company careers page and copies it. They are NOT copies of real postings, and the layouts come from the author's recollection of those boards; none was checked against a live page (no crawling is permitted).
- 10 deliberately partial pastes (`data/pastes/P31..P40.txt`): 4 cut off mid-text (P31-P34), 3 without the role body (P35-P37), 3 with only search-result cards or navigation (P38-P40). P31-P37 are derived from named source postings among P01..P30; P38-P40 are written separately.
- The README says to reuse the 30 E12 postings. E12 is being run by another specialist at the same time, so E13 does not depend on it (deviation recorded in FINDINGS.md).
- Each paste has a synthetic capture time (`captured_at`, Asia/Singapore, UTC+8).

## Field states (gold labels)

For each of five fields the gold label is one of:

- `present`: the value is in the paste.
- `explicit_absence` (pay, closing date) or `hidden_labelled` (employer): the paste states that the value is not given or hidden (for example "Salary: not disclosed", "Open until filled", "Company name confidential").
- `missing`: neither the value nor an explicit statement is in the paste.

A paste "contains the minimum fields" when no field is `missing`. Duties/requirements count as `present` when the paste has any responsibilities, requirements or role description text.

Silent absence is a miss. A board that simply does not show a closing date, so the paste has no closing date line, is a `missing` closing date.

## Partial-paste truth

`partial_truth` is true for: (a) cut off mid-text, meaning the text ends in the middle of a sentence or word, or on a "show more" or ellipsis teaser; (b) role body missing, meaning no responsibilities, requirements or description text; (c) only job cards or navigation text, meaning a search-result or site page that is not one posting.

A paste that stops at a natural section end (for example the user did not copy the company overview or footer) or starts below the page header is NOT partial. It can still have `missing` fields. The 30 "complete" pastes are non-partial in this sense; some are field-incomplete. A "false flag" is a partial flag raised on one of the 30.

Because a missing role body is defined as partial, `duties` is `present` in all 30 pastes.

## Closing date value

`closing_date_iso` is the calendar date the posting closes in Singapore time, or null. A relative statement ("Closing in 9 days") resolves against `captured_at`.

## Stale rule (precise)

Evaluated at a given `now` (timezone-aware):

- closing date passed: `closing_date < now.date()` in Asia/Singapore. Closing on today's date has NOT passed.
- snapshot old: `now - captured_at > 7 days` exactly (7 days to the second is not old).
- Notice shows if either holds. A posting with no closing date is judged on age alone.
- The notice text includes a prompt to paste the posting again.

## Tests

1. Rule table: `data/stale_rule_cases.json`, hand-written (capture time, closing date or none, now, expected notice and reason), with boundaries around 7 days, closing today, midnight in Singapore versus UTC, and no closing date.
2. End to end: for every paste in P01..P30 that has a gold `closing_date_iso`, plus those with none, the snapshot step extracts the closing date itself and the notice is compared with the notice computed from gold values, at four `now` times: 2026-11-10T12:00, 2026-11-16T12:00, 2026-11-19T12:00, 2026-12-10T12:00 (all +08:00).

## Integrity test

Every one of the 40 pastes is stored and read back from disk; sha256 of the stored text must equal sha256 of the original bytes. A correction (an edited copy) is then applied and "restore original" must return the original bytes exactly. Pastes include CRLF line endings, non-breaking spaces, zero-width characters and emoji, which must not be normalised in storage.

## System under test

`harness/snapshot.py` is the snapshot step: deterministic (regular expressions and counts). `harness/llm_check.py` is a light LLM check with the same outputs. The deterministic step is the primary system for the threshold verdicts. The LLM check, and the union of the two partial flags, are reported as secondary variants. Both are declared here before the run.
