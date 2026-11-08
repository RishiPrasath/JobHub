# Findings

**Short answer:** no single tool wins on every page. Plain `httpx` + `trafilatura` handled most homepages in about 0.3 s, but returned nothing on JavaScript-rendered job pages. Of the browser-based options, **Playwright rendered the most pages completely** (5 of 5 job pages), **Crawl4AI is the best ready-made container service**, and **Lightpanda is by far the lightest** but is AGPL and was incomplete on job pages. Recommendation: a two-tier service, with plain fetch first and a Playwright render tier as fallback (details in section 4). The benchmark is small (25 URLs, one run), so treat the ranking as indicative.

## 1. Survey (GitHub API, 2026-11-01)

| Tool | Licence | Stars | Last push | Free in Docker? | Verdict |
|---|---|---|---|---|---|
| Playwright | Apache-2.0 | 99k | 2026-10-31 | Yes, official `mcr.microsoft.com/playwright` images | Shortlisted |
| Puppeteer | Apache-2.0 | 96k | 2026-11-01 | Yes (Chrome only) | Same class as Playwright; not tested separately |
| Selenium | Apache-2.0 | 35k | 2026-11-01 | Yes | Heavier, test-oriented; not tested |
| chromedp / Rod (Go) | MIT | 13k / 7k | 2026-10 / 2026-08 | Yes | Good if the service is in Go; not tested |
| Crawl4AI | Apache-2.0 | 87k | 2026-11-01 | Yes, REST API in the image | Shortlisted |
| Lightpanda | **AGPL-3.0** | 40k | 2026-11-01 | Yes, `lightpanda/browser` | Shortlisted |
| Steel Browser | Apache-2.0 | 8k | 2026-10-31 | Yes, REST + CDP; "public beta" | Shortlisted |
| Scrapling | BSD-3-Clause | 91k | 2026-10-31 | Yes, plus an MCP server | Not benchmarked; part of it is evasion-oriented |
| Scrapy (+ scrapy-playwright) | BSD-3-Clause | 65k | 2026-10-30 | Yes | A crawling framework, not a render service |
| Crawlee (Node) | Apache-2.0 | 26k | 2026-11-01 | Yes | Framework with queues; not benchmarked |
| Firecrawl | **AGPL-3.0** | 198k | 2026-10-31 | Self-host needs API, workers, Playwright, Redis, RabbitMQ, Postgres; API unauthenticated by default | Excluded: heavy and AGPL |
| Browserless | **SSPL-1.0 or commercial** | 14k | 2026-10-30 | Free only for non-commercial or SSPL-compatible open source | Excluded: licence risk for a product |
| Jina Reader | Apache-2.0 | 12k | 2026-05-22 | Self-host image exists but needs assets fetched separately; hosted r.jina.ai has anonymous limits | Not benchmarked |
| httpx, selectolax, trafilatura | BSD / MIT / Apache | 16k / 2k / 7k | 2026-10 to 11 | Yes | Baseline tier |
| browser-use, Stagehand, Playwright MCP | MIT / MIT / Apache | 120k / 26k / 39k | 2026-10-30/31 | Yes | Agent layers that need an LLM; a different problem |
| Camoufox, Nodriver, undetected-chromedriver (Patchright repo not found at the path tried) | MPL-2.0, AGPL-3.0, GPL-3.0 | 13k / 5k / 13k | 2026-10 (UC: 2025-07) | n/a | **Not run.** Their purpose is avoiding bot detection, which is out of scope |

Notes from the pages themselves:
- Playwright's own Docker page says the image is "intended to be used for testing and development purposes only". For untrusted sites it recommends a non-root user with its seccomp profile, `--init` and `--ipc=host`. Alpine is not supported.
- Lightpanda's README claims about 16x less memory and 9x faster than headless Chrome from its own 100-page test. Linux needs glibc; there is no Windows build.
- Crawl4AI's server needs an API token, `--shm-size=1g`, and takes about 10 seconds to start. The README says core crawling needs no LLM.
- Google search worked in Claude in Chrome (it cannot be reached from plain web search) but returned mostly SEO comparison articles from tool vendors. I used it to find candidates only, not as evidence for any claim.

## 2. Benchmark (Docker, same 25 URLs per tool)

URLs: 20 employer homepages found in the persona run and 5 MyCareersFuture job pages. robots.txt was checked first (none were blocked). Request pacing was 1.5 s. "Name found" means a distinctive employer-name word appeared in the text; it is a rough proxy for "the real page content arrived", not a quality score.

| Tool | Homepages OK (of 20) | Name found | Median s | Job pages OK (of 5) | Name found | Median s |
|---|---|---|---|---|---|---|
| httpx + trafilatura | 16 | 14 | 0.32 | **0** | 0 | 0.05 |
| Lightpanda (via Playwright CDP) | 19 | 19 | 0.54 | 5 | 2 | 1.05 |
| Crawl4AI `/md` (fit) | 19 | 18 | 0.81 | 5 | 2 | 0.73 |
| Steel `/v1/scrape` | 19 | 17 | 0.93 | **0** | 0 | 0.23 |
| Playwright (Chromium, new browser per URL) | 19 | 19 | 2.52 | 5 | **5** | 3.22 |

