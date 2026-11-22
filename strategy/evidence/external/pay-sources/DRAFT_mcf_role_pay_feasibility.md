# DRAFT: Can JobHub average posted pay for a role from MyCareersFuture?

Run 2026-11-21 (SGT evening) in Claude's built-in browser. Probe script: `DRAFT_mcf_role_pay_probe.py` (same logic, in Python; not yet run as Python). Only aggregate numbers below were kept; no posting content was saved.

## Verdict

**Technically feasible and easy. Not shippable without SWDA's written permission.**

- [verified] robots.txt allows all agents except `meta-externalagent`.
- [verified] The search page loads results from the site's own `POST https://api.mycareersfuture.gov.sg/v2/search?limit=N&page=P` with body `{"search": "<role>"}`. No login or token was needed for search. `limit=100` works. `sortBy: ["relevancy"]` is rejected with HTTP 400 (omit it).
- [verified] Each result has `salary.minimum`, `salary.maximum`, `salary.type.salaryType`. The rendered cards show the same as "$X to $Y Monthly", so scraping the UI DOM would also work but is more brittle than reading the page's own request.
- [verified] In 887 postings across 5 searches, **0 omitted salary** and all were "Monthly". MCF requires a salary range on every posting, so coverage is complete.
- [verified] `ssocCode` was null on all 20 search results checked, so search results cannot be joined to MOM occupations by code; matching has to be by title.
- [verified] Search is relevance-ranked and loose ("software engineer" returned 1,158). Requiring every query word in the title kept 83 to 95% of fetched results.

## Reliability of the salary fields

- [verified] A few values look wrong: 1 to 2 postings per role were excluded (below $500 or max < min), and title-matched minimums go as low as $800 to $1,100 for accountant and data analyst roles, which are probably part-time or intern posts tagged Monthly.
- [inferred] Ranges are wide (software engineer up to $10k to $20k). The midpoint is a reasonable single figure; median is more robust than mean.
- [inferred] Postings skew junior/executive level (see level mix in run), and the API caps practical sampling at what we page through (200 per role here; totals were 87 to 1,158).

## Sample results (title-matched, monthly SGD, midpoint of each posting's range)

| Search | API total | Used | Median min | Median max | Median midpoint | Mean midpoint |
|---|---|---|---|---|---|---|
| software engineer | 1,158 | 190 | 6,000 | 9,500 | 7,900 | 9,336 |
| data analyst | 87 | 82 | 4,500 | 5,650 | 5,000 | 5,384 |
| accountant | 400 | 186 | 4,000 | 5,150 | 4,625 | 4,928 |
| staff nurse | 550 | 199 | 3,000 | 5,000 | 4,000 | 4,159 |
| hr executive | 549 | 148 | 3,000 | 4,000 | 3,650 | 3,663 |

## Against MOM Occupational Wages June 2025 (gross monthly median, local copy in E10)

| Search | Closest MOM occupation (SSOC 2024) | MOM gross median | Posting median midpoint | Gap |
|---|---|---|---|---|
| software engineer | Software developer (25121) | 7,808 | 7,900 | +1% |
| data analyst | Statistical officer/Data analyst (21231) | 5,869 | 5,000 | -15% |
| accountant | Accountant excl. tax (24111) | 5,968 | 4,625 | -23% |
| staff nurse | Registered nurse (22200) | 5,210 | 4,000 | -23% |
| hr executive | Personnel/HR officer (24233) | 4,565 | 3,650 | -20% |

[inferred] Posted pay runs below the MOM median for 4 of 5 roles. Likely reasons: MOM covers all employed residents including long-tenured staff, gross includes allowances and overtime (nursing shift pay), and posting titles mix in assistant/junior roles. So a posting average is a "what is being advertised now" figure, not a substitute for the MOM benchmark.

## Terms caveat and what shipping would need

MCF terms (read 2026-11-21, see `DRAFT_sg-pay-benchmark-sources.md`) bar storing, reproducing, caching or transmitting site content without **written permission from SWDA (Workforce Singapore)**. A live "average posted pay" feature would do all of that. Options:

1. Ask SWDA in writing for permission to compute and display aggregate salary statistics from MCF search (aggregates only, attributed, no posting text). This is the only route to ship it on MCF data.
2. Without permission, keep the MOM/data.gov.sg benchmark (Open Data Licence) and let users paste a posting's pay range themselves for comparison.
