# 0002: Round 10 must-have review

Status: accepted (item by item; open items listed below)
Date: 2026-11-20
Decided by: owner

## Context

[Round 10](../../01_research/rounds/R10-competitor-features-and-differentiation/round-synthesis.md) listed 14 MUST HAVE features (M1 to M14) that competitors already offer. The owner is reviewing them one at a time and deciding, for each, whether and how it enters v1. This file records each decision as it is made.

These decisions set direction for v1. They do not change any feature's `scope` value, which stays `candidate` until the gates in [03_features/README.md](../../03_features/README.md) are met.

## Decisions

### M1: Paste or URL intake, useful result in under a minute

- Options considered: (1) paste only; (2) paste plus URL, with paste as fallback; (3) option 2 plus screenshot.
- **Decision: option 2.** The user can paste the posting text or give a URL. JobHub fetches the single page the user chose when it can; when it cannot (LinkedIn, login walls, bot checks), it asks the user to paste. Target: 60 seconds or less from paste to first useful result. Each saved posting records its source ("pasted" or "fetched from URL on date"). Screenshot intake is deferred.
- Affects: [FEAT-005](../../03_features/FEAT-005-paste-capture.md) (currently paste only; URL fetch to be added), [FEAT-002](../../03_features/FEAT-002-single-posting-review.md) (time target).
- Evidence: R10 runs A and C (paste or link intake is universal; speed to first value is the most praised point); E13 Part A (snapshot and stale rule work; paste completeness 63%).
- Consequences: a URL fetch is one page the user picked, not crawling, so it stays inside the "no crawling" rule. The 60-second target needs measuring in E13 Part B or the first user test.

### M2 and M3: Red-flag list and next steps

- Options considered: (1) flags only, quoted; (2) flags plus a fixed next step per flag type; (3) option 2 plus report links.
- **Decision (owner, 2026-11-20):**
  - Red flags are not limited to scams. They cover toxic work environment, exploitative terms and scam signals, in categories still to be finalised.
  - JobHub only **identifies**. Reporting scams is **out of scope**: no report links or report flows. The correct parties handle reporting.
  - Option 3 is rejected. Whether a plain informational pointer (for example "ScamShield helpline 1799") may appear as optional text is still to be confirmed by the owner.
- **Follow-up decision (owner, 2026-11-20, "1 and 2 will be nice", read as yes to both open questions):**
  - Five categories are final for v1: (1) scam signals, (2) exploitative terms, (3) toxic environment signals, always labelled as weaker "may suggest, worth asking" signals, (4) unfair or discriminatory hiring against TAFEP guidelines, (5) vague or misleading posting.
  - v1 runs **text-only** checks on the posting. Checks that need outside data (contact versus company, .gov.sg domain, reposting, layoffs, reviews, market pay) are added when the employer check and company research are built.
  - A flag may carry a plain information line, such as "ScamShield helpline: 1799", with no link or report button.
  - Wording rules: quote the exact posting line and name the rule or source; no score, no "safe" or "scam" verdict, no legal conclusion (category 4 says "against TAFEP guidelines", not "illegal"); when nothing is found, say "No red flags found in the text" and state what was not checked.
- M3 (next step per flag) is covered by this decision: next steps become optional information lines only.
- Affects: [FEAT-002](../../03_features/FEAT-002-single-posting-review.md), [FEAT-006](../../03_features/FEAT-006-official-red-flag-evidence.md), [FEAT-007](../../03_features/FEAT-007-harmful-signals-pack.md) (its five posting-wording categories will need to match the final list).
- Evidence: R10 runs C and E.

### M4: Salary shown or "not disclosed", plus posting age

