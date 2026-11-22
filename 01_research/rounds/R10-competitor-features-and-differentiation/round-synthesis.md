# Round 10 synthesis — Competitor features and differentiation

Date: 2026-11-21
Status: draft for owner review. Not a scope decision. The round lead's synthesis is kept separate from the run findings it draws on; claims below cite the run, and each run cites its sources with evidence labels.

Runs: [A — AI agents and copilots](runs/2026-11-21-ai-agents-and-copilots/findings.md), [B — resume and cover-letter tools](runs/2026-11-21-resume-and-cover-letter-tools/findings.md), [C — posting and scam checkers](runs/2026-11-21-posting-and-scam-checkers/findings.md), [D — company research tools](runs/2026-11-21-company-research-tools/findings.md), [E — Singapore and regional](runs/2026-11-21-singapore-and-regional/findings.md). Builds on [R07](../R07-competitive-landscape/round-synthesis.md) and the [AIApply note](../R07-competitive-landscape/2026-11-20-aiapply-competitive-note.md).

## Coverage

About 55 products and sources across five groups, all public pages read on 2026-11-21. No logins, purchases or posting submissions.

| Group | Products |
|---|---|
| A. AI agents and copilots | LazyApply, JobCopilot, LoopCV, Wobo (incl. ChatGPT/Claude app), JobHire.AI, Scale.jobs, Massive (pivoted), Final Round AI, Welcome to the Jungle (ex-Otta), HiringCafe, general LLMs / OpenAI Jobs |
| B. Resume and cover letter | Enhancv (incl. Resume MCP), Resume Worded, Resume.io, Zety, Novoresume, FlowCV, Reactive Resume, LinkedIn Premium (Resume Tips, Apply Assistant), CoverLetter AI; brief: Canva, Copilot, Grammarly, Yoodli |
| C. Posting and scam checkers | ScamShield, SPF/GovTech advisories, MOM EA Directory and FCF watchlist, TAFEP, ACRA Bizfile, LinkedIn job verification, Jobstreet Security Hub, Indeed safety, FlexJobs, ghost-job extensions, HiringCafe, Norton Genie, Bitdefender Scamio, ScamAdviser, LoopCV and Fake Job Shield checkers |
| D. Company research | Glassdoor, Indeed company pages, Blind, Levels.fyi, NodeFlair, AmbitionBox, Crunchbase, LinkedIn Premium insights, Layoffs.fyi, MOM retrenchment rule, ChatGPT/Perplexity deep research, Teal |
| E. Singapore and regional | MyCareersFuture / CareersFinder, Career Kaki, ResumeBoostSG, NTUC AI Career Coach, Careers & Skills Passport / SEEK Pass, Jobstreet, LinkedIn, NodeFlair, Glints, Indeed SG, Careers@Gov; lighter: FastJobs, GrabJobs, eFinancialCareers, Foundit |

## What the round established

1. **Scores and verdicts are the market default.** Fit percentages (MCF, Wobo, Jobstreet "Very strong applicant", NTUC match bands), ATS scores (NodeFlair, Enhancv, Resume Worded, Resume.io), scam scores (ScamShield labels, ScamAdviser, GhostJob, LoopCV) and star ratings (Glassdoor, Indeed, Blind). Every verdict tool also disclaims its own verdict. Only government and registry sources give plain evidence. (A, B, C, D, E)
2. **Nobody reads the specific posting for risk.** Boards show a static scam banner and a report link; scam checkers handle messages, numbers and domains, not postings; ghost-job extensions are tiny, US-only and score-based. (C, E)
3. **Singapore scams now borrow real identities.** Impersonators quote a real agency's MOM licence number and ask victims to change Singpass contact details (SPF/GovTech, 15 May 2026). A registry match proves the company exists, not that the contact belongs to it. (C, E)
4. **Tailoring is commoditised; truthfulness is not solved.** Every tool tailors. The best pattern is "propose, then approve" (Resume Worded AutoFix, Enhancv MCP, Reactive Resume, LinkedIn Apply Assistant), but no product links a resume line back to a source fact. Enhancv claims "no hallucinations" while its own reviews report changed dates and removed employer names. (B)
5. **Chat-native competitors exist.** Wobo runs inside ChatGPT and Claude; Enhancv's Resume MCP tailors and stores a copy per job from inside Claude or ChatGPT. JobHub's chatbot is not novel by itself. (A, B)
6. **Billing is the category's top complaint, ahead of AI quality.** Auto-renewing trials (Zety S$2.95 to S$34.95 every 4 weeks; Resume.io), download paywalls, hidden checkout prices, hard cancellation. Volume products have the worst ratings (JobCopilot 1.7, LazyApply 2.1 on Trustpilot). (A, B)
7. **Free local alternatives raise the floor.** MCF, Career Kaki, NTUC AI Career Coach and NodeFlair give free search, salary data, AI resume help and coaching. Reactive Resume is a free open-source baseline. JobHub cannot win on generation or price alone. (B, E)
8. **No tool maps a brand to the Singapore employing entity.** Crunchbase returns the US holding company; review sites blend sub-populations and share owners (Glassdoor and Indeed merged 2026-07-01). (D)
9. **Salary data on boards has visible, unflagged errors** (Glints "$200 - 300/Month" full-time; a rupiah-priced Singapore listing; Indeed "$14,000 - $16,000 a year"; Jobstreet "Salary match" while salary is hidden). (E)
10. **Churn is high.** Massive pivoted to AI data sourcing; Otta was absorbed into Welcome to the Jungle; Final Round AI moved to covert live interview help. (A)

