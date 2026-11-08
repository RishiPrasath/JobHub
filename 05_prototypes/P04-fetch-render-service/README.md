# 04 — fetch-render service

A small container that fetches a public page and returns its main text. It tries plain HTTP first and starts a headless Chromium (Playwright) only when the plain result is thin. Everything is free and open source (FastAPI, httpx, trafilatura, Playwright, Apache-2.0 / BSD / MIT).

Research behind it: [scraping-tools run](../../01_research/rounds/R05-technical-feasibility-and-ai-sdlc/runs/2026-11-01-scraping-tools/findings.md).

## Run

```bash
docker compose up -d --build
curl -s localhost:8080/health
curl -s -H "Authorization: Bearer local-dev-token" -H "Content-Type: application/json" \
  -d '{"url":"https://www.activate.sg/"}' localhost:8080/fetch
```

Set `FETCH_TOKEN` to change the token. The port is bound to `127.0.0.1` only.

## API

`POST /fetch` with `{"url", "mode": "auto|plain|render", "wait_for": "css selector (optional)", "settle_ms": 0}` returns `status` (`ok`, `thin`, `blocked_by_robots`, `error`), `tier` (`plain` or `render`), `http`, `chars`, `seconds`, `final_url` and `text`.

## Rules it enforces
- Public `http(s)` URLs only; loopback, private, link-local and reserved addresses are refused, including requests the page makes itself and the final redirect target.
- robots.txt is checked (cached 10 minutes) with an honest user agent (`FETCH_UA`).
- Images, media and fonts are not downloaded.
- At most 3 renders at a time (`FETCH_CONCURRENCY`), 30 s page timeout.
- No stealth, no CAPTCHA handling, no login.

## Container hardening
Non-root `pwuser`, read-only root filesystem with a 512 MB `/tmp`, all capabilities dropped, `no-new-privileges`, Playwright's seccomp profile (so Chromium's own sandbox stays on), 2 GB memory and 512-process limits, `init: true`.

## Known gaps
No retries, no queue, no persistent cache, no per-host rate limit (callers must pace themselves), image is 3.76 GB, and the security probes were a short list. Fetching a page that needs a click or a login is out of scope.
