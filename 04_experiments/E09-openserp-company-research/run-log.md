# Run log, 2026-11-07

Commands and outcomes, in order. Times are local (Singapore). Nothing here is reconstructed from memory: each line corresponds to a tool call in the session.

## Setup
1. `docker info` failed: Docker Desktop was not running. Started it (`Start-Process "Docker Desktop.exe"`); the engine answered after about 1 minute. The registry and SearXNG containers from earlier work restarted by themselves.
2. `git clone --depth 1 https://github.com/karust/openserp.git vendor/openserp` -> commit `98f42fb`, tag v0.8.18 (2026-11-03). GitHub API: 1,556 stars, MIT, Go, 26 open issues, pushed 2026-11-03.
3. Read the full README, `Dockerfile`, `docker-compose.yaml`, `config.yaml`, `docs/openapi.yaml` (error shapes), `extract/` sources.
4. Source checks: no telemetry beyond blocking tracker domains; extraction code has no robots.txt handling; blocked-page detection in the extractor is HTTP status only (`403/401` -> "blocked", `429` -> "rate limited").
5. `docker compose build` -> image `jobhub-openserp-experiment:0.8.18`, 568 MB (Go build stage, `chromedp/headless-shell` runtime).
6. `docker compose up -d`: container healthy inside, but the host port did not answer (`docker port` empty, published ports `[]`). `docker compose down && docker compose up -d` fixed it. Cause: the first start raced Docker Desktop's startup. Recorded as an operational note.

## Phase 1 check
7. `GET /health` -> six engines `ready`. First search `GET /duckduckgo/search?text=Randstad+Singapore+employee+reviews&limit=5` -> 200 in 1.0 s; envelope `query, meta{took_ms, engines_failed, version}, results[], serp_features, pagination`; result keys `id, rank, type, title, url, display_url, snippet, domain, favicon, position, engine, domain_info`; ads are typed `ad` and carry long tracking URLs.

## Phase 2
8. Engines (`phase2_engines.py`, 6 x 2 queries, 8 s apart): DuckDuckGo, Bing, Google answered (1.0 s, 3.3 s, 3.6 s); Ecosia 403 `blocked`; Yandex 429 `captcha_detected` (service logged "skipping retries"); Baidu answered, but the obscure query returned junk domains.
9. Extraction (`phase2_extract.py`): 12 pages; results in REPORT.md. Reddit returned HTTP 200 whose content was a "Prove your humanity" challenge (490 real characters plus a large inline image); Glassdoor returned 502 `extract_failed`.
10. Identity and private addresses (`phase2_identity.py`): main service rejects loopback, link-local metadata address, private container address and `file://` with 400 `INVALID_PARAM: target not allowed`. To observe headers, started a second disposable container with the lab switch `OPENSERP_EXTRACT_ALLOW_PRIVATE_NETWORKS=true`:
    ```bash
    docker run -d --name openserp-lab --network 09_openserp-company-research_default --init --shm-size 1g --read-only \
      --tmpfs /tmp:size=512m --tmpfs /home/chrome:size=256m,uid=1001 --cap-drop ALL \
      -e OPENSERP_SERVER_HOST=0.0.0.0 -e OPENSERP_SERVER_PORT=7000 -e OPENSERP_EXTRACT_ALLOW_PRIVATE_NETWORKS=true \
      -v ./config/openserp.yaml:/usr/src/app/config.yaml:ro jobhub-openserp-experiment:0.8.18 serve
    docker compose --profile tools run --rm --name p2echo -e SELF_HOST=p2echo -e OPENSERP_URL=http://openserp-lab:7000 harness python phase2_identity.py
    docker rm -f openserp-lab
    ```
    The echo site saw `Mozilla/5.0 ... Chrome/146.0.0.0` with `sec-ch-ua: "Google Chrome";v="146"` in fast mode and `Chrome/152` in rendered mode; it fetched a robots.txt-disallowed path and never requested robots.txt. Lab container removed.
11. Cache, rate limit, breaker: repeat of a cached query 15 ms then 3 ms; five different DuckDuckGo queries back to back took 0.9 s then about 6 s each (10 per minute); Ecosia circuit opened after 3 failures (`retry_in` 299 s); `mode=any&engines=ecosia,duckduckgo` still returned 200 in 1.2 s.

## Phase 3
12. Smoke test, one agent (`p7-fictitious`): 48.6 s, brief `cannot_verify / low`. Its outputs were deleted before the full run to avoid mixing two runs. The service's one-hour search cache was still warm for that agent's six queries, which is why `p7-fictitious` took only 20 s in the full run; its timing is not comparable with the other seven.
13. Harness fixes made after Phase 2 findings, before the full run: strip inline `data:` images before measuring content, add challenge phrases ("prove your humanity", "not for bots"), and skip pages that never mention the company name.
14. Full run, 8 agents in parallel: 588 s wall, 48 searches (all answered by DuckDuckGo), 64 page reads, 16 model calls, 39,033 tokens. Registry ground truth for the eight companies from the local company-registry service (`outputs/phase3/ground_truth_registry.txt`).
15. Finding: the lookalike "DBS Bank Singapore Recruitment Pte Ltd" was rated `appears_real_and_consistent / high`. Wrote `rescore_gate.py` (deterministic, over saved outputs) after seeing this, so its results are a repair, not an unbiased test.
