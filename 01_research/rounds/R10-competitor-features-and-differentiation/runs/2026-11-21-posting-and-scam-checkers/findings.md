# Run C findings: posting, scam and ghost-job checkers; employer verification

Date: 2026-11-21. Desk research only. No real posting was pasted into any checker. Evidence labels as in the [round brief](../../round-brief.md); search-result summaries that were not opened count as **2nd**.

Tools used: WebSearch and WebFetch, plus Kimi WebBridge (session `jobhub-r10-scam`, read-only, closed afterwards) for pages that blocked fetches or needed rendering (Norton blog, FlexJobs, HiringCafe).

Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report.

## Headline facts

- **Verdicts dominate.** Every consumer checker gives a verdict or score: ScamShield has four fixed labels, ScamAdviser scores 1 to 100, GhostJob 0 to 100, LoopCV 0 to 10. Only government and registry sources (SPF, TAFEP, ACRA, MOM) give plain evidence.
- **Borrowed licence numbers.** The SPF and GovTech advisory of 15 May 2026 says impersonators give the real licence number of the agency they pose as, so an MOM EA Directory check comes back valid. At least 20 cases since March 2026. (V-site)
- **The FCF watchlist is gone.** A 24 Feb 2026 written parliamentary answer says it was folded into COMPASS in 2023 after close to 1,000 firms were listed. It was never fully public, so JobHub cannot use it. (V-site / 2nd)
- **LinkedIn's badge verifies the poster and company page, not the job.** LinkedIn says so itself. (V-site)
- **ACRA publishes its own consumer checklist** (live status, address, entity age from the UEN year, whether the person contacting you is in charge). Basic search is free; profiles cost S$5.50 to S$50. (V-site)

## Per tool

### 1. ScamShield (GovTech, SPF and NCPC)

- **Checks:** messages, phone numbers and links. There is no job-posting check. (V-site)
- **Inputs:** screenshot or pasted text with sender ID, a caller's number, or a link. Email, social media and shopping platforms are not supported; the workaround is "Others". (V-site)
- **Output is a verdict.** Messages: "Beware, this looks like a scam" / "Be careful, we're not sure about this one" / "This message looks safe" / "This looks like spam". Links: "This is not a verified link" / "This link looks safe". (V-site)
- **Data:** an AI/ML classifier, police-flagged numbers and report volume. IMDA-registered senders and official government, bank and hospital sites are treated as safe. Unreviewed senders usually get "not sure". (V-site)
- **Job-scam page:** red flags are commission for simple tasks, upfront payment, using your own money or bank account, Singpass credentials or Singpass QR codes. Steps: contact the company directly, talk to someone you trust, call 1799. It does not mention the MOM EA Directory (V-site). An ask.gov.sg answer reportedly does (2nd; page returned 403).
- **Limits:** Singapore-only app, mainly local numbers. WeChat, Messenger and TikTok not covered. A check is not a police report. (V-site)
- **Sentiment:** a Mothership reviewer found a number lookup took under a minute and showed 108 prior reports. (2nd)
- **Lesson:** link out to ScamShield for numbers, links and messages; do not compete on its verdict. "Link looks safe" can give false comfort about a ghost or misleading job.

### 2. SPF and GovTech advisories

- **15 May 2026 (concert crew jobs):** scammers impersonate real recruitment agencies on Telegram and Carousell, collect NRIC and date of birth, get victims to change Singpass contact details, then open financial accounts in their names. Scammers "sometimes give the licence number of the agency they are impersonating". Advice: a valid licence number does not prove the person is genuine; a Certificate of Clearance is not needed for local jobs. At least 20 cases since March 2026. (V-site)
- **14 Sep 2026 (trading-card task scams):** at least 12 cases since 25 Aug, at least S$71,000 lost; victims made crypto deposits to unlock tasks. (V-site)
- **Output:** evidence and advice, never a verdict on a posting.
- **Lesson:** best Singapore red-flag sources to quote with date and link. A registry match proves the company exists, not that the contact belongs to it.

### 3. MOM EA Directory and the FCF watchlist

- **EA Directory** (service2.mom.gov.sg/eadirectory): renders client-side; the fetch showed only "Content is loading". Search and result fields not read. (V-site / I)
- **FCF watchlist:** close to 1,000 firms listed 2016 to 2023, mostly ICT, professional services and construction; criteria built into COMPASS in 2023. (V-site) Never fully public. (2nd)
- **Lesson:** do not promise the FCF watchlist. Pair any EA licence lookup with the SPF warning about borrowed licence numbers.

