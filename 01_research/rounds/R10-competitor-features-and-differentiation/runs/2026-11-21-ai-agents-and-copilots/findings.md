# Run A findings: AI job-search agents and application copilots

- Run date: 2026-11-21
- Scope: AI auto-apply agents, human-assisted application services, AI-first job search engines, interview copilots, and general chat assistants used as job agents. Excludes AIApply, Jobright, Simplify, Sonara, Teal, Careerflow, Jobscan and Huntr (covered in R07 and the AIApply note).
- Method: desk research only. No accounts, logins, purchases or form submissions.
- Tools: Kimi WebBridge (session `jobhub-r10-autoapply`, read-only text extraction) for HiringCafe, Wobo, JobHire, the JobCopilot home page, Final Round AI, Welcome to the Jungle, usemassive.com and all Trustpilot pages. WebFetch for JobCopilot pricing, LoopCV pricing, Scale.jobs pricing and the 6figr LazyApply review. WebSearch for discovery. lazyapply.com returned "Access Denied" to both tools.
- Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report.

Evidence labels as in the [round brief](../../round-brief.md). Competing auto-apply vendors (LoopCV, Scale.jobs, Scoutify, FastApply, 6figr/JobGPT, Jobright) write many third-party reviews; they are used for facts only.

## Headline findings

- usemassive.com now runs a different business (AI post-training expert sourcing, "Do a Huddle, Inc. (dba Massive)"). The job product looks retired or pivoted.
- Final Round AI now presents itself as a live interview copilot with a "Stealth Mode" hidden from screen sharing. No job-search product found on the pages read.
- Wobo already ships a chat-native agent inside ChatGPT and Claude: match percentages, tailored resumes, "add it if you have it" for missing skills, confirmation before bulk-applying.
- HiringCafe is free and showed 31,155 Singapore jobs from 2,772 companies.
- Trustpilot today: JobCopilot 1.7, LazyApply 2.1, Final Round 2.8, LoopCV 3.8, JobHire 4.1, Wobo 4.5, Scale.jobs 4.5.
- The most common complaint across the category is billing (hard to cancel, surprise annual charges, hidden pricing, slow refunds), not AI quality.

## 1. LazyApply

Browser-extension bot that fills in and submits applications in bulk (V-3p 6figr). Claims worldwide, optimised for US and Canada; Trustpilot contact country India (V-3p).

| Feature | Status | Evidence |
|---|---|---|
| Intake | Extension on Greenhouse, Dice, Indeed, ZipRecruiter; a 2022 review mentions LinkedIn Easy Apply | V-3p |
| Posting analysis | Not found | I |
| Fit scoring | None found; users report applications to mismatched jobs | V-3p |
| Resume / cover letter | AI cover letters, resume keyword suggestions | V-3p |
| Claims grounded? | Not stated; users report wrong data entered (for example a wrong middle name) | V-3p |
| Human review before submit | Not mentioned; users say they must monitor it closely | V-3p |
| Tracking | Dashboard | V-3p |
| Company research, scam checks, interview help | Not found | I |
| Other | "Smart Referral Emails" to employees at target companies; Gmail account required | V-3p |

- **Automation:** full auto-submit, up to 1,500 applications a day (V-3p).
- **Pricing (USD, annual; 6figr says verified Oct 2026):** Basic $99/yr (15/day), Premium $149/yr (150/day), Ultimate $999/yr (1,500/day). No free tier or trial; 30-day money-back (V-3p).
- **Singapore:** not stated (I).
- **Sentiment:** Trustpilot 2.1 from 110, 58% one-star; no replies to negative reviews (V-3p). Complaints: Gmail-only requirement hidden before payment, refunds ignored, forms filled wrongly, weeks-long outages early 2026 (V-3p). LinkedIn accounts restricted after mass applying; one user sent 14,000 applications and got mass rejections (2nd).
- **Lesson:** do not auto-submit, never act inside the user's LinkedIn session, disclose all requirements before payment.

## 2. JobCopilot

AI copilot that searches 500,000+ company career pages daily and autofills applications; claims 100,000+ users; Trustpilot lists France (V-site, V-3p).

