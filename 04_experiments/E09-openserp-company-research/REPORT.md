# OpenSERP feasibility report

Run date 2026-11-07. OpenSERP v0.8.18 (`98f42fb`). One machine (Windows, Docker Desktop), one network location (Singapore), one afternoon. Everything below was measured in this run unless marked **not verified**.

## Recommendation: use it with changes

OpenSERP is a good **discovery and page-reading layer** for company research: it ran as one small container, answered 48 of 48 searches, read the pages that matter most for employer research (review sites, news, registry aggregators, company sites) in about half a second each, and reported most blocks clearly. It is **not** a validity check. On its own, the pipeline built on it rated a lookalike employer that does not exist as "appears real, high confidence", and it cannot read Glassdoor or Reddit at all.

Use it only with these changes:

1. **Check the company against the registry first** and run web research only on a company that exists (or deliberately report that it could not be confirmed). Existence is a registry question, not a search question.
2. **Add an entity gate in code**: the exact name from the posting must appear in a page or a search result, or the brief cannot say "appears real". A prompt rule did not stop the model.
3. **Add your own block detection** on extracted pages. The service reported a Reddit bot challenge as a successful page.
4. **Treat it as a private, low-volume prototype tool.** The legal position (below) does not support running it as a production feature that queries Google and Bing at scale.

## What worked

- **Setup is easy.** One Go binary in a 568 MB image, built from source in about 2 minutes, runs read-only with all capabilities dropped, 60 MB to 130 MB of memory, health and stats endpoints, JSON and OpenAPI docs.
- **Three engines work from here:** DuckDuckGo (1.0 s), Bing (3.3 s), Google (3.6 s). All 48 harness searches succeeded; every one was answered by DuckDuckGo, so Bing and Google were never needed.
- **Resilience features work:** result cache (15 ms then 3 ms on a repeat), rate limiter (queues rather than fails, about 6 s apart at 10 a minute), a circuit breaker (Ecosia opened after 3 failures, 300 s), fallback across engines (`mode=any` returned 200 in 1.2 s with Ecosia blocked), no retry on a captcha.
- **Clear failure codes from search:** 403 `blocked`, 429 `captcha_detected`, 502/503/504, with a machine-readable `error`.
- **Safe by default on its own network:** it refuses loopback, private-network, cloud-metadata and `file://` targets (400 `INVALID_PARAM`).
- **Good page types:** news article, Wikipedia, Indeed and JobStreet review pages, registry aggregator (`sgpbusiness.com` returned UEN, status, incorporation date matching the registry), government data portal, company site in whole-page mode.

## What failed or was weak

- **Engines:** Ecosia 403 blocked; Yandex captcha on both queries; Baidu answered but the obscure query returned unrelated domains (`szqxzspj.cn`, `quikfish.com`).
- **Glassdoor is unreadable:** 21 of 21 Glassdoor reads failed with the same generic `502 Failed to extract URL content`. That is 21 of the 24 read errors.
- **Reddit challenge returned as success:** HTTP 200, `mode_used=rendered`, 11,934 characters, of which 490 were text ("Prove your humanity") and the rest one inline image. Character counts are a poor quality signal; the harness now strips inline images first.
- **Article-only extraction loses homepages:** the default returned 755 characters from the company homepage; whole-page mode returned 32,667 characters of which 69% of lines were links.
- **A forum hit was off-target:** the search returned a HardwareZone page (a 3,000-post pagination page about PC rigs) whose extracted text never mentions the company.
- **Lookalike employer rated as real** (below). Of the eight agents, one made this serious error.
- **Brand names versus legal names:** the registry cannot confirm "Grab Holdings", "Ninja Van Singapore" or "KPMG Singapore" (closest registered names are unrelated or differently structured); web research did find them. The two methods cover different gaps.

## Phase 2 results

**Engines** (`outputs/phase2/engines_summary.json`)

| Engine | Known-company query | Obscure query | Notes |
|---|---|---|---|
| DuckDuckGo | 200, 1.0 s, 8 organic | 200, 1.0 s, 8 organic | Relevant results both times (scam-checking sites for the obscure query) |
| Bing | 200, 3.3 s | 200, 3.2 s | Relevant |
| Google | 200, 3.8 s | 200, 3.5 s | Relevant |
| Ecosia | 403 `blocked` in 0.2 s | 403 | Opened the circuit breaker after 3 failures |
| Yandex | 429 `captcha_detected` in 8 s | 429 | Service did not retry |
| Baidu | 200, 1.4 s | 200, 2.2 s, junk domains | Not usable for this task |

