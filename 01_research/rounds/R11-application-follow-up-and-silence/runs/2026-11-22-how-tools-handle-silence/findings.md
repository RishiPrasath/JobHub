# Run D findings: How existing tools and portals handle application status and employer silence

Run date: 2026-11-22. Role: Competitive Landscape Researcher (#05). Read-only desk research on public pages. No logins, accounts, purchases or form submissions. Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report.

Evidence labels as in the [round brief](../../round-brief.md).

**Method caveat.** Page text came through a fetch tool that summarises each page, so quotes and thresholds are as summarised, not read raw. Where a page returned 403 or 404, or only a search snippet exists, the label is 2nd or I. "TYPICALLY REPLIES IN 30 DAYS" on MyCareersFuture comes from R10 and was not re-verified. Feature lists already in R07/R10 were not repeated.

## Scope

About 17 products: Teal, Huntr, Simplify, Careerflow, Jobscan, Notion/Trello templates, LinkedIn, JobStreet/SEEK, MyCareersFuture, Indeed, Glassdoor, Workday, Greenhouse, Lever, Ashby, Wellfound, and a Notion "Job Search HQ" template.

Read directly: LinkedIn Help (a508716) and hirer-responsiveness insights; Indeed job-seeker help and employer badge help; Workable's Indeed-badge help; Simplify Email Integration; Huntr activities, pricing and tracker pages; Careerflow reminders and home; Jobscan tracker; Ashby auto-reject release; Greenhouse rejection-email help and October 2025 release notes; SEEK developer docs; MOM parliamentary reply of 14 Oct 2025; Notion's official template page; Product Hunt listing for Job Search HQ; a Workday candidate-view guide (UW-Madison); Fortune (Bloomberg) 2 Feb 2025; the Greenhouse press release via PRNewswire; Wellfound's blog.

Blocked (403/404), snippets only (2nd): Teal help centre, pricing and tracker page, Teal blog, Glassdoor blog, SEEK's Medium post, Microsoft Learn LinkedIn page, Lever help, Careerflow tracker URL. The MyCareersFuture FAQ PDF was unreadable and not relied on.

## Product-by-product

| Product | What it does about status or silence | Data source | Price gate | Label | Note |
|---|---|---|---|---|---|
| Teal | Statuses Bookmarked to Accepted, follow-up dates, stage-based follow-up and withdrawal email templates. Its guidance reportedly says to archive after about 3 weeks of silence and send up to three follow-ups. | User-entered | Not verified (pricing page blocked) | 2nd (search snippets) | Marketing line "Never miss a follow-up again." No automatic closure found. Free vs Teal+ split unverified. |
| Huntr | Kanban stages. Activities act as a to-do list ("log follow-up emails as activities"). Moving a job to Apply, Interview, Offer Received or Offer Accepted auto-logs an activity. | User-entered | Free up to 100 jobs; Pro $40/mo, $30/mo quarterly or $26.66/mo half-yearly on the pricing page (tracker page says $30/mo; sources disagree) | V-site | Activities page does not describe reminders or archiving; pricing page does not mention reminders. |
| Simplify | Free tracker. Gmail integration matches email threads to jobs and recommends status changes, including rejections. Nothing changes until the user approves. | Inferred from user's email, user-approved | Tracker and Gmail sync free; Simplify+ only for AI drafting | V-site | Marketing says a good tracker should "remind you to follow-up"; not confirmed Simplify does. Integration described as beta in a snippet (2nd). |
| Careerflow | Tracker with "set reminders for follow-ups"; reminder types include message, thank-you, check-in and recurring. Page does not mention ghosting. | User-set | Basic (free) tracker "limited"; Premium $8.99/wk to $14.41/mo annual; reminders' plan not stated | V-site | Claims such as "10X faster" are unsupported vendor claims. |
| Jobscan | Tracker boards with tasks, contacts and notes. No ghosted status, no reminders mentioned. | User-entered | Page says "free" and links to pricing; tiers not seen | V-site | Silence not addressed. |
| Notion "Job Search HQ" (paid template) | Dedicated Ghosted Kanban status, a "who to follow up with today" view; one commenter says it pushed them to reply to a recruiter. | User-entered | About $3.60 one-time | V-3p (Product Hunt) | Commenters praise the Ghosted column; one asked for real notifications because they must open the page daily. |
| Notion official template | Generic progress review and deadline colouring. No Ghosted status or reminders shown. | User-entered | Price not shown | V-site | 4.85 average from 800+ ratings, from Notion's own page. |
| Trello / Airtable templates | Not read (Trello page failed to load). | I | n/a | I | Searches show custom-column trackers with "Ghosted" as an example column (ClickUp roundup, 2nd). |
| LinkedIn (applied jobs, Easy Apply) | Applicant sees "Application viewed" and "Resume downloaded" for Easy Apply. Page says these do not guarantee a message or interview. | Employer-action-derived | None found | V-site | Help page lists no "rejected" status. Developer docs reportedly list rejected too (2nd). |
| LinkedIn hirer responsiveness insights | Job pages show "Actively reviewing applicants", "Review time is typically 1 week" (hidden if the average exceeds 21 days), "Responses managed off LinkedIn", or "No response insights available yet". | Inferred from employer actions (views, rejections, InMail) | None stated | V-site | Review time uses at least 35% of applications over 30 days. Hirers can opt out. Fortune (Feb 2025) said it was being tested on a small number of postings. |
| Indeed (applied jobs) | Employer-set: Application viewed, Employer reached out, Not selected. User-set: No longer interested, Interviewing, Offer received, Hired. Indeed-set, mobile only: Applied, Employer reviewing, "Response seems unlikely" (employer hired enough, or no activity for at least two weeks), Job closed. User can Archive. | Mixed: employer, user, Indeed inference | None found | V-site | Closest mainstream "closure" signal. Indeed says on Trustpilot that employers handle outreach (2nd). |
| Indeed Responsive Employer badge | Icon on listings when the employer's response rate is above 51%, recalculated weekly over 30 days. Counts emails, replies, updating status in ATS, automated not-selected emails. Fortune adds median response-time labels since 2023. | Employer behaviour | Employer needs ATS disposition sync; free to job seekers | V-site (Indeed AU help, Workable help) | Indeed's own page does not describe how the badge looks. Median vs average for labels unverified. |
| MyCareersFuture | "Typically replies in N days" (R10). MOM said on 14 Oct 2025 it is introducing filters to help identify more responsive employers. Search snippets say status shows "Under Review" once the employer downloads the resume; a curated list of employers commits to updating status within 4 weeks (snippet). | Employer behaviour (inferred) / employer-supplied | Free | V-3p for the MOM reply; 2nd for the rest | MCF FAQ PDF unreadable; statuses and the 4-week list unverified. |
| JobStreet / SEEK | JobStreet sends an update when an employer views, and an "unlikely to progress" update when an employer marks the application so. SEEK's Medium post (blocked) reportedly says "Not Suitable" triggers an email after 48 hours. "Viewed status unavailable" appears for external ATS. | Employer-set | None found | 2nd (snippets) | JobStreet Malaysia help (2nd) says no reply within 2 months means consider it unsuccessful; no Singapore help page confirming this. JobStreet SG follow-up article (30 Oct 2026) gives no status tracking. |
| Glassdoor | No application-status or employer-response feature found. Publishes ghosting data in interview reviews. | n/a | n/a | I | Data blog blocked; snippets only (2nd). |
| Workday (candidate view) | UW-Madison guide: Submitted, In Progress, Completed (inactive tab), Withdrew. Closing the requisition or changing status "does not send them any kind of notification". | Employer-supplied | n/a | V-3p (university HR guide, updated 12 Dec 2025) | One institution's configuration; labels vary by employer. |
| Greenhouse | Employer-side: default and custom rejection-email templates. Verified badges (Communicative, Fair, Prepared, Respectful) in beta, announced 25 Sep 2024. | Employer-supplied | Employer product | V-site / V-3p | Press release gives no timeframe or required actions for "Communicative". It cites 31% of candidates never hearing back (Greenhouse data, Q2 2024) and about 14.4 million ignored applications. |
| Ashby | Auto-reject by criteria, with the notification email schedulable for later (released 26 Mar 2021). No inactivity-based auto-reject found. | Employer-set | Employer product | V-site | Delayed emails are a mechanism, not a timing standard. |
| Lever | Inactivity alerts for recruiters (search snippet). Help page returned 404. | Employer-side | n/a | 2nd | Alert goes to the recruiter, not the candidate. |
| Wellfound | Blog on ghosting gives no platform responsiveness labels and no follow-up interval. | n/a | n/a | V-3p | Do not equate Wellfound with the "Responds quickly" badge, which was Djinni's. |

## Patterns

- **Closure or auto-archive.** The only platform-side "closure" signal confirmed is Indeed's "Response seems unlikely" (mobile only) after two weeks with no activity. Teal's help reportedly suggests archiving after about 3 weeks (2nd). JobStreet Malaysia advice reportedly says 2 months (2nd). Lever's inactivity alerts go to the employer's recruiter. No tracker found auto-closes on a user-set N.
- **Expected-wait or responsiveness.** Three variants: LinkedIn's per-job review time (hidden above 21 days), Indeed's response-rate badge and (reportedly) median-time labels, and MyCareersFuture's "typically replies" label (R10). All are derived from employer behaviour, not from the individual's own application, and stop at the employer level.
- **Follow-up reminders.** Careerflow offers explicit reminders. Huntr uses activities and to-dos. Teal offers follow-up dates and templates. Simplify suggests a good tracker does this but this was not confirmed. Notion templates use views, with one user asking for real notifications.
- **Templates.** Teal has stage-based follow-up and withdrawal templates (2nd). JobStreet advice pages give sample follow-up emails. Platforms do not send follow-ups.
- **Employer-side auto-reject.** Greenhouse and Ashby let employers send rejection emails and (Ashby) delay them. Indeed counts automatic not-selected emails towards the badge. Workday setups may not notify on closing (one guide). Greenhouse's Verified Communicative badge is aimed at this, but criteria were not in the release text.

## What users say, with bias noted

- **Job Search HQ commenters (Product Hunt, 2026):** praise the Ghosted status as making silence "visible". Commenters on a paid-template launch page: self-selected, likely friendly to the maker.
- **Indeed "Response seems unlikely":** one Fishbowl post by an applicant who had interviewed and then saw it; one commenter called it discouraging but not final. Anecdote.
- **Teal:** Trustpilot 4/5 on 107 reviews (snippet); the page says customers were not invited, so self-selected. Most common request was custom columns. No comment on reminders found.
- **Huntr:** Trustpilot 4.5 on 19 reviews; Chrome Web Store 4.8; one reviewer found the tracker too complex (snippets). No comment on reminders found.
- **LinkedIn insights:** a Blind thread questioned reliability of related labels; recruiter-written explainers note the label reflects recruiter activity in LinkedIn, not hiring intent. Opinion.
- **Vendor and recruiter claims, not evidence of effect:** LoopCV (auto-apply vendor) claims "1-3% Easy Apply response rate" with no source. Greenhouse's ignored-application figures are its own data. Careerflow's "10X faster" is marketing.

## Gaps no tool fills (absence is interpretation)

- No tool turns a user's own application age and employer type into an expected wait for that application.
- Reminders trigger on dates the user sets; none found trigger on employer behaviour (for example "this employer typically replies in 30 days, you are at day 21").
- Employer-side "viewed" signals disappear for external-ATS applications (LinkedIn "managed off LinkedIn", SEEK "viewed status unavailable", Workday).
- No source found showing that reminders, badges or labels change employer behaviour or user outcomes.
- None found helps the user decide to stop, apart from Indeed's mobile status and Teal's guidance; none records the decision for later reuse.
- Responsiveness labels are about employers, not roles or recruiters.

## What could NOT be found

- Teal, Careerflow and Glassdoor primary pages (blocked or 404).
- The MyCareersFuture status list, the 4-week employer commitment list, and the "typically replies in N days" definition on an MCF page.
- A Singapore JobStreet status list; only Malaysia-era and snippet descriptions.
- Lever and SmartRecruiters candidate-side status behaviour, and Ashby candidate-side status.
- Trello and Airtable template contents.
- Indeed's exact label wording for response time; badge appearance.
- Any study of whether reminders or follow-ups improve replies, and real user reaction to MCF labels.
- Whether LinkedIn Premium gates responsiveness insights.

## Limitations and assumptions

- Desk research only; AI-gathered evidence capped at N2. Shows what features say they do, not whether they work.
- Page summaries came through a fetch tool, so exact wording and thresholds may differ slightly.
- Pricing observed on 2026-11-22 can change; Huntr's pro price differs between two of its own pages.
- Many pages show no publication date.
- Mobile apps and logged-in views were not checked; Indeed's mobile-only statuses were not tested directly.
- Greenhouse and Glassdoor ghosting figures are vendor-reported; sample sizes and methods not seen.

## Implications for the FEAT-012 candidate approaches (observations, not decisions)

1. **Plain status list.** The baseline every tracker offers. Common practice lets the user set the status; Indeed and LinkedIn add employer-derived statuses JobHub cannot see. Consistent with S-20 in the FEAT-012 file. A status-only list sits with Simplify and Huntr, free to start; no tracker evidence that reminders are needed for it to be useful, but also no test of that.
2. **Expected-wait signal.** The pattern exists in three places (LinkedIn review time, Indeed response rate and median labels, MCF "typically replies"), all employer-level and derived from employer behaviour. None is personalised to the user's application; LinkedIn hides it above 21 days and shows "managed off LinkedIn" for external-ATS jobs. JobHub would need a Singapore source such as the MCF label; R10 notes one exists. Reliability unknown, and MOM's planned filters are unspecified.
3. **Give-up-after-N-days rule.** Indeed uses 2 weeks of inactivity (platform-side, mobile); Teal's guidance reportedly 3 weeks (2nd); JobStreet Malaysia reportedly 2 months (2nd). No consensus N. All three are advice or platform inference, not tested outcomes. A user-set N would differ from what was seen, since no tracker read does it.
4. **Follow-up templates.** Teal (reported), JobStreet advice pages and Careerflow reminders cover this, but only JobStreet's Singapore article is a fully read source: one follow-up after 1 to 2 weeks, then move on. Fits the principle that JobHub never messages employers, since templates are for the user to send. No evidence follow-ups change reply rates.
5. **Closure step.** Indeed's Archive plus "Response seems unlikely", Teal's archive advice and Workday's "Completed" tab show closing is normal in tools. No tool found links closure to a decision record or learning loop, so the FEAT-004 link would be unusual rather than copied. Job Search HQ's Ghosted column shows users value naming silence, though the evidence is a few comments on a paid template.

Open items for the decision gate: MCF label definition and status list, Singapore JobStreet status wording, and Teal/Careerflow primary pages.