- Options considered: (1) quote salary or "not disclosed", posted and closing dates, stale notice; (2) option 1 plus salary sense checks; (3) option 2 plus market pay comparison.
- **Decision (owner, 2026-11-20): option 2 for v1, with market pay comparison as an exploration item.**
  - The review quotes the salary as written, or says "Salary not disclosed". Many portals and postings do not declare salary, so a missing salary is a normal case: it is shown as **information, not a red flag**.
  - Posted date, closing date and the existing stale notice (FEAT-005 rule) are shown when known.
  - Salary sense checks run on the posting text: wrong pay unit (monthly vs yearly), wrong currency, implausibly low full-time pay, a range wider than 2x. They are quoted as "looks inconsistent, check with the employer" under red-flag category 5. JobHub never converts a figure silently.
  - **To explore (not v1 build):** market pay comparison, including where an estimate would come from (official pay data such as MOM wage tables, MyCareersFuture ranges, permitted sources like Levels.fyi) and how to state its basis. Links to [FEAT-009](../../03_features/FEAT-009-pay-benchmark.md) and [Round 08](../../01_research/rounds/R08-market-value-and-salary-benchmarking/round-synthesis.md).
- Affects: FEAT-002, FEAT-005, FEAT-009.
- Evidence: R10 run E (MyCareersFuture shows a range on every job; Glints, Indeed and Jobstreet show unflagged salary errors; EP salary-advertising rule).

### M5: Basic employer facts

- Options considered: (1) ACRA lookup only when the posting gives a registered legal name or UEN; (2) option 1 plus brand-to-legal-entity matching, labelled "possible match, please confirm"; (3) option 2 plus explicit "employer hidden" handling.
- **Decision (owner, 2026-11-20): option 3**, building on the proven legal-name path from E11 Part A.
  - Legal name or UEN given: show ACRA facts (live status, registered address, entity age from UEN year), each with source, date and a "what this does not prove" line.
  - Brand only: show the best match as "possible match, please confirm", never as certain, until brand matching passes a retest.
  - Employer hidden (for example an agency hiding its client): say so plainly, add it to red-flag category 5, and **prompt the user to ask the recruiter or agency who the client is**, as a suggested question.
- Affects: [FEAT-001](../../03_features/FEAT-001-employer-identity-check.md) (needs a "not disclosed" state, which E11 found missing), [FEAT-003](../../03_features/FEAT-003-verification-questions.md) ("who is the client" is a question only the employer can answer).
- Evidence: E11 Part A (13 of 13 legal names, 6 of 6 lookalikes rejected, 0 of 8 brands, hidden-employer errors); R10 runs C, D and E (borrowed-licence scams; no competitor maps brand to the Singapore entity).

### M6: Profile from an uploaded resume, with preferences

- **Decision (owner, 2026-11-20): option 3.** Resume upload (PDF or Word) pre-fills the profile and the user confirms every field; LinkedIn data-export import is added once feasibility is confirmed (see below); the optional preference setup includes a **deal-breakers section, added to v1 direction**, and each deal-breaker is checked against each posting by quoting the matching posting line, with no score.
- The owner also said to proceed with **generating a custom resume PDF for each role**; this is recorded under M8 and M10.
- Affects: [FEAT-016](../../03_features/FEAT-016-candidate-profile.md), [FEAT-017](../../03_features/FEAT-017-initial-setup-job-preferences.md), [FEAT-010](../../03_features/FEAT-010-profile-comparison.md) (the deal-breaker check is a narrow form of comparison; decision [0001](0001-profile-comparison-after-profile.md) on order still applies).

Earlier notes on M6:


- Options considered: (1) as written in FEAT-016 and FEAT-017 (PDF or Word upload, confirm every field, optional preference setup); (2) option 1 plus LinkedIn data-export import; (3) option 2 plus deal-breakers checked against each posting, quoted, no score.
- **Owner so far (2026-11-20):** LinkedIn import is wanted, but its feasibility must be checked first. Choice between options awaits the owner after an explanation of option 3.
- **To explore: LinkedIn import feasibility.** First check (LinkedIn help article a1339364, read 2026-11-21): members request "Download your data" from Settings & Privacy on desktop only; Profile, Positions, Education, Skills, Certifications and Languages are in the set "available within 10 minutes" (the full archive takes 24 to 48 hours); the download link lasts 72 hours. The help page does not state the file format; the common belief that it is a ZIP of CSV files is unconfirmed. Still to check: file format and field layout from a real export, and the User Agreement terms on reusing the export.

