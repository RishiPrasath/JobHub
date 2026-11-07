# Findings: registry-first company research flow

Run 2026-11-07. Prototype 05 against 14 cases whose expected headlines were committed before the flow was built (`tests/cases.json`, commit `fcaefda`). The cases are mine, there are only 14, the model step is non-deterministic, and several fixes below were made after seeing a failure. Read the numbers with that in mind.

## Short answer

The flow works end to end as a Docker service and gave the expected headline on every case it completed. Its most valuable behaviour is the one the earlier experiment failed at: a lookalike employer was **not** called real. Its weakest point is evidence quality, not verdicts: with restricted review sites linked out, what it can read about a company is mostly the company's own pages, news, and registry directories, and it has little or no employee experience.

## Results by run

| Run | Code | Cases | Result |
|---|---|---|---|
| 1 | first version | all 14 | **14 of 14 as expected** (8 seen before, 6 new), 0 dangerous |
| 2 | page selection changed (below) | the 11 that use the web | 10 as expected, **1 dangerous**: Avanguarde (c03) rated `exists_and_consistent`, on my pre-registered "wrong" list |
| 3 | registry mirrors no longer count as independent (below) | c01, c02, c03, c09 | 4 of 4 as expected |
| final | the same code, a later model-wait cap added by someone else | all 14 | **13 of 13 completed as expected**; c11 did not complete in this run (the Docker services were stopped by something other than me partway through, see below). **c11 was then re-run on its own after the services were restarted: as expected (`could_not_confirm_company`, 76 s)**, so all 14 are as expected, though not all in a single uninterrupted run |

Cleanest numbers: **run 1's six new cases were 6 of 6** on the original design, before any fix. After the fixes, the three new web cases (c09 to c11) were still as expected where they ran.

Notes on cases that tell you something:
- **c08 lookalike "DBS Bank Singapore Recruitment Pte Ltd" -> `likely_lookalike`** in every run. The registry's closest name is DBS Bank Ltd, and the exact posted name appeared in no page and no search result. This is the case experiment 09's model rated "real, high confidence".
- **c04 to c06 brands (Grab Holdings, Ninja Van Singapore, KPMG Singapore) -> `brand_legal_entity_unconfirmed`**: the registry has no entity with that exact name, the web clearly uses it. Right answer, but resting on a rule (the exact name seen at least 3 times) that I set from experiment 09's eight companies.
- **c07 fictitious and c10, c11 invented lookalikes -> `could_not_confirm_company`** (c10 was `likely_lookalike` in run 1). Both were accepted.
- **c12 to c14** (wrong company ID, struck-off name, government agency) are decided by the registry alone in under a second. They are right, but they test the registry, not the web research.
- **c02 Lazada** moved between `exists_and_consistent` and `exists_limited_evidence` across runs with no code change; both were pre-registered as acceptable. That boundary depends on the model's rating and is not stable.

## Problems found and what changed

1. **Reading budget was wasted on off-topic pages.** Run 1: of 88 page reads in the 11 web cases, 36 were usable and **40 were off-topic** (generic scam-awareness sites that rank for the "scam" query). For KPMG, none of 8 reads was usable and its brief had nothing to cite. Fix: only read results whose title, snippet or address mention the company. Run 2: of 70 reads, 56 usable, 4 off-topic; KPMG went from 0 to 8 usable pages.
2. **Registry directories were counted as independent corroboration.** Avanguarde's four "agreeing" pages were three sites that republish registry records (sgpbusiness, companies.sg, recordowl) and one government job posting; the headline said "public sources agree". My pre-registered expectation (limited evidence) was right. Fix: those sites no longer count toward "several sources agree". **This fix was made after the failure, so c03 is no longer a clean test.**
3. **A registry outage was worded as a registry finding.** With the registry unreachable and the web using the exact name, the headline said the registry had no such entity. Now it is `web_evidence_only`: "the registry could not be reached, so existence as a registered company is unchecked."
4. **The model step could hang for 14 minutes.** The free-tier model hit its limit and my retry loop honoured very long retry delays (two cases took about 14 minutes). Someone else added a cap that fails fast into "summary unavailable"; I kept it.

## Outages (live, then also as unit tests)

Pointing the flow at a dead service, one at a time, on a company whose searches were cached:

| Down | What the output said |
|---|---|
| Registry | `registry_unavailable`; headline `web_evidence_only`, never "exists" |
| Search | `search_unavailable`; headline `exists_limited_evidence`; "not evidence that nothing is wrong"; no summary written |
| Page reader | stopped after two failed reads; summary written from search snippets only; reader error listed |
| Model (bad key) | `summary_unavailable`; headline and sources still returned |

24 no-network tests cover every headline row and these outages, restricted-site handling, the time budget, the off-topic filter and the registry-mirror rule.

## The HTTP service

Checked: `POST /research` returns a job, `GET /research/<id>` returns state, result and a readable text version, an identical request within an hour is served from cache, `/status` shows whether the registry, search and reader are reachable, and four kinds of bad input (missing, empty or too-long employer, invalid JSON) return 400, an unknown job 404, and other methods 405.

## What it cannot do (the important part)

- **It does not read employee experience.** Glassdoor failed 21 of 21 reads in experiment 09, Reddit returned a bot challenge, and LinkedIn, Indeed and JobStreet are deliberately linked out under the default policy because their terms restrict automated access (not re-checked in this session). So a brief for a well-known company is mostly company pages, news and registry data, plus an "open these yourself" list of review links (13 for Raffles). The draft plan in `_drafts/company-research-service-plan.md` puts Glassdoor, Indeed, JobStreet and Reddit first; this result says those are the sources a respectful automated reader can least get.
- **It cannot tell two companies with the same exact name apart** unless both are live in the registry.
- **Page reading is by the fetch service with an honest identity and robots.txt checks**, so some sites that a real browser can read will refuse it (3 pages blocked by robots.txt in the 11 web cases).
- **The brand rule is fragile.** `brand_legal_entity_unconfirmed` needs the exact name seen 3 or more times in pages and search results; KPMG had 3 in the earlier experiment and 10 here. A less-covered brand would fall to `could_not_confirm_company`.
- **Model quality varies.** Some claims are labels rather than statements ("Legal name and registration details"); the quote check proves a quote exists in a source, not that the source is about the right company, which is why the gate and the headline logic exist in code.

## Not done

- The final regression was never one uninterrupted run of all 14: 13 completed together and c11 was re-run alone afterwards (as expected).
- Search was DuckDuckGo in practice in experiment 09. In this flow's final runs DuckDuckGo's circuit breaker opened and Bing answered some queries (visible in the registry-outage test, "bing, duckduckgo"), so fallback was exercised at least once, but not measured.
- No load test, no concurrent-user test, no token-use measurement for this flow.
- The stack was stopped partway through the final run by something other than me; it has since been restarted (search, flow). To run again from scratch, start the four services in the order given in the README.
