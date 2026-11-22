# E16 run-002 (2026-11-21): primary terms re-read with the Clearcote browser

Part A only. Same method rule as run-001: terms, robots and developer pages only; no review, company or forum page fetched. No Groq calls.

- Reader: `tools/clearcote_reader.py` 0.1.0 on the Clearcote open build (Chromium 151.0.7922.108, Python SDK `clearcote` 0.70.1, no licence key, headless, one fixed fingerprint seed). robots.txt checked first for `*` and `JobHubResearch`; at least 5 s between requests to a host; one attempt per URL; blocks recorded, not worked around.
- Harness: `harness/clearcote_terms_read.py`. Log: `outputs/reads.jsonl`. Page text: `outputs/raw/*.txt` (third-party text; see SCOPE decision 6 before committing).
- Why rerun: run-001 used a fetch tool that returned model-written extracts and could not open Glassdoor (HTTP 403), Reddit (host unreachable) or the full Google Maps Platform terms. This run reads raw rendered text.

| Source | run-001 | run-002 | Classification change |
|---|---|---|---|
| Glassdoor terms, legal and developer pages (4 URLs) | HTTP 403, NOT READ | Not fetched: Glassdoor's robots.txt disallows `/about/terms/`, `/legal/` and `/developer/index.htm` for all agents | None. Still provisional; a human must read the terms in a normal browser |
| Reddit User Agreement | Host unreachable, secondary only | Read (HTTP 200). Bars collecting data "by any means (automated or otherwise)" except as permitted; crawling only per robots.txt, and scraping without Reddit's prior written consent is prohibited | Not permitted, now on primary text (was provisional) |
| Reddit Data API Terms | Secondary only | Read. Commercial use, or any use not expressly permitted, needs a separate agreement; no deriving revenue without written approval; no retaining User Content beyond the approved use case | Confirms: needs an agreement with Reddit |
| Google Maps Platform Terms, Service Specific Terms, Places policies | Partly read | Read. Terms 3.2.3(a) "No Scraping": no pre-fetching, indexing, storing or rehosting Google Maps Content outside the Services; general restrictions include creating derivative works. Places policies allow showing reviews only with author attribution and a link to the source review | Not permitted for the intended use (store and summarise); unchanged, now on primary text |

Part A verdict: unchanged, **fail** (0 external sources permitted for the intended use). The rerun turned two provisional classifications (Reddit, Google Maps) into primary-text ones. Glassdoor stays provisional because its own robots.txt excludes automated reading of its terms.

Requests: 9 URLs attempted, 5 page loads, plus robots.txt reads. Clearcote also made one geo-IP lookup at launch (it does this to set timezone and language).