| Feature | Status | Evidence |
|---|---|---|
| Intake | Set filters once; copilot finds jobs daily; Chrome extension | V-site |
| Fit scoring | Filters and exclusion words; users report exclusions ignored | V-site; V-3p |
| Resume / cover letter | AI resume and cover letter builders; per-job tailoring only on Elite | V-site |
| Claims grounded? | Not stated | I |
| Human review before submit | Optional: "with the option to review before applying" | V-site |
| Tracking | Tracker dashboard | V-site |
| Scam checks | "Exclusively applies to verified jobs on official company career pages" | V-site |
| Interview help | AI mock interviews, salary negotiation | V-site |
| Other | Paid credits to unlock hiring-manager emails; learns from your edits | V-site |

- **Automation:** full auto-apply, review optional, up to 50 matches a day (V-site).
- **Pricing (read 2026-11-21, "$"):** Premium about $0.93/day (1 copilot, 20 matches/day); Elite about $1.05/day (3 copilots, 50/day, tailoring, hiring-manager credits). Weekly, monthly and quarterly options mentioned, not priced (V-site).
- **Singapore:** only "worldwide" claimed (V-site).
- **Sentiment:** Trustpilot 1.7 from 102, 64% one-star. Cannot cancel, unexpected auto-renewal, support email bouncing, poor matches, 500+ applications with no contact (V-3p).
- **Lesson:** "verified jobs" is a strong claim, but users judge on match quality and honest billing.

## 3. LoopCV

Auto-apply built around "loops" (search + CV + cover letter). Scans 30+ boards daily, applies, sends recruiter follow-up emails. Athens, Greece (V-site, V-3p).

| Feature | Status | Evidence |
|---|---|---|
| Intake | Loops; extension for login-gated boards that does not ask for your password | V-site |
| Fit scoring | "CV matching" | V-site |
| Resume / cover letter | AI CV checks on paid tiers; messages editable before sending | V-site |
| Human review before submit | Not clearly described | V-site / I |
| Tracking | Tracker; reviewers praise the "inbound dashboard" | V-site; V-3p |
| Company research, scam checks, interview help | Not found (a separate paste-in scam checker exists; see run C) | I |
| Other | Dynamic follow-up emails | V-site |

- **Pricing (EUR, read 2026-11-21):** free plan with no time limit; paid from €9.99/month; refund within 7 days if under 10% of quota used; student discount (V-site).
- **Singapore:** not stated (I). A Latin American user found no suitable jobs (V-3p).
- **Sentiment:** Trustpilot 3.8 from 132 (64% five-star, 20% one-star). Praise for stability; complaints about errors and a two-month refund ordeal (V-3p).
- **Lesson:** a real free tier and a published refund rule build trust.

## 4. Wobo

"AI recruiter": scans 50+ sources, shows match percentages, applies for you, swipe-to-apply on iOS. Also runs as an app inside ChatGPT and Claude. Brooklyn, NY (V-site).

| Feature | Status | Evidence |
|---|---|---|
| Intake | CV upload plus chat onboarding; daily feed; paste a job URL in chat | V-site |
| Posting analysis | "Am I qualified?" comparison of experience, skills, education and gaps | V-site |
| Fit scoring | Yes, percentages (94%, 91% and so on) | V-site |
| Resume / cover letter | Tailored per job on paid tiers; "Wobo Persona" answers screening questions in your voice | V-site |
| Claims grounded? | Partly: "Payments experience isn't in your profile yet; add it if you have it" | V-site |
| Human review before submit | Chat app asks you to review and confirm; on Autopilot, Wobo picks the jobs | V-site |
| Tracking | Sent, queued and "needs you" statuses | V-site |
| Company research | Size, industry, ratings, "key signals" | V-3p |
| Scam checks | "Every job is pre-vetted. No ghost listings." (method not shown) | V-site |
| Interview help | Not found | I |

- **Pricing (USD/month, read 2026-11-21):** Free (5 applications/day); Unlimited $34.99; Autopilot $44.99 with 5-day free trial; quarterly discount (V-site).
- **Singapore:** not stated (I).
- **Sentiment:** Reviews.io 4.7 from 336 (V-site). Trustpilot 4.5 from 113, paid Trustpilot subscription (V-3p).
- **Lesson:** Wobo already ships chat + tailoring + confirm-before-send. JobHub must separate itself through no scores, no bulk apply and quoted evidence.

