# Run brief — free programmatic scraping tools, Playwright equivalents

Status: complete for this pass (survey, benchmark, service built and tested)

## Research question

How can JobHub fetch and read public web pages programmatically, for free, with tools equivalent to Playwright, and which option is best to run as a containerised service?

## Why

The company-research service ([prototype 03](../../../../../05_prototypes/P03-company-research-pipeline/README.md)) reads one page per site with plain HTTP. Earlier runs found plain fetch enough for many sites, but some pages are JavaScript-rendered or refuse plain clients, and the job-board side currently depends on Kimi WebBridge (the user's own browser), which is not a service. A containerised fetch-and-render service is the missing piece.

## Scope

In: free and open-source tools (or genuinely free tiers with no card and no credits) that fetch pages, render JavaScript, and extract text or structure; they must run in Docker on a local machine.

Out: paid scraping APIs, credit-based tiers, and anything needing a card. Bypassing CAPTCHAs, bot-detection evasion and login-wall scraping are out of scope. Tools that exist mainly for evasion are described in the survey for completeness but are not run against sites.

## Candidate set (to be extended during the survey)

| Group | Candidates |
|---|---|
| Browser automation | Playwright, Puppeteer, Selenium, Chromedp / Rod (Go) |
| Browser-as-a-service (self-hosted) | Browserless (open core), Steel Browser, Lightpanda |
| Crawl frameworks | Crawlee, Scrapy (+ scrapy-playwright), Scrapling |
| LLM-oriented extractors | Crawl4AI, Firecrawl (self-host), Jina Reader, ScrapeGraphAI |
| Plain HTTP + parsing | httpx / requests, curl_cffi, selectolax, BeautifulSoup, trafilatura |
| Agentic browser layers | browser-use, Stagehand, Playwright MCP |
| Evasion-oriented (survey only) | Patchright, Camoufox, Nodriver, undetected-chromedriver |

## Criteria

1. **Cost:** free forever, no card, no credits. Licence checked (open source vs source-available).
2. **Docker fit:** official image, image size, memory at idle and under load, runs as non-root, read-only filesystem.
3. **Rendering:** handles JavaScript pages; waits sensibly.
4. **Extraction quality:** clean main text or markdown without hand-written selectors.
5. **Politeness:** robots.txt support, rate limiting, honest user agent.
6. **Service shape:** HTTP API, concurrency, queueing, timeouts, retries.
7. **Maintenance:** last release, open issues, maintainers (checked on the repository pages).
8. **Fit for JobHub:** reads employer homepages and about/careers pages; optionally job-board pages (public ones only).

## Method

1. **Survey (web).** For each candidate: repository, licence, last release, stars, docs, pricing page where any hosted tier exists. Accessed pages recorded in `sources.md`.
2. **Claude in Chrome.** Used for pages that plain web search or fetch cannot read (JavaScript-rendered docs, pricing pages, GitHub release pages, search result pages). Read-only; no logins.
3. **Shortlist** of up to five on the criteria above.
4. **Benchmark in Docker** on the same set: 20 employer homepages from `05_prototypes/P03-company-research-pipeline/samples` and the earlier persona run (known good and known JS-heavy), plus 5 public MyCareersFuture job pages. Per tool and page: status, time, text length, whether the main text is present, memory use. Scripts in `code/`, raw results in `outputs/`.
5. **Service test** of the winner: a small HTTP wrapper in a container with a read-only filesystem and dropped capabilities, called by the existing pipeline.
6. **Recommendation** with what was verified, what was not, and the cheapest next step.

## Outputs

`findings.md` (survey table, benchmark results, recommendation), `limitations.md`, `sources.md`, `README.md`, `code/`, `data/`, `outputs/`.

## Rules

- Public pages only; no login, no CAPTCHA handling, no stealth or user-agent spoofing.
- robots.txt checked before each fetch in benchmarks; honest user agent.
- No accounts created; no card; no secrets printed or committed.
- Pacing between requests to the same host.
- Claims about tools are tied to a page read on the access date; anything from memory is labelled as such.

## Date

2026-11-01 (Singapore).
