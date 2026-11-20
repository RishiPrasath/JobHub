# JobHub scope

Status: **v1 direction agreed by the owner on 2026-11-20** ([0003](decisions/0003-v1-scope-answers.md), [0002](decisions/0002-round-10-must-have-review.md)). Feature `scope` values on the board below are unchanged: they stay `candidate` or `later` until the gates in [03_features/README.md](../03_features/README.md) are met. Levels are provisional.

## Accepted so far

- The four proposed feature ideas should work across the full job journey. This is a direction, "not a final MVP, platform, architecture or implementation commitment" ([decision log](../strategy/08_decision-log.md)).
- The standalone interview feature is deferred.
- The product surface stays open; v1 must work well on a phone.
- Profile comparison follows the candidate profile ([0001](decisions/0001-profile-comparison-after-profile.md)).

## v1 direction (owner, 2026-11-20)

v1 is a single-posting review for Singapore job seekers, built now and tested with simulated profiles. Users: early-career (0 to 3 years), mid-career switchers, and lower-wage, shift or gig workers. Principles: no fit scores or verdicts, never invent resume claims, decide before you apply, free in v1.

| Area | Decision | Status | Source |
|---|---|---|---|
| Intake | Paste box plus URL fetch of one user-chosen page, one shared posting schema, paste as fallback; first result in 60 seconds or less; source and date recorded; screenshot later | Decided | 0003, 0002 M1 |
| Posting review | Quote every finding with a link to its line; red flags also name a dated official source; no score or label; "what this review didn't check" footer | Decided | 0002 S1 |
| Red flags | Five categories: scam signals, exploitative terms, toxic environment (weaker signals), unfair hiring (TAFEP), vague or misleading; text-only in v1; JobHub identifies only, no reporting; plain info lines such as "1799" allowed | Decided | 0002 M2, M3 |
| Salary and age | Salary quoted or "not disclosed" (information, not a flag); posted and closing dates; stale notice; salary sense checks | Decided | 0002 M4 |
| Employer identity check | ACRA facts for legal names; brand matches labelled "possible"; hidden employer stated with a prompt to ask who the client is | Decided; method to explore | 0003, 0002 M5 |
| Brand-to-company identity card | Website step plus combined card (ACRA, MOM agency directory, .gov.sg, LinkedIn badge) with "doesn't prove" lines | In scope; logic to design | 0002 S3 |
| Company vs contact | Text mismatches and domain check in v1 | Decided | 0002 S2 |
| Singapore rules pack | Rules panel, public rules page, upkeep with owner sign-off | In scope; design to discuss | 0002 S4 |
| Questions to ask the employer | Built from the posting's gaps; option not chosen (E12: 38% against an 80% bar) | In scope; needs discussion | 0002 S5 |
| Profile management | Full profile, edit by hand or via chatbot as proposed changes; resume upload confirmed field by field | Decided | 0003, 0002 M6 |
| Preferences and deal-breakers | Pay floor, arrangement, job type; deal-breakers from a built-in list plus custom, hard or soft; each checked against the posting by quoting the line | Decided | 0003, 0002 M6 |
| "What am I missing" | Hard facts plus "not found in your profile" list, quoted, no score | Decided | 0002 M7 |
| Chatbot and tailored documents | Tailored resume and cover letter as separate records tied to a captured posting; built from a chosen base resume version (several allowed); selection first, then approved rewording after a retest; free PDF and Word | Decided | 0003, 0002 M8 to M10 |
| Claim linking | Every line linked to a profile fact; unlinked lines block export; optional "can you explain this?" check | In scope; details to discuss | 0002 S6 |
| Search-link builder | Links per board with supported filters and saved searches prefilled from preferences; fetches nothing | Decided | 0003, 0002 M12 |
| Company research | Experimental; quoted, dated, sourced cards, never scores; best sources and what to watch for undecided | In scope (experimental); needs discussion | 0003, 0002 S9 |
| Decide before apply | Never applies, bulk-applies or fills forms; "ready to apply?" checklist; copy-ready data panel for the user to paste into employer forms | Decided | 0002 S12 |
| Saved-jobs list and decision record per job | Options presented, not chosen | Pending; discuss together | 0002 M11, S7 |
| Pricing and privacy | Free in v1; pricing principles kept for later; privacy notice before any real resume upload | Decided | 0002 M13, M14 |

## To explore

- LinkedIn data-export import feasibility (0002 M6).
- Market pay comparison and its data source (0002 M4; FEAT-009).
- Fuller strengths-and-gaps narrative and transferable-skills mapping (0002 M7).
- Pasted recruiter messages and chat screenshots (0002 S2).
- Job-posting search service from portals: legal grey zone in Singapore; read MyCareersFuture and Jobstreet terms and robots.txt; get legal review before any build ([legal note](../01_research/rounds/R10-competitor-features-and-differentiation/2026-11-21-scraping-legal-note.md)).
- Employer lookup method and company research sources (0003).
- Preference improvement ideas, saved for later (0002).

