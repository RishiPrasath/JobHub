# E14 thresholds (copied verbatim from README.md, 2026-11-10)

Treated as confirmed by the owner's instruction to run (brief rule 1). Not changed after this file was frozen.

## Part A: source access retry
- **Pass:** at least one employment-relevant official source is readable and permitted by its terms.
- **Fail:** none is. In that case the feature narrows to MAS enforcement actions, CASE alerts and links to the official lookups the user runs themselves, and the owner decides whether to keep it.
- Sources that are readable but not permitted count as not readable.

## Part B: harder sweep (applied to the fixed sweep)
The difference between the arms is reported, not part of the pass bar.
- **Pass:**
  - recall at least 70% on the harder set
  - unsupported claims 2% or less
  - no more than 10% of controls (at most 1 of 15) given a wrong employer-level flag
  - 100% of impersonation warnings labelled as brand impersonation
- **Fail:** recall under 50%, or any unsupported claim shown without a source.
- **Inconclusive:** anything between.

## Part C: do people misread it
- **Pass:**
  - at least 75% read the impersonation warning correctly
  - at least 75% do not treat "nothing found" as clean
- **Fail:** fewer than 50% on either measure.
- **Inconclusive:** anything between.

## Notes added at freeze (not changes to thresholds)
- Part B sample is reduced from 30 to about 10 organisations (5 known problems + 5 controls) by the coordinator's instruction. With 5 known problems, recall moves in steps of 20 points (70% is reachable only as 4/5 = 80%); with 5 controls, one wrong flag is 20%, which exceeds the 10% bar, so the control criterion is tested as "zero wrong flags" and cannot show 10% resolution.
- Part C is not run with participants. A simulated pilot cannot satisfy any Part C threshold; verdict for Part C is "Not run with participants" (thresholds untested).
