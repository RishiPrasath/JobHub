# AI-assisted job seeking and trust

## Executive finding

AI is most defensible as a reviewable assistant for discovery/filtering, requirement extraction, evidence-grounded drafting, interview practice and application organisation. The main danger is not that it produces no value; it makes unsupported, generic or stale content cheap to produce at scale.

## Capability and control matrix

| Workflow | Observed capability | Failure mode | Minimum control |
|---|---|---|---|
| Discovery/matching | Natural-language search and profile/preference matching | Hidden rationale, stale/duplicate results, missed adjacent careers | Show criteria, inclusion/exclusion reasons, freshness, source and confidence |
| Posting summarisation | Extract requirements and provide concise summaries | Omit required/preferred distinction or invent context | Preserve original, timestamp, source and exact supporting text |
| Resume tailoring | Keyword analysis, versions, bullets, summaries and letters | Keyword stuffing, generic language, fabricated metrics, false confidence | Claims ledger, per-claim approval and before/after diff |
| Cover letters | Draft structure and variants from supplied evidence | Repetition, false employer facts, homogenisation | Candidate-specific evidence and human final pass |
| Interview practice | Role-specific questions, recording and feedback | Formulaic feedback, transcription error, unsafe live assistance | Practice/post-session feedback; consent, retention and policy checks |
| Employer research | Multi-source summaries with citations | Stale reviews, defamation, marketing treated as fact | Source tiers; separate facts, signals and unresolved claims |
| Tracking/follow-up | Saved jobs, stages, notes, versions and reminders | Lock-in, incomplete history, wrong status inference | Portable Markdown/CSV/JSON export and manual editing |
| Autofill/automation | Prefill and browser-based navigation | Wrong answers, duplicates, consent/policy breaches, irreversible submission | Draft-only by default; field review and final explicit submit |
| Privacy/retention | Policies differ across general and dedicated tools | Users misunderstand retention, review or training use | Point-of-upload disclosure, redaction, deletion and provider details |
| Browser agents | Read pages and potentially fill forms | Indirect prompt injection or data exfiltration | Untrusted-data boundary, allowlists, sandboxed extraction and action confirmation |

## General-purpose versus dedicated tools

General-purpose assistants are flexible for unusual, cross-industry or research-heavy work, but require users to build the workflow and maintain records. Dedicated tools integrate tracking, matching, resume versions, interview practice or autofill, but may centralise more sensitive data, impose subscriptions, obscure scoring logic and make switching harder. This comparison does not select a provider.

## Trust and ownership principles supported by the evidence

- The user’s evidence ledger should be canonical; AI may propose wording but must not create facts.
- Each meaningful recommendation should expose source, date, confidence and uncertainty.
- Job discovery, drafting, export and submission should be separable permission states.
- Sensitive eligibility, salary, work authorisation, disability, criminal-history and demographic questions should never be auto-answered.
- Postings, resumes, reviews, websites and tool outputs are untrusted content, not instructions.
- Records should remain exportable without requiring an ongoing subscription.
- Privacy, retention, subprocessors and training use should be stated before upload.
- Interview practice should be preferred over hidden live assistance; employer rules and consent matter.

## Bounded evaluation proposal

Before any product or architecture decision, a provider-neutral synthetic/redacted test could compare a manual workflow, a general assistant and one dedicated tool across eight sectors, three experience levels, clear/ambiguous/stale postings, career transitions, missing evidence and adversarial postings. Measures should include unsupported claims, required/preferred classification, provenance, stale-posting detection, genericity, voice preservation, uncertainty calibration, bias under equivalent-profile substitutions, prompt-injection resistance, export completeness, review time and incorrect/unauthorised actions.

Suggested experimental safeguards are zero fabricated credentials or metrics, explicit approval for every consequential claim and submission, complete export, and no accepted subgroup degradation without explanation. These are test thresholds, not product requirements.
