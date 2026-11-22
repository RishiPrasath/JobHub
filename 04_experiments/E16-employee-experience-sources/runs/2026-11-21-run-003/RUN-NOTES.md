# E16 run-003 (2026-11-21/22): new sources, live terms, small extraction

Asked by Rishi: "try to scrape the info, if cannot we decide later what to do" (FEAT-008).
Reader: Claude's built-in browser on Rishi's PC (the cloud container and device shell have no internet). One request at a time, at least 5 s apart per host, robots.txt read first, no login, no CAPTCHA or block worked around. No third-party review text saved; only counts, ratings, dates and short notes.

Labels: **verified** = seen live in this run; **inferred** = reasoning from what was seen, or carried from runs 001/002.

## 1. Source classification

| # | Source | robots.txt (read live) | Terms (read live) | Class | Status |
|---|---|---|---|---|---|
| 1 | Glassdoor | Disallows its own terms pages for all agents (run-002) | Not read: robots bars it | Barred, link-out only | inferred (run-002) |
| 2 | Indeed company reviews | n/a | D.21 bars crawling, scraping, AI tools (run-001) | Barred | inferred (run-001) |
| 3 | JobStreet company reviews | n/a | 7(d) bars data mining, robots, scraping (run-001) | Barred | inferred (run-001) |
| 4 | Reddit | n/a | Scraping needs prior written consent; commercial API use needs an agreement (run-002) | Barred | inferred (run-002) |
| 5 | Google Maps reviews | n/a | 3.2.3(a) "No Scraping", no storing (run-002) | Barred for this use | inferred (run-002) |
| 6 | Blind, HardwareZone | n/a | Both bar scraping (run-001) | Barred | inferred (run-001) |
| 7 | **Glints** (glints.com/sg/about/terms, effective 10 Feb 2026) | Allows public pages | Clause (h): users are "prohibited in using screen scraping, data mining, robots or similar data gathering and extraction tools"; content is for "personal non-commercial use" | Barred (also has no real review product) | verified |
| 8 | **NodeFlair** (nodeflair.com/terms-of-service, last updated 29 Apr 2021) | `User-agent: * Allow: /`, `Disallow: /api/v2`; Cloudflare content signal `search=yes, ai-train=no, use=reference`; ClaudeBot/GPTBot etc. disallowed | No clause against automated reading. But: "no copying for any commercial or business use is permitted" and "You must not use any part of the content on our site for commercial purposes without obtaining a licence" | **Restricted**: reading for research not prohibited; any product use needs a licence from NodeFlair | verified |
| 9 | **AmbitionBox** | robots.txt itself returned HTTP 403 "Access Denied" | Not reached | Blocked; stopped | verified |
| 10 | Kununu | Not fetched: browser asked for site approval; DACH-focused, little SG coverage | Not read | Not checked | inferred |
| 11 | Comparably | Allows most pages, disallows review sitemaps | Terms URL returned HTTP 400; US-focused | Not resolved | verified (robots only) |
| 12 | **Great Place to Work** (greatplacetowork.com/terms-and-conditions, modified 29 May 2026; SG site links to these) | SG site: `Disallow:` (nothing) | "you will not use any spider, robot or any other automated mechanism to access the Site"; copies for non-commercial use only | Barred for automation; link-out or manual "certified" fact only | verified |
| 13 | **TAFEP Tripartite Standards adopters** (tal.sg) | robots.txt returns 404 (no rules) | tal.sg/tafep/terms-of-use: no clause on scraping or automation; users must not use information "except for the purposes for which this Website has made such information available" | **Allowed with care**: the list exists to show job seekers which employers adopted the standards | verified (terms), inferred (purpose reading) |
| 14 | Hacker News (Algolia API) | Public JSON API | Not reviewed in depth | Allowed technically, but useless (see below) | verified (counts) |
| 15 | LinkedIn | n/a | Bars scraping (earlier research) | Barred | inferred |

## 2. What extraction returned

### NodeFlair (restricted; research read only, aggregates only)
Data comes from schema.org `EmployerAggregateRating` JSON-LD on each `/companies/<slug>/reviews` page, plus review ages on page 1 (newest first).

