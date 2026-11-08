# Round 05 synthesis

Status: draft synthesis written during the 2026-11 reorganization; owner review pending

Research date: 2026-11-01, Singapore, with a registry recheck on 2026-11-03.

## Question

Which technical, evaluation, model, tooling and development-process assumptions hold up? The three runs actually tested one part of this: whether company and role research can run as a free, containerised service.

## What was done

- [Company research tooling](runs/2026-11-01-company-research-tooling/README.md): pricing and terms claim check, plus experiments on a 15-posting set.
- [Scraping tools](runs/2026-11-01-scraping-tools/README.md): GitHub survey, a 25-URL benchmark in Docker, and a wrapper service built and tested.
- [Persona job search](runs/2026-11-01-persona-job-search/README.md): seven persona agents searched MyCareersFuture, and 34 employers went through the service. A later [registry recheck](runs/2026-11-01-persona-job-search/research/acra-recheck.md) changed the matching rules.

## Key findings

The runs use no confidence scale. "None stated" below still carries the run's own qualifier where it gave one.

| Finding | Confidence | Source |
|---|---|---|
| A $0, no-card stack worked end to end for identity (ACRA bulk data), pages (plain fetch), site history (Wayback) and extraction (Groq with citation checking). It did not work for news (GDELT) or Cloud Run hosting | None stated | [Tooling findings](runs/2026-11-01-company-research-tooling/findings.md) |
| Vendor claims were checked individually, for example Tavily's free tier and Gemini's free-tier data use | Per claim: "Verified", "Partly verified", "Probably true", "Consistent", "Not supported" or "Not checked" | [Tooling findings](runs/2026-11-01-company-research-tooling/findings.md) |
| After the rule fixes, the 15 postings gave 11 exact, 1 likely, 3 needs-confirmation and 0 unresolved registry results | None stated; "a repair of known failures, not evidence of general accuracy" | [Tooling findings](runs/2026-11-01-company-research-tooling/findings.md) |
| Citing numbered excerpts and rejecting unmatched quotes cut unverified quotes from 28% to 7%. This checks the quote, not whether the answer is right | None stated; "suggestive, not statistically tested" | [Tooling limitations](runs/2026-11-01-company-research-tooling/limitations.md) |
| Site discovery: Wikidata returned 9 of 15 (7 correct, 2 wrong) and domain guessing verified 5 of 15 with 1 false positive. Local SearXNG found all 11 employers with a known official site | None stated; the run calls SearXNG "the strongest result so far" and also lists it as "Not recommended" | [Tooling findings](runs/2026-11-01-company-research-tooling/findings.md) |
| Plain fetch handled 16 of 20 homepages and 0 of 5 job pages; Playwright rendered 5 of 5 job pages with the employer name found. Recommendation: plain fetch first, then a Playwright render tier | None stated; "treat the ranking as indicative" | [Scraping findings](runs/2026-11-01-scraping-tools/findings.md) |
| The wrapper service returned all 5 job pages and 19 of 20 homepages on the same 25 URLs, and passed a short list of hardening probes | None stated; "not an independent estimate" | [Scraping findings](runs/2026-11-01-scraping-tools/findings.md), [limitations](runs/2026-11-01-scraping-tools/limitations.md) |
| Lightpanda returned full descriptions on 5 of 5 job pages once waits were set; AGPL, the hostname 403 and the telemetry default remain open | None stated | [Scraping findings](runs/2026-11-01-scraping-tools/findings.md) |
| The persona pipeline works in shape: 23 official sites found for 34 employers, 21 pages readable, 73 supported answers of 100, 3 rejected, 24 not found | "Promising prototype, not a reliable service" | [Persona findings](runs/2026-11-01-persona-job-search/findings.md) |
| Registry matching on the 34 employers moved from 28 exact, 5 needs-confirmation and 1 unresolved to 33 exact and 1 public body. The site step was not re-run | None stated; "a repair, not a test" | [ACRA recheck](runs/2026-11-01-persona-job-search/research/acra-recheck.md) |
| Citation checking cannot catch a wrong site, because a real quote from the wrong company still passes | None stated; the wrong-site calls are one reviewer's hand judgement | [Persona findings](runs/2026-11-01-persona-job-search/findings.md), [limitations](runs/2026-11-01-persona-job-search/limitations.md) |

## What remains unknown

- No run examined AI SDLC or development-process assumptions, despite the round's name and purpose.
- Accuracy on fresh postings, since rules were tuned on the same 15 and 34 employers.
- Answer correctness: no gold answer set or full human review exists.
- Tavily's free tier for long-tail employers, and whether Google's custom-search endpoint survives 1 January 2027.
- News, layoff, turnover and reposting signals, and careers or about pages (one page per site was read).
- A user flow for confirming ambiguous registry matches, and UEN or postal-code cross-checks.

## Limits and internal conflicts

- Samples are small, Singapore-only and from one day. Eight of the 15 tooling postings were added by the assistant, and the 4-agent report that run set out to check was missing.
- The persona site numbers replay saved search results, limited to the top five per query, because SearXNG's engines were suspended.
- The persona findings say "about 4 of 23" sites are doubtful, but name five candidates.
- The persona summary says search throttled after "about two dozen" queries; its detail section describes suspension on a second pass, at about 80 queries in the hour.
- Tooling documents are partly stale within themselves. The README and a "what was not done" note say no Docker image was built, while a later container check ran `acra-update` inside the container. The limitations note says E1 fixes were not re-run, while E1c re-ran them.
- SearXNG's role is unresolved between the E9 result and the recommended-stack table.
- Nothing here is a statement about any employer's conduct or legitimacy, and no stack or architecture is accepted by this round.
