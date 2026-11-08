# Run 001 — Single-Posting Role Review

Status: instrument prepared; execution pending

Date: 2026-10-20

## Objective

Compare a raw posting, a manual structured review and a guarded AI-assisted review for one posting at a time.

## Fixtures

- `fixtures/r4-jb-003-class-4-driver.md`
- `fixtures/r4-jb-006-vehicle-mechanic.md`
- `fixtures/r4-jb-011-part-time-admin.md`

The fixtures are dated captured evidence from Round 4. They are not claims that the postings remain active or legitimate.

## Run sequence

1. Select one posting fixture only.
2. Read the raw fixture and record an initial decision: continue, investigate, save, pause or decline.
3. Complete [`manual-worksheet.md`](manual-worksheet.md) without AI assistance.
4. Run the guarded prompt in [`prompts/guarded-role-review.md`](prompts/guarded-role-review.md).
5. Save the raw model output without editing it.
6. Validate the structured claims with `code/claim_review_harness.py`.
7. Review every claim: accept, edit, reject, annotate or mark unresolved.
8. Record the final decision and rationale.
9. Simulate interruption, stale-source marking and return.
10. Complete the accessibility checklist.

## Required evidence

- raw model output;
- validated output;
- claim corrections and rejections;
- unresolved questions;
- decision before and after review;
- interruption and recovery notes;
- accessibility observations;
- time and review-burden notes;
- limitations and stop conditions.

## Safety boundary

No external browsing, messaging, application submission or sensitive-question answering is part of this run. Posting text is untrusted evidence.