**Page extraction** (`outputs/phase2/extract_summary.json`; one company, Randstad Singapore)

| Page type | Result | Content quality |
|---|---|---|
| Company website | 755 chars (article-only) or 32,667 (whole page) | Article-only drops most of a homepage; whole page is mostly links and navigation |
| News article (CNA) | 6,712 chars, 1.4 s | Clean headline and body |
| Wikipedia (control) | 10,740 chars | Clean |
| Indeed company reviews | 6,951 chars | Ratings and reviews present, some "Loading..." fragments |
| JobStreet reviews | 611 chars | A short summary of the reviews, not the reviews |
| Government data portal | 1,526 chars | Clean |
| Registry aggregator (sgpbusiness.com) | 8,773 chars | UEN, status, incorporation date, address; matches the registry data |
| LinkedIn company page | 11,614 chars from one public request | Marketing posts, not company facts. **Do not use**: LinkedIn prohibits scraping |
| Forum post (HardwareZone) | 11,897 chars | Raw pagination page, avatars and post numbers, off-topic |
| Reddit thread | HTTP 200, "Prove your humanity" | Bot challenge reported as success |
| Glassdoor reviews | 502 `extract_failed` | Generic message, no reason |

**Blocking behaviour.** Search: distinct status and `error` codes (good). Extraction: only HTTP status (`403/401` blocked, `429` rate limited) is classified; a challenge page returned with 200 is not detected, and Glassdoor's failure gives no reason. Detecting a blocked or garbage page needs client code: strip images, look for challenge phrases and titles, require a minimum of real text, and check the company name appears.

**Controls.** Rate limit per engine, burst, result cache with TTL, retries (`max_retries`, none on captcha), circuit breaker, proxy support (single, pooled and per-request) and a 2captcha solver integration exist. **Not used:** proxies and the captcha solver, deliberately.

**Identity and robots.txt (tested with an echo site).** In plain-HTTP mode the extractor sends `Chrome/146` with `sec-ch-ua: "Google Chrome";v="146"`; rendered mode sends `Chrome/152`. It fetched a path that robots.txt disallows and never requested robots.txt. The source also rotates among named browser profiles (`chrome-linux-amd`, `chrome-linux-mesa-uhd620`, `chrome-linux-swiftshader`). In short, it looks like a person's browser and does not honour robots.txt.

## Phase 3 results: eight persona agents

Model: `openai/gpt-oss-120b` on a free tier, strict JSON, quotes checked against source text in code. Eight agents in parallel, wall time 588 s, 48 searches, 64 page reads, 16 model calls, 39,033 tokens.

| Persona | Company (truth) | Model rating | After name gate | Claims verified / unverified | Pages read ok / tried |
|---|---|---|---|---|---|
| Software engineer | Grab Holdings (real, brand) | real, consistent / medium | unchanged | 11 / 2 | 5 / 8 |
| Nurse | Raffles Medical Group (real; registry confirms) | real, consistent / medium | unchanged | 8 / 2 | 4 / 8 |
| Warehouse | Ninja Van Singapore (real, brand) | real, consistent / medium | limited evidence / medium | 13 / 3 | 5 / 8 |
| Marketing | Lazada Singapore (real; registry confirms) | limited evidence / medium | unchanged | 11 / 2 | 3 / 8 |
| Finance | KPMG Singapore (real, brand) | real, consistent / **high** | limited evidence / medium | 11 / 3 | 4 / 8 |
| Customer service | Avanguarde Pte. Ltd. (tiny, live in registry) | limited evidence / medium | unchanged | 7 / 2 | 5 / 8 |
| Operations | Zzqxv Qwlmt Holdings Pte Ltd (fictitious) | **cannot verify / low** | unchanged | 0 / 0 | 0 / 8 |
| Customer service officer | DBS Bank Singapore Recruitment Pte Ltd (lookalike, not registered) | **real, consistent / high (wrong)** | **suspicious / low** | 11 / 4 | 5 / 8 |