## 5. JobHire.AI

Background auto-apply service, "U.S. Roles Only". Florida address on site; Trustpilot says Cyprus (V-site, V-3p).

| Feature | Status | Evidence |
|---|---|---|
| Intake | Resume upload and preferences | V-site |
| Fit scoring | Resume score threshold you set | V-site |
| Resume / cover letter | AI tailoring, custom cover letters, auto-written screening answers; marketing says it "bypasses ATS filters" | V-site |
| Human review, posting analysis, company research, scam checks, interview help | Not found | I |
| Tracking | Dashboard; employer messages go to your inbox | V-site |

- **Automation:** full auto; the site cites "847 applications in 6 weeks" as a positive (V-site).
- **Pricing:** pricing page 404 (V-site). Third parties cite about $49/month for about 40 applications/day, 3- and 6-month bundles, no free tier, auto-renewal, BBB F (2nd).
- **Singapore:** no, US roles only (V-site).
- **Sentiment:** Trustpilot 4.1 from 1,109; highlighted reviews are "Invited"; replies to 48% of negative reviews (V-3p).

## 6. Scale.jobs (human-assisted)

Human virtual assistants apply with a tailored resume and cover letter per job and send a screenshot as proof. Woodstock, GA (V-site).

| Feature | Status | Evidence |
|---|---|---|
| Intake | Onboarding call; Chrome extension to shortlist jobs from any site | V-3p |
| Resume / cover letter | ATS-tailored per application; $199 expert resume add-on | V-site |
| Human review before submit | Humans submit; no user approval step described | V-site |
| Tracking | Proof screenshots, team chat, outcome manager, re-targeting every 15 days | V-site |
| Company research | "Personalized with company research" | V-3p |
| Scam checks, interview help | Not found | I |

- **Pricing (USD, one-time, read 2026-11-21):** $399 for 500 applications, $599 for 1,000, $999 for 1,500; Klarna pay-in-4; unused credits refunded if hired (V-site).
- **Singapore:** not stated (I).
- **Sentiment:** Trustpilot 4.5 from 254; paid subscription, invites reviews (V-3p).
- **Lesson:** proof per action builds trust. JobHub's quoted evidence is the same lever.

## 7. Massive (usemassive)

- **Then:** AI agent that matched jobs, wrote materials and submitted from its own servers; iOS app with Pro (150) and Ultra (600) tiers; about $99/month for 200 applications or $117/quarter; Trustpilot reportedly 1.7 (all 2nd, from competitors).
- **Now:** homepage shows an AI post-training data sourcing business, "Do a Huddle, Inc. (dba Massive)" (V-site). No shutdown notice found.
- **Lesson:** volume products churn quickly. Re-check competitor status every round.

## 8. Final Round AI

- Interview CoPilot desktop app: listens to live interviews and privately suggests answers; "Stealth Mode" hides it from screen sharing; mock interviews in eight scenarios, coding screen reader, automatic debriefs. Zoom, Meet, Teams, HackerRank, CoderPad, HireVue (V-site). Free tier covers job-description parsing and a prep checklist (V-site). No job-search or auto-apply feature on pages read (I).
- **Pricing (USD):** Free; Pro from $25/month; no free trial (V-site). One reviewer says an advertised $41.67/month became a $500 yearly charge at checkout (V-3p).
- **Sentiment:** Trustpilot 2.8 from 280: refunds denied, stealth mode visible during screen share, bugs (V-3p).
- **Lesson:** avoid covert live help. Build interview prep from the user's own stories.

## 9. Welcome to the Jungle (formerly Otta)

- app.otta.com redirects to app.welcometothejungle.com: "We're moving. Your job search is about to get smarter." Promises "No endless feed, just job recommendations" and better company insights (V-site).
- Free AI Candidate Coach (email signup) compares CV to a job description ("what's landing, what's missing"); helps with honest, specific cover letters, interview prep and a LinkedIn audit (V-site).
- **Region:** Europe, UK and US tech (I). Free for candidates (V-site for coach; I for platform).
- **Lesson:** CV-vs-JD coaching is free and commoditised. JobHub's value lies elsewhere.