- `en.chinaconstruction.cscec.com` failed everywhere with an invalid certificate, so the one error per tool is the site, not the tool.
- **Job pages are the discriminator.** MyCareersFuture is a JavaScript app. Plain fetch got an empty shell. Steel's single scrape call returned only the logo, so it did not wait for the content. Lightpanda and Crawl4AI returned content but often only a fragment (548 and 993 characters at the median, against 5,489 from Playwright). I did not tune waits for any tool, so the shortfall may be fixable.
- **Memory (Docker stats, idle, then after a run):** Lightpanda 3 MB, then 29 MB; Crawl4AI 327 MB, then 550 MB; Steel 396 MB, then up to 2.1 GB; Playwright used a throwaway container that was not measured separately.
- **Image sizes:** Lightpanda 225 MB, Playwright Python 3.4 GB, Steel 3.8 GB, Crawl4AI 8.2 GB.
- Playwright's time includes starting a new browser for each URL. A kept-alive browser would be much faster, so its 2.5 s is a worst case.

## 3. Problems found while testing

1. **Lightpanda refused the connection by hostname.** `ws://lightpanda:9222` returned `403 Host not allowed`; it worked when I used the container's IP address. A service needs to handle this.
2. **Lightpanda sends telemetry by default.** Its startup log showed `telemetry disabled=false`. I set `LIGHTPANDA_DISABLE_TELEMETRY=true` in the compose file; I did not verify that the setting stops it.
3. **Lightpanda's compose command was wrong at first** (the image already starts the server; overriding the command broke it).
4. **Crawl4AI's output starts with cookie-banner text** on every MyCareersFuture page, so extracted text still needs cleaning.
5. **Steel's scrape endpoint has no obvious wait option** in what I called; the job-page failure is a consequence of how I called it.

## 4. Recommendation

1. **Tier 1: `httpx` + `trafilatura`** (already in the pipeline). It is fast, tiny, and handled 16 of 20 homepages. Escalate when the text is under about 200 characters.
2. **Tier 2: a Playwright render service**, in a container of our own with a small HTTP wrapper. Reasons: Apache-2.0, official Microsoft image, it produced complete text on every page that loaded, and we control waits, timeouts, concurrency and the user agent. Run it as a non-root user with the seccomp profile, a read-only filesystem and dropped capabilities, and keep one browser alive.
3. **Runner-up: Crawl4AI** if we want a ready-made API with markdown output instead of writing the wrapper. It worked out of the box at 0.8 s median, but its default "fit" output was short on job pages and it is the biggest image (8.2 GB).
4. **Watch: Lightpanda.** It is a fraction of the memory and speed cost, but it is AGPL, its first-pass coverage on job pages was partial (fixed with waits, see section 5), and it needs the hostname and telemetry fixes. Revisit as a cheap middle tier after the AGPL question is settled.
5. **Do not use** Firecrawl (heavy, AGPL, unauthenticated by default) or Browserless (SSPL/commercial) for a product.


## 5. Service built and tested (follow-up, same day)

The wrapper is in [`05_prototypes/P04-fetch-render-service`](../../../../../05_prototypes/P04-fetch-render-service/README.md): FastAPI around one long-lived Chromium, plain fetch first and render on a thin result, robots.txt check, honest user agent, bearer token, refusal of non-public addresses.

**Same 25 URLs through the service (`mode: auto`):**

| | Homepages (of 20) | Median s | Job pages (of 5) | Median s |
|---|---|---|---|---|
| Service, auto | 19 OK, name found in 17; 17 answered by the plain tier, 2 escalated to render | 0.57 | 5 OK, name found in 5 | 2.9 |
| Service, render only | 19 OK, name found in 17 | 2.2 | 5 OK, name found in 5 | 2.9 |

The one remaining miss is the site with the invalid certificate. All 5 job pages returned text containing both "responsibilities" and "requirements", so the content is the real job description. Rendering through one kept-alive browser took the Playwright homepage median from 2.5 s to 2.2 s, and auto mode cut it to 0.57 s by skipping the browser for most sites.

**Checks (`outputs/service_checks.txt`):**
- Refused with HTTP 400: `127.0.0.1`, `169.254.169.254`, `10.0.0.1`, `host.docker.internal`, `file://`. A missing token gave 401. A page disallowed by robots.txt (a Google search URL) returned `blocked_by_robots` without being fetched.
- Container runs as `pwuser` (uid 1001) with a read-only root filesystem, all capabilities dropped, a 512-process limit, 2 GB memory limit and Playwright's seccomp profile. Chromium started **with its own sandbox on** (no `--no-sandbox`). Only `/tmp` is writable.
- Memory: 374 MB after the 50-request benchmark, 430 MB after six parallel render requests. Image size 3.76 GB.

**Rerun of the other two tools with waits (job pages only, `outputs/retest_waits.json`):**
- **Lightpanda** with load, network idle and a 3 s settle returned a full description on **5 of 5** pages (4.9k to 11.9k characters, all containing "responsibilities"), at about 6 s each. The earlier gap was missing waits, not missing JavaScript support. Memory stayed under 30 MB.
- **Crawl4AI** with unfiltered markdown returned 3.0k to 10k characters, but only **2 of 5** contained "responsibilities". I did not set a wait, so I cannot say whether it would reach 5 of 5.

**Updated conclusion:** the Playwright-based service holds up as the recommended render tier. Lightpanda moves from "incomplete" to "viable as a lighter tier" once waits are set, with the AGPL licence, the hostname 403 and the telemetry default still to resolve. Crawl4AI stays the ready-made alternative but needs wait settings tested.
