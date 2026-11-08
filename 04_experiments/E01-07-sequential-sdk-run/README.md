# E01-07: Sequential SDK run (2026-10-19)

Status: complete, **narrative only (T1)**. Raw responses were observed but not saved, so these results cannot be reproduced from this repo.

This record replaces seven placeholder folders that held only a topic description. The work is written up in [findings.md](findings.md), and the earlier run in [draft-report.md](draft-report.md).

| ID | Topic | Question | Outcome | Lines |
|---|---|---|---|---|
| E01 | Source grounding | Do outputs stay faithful to the posting and keep locators, qualifiers and ownership? | Pass with schema caveat | 40-63 |
| E02 | Contradiction handling | Are conflicting values kept rather than silently resolved? | Pass on dedicated fixture; weakened in holistic flow | 65-77 |
| E03 | Profile comparison | Can explicit candidate facts be compared cautiously with requirements? | Fail | 115-132 |
| E04 | Resume alignment | Do suggestions stay truthful and evidence-backed? | Partial safety; failed factuality | 134-155 |
| E05 | Prompt injection and safety | Does it resist untrusted instructions? | Pass on the tested fixture only | 177+ |
| E06 | Industry portability | What is shared, and what needs sector extensions? | Partial pass | 157-175 |
| E07 | Model comparison | How do models compare on the same fixture? | Partly run; not structured as a comparison | 28-32, 193+ |
