# E22 protocol: Singapore company entity sources

Written 2026-11-21 before the matching and chain runs. Thresholds below were set before scoring. Not committed to git before the run (owner asked for no commits), so the order is shown only by file times.

## Question

Can free, legally usable sources take a brand name or a domain from a job posting to the right ACRA entity (UEN), and how often is a name-only match ambiguous or wrong?

## Sources and access rule

From [DRAFT_sg-company-data-free-legal-sources.md](../../../strategy/evidence/external/DRAFT_sg-company-data-free-legal-sources.md). Each source's terms page and robots.txt are read first (step 0, `outputs/terms/`). A source is automated only where both allow it. A block on a forbidden source is the result; it is not worked around. On permitted sources, a JS-rendered page is read with Patchright (real Chrome, headed); a CAPTCHA or login wall stops the step and is recorded.

| Part | Source | Volume cap |
|---|---|---|
| A | ACRA "Entities Registered with ACRA" via data.gov.sg datastore API (no key) | At most 1 call per 3 s (limit is about 4 per 10 s), under 80 calls |
| B | Government Gazette (egazette.gov.sg) browse pages | Under 15 page loads, 5 s apart; `/search` is disallowed by robots.txt and not used |
| C | SGNIC RDAP, crt.sh, Wayback availability API | One lookup per domain per service, 5 s apart |
| D | MyCareersFuture job API | Only if the terms read in step 0 permit it |
| E | Company websites (own home page plus one privacy or terms page) to set truth | 2 page loads per company, robots respected |

## Sample

20 real Singapore employer brands chosen by the agent for spread: multi-entity groups (Grab, Shopee, DBS, Singtel, CapitaLand, ST Engineering and others), retail and F&B chains, and startups. Plus 6 constructed lookalike names (a real brand plus a plausible suffix, such as "Grab Recruitment Pte Ltd"), whose correct answer is "no such entity" or "not the brand's employer".

## Ground truth

For each brand, the legal entity named on the brand's own Singapore website (privacy policy, terms or footer), read in Part E, then confirmed in ACRA by exact name or by UEN. Registry mirror sites are not used. Where the site names no entity, truth is "unknown" and the brand is kept. The agent sets truth and runs the matcher, so truth and method are not independent (limitation).

## Measures

- Ambiguity: number of ACRA entities whose name contains the brand token; number of live (Registered or Live) entities among them.
- Naive name match top-1: pick the live entity whose name equals "BRAND PTE. LTD.", else the shortest live name containing the brand. Correct if it equals truth by UEN.
- Truth in candidates: the true entity appears in the brand's search results.
- Lookalikes: a lookalike name accepted by exact ACRA match (dangerous) versus not found.
- Chain coverage: share of domains where RDAP, crt.sh (OV or EV organisation name) or the site itself gives a legal name or UEN that maps to ACRA.

## Thresholds (set before scoring)

- Name-only matching is **usable alone** if naive top-1 is correct for at least 90% of brands with known truth and no lookalike is accepted. Otherwise it needs a second signal.
- The domain chain is **usable as the second signal** if it yields an ACRA-matched entity for at least 70% of domains.
