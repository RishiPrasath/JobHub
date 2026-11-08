# Run brief

## Research question

When job seekers in different professions each search for roles and the employers behind them are then researched, does the new company-research service ([prototype 03](../../../../../_prototypes/03_company-research-pipeline/README.md)) find useful, verifiable information on real employers?

## Method

1. **Persona sub-agents.** Seven agents, one per persona already defined in `_prototypes/02_persona-job-review-v3/data/personas.json`: office and administration, technology, skilled trade and operations, healthcare and care, retail/hospitality/service, culinary and food service, career change or early career. Each ran up to three searches relevant to its profession and kept five links.
2. **Browser access: Kimi WebBridge.** The user's own browser, through the local daemon. Each persona had its own session and tab group ("JobHub job search: <persona>"). A shared helper (`code/mcf_search.py`) did the browser steps; agents chose search terms and judged relevance.
3. **Source: MyCareersFuture only.** A government job board with public search pages. LinkedIn, Indeed, Glassdoor and JobStreet were not used, following the earlier research guidance to link out to boards that ban scraping.
4. **Collation.** One list of all captured links: `links_all.json`.
5. **Job details.** `code/mcf_details.py` opened each link in the browser and saved the visible text to `details/`.
6. **Company research.** The prototype-03 `investigate` command, run in Docker, took each unique employer through registry match (ACRA), site discovery (local SearXNG, then verification), page capture, Wayback history, and cited Groq answers to five fixed questions.

## Rules followed

- Read-only browsing: no login, no apply, no clicking beyond loading pages, no form entry.
- Searches and page loads were paced (3 to 6 seconds apart).
- robots.txt checked before every company page fetch. Blocked pages are reported as blocked.
- Browser tabs were left open (closing is the user's call).
- Only public company information is sent to Groq.

## Date

2026-11-01 (Singapore).
