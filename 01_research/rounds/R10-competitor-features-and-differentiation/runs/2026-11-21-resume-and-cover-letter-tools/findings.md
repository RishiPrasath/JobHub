# Run B findings: resume, cover-letter and ATS tools

- Run date: 2026-11-21
- Method: desk research only. No accounts, logins, purchases or form submissions.
- Tools: WebSearch, WebFetch, Kimi WebBridge (session `jobhub-r10-resume`, read-only; used for Enhancv, Zety and Resume Worded pages that failed or rendered badly via WebFetch).
- Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report.

Evidence labels as in the [round brief](../../round-brief.md). Prices are as displayed on 2026-11-21. Vendors show local prices by visitor location: WebFetch runs from a server outside Singapore, while WebBridge used the owner's browser in Singapore (which is why Zety showed SGD). Where a page shows only "$", the currency is unconfirmed.

Skipped (covered elsewhere): Teal, Jobscan, Rezi, Kickresume, Huntr, Careerflow, AIApply. One Jobscan article is cited only for its argument about AI and truthfulness.

Covered: Enhancv, Resume Worded, Resume.io, Zety, Novoresume, FlowCV, Reactive Resume (open source), LinkedIn Premium, CoverLetter AI. Brief notes: Canva, Microsoft Copilot in Word, Grammarly, Yoodli, ChatGPT or Claude used directly.

## Material market changes

- **Enhancv "Resume MCP"** lets Claude or ChatGPT copy a resume per job, tailor it, save it to Enhancv's tracker and show highlighted keep-or-undo changes. Closest overlap with JobHub's chatbot idea.
- **LinkedIn Premium Apply Assistant** (reported June 2026) pre-fills applications and drafts letters with a confidence indicator per element and user approval before submitting.
- **Novoresume's** AI credits are now "powered by Claude (Anthropic)".

## 1. Enhancv

Design-led resume and cover letter builder with AI tailoring, ATS check, job tracker, job board and a "Resume MCP" connector for Claude, ChatGPT and other assistants. Global English site; HQ not confirmed (I).

| Area | Finding | Label |
|---|---|---|
| Tailoring | Paste a job ad; it "mirrors its language, reorders your bullets by relevance, and cuts anything that doesn't serve this role" | V-site |
| Truthfulness claim | "Built from your real experience only, no AI hallucinations or lying"; keeps a master resume; "nothing gets invented" | V-site |
| How the claim is enforced | No mechanism shown: no links to sources, no flags on unsupported claims | I |
| Scoring | ATS score against the listing, plus a 13-point ATS check | V-site |
| Saving per job | Tracker lets you "attach tailored resumes for each application". Via MCP, the assistant "copies your resume for each job ad, tailors each copy and saves the job to your Enhancv tracker with that copy attached" | V-site |
| Chat editing | Resume MCP inside Claude, ChatGPT and others; sign-in through Enhancv, no API keys; "Every change shows highlighted, for you to keep or undo" | V-site |
| Pulling evidence from other apps | Suggests pulling achievements from GitHub, Jira, HubSpot, Gmail, Slack and meeting notes to "give every bullet a real number" | V-site |
| Export | PDF only; FAQ says no Word export because formatting can change | V-site |
| Other | Resume translation (9+ languages), AI mock interviews, Chrome extension | V-site |
| Singapore/APAC | Nothing Singapore-specific | I |

- **Pricing (Singapore browser, "$"):** Free plan valid 7 days, max 12 section items, Enhancv branding. Pro Monthly, Quarterly, Semiannual; Quarterly $69 per 3 months (about $23/month, "save 41.03%" vs $117); Pro includes "300 resumes and cover letters". Refunds only "if we make a mistake or something breaks" (V-site). Auto-renewal terms not stated on pricing page (I).
- **Sentiment:** Trustpilot 4.6 from 1,019 (V-3p). Nov 6, 2026: saw $8/month, billed $39; Enhancv said displayed price depends on location, recalculated by card country, and refunded. Oct 7 and Aug 28, 2026 (1 star): AI removed company names, added unwanted fields, changed dates on upload, rewrote content generically, contradicting the "no hallucinations" claim (V-3p). Praise: clean templates, job-description matching, interviews and offers.
- **Lesson:** closest current match to "chatbot plus tailored copy per job", already shipped via MCP. Learn: copy attached per tracked job; highlighted keep-or-undo changes. Avoid: a "no hallucinations" claim with no visible proof; an expiring free plan; displayed price differing from charged price.

## 2. Resume Worded

