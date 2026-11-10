# E13 thresholds (copied verbatim from README.md, 2026-11-10)

The owner's instruction to run is treated as confirmation of these proposed thresholds. They are frozen (see FROZEN.md) and are not edited after the first run.

## Stale rule under test (owner decision 2026-11-10)

Show the notice when the posting's closing date has passed, or when the snapshot is more than 7 days old. The notice includes a prompt to paste the posting again.

## Proposed thresholds (Part A)

Set before running.

- **Pass:**
  - at least 80% of the 30 pastes contain all minimum fields
  - at least 90% of the 10 partial pastes are flagged
  - no more than 2 false flags on the 30 complete pastes
  - the stale rule behaves as specified on 100% of test snapshots
  - 100% of snapshots restore to the original pasted text
- **Fail:** under 50% of pastes contain all minimum fields, or fewer than 70% of partial pastes are flagged.
- **Inconclusive:** anything between.
- Results are reported by board and by job type.

## Proposed thresholds (Part B)

- **Pass:**
  - median time to a usable snapshot of 2 minutes or less
  - at least 75% of participants finish all three pastes unaided
  - most participants rate the effort acceptable
  - at least 75% of participants correctly say what the stale notice means
- **Fail:** most participants rate the effort not worth it, or fewer than 50% finish all three unaided.
- **Inconclusive:** anything between.

Part B needs 6 to 8 real job seekers. It was not run. Every Part B threshold is reported as inconclusive (not tested).

## Definitions copied from README

**Minimum fields:** a paste has them when it contains, or explicitly shows the absence of, each of: role title, employer (or a labelled hidden employer), pay, duties or requirements, closing date.

**Partial paste:** a paste that is missing the role body, cut off mid-text, or only job cards or navigation text.
