# Prototypes

Stage question: **what does it look like in use?**

| ID | Demonstrates | Status | What it showed | Supports |
|---|---|---|---|---|
| [P00](P00-single-posting-review/README.md) | Evidence-first posting review | UX instrument; no test notes | Nothing recorded | FEAT-002, FEAT-004 |
| [P01](P01-paste-and-capture-v2/README.md) | Paste or link to report | Bounded checks | HTTP 200 does not prove capture | FEAT-005 |
| [P02](P02-persona-job-review-v3/README.md) | Persona lens, capture server | Acceptance list only | Nothing recorded | FEAT-002 |
| [P03](P03-company-research-pipeline/README.md) | Registry service, research endpoint | Registry is live; used by P05 | Tests on unseen names | FEAT-001 |
| [P04](P04-fetch-render-service/README.md) | Robots-respecting page reader | Dependency of P05 and E10 | No per-host limit or retries | FEAT-001 |
| [P05](P05-company-research-flow/README.md) | Registry-first flow with cited brief | Most mature | 14 of 14 expected, not in one run | FEAT-001 |

P05 needs P03, P04 and E09 running. Docker project names are pinned, so existing networks and the registry volume carry over.
