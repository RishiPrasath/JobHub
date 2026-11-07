# Experiment 09: can OpenSERP power company research for job postings?

Date run: 2026-11-07 (Singapore). Status: complete. Result: **use it with changes**, for a private, low-volume prototype only. Read [REPORT.md](REPORT.md) for the findings, scores and recommendation, and [INTEGRATION-PROPOSAL.md](INTEGRATION-PROPOSAL.md) for how it would plug into the job-posting flow. [AGENT-TEST.md](AGENT-TEST.md) answers the follow-up question: nine independent expert-researcher agents, using only OpenSERP, on companies across industries (result: partly fulfils the purpose; solid on existence and business situation, weak on culture, pay and interviews).

OpenSERP ([karust/openserp](https://github.com/karust/openserp), MIT) is a self-hosted search service that drives a headless Chrome against Google, Bing, DuckDuckGo and other engines, and can read result pages as Markdown. Pinned here at **v0.8.18, commit `98f42fbaf7aa6b60f54c8581369166943b209e28`** (2026-11-03).

## Reproduce

Needs only Docker (Compose v2). The language-model steps need `GROQ_API_KEY` in the repo-root `.env` (free tier; the same file the company-research prototype uses).

```bash
cd _experiments/09_openserp-company-research

# 1. get the pinned source and build the service (about 2 minutes)
git clone https://github.com/karust/openserp.git vendor/openserp
git -C vendor/openserp checkout 98f42fbaf7aa6b60f54c8581369166943b209e28
docker compose up -d --build            # API on http://127.0.0.1:7000 ; first start can race Docker Desktop, run `docker compose down && docker compose up -d` if the port does not answer
curl http://127.0.0.1:7000/health

# 2. Phase 2 probes (each runs in a throwaway python container; standard library only)
docker compose --profile tools run --rm harness python phase2_engines.py     # 6 engines x 2 queries, about 3 minutes
docker compose --profile tools run --rm harness python phase2_extract.py     # 8 page types, about 2 minutes

# 3. Phase 3: eight persona sub-agents in parallel, then the name gate (about 10 minutes, about 40k model tokens)
docker compose --profile tools run --rm harness python phase3_agents.py
docker compose --profile tools run --rm harness python rescore_gate.py
```

`phase2_identity.py` needs a second, disposable OpenSERP container with `OPENSERP_EXTRACT_ALLOW_PRIVATE_NETWORKS=true` (the main service refuses private addresses). Its exact `docker run` is in [run-log.md](run-log.md).

## What is in this folder

| Path | What |
|---|---|
| `docker-compose.yml`, `config/openserp.yaml` | The service: built from source, local-only port, read-only filesystem, all capabilities dropped, request rates cut from 60 to 10 a minute per engine, no proxies, captcha solver off |
| `harness/phase2_*.py` | Capability probes (engines, extraction, identity and private-address behaviour) |
| `harness/phase3_agents.py` | The persona sub-agent harness (queries, search, read, cited brief, quote verification) |
| `harness/rescore_gate.py` | The name gate applied over the saved Phase 3 outputs |
| `outputs/phase1` to `phase3` | Raw results: search responses, page logs, briefs, per-agent logs, summaries |
| `run-log.md` | Commands run and what happened, in order |
| `REPORT.md`, `INTEGRATION-PROPOSAL.md` | The written deliverables |
| `AGENT-TEST.md`, `outputs/agents/`, `outputs/agents_run2/` | The nine-agent expert-researcher test, run twice (run 2 with DuckDuckGo re-enabled): brief, each agent's report, assessment and call log, and the registry check of their claims |

**Not committed:** `vendor/openserp/` (re-created by step 1) and the extracted text of third-party pages (reviews, forum and news pages), which stays on the machine that ran the experiment. Page URLs, outcomes and the briefs, which hold only short attributed quotes, are committed.

## Rules followed

Local Docker only; low request rates (10 a minute per engine, plus the harness's own pacing); no proxies, no captcha solving, no logins; blocked pages were recorded and not retried by other means. One caveat: OpenSERP itself presents a real-browser identity and does not read robots.txt, and the experiment fetched a small number of third-party pages through it. See the legal section of the report.
