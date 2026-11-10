# E13: paste capture

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-005, ASM-005

## Question

Will real job seekers paste a posting into JobHub with acceptable effort, and does the pasted text carry what a posting review needs, with partial pastes and a stale snapshot flagged clearly?

FEAT-005 is not treated as feasible until this experiment has run. Earlier evidence is [P01 capture notes](../../05_prototypes/P01-paste-and-capture-v2/capture-test-notes.md): one detail page captured, one search page did not, and a repeat visit returned a short page with HTTP 200 (FND-P01-01, T2, bounded checks). No job seeker has pasted a posting into a tool. The phone-to-laptop loss claim is unproved (FND-R01-01), so capture is a fallback and not the lead feature.

## Hypotheses

- **H1 (paste quality):** pasted postings from varied boards contain the minimum fields a review needs, and partial pastes can be detected.
- **H2 (effort):** people complete a paste quickly and unaided, and consider the effort acceptable (ASM-005).
- **H3 (stale notice):** people understand what the stale notice means and what to do about it.

## Definitions

**Minimum fields:** a paste has them when it contains, or explicitly shows the absence of, each of: role title, employer (or a labelled hidden employer), pay, duties or requirements, closing date.

**Stale rule under test (owner decision 2026-11-10):** show the notice when the posting's closing date has passed, or when the snapshot is more than 7 days old. The notice includes a prompt to paste the posting again.

**Partial paste:** a paste that is missing the role body, cut off mid-text, or only job cards or navigation text.

## Part A: paste quality

Runnable by the agent team. Needs no participants.

### Sample

The 30 hand-collected postings from [E12](../E12-single-posting-review/README.md), taken as pasted. No new collection is needed.

In addition, 10 deliberately **partial pastes** made from those postings by a human: 4 cut off mid-text, 3 with the role body missing, 3 with only search-result cards or navigation text.

### Method

1. A human reviewer marks, per posting and **before any run**, which minimum fields are present or explicitly absent. Labels are committed first.
2. Run the snapshot step (paste in, dated snapshot out, with the partial-paste check and the stale rule) on all 40 inputs. The snapshot step does not exist yet. A minimal version is built for this test and its version is recorded.
3. Score the snapshot and the flags against the labels.
4. Test the stale rule on a set of snapshots with known closing dates and capture dates, including postings with no closing date.
5. Write `FINDINGS.md`, add a finding to [findings.md](../../02_analysis/findings.md), and update FEAT-005.

### Measures

- **Paste completeness:** share of the 30 pastes that contain all minimum fields.
- **Field-level misses:** which field is missing most often, by board and by job type.
- **Partial-paste detection:** share of the 10 partial pastes flagged to the user, and false flags on the 30 complete pastes.
- **Stale rule accuracy:** share of test snapshots where the notice shows or does not show as the rule says.
- **Snapshot integrity:** the pasted text is stored unchanged, with its capture time, and can be restored after a correction.

### Proposed thresholds (Part A)

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

## Part B: do people paste

Needs 6 to 8 job seekers, recruited by the owner. The same people can take part in E12 Part B if the sessions are kept separate.

### Design

Each participant pastes **three real postings of their own choosing** from different sources, at least one of them copied on a phone. The researcher watches and notes; the snapshot step is the minimal version from Part A. Participants are not coached on what to copy.

After the pastes, the participant sees one snapshot with the stale notice shown (a planted older snapshot) and is asked what it means and what they would do.

### Measures

- Time from opening the paste box to a usable snapshot, per paste
- Pastes abandoned, and the reason
- Whether the paste carried the minimum fields (scored by the researcher)
- Whether partial pastes were flagged and whether the participant fixed them
- Whether the participant understood the stale notice and its prompt
- A short effort rating after the third paste, and whether they would paste postings like this again
- Phone pastes reported separately

### Proposed thresholds (Part B)

- **Pass:**
  - median time to a usable snapshot of 2 minutes or less
  - at least 75% of participants finish all three pastes unaided
  - most participants rate the effort acceptable
  - at least 75% of participants correctly say what the stale notice means
- **Fail:** most participants rate the effort not worth it, or fewer than 50% finish all three unaided.
- **Inconclusive:** anything between.

Participants consent to notes. They paste postings of their own choosing, and only the researcher's notes are kept. No participant's personal details are stored beyond the findings file.

## Prerequisites

- The 30 E12 postings and their labels, or equivalent
- A minimal paste-and-snapshot step, built for the test
- A human reviewer for the field labels who is not running the snapshot step
- Owner time to recruit participants

## How the result is used

| Outcome | What it does to FEAT-005 |
|---|---|
| Part A pass, Part B pass | Evidence for the owner to raise the levels and to consider `in`. The gate needs N3, T2 and a recorded owner decision. The owner sets the levels. |
| Part A pass, Part B fail | Paste works technically but costs too much. Rethink the entry (for example a browser extension or share-sheet), which is a separate decision. |
| Part A fail or inconclusive | Do not build. Record which boards or fields failed, and decide whether to narrow or park. |

## Layout

- `protocol/` sample design and the committed thresholds
- `data/` the pastes, partial pastes and frozen field labels
- `harness/` scoring scripts
- `runs/YYYY-MM-DD-run-001/outputs/` raw results, never edited
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Link capture and crawling (job-board crawling is still awaiting owner confirmation in [SCOPE.md](../../06_scope/SCOPE.md)), browser extensions, phone-to-laptop handoff, whether the posting is still live on the board, and what the review does with the snapshot (see [E12](../E12-single-posting-review/README.md)).

## Decisions for the owner before the run

1. Confirm or change the thresholds and the stale rule (closing date passed, or snapshot older than 7 days).
2. Confirm the sample: the E12 postings plus 10 partial pastes.
3. Decide who writes the field labels and who makes the partial pastes.
4. Decide who recruits the Part B participants, and whether they overlap with E12.
5. Decide who builds the minimal snapshot step and where it lives.

## Deviations

None yet.

## Limitations

- 30 pastes and 6 to 8 participants support direction, not statistics.
- Participants choose their own postings, so the mix of boards is not controlled.
- The snapshot step is a minimal version, not the product.
- The 7-day rule is a starting guess and is not validated against how fast postings change.
- Pasting is tested on the participant's own device; behaviour on other devices is not.