### 4. TAFEP job-ad guidance

- Wording to avoid on age, gender, race, language, nationality, marital status and religion, with examples such as "Below 30 only", "Preferably female", "Chinese/Malay/Indian preferred", "EP/S Pass/WP holders preferred". Acceptable example: "All races are welcome". Reports go through TAFEP Contact Us. (V-site)
- MyCareersFuture reportedly has a "Report Discriminatory Job Ads" feature. (2nd)
- **Lesson:** cleanest rule source for FEAT-007. Quote the posting's phrase next to the TAFEP example it resembles and offer the reporting route without labelling the employer.

### 5. ACRA Bizfile

- **Searches:** Entity, Industry, People, Reserved name. Entity search shows live status and registered address, including some non-ACRA entities. (V-site)
- **Consumer checklist:** live status and valid address; entity age (first four UEN digits are the year); officers, including whether the contact is in charge; frequent officer changes; paid-up capital. (V-site)
- **Pricing:** entity search free; Business Profile S$5.50; People Profile S$33; CCFP S$50. (V-site)
- **Caveats (ACRA's own):** helps assess trust, does not guarantee it; may not show everyone involved. (V-site)
- **Lesson:** quote the free facts (status, address, UEN year) and turn the rest into questions.

### 6. LinkedIn job verification badge

- Shows the company page is verified and the poster has verified they work there. Drill-down lists identity (CLEAR in the US), workplace (work email, Entra Verified ID or Learning licence), school and official company page. (V-site)
- LinkedIn's caveats: a badge does not make you more likely to be hired, does not mean the job is a better fit, and says nothing about job details; no badge does not mean fraud; still a pilot. (V-site)
- Company page verification expanded Sep 2025; new fake-profile checks Sep 2026. (2nd)
- **Lesson:** show the badge as one fact among many, and copy LinkedIn's "what this does not mean" style.

### 7. Jobstreet SG Security Hub

- Trust and Safety team "verifies new hirer accounts" and reviews flagged ads before they go live. (V-site)
- Red flags: too good to be true or jobs you never applied for; repeated offers with small name or number changes; fees, ID or bank details before a formal offer; vague ads, generic email domains, urgency; fake tests in code repositories; deepfakes in video interviews. (V-site)
- Official channels listed; never contacts by SMS or social media; official WhatsApp only from "SEEK Pass". "Report the job ad" link on each ad. (V-site)
- No verified-employer badge found. (I)
- **Lesson:** good checklist, but no evidence shown on each posting.

### 8. Indeed

- Red flags: email domain mismatch, a role different from the one applied for (bait and switch), no interview, fees ("You should never have to send money to apply for a job on Indeed"), money transfers, opening accounts, advance payment then a request to send money back. Nothing shown on the posting itself. (V-site)
- **Lesson:** JobHub stores the original posting, so it can show a bait-and-switch with quotes.

### 9. FlexJobs

- Every listing "hand-screened"; rejects commission-only, MLM and too-good-to-be-true offers; no ads. (V-site, WebBridge)
- Price: US$2.95 for 14 days, then US$23.95 every 4 weeks; US$29.85 per quarter; US$71.40 per year; 14-day refund. Claims 245,136 jobs. Also sells ExpertApply auto-apply. (V-site)
- Singapore relevance low. (I) Verdict is implicit: listed means "legit".
- **Lesson:** people pay for trust. Avoid the auto-renewing trial.

### 10. Ghost-job extensions

- **GhostJob (Chrome, LinkedIn only):** signals are reposts, age, pay clarity, location, specific responsibilities, presence on the careers site; missing sources marked "uncertain". Output is a 0 to 100 Trust Score "with supporting evidence"; says it cannot confirm hiring plans. Pro compares up to 3 employer postings. Sends job descriptions to its API and, for Pro, to OpenAI. 46 users, no ratings, updated 29 Sep 2026. (V-site)
- **Others (store snippets only):** Subspace, Ghost Buster (30-day or repost flag), Repostd, VantageCV, Ghost Job Hunter. (2nd)
- Mostly scores, tiny user bases, no accuracy data, US boards. None cover Jobstreet or MyCareersFuture. (I)
- **Lesson:** use their signals as facts, not as a score.

### 11. HiringCafe

- 31,180 Singapore jobs at 2,772 companies today. Filters for Date Posted, Apply Process, Exclude Jobs and a new "Activity & Outcomes". Cards show posting age and source link. (V-site, WebBridge) Filter panels would not open. (I)
- Reportedly uses AI to filter out ghost jobs, scams and offshore shops. (2nd)
- **Lesson:** posting age as a fact is good; silent filtering is the opposite of JobHub's approach.

### 12. Norton Genie and Scam Protection

- Analyses text, images and links plus "emotional and contextual cues"; now inside Norton 360 (Safe SMS, Safe Web, Genie; higher tiers add Safe Call, Email and up to US$10,000 reimbursement). (V-site, blog via WebBridge)
- Verdict with reasons; next steps when unsure. (2nd) App free; Norton disclaims it may not stop every threat. (V-site)
- **Lesson:** lead with next steps every time, not only when unsure.

### 13. Bitdefender Scamio

- Inputs: text, links, QR codes, screenshots or a description, via web, WhatsApp, Messenger or Discord. Output: safe or threat with explanation and tips. Data: sender info, structure, language patterns, rules, known-scam database. Free with account; "early access", may not be fully accurate. (V-site)
- A Tom's Guide reviewer says it missed an obvious fake dating request. (2nd)
- **Lesson:** chat-app delivery fits Singapore, where job scams arrive by WhatsApp and Telegram.

### 14. ScamAdviser

- Domain score 1 to 100 from 40+ sources including user reviews; hosting and country mismatches lower it. Legitimate businesses complain about unfair low scores. (2nd; owner pages returned 403)
- **Lesson:** show raw domain facts, not a score.

### 15. Paste-in AI job-scam checkers

- **LoopCV:** paste text; 0 to 10 risk score, red and green flags, advice; no disclaimer or data-retention statement. (V-site)
- **Fake Job Shield:** rule-based (payment, crypto, investment, urgency); score plus explanation; says it "doesn't determine whether an employer or job is genuine". 3 users. (V-site)
- RoamJobs, TryApplyNow, Jobicy (human review), Apify actors. (2nd)
- **Lesson:** crowded, and every tool scores. A red-flag list is table stakes, not a moat.

### 16. Jobright and Teal

- Jobright reportedly flags weekly reposts and compares listings against careers pages (2nd); no official page found (I). No posting-age feature found for Teal (I).

## Patterns

1. Verdicts dominate; only government and registry sources give plain evidence.
2. Every verdict tool disclaims its own verdict.
3. Checks are split by object (message, domain, poster, board, freshness, entity). No tool joins the posting, the company and the contact channel.
4. Singapore scams now borrow real company identities and licence numbers.
5. Ghost-job tools focus on US boards, are small and have no accuracy data.
6. Job boards teach red flags but explain nothing on each posting.
7. Paste and screenshot are the standard inputs; consumer tools often deliver through chat apps.

## Table stakes users expect

1. Paste or link in, result in under a minute (screenshot is a common extra).
2. A plain list of red flags found: fees, Singpass or personal data requests, chat-app-only contact, pay too good to be true, vague role, urgency.
3. A concrete next step: call 1799, contact the company through its official site, report the ad.
4. The basic check is free.
5. Links to official sources (ScamShield, MOM, ACRA, TAFEP).
6. A freshness signal such as posted date or age.

## Gaps JobHub could own

1. **Evidence-only posting review:** quote the posting's phrase next to a dated official source (SPF, TAFEP, ScamShield), with no score. No tool in the set does this.
2. **Company versus contact separation:** "the company exists and is licensed" shown apart from "this Telegram or WhatsApp contact is linked to it: unverified". Answers the May 2026 impersonation pattern directly.
3. **Questions built from missing facts:** no legal entity named, no pay stated, agency hides its client, unknown contact person.
4. **A Singapore rule pack in one view:** TAFEP wording, MOM licence, ACRA status, SPF advisories.
5. **Freshness, careers-page presence and a stored snapshot shown as facts**, covering Singapore boards that ghost-job tools ignore, and showing later if the offer differs from the posted role.
6. **An honest scope statement for each check** ("this confirms X, not Y").

## Avoid

- Any score or "looks safe" label.
- Promising the FCF watchlist.
- Treating a licence or ACRA match as proof the job is real.
- Silent filtering (HiringCafe).
- Auto-renewing trials (FlexJobs).
- Undisclosed third-party AI processing of the user's postings.

## Limitations

- No tool was run on any posting.
- MOM EA Directory fields not read.
- Pages that returned 403 (Norton product page, ScamAdviser, Jobicy, ask.gov.sg) stay 2nd.
- HiringCafe filter panels unread.
- Sentiment is thin and mostly 2nd.
