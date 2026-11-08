# Run brief

## Research question

What is the freest and easiest-to-set-up stack for a JobHub service that researches a company and a role from public sources, and which parts of it hold up when run on a real posting set?

## Context

The earlier 4-agent options report (`research\2026-11-01-company-research-tooling-options.md`) was not available in the repository, so this run redoes the work from first principles: re-check pricing and terms pages, then run small experiments. The feature definition and its smallest experiment come from [the company and role research service idea](../../../../../03_features/source-ideas/01_company-and-role-research-service.md).

## Posting set (15 postings, 5 industry groups)

`data/postings.json`. Seven postings come from the prototype-02 link set, one from fixture R4-JB-011, and seven were added to cover large employers, a public institution, a co-operative, a group company and a staffing agency. Only employer name, title and industry are used. Posting text itself is not an input to these experiments.

## Experiments

| ID | Question | Tool tested | Script |
|---|---|---|---|
| E1 | Can the employer be resolved to a legal entity for free? | ACRA open data (live API, then bulk CSV) | `code/e1_*.py`, `code/e1a_*.py`, `code/e1b_*.py` |
| E2 | Does plain HTTP plus robots.txt retrieve usable company pages? | stdlib HTTP, `robotparser`, HTML + JSON-LD extraction | `code/e2_fetch_plain.py` |
| E3 | Does a headless browser add anything over plain fetch? | Playwright (Chromium, no stealth) | `code/e3_playwright_render.mjs` |
| E4 | Can site age and recent news be obtained for free? | Wayback CDX, GDELT DOC 2.0 | `code/e4_history_news.py` |
| E5 | Does numbered-excerpt citation plus code-side quote checking reduce unsupported claims? | Groq `openai/gpt-oss-120b`, strict JSON schema | `code/e5_groq_grounded_extraction.py` |
| E7 | Can official sites be found without a search API? | Wikidata search + P856 | `code/e7_wikidata_website_discovery.py` |
| E6 | What does the whole chain yield per posting? | Composite of E1 to E5, E7 | table in `findings.md` |

**Tavily and Serper were not run.** Both need an account and API key, which the user must create, and the user then ruled out cards and one-time credits (leaving Tavily's recurring free tier as the only API candidate). Official sites for E2 to E4 were found with the assistant's own web search, which is not a candidate provider; it only shows how often an official site exists to be found.

**User constraints added mid-run:** strictly free, no card, no credits, mostly scraping, runs in a Docker container, local hosting.

## Rules followed

- Public pages only; no login, no CAPTCHA handling, no stealth or user-agent spoofing.
- robots.txt checked before every page fetch; connection resets reported as blocked, not retried by other means.
- No accounts created, no card used, no secrets printed or committed (`.env` is git-ignored and was only read by the Groq script).
- No claim about any employer's quality or legitimacy is made.

## Date

2026-11-01 (Singapore).
