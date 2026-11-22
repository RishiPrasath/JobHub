# E14 run-002 (2026-11-21): retry of unreadable sources with the Clearcote browser

Retries only what run-001 could not read: SGX (Part A) and the Part B cited pages that returned HTTP 403. No model calls. run-001 outputs are untouched.

- Reader: `tools/clearcote_reader.py` 0.1.0 on the Clearcote open build (Chromium 151.0.7922.108, SDK 0.70.1, no key, headless). robots.txt first; at least 5 s per host (or Crawl-delay); one attempt per URL; HTTP 401/403/429 and challenge pages are recorded and not worked around. Terms are read before any content page.
- Harness: `harness/clearcote_rerun.py` (stage `terms`, then `content` by label). Log: `outputs/reads.jsonl` (the first terms pass hit a transient network error on SGX robots.txt and was repeated; both passes are logged). Page text: `outputs/raw/`.

## Part A: SGX

| Item | run-001 | run-002 |
|---|---|---|
| SGX Terms of Use (sgx.com/terms-use) | Body did not render (884 characters), terms unread | **Rendered and read** (HTTP 200, 135,170 characters; sha256 in `reads.jsonl`). robots.txt: Allow all |
| What the terms say | Unknown | Personal, non-commercial viewing only; no copying, storing or reproducing Materials without written permission; section 4 "Prohibition on Data Scraping and AI Model Training" bars automated scraping, data mining, bots or extraction tools to capture content for AI systems or "any other form of data analysis software" without SGX's prior written consent |
| SGX Data Direct terms | No text | Not fetched: datadirect.sgx.com robots.txt returns HTTP 403, treated as disallow all |
| SGX company announcements list | Rendered "Loading...", no list | **Not fetched, by design**: the terms now read forbid this use without SGX's written consent |

Class change: SGX moves from NR (not readable, terms unread) to **R-NP** (readable, not permitted for automated use). Part A verdict unchanged: narrow pass on the MOM lists.

## Part B: cited pages that returned HTTP 403

| Citation | run-001 | run-002 |
|---|---|---|
| ComplaintsBoard (O04, three pages) | HTTP 403 | Not fetched: complaintsboard.com robots.txt returns HTTP 403 (disallow all); its terms page is also excluded |
| Robert Walters Malaysia fraud alert (O10) | HTTP 403 | Not fetched. robots.txt allows it, but the site's terms page could not be located (two guessed URLs returned 404), and run-001's 403 was the site refusing an automated reader. Retrying through a fingerprint-masking browser would work around that refusal, so it was left for a human to open |

Part B unsupported-claims check stays **weakly verified** (3 cited pages checked). Part B recall verdict unchanged: fail (20%).
