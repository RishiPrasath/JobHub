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
docker compose up -d registry          # first start provisions the current ACRA release by itself (see below)
docker compose run --rm pipeline resolve "Palo IT Singapore"
docker compose run --rm pipeline batch-resolve /samples/postings.json /data/out.json
docker compose run --rm pipeline research "Palo IT Singapore" --site https://www.palo-it.com/
```

- The registry data lives in the `acra-data` Docker volume, never in the image or the repo. `acra-update` forces a fresh download and switch by hand; `acra-status` compares the local copy with ACRA's published release.
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

## Registry matching states (`pipeline/acra.py`)

| State | Meaning |
|---|---|
| `exact_by_uen` | A company ID was supplied and found |
| `exact` | The posted name equals one registered name word for word (sibling entities that only add words are listed in `siblings`) |
| `likely` | Very close name, no extra words in the registered name |
| `needs_confirmation` | Weak match, a brand/extra word was dropped, a former or alternate name matched, the registered name adds words, or two live entities share the name. A person should confirm |
| `public_body` | Looks like a statutory board or ministry; these are not in the company datasets |
| `unresolved` | Nothing in the registry contains the name |

Checks (run inside the container, see `tests/`): `acra_personas.py` resolves the persona-run employers by persona; `acra_random_names.py` and `acra_shortened_names.py` test 300 and 211 registry names that were not used for tuning.

## Registry service: self-provisioning and self-refreshing (`pipeline/registry.py`)

`docker compose up -d registry` starts a small HTTP service on `127.0.0.1:8090`. Nothing is baked into the image or the repo; the data lives in the `acra-data` volume.

1. **Provision on start.** It asks data.gov.sg when the ACRA collection was last updated and compares that with the copy in the volume. With no copy (first provision) it downloads all 27 files (about 641 MB, about 4 minutes), builds the index, checks it, and only then goes live. Until then `/health` returns 503 and `/resolve` returns 503 with `Retry-After`; `/status` shows the step and file count.
2. **Refresh while running.** Every `ACRA_CHECK_HOURS` (default 24) it repeats the cheap timestamp check. On a new release it builds a new index beside the live one, checks it, and switches by rewriting `registry.json`. The previous index is kept until the next refresh.
3. **Separate worker.** Downloading and indexing run in a child process at low priority, so a refresh cannot slow lookups (tested at 95% CPU) and a worker that dies cannot take the server down. A lock stops two refreshes on one volume.
4. **Failure keeps serving.** A failed download or check is recorded as `last_error` in `/status`; the old copy keeps serving; it retries after `ACRA_RETRY_MINUTES` (30), or every 1 to 15 minutes while there is nothing to serve yet. Downloads resume: finished files are kept, and files are written as `.part` and renamed so a crash never leaves a half file that looks complete.
5. **Checks before going live.** Row counts agree, at least `ACRA_MIN_ROWS`, no more than a 10% drop from the last index, a test lookup works, every file has the expected columns, and the release did not change during the download. The disk needs `ACRA_MIN_FREE_GB` (1.5) free before a refresh starts.
6. **Age is visible.** `/status` shows `registry_as_of`, `age_days`, `stale` (older than `ACRA_MAX_AGE_DAYS`, 45), request counters and latency. Every `/resolve` answer carries `registry_as_of` and `registry_stale`.
7. **Self-test, nightly and after every refresh** (`pipeline/selftest.py`). It looks up 12 long-lived companies by name and by registry ID, checks that a nonsense name is not matched and that a statutory board is recognised as a public body, and checks entity counts, the live-company share, lookup speed, release age and free disk. The result is in `/status` (`selftest`) and `/health` (`degraded`); `GET /selftest` runs it on demand (about 0.3 s). It runs when the first index appears, then at 18:00 UTC (02:00 Singapore, `ACRA_SELFTEST_HOUR_UTC`). If an index fails it right after a refresh and the previous index passes, the service switches back to the previous index, records why in `last_error`, and skips that release until ACRA publishes the next one. A canary company can legitimately change (a rename or merger): the name check passes at 80%, and the failing names are listed so a canary can be retired in `selftest.py`.
8. **Protected against bad input.** Names and hints over 200 characters get 400 (one 5,000-character name used to run the container out of memory), lookups are read-only, abort after 8 s (504), at most `ACRA_MAX_CONCURRENT` (16) run at once (else 503), all errors are JSON, and the container has a 1.5 GB memory limit, a process limit and a clean SIGTERM shutdown.

```bash
curl localhost:8090/status
curl 'localhost:8090/resolve?name=Palo+IT+Singapore'
python tests/registry_probe.py      # 25 probes: bad inputs, the self-test endpoint, and a 400-request load test
```

Disk: about 0.9 GB at rest (the live index and the previous one) and about 1.7 GB while a refresh runs. A company registered after the latest ACRA release will not be found until the next release, which is why answers carry the registry date. The pre-existing `acra_csv` folder from the older CLI flow is not removed automatically.

Failure-path tests: `tests/registry_stubs.py` (release changes mid-download, low disk, wrong file format, index too small) and `tests/selftest_stubs.py` (bad index detected, corrupt file, rollback, rejected release skipped, no previous index).

