# Run D findings: company and employer research tools

Date: 2026-11-21. Desk research, no logins. Test company on every tool: Grab. Evidence labels as in the [round brief](../../round-brief.md).

Tools used: WebSearch, WebFetch, and Kimi WebBridge (session `jobhub-r10-company`, read-only). Bot checks on Glassdoor and Teal (Cloudflare) and an Akamai block on AmbitionBox were not bypassed. Interview Query returned HTTP 429; The Org's Grab page was "not found".

Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report. It is a condensed record.

## Per-tool findings

| Tool | Key facts | Label |
|---|---|---|
| **Glassdoor** | Trust page: "employers cannot pay to have reviews removed". Pre-moderates, acts as a "neutral forum" that does not fact-check, keeps old reviews (new content must be within 5 years), will not remove company profiles on request | V-site (WebBridge) |
| | Merged into Indeed Inc. on 2026-07-01; Indeed login now required | V-3p (Reworked, 2026-07-24) |
| | Real names required on profiles since 2024 (Fishbowl and communities added 2023) | V-3p (Fortune) |
| | 12-month give-to-get access | 2nd |
| | Grab Singapore page not read (bot check) | I |
| **Indeed SG** | Grab 3.9 "based on 791 reviews", while the review list shows 132. Sub-ratings shown. Newest review 2026-02-08. Riders and corporate staff blended into one rating. Free | V-site |
| **Blind** | Grab 3.5 from 936 reviews. Content gated behind work-email verification. Anonymity claim disputed | V-site / 2nd |
| **Levels.fyi** | Grab SWE Singapore medians: G3 SGD 116,391 to G6 SGD 331,785, updated 2026-11-20, data-point count not shown. Detail behind "add your salary" or its MCP | V-site |
| | Verification tiers: offer letter, W-2 or pay stub, then work email, then anomaly checks, 12-month window | V-site |
| | Offers a free MCP server and `.md` pages: a possible permitted-source route that E16 did not test | V-site / I |
| **NodeFlair** | SGD salaries with sample size (Senior SWE S$10,070 from 88 points). Its 556 reviews are labelled "From Other Platform" with no platform named; newest page-1 reviews "over 2 years ago". Interview questions dated July 2024. Shows a Glassdoor rating | V-site |
| | Salary sources include payslips and MyCareersFuture | 2nd |
| **AmbitionBox** | Blocked. Owned by Naukri's parent; ML fake-review filtering claims and review-removal complaints; small-sample caveats on pages. No Singapore coverage found | 2nd / I |
| **Crunchbase** | Legal name shown as "Grab Holdings Inc." (holding company, not the Singapore employer). Founding, funding and IPO fields obfuscated. Opaque Growth Score 86 and Heat Score 47 | V-site |
| | Pricing page "not found"; free tier and prices conflict across sources | V-site / 2nd |
| **LinkedIn Premium insights** | 24-month headcount and hiring trend, tenure, top titles, Bing-powered "strategic priorities". Built from profiles with an unspecified minimum. Premium only | V-site (help page) |
| **Layoffs.fyi** | Every entry has a source link; site says it is "likely an undercount". 2025: 122,606 people; 2026 YTD: 149,158. Shows an odd "2027" row. One maintainer | V-site |
| **MOM retrenchment rule** | Employers with 10+ staff must notify retrenchments within 5 working days; no per-company publication found | 2nd / I |
| **ChatGPT / Perplexity deep research** | Wrong or vague citations; no flag for closed postings | 2nd |
| **Teal** | User-entered company notes per job | 2nd |

## Patterns

- Every review site produces a star rating; none shows how fresh or how independent the underlying reviews are. Indeed's headline count (791) and visible list (132) disagree; NodeFlair imports reviews from an unnamed platform.
- Ownership concentration: Glassdoor and Indeed are now one company, so they are not independent sources.
- No tool maps a brand to the Singapore employing entity. Crunchbase returns the US holding company.
- Pay data is the strongest category (Levels.fyi, NodeFlair), with sample sizes on NodeFlair only.
- Paywalls and gates are common: give-to-get, work-email verification, Premium-only insights.

## Table stakes users expect

1. One company page combining ratings, reviews, salaries and interviews.
2. Pay by role and level in SGD, with sample size.
3. Interview process and questions by role.
4. Basic identity and size facts: HQ, size band, industry, funding or listing status.
5. A growth or shrinkage signal (headcount trend, layoffs), with free entry-level access.

## Gaps JobHub could own

1. Quoted, dated, attributed facts as the unit of research, with no star ratings.
2. Mapping the brand to the Singapore employing entity (ACRA UEN). No competitor found does this.
3. Freshness and independence labels: newest-item date, count in the last 24 months, shared-owner flag.
4. Link-out cards with honest access notes ("user-generated, gated, last review 2024"), consistent with E16's no-summarising result, with official Singapore lookups shown separately.
5. An explicit "not found", and research stored per job so it can be re-checked later.

## Limitations

- One large test company only. Small-company coverage, which matters most for scam risk, was not tested.
- Glassdoor, AmbitionBox and Teal facts are second-hand.
- Prices conflict across sources.
- The WebBridge browser may carry the owner's own sessions, so some views may differ from a logged-out user's.
