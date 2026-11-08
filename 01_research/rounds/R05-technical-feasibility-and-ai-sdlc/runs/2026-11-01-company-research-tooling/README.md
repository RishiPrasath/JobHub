# Round 05 run — company and role research tooling

Status: experiments E1 to E5 and E7 run; Tavily untested; no Docker image built

Date: 2026-11-01 (Singapore)

## Purpose

Find the freest and easiest-to-set-up way to research a company and a role as a service inside JobHub, by re-checking pricing and terms and running small experiments on 15 postings.

## Files

- [brief.md](brief.md) — question, experiments, rules
- [findings.md](findings.md) — claim check, results, recommended stack
- [limitations.md](limitations.md) — what was not shown
- [sources.md](sources.md) — pricing/terms pages and data sources
- `data/postings.json` — the 15-posting set
- `code/` — one script per experiment (run with `python -I`; Playwright script needs the `_prototypes/02_persona-job-review-v3` `node_modules`)
- `outputs/` — raw JSON and console logs per experiment; `outputs/pages/` holds captured page text

## Headline

A $0, no-card stack worked end to end for identity (ACRA bulk data), pages (plain fetch), site history (Wayback) and extraction (Groq with citation checking), but not for news (GDELT throttled) or hosting (Cloud Run needs billing). Site discovery works for large employers through Wikidata and fails for small ones, where only a search API (Tavily's recurring free tier) could help; that is untested.
