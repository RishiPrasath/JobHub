# Query and sampling plan for the next pass

## Purpose

The next pass should reduce convenience-sample bias and test whether the current field taxonomy holds across source types, occupations and industries. It should not broaden into general job-search research without a separate brief.

## Source strata

### 1. Job-board details

Use the expanded AgentHub coverage registry rather than limiting the run to the initial six ecosystems. The primary accessible candidate set currently includes Indeed Singapore, Jobstreet Singapore, MyCareersFuture, FastJobs, Careers@Gov, JobsCentral, foundit Singapore, NodeFlair, eFinancialCareers Singapore, Michael Page Singapore, Wellfound, YC Jobs, GovTech Careers, DSTA Careers, CSA Careers, MDDI Career Options and A*STAR Careers. Add comparable detail pages across:

- office/professional;
- frontline/retail/food service;
- logistics/driving/warehouse/trade;
- regulated, public-service or credential-led work where available.

Do not treat this as one undifferentiated list. Sample at least:

- four general/multi-sector boards;
- three specialist, recruiter or startup sources;
- three public-sector/statutory-board sources;
- two employer/ATS sources;
- two degraded or blocked outcomes recorded separately.

### 2. Public-service and employment-support pages

Sample event-based listings, career-conversion programmes, vacancy PDFs and public-service landing pages separately from ordinary job details. Do not count them as the same page type.

### 3. Employer and ATS pages

Add direct-employer, Workday, Greenhouse/Careers@Gov, healthcare, recruitment-agency and talent-pool pages. Record the underlying system only when the page itself supports the identification. Do not count an employer/ATS page as an independent board if it is a copy of a board listing.

### 4. AgentHub route outcomes

Use [coverage-registry.md](coverage-registry.md) as the source-selection ledger. A route marked readable is eligible for a Chrome detail-page inspection; readable-but-short, redirecting or no-JSON routes require manual review; blocked routes remain evidence of access limitation only.

### 5. Variants and failure states

Include search results, employer profiles, open applications/talent pools, application interstitials, downloadable vacancy documents, expired/closed pages and blocked/shell pages.

## Query families

- `[board] Singapore [occupation] salary requirements application`
- `[board] Singapore [frontline/trade role] shift allowance licence`
- `[board] Singapore [regulated role] registration qualification closing date`
- `site:[employer ATS] Singapore [role] responsibilities requirements benefits`
- `site:[board] Singapore [role] "what we are looking for"`
- `site:[board] Singapore [role] "how to apply"`
- `site:[board] Singapore [role] expiry OR closing OR updated`
- `site:[board] Singapore [role] allowance OR commission OR "up to"`
- `site:[board] Singapore expired job repost help`

Queries are discovery aids only. The final evidence record must cite the direct page opened and distinguish search result context from detail-page content.

## Minimum next-pass target

- 16 board detail pages across at least 10 distinct board, specialist, agency or public-sector ecosystems;
- 8 employer/ATS detail pages;
- 5 public-service/support/event/PDF pages;
- 6 page-type variants;
- 3 unavailable, expired, blocked or shell outcomes logged.

This produces a bounded 38-record matrix. Ensure at least eight contexts are represented and at least two source types are available for each context where feasible. Use at least one detail page from each selected source family, then repeat four source families to test within-source variation. Keep the accessible candidate set separate from the degraded/blocked/manual-only set.

## Quality controls

- Keep a duplicate cluster for syndicated copies.
- Record exact URL, final URL, canonical URL if shown, access time/timezone and browser method.
- Preserve raw labels, raw compensation wording and conditions.
- Mark ownership at field level where practical.
- Separate not present, not visible, inaccessible and unknown.
- Record contradictory values rather than choosing one silently.
- Do not use snippets or stale cached text as detail-page evidence.
- Stop collection if access restrictions make further pages non-comparable; report the gap.