| Employer | Reviews | Rating /5 | Website in JSON-LD | Newest review | Status |
|---|---|---|---|---|---|
| Grab | 556 | 4.0 | grab.careers | "over 2 years ago" (oldest ~12 years) | verified |
| DBS Bank | 396 | 3.8 | dbs.com | "over 2 years ago" | verified |
| Singtel | 196 | 3.7 | singtel.com | not read (server timeout) | verified (count) |
| Carousell | 39 | 4.3 | sg.carousell.com | not read (HTTP 524) | verified (count) |
| Sea | 34 | 3.6 | seagroup.com | not read | verified (count) |
| Sheng Siong | 0 | none | none | page says no reviews yet | verified |
| Shopee, Ninja Van | not read | | | requests timed out after 25 s | verified (timeout) |

Findings:
- **Recency fails E16's 24-month window**: for Grab and DBS every review on page 1 is over 2 years old, and the latest interview questions shown are dated July 2024 (verified). Inferred: NodeFlair's review intake largely stopped around mid-2024.
- **Provenance problem**: every review card seen was labelled "From Other Platform" (4 of 4 on each page read; verified). The oldest Grab cards are ~11-12 years old, older than NodeFlair (inferred: imported from another review site, possibly Glassdoor; not confirmed). Even with a NodeFlair licence, the rights to imported reviews are unclear.
- **Coverage is tech-only**: big tech and banks have counts; a large non-tech employer (Sheng Siong) has none (verified for one employer).
- **Reliability of the site**: two of seven page loads timed out and one returned Cloudflare 524 (verified).
- **UEN tie-in**: NodeFlair gives a company name and a website, not a UEN. Matching would go through domain → UEN (the E11 approach). Grab's site is grab.careers, not grab.com, so domain matching needs a manual alias table (inferred).

### TAFEP Tripartite Standards adopters (allowed with care)
The page loads one JSON file, `tal.sg/tafep/api/tal/PageContent/GetTafepTSListing` (~19 MB, one request; verified).
- 60,030 rows = 21,116 organisations; fields: CompanyName, **CompanyUen**, Website, SsicDescription, Programme (10 standards: AFW, FWA, GH, LWW, MFL, RP, SEP, TCE, UCL, WLH), Status, LastUpdatedDate. Every row has a UEN. 60,029 Active, 1 Rescinded. Updates run from 6 Jan 2023 (bulk load) to 20 Nov 2026, so it is maintained (verified).
- Sample employers: DBS Bank Ltd 196800306E (8 standards), GrabTaxi Pte Ltd 201324745D (6), Singapore Telecommunications Ltd 199201624D (10), Carousell Pte Ltd 201300296D (1), Sheng Siong Supermarket Pte Ltd 198304925E (3), Shopee Singapore Pte Ltd 201503526N (2), Ninja Logistics Pte Ltd 201412014E (3), Randstad Pte Ltd 199304055W (1) (verified).
- What it is: an employer's own pledge to follow good practice, checked by TAFEP. **It is not employee experience**, and absence from the list proves nothing.
- UEN tie-in: exact, via CompanyUen (verified).

### Hacker News
Comment hits in the last 24 months: "work at grab" 2; "worked at grab", "worked at shopee", "worked at dbs", "worked at carousell" 0 each (verified). Not a usable source.

## 3. Answer for FEAT-008

- No source both allows automated reading **and** has recent first-hand employee reviews of Singapore employers. Part A stays **fail** for review text.
- NodeFlair is the only review site that does not bar automated reading, but using it in the product needs a licence, its reviews are mostly over 2 years old and imported from elsewhere, and it covers tech employers only.
- The one usable new find is the TAFEP Tripartite Standards list: free, UEN-keyed, current, covering 21,116 employers. It is a "good practice pledge" signal, not reviews.

## 4. Options for Rishi to decide later
1. **Link-out cards** to Glassdoor, Indeed, JobStreet, NodeFlair and Reddit search for the employer, with no copied ratings or text.
2. **TAFEP Tripartite Standards badge** keyed by UEN ("adopted 6 of 10 standards, incl. flexible work and grievance handling"), with a link to TAFEP. Can be built now.
3. **User-pasted reviews**: the user pastes reviews they found; JobHub summarises them for that user only and does not store them.
4. **Ask for permission**: email NodeFlair (support@nodeflair.com) about a licence for aggregate ratings; ask Glassdoor/SEEK about partner access (unlikely, and NodeFlair's imported reviews may not be theirs to licence).
5. **JobHub's own contributions** later (cold start; consent and PDPA design needed).

Not done: Kununu (needs site approval; low SG relevance), Comparably terms (HTTP 400), Shopee/Ninja Van on NodeFlair (timeouts). Classification is an AI reading of terms, not legal advice.
