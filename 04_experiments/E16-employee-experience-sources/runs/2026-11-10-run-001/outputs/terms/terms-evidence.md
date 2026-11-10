# Terms and policy evidence log (raw record, 2026-11-10, not edited after the run)

Fetch tool: WebFetch (returns a model-written extract of the page). Short phrases only are quoted. Dates are as stated by the page or tool. "NOT READ" means the primary text could not be retrieved.

## 1 Glassdoor
- https://www.glassdoor.com/about/terms/ : HTTP 403. NOT READ.
- https://www.glassdoor.com/legal/terms-of-use : HTTP 403. NOT READ.
- https://www.glassdoor.sg/about/terms/ : HTTP 403. NOT READ.
- https://www.glassdoor.com/developer/index.htm : HTTP 403. NOT READ.
- https://www.glassdoor.com/robots.txt : read. Individual review pages, paginated review/interview pages and filtered URLs are disallowed for generic agents. Many named AI/crawler bots (GPTBot, ClaudeBot, anthropic-ai, CCBot, Diffbot, others) are disallowed, some fully, some with exceptions for /blog/, /About/, /employers/. The terms path itself is disallowed. The file has no terms statement.
- Secondary (WebSearch summary, not Glassdoor's text): trackers quote a clause barring "robot, spider, scraper, data mining" tools "without our express written permission"; commentators disagree whether this reaches logged-out public pages. A conductatlas.com page for the clause says it is "no longer published" and shows no text, so it gave no usable quote. One secondary source cites a Terms revision dated July 1, 2026 (unverified).
- Secondary on API: the public partner API stopped taking new applications in 2021; access is now enterprise/sales-led (ATS, programmatic recruitment, employer-brand partners); legacy data was aggregates (ratings, salaries), not per-review text. Resellers (Bright Data, Oxylabs, Decodo and others) sell scraped Glassdoor datasets. None of this was verified from Glassdoor.

## 2 Indeed
- https://www.indeed.com/legal : read in chunks covering about 86 percent of the 348,998 characters (0 to 300,000), plus a fifth call on the remainder that returned only affiliate and data-processing text. Terms updated September 29, 2026 (as stated by the tool).
  - Section D.21 (Site Rules): may not "crawl, scrape, extract data from, reproduce, duplicate, copy" the Site; no "automated system (bots, scrapers, spiders, AI or Agentic AI)" without express written permission; no accessing the Site to develop or train AI/ML models; crawling "conditionally" permitted "solely as outlined in our robots.txt file"; no access "other than the public interfaces provided by Indeed".
  - Section D (IP): Indeed owns "compilations of information available through the Site". Reviews, ratings and answers "may be displayed publicly on the Site".
  - Section A: Site use is for a "personal, non-commercial purpose of seeking employment".
  - Section C (APIs): API use is monitored and limited; on cancellation delete "all User Content acquired through the Site or API". The API terms found cover Indeed Ads/Apply/plugins; no review-data API was found in the text read.
  - Section 22.4: the scraping and bot prohibitions apply to third-party AI platforms.
- https://www.indeed.com/robots.txt : read. For generic agents only /cmp/*/write-review and a few other /cmp paths are blocked; review pages are not blocked. Named training bots (GPTBot, ClaudeBot, anthropic-ai, CCBot) have Disallow /cmp/. GoogleOther has Disallow /. A robots.txt that allows a path does not override the terms' ban on reproducing content.

## 3 JobStreet (SEEK)
- https://sg.jobstreet.com/terms : read. "Website Terms and Conditions", last updated 20 July 2026 per the fetch (a search snippet said 21 April 2026; the dates disagree and the fetched page is taken as current).
  - 7(d): "data mining, robots, screen scraping" prohibited "except with our prior written consent".
  - 7(b)(ii) and (iii): no "aggregating, copying or duplicating" Content; no "reproducing any of the Content for general use".
  - 5(c): Content for "personal, non-commercial purposes". 7(c): no "unauthorised commercial use".
  - 9(b): sites "designed for individual human use"; automated access only via a specific interface "such as an API"; no public API for company reviews was found.
  - 11(f): public User Content may be accessed, stored and reproduced by other Users for personal use (users, not services).
  - The extract says the terms do not address company reviews specifically.
- https://sg.jobstreet.com/robots.txt : read. Generic agents: query-string URLs, /graphql and /api/jobsearch/ blocked; /companies not named. AI bots (anthropic-ai, GPTBot, CCBot, others) disallowed from /companies.

## 4 Reddit
- https://www.reddit.com/robots.txt and https://www.redditinc.com/policies/data-api-terms : the fetch tool is not permitted to fetch these hosts. NOT READ.
- Secondary (WebSearch; vendor and blog pages, not Reddit's text): Data API Terms reportedly require a separate agreement for commercial use; the free tier is non-commercial (about 100 requests per minute via OAuth); a commercial price of about 0.24 USD per 1,000 calls is widely quoted but sources disagree and no official table was seen; the User Agreement reportedly bars scraping without prior written consent. All unverified.
- E09 (repo evidence): Reddit returned a bot challenge reported as success.

## 5 Blind
- https://www.teamblind.com/terms and /terms-of-service : HTTP 404. Found by search: https://us.teamblind.com/setting/term_and_privacy : read. Terms of Use effective October 4, 2026; Privacy Policy May 20, 2026 (per the tool).
  - Section 3 (Prohibitions): "Crawling, scraping, data mining, data extracting, duplicating, copying" "without explicit permission from Teamblind, whether through automated or manual means".
  - 2.1: user content is licensed to Blind including for AI/ML training. 1.7: the user's own licence is "personal, non-commercial".
  - No API mentioned in the three documents.
- https://www.teamblind.com/robots.txt : read. Generic agents: only search, history and blog-internal paths blocked. Named AI bots (GPTBot, CCBot, ClaudeBot, anthropic-ai, Google-Extended, Applebot-Extended, Bytespider) disallowed site-wide. No rule for company or review paths.
- Singapore coverage not measured (Part B not run).

## 6 Google Maps reviews via Places API
- https://developers.google.com/maps/documentation/places/web-service/place-details : read. `reviews` returns "up to five" reviews per place; fields: author attribution, relative publish time, text, rating. Requesting `reviews` or `reviewSummary` uses the Place Details Enterprise + Atmosphere SKU (paid; price not read).
- https://developers.google.com/maps/documentation/places/web-service/policies : read. Must "credit the author" and link to the original review; reviews are ordered by relevance by default. "Cache or store Google Maps Content only as expressly permitted"; "You may not copy and save user reviews, business names, or addresses." Place IDs may be stored indefinitely; coordinates up to 30 days. Reviews are not verified by Google.
- AI review summaries (`reviewSummary`): search results from Google's documentation list English in India, the UK and the US and Japanese in Japan (an older page lists more Latin American regions). Singapore is not in what was read. Required heading, "Summarized with Gemini" disclosure and a report link.
- https://cloud.google.com/maps-platform/terms and /maps-service-terms : the fetch returned only a title (page truncated). The full Maps Platform ToS text was NOT READ, so its scraping and summarisation clauses are not verified.
- Content type: Google Maps reviews of a place are mostly customer reviews. The API does not distinguish employee reviews. Not measured.

## 7 HardwareZone Forums (SPH Media)
- https://forums.hardwarezone.com.sg/tnc : read. "Website Terms and Conditions", updated 19 February 2026.
  - 4.2: users must not "use automated tools (such as scrapers, spiders, or bots)"; must not "reproduce our content on another server or website"; must not "sell, license, broadcast, or commercially exploit our content".
  - 4.3.1(8): no "automated process ... scripting software or bots".
  - 4.3.2: members assign SPH Media co-ownership of user-generated content; nothing licenses it to other users or third parties.
- HardwareZone robots.txt was not fetched.

## 8 TAFEP and MOM
- https://www.tal.sg/tafep (landing page) : read. Describes guidelines, standards and a reporting route. No public list of employer complaint outcomes found. Copyright notice "All rights reserved".
- https://www.tal.sg/tafep/terms-of-use : read. No bots/scraper clause found; copyright infringement not allowed; nothing granting reuse.
- https://www.mom.gov.sg/terms-of-use : read. Last updated 14 March 2024. Section 7: all rights reserved; fair dealing for private study, research, criticism or review; no commercial reuse "without our prior written permission". Section 6: caching and framing prohibited except as set out. Singapore Open Data Licence not mentioned on this page.
- Neither publishes first-hand employee or candidate accounts. Regulator and enforcement records belong to E14.

## 9 Licensed or partner data
- See Glassdoor secondary notes. No provider was contacted (not authorised). Dataset resellers were not evaluated; their rights over the underlying reviews were not verified.

## 10 Job-seeker contributions
- No third-party terms apply. Nothing fetched. Consent, PDPA and moderation are design questions, not tested here.

## 11 Link-out only
- No reading. Not tested here.

## Not checked
Kununu, AmbitionBox, Comparably, Fairygodboss, LinkedIn (E09 notes LinkedIn prohibits scraping; terms not re-read), Facebook groups, Telegram groups, the full Google Maps Platform ToS, the Reddit and Glassdoor primary terms.
