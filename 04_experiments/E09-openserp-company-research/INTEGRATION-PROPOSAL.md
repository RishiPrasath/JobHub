# Proposal: where company research plugs into job-posting analysis

Short, and a proposal only. Nothing here is built. It follows from [REPORT.md](REPORT.md).

## Principle

Say what could not be verified. Never turn "I could not read it" or "I found nothing" into "no problems". Every output carries what was checked, what was blocked, and what is unknown.

## Flow

```
job posting (employer name, optional company ID, optional URL)
        |
 1. REGISTRY CHECK            existing /check service: exists? which entity? live? lookalike?
        |                      verdicts: confirmed, probable, multiple_entities, similar_name_only,
        |                      registered_not_active, uen_name_mismatch, public_body, not_in_registry
        |
 2. DECIDE WHAT WEB RESEARCH MAY SAY
        |   confirmed / probable      -> research the registered legal name AND the brand name
        |   brand-only (registry can't confirm: Grab, Ninja Van, KPMG here) -> research, mark "brand, legal entity not confirmed"
        |   similar_name_only / not_in_registry -> research only to look for scam reports, never to build a positive profile
        |   registered_not_active / uen_name_mismatch -> report it prominently, research optional
        |
 3. SEARCH (OpenSERP, DuckDuckGo first, Bing/Google as fallback)
        |   entity-aware queries: legal name, brand, "scam", "layoffs", "reviews", "interview"
        |   per-user and global query budget; cache for an hour; breaker state read from /stats/cb
        |
 4. READ (allow-listed sources only)
        |   company site, news, registry aggregators, review sites that permit it
        |   never: LinkedIn, Glassdoor, Reddit (unreadable or restricted); link out instead
        |   every page: strip images, challenge-text check, minimum real text, mentions the name
        |
 5. NAME GATE (code)          exact posting name in a page or a search result, else no "appears real"
        |
 6. BRIEF (model)             numbered sources, a quote per claim, quotes verified in code
        |
 7. OUTPUT                    verdict + facts + red flags (each cited or marked unverified)
                              + "could not read" list + "could not verify" list + registry date + disclaimer
```

## Failure handling: report, never guess

| Situation | What the system does | What the user sees |
|---|---|---|
| Registry service down | Skip step 1, do not run step 5's positive wording | "Company registry check unavailable." No "confirmed". |
| Employer not in registry | Search only for scam reports | "No registered company with this exact name. Closest: X." |
| Posting company ID does not match the name | Stop and show it | "The ID belongs to a differently named entity." |
| Search service down or all engines blocked/open breaker | No web brief | "Web research unavailable now." Not "no red flags found". |
| One engine blocked | Fall back to the next engine, record which answered | Nothing, unless all fail |
| Page unreadable (Glassdoor 502, Reddit challenge, login wall, thin) | Mark source failed, keep the search snippet flagged "snippet only" | Listed under "could not read", with the site name |
| Exact name never appears | Cap at "inconsistent or suspicious" or "cannot verify" | "Evidence describes a similarly named company." |
| Model quote not found in source | Claim kept but labelled unverified | "Unverified" tag |
| Model or rate limit failure | Retry once, then return the sources with no brief | "Summary unavailable; here are the sources." |
| Time budget exceeded | Return what was gathered | "Partial: N of M sources read." |

## Build order

1. Wire step 1 and the output wording (days; the registry service and `/check` exist).
2. Move the entity gate and the page checks from this experiment's harness into the pipeline, with tests for the lookalike, fictitious and brand-name cases used here.
3. Add step 3 and 4 with the allow-list, behind a feature flag and a per-user query budget.
4. Re-run the eight-persona test plus 20 new companies chosen before looking at results, to get an unbiased number.

## Open decisions for the product owner

- Is a private, low-volume deployment acceptable, or does this need to scale? At scale the search step needs a licensed API, not scraped result pages.
- Which review sites may be read? The honest default is none beyond those whose terms permit it, with a link out instead.
- Should an unverifiable employer be shown as "unverified" or held back? This proposal shows it, with the reason.