## MUST HAVE (table stakes)

What users already get elsewhere and will expect on day one. Missing these makes JobHub look incomplete, whatever its differentiators. Each row is tied to the v1 scope item it belongs to.

| # | Must-have feature | v1 scope item | Who already does it | Runs |
|---|---|---|---|---|
| M1 | **Paste text or a URL and get a useful result in under a minute**; screenshot intake is a common extra | Paste and URL intake; posting review | ScamShield, LoopCV, Wobo, CV-vs-JD tools, AIApply ("under five minutes") | A, C |
| M2 | **A plain list of red flags found in the posting**: fees, Singpass or personal data requests, chat-app-only contact, pay too good to be true, vague role, urgency | Posting review with Singapore red flags | Jobstreet Security Hub, Indeed, ScamShield guidance, paste-in checkers | C, E |
| M3 | **A concrete next step** with each concern: call 1799, contact the company through its official site, report the ad | Posting review | ScamShield, Norton, Jobstreet, MCF banner | C |
| M4 | **Salary shown, or an explicit "not disclosed"**, plus posted date, closing date or age | Posting review | MCF, HiringCafe, LinkedIn | C, E |
| M5 | **Basic employer facts**: UEN or legal name, size, address, industry, link to official sources (ACRA, MOM, ScamShield) | Employer identity check; company research | Jobstreet (UEN on page), Glints, Crunchbase, LinkedIn | C, D, E |
| M6 | **Reusable profile from a resume upload** (PDF, Word, LinkedIn export), with preferences and exclusions | Profile management; preferences and deal-breakers | Nearly all of A and B | A, B |
| M7 | **A "what am I missing" check** of the posting against the profile (as a list, not a score) | Posting review; profile | WTTJ coach, Wobo, Resume Worded, NodeFlair | A, B |
| M8 | **Tailored resume and cover letter per job**, editable inline, with each AI change accepted or rejected | Chatbot with human-verified documents | Resume Worded, Enhancv, Reactive Resume, LinkedIn | B |
| M9 | **Several saved versions, each attached to the job it was made for** | Documents stored per job | Enhancv, FlowCV, Teal | A, B |
| M10 | **Free, unbranded PDF and Word export** of the user's own documents | Documents per job | FlowCV, Reactive Resume (Zety and Resume.io paywall this and are hated for it) | B |
| M11 | **A simple list of saved jobs with a status** (saved, reviewing, applied, declined) | Decide before apply; profile | Every tracker in A and B | A, B |
| M12 | **Links out to search on the major boards**, with keyword, location, salary and date filters | Search-link builder | Boards' own search; HiringCafe as an aggregator | A, E |
| M13 | **A free tier that does real work, clear pricing, one-click cancel, a stated refund window** | Simple pricing | LoopCV, FlowCV, Novoresume Pro Pass | A, B |
| M14 | **Privacy basics stated up front**: what is stored, which AI provider processes it, how to delete | All | Weak across the category; GhostJob sends JDs to OpenAI on Pro | B, C |

## STAND OUT (differentiators)

Where JobHub can be clearly better, because competitors do not do it, do it badly, or do the opposite. Ordered by strength of evidence and fit with v1.

