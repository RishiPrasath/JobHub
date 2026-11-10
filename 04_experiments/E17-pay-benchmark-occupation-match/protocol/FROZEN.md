# FROZEN

Frozen at 2026-11-10T09:57:00Z, before the first Groq model call. Not committed to git (the owner has not asked for commits).

| File | sha256 |
|---|---|
| protocol/thresholds.md | 90d006af6248b44d7d9720a13bdf48e75532b08b1c3a3a72f7500b5826a83d16 |
| data/postings.json | ccf5fd5c6470a1b7a8d2e4dcda6b3e262492c81dd923f818ef6694f2403b5964 |
| data/postings_blind.json | 2bc8a7b7bbc1ce9795829ed36fb2492477402c465df3e0c13154a6a4967bf041 |
| data/labels_A.json | 08c2b9bb80936ad03e4d926c40ea34392e8543d7a7203bcf617177312fbb8621 |
| data/labels_B.json | e7b58d0f3691d78d206ac28c36560e376423fa05996978317a2db760da5ba2e7 |
| data/label_disagreements.json | 9e72d9909c50358c7ddbea05566e54164ed38057a9eed2a7120e4c374c4c2d0c |
| data/gold.json | 1a05ac9c9c0745c7fd42d0c747de760977d494163a0c5983f05347bd4c738aa0 |
| harness/shortlist.py | a1174e030435d3a6dc97195dfcfe17b1d61cb6085fe5280f84df116605e3b495 |

Gold labels were written by two AI labellers (A: the specialist, B: a fresh blind sub-agent with no access to A's labels or any matcher output) and reconciled by the rule in harness/make_gold.py, all before any matcher ran. The B labels were produced before A's labels existed on disk.
