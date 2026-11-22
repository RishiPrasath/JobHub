# Scraping job portals while logged out: legal note

Date: 2026-11-21. Desk research answering an owner question during the R10 must-have review. **Not legal advice.** Labels: V = source read directly; P = partly verified; U = unverified.

## United States

| Point | Finding | Label | Source |
|---|---|---|---|
| Meta v. Bright Data (N.D. Cal., 23 Jan 2024) | Summary judgment for Bright Data on contract claims: Meta's terms bind account holders, and logged-out scraping of public data was "unrelated to the purpose of its accounts". Survival clause did not bind Bright Data after it closed its accounts. | V | https://blog.ericgoldman.org/archives/2024/01/game-on-bright-data-scores-major-victory-in-web-scraping-dispute-with-meta-guest-blog-post.htm |
| Meta drops case | 23 Feb 2024: Meta dismissed remaining claim without prejudice and gave up its appeal. | V | https://techcrunch.com/2024/02/26/meta-drops-lawsuit-against-web-scraping-firm-bright-data-that-sold-millions-of-instagram-records/ |
| hiQ v. LinkedIn, 9th Cir. April 2022 | CFAA "without authorization" likely does not apply to a public site that "has erected no gates to lift or lower". Preliminary-injunction ruling, not final merits. | V (opinion PDF) | https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/18/17-16783.pdf |
| hiQ, Nov 2022 | hiQ breached the User Agreement through scraping and fake accounts; it had agreed to the terms when creating a corporate account. Order itself not read. | P | https://www.zwillgen.com/alternative-data/hiq-v-linkedin-wrapped-up-web-scraping-lessons-learned/ |
| hiQ settlement, Dec 2022 | $500,000 consent judgment; permanent injunction on scraping "whether logged in or not"; delete data and code. | V | https://newmedialaw.proskauer.com/2022/12/08/hiq-and-linkedin-reach-proposed-settlement-in-landmark-scraping-case/ |
| X Corp v. Bright Data (May 2024) | Contract claims dismissed as preempted by the Copyright Act, with leave to amend. | U (search result only) | https://skadden.com/insights/publications/2024/05/district-court-adopts-broad-view |
| LinkedIn User Agreement s8.2 | Bans scraping via "crawlers, browser plugins and add-ons" and "bots or other unauthorized automated methods". | V | https://www.linkedin.com/legal/user-agreement |

## Singapore

| Point | Finding | Label | Source |
|---|---|---|---|
| Computer Misuse Act s3 | Scraping "may be illegal" under s3; "appears to be no local cases". | P (legal guide, not statute) | https://singaporelegaladvice.com/law-articles/legal-scrape-crawl-websites-data-singapore/ |
| Copyright Act 2021 ss243/244 | Computational data analysis exception needs lawful access; IPOS official: circumventing a paywall or breaching terms of use is not lawful access; exception cannot be removed by contract. | P (secondary) | https://www.asiaiplaw.com/article/computational-data-analysis-exception-in-singapores-copyright-act-2021-a-game-changer |
| PDPA | Publicly available data exception can generally be relied on; data behind logins or paywalls needs separate assessment (PDPC advisory guidelines, 31 July 2026; not binding). | P (secondary) | https://www.hlc.com/en/publications/singapores-pdpc-finalises-guidance-on-the-use-of-personal-data-in-generative-ai |
| Case law | No Singapore scraping decision found; 99.co v PropertyGuru concerned manual copying of listing photos. | P | Reed Smith summary (search) |

## Unsettled

- Whether site terms bind logged-out visitors who never accepted them (Meta's judge noted Meta could rewrite its terms).
- The CFAA position is a preliminary 9th Circuit view; other US circuits may differ.
- How far copyright preemption (X Corp) spreads.
- Whether CMA s3 covers logged-out scraping after technical blocks or a cease-and-desist.
- Whether breaching terms while logged out defeats "lawful access" under s244.
- How the PDPA exception applies to personal data on job portals (recruiter names).

## Implication for JobHub

The search-link builder plus paste or a single user-chosen URL avoids these questions. Any future aggregation would need a proper legal review.