### M7: "What am I missing" list

- Options considered: (1) hard facts only; (2) hard facts plus skills and experience as "not found in your profile"; (3) a full strengths-and-gaps narrative.
- **Decision (owner, 2026-11-20): option 2 for v1**: structured hard facts (employment type, arrangement, location, notice, right to work, stated pay against minimum) compared directly, plus a "not found in your profile" list for skills and experience, each with the posting line quoted. No score, never "you lack this".
- **To explore and test (experimental):** option 3, a fuller strengths-and-gaps narrative; and **transferable-skills mapping**, showing how skills from one role or industry may carry over to another (relevant to career switchers).
  - Risk to beat: E18 Part A, where free-text comparison gave 14% unsupported points and 10% hard-fact errors.
  - Guardrail: every statement quotes its evidence (posting line and profile fact); transferable-skill links are labelled as suggestions for the user to confirm.
- Affects: [FEAT-010](../../03_features/FEAT-010-profile-comparison.md) (decision 0001 on order still applies).
- Evidence: E18 Part A; R10 runs A, B and E (CV-vs-JD gap checks are free and common, usually with a score).

### M8, M9 and M10: Tailored resume and cover letter per job, change-by-change review, PDF and Word export

- Options considered: (1) select and order the user's own profile entries, cited, gaps shown not filled; (2) option 1 plus light rewording the user approves, every changed line linked to a profile fact and unlinked lines blocked from export; (3) free AI writing with a final review.
- **Decision (owner, 2026-11-20): option 2, built in two steps.** Ship option 1 first (supported by E19), then enable rewording once it passes a retest with no invented claims. The chatbot asks rather than invents. Free PDF (the custom resume PDF for the role, per M6) and Word export, no watermark.
- **Data model (owner):**
  - **Tailored resume** and **tailored cover letter** are **separate entities**, each tied to one job posting the user captured.
  - The candidate can keep **several base resume versions** for different types of roles (for example one per role type). A tailored resume starts from a chosen base version.
- Affects: [FEAT-011](../../03_features/FEAT-011-resume-suggestions.md), [FEAT-016](../../03_features/FEAT-016-candidate-profile.md) (base resume versions), [FEAT-005](../../03_features/FEAT-005-paste-capture.md) (captured posting as the parent record).
- Evidence: E19 (ledger-constrained method put no fabricated credential, employer or metric on 20 sets; free rewording produced an unsupported relabelling); R10 run B (propose-then-approve is the best competitor pattern; no product links claims to sources; download paywalls are the top complaint).

### M11: Saved-jobs list with a status per job

- **Status: pending, owner will decide later (2026-11-20).**
- Options presented for reference: (1) simple list with status, the user's decision and reason, and links to the posting snapshot, review and documents, status changed only by the user; (2) option 1 plus a notes field and key dates; (3) option 2 plus reminders and contacts (full [FEAT-012](../../03_features/FEAT-012-application-tracker.md)). Recommendation given: option 1 plus notes, reminders and contacts later.
- Related: [FEAT-004](../../03_features/FEAT-004-review-and-decision-record.md) (decision record), FEAT-012 (scope `later`).

### Side decision: job-posting search service (exploration item)

- **Decision (owner, 2026-11-20):** add a job-search service that finds postings from job portals to scope **as an exploration item, not v1 build**, and decide later how to navigate the legal position. This reopens the earlier "no job-board crawling" position listed in SCOPE.md as rejected-in-documents; the owner's decision here supersedes that for exploration only.
- **Findings so far** ([legal note](../../01_research/rounds/R10-competitor-features-and-differentiation/2026-11-21-scraping-legal-note.md); not legal advice):
  - Singapore: no law bans scraping by name and no court has ruled on it. Possible exposure under the Computer Misuse Act s3 (higher if blocks are bypassed or a stop request is ignored), the Copyright Act 2021 computational data analysis exception (needs lawful access; breaching terms of use is not lawful access per an IPOS official; republishing full posting text is likely outside the exception, inference), the site's terms of use (whether they bind logged-out visitors is untested), and the PDPA (recruiter personal data; publicly available exception per advisory guidance).
  - Per-site risk: LinkedIn high (terms ban scraping; hiQ precedent); Jobstreet medium to high (terms not yet read); MyCareersFuture lowest of the three (government site, publishes `llms.txt`) but terms not yet read.