## Board

Generated from `03_features/` by `tools/validate.py`. Do not edit between the markers.

<!-- BOARD:BEGIN -->
| Feature | Scope | Need | Feasibility | Result | Next |
|---|---|---|---|---|---|
| [FEAT-001 Employer identity check](../03_features/FEAT-001-employer-identity-check.md) | candidate | N2 | T3 | mixed | ASM-001 |
| [FEAT-003 Verification questions](../03_features/FEAT-003-verification-questions.md) | candidate | N2 | T2 | fail | ASM-003 |
| [FEAT-006 Red-flag evidence from official sources](../03_features/FEAT-006-official-red-flag-evidence.md) | candidate | N2 | T2 | mixed | ASM-006 |
| [FEAT-007 Discriminatory and harmful signals pack (Singapore)](../03_features/FEAT-007-harmful-signals-pack.md) | candidate | N2 | T2 | inconclusive | ASM-007 |
| [FEAT-009 Pay benchmark with stated basis](../03_features/FEAT-009-pay-benchmark.md) | candidate | N2 | T2 | inconclusive | ASM-009 |
| [FEAT-013 Offer and contract checks](../03_features/FEAT-013-offer-and-contract-check.md) | candidate | N2 | T1 | inconclusive | ASM-013 |
| [FEAT-002 Single-posting review with source-linked claims](../03_features/FEAT-002-single-posting-review.md) | candidate | N1 | T2 | mixed | ASM-002 |
| [FEAT-005 Paste capture with snapshot and stale notice](../03_features/FEAT-005-paste-capture.md) | candidate | N1 | T2 | mixed | ASM-005 |
| [FEAT-008 Employee experience and reviews](../03_features/FEAT-008-employee-experience.md) | candidate | N1 | T2 | fail | ASM-008 |
| [FEAT-004 Accept, edit, reject and decision record](../03_features/FEAT-004-review-and-decision-record.md) | candidate | N1 | T1 | inconclusive | ASM-004 |
| [FEAT-010 Profile and preference comparison](../03_features/FEAT-010-profile-comparison.md) | candidate | N1 | T1 | mixed | ASM-010 |
| [FEAT-011 Evidence-linked resume suggestions](../03_features/FEAT-011-resume-suggestions.md) | candidate | N1 | T1 | inconclusive | ASM-011 |
| [FEAT-015 Interview practice](../03_features/FEAT-015-interview-practice.md) | candidate | N0 | T0 | none | ASM-015 |
| [FEAT-016 Candidate profile](../03_features/FEAT-016-candidate-profile.md) | candidate | N0 | T0 | none | ASM-016 |
| [FEAT-017 Initial setup of job preferences](../03_features/FEAT-017-initial-setup-job-preferences.md) | candidate | N0 | T0 | none | ASM-017 |
| [FEAT-012 Application tracker and reminders](../03_features/FEAT-012-application-tracker.md) | later | N1 | T0 | none | ASM-012 |
| [FEAT-014 Autofill without retyping](../03_features/FEAT-014-portal-autofill.md) | later | N1 | T0 | none | ASM-014 |
<!-- BOARD:END -->

## Decisions needed

1. **First slice:** decided 2026-11-20: posting review with the employer identity check in v1 ([0003](decisions/0003-v1-scope-answers.md)).
2. **Profile comparison:** decided 2026-11-10, later, after the profile is built ([0001](decisions/0001-profile-comparison-after-profile.md)).
3. **Company research sources:** open; to discuss (0002 S9).
4. **First user and target outcome:** decided 2026-11-20: three user groups; proposed success measure in 0003.
5. **Earlier approvals:** `reports/10` calls the hypothesis "approved", but no decision is logged. What actually happened?
6. **Third-party text in git:** ignored in E09, tracked in E10. Which policy applies?
7. **Open from 0002:** saved-jobs list and decision record (M11, S7); identity-card logic (S3); rules pack design (S4); employer questions (S5); claim-linking details (S6).

## Deferred, judged later on practicality

Fit scores and hiring prediction, scam or legitimacy verdicts, auto-apply and employer messaging, continuous employer monitoring. Owner decision 2026-11-20: this list is not locked ([0003](decisions/0003-v1-scope-answers.md)). Automatic resume and cover letter generation is no longer rejected: it is in v1 with human verification and claim linking. Job-board crawling is reopened as an exploration item only. Sources: `reports/09` and `reports/13`.

## Next step

Discuss the open items above, then start build stage 1 (posting input, shared posting record, posting review with deal-breakers, search links) and test with simulated profiles.