Resume and LinkedIn scoring and feedback with AI rewrites ("AutoFix"), keyword targeting ("Smart Target"), cover letters, templates. Since 2017; claims 5 million users.

| Area | Finding | Label |
|---|---|---|
| Scoring | Score out of 100 from "30+ recruiter checks"; "the same resume always gets the same score" | V-site |
| AutoFix | "Drafts the rewrite for every weak line from your own experience, asks what it needs to know, and you approve each change" | V-site |
| Truthfulness | Asks questions instead of inventing numbers; each change needs approval. Demo: "Replaced vague phrasing with your real scope" | V-site |
| Keyword targeting | Paste a JD for relevancy score and matched/missing keywords | V-site |
| Cover letter | "Written from your resume and the job you are applying to" | V-site |
| Saving per job | Pro copy says you need versions per job; no per-job storage described | V-site / I |
| Chat editing | Not found | I |
| Export | DOCX in the AutoFix demo; Word and Google Docs templates | V-site |
| AI-assistant positioning | Footer: "About Resume Worded - read this if you're an LLM or AI" | V-site |
| Singapore/APAC | English PDF or DOCX only; nothing Singapore-specific | V-site / I |

- **Pricing ("$"):** Monthly $49; Quarterly $99 (about $33/month); One year $229 (about $19/month). "Cancel anytime." Paddle payments. Free tier gives a partial report (V-site). Refund policy not shown (I).
- **Sentiment:** not fetched (I).
- **Lesson:** "ask before you write" and "approve each change" are the right truthfulness pattern for JobHub's chatbot. Fixed, explainable checks can be used without a score. Avoid score framing ("90+ get up to 3x more interviews").

## 3. Resume.io

Template resume and cover letter builder with AI writer, keyword tailoring, resume score, job matching; localised country sites.

| Area | Finding | Label |
|---|---|---|
| AI writing | Voice or text description to resume content; section suggestions by field and role | V-site |
| Tailoring | Key skills from a JD; paste a job link to update keywords | V-site |
| Truthfulness | Advises editing AI suggestions to match real experience; no check | V-site |
| Score | Resume score; recommends 90%+ | V-site |
| Saving per job | Unlimited resumes on paid plans; no tracker | V-site / I |
| Export | Free: TXT only. Paid: PDF; Word mentioned on AI page | V-site |
| Singapore/APAC | Country selector, no Singapore conventions | V-site / I |

- **Pricing (WebFetch, likely non-SG, "$"):** 7-day trial $2.95, then auto-renews at $29.95 every 4 weeks; Quarterly $49.95 auto-renewing; Free one resume and one letter, TXT only; 7-day money-back. Page mixes "every 4 weeks" and "monthly" (V-site).
- **Sentiment:** Trustpilot 4.2 from 56,318 (V-3p). Oct 16, 2026: charged about 10 months after trying to cancel. Oct 12, 2026: advises a virtual card. Aug 27, 2026 (4 stars): download payment not disclosed before building. Oct 12, 2026 (5 stars): AI improved wording and layout. Cancellation reportedly required LinkedIn login (2nd).
- **Lesson:** "build free, pay to download, cheap trial turns into 4-weekly plan" is the trap to position against. Every 4 weeks means 13 charges a year.

## 4. Zety

Template resume, CV and cover letter builder with "Improve with AI" and "Generate", a resume check for "30+ issues", instant job matches, bundled Bold.Pro. Footer "© 2026 Works Limited"; 7 language sites (V-site).

| Area | Finding | Label |
|---|---|---|
| Truthfulness | No statement found | I |
| Saving per job | "Customize and edit your resume for different jobs"; no tracker | V-site |
| Export | Free: TXT only. Paid: PDF, Word, TXT | V-site |
| Singapore/APAC | SGD prices for SG visitor; no Singapore conventions | V-site / I |

- **Pricing (SGD, SG browser):** Basic free (TXT only). Pro 14-day trial S$2.95, then "auto-renews at S$34.95 billed every 4 weeks". Annual S$71.40 upfront (S$5.95/month), auto-renews (V-site). The trial converts into the 4-weekly plan, far dearer than annual (I).
- **Sentiment:** Trustpilot 4.4 from 12,917, 14% one-star (V-3p). Nov 10, 2026: charged months after cancelling; Zety replied the trial auto-renews. Nov 12, 2026: missed renewal terms due to language barrier; goodwill refund. Nov 15, 2026 (4 stars): asks for renewal reminders. Praise: easy interface, AI bullet tool. Many similar complaints on Sikayetvar (2nd, titles only).
- **Lesson:** local currency is good. A trial converting without reminders is the category's top complaint. Show total yearly cost, send reminders, never paywall a user's own document.

