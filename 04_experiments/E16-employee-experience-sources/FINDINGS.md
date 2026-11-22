# E16 findings: employee-experience sources (run 001, 2026-11-10)

Written by the coordinator from the specialist's report, because the specialist could not save files named as reports. The underlying records are in `protocol/` and `runs/2026-11-10-run-001/outputs/`.

## Status

Part A ran and **failed** its proposed threshold. Part B was not run, because no source was permitted. Part C was not run (conditional on A and B passing, and it needs participants). No Groq calls were made. Only terms pages, `robots.txt` files and API documentation were fetched. No review page was fetched and no accounts were counted.

## Thresholds and results

| Threshold (frozen before any fetch) | Observed | Verdict |
|---|---|---|
| Part A pass: at least one source permitted for the intended use (read and summarise with attribution) | 0 of 8 existing external sources qualify | **Fail** |
| Part B pass: at least 5 first-hand accounts from the last 24 months for at least half of 20 employers; fail under 25% | Not run, no permitted source | Not run |
| Part C pass: at least 75% understand a summary reflects individual accounts; fail under 50% | Not run | Not run |

## Part A: source classification

| Source | Class | Basis |
|---|---|---|
| Indeed | Link-out only | Terms (D.21) bar crawling, scraping, reproducing and AI or automated tools without written permission |
| JobStreet | Link-out only | Section 7(d) bars data mining, robots and screen scraping without written consent |
| Blind | Link-out only | Section 3 bars scraping and copying without explicit permission, automated or manual |
| HardwareZone | Link-out only | Section 4.2 bars scrapers and reproducing content elsewhere |
| Glassdoor | Link-out only (provisional) | HTTP 403 on all four terms and developer URLs; `robots.txt` was read; the terms position rests on secondary reports |
| Reddit | Not permitted (provisional) | The fetch tool could not reach the host; commercial use reportedly needs a separate agreement (secondary only) |
| Google Maps reviews via Places API | Not permitted for the intended use | Up to 5 reviews per place; terms say reviews may not be copied and saved; paid; mostly customer reviews; AI review summaries not listed for Singapore |
| TAFEP and MOM | Not a lived-experience source | They hold no first-hand accounts. Regulator records belong to E14. |
| Licensed or partner data | Unresolved | No provider was contacted. Glassdoor's partner API reportedly closed to new applicants in 2021 (secondary). |
| Job-seeker contributions | Permitted in principle | Not an existing source; no coverage at launch |

The strict reading of Part A counts external sources only. If job-seeker contributions counted, Part A would pass on paper, but Part B would start near zero.

## Part B employer list

The 20-employer list (6 large, 6 mid-size, 5 small, 3 agencies, 10 drawn from the E09 personas) was frozen so a later run can reuse it. Small-employer sizes are unverified. No counts exist.

## Deviations

- The fetch tool returns a model-written extract, not the raw page, so quoted terms are as that tool reported them.
- Primary terms could not be read for Glassdoor, Reddit and the full Google Maps Platform terms.
- The Indeed terms were read through about 86% of their length.
- JobStreet's terms date disagrees between sources (20 July versus 21 April 2026).
- Thresholds and the employer list are frozen by file hash and not committed to git, since commits were not requested.
- Kununu, AmbitionBox, Comparably, LinkedIn, and Singapore copyright and PDPA law were not examined.
- The classification is an AI reading of terms, not legal advice.

## Limitations

- No coverage figures exist for any site.
- Whether showing only a rating number copied from a review site is allowed was not tested.
- Several classifications are provisional until a human checks the primary terms.

## Feasibility recommendation for FEAT-008

**Narrow to link-out cards.** On current evidence no existing external source can be read and summarised lawfully for this purpose, and E09 found that search-snippet ratings were sometimes plainly wrong. A build that reads or summarises review text is **not supported**. A link-out card (pointing the user to the right sites without copying ratings, snippets or review text) is not blocked by these terms but has not been tested for usefulness.

Proposed feasibility level: T2 (a survey result, not a working pipeline). `result: fail` is confirmed for any build that reads review text. No change to the need level.

## Still needs real participants or a human

- Whether job seekers find link-out cards useful (not tested).
- A human check of the Glassdoor, Reddit and Google Maps classifications against their primary terms.
- Any licence enquiry to a review provider.

## Next actions and owner decisions

1. Accept narrowing FEAT-008 to link-out cards, or park it.
2. Decide whether job-seeker contributions count toward Part A.
3. Decide who, if anyone, contacts Glassdoor or SEEK about a licence, and on what budget.
4. Have a human confirm the provisional classifications.

## Run-002 (2026-11-21): primary terms re-read with the Clearcote browser

See `runs/2026-11-21-run-002/RUN-NOTES.md`. Reddit's User Agreement and Data API Terms and the Google Maps Platform terms were read in full from the rendered pages. Reddit is now "not permitted" on primary text (scraping needs prior written consent; commercial API use needs a separate agreement). Google Maps stays "not permitted for the intended use" (no storing or rehosting outside the Services). Glassdoor was not read: its robots.txt disallows its terms and developer pages for all agents, so a human has to read them. Part A stays **fail**; no level change.

## Run-003 (2026-11-21): new sources and small extraction

See `runs/2026-11-21-run-003/RUN-NOTES.md`. New sources read live: Glints (barred, clause h), Great Place to Work (barred, no robots or automated access), AmbitionBox (robots.txt returns 403), NodeFlair (automated reading not barred, but commercial use needs a licence), TAFEP Tripartite Standards adopters (no automation clause; robots.txt 404). NodeFlair aggregates for 6 employers: newest Grab and DBS reviews are over 2 years old, cards are labelled "From Other Platform", and non-tech coverage is empty (Sheng Siong 0). TAFEP list: 21,116 organisations with UEN, maintained to 20 Nov 2026, but it is an employer pledge, not employee experience. Part A stays **fail** for review text; a UEN-keyed Tripartite Standards badge is buildable now.
