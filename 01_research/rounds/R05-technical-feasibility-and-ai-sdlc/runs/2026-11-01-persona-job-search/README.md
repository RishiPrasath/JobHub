# Round 05 run — persona job search and company research

Status: complete for this pass

Date: 2026-11-01 (Singapore)

## Purpose

Seven job-seeker persona agents search MyCareersFuture in the user's browser (Kimi WebBridge); their links are collated, job details are read, and every employer is run through the new company-research service in Docker.

## Files

- [brief.md](brief.md), [findings.md](findings.md), [limitations.md](limitations.md), [sources.md](sources.md)
- `links/<persona>.json` — what each persona agent kept
- `links_all.json` — all 34 unique links in one list
- `details/` — one JSON per job page, plus pass summaries
- `research/employers.json` — the 34 employers; `research/results.json` — final service output; earlier passes kept as `results_pass1.json`, `results_pass1b_fix.json`, `results_pass2_throttled.json`
- `code/` — search and detail helpers (`mcf_search.py`, `mcf_details.py`)

## Headline

34 jobs, 34 employers: 28 matched exactly to the company registry, 23 official sites found, 21 pages read, 73 supported answers. About 4 of the 23 sites look wrong, and the search source throttled after about two dozen queries.