## 5. Novoresume

Resume, CV and cover letter builder; AI credits "powered by Claude (Anthropic)" (V-site).

| Area | Finding | Label |
|---|---|---|
| AI | Credits: Basic 2/month, Pro 40/month, Pro Pass 10 | V-site |
| Truthfulness | No statement found | I |
| Saving per job | Pro up to 144 documents; no job link | V-site / I |
| Export | PDF with "real text layer" | V-site |
| Free plan | 1 resume, 1 page, 8 templates, branding on PDF; never expires | V-site |
| Singapore/APAC | Regional prices on plan cards did not render | V-site |

- **Terms (V-site):** Pro monthly/quarterly/yearly, auto-renews, cancel in settings. Pro Pass: one month, paid once, no renewal. 14-day money-back on first upgrade. After Pro ends, documents stay saved and users can swap Pro features for free ones so downloads work.
- **Sentiment:** Trustpilot 4.3 from 1,610 (V-3p). Oct 7, 2026: quarterly rose €35.99 to €49.99 on repurchase (company: lower price was a discount); job tracker removed. Sep 15, 2026: one-page download now asks for payment (premium element triggers it). Sep 1, 2026: watermark on free plan. Praise: easy templates, helpful support.
- **Lesson:** learn from the non-renewing one-month pass and "downgrading keeps documents downloadable". Avoid premium elements that quietly block downloads.

## 6. FlowCV

Lightweight resume and cover letter builder; Pro adds job tracker and AI tools. Uniqkorn Creative GmbH (EU) (V-site).

| Area | Finding | Label |
|---|---|---|
| AI | Bullets, summaries, grammar, translation; no JD tailoring claim | V-site |
| Truthfulness | Not mentioned; GDPR statements only | V-site |
| Saving per job | Pro: "duplicate and save unlimited versions for specific roles"; Job Tracker on Pro | V-site |
| Export / import | PDF only (text-based); import from PDF, DOCX, image or pasted text | V-site |
| Singapore/APAC | Not found | I |

- **Pricing ("$"):** Free 1 resume + 1 letter, unlimited unbranded PDF downloads, 3 imports. Pro $60/year ($5/month); monthly and quarterly amounts not shown. Auto-renews; 14-day full refund; 25% student discount. After downgrade, oldest resume and letter stay editable and downloadable (V-site).
- **Lesson:** unlimited unbranded free PDFs are workable and set expectations that downloading your own resume should never be paywalled.

## 7. Reactive Resume (open source)

MIT-licensed, self-hostable builder (v6), 45.9k GitHub stars. Public site rxresu.me; reactiveresume.com is parked (V-site). Below from GitHub (V-3p).

| Area | Finding |
|---|---|
| AI | Assistant "proposes edits that you can accept or reject"; drafts letters from resume + posting; optional web search |
| AI providers | OpenAI, Anthropic, Gemini, OpenRouter, Ollama, compatible endpoints; user brings own |
| Export | PDF, DOCX, Markdown, JSON |
| Import | JSON Resume, LinkedIn export, PDF, Word |
| Library and sharing | Tagged library; public links with optional password and view stats; 18 templates |
| Price | Free |

- **Lesson:** the open-source baseline is free, private, multi-format, bring-your-own-model, with accept-or-reject edits. JobHub should compete on judgement (posting review, fact-linked tailoring, decision record per job), not price.

## 8. LinkedIn Premium

- **Resume Tips:** compares an uploaded resume with a posting and suggests rewrites of chosen sections; user decides what to keep. Desktop, English only. LinkedIn tells users to check responses "for authenticity" as they "may contain inaccuracies" (V-site).
- **Cover letters:** drafts from profile and job (2nd).
- **Premium Apply Assistant** (reported June 2026): highlights strong-match roles, pre-fills applications, drafts letters, shows a confidence indicator per element; user approves before submitting; also works for jobs off LinkedIn (V-3p citing Social Media Today; 2nd for original).
- **Price:** about $30/month, unverified (2nd).
- **Lesson:** "per-element indicator plus approve everything" is a good pattern; JobHub should show a link to the source fact, not a confidence number. The Apply Assistant pushes volume; "decide before you apply" is the counter-position.

## 9. CoverLetter AI (coverletter.ai)

