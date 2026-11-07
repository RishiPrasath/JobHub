# Agent test: can an expert employer researcher do the job with OpenSERP?

Run 2026-11-07, after the scripted harness (Phase 3). Nine independent agents, each briefed as a former recruiter and HR analyst advising a job seeker, were given only OpenSERP (search and page extraction) and a budget of 12 searches and 10 page reads. Eight chose a company in an industry I assigned; the ninth was asked to vet an offer from a company I made up, without being told it was made up. Their brief is `outputs/agents/BRIEF.md`; each agent's report, structured assessment and call log is in `outputs/agents/A1` to `A9`.

## Run 2: DuckDuckGo back on, same nine companies, fresh agents

Run 1 (everything below this section) lost most of its search capacity: DuckDuckGo's circuit breaker had opened after the volume we put through it earlier, Google returned a CAPTCHA every time, so Bing carried the load. Before run 2 I checked DuckDuckGo: it had recovered by itself (the breaker only needed a request to close; nothing had to be switched on). I then reran the **same nine assignments with fresh agents who were told not to look at run 1**, telling them to use DuckDuckGo first and Bing second and to skip Google. Brief: `outputs/agents_run2/BRIEF.md`; agents' reports, assessments and call logs: `outputs/agents_run2/`.

**What changed: search got much more reliable and faster.**

| | Run 1 | Run 2 |
|---|---|---|
| Search calls that succeeded | 77 of 95 (81%) | **79 of 82 (96%)** |
| Search failures | 13 timeouts, 3 CAPTCHAs, 2 service errors | 3 timeouts |
| By engine | Bing 77 of 91; DuckDuckGo 0 of 1; Google 0 of 3 | **DuckDuckGo 42 of 45; Bing 37 of 37** |
| Median search time (successful) | 31 s | **13 s** (90th percentile 27 s) |

**What did not change: the answers.**
- Page extraction was the same: 52 of 66 (79%) in run 2 against 58 of 73 (79%) in run 1, with the same generic 502 on Glassdoor (0 of 9 more attempts) and on PDFs and aggregator pages. Several 200 responses were again not usable (a sign-in page from Indeed, a JavaScript notice from Tech in Asia, a bot challenge from Reddit, an almost empty Singlife newsroom page).
- Coverage by need was almost identical: identity answered by all 8 with high confidence again; culture, pay and interview partial and low confidence (15 of 21 low, against 18 of 21 before). Self-scored coverage 2.9 against 3.0, extraction 3.4 against 3.4; only reliability improved (3.6 against 3.0, search relevance 3.8 against 3.9).
- Every one of the 8 agents again rated reliance "with caveats" and advised applying with care; the made-up employer again got "do not proceed and do not pay", with the same careful wording that no trace is not proof of absence. (DuckDuckGo still timed out twice for that agent.)

**Two things the repeat revealed that one run could not.**
1. **Stable facts were stable.** For Ninja Van (12% Singapore cut in August 2025, legal entity Ninja Logistics Pte. Ltd.), GVT (Aalberts acquisition, about 1,800 staff), ECON (TPG take-private, One Aged Care), The Learning Lab (Indeed 3.0 of 5 from 22 reviews, private-equity ownership) and Recruit Express (licence 99C4599, HRnetGroup subsidiary), both runs agreed. The company IDs and registration dates again match the registry.
2. **Findings that depended on query wording were not stable, and one of them was serious.** Run 1's Singlife agent found the regulator's S$93,750 fine on its financial-adviser arm with a specific query ("MAS PIAS Singlife misconduct financial advisers action penalty"). Run 2's agent used a generic one ("Singlife MAS penalty OR complaint OR scam OR fraud"), got noise, and reported **no regulatory penalty found**, with a note that its search was weak. Same tool, same company, opposite red-flag result. Likewise Grab's headcount was a third-party "56K to 58K" in run 1 and "about 11,000 to 12,660" in run 2 (the second matches the 12,000 seen in earlier testing), and Sheng Siong's was a 2010 figure in run 1 and an unverified 4,174 in run 2. About a quarter of all searches in both runs (24 of 95 and 24 of 82) used OR-style queries, which several agents said returned noise.

**What this adds to the answer.** Re-enabling DuckDuckGo fixed a real weakness (reliability and speed of search) and is worth keeping on. It does not change the main finding. Whether a serious red flag is found depends on how well the researcher words a query, which a job seeker cannot be expected to do and an automated system cannot rely on without several targeted, entity-specific queries per risk type (regulator, court, complaints, layoffs, scams) run every time.

## The answer (from run 1; run 2 supports it)

**Partly.** OpenSERP lets an expert researcher answer "is this employer real, who owns it, how is the business doing, has it laid people off, and is the offer a scam pattern?" with sources, in about 10 minutes per company. It does **not** let them reliably answer "what is it like to work there, what does it pay, and how does the interview go?". Those answers came back thin, from snippets, and at low confidence.

| What a job seeker needs | Result across the 8 agents who chose a company |
|---|---|
| Is it a real, operating company? | **Answered by all 8, high confidence each time** |
| What it does, its size and headcount | Partial 7, answered 1. Headcount mostly missing, conflicting (Ninja Van: about 3,000, "1,001-5,000" and "65,000") or third-party estimates (Grab) |
| Financial performance | Answered 3 (the listed or large ones), partial 5. Private and PE-owned firms: thin |
| Layoffs and restructuring | Answered 1, partial 4, **not found 3**. Found well when news covered it (Ninja Van 2024 and 2025, Grab 2023). "Not found" can't be read as "none" |
| Culture and employee sentiment | Answered 1, partial 7; **confidence low in 6 of 8** |
| Pay and benefits | Partial in all 8; **confidence low in 7**. Several Glassdoor snippets were wrong ("SGD 4,100 per year", "SGD 6,023 a year") or conflicting (a nurse at S$1,800 to S$3,575) |
| Interview and hiring | Partial 5, not found 3; low confidence in all |
| Red flags and scams | Partial 6, not found 2. The best result was a regulator fine on an insurer's adviser arm, from a primary source |
| Recent news | Answered 5, partial 3 |