## 10. HiringCafe (hiring.cafe, redirects to hiringcafe.com)

- Free search engine that scrapes company career sites directly; filters out "external recruiting agencies and fake consulting firms"; detects "stale postings, duplicate roles". AI "Talent Agent" finds jobs daily; tracker, saved searches, boards, hidden companies (V-site).
- **Filters:** apply process, exclude jobs, activity and outcomes, company stage, size and industry, new "Sponsored Jobs" filter (V-site).
- **Job cards:** extracted years of experience, requirements summary, tools, one-line company description (V-site).
- **Singapore:** yes; 31,155 Singapore jobs from 2,772 companies, including GovTech (V-site).
- **Pricing:** free; "No pay-to-win job discovery" (V-site). Sponsored filter suggests employer monetisation is starting (I).
- **Reputation:** r/hiringcafe 100K+ members; BBB A+ (V-site).
- **Lesson:** do not compete on inventory. Make it a target in the search-link builder.

## 11. General LLMs as job agents

- **Wobo inside ChatGPT and Claude:** search, fit check, tailoring, bulk apply "up to 10 at a time" after confirmation (V-site).
- **OpenAI Jobs:** hiring platform announced Sept 2025 targeting mid-2026; a ChatGPT "Jobs" agent reportedly tested early 2026. No confirmed public launch found (2nd).
- **Plain chatbots:** tailor documents for free, but risk invented claims and keep no record per job (I).
- **Lesson:** JobHub's chatbot must add claims locked to the profile, per-job storage, Singapore red flags and quoted evidence.

## Patterns

1. Most products sell volume: LazyApply (1,500/day), JobCopilot (50/day), JobHire (847 in 6 weeks), Scale.jobs (1,500) (V-site, V-3p).
2. Volume products have the worst sentiment: JobCopilot 1.7, LazyApply 2.1, Massive reportedly 1.7 (V-3p, 2nd).
3. Billing friction is the top complaint, ahead of AI quality (V-3p).
4. Review before submit is optional, not the default (V-site).
5. "Real jobs only" claims are converging, but none show how the check works (V-site, I).
6. Match percentages are standard in the interface (V-site).
7. Chat-native agents have arrived (V-site).
8. Interview help is drifting toward live, covert assistance (V-site).
9. Churn is high: Massive pivoted, Otta absorbed into WTTJ (V-site).
10. Singapore is rarely addressed; only HiringCafe visibly serves it (V-site, I).

## Table stakes users expect

1. Upload a resume once to build a profile with preferences and exclusions.
2. A tailored resume and cover letter for each job.
3. An application tracker with a status per job.
4. A CV-vs-JD "what am I missing" check.
5. A free tier or free tool, plus easy cancellation.

Also common: a promise that jobs are real and not ghost listings.

## Gaps JobHub could own

1. A posting review that quotes the posting text behind each point. Competitors say "pre-vetted" or "verified" but show no evidence.
2. Singapore red flags and an employer identity check.
3. Claims grounded in the verified profile, confirmed by the user before saving.
4. "Decide before apply" with no scores and no bulk sending.
5. Simple published pricing, one-click cancel and a plain refund rule.

Plus: a search-link builder that complements HiringCafe and MyCareersFuture rather than competing with them.

## Things to avoid

- Auto-submit, and automating the user's LinkedIn session.
- Covert live interview help.
- Requirements not disclosed before payment; prices shown only at checkout.

## Limitations

- LazyApply's site was blocked to both tools; its facts come from a competitor-written review (6figr/JobGPT).
- JobHire pricing is second-hand only.
- Massive's status is inferred from its current homepage.
- Final Round AI's job-search side, if it still exists, was not found.
- Reddit was not read directly; Reddit sentiment is second-hand.
- Trustpilot scores are a 2026-11-21 snapshot; several vendors invite reviews or pay for Trustpilot, which can push scores up.
- Singapore availability was not checked by signing up; "not stated" means the pages read did not mention it.
- Careery, Bandana, Kickresume auto-apply and Perplexity were not researched.
