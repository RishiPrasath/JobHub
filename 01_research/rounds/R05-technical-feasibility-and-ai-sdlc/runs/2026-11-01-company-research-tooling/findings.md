# Findings and recommendation

Everything below cost $0, used no card, and created no accounts. Results are from a 15-posting set on one day from one home connection (see `limitations.md`).

## 1. Claim check (task 1)

| Claim | Result | Evidence |
|---|---|---|
| Tavily: 1,000 free credits a month, no card | **Verified** | Tavily credits docs: "1,000 free API Credits every month", "No credit card required". Basic search = 1 credit, advanced = 2. |
| Serper is a fallback | **Partly verified** | Homepage: 2,500 free queries, no card. Whether the free queries expire is not stated; paid credits expire after 6 months (secondary sources). Public pricing page reportedly 404s. |
| ACRA on data.gov.sg is free, commercial use allowed | **Verified, with a rate-limit caveat** | Dataset pages cite the Open Data Licence ("free forever for personal or commercial use"). The live API returned 429 after a few dozen calls; the bulk-download route worked without a key. |
| Groq `gpt-oss-120b` free, strict JSON | **Verified in use** | Worked with the existing key, strict `json_schema` accepted. Documented limits: 30 requests/min, 1,000/day, 8,000 tokens/min, 200,000 tokens/day. The docs page labels these "Developer plan base limits", so which tier the account is on must be checked in the console. |
| Cloud Run in Singapore is $0, no card | **Not supported** | Singapore is Tier 2 pricing. The setup guide requires billing enabled on the project. Whether a card is mandatory was not stated on the pages read; a billing account normally needs one. Treat as "needs a card until shown otherwise". |
| Bing Search API retired; Google Custom Search closed to new users | **Verified** | Microsoft lifecycle page: Bing Search APIs retired 11 Aug 2025. Google: closed to new customers, existing customers must move by 1 Jan 2027 (confirmed on Google's page per secondary summary). |
| GitHub Models retired | **Probably true, one step short of confirmed** | Secondary sources: closed to new customers 16 Jun 2026, shut down 30 Jul 2026. GitHub's own notice was not opened. |
| Cerebras free tier restricted | **Consistent** | Secondary sources: $5 trial credit only after adding a verified payment method, expiring in 30 days. Official docs not opened. |
| Gemini free tier trains on your data | **Verified** | Gemini API additional terms: unpaid services may be used to improve products and reviewed by humans. EEA, UK and Switzerland get paid-tier data terms. |
| Brave needs a card | **Verified, and it matches the report's decision framing** | Brave quickstart: a card is required even for free plans; $5 monthly credit is roughly 1,000 queries; attribution required. |
| SearXNG gets blocked often | **Not checked** | |
| LinkedIn, Glassdoor, Indeed, JobStreet ban scraping | **LinkedIn verified; the others not checked** | LinkedIn help centre bars crawlers and bots. |
| Wayback and GDELT are usable free history/news | **Wayback yes, GDELT no** | See E4. |

## 2. Experiment results (task 2)

### E1 Employer resolution with ACRA

- **Live API:** unusable for matching. Free-text `q` returned unrelated names ("Paka Lolo" for "Moda Paolo"), and the unauthenticated limit triggered 429 within a few postings ("try again in 10 seconds"). The API can still serve single UEN lookups.
- **Bulk CSV:** 26 files, 641 MB, 2,066,468 entities, downloaded with no key in a few minutes. Local token matching over all rows took under a minute for all 15 employers.
- **Outcome with a simple rule (all query tokens must appear in a name or former name; score by string ratio):**

| State | Count | Postings |
|---|---|---|
| exact | 10 | P01, P02, P03, P06, P07, P08, P10, P11, P13, P15 |
| likely | 1 | P05 (posting says "Thye Hua Kwan Hospital", ACRA says "Ang Mo Kio - Thye Hua Kwan Hospital Ltd.") |
| ambiguous | 2 | P12 (NTUC FairPrice Co-operative is not in ACRA; the only hit is the Foundation, correctly not auto-accepted), P14 (a dissolved sibling scored 0.91 against the live 1.0) |
| unresolved | 2 | P04 (ACRA spells it "GRABTAXI HOLDINGS", one word), P09 ("JL99" is not in the registered name "THE SUPREME HR ADVISORY") |

- **Three real defects found:**
  1. **Sibling entities can pass as "exact".** P11 matched `NATURELAND SINGAPORE PTE. LTD.` at 1.0, but the posting URL slug says `natureland-care`, and `NATURELAND CARE PTE. LTD.` is also in ACRA. Name matching cannot tell siblings apart. The posting's own UEN (MyCareersFuture shows one) or URL slug must be used first, and name matching treated as a fallback that needs confirmation when several live entities share the stem.
  2. **Rule fixes are needed, not new tools.** Preferring live entities would turn P14 into exact. Trying joined/split token variants would find GRABTAXI (checked by direct lookup, not re-run through the matcher). Dropping an unmatched leading token would surface The Supreme HR Advisory for P09, but only as "needs user confirmation".
  3. **Brand names are not legal names.** P09 shows an agency posting under a brand-like string.
- Ten "exact" matches were checked only by reading name and industry. Only the four UENs also found through web search (P01, P02, P07, P09's sibling) were independently cross-checked.

### E1c Resolution rules v2 (same 15 postings, rerun after the fixes)

Implemented in [prototype 03](../../../../../05_prototypes/P03-company-research-pipeline/README.md) (SQLite FTS5 index over the same 2,066,468 rows, built in 25 seconds, 15 lookups in under 0.2 seconds). Changes: prefer live entities, try joined tokens ("grab taxi" to "grabtaxi"), retry with one token dropped (flagged, never auto-accepted), flag sibling entities with similar names, accept a UEN or a posting-URL name hint, and keep "Singapore" as a name token. Output: `outputs/e1c_acra_rules_v2.json`.

| State | v1 | v2 |
|---|---|---|
| exact | 10 | 11 (P01, P02, P03, P04, P06, P07, P08, P10, P11, P13, P14) |
| likely | 1 | 1 (P05) |
| needs confirmation | 0 (2 "ambiguous") | 3 (P09, P12, P15) |
| unresolved | 2 | 0 |

- **Fixed:** Grab (now `GRABTAXI HOLDINGS`), Little Skool-House (dissolved sibling ignored), Natureland (with the URL hint `natureland care` it resolves to `NATURELAND CARE PTE. LTD.`; **without the hint it is flagged with 9 sibling entities and not auto-picked**), JL99/Supreme HR (now surfaces `THE SUPREME HR ADVISORY PTE. LTD.` but only as needs-confirmation).
- **Correctly not auto-accepted:** NTUC FairPrice (the co-operative is not in these datasets; only the Foundation matches), Randstad (`RANDSTAD PTE. LIMITED` plus a sibling `RANDSTAD FTC PTE. LTD.`).
- **A bug I introduced and fixed in the same session:** treating "Singapore" as a noise word made "Singapore General Hospital" match any "General Hospital" and flag it wrongly; keeping it as a name token fixed that.
- **Caveat:** these rules were adjusted after looking at the same 15 postings, so the improvement is a repair of known failures, not evidence of general accuracy. It needs a fresh posting set. The Natureland result also depends on the hint, which only exists when the posting URL contains the company slug.

### E2 Plain HTTP with robots.txt

- 11 official sites were available (4 postings had no discoverable official site: P01, P02, P09, P13).
- robots.txt was read and allowed the page on 8 sites; HRnet's site has no robots.txt (404, treated as no restriction); DHL's and Marina Bay Sands' robots.txt requests timed out. Plain fetch returned usable text (500+ visible characters) for **9 of 11** in 0.1 to 1.9 seconds each.
- **2 of 11 blocked:** DHL (P08) and Marina Bay Sands (P10) timed out on robots.txt and reset the page connection after about 40 seconds. Reported as blocked; nothing was done to get around it.
- Schema.org `Organization` JSON-LD appeared on 5 of the 9 readable pages (P03, P04, P11, P14, P15), and none of them gave a legal name or UEN check on its own. Useful when present, not something to depend on.

### E3 Playwright against the same 11 sites

- Of the 9 sites plain fetch could read, rendered text was **shorter on 6** (it drops navigation and footer text) and **longer on 3** (P05 3,754 to 6,618 characters; P07 1,361 to 1,589; P12 2,532 to 2,790). I did not read the extra text to judge whether it was useful, so "adds little" is a character-count judgement, not a content review.
- It took 1 to 9 seconds per page versus under 2 for plain fetch, and needs a browser binary.
- **Both blocked sites also failed in the browser** (`ERR_HTTP2_PROTOCOL_ERROR`). With no stealth or spoofing, a browser does not unblock them.
- Conclusion for this sample: Playwright is a fallback for thin pages, not the default.

### E4 History and news

- **Wayback CDX: 11 of 11 sites returned results**, giving first capture year and number of years with captures (for example HRnet 2013 and 14 years, Palo IT 2012 and 8 years). A usable "site continuity" signal, at no cost. About 4 seconds between calls was polite and sufficient. My first query form returned zero captures and 503s; the working form is `collapse=timestamp:4`, one row per year.
- **GDELT DOC 2.0: 14 of 15 requests returned 429**, even with 12 to 16 seconds between calls. The one successful call returned 0 articles. Not usable from this connection; drop from v1.
- Neither source says anything about layoffs or turnover for these employers in this run.

### E5 Groq `gpt-oss-120b` with and without citation checking

Same 9 pages and the same 5 fixed questions, run twice. Each page was trimmed to about 6,000 characters of numbered excerpts.

| | A: free quotes | B: numbered excerpt, code checks quote |
|---|---|---|
| Valid JSON | 9 of 9 | 9 of 9 |
| Answers claimed as supported | 32 | 30 |
| Quote found verbatim in the page | 23 (72%) | 28 (93%) |
| Quote **not** found | **9 (28%)** | **2 (7%)** |
| Tokens (9 pages) | 14,194 | 15,583 |
| Latency | about 1.4 seconds per page | about 1.4 seconds per page |

- In A, the 9 failures were mostly quotes stitched from separate parts of the page with "..." (a spliced quote that reads as one sentence), plus one broken character. In B the 2 failures were one empty quote and one stitched quote; code rejects both, so they never reach the user.
- This supports the report's suggested fix: **making the model cite a numbered excerpt, and rejecting quotes that are not in that excerpt, cut unverified quotes from 28% to 7% and makes the remainder detectable.**
- It checks the quote, not whether the answer is right. A quote can be genuine and the answer still wrong. Answers were only spot-checked (for example Randstad and HRnetGroup were labelled recruitment agencies, Palo IT and SGH direct employers).
- Hiring and careers questions mostly came back `not_found` because only the home page was read. That is a pipeline limit, not a model failure.
- Budget: about 1.7K tokens per page. At the documented 200K tokens/day, that is roughly 100 page analyses a day on the free plan, which suits experiments but not a launch.

### E7 Official-site discovery without a search API (Wikidata)

Run after the user ruled out cards and one-time credits. Wikidata's search plus the "official website" property (P856) is free, official and keyless.

- Returned a website for **9 of 15** employers. Of those, **7 were correct and current** (P03, P04, P06, P07, P08, P10, P12), though some links were old paths (SGH `.../Pages/default.aspx`, DHL's old URL).
- **2 were wrong:** P05 listed `amkh.com.sg` (the live site is `amkh.org.sg`), and P11 "Natureland" matched a UK seal sanctuary. P15 returned the global `randstad.com`, not the Singapore site. A wrong hit is worse than no hit, so every Wikidata result must be fetched and checked against the ACRA name or address before use.
- **No result for all four small employers** (P01, P02, P09, P13) and for P14. Wikidata only knows notable organisations.
- So Wikidata covers large employers and does nothing for the long tail. The long tail is where only a search API (Tavily's recurring free tier) or the posting's own link would help.

### E8 Official-site discovery by guessing domains (no search engine)

Requested after the user asked for a scraping approach instead of API keys. For each employer, candidate domains were generated from the posting name and the registered name (joined and hyphenated words, five TLDs), pruned by DNS, then only the candidate's own homepage was fetched after a robots.txt check. A site counted as "verified" when every distinctive word of the legal name appeared in the title or first 3,000 characters. Output: `outputs/e8_domain_guess.json`.

- **5 of 15 verified:** P03 `palo-it.com` (correct), P14 `littleskoolhouse.com/.sg` (correct), P15 `randstad.com.sg` and `.com` (correct), P11 `naturelandcare.com` and P13 `curos.com.sg` (plausible, **not independently confirmed**).
- **P13 is a new find:** web search had found no official site for Curos Learning.
- **1 false positive:** P06 Singapore General Hospital verified `generalhospital.com`, which is a different organisation. The name-word check is too weak when the name is generic.
- **Missed 10:** every name where the real domain is not a join of the name (Grab uses `grab.com`, AMKH uses `amkh.org.sg`, Palo, Marina Bay Sands blocked or not matched, and the four small employers have no site at all).
- Conclusion: domain guessing is a cheap supplement for names that map directly to a domain, not a replacement for search. It needs a stronger check, such as the ACRA postal code appearing on the page, before its output can be trusted.

### Search-engine scraping, checked but not run

robots.txt on 2026-11-01: Google, Bing, Mojeek and Brave disallow `/search`; DuckDuckGo disallows `/html`, `/lite` and `/` for `User-agent: *`. So automated scraping of their result pages is disallowed by the sites' own rules. Not run.

### E9 Local SearXNG in Docker (the strongest result so far)

Requested after the user asked for locally run search returning URLs, headings and descriptions. SearXNG 2026.10.30 in a Docker container, localhost only, JSON on, limiter off, queried with `"<registered name> Singapore"` at 3-second spacing. Script `code/e9_searxng_local.py`, output `outputs/e9_searxng_local.json`.

- **All 11 employers with a known official site were found:** the right domain ranked 1st for 9 (Palo IT, AMKH, SGH, HRnet, DHL, Marina Bay Sands, Natureland, Little Skool-House, Randstad), 2nd for Grab and 4th for FairPrice (after a group site and news pages).
- **Small employers:** found `modapaolo.com.sg` (P01), `curos.com.sg` (P13, which web search had missed) and `thesupremehr.com` (P09, the registry's Supreme HR Advisory). Nothing real for Yan Business Group (P02): only directory and scam-report pages.
- Each result carries URL, heading (title) and a description, which is what the user asked for.
- **Which engines answered:** only "google cse" (300 results over 15 queries) and Brave (86). DuckDuckGo returned a CAPTCHA every time. After roughly four queries at 3-second spacing SearXNG suspended Brave ("too many requests"), leaving Google alone for the rest. Each query still returned 20 to 39 results. I did not try to get around any suspension.
- **It is not fully local.** SearXNG relays queries to Google and Brave. "google cse" is Google's custom-search element endpoint, scraped without a key (`use_official_api: False`). Google has said its Custom Search JSON API closes on 1 Jan 2027; whether this endpoint survives is unknown, so the main engine could disappear.
- **Integrated into prototype 03:** `find-site` now searches through SearXNG, checks the legal name's words on each candidate page, and caches verified sites by UEN. Tested in Docker: Curos Learning found `curos.com.sg` and was then served from the cache with no external call. Moda Paolo's search found the right site but the page could not be read for verification (shown as `page_unreadable`). A job-listing site (bebee.com) passed the first name check, so I added it and similar aggregators to the exclusion list.

### Other local-search options reviewed (not run)

| Option | What it is | Fit |
|---|---|---|
| SearXNG | Local metasearch proxy | Works now (E9); depends on Google/Brave staying reachable |
| YaCy | Runs its own crawler and index, JSON search at `/yacysearch.json` | Genuinely local, but it only knows pages you crawl; nothing to search until seeded |
| Marginalia | Open-source engine with its own index of small sites | Needs heavy hardware (README: 32 GB advised); its index is small independent sites, unlikely to include Singapore SMEs |
| Common Crawl index | Free public index queried by URL/domain, not by company name | Could seed a local Singapore-domain list, but no name search; not tested |
| Whoogle | Proxies Google | A user report says upstream changes broke it |
| Local cache (built) | UEN to verified site in SQLite | Fully local after the first lookup |

### DuckDuckGo module, added at the user's request

Added to prototype 03 as `pipeline/websearch.py`, on by default at the user's request (`JOBHUB_ENABLE_DDG=0` turns it off), with throttling and a no-retry block breaker. **Tested twice: DuckDuckGo answered the honest-user-agent client with its anti-bot page both times, so no search results were obtained.** The `ddgs` library might succeed by imitating a browser; that was not used, since it amounts to evading the block. Until a sanctioned route exists, small employers with no findable site stay "no official site found".

### Container check (prototype 03)

`docker compose run --rm pipeline acra-update` completed inside the container with no key: **27 CSV files, 2,124,508 rows indexed** (the host run had 26 files and 2,066,468 rows, because one dataset had been missed). A containerised `resolve "Palo IT Singapore"` returned `PALO IT SINGAPORE PTE. LTD.` Container-level `research` with Groq was not run; it was run on the host.

### E6 Whole chain, per posting

| Posting | Identity (ACRA) | Official site | Page read | Wayback | Cited answers |
|---|---|---|---|---|---|
| P01 Moda Paolo | exact | none found | no | n/a | no |
| P02 Yan Business Group | exact (sole prop) | none found | no | n/a | no |
| P03 Palo IT | exact | yes | yes | 2012 | yes |
| P04 Grab | **unresolved** (spelling) | yes | yes | 1997 | yes |
| P05 Thye Hua Kwan Hosp. | likely | yes (differently named) | yes | 2008 | yes |
| P06 SGH | exact | yes | yes | 2000 | yes |
| P07 HRnet Ventures | exact | group site only | yes | 2013 | yes |
| P08 DHL Supply Chain | exact | yes | **blocked** | 1996 | no |
| P09 JL99 / Supreme HR | **unresolved** (brand) | none found | no | n/a | no |
| P10 Marina Bay Sands | exact | yes | **blocked** | 2007 | no |
| P11 Natureland | exact, **probably wrong sibling** | yes | yes | 2012 | yes |
| P12 NTUC FairPrice | ambiguous (not in ACRA) | yes | yes (thin) | 1999 | mostly not found |
| P13 Curos Learning | exact | none found | no | n/a | no |
| P14 Little Skool-House | ambiguous (fixable) | yes | yes | 2001 | yes |
| P15 Randstad | exact | yes | yes | 2009 | yes |

Counts: official site found 11 of 15; page read 9 of 15; cited answers produced for 8 of 15 (P12's were thin). Every small employer (P01, P02, P09, P13) is exactly the case where public web evidence is weakest. The service will often have to say "no official site found, only the registry record".

## 3. Recommended stack (task 3)

**Constraints set by the user during this run:** strictly free, no card, no one-time credits, mostly scraping, sustainable, and runnable in a Docker container. Under that rule Serper (one-time credits), Brave (card), Exa (credits), Cerebras (card), Cloud Run (billing) and Gemini's free tier (trains on data) are out.

**Tier check for search (the only layer that is not already keyless):**

| Option | Tier type | Fit |
|---|---|---|
| Tavily Researcher | **Recurring**: 1,000 credits/month, "reset on the first day of each month", no card (Tavily pricing page) | Only recurring free API found. Needs a free account and key; user has not agreed to make one. Optional |
| Serper, Exa | One-time credits | Excluded |
| Brave | Card required | Excluded |
| Google Custom Search | Closing 1 Jan 2027 | Excluded |
| Self-hosted SearXNG | Free forever, but it scrapes Google/Bing, which block and CAPTCHA a single IP and breach those engines' terms | Not recommended |
| Wikidata (E7) | Free, official, keyless | Covers large employers only |

Scraping search engines themselves is the part that fails, so "mostly scraping" applies to the **company's own public pages** (E2), not to Google or Bing.

| Layer | Pick | Why | Cost to start | Trade-off |
|---|---|---|---|---|
| Identity | ACRA bulk CSV in a local table, refreshed weekly; use the posting's UEN when it has one | Free, no key, fast; returned a candidate for 13 of 15 on a first rule set (11 confident, one of those probably the wrong sibling) | $0 | Needs sibling handling and fuzzy rules; co-operatives and public bodies are absent; 641 MB to host |
| Site discovery | Wikidata P856, then the posting's own employer link if present, then optionally Tavily's free tier, else "no official site found" | Wikidata gave 7 correct sites of 11 findable, with no key | $0 | Two wrong hits in 15, and none for small employers; every hit must be checked against the registry name |
| Pages | Plain HTTP with robots.txt first; Playwright only for thin pages | Plain fetch got 9 of 11 in under 2 seconds; the browser made no difference to the 2 blocked sites and gave more text on only 3 | $0 | Some large employers block automated reads; report them as blocked |
| History | Wayback CDX | 11 of 11 worked | $0 | Site age only; no news or turnover signal |
| News | None for v1 | GDELT returned 429 for 14 of 15 requests | n/a | Layoff and stability questions stay "not researched" |
| LLM | Groq `gpt-oss-120b`, strict JSON, numbered excerpts, code rejects unverified quotes | 28% to 7% unverified quotes, about 1.4 seconds per page | $0 on the free plan | Roughly 100 pages/day on documented limits; check which tier the account is on |
| Hosting | Docker container run locally (decided by the user) | Everything above is plain Python or Node plus a data file, so it containerises without extra services. Docker 28.5.1 is installed here but the daemon was not running, so no container was built or tested | $0 | The ACRA CSVs (641 MB) should be a mounted volume or a build-time download, not baked into the image; Playwright, if kept, adds roughly a browser's worth of image size |

User answers recorded: no card; Groq is on the free plan and public pages may be sent to it; local hosting for now.

## 4. What was not done

- Tavily was not tested (needs a key; the user has not agreed to create one). Serper was dropped as one-time credits.
- No Docker image was built; the daemon was off.
- Layoffs, turnover and reposting signals were not tested, since GDELT failed and no other free source was run.
- Review sites (Glassdoor, JobStreet and similar) were not accessed, per the report's scraping guidance.
- Human review against a gold answer set was not done; only spot checks.

## 5. Next steps

1. ~~Fix the ACRA rules and re-run E1~~ Done (E1c). Next: test on a fresh set of postings that was not used to tune the rules.
2. ~~Write a Dockerfile and compose file~~ Done in prototype 03; see "Container check" below.
3. Optional: test Tavily's recurring free tier on the long-tail employers if the user decides to create a key.
4. Add a second page per site (careers, about) and re-run E5 to see whether hiring questions get answered.
