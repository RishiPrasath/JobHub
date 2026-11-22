# Run D findings: Form friction, autofill tools, and Singapore rules on what forms may ask

Run date: 2026-11-22. Role: Competitive Landscape Researcher (#05). Read-only desk research (about 17 web searches, about 14 public pages fetched). No accounts, sign-ins, installs, typed input or submissions. Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report.

Evidence labels as in the [round brief](../../round-brief.md). Chrome Web Store, Trustpilot, Teal and Monster returned HTTP 403 and were not read directly.

**Could not be seen:** any live employer form or Workday tenant; Simplify's terms of service; the Monster report (figures via search summary, 2nd); the Appcast and InFlight primary reports (2nd, via SHRM and press releases); PDPC 2024 NRIC statements; Workday, Greenhouse and Lever terms on automation.

## Friction evidence

| Metric | Figure | Source | Geography | Date | Sample | Bias | Label |
|---|---|---|---|---|---|---|---|
| Average completion time, Fortune 500 flows | 4 min 52 s; about 51 clicks; about 9 more clicks before the form; 48% show ATS logos | InFlight audit via SHRM and press release | US | Nov 2021 | One role searched ("software developer"), Fortune 500; N not stated | Vendor audit; one role; large employers only | 2nd |
| Quit mid-application (length or complexity) | 60% | CareerBuilder survey via SHRM | Not stated (US-based experts) | Mar 2016 | N not given | Old; method unknown | V-3p |
| Re-entering work history as an abandonment cause | Named as a cause, no figure; quote: "Candidates hate re-entering resume information" | SHRM, 2016 | Not stated | 2016 | None | One agency's quote | V-3p |
| Abandoned an application as "too tedious" | 92% ever; 32% often or very often; Gen Z 42% | Resume Genius with Pollfish | US | 10 Nov 2026 | 900; Baby Boomers only 45 | Resume-tool vendor; self-report; fieldwork dates not stated | V-3p |
| Manual form filling "most annoying" part | 30% of respondents | Same survey | US | 2026 | 900 | Same | V-3p |
| Stated drop-off thresholds | 43% would quit within 15 min; 6 in 10 by 20 min | Monster survey via search summary | US | Fielded 7 Feb 2026 | 1,002 employed workers | Stated intent, not behaviour; vendor; employed people only | 2nd |
| Click "Apply" but never finish | 92% | Appcast via search summary | Not stated | Not stated | Not stated | Vendor data; different definition from a mid-form quit | 2nd |
| Completion vs question count | Falls by almost 50% at 50 or more questions versus 25 or fewer | Appcast via search summary | Not stated | Not stated | Not stated | Vendor | 2nd |
| Average application drop-off | 41.2% | Recruitee "State of Hiring" via search summary | Not stated | Not stated | Not stated | Recruitee sells recruiting software | 2nd |
| Workday claims (account per employer, resume re-entry, about 30 minutes for a "5-minute" form, timeouts, mobile upload failures) | Anecdotal, unmeasured; its "365%" figure is impossible as stated | Simplify blog, 13 Feb 2025, updated 12 Nov 2026 | Not stated | 2025 to 2026 | None | Simplify sells a Workday autofill | V-3p |
| Workday session timeout | "Within ten minutes" | Chrome Web Store listing for Prevent-Workday-Timeout, plus a Resuminder guide saying refresh, back button or timeout can discard unsaved stage input | Not stated | Not stated | None | Developer claims; tenant behaviour varies | 2nd |
| Smartphone share of active candidates starting a search | 86% | Kelton via SHRM 2016 | US | 2016 | Not stated | Old | V-3p |
| Why re-entry exists | Parsers can merge job titles or assign one date range to several roles; re-entry may be deliberate | Jobscan and FroGHire via search summary | Not stated | Not stated | None | Both are ATS and resume vendors | 2nd |
| Checkout form benchmark (analogy only) | Average 11.3 fields; testers intimidated at 10 to 15+ fields; 17% abandoned a purchase in 3 months because checkout was too long or complex | Baymard | Not stated for the 2026 survey | 2024 benchmark; 2026 survey | 1,000+ shoppers (2026) | Not job forms; Baymard is retesting its checkout research, results expected 2027 | 2nd |

Not found: CAPTCHA frequency on job forms, mobile-specific completion rates, any Singapore-specific time-to-complete figure.

## Tool by tool

| Tool | What it saves or fills | Answer-bank features | Where it fails | Source | Label |
|---|---|---|---|---|---|
| Simplify Copilot | Maps form questions to profile data on "100+" portals, including Workday, Greenhouse, iCIMS, Taleo, Lever, SmartRecruiters. The user reviews and submits in the browser. Per its privacy policy (updated 19 Aug 2026) it collects form field labels, options and entered values; stores a profile copy, resume and recent answers locally; demographic answers are optional and used to pre-fill equal-employment sections. | Profile sections (Profile, Personal Info, Job Preferences). A help-centre article says custom-question answers are reused when the same question recurs; a Simplify FAQ says these are stored in the browser only. No single screen to browse, search or filter all saved answers was found. | Workday is brittle and memory-heavy in Firefox reviews. A competitor blog reports certifications filed under education, wrong dates, no fill on some sites, and that it works best on large ATS platforms. Billing complaints concern the paid tier, not autofill. | simplify.jobs/autofill (V-site), privacy policy (V-site), LoopCV and Adzuna blogs, Firefox reviews | V-site and 2nd |
| Teal extension | Job tracker plus AI autofill using the job description and Teal resumes; user edits before submitting. Chrome Web Store 4.9. | Not found | Not found; review sites disagree on how strong its autofill is | Search summary of Teal pages and comparison blogs | 2nd |
| LazyApply | Mass-apply on LinkedIn, Indeed, ZipRecruiter and Dice with autofill, AI cover letter and resume tool | Not found | Web Store rating about 2.9 to 3.6; review summaries say it "makes major mistakes" and sends applications without per-application review. Teal's own review is a competitor view and could not be read | Search summary of Chrome Web Store and Teal | 2nd |
| Jobscan | Resume-to-job-description analyser with an extension component; does not autofill applications | Not applicable | Not applicable | Search summary of comparison blogs | 2nd |
| Browser autofill and password managers | Contact fields and passwords | Not researched | Not researched | None | I |
| Workday-only helper extensions (SpeedyApply, Prevent-Workday-Timeout, Workday Account Auto-Fill) | Per-store descriptions: autofill or keep the session alive | Not found | One review said progress "was uploaded" but came back empty; another said it works only 1 time in 3 | Chrome Web Store reviews via search summary | 2nd |

Workday, Greenhouse and Lever behaviour was seen only through Simplify's own claims and user reviews. Nothing was read from Greenhouse's or Lever's own pages.

## Coping workarounds

- Simplify and similar extensions (above).
- A session-keepalive extension for Workday; its existence suggests the timeout is a real pain, though only the developer says so.
- Spreadsheets, notes apps, browser autofill and password managers: no source describing how job seekers use these was found. A gap, not a finding.
- Employers' own workaround: Greenhouse offers "application limits" to block repeat applications from the same candidate, showing the employer side is already adding friction against bulk applying.

## Terms and bot-detection risks

- No Workday, Greenhouse or Lever terms on automated filling were found; their terms pages were not read.
- Greenhouse's CEO describes an "AI doom loop" and says its data shows applicants using auto-apply tools (Fortune, 27 Jul 2026; 2nd). Greenhouse cites a figure that 22% use automated bots (2nd). How detection works is not stated.
- Nothing found about account bans for using extensions.
- Installing Simplify is described as agreeing to its terms (search summary; terms not read). The extension asks for access to data on all websites (Firefox listing, via search summary), a permission a JobHub copy tool would not need.
- Inference: a tool that never fills, clicks or submits does not match the "bot" pattern, though no terms were read to confirm.

## Singapore guidance on what forms may ask

**TAFEP "Preparing Job Application Forms"** (V-site, no publication date, footer 2025):
- Core test: "Fair job application forms collect information only directly related to the qualifications."
- Fields to remove: age (including date of birth), gender, race, religion, marital status and family responsibilities, disability, photographs, National Service liability, mental health condition, and NRIC number.
- "NRIC numbers can reveal the age of a person." Accept alternatives such as a passport number.
- If a sensitive field is truly needed: "request for these at the point of job offer or state your reasons clearly."

**PDPC Advisory Guidelines for NRIC** (issued 31 Aug 2018, V-3p, read via PDF text extraction):
- The guidelines' own example treats an application form that "does not require Benny to provide his NRIC number" as the model; employers collect the NRIC later for employment records under the Employment Act.
- "There is no requirement under the law to ask for NRIC numbers for the purpose of job applications."
- Other exceptions (for example evaluative purposes, or highly accurate identification) may apply, but conduct must still be reasonable (para 3.10).
- A search summary says a Dec 2024 ministry statement means the guidelines will be updated and stay valid meanwhile; the update was not seen (2nd).

**MOM written parliamentary answer, 8 Sep 2026** (V-site): does not mention application forms. Employers should "only ask for information relevant to assessing" suitability and explain why if asking for personal information before an offer. Adverse decisions based on protected characteristics would breach the Workplace Fairness Act; the page gives no commencement date (a search summary says end 2027, 2nd).

## Clipboard and privacy flags

- **Windows clipboard history** (Microsoft Support, V-3p): when on, keeps 25 items; unpinned items clear on restart; pinned items persist; sync across devices is tied to the Microsoft account. No sensitive-data warning on the page.
- **Browser clipboard** (MDN, V-3p): `navigator.clipboard.writeText` needs HTTPS and a user action. Firefox and Safari do not use the clipboard-write permission; Chromium may request it. Reads are the more gated direction, so a copy-only tool avoids the read prompt.
- **Android** (search summary, 2nd): developers can flag sensitive clips so keyboards hide the preview; Gboard history retention reported inconsistently (about an hour unless pinned); reports say Samsung's keyboard kept copied passwords; GrapheneOS added "Secure Paste" in Sept 2026.
- **iOS:** not researched.
- Inference: anything copied from a store (phone number, notice period, salary expectation) may linger in clipboard history or sync with the cloud.

## What could NOT be found

- Any first-party Singapore time or abandonment figure.
- Share forced to retype after resume parsing as a number (apart from Resume Genius's "30% most annoying" about manual filling).
- CAPTCHA frequency on application forms; mobile completion rates for applications.
- How job seekers use spreadsheets, notes apps or password managers.
- Terms from Workday, Greenhouse, Lever or iCIMS about automated filling, and any documented account bans.
- Any documented "saved answers" screen in Simplify, Teal or LazyApply with grouping, tags, search, per-job and recent filters.
- Simplify's terms; the 2024 PDPC statements; TAFEP's sample application form.

## Limitations

- Vendor surveys dominate the friction data and define abandonment inconsistently; most are US-only and several are 5 to 10 years old.
- Some figures reached the run only through search summaries (Monster, Appcast, Recruitee, InFlight, Teal, LazyApply).
- Tool-review blogs are mostly competitors or affiliate sites.
- TAFEP's page has no publication date, and the Workplace Fairness Act is not yet in force, so the rules are currently guidance.
- Overall confidence is low to moderate; supports a direction, not figures to quote as fact. N2 at best.

## Implications for a store-filter-copy tool (observations, not decisions)

- Friction is real and widely reported, but there is no Singapore figure. The retyping complaint is consistent across sources, so the owner's framing has support, though the figures are US vendor data.
- Simplify's answer reuse works by exact-question matching and the store is browser-local; no browse, search or filter screen was found. A store filtered by section, field name, per-job and recently used would offer something the reviewed tools did not show, though it may simply not have been seen.
- Re-entry may be intentional on employers' side because parsers merge titles and dates. Work-history entries therefore likely need to be copyable per entry (job title, employer, start date, end date, description separately), not as one block.
- Session timeouts (Workday, reportedly about 10 minutes) imply copy items should be fast to reach and phone-friendly, since typing and switching apps risk losing a stage.
- Fields Singapore guidance says to avoid (age or date of birth, gender, race, religion, marital or family status, disability, photographs, National Service, mental health, NRIC) match the FEAT-016 "Not collected" list. If an employer's form still asks for them, the store would need a position on that. The NRIC exception at offer stage is the likely case.
- A copy-only tool never touches the page, so the bot-detection and terms concerns about autofill do not seem to apply, though that was not verified against any employer's terms.
- Clipboard history on Windows and phone keyboards may keep copied personal details, and Windows can sync them. Copy buttons for contact details, work authorisation or salary expectation may deserve a flag for the Responsible AI Reviewer.
- A page-level copy button needs HTTPS and a click. Write-only copy avoids the read prompts that Firefox and Safari show.