| # | Stand-out feature | v1 scope item | Why it stands out | Runs |
|---|---|---|---|---|
| S1 | **Evidence-only posting review**: every finding quotes the posting line and, for red flags, a dated official source (SPF, TAFEP, ScamShield, MOM). No score, no "looks safe" | Posting review with quoted facts and Singapore red flags | No tool in five groups does this. Every consumer checker gives a verdict and then disclaims it | C, E, A |
| S2 | **Company versus contact separation**: "the company exists and is registered" shown apart from "this Telegram or WhatsApp contact is linked to it: unverified" | Employer identity check | Directly answers the May 2026 borrowed-licence impersonation pattern; no checker joins posting, company and contact | C, E |
| S3 | **Brand-to-Singapore-entity mapping with stated limits**: UEN from ACRA (status, address, entity age from UEN year), .gov.sg check for government jobs, MOM agency directory pointer, LinkedIn badge, each with "what this does not prove" | Employer identity check | No competitor maps brand to the local employing entity; Crunchbase returns the holding company | C, D, E |
| S4 | **Singapore rule pack in one view**: TAFEP wording examples (age, race, nationality, language), EP salary-advertising rules, Singpass and Certificate of Clearance warnings, government-job domain check; presented as guideline concerns, not legal violations | Posting review with Singapore red flags | Global tools have none; government sources are scattered across agencies | C, E |
| S5 | **Questions built from what is missing or odd**: no legal entity, no pay, agency hiding its client, implausible pay or currency, "salary match" with salary hidden | Posting review | Turns gaps into actions without verdicts; local boards pass these errors through unflagged | C, E |
| S6 | **Every resume and cover-letter claim linked to a confirmed profile fact**; unsupported lines flagged and blocked from export until confirmed or removed; the chatbot asks rather than invents | Chatbot with human-verified documents | Nobody links claims to sources; Enhancv's "no hallucinations" claim is contradicted by its reviews; invented content is AIApply's sharpest complaint | B, A |
| S7 | **One decision record per job**: posting snapshot, review, the user's decision and reason, and the exact verified documents, kept together and re-checkable after the posting disappears | Decide before apply; documents per job | Competitors store a resume copy per job at most; snapshot also exposes bait-and-switch offers | A, B, C |
| S8 | **Preferences and deal-breakers explained against the posting** ("you said no rotating shifts; the posting says 'rotating shifts'"), not a match percentage | Light preferences and deal-breakers | Fit scores are universal locally and globally; filters still produce irrelevant matches | A, E |
| S9 | **Company research as attributed, dated link-out cards** with freshness and independence labels (newest item date, count in last 24 months, shared-owner flag, "not found" stated) | Experimental company research | Review sites hide freshness and ownership; deep-research chatbots give vague citations | D |
| S10 | **Neutral, multi-board search-link builder** (MCF, Jobstreet, LinkedIn, Indeed, Glints, Careers@Gov, eFinancialCareers, Foundit, HiringCafe) feeding paste intake, with no crawling | Search-link builder | Boards push their own inventory and mass apply; observed URL patterns are in run E | E, A |
| S11 | **Honest pricing as a visible feature**: no converting trial, no download paywall, renewal reminders, total yearly cost shown, a one-off pass, documents downloadable after downgrade | Simple pricing | Billing is the category's top complaint (Zety, Resume.io, JobCopilot, LazyApply, Final Round) | A, B |
| S12 | **"Decide before apply" instead of volume**: no bulk apply, no auto-submit, no acting in the user's LinkedIn session | Principle across v1 | Volume products have the worst ratings and blacklist risk; JobHub becomes the quality counter-position | A, E |

## What not to compete on

- Job inventory, discovery feeds or crawling (HiringCafe, boards, JobCopilot own it).
- Free generic tailoring or coaching on its own (Career Kaki, NTUC, NodeFlair, WTTJ, Reactive Resume are free).
- Auto-apply volume or covert live interview help (LazyApply, JobCopilot, Final Round AI).
- Star ratings or a single trust score for employers or postings.

## Contradictions and open questions

- Users may want a single "is this safe?" answer. JobHub's no-verdict stance needs a test: does quoted evidence plus a next step feel as useful as a label? (Ties to FEAT-002 and FEAT-006 assumptions.)
- Enhancv and Wobo already ship chat-native tailoring inside Claude and ChatGPT. JobHub's chatbot only stands out if S6 and S7 are visible, not just claimed.
- Levels.fyi offers an MCP server and `.md` pages that might be a permitted data route for pay context; not tested and not in v1.
- Careers & Skills Passport and SEEK Pass verify candidate credentials; a later route to "never invent claims" with verified facts. Not in v1.
- Most sentiment is Trustpilot snapshots, some from vendors that pay Trustpilot or invite reviews.

## Limitations

- Public pages only; no logged-in product testing. Prices vary by visitor region and some "$" currencies are unconfirmed.
- Kimi WebBridge used the owner's browser, so some Singapore pages showed personalised elements (recorded as features only, no personal data).
- Several sites blocked access (LazyApply, Glassdoor SG, AmbitionBox, FastJobs, GrabJobs); those facts are second-hand.
- Reddit was not read directly.
- One test company (Grab) for company research; small employers, which matter most for scam risk, were not tested.
