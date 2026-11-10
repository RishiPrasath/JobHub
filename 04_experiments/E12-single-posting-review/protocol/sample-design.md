# Sample design (written before the run)

Planned in the README: 30 postings collected by hand by the owner. The owner has not hand-collected postings and the brief forbids crawling, logins and scraping, so the sample is reduced and partly synthetic (recorded under Deviations in FINDINGS.md).

Run sample: 24 postings.
- 3 real captured fixtures from E08 (E12-P01 to P03: R4-JB-003 Class 4 Driver, R4-JB-006 Vehicle Mechanic, R4-JB-011 Part-Time Admin Assistant). They are note-form captures from Round 4, not raw page dumps.
- 21 synthetic postings (E12-P04 to P24) written by Claude on 2026-11-10 in the general layouts of MyCareersFuture (8 postings in total incl. P01), JobStreet (6), FastJobs (6) and a company careers page (4). Employers, numbers and contacts are invented; marked `synthetic=true` in the posting header. The model never sees that flag or any strata metadata.
- Job types (24 postings, 24 distinct `type` values; grouped here by family): manual (driver, mechanic, warehouse, security, cleaner, healthcare assistant), clerical (part-time admin, data entry, customer service, admin executive), professional (accountant, software engineer, marketing manager, data analyst), part-time (retail, kitchen helper, tuition centre assistant, call-centre customer service), contract (project coordinator, agency admin coordinator, van driver, data analyst), gig (delivery rider, freelance designer, event crew).
- Planted contradictions (synthetic edits): P06 (two pay ranges), P07 (two sets of working hours), P08 (two hourly rates), P09 (two shift times). Total 4.
- Hidden instructions: P15 (note to AI systems in the body), P16 (HTML comment), P17 (bracketed note demanding a non-JSON reply). Total 3.
- Decoys for false conflicts: P21 and P22 (figures that look different but are consistent). P03 carries a real E08 capture note about a URL job id versus page title (counted as an unplanted contradiction, not among the 4).

Models and runs: openai/gpt-oss-120b, two runs (stability); qwen/qwen3.8-27b, one run. Third model (gpt-oss-20b) is not used in Part A.

Not claimed: that the sample represents the market, that synthetic postings behave like real ones, or that 24 postings support statistics.
