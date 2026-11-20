# 0003: v1 scope answers

Status: accepted
Date: 2026-11-20
Decided by: owner

## Context

The scope proposal "JobHub: where we are and proposed first scope" (a Claude Doc, 20 Nov) asked five questions to turn the proposal into a recorded scope decision. The owner answered all five on 20 November and added several items in the same session. This file records those answers. The Round 10 feature-by-feature review that followed is recorded separately in [0002](0002-round-10-must-have-review.md); the number order reflects when each file was written, not when decisions were taken.

These decisions set v1 direction. They do not change any feature's `scope` value, which stays as generated on the board until the gates in [03_features/README.md](../../03_features/README.md) are met.

## Decisions

1. **v1 shape:** a single-posting review for Singapore job seekers, built straight away and tested with simulated profiles.
2. **Employer identity check is in v1** ([FEAT-001](../../03_features/FEAT-001-employer-identity-check.md)); the lookup method is explored first (registry source, brand-to-legal-entity matching, hidden employers).
3. **Light preferences are in v1:** pay floor, arrangement, job type, and deal-breakers from a built-in list plus custom entries, each marked hard (must avoid) or soft (prefer to avoid).
4. **Users:** three groups in Singapore: early-career (0 to 3 years), mid-career industry switchers, and lower-wage, shift or gig workers. Built-in deal-breaker and red-flag lists need a common core plus a few items per group; test postings must cover all three; the screen must work well on a phone. Suggested test order: owner trial, early-career, gig and shift, switchers. Proposed success measure: a decision plus at least 2 real questions within 10 minutes, and higher stated confidence.
5. **Never-do list not locked:** fit scores, verdicts, auto-apply, monitoring and the rest are deferred and judged later on practicality. Employer research and fetching job details are "to be explored", not ruled out.
6. **Build now, test with simulated profiles** across job-seeker types and industries. Risk kept in view: simulated users are not evidence about real job seekers; one or two real users before launch would be a cheap check.

Added in the same session:

7. **Two ways in, one posting record:** a paste box and a URL fetch, both producing the same job-posting fields, each with quoted source text, a saved snapshot and an explicit "not found" for missing fields. Paste is the fallback when a URL can't be fetched. (Refined in 0002 M1.)
8. **Chatbot and tailored documents:** a chatbot for everyday actions (update the profile, scan a posting, update the resume, generate a tailored resume and cover letter). Nothing generated is stored until the user reads and confirms it; every claim must trace to a confirmed profile fact. Tailored resumes and cover letters are stored per job as separate records; several base resume versions are allowed. (Refined in 0002 M8 to M10 and S6.)
9. **Full profile management** ([FEAT-016](../../03_features/FEAT-016-candidate-profile.md)): view, add, edit and delete every section by hand or through the chatbot; chatbot changes show as proposed changes the user accepts; resume upload pre-fills with each field confirmed. Profile comparison (FEAT-010) still follows decision 0001.
10. **Search-link builder** from saved preferences, in build stage 1; JobHub fetches nothing; link formats kept in one config file with a check. (Refined in 0002 M12.)
11. **Company research is experimental:** ships only if source and reliability questions get workable answers; results shown as quotes with source, date and link, never scores or verdicts. Exploration track to widen sources and record access routes and terms. (See 0002 S9.)

Suggested build order (from the proposal): (1) posting input, shared posting record, posting review with deal-breakers, search links; (2) profile management and chatbot; (3) tailored resume and cover letter with claim check and per-job storage; (4) employer identity check and URL fetch, once explored.

## Evidence (finding IDs)

FND-E11-01 (employer check), FND-E13-01 (paste capture), FND-E03-01 and FND-R03-02 (profile comparison), and the E19 result recorded in [FEAT-011](../../03_features/FEAT-011-resume-suggestions.md).

## Consequences

- v1 needs accounts, encryption at rest, export and full delete, because the profile holds right-to-work status, contact details and work history. A privacy notice comes before any real resume upload (0002 M13 and M14).
- Model choice needs early testing (Groq daily limits and model variance in the 10 and 11 November runs).