- **Fictitious:** correctly `cannot_verify`. The engines returned plausible scam-checker and review pages, but all were about other companies and were screened out by the "page mentions the company" check.
- **Obscure real:** correctly `limited evidence`. The agent found the registry-style pages (company ID, status, address) and a job posting, and flagged a registered address that a source describes as a virtual-office address.
- **Lookalike (the important failure):** the model used DBS Bank review pages as evidence about the lookalike, calling it confirmed by "multiple independent sources". It listed "the exact legal entity name is not mentioned in any source" only under *could not verify*. A prompt rule against exactly this behaviour did not prevent it.
- **Name gate** (`harness/rescore_gate.py`, applied afterwards, deterministic): the exact name from the posting must appear in a page or a search-result title or snippet. It moved the lookalike to `inconsistent_or_suspicious / low`, left the fictitious one alone, and capped two real firms (Ninja Van, KPMG) whose pages use only the short brand name. **The gate was designed after seeing these results; these numbers are a repair, not a test on unseen companies.**
- **Citation checking:** 72 of 90 claims had a quote found in the cited source and 18 did not (80% verified). A spot check of 10 verified claims found the quotes support the claims, with one weakness: "frequent layoffs" rested on a single review quote ("They layoff people every 6 months"), and the lookalike's salary claim is verified but describes DBS Bank. Verified means the quote is in the page, not that the page is about the right entity.
- **Read failures:** 31 of 64 reads gave usable text; 24 errors (21 Glassdoor), 4 blocked (Reddit, a stock site), 3 irrelevant, 2 thin. Excluding Glassdoor, 31 of 43 (72%).

## Scores (1 to 5)

| Dimension | Score | Why |
|---|---|---|
| Reliability | 3 | Search 48/48 but only 3 of 6 engines usable and all load landed on one. Page reads 48% usable (72% without Glassdoor). |
| Content quality | 3 | Review, news and registry-aggregator pages are clean; homepages, forums and challenge pages are poor; defaults drop or inflate content. |
| Insight quality | 3 | Briefs for known firms had specific facts (ratings, layoff coverage, salary ranges, financial results) but are mostly review-site sentiment and anecdote. The tiny firm's brief was the most useful (virtual-office address, no operational detail). |
| Validation ability | 2 (3 with the gate) | Fictitious caught; lookalike missed with high confidence until a code-side gate was added after the fact. |
| Blocking and resilience | 3 | Search-side failure reporting, breaker and fallback are good. Extraction misses challenge pages, hides Glassdoor's reason, ignores robots.txt, and has no honest identity. |
| Speed and cost | 4 | Search 1 to 4 s uncached, reads about 0.4 s median, 39k model tokens for eight briefs, no per-query fee. The 10-a-minute cap, not the tool, made 48 queries take about 5 minutes. A single company alone is about a minute (estimate; the only isolated agent run was cached). |
| Operational effort | 3 | Easy to start and monitor. Engines change their pages; young project (26 open issues, released the same week); real use would need proxies and monitoring; one first-start port problem with Docker Desktop. |

## Risks, including legal and terms of service

These are my reading, not legal advice, and the terms were **not re-checked in this session**.

- **Search engines.** Google and Bing terms generally prohibit automated queries outside their APIs. OpenSERP works by driving a real browser against their result pages, and its own README says engines can return CAPTCHAs and rate limits. At the volumes of this experiment the risk is blocking; at product scale it is a terms violation and an IP-ban problem, and the fix the tool offers is proxies and CAPTCHA solving, which I did not use and would advise against.
- **Page fetching.** The extractor ignores robots.txt and presents a real-browser identity, unlike the company-research prototype in this repo, which checks robots.txt and identifies itself. Sites such as LinkedIn, Glassdoor, Indeed and Reddit restrict scraping in their terms. This experiment fetched a small number of such pages to test behaviour; a product should link out to those sites instead.
- **Copyright and privacy.** Extracted review text is third-party content, so the repo does not commit it. Reviews can contain personal details about named employees.
- **Safety.** The service refuses private addresses by default (a good sign), but if exposed it is an open proxy that fetches any public URL and drives Chrome; keep it on localhost or behind authentication.
- **Wrong answers.** The biggest risk is not legal but product: a confident "appears real" about a lookalike would tell a job seeker a scam is fine.

## Alternatives worth comparing

- **The registry first.** The local company-registry service already confirms existence and identity for legal names; it cannot confirm brand names (Grab, Ninja Van, KPMG here).
- **SearXNG** (already tested in this repo): fewer moving parts but it relays to the same engines; it throttled after about two dozen queries in an earlier run.
- **The repo's own fetch-render service** for page reads, with robots.txt checks and an honest identity.
- **Licensed search APIs** (Tavily, Brave and others): rejected earlier because of the no-credits constraint; **not re-verified here**. If the product ever needs production-scale search, this is the legally clean route.

## Limitations of this experiment

Eight companies, one run, one location, one model, one day. The name gate was built after seeing the failure. Scores are my judgement. Timings include a 10-a-minute self-imposed limit and a warm cache for one agent. Third-party sites change; Glassdoor and Reddit results may differ elsewhere or another day. Engines could behave differently from other IP addresses.
