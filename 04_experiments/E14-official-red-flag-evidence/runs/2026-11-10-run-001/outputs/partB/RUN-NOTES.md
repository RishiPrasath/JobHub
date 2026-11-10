# Part B run notes (2026-11-10)

- Executors: 20 blind general-purpose sub-agents on the Haiku model (10 fixed-sweep web part, 10 free-form), each given only an organisation name. They wrote armA/Oxx.json and armB/Oxx.json. Neutral codes O01 to O10; mapping kept out of their prompts.
- Fixed-sweep web part: 60 queries (6 x 10), 0 page reads. Free-form: 67 queries, 17 successful page reads, 7 failed reads (HTTP 403 or errors).
- Sub-agent tokens as reported by the harness (include the base context each agent starts with, so they overstate marginal cost): fixed sweep about 791,000 over 10 agents (24 to 66 seconds each); free-form about 833,000 over 10 agents (42 to 86 seconds each). WebSearch is a US-only tool.
- Deviation: the O10 fixed-sweep agent made one stray call to an unrelated visualisation tool (mcp__visualize__read_me). It had no effect on the output.
- Searches were WebSearch (standard), not OpenSERP as in E10; engine and ranking differ from E10.
- Direct list check: harness/list_check.py, output list_check.json. Matches all 5 known problems and none of the 5 controls (C4 Recruit Express was not matched to flagged RECRUITU PTE. LTD.). By construction.
- Scoring: scoring_manual.json, written after all outputs.
- Verification done by the lead: MOM press release naming Wonderful Agency (opened: 14 charges on 28 May 2026, licence status not mentioned); Randstad 2018 statement (opened, impersonation); Kelly Services letterhead article (opened, supports). Robert Walters Malaysia page and ComplaintsBoard page returned HTTP 403 and could not be checked.
