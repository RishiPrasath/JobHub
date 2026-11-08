# Limitations

- **Small sample:** 25 URLs, one run per tool, from one country and one job board. Not representative of the web.
- **Quality proxy is weak.** "Name found" and character counts do not show that the extracted text is the right or complete content. I did not read the extracted text for correctness. Crawl4AI's markdown and Playwright's raw `innerText` are different outputs (pruned markdown vs everything on the page), so character counts are not directly comparable.
- **No tuning.** Wait conditions, page timeouts and filter settings were left at defaults for Crawl4AI, Steel and Lightpanda, and a fixed load-then-8-second wait was used for Playwright. Results could change a lot with tuning.
- **Playwright timing includes browser start-up for every URL.**
- **Memory figures are one `docker stats` sample after each run,** not peaks.
- **Not benchmarked:** Puppeteer, Selenium, Rod/chromedp, Scrapy, Crawlee, Scrapling, Jina Reader, and the agent layers. Their rows in the survey come from repository metadata and READMEs only.
- **Evasion tools were not run,** on purpose. Statements about them come from their repository descriptions.
- **Pages read through WebFetch are summaries by a small model.** Licence text for Browserless was quoted from that summary and should be checked in the repository before any commercial decision. AGPL and SSPL implications are not legal advice.
- **No live check of Jina's hosted limits or Browserless's commercial pricing.**
- **The "last push" date is not a release date;** I did not check releases or issue health beyond counts.
- **Search results from Google were vendor-written comparison posts** and were not used as evidence.
- Docker ran on a single Windows machine with 15.5 GB of memory.

## Added with the service test
- **The wrapper test used the same 25 URLs** the tools were first compared on, so there is no unseen test set. Nothing was tuned on the pages, but the numbers are not an independent estimate.
- **The "responsibilities/requirements" check** is a keyword test on five pages, not a read of the text.
- **Security checks were a short list of probes:** no DNS-rebinding test, no redirect-chain test beyond the final URL, no test of hostile pages, and no load test beyond six parallel requests. The seccomp profile is Playwright's published one, not reviewed by me.
- **Crawl4AI and Lightpanda waits were tried once** on five pages, with one wait setting each.
- **One robots.txt probe** (a Google search URL) was used to confirm blocking works.
- **Image size 3.76 GB** is large; a slimmer build was not attempted.
