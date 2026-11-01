# Prototype 03 — Company research pipeline

A small, free, container-ready pipeline from the [2026-11-01 company research tooling run](../../02_research/03_research-rounds/05_technical-feasibility-and-ai-sdlc/runs/2026-11-01-company-research-tooling/README.md). Python standard library only; no pip install, no paid service, no card.

```text
employer name (+ optional UEN or name hint from the posting)
  -> ACRA registry match (local SQLite from data.gov.sg bulk CSVs)
  -> official site page (plain HTTP, robots.txt checked, blocked = reported as blocked)
  -> Wayback first-capture year
  -> Groq gpt-oss-120b answers 5 fixed questions, each citing a numbered excerpt;
     code rejects any quote that is not in the cited excerpt
```

## Run with Docker

```bash
docker compose build
docker compose run --rm pipeline acra-update
docker compose run --rm pipeline resolve "Palo IT Singapore"
docker compose run --rm pipeline batch-resolve /samples/postings.json /data/out.json
docker compose run --rm pipeline research "Palo IT Singapore" --site https://www.palo-it.com/
```

- `acra-update` downloads about 641 MB from data.gov.sg and builds the index. It is slow on purpose (it waits out the API's 429 limit) and only needs repeating when you want fresher registry data. The data lives in the `acra-data` Docker volume, not in the image.
- `research` needs `GROQ_API_KEY` in the repo-root `.env` (git-ignored). Compose passes it in as environment variables. Only public company pages are sent to Groq.

## Local search: SearXNG in Docker (default), DuckDuckGo as last resort

`docker compose up -d searxng` runs a private SearXNG metasearch container (config in `searxng/settings.yml`: JSON on, limiter off, localhost only). It returns **URL, heading (title) and description** for each result and needs no key.

```bash
docker compose run --rm pipeline search "Palo IT Singapore"
docker compose run --rm pipeline find-site "Curos Learning"   # registry match -> search -> verify page -> cache by UEN
```

`find-site` stores each verified site in `sites.sqlite` (keyed by UEN), so an employer is searched once. Searches are spaced 3 seconds apart (`SEARCH_MIN_INTERVAL`); faster makes SearXNG's Brave engine suspend itself.

**SearXNG is a local proxy, not a local index.** It still depends on Google (via its "google cse" engine) and Brave answering. DuckDuckGo refuses it with a CAPTCHA. If SearXNG itself is unreachable, the pipeline falls back to a direct, unsanctioned DuckDuckGo request (`JOBHUB_ENABLE_DDG=0` turns that off), which is currently blocked too. It is **unsanctioned**: DuckDuckGo's robots.txt disallows `/html` and `/lite`. Guardrails: honest user agent, no header spoofing or proxies, at least 2 seconds between requests, and the first block trips a breaker with no retry. Every candidate site is fetched (robots.txt checked) and must contain the registered name's words before it counts.

**Tested 2026-11-01: DuckDuckGo returned its anti-bot page to this client on the first request, so the module reports `blocked`.** The `duckduckgo-search`/`ddgs` library may get through by imitating a browser; that is deliberately not done here. The rest of the pipeline works without it.

## Resolution states

| State | Meaning |
|---|---|
| `exact_by_uen` | The posting gave a UEN and it exists in the registry |
| `exact` | One live entity matches the name |
| `likely` | One live entity matches but the registered name differs |
| `needs_confirmation` | Sibling entities share the name, the match needed a dropped word (brand names), or the name match is weak. **Ask the user; do not pick** |
| `unresolved` | Nothing in the registry contains the name tokens |

Pass `--uen` when the posting shows one, and `--hint` for a name taken from the posting URL.

## Known limits

- Co-operatives, societies and public bodies may be absent from the corporate-entity datasets (NTUC FairPrice Co-operative is not found; the Foundation is returned and flagged).
- No JavaScript rendering. A page under 500 characters of visible text is reported as `thin`.
- Only one page per site is read, so hiring and careers questions are often `not_found`.
- The rules were tuned after seeing the 15 research postings and have not been tested on a fresh set.