- **Routes to evaluate:** company career-page feeds (for example public ATS job feeds); official data access or a partnership (for example with MyCareersFuture or WSG); user-initiated fetch of a single posting (already in M1); search links only (M12).
- **Next steps:** read MyCareersFuture and Jobstreet terms and robots.txt; check for an official MyCareersFuture data route; get a short Singapore legal review before any build.

### M12: Search links to other job boards

- Options considered: (1) keyword and location links per board; (2) option 1 plus each board's supported filters, stating when a filter is unsupported; (3) option 2 plus saved searches prefilled from preferences and deal-breakers.
- **Decision (owner, 2026-11-20): option 3.** No crawling, scraping or login; links open the board's own results and the user pastes or links back any job. Boards listed in a fixed order with no promotion. Each link pattern gets a simple periodic check, since boards change URLs without notice.
- Boards and URL patterns: R10 run E (MyCareersFuture, Jobstreet, LinkedIn, Indeed, Glints, eFinancialCareers, Foundit; HiringCafe and Careers@Gov partial).
- Affects: the search-link builder (no feature file yet), [FEAT-017](../../03_features/FEAT-017-initial-setup-job-preferences.md).

### M13 and M14: Free tier, simple pricing, one-click cancel, clear privacy terms

- Options considered: (1) principles only, prices later; (2) option 1 plus a draft free-vs-paid split; (3) fully free for v1, decide on money after user testing.
- **Decision (owner, 2026-11-20): option 3. v1 is fully free;** the commercial model is decided after user testing.
- Kept as principles for any later paid plan: a free tier that does real work; no trial that converts into a subscription; no download paywall on the user's own documents; one-click cancel; renewal reminders; total yearly cost shown.
- **Requirement:** a plain privacy notice (what is stored, which AI provider processes it, how to delete it) is written **before any real user uploads a resume** (PDPA and AI processing).
- Evidence: R10 runs A and B (billing is the category's top complaint).

## STAND OUT review

### S1: Evidence-only posting review

- Options considered: (1) quote red flags only; (2) quote every finding, red flags also naming a dated source; (3) option 2 plus a "what this review didn't check" footer.
- **Decision (owner, 2026-11-20): option 3.** Every finding links to and quotes its posting line; red flags also name the dated official source (SPF, TAFEP, ScamShield, MOM); no score, "safe" or "scam" label; each review ends with what it did not check (for example "Employer contact not verified. Pay not compared to market.").
- Affects: [FEAT-002](../../03_features/FEAT-002-single-posting-review.md), FEAT-006, FEAT-007.

### S2: Company versus contact, checked separately

- Options considered: (1) text-only comparison of contact details with the named employer; (2) option 1 plus a domain check against the company's official site; (3) option 2 plus recruiter messages or chat screenshots the user adds later.
- **Decision (owner, 2026-11-20): option 3 as the direction, to be explored further.** v1 core is option 2: quoted text mismatches (Gmail for a large company, chat-app-only contact) and an email or apply-link domain check reported as "matches", "doesn't match" or "couldn't confirm", always with "a matching domain doesn't prove the person is genuine".
- **To explore:** adding pasted recruiter messages and chat screenshots to a job. Open questions: reading screenshots (OCR, deferred under M1); privacy of chat content, which may include third parties' personal data (PDPA); how contact details in messages are stored, shown and deleted.
- Evidence: SPF/GovTech advisory 15 May 2026 (borrowed licence numbers); R10 run C (no checker joins posting, company and contact).
- Affects: FEAT-001, FEAT-002, FEAT-005.

### S3: Brand to Singapore legal entity, with each check's limits

- Options considered: (1) M5 as decided (ACRA only, brands as "possible match"); (2) option 1 plus finding the legal name or UEN on the brand's own website (footer, privacy policy, terms) and confirming on ACRA; (3) option 2 plus a combined identity card (ACRA, MOM agency directory for agencies, .gov.sg check for government jobs, LinkedIn badge), each with a "doesn't prove" line.
- **Decision (owner, 2026-11-20): option 3 is in scope; the logic is to be designed** in further discussion before build.
- **Open questions:** how brand-to-legal-name matching works (website step, retest on E11 brand cases); how confidence is shown without a score; what the card says when checks disagree; MOM Employment Agencies Directory access (client-rendered page; shown as a "check here" link until solved).
- Affects: [FEAT-001](../../03_features/FEAT-001-employer-identity-check.md).

### S4: Singapore rules pack in one view

- Options considered: (1) rules stay inside the red flags; (2) option 1 plus a "Singapore rules checked" panel on each review and a public rules page with sources and dates; (3) option 2 plus an upkeep process (monthly check of SPF, TAFEP, MOM, ScamShield; owner sign-off on each new or changed rule; change log).
- **Decision (owner, 2026-11-20): option 3 is in scope; the design is to be discussed further.**
- Overlap already decided: scam signals (M2 category 1), TAFEP wording (M2 category 4), .gov.sg check (S3). New: Employment Pass salary-advertising rule shown as information only (the role's pass type is usually unknown); keeping rules current (advisories change; Workplace Fairness Act expected around end-2027); showing the rules openly.
- **Open points:** who signs off rule changes; how often rules are reviewed; how much rule detail users see.
- Affects: FEAT-006, FEAT-007.

### S5: Questions to ask the employer, built from the posting's gaps

- Options presented: (1) standard questions only (already in v1, FEAT-003); (2) fixed question templates per gap type (no pay, vague duties, hidden employer, contradiction, odd salary unit), shown only when that gap is found, with the posting line quoted; (3) option 2 plus labelled AI-written questions for uncovered gaps, after a retest.
- **Decision (owner, 2026-11-20): in scope, needs more discussion. No option chosen yet.**
- Issue to resolve: E12, where only 38% of 92 generated questions met all four checks (bar 80%), and none named an applicable official route.
- Affects: [FEAT-003](../../03_features/FEAT-003-verification-questions.md).

### S6: Every resume and cover-letter claim linked to a profile fact

- Options considered: (1) links shown, unlinked lines warned but exportable; (2) unlinked lines block export until linked, added to the profile, or removed; (3) option 2 plus an optional "can you explain this?" check on reworded lines before export.
- **Decision (owner, 2026-11-20): option 3, in scope, requires discussion.** Builds on M8 to M10 (ask rather than invent; selection first).
- **Open points:** how strict the export block is for cover letters (which contain more framing than facts); what counts as an acceptable link to a fact (exact match for numbers, dates, titles and employers; looser for wording?); how the explain check works and how it stays optional and quick.
- Evidence: E19; R10 run B (no competitor links claims; Enhancv reviews; Jobscan's "claims candidates can't defend" argument).
- Affects: [FEAT-011](../../03_features/FEAT-011-resume-suggestions.md), FEAT-016.

### S7: One decision record per job

- Options presented: (1) decision label and reason only; (2) full record: posting snapshot, review, decision and reason, approved documents, exact files sent; (3) option 2 plus comparing a later offer with the original posting (overlaps [FEAT-013](../../03_features/FEAT-013-offer-and-contract-check.md)).
- **Decision (owner, 2026-11-20): in scope, needs discussion**, together with M11 (saved-jobs list), since that list is how records are browsed.
- Affects: [FEAT-004](../../03_features/FEAT-004-review-and-decision-record.md), FEAT-005, FEAT-012.

### Preferences improvement (owner request, 2026-11-20)

- The owner asked to discuss how to improve candidate preferences ([FEAT-017](../../03_features/FEAT-017-initial-setup-job-preferences.md)). **Ideas saved for later discussion (owner, 2026-11-20); nothing decided.**
  1. Hard vs soft deal-breakers ("never" shown as a red line, "prefer not" as a note). Value: fewer false alarms. Risk: one more choice.
  2. Deal-breakers picked from a list plus free text (rotating shifts, weekend work, commission-only, bonds, travel over 50%, probation over 6 months). Value: reliable matching to posting text. Risk: list needs Singapore wording.
  3. Shift and schedule needs (shift pattern, weekends, overnight, maximum commute). Value: matters most for non-office roles competitors ignore. Risk: longer setup.
  4. Career-switcher mode (target fields, skills you think transfer; "not found in your profile" becomes "may transfer: please confirm"). Value: helps switchers. Risk: depends on transferable-skills exploration (M7).
  5. Minimum pay with "allowances included?" and "monthly or yearly". Value: avoids unit mistakes. Risk: low.
  6. Learn from decisions: after the same decline reason twice, suggest adding it as a deal-breaker; never added without the user's OK. Value: preferences improve without setup. Risk: may feel intrusive.
  7. Sensible defaults and skip: everything optional, a 5-tap short version first. Value: faster start. Risk: thinner data.
  8. Never filter jobs out; only show the matching posting line (competitors' filters are ignored and still produce wrong applications). Value: user stays in control.
  - Recommendation given for v1: ideas 1, 2, 5 and 7, plus a short form of 3 (shifts and weekends); 4 after the transferable-skills exploration; 6 after the first user tests.

### S8, S10 and S11: covered by must-have decisions

- S8 (deal-breakers explained against the posting) is covered by M6; S10 (neutral search-link builder) by M12; S11 (honest pricing) by M13 and M14.

### S9: Company research as dated, sourced cards

- Options presented: (1) official facts only (ACRA, layoffs, MOM retrenchment); (2) option 1 plus link-out cards for review and pay sites with freshness and ownership labels, no summarising; (3) option 2 plus a short summary of review themes (not supported by E16).
- **Decision (owner, 2026-11-20): in scope (experimental), needs discussion. No option chosen yet.**
- **Open questions:** which sources are best (official, review, pay, layoffs; Singapore coverage; access limits such as Glassdoor and AmbitionBox bot checks); what to look out for (freshness, sample size, shared ownership such as Glassdoor and Indeed, blended populations, imported reviews, small employers).
- Evidence: R10 run D; E16.
- Affects: [FEAT-008](../../03_features/FEAT-008-employee-experience.md), FEAT-001.

### S12: Decide before you apply

- Options considered: (1) principle only, no auto-apply; (2) option 1 plus a skippable "ready to apply?" checklist (decision recorded, red flags reviewed, documents approved); (3) option 2 plus help with application forms later.
- **Decision (owner, 2026-11-20): option 3, with the owner's clarification.** JobHub never applies, bulk-applies, fills forms or acts in the user's accounts. The "ready to apply?" checklist is kept. "Form help" means a **copy-ready data panel**: the user's data (notice period, right to work, contact details, work-history snippets, saved answers) kept in one place to copy and paste into employer forms. No automation, no browser extension, no logging in anywhere. The user does everything on the employer's site and clicks submit.
- Affects: [FEAT-014](../../03_features/FEAT-014-portal-autofill.md) (updated; scope stays `later`), FEAT-004, FEAT-017.

## Open items

- M11 and S7: to be discussed together.
- S3: matching logic to be designed. S4: design to be discussed. S5: option and design to be discussed. S6: details to be discussed.
- Preferences improvement: ideas saved above, discuss later.
- S9: best sources and what to look out for, to be discussed.
- To explore: LinkedIn import feasibility (M6); market pay comparison (M4); fuller narrative and transferable skills (M7); pasted recruiter messages and screenshots (S2); job-posting search service (legal review first).
