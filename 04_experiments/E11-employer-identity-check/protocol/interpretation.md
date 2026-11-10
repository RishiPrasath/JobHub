# How the README thresholds are applied to this sample (written before the first run)

The README thresholds assume 60 postings (15/20/10/10/5). The sample is 39 synthetic postings:
large 9, SME 8, hidden or agency 6, brand differs 10, lookalike or fictitious 6. The thresholds text is not changed. This file fixes how it is read.

1. Absolute caps are applied literally, because a smaller sample makes them easier to meet: "wrong accepted at most 2" and the fail line "wrong accepted 4 or more", "2 or more lookalikes confirmed as real".
2. Rates are applied as proportions, rounded up to a whole posting, because a smaller denominator makes them harder to meet:
   - Correct on at least 70% of postings where truth is known (known = truth type entity, not_disclosed or not_real; "unknown" excluded). Fail line: under 50%.
   - Lookalikes: at least 80% not confirmed as real, which with 6 items means at least 5 of 6.
   - Agency and anonymous: no company named on at least 90%, which with 6 items means 6 of 6. Reported split into 3 anonymous and 3 agency-named.
   - Stability: same headline in both runs on at least 90% of postings (36 of 39).
3. "Correct" is defined in data/ground_truth.json (scoring block). A "wrong accepted" counts any posting where the flow accepts an entity or brand that the truth says should not be accepted, including accepting any entity for a hidden-employer or lookalike posting, and accepting an unknown-truth entity that is not in plausible_uens.
4. The README stratum counts (15/20/10/10/5) are not met. Strata are reported separately, and any claim is limited to the strata actually tested.
5. The small-employer stratum: none of the 8 SME-stratum employers is a micro business. They are small chains, startups and mid-size firms whose own site names the legal entity. A result here supports "known employers" only.
6. Verdict words: pass if every Pass line holds; fail if any Fail line holds; otherwise inconclusive. Lines that the sample cannot test are reported inconclusive, not pass.
7. Part B is not run (no participants). Part B thresholds are inconclusive by construction.
