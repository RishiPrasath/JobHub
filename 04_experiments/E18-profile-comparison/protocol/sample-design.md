# E18 Part A sample design (reduced; see FINDINGS.md Deviations)

Written 2026-11-10 before any model call.

- 15 postings: 3 real captured records from the E08 fixtures (J03 = R4-JB-003, J06 = R4-JB-006, J11 = R4-JB-011; they are capture summaries, not full postings) and 12 synthetic postings (S01 to S12, `synthetic: true`). The owner has not hand-collected postings. Not a market sample.
- 3 synthetic candidate profiles in the FEAT-016 section layout and FEAT-017 preference fields: P1 logistics background (permanent resident), P2 administrative (citizen), P3 early-career with adjacent skills (S Pass holder).
- 15 x 3 = 45 single comparisons, plus the batch condition: J03, J06 and J11 sent together in one request, once per profile (3 batch comparisons per method, 9 posting-level results).
- Job families: logistics, trade, administrative, retail, data entry, customer service, accounting, IT support, food and beverage (9). Boards: real captures come from 3 boards (MyCareersFuture, FastJobs, Jobstreet); the synthetic ones are not tied to a board.
- Case types (a posting can carry several): employment-type or arrangement mismatch (J11, S03, S04, S11), adjacent-skill traps (S02, S03, S09, S10, S12), hard requirement the profile lacks (J03, J06, S05, S07, S10, S11, S12), posting silent on a field (J03, J06, J11, S06, S07), preferred versus required wording (S01, S02, S07, S10, S11), right-to-work wording (J06 ambiguous, S10 Singaporeans only, S11 pass holders, S12 citizens and PRs), batch condition (J03, J06, J11), contamination (S09 related-jobs block), hidden instruction (S08).
- Gold labels: data/gold.json, per posting and profile: status for employment type, work arrangement, location, pay against minimum, notice period, right-to-work flag, and one label per stated requirement (with type required or preferred, kind and a posting excerpt). Written by hand by the specialist (an AI) before any run, from the posting text and the profile fields only.
- Part B (participants) is not run.