Every one of the 8 agents rated its own conclusion "usable with caveats" for relying on OpenSERP in a job decision: none said yes, none said no. All 8 recommended "apply with care"; the made-up company got "do not proceed and do not pay the fee". Self-reported scores, averaged: search relevance 3.9, extraction quality 3.4, coverage of the job seeker's needs 3.0, reliability 3.0 (out of 5).

## The fake employer (A9)

The job seeker's offer came from "Quillfeather Dynamics Pte Ltd", with a recruiter on messaging apps and an upfront fee. The agent found no company by that name, did not treat the similar names Bing returned as evidence (Feather Dynamics, Quillfeather Analytics, a struck-off Quill Pte Ltd), matched the offer to official scam guidance (ScamShield: pay-upfront jobs are "likely a scam"), and advised paying nothing and verifying the company ID. It was careful to say that not finding a company is not proof it doesn't exist, which is the right calibration. The registry independently confirms no such company exists. This is the strongest result of the test, and it needed no review-site access.

## What I checked independently

- **Company identity, 6 of 6 correct.** Each agent that gave a company ID (A2, A3, A4, A6, A7, A8) gave one that exists in the registry, under the name the agent gave, live; the four that also stated a registration date (A4, A6, A7, A8) were right. For A4, the web research found the legal entity behind the Ninja Van brand (Ninja Logistics Pte. Ltd.), which the registry cannot work out from the brand. In the other direction, the registry confirms the Singapore entity behind Grab (GrabTaxi Holdings Pte. Ltd.), which the agent did not give. A5's insurer and A1's Grab Holdings could not be matched to a registered name by name alone. A9's made-up company is not registered. (`outputs/agents/registry_check_of_agent_claims.json`)
- **One high-stakes claim:** A5's finding that the regulator fined Singlife's financial-adviser arm S$93,750 is present in the saved search result from the regulator's own page.
- **Not checked:** financial figures, ownership changes, review ratings and layoff numbers beyond the above. They are cited but I did not open the sources myself. Several agents flagged their own conflicts (for example Grab's profit figure, and a data-site claim about Singlife's acquisition that "looks wrong").

## How the tool behaved (168 calls in the logs)

- **Search: 77 of 95 succeeded (81%).** Failures: 13 timeouts (HTTP 504), 3 Google CAPTCHAs (429), 2 service errors (503, one was DuckDuckGo's disabled engine). **Bing did nearly all the work** (77 of 91 calls). All 3 Google calls and the 1 DuckDuckGo call failed. In this run there was effectively one working search engine.
- **Search latency: median 31 s, 90th percentile 37 s.** This is inflated: nine agents queued on one engine with a 10-a-minute cap. A single user alone saw about 3 to 6 s per query in earlier tests. Under any real concurrency this setup is slow.
- **Page reads: 58 of 73 returned content (79%), about 1 s each.** All 15 failures were the same generic 502. **Glassdoor failed 8 of 8.** Also failing: stockanalysis, financecharts, SGX links, scamadviser, complaintsboard, compworth. Indeed and JobStreet usually read well (one agent hit a cookie wall), Straits Times, company sites, registry directories, Wikipedia, news and regulator pages read well. Reddit returned success twice, but the agents that opened it reported a bot challenge, so HTTP success overstates what was usable.
- **Agents had to cope with failure, and did:** they retried once, waited, switched query wording, used search snippets where a page failed, and reported what they couldn't find rather than filling it from memory (they kept a separate "from memory, unverified" list, and kept it small).

## Why the culture, pay and interview answers are weak

The sources where employees describe their experience are the ones the tool reads least well: Glassdoor (0 of 8), Reddit (challenge page). Indeed and JobStreet worked, but their terms restrict automated access and the production flow deliberately does not read them. What is left is rating numbers from search snippets, a handful of reviews from JobStreet and Indeed, and market salary benchmarks that are not specific to the company. Those are real signals but low-confidence ones, and several snippet figures were plainly wrong.

## What this means for the product

- OpenSERP is worth keeping as a **discovery and reading layer for the factual brief**: identity and ownership, finances, layoffs, news, regulator actions and scam patterns. Combined with the company registry (which confirms the legal entity) it covers the "is this real and what is going on with the business" half of the job.
- It does not make **working culture, pay or interview process** a solved problem. Closing that gap needs different sources, not a better search: licensed or permitted review data, job seekers' own contributions, and primary Singapore sources such as the regulator and enforcement lists (the best single finding in the test).
- Operationally, one engine was carrying the load. A real deployment needs a second working engine or a licensed search API, and a queue that doesn't turn every query into a 30-second wait.

## Limits of this test

Nine companies, one run, and only the identity claims and one regulatory claim verified. Agents graded themselves. They were limited to 12 searches and 10 page reads, which one agent said forced reliance on snippets; a bigger budget might have helped culture, pay and interview coverage somewhat, but not the blocked sites. The agents are the same model family as the one that built the tool, and I did not repeat any run, so there is no estimate of variation. Agents read some sites (Glassdoor, Indeed, JobStreet, Reddit) once each through a tool that presents itself as a real browser; that is a terms-of-service risk a product would not take. Eight of nine agents could not save their own `report.md` (the harness refused subagent report files), so I saved their returned text as `report.md`, labelled as transcribed. A7 chose a company larger than the small one requested. A9's message said it wrote a report and assessment file, but neither exists, and it counted 6 successful searches where its log shows 5.