- Upload resume, paste JD; matches keywords, tone and seniority; 26 templates (4 ATS-safe); inline editing; saved letters on paid plans; PDF or text export; resume kept in browser up to an hour during signup; no fact-checking claim (V-site).
- **Pricing ("$"):** Free 1 letter/day; Weekly $9.99 auto-renewing weekly; Lifetime $49 with 7-day money-back (V-site).
- **Lesson:** weekly auto-renewal is a trap; a stand-alone cover letter is a commodity.

## 10. Brief notes

- **Canva:** templates plus Magic Write ("powered by OpenAI"); no JD tailoring; one template labelled ATS-friendly; PDF, JPEG, PNG; Word mentioned (V-site).
- **Microsoft Copilot in Word:** marketed as resume builder; university guides use it to list skills missing against a JD (2nd).
- **Grammarly:** Resume Builder agent for Pro and Plus gives an "alignment score" against a JD and does not promise to beat ATS; cover letter generator (2nd).
- **Yoodli:** Starter free (5 lifetime sessions); Pro $8/month, Advanced $20/month billed yearly; "Yoodli does not offer refunds on cancellation"; no JD- or resume-built mock interviews on pricing page (V-site).
- **ChatGPT or Claude directly:** Jobscan (Oct 5, 2026, Julia Tell) argues AI-written resumes produce claims candidates cannot defend; recommends writing facts first, refining with AI, then asking per bullet "what would you say in the interview" (V-3p). UCSD and Wisconsin career centres report invented duties, degrees and certifications (2nd). A Resume Builder survey via Computerworld: 32% said they lied about skills using AI (2nd).

## Patterns

1. **Tailoring is everywhere; checking it is not.** Only Enhancv claims no hallucinations, and its reviews report changed dates and employer names. No product links a claim to a source fact.
2. **Best truthfulness design is "propose, then approve"** (Resume Worded, Enhancv MCP, Reactive Resume, LinkedIn). None shows why a line is supported.
3. **Chat editing has moved into general assistants** (Enhancv MCP; direct ChatGPT/Claude use).
4. **Scores are everywhere** (ATS, out of 100, relevancy, alignment, confidence). No scores is a genuinely different stance.
5. **Two pricing camps:** trial traps (Resume.io, Zety) vs transparent (FlowCV, Novoresume pass, Reactive Resume). Billing dominates negative reviews in the first camp.
6. **Per-job versions exist but are thin.** Enhancv and FlowCV keep a copy per job; nobody keeps a decision record.
7. **No Singapore conventions anywhere.** Only localisation found: SGD pricing on Zety.
8. **Export gaps:** Enhancv and FlowCV PDF only; Zety and Resume.io paywall PDF and Word; Reactive Resume gives PDF, Word, Markdown, JSON free.

## Table stakes users expect

1. Paste a JD, get a tailored resume and cover letter in seconds with matched and missing keywords.
2. Several saved versions, attached to a tracked job.
3. Inline editing where each AI change can be accepted or rejected.
4. A free, unbranded PDF of your own document, plus Word.
5. ATS-safe templates; import from PDF, Word or LinkedIn.
6. Clear cancel-anytime terms and a 7 to 14 day refund window.

## Gaps JobHub could own

1. **Each claim linked to its source.** Unsupported lines are flagged and cannot be exported until confirmed or removed.
2. **A chatbot that asks instead of inventing** when the job asks for something the profile lacks.
3. **A decision record per job:** posting review, the user's decision, and the checked resume and letter kept together.
4. **Singapore-aware checks:** prompt for a work pass or citizenship line; warn about NRIC, date of birth or age, photo, marital status and religion (in line with TAFEP's list of fields employers should not ask for; applying it to resumes is an inference); flag expected-salary placement.
5. **Feedback that explains instead of scoring.**
6. **Honest pricing as a feature:** no trial that converts, no download paywall, renewal reminders, a one-off pass, documents downloadable after downgrade.
7. **An interview check before export:** "how would you explain this line?"

## Limitations

- Prices depend on visitor region; Novoresume prices did not render; many "$" prices lack a confirmed currency.
- No accounts created, so AI behaviour comes from vendor claims and reviews, not testing.
- Trustpilot read from the first page only; scores are snapshots.
- Grammarly, Copilot, LinkedIn cover letter details and LinkedIn price are 2nd.
- Not researched: Resume Worded reviews, Big Interview, Canva Pro pricing.
- Singapore resume sources are mostly commercial blogs. TAFEP guidance targets employer forms; applying it to resumes is an inference.
