# 05: registry-first company research flow

Given the employer named in a job posting, answer in this order: **does it exist and is it the entity the posting names** (company registry), then **what do public sources say** (search and read), then **write it up with citations and an explicit list of what could not be read or verified**. It implements [the integration proposal](../../_experiments/09_openserp-company-research/INTEGRATION-PROPOSAL.md) from experiment 09.

It is a prototype: local only, stdlib Python, one container. It is a separate attempt from the evidence-first service being built in prototype 03 (`pipeline/service.py`), and does not touch it.

## How it works

```
posting (employer, role?, company ID?, url?)
  1. registry check ........ prototype 03 registry service  /check   exists? which entity? live? lookalike?
       if the registry settles it (ID mismatch, public body, not active, several entities): stop, no web research
  2. search ................ OpenSERP (experiment 09), search only; five entity-aware queries, DuckDuckGo then Bing
  3. read pages ............ prototype 04 fetch service (robots.txt checked, honest identity, private addresses refused)
       restricted sites are never fetched; they are listed under "open these yourself"
       pages are screened: challenge text, too thin, never mentions the company name
  4. name gate ............. the exact posting name must appear in a page or a search result
  5. cited brief ........... model writes claims with quotes from numbered sources; every quote is checked in code
  6. headline .............. derived from registry verdict + gate + evidence; the model's own rating is an input, not the answer
```

### The headline

| Headline | Meaning |
|---|---|
| `exists_and_consistent` | Registered, and several public sources agree it is the company named |
| `exists_limited_evidence` | Registered, but the web evidence is thin or could not be gathered |
| `brand_legal_entity_unconfirmed` | The registry has no entity with this exact name, but sources clearly use it (a brand: Grab, Ninja Van, KPMG here) |
| `likely_lookalike` | The registry's closest name is a different entity and no source uses the posted name. Be careful. |
| `could_not_confirm_company` | Neither the registry nor the web confirms it |
| `ambiguous_entity` | Several live companies share the exact name; a company ID or address is needed |
| `not_active` | Registered, but struck off, in liquidation, ceased, suspended and so on |
| `identity_mismatch` | The company ID in the posting does not match the name, or does not exist |
| `public_body` | A government body; check its own .gov.sg site |
| `web_evidence_only` | The registry could not be reached; sources use the exact name, but existence as a registered company is unchecked |
| `unavailable` | The registry could not be reached and the web does not settle it |

When a company is not confirmed (`likely_lookalike`, `could_not_confirm_company`, and so on), positive facts are hidden and only red flags remain, with a note saying so.

### When something is down

Nothing is turned into "no problems found". Each failure is listed under `degraded` and in the wording:

| Down | What happens |
|---|---|
| Registry | `registry_unavailable`; the headline can never say "exists"; web evidence alone gives at most `web_evidence_only`, or `unavailable` |
| Search | `search_unavailable`; no web summary; "this is not evidence that nothing is wrong" |
| Page reader | stops after two failures; falls back to search snippets, labelled snippet only |
| Model | the headline and sources are still returned, with `summary_unavailable` |
| Time budget (`DEADLINE_SECONDS`, 300) | later steps skipped, `partial: true` |

## Run it

Start the three services it depends on, each from its own folder, then this one:

```bash
cd _prototypes/03_company-research-pipeline && docker compose up -d registry     # company registry (first start downloads the registry, about 4 minutes)
cd _prototypes/04_fetch-render-service      && docker compose up -d                # page reader
cd _experiments/09_openserp-company-research && docker compose up -d --build       # search (see its README for the clone step)
cd _prototypes/05_company-research-flow     && docker compose up -d --build        # this service, http://127.0.0.1:8100
```

The model step needs `GROQ_API_KEY` in the repo-root `.env`.

```bash
# one company from the command line
docker compose run --rm flow research "Raffles Medical Group" --role "Staff Nurse"

# or as a service: research takes up to a few minutes, so it is a job
curl -s -X POST localhost:8100/research -H 'Content-Type: application/json' -d '{"employer":"Ninja Van Singapore","role":"Warehouse Associate"}'
curl -s localhost:8100/research/<id>          # state: queued | running | done | failed ; "result" (full JSON) and "text" (readable)
curl -s localhost:8100/status                 # are the registry, search and reader reachable?
```

Settings are in `docker-compose.yml`: `READER` (`fetch` default; `openserp` only to compare, it looks like a real browser and ignores robots.txt) and `READ_POLICY` (`conservative` default also links out Indeed and JobStreet; `permissive` reads them).

## Tests

```bash
# no network: every headline row and each outage (23 tests)
MSYS_NO_PATHCONV=1 docker run --rm --entrypoint python -e PYTHONPATH=/app jobhub-company-research-flow:dev -m unittest discover -s /app/tests -p "test_flow.py" -v

# live: 14 cases whose expected headlines were committed before the flow was built (tests/cases.json, commit fcaefda)
docker compose run --rm flow cases /app/tests/cases.json /outputs/cases
```

Results and their limits are in [FINDINGS.md](FINDINGS.md).
