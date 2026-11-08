# Round 05 run — free scraping tools and a containerised service

Status: complete for this pass (survey, benchmark, service built and tested)

Date: 2026-11-01 (Singapore)

## Files
- [brief.md](brief.md) — plan, criteria, method
- [findings.md](findings.md) — survey, benchmark, recommendation
- [limitations.md](limitations.md), [sources.md](sources.md)
- `code/` — GitHub survey (`s1_github_survey.py`), benchmark harness (`bench.py`, `run_bench.sh`), throwaway stack (`docker-compose.bench.yml`)
- `data/urls.json` — the 25 benchmark URLs
- `outputs/` — raw results per tool (`b_*.json`), summary, memory samples, logs

## Headline
Plain fetch handles most homepages in about 0.3 s but nothing on JavaScript job pages. Playwright rendered every page that loaded. Crawl4AI is the best ready-made service, Lightpanda the lightest (AGPL; full on job pages once waits are set). Recommendation: plain fetch first, then a Playwright render service. The wrapper is built in `05_prototypes/P04-fetch-render-service` and passed the same 25 URLs and basic hardening checks.
