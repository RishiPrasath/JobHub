# Round 10 brief — Competitor features and differentiation

Date started: 2026-11-21

## Decision this round informs

Which features JobHub v1 must have to be credible next to existing tools, and which features should carry its positioning. This round does not change scope; scope decisions belong in `06_scope/decisions/`.

## JobHub v1 scope used as the yardstick

1. Posting review with quoted facts and Singapore red flags
2. Employer identity check
3. Light preferences and deal-breakers
4. Paste and URL intake
5. Profile management
6. Chatbot with human-verified tailored resumes and cover letters stored per job
7. Search-link builder (builds search URLs for other boards; no crawling)
8. Experimental company research

Principles: no fit scores or verdicts, never invent resume claims, decide before apply, simple pricing.

## Competitor groups (one run each, in parallel)

| Run | Group | Excludes (already covered) |
|---|---|---|
| A | AI job-search agents and application copilots | AIApply, Jobright, Simplify, Sonara, Teal, Careerflow, Jobscan, Huntr |
| B | Resume, cover-letter and ATS tools | Teal, Jobscan, Rezi, Kickresume, Huntr, Careerflow, AIApply |
| C | Posting, scam and ghost-job checkers; employer verification | — |
| D | Company and employer research tools | — |
| E | Singapore and Southeast Asia platforms | Only new features for MyCareersFuture, Jobstreet, LinkedIn |

## Evidence standard

| Label | Meaning |
|---|---|
| **V-site** | Read directly on the vendor's or owner's page on the run date |
| **V-3p** | Read directly on a fetched third-party page |
| **2nd** | Reported by a third party citing a source that was not fetched |
| **I** | Inference, or "not found" on the pages read |

Competitor-written reviews are used for facts only. No logins, purchases, accounts, form submissions or posting-checker submissions.

## Tooling

The owner asked for subagents using the Kimi WebBridge CLI. It is installed (`kimi-webbridge` v1.11.3, skill v1.11.0). Its daemon was started for this round. At the first check its Chrome extension was not connected; by the time the five runs started it was, and all five runs used it (read-only, one session per run) for pages that block plain fetches, alongside WebSearch and WebFetch. The daemon reported a version mismatch with the extension (v1.11.3 vs v2.0.x) but calls worked. WebBridge used the owner's own browser, so some pages showed personalised elements; no personal data was recorded. Bot checks (Cloudflare, Akamai) were not bypassed. Each run's `sources.md` records the tool used per page.

The research subagents were not permitted to write files, so the round lead saved each run's `findings.md` and `sources.md` from the subagent's returned report.

## Stopping rule

One bounded pass per group, roughly 8 to 10 products each. Gaps go to `decision-gate.md`, not to an open-ended second pass.
