# Run E findings: How long to wait before archiving a no-reply application

Run date: 2026-11-22. Added after the main R11 pass, at the owner's request, to settle one open question: should the wait before archiving be a fixed value, user-chosen, or a default the user can change? Read-only desk research (about 12 searches, about 20 page fetches). No logins or submissions. Note: the research subagent was not allowed to write files, so this file was saved by the round lead from its returned report. It extends runs A to D and does not redo them.

Evidence labels as in the [round brief](../../round-brief.md). Search-engine summaries were used as leads only and are labelled 2nd.

**Fetched and read:** Scoutify Data Lab (Nov 2026), Careery benchmark page, Indeed Singapore help (My Jobs), Workstream help (auto-archive), Wellfound help (expiry), MOE school-counsellor application page (updated 5 Nov 2026), MHA application-process page, HCA articles on the Glassdoor 2017 and Robert Half 2018 Singapore surveys, Spool's UIE post, Jachimowicz et al. 2019 (abstract only).

**Blocked or failed (not worked around):** Teal help pages (403); Singstat/DOS FAQ and SID recruitment page (404); ask.gov.sg (403); an MCF content page had no timing information.

## Findings

**E1. The best public response-delay distribution is a vendor dataset; it shows a real but modest late tail (V-3p, vendor, medium confidence).**
- Scoutify Data Lab: 132,127 cold applications to company career sites, sent 1 Jun to 26 Sep 2026 and measured on 10 Nov 2026, so each had at least 45 days.
- 43% got a human reply within 45 days; 57% got none.
- Of the replies: median about 5 days; 61% within 1 week; 77% within 2 weeks; 92% within 1 month; about 1 in 12 replies arrived after 1 month.
- Interview invitations: median about 2 days; 69% within 1 week; 7% after 1 month.
- Lead's arithmetic (I): about 3 to 4% of all applications (0.43 x 0.08) got a first human reply after day 30.
- Nothing past day 45 was observed, so the tail beyond 6 weeks is unmeasured.
- Bias: Scoutify sells an auto-apply service; data skews to large US employers on Workday and Greenhouse; the applications were programmatic and cold; replies sent to a candidate's own inbox were not captured; "human reply" includes automated first-round screens.

**E2. A second vendor dataset points the same way but is weaker (V-3p, vendor, low to medium).** Careery: 1,000+ anonymised users tracked 45 days, first interview-related email only; median 6.7 days, middle half 4.5 to 8.1 days. It reports no share replying after 2, 4 or 6 weeks and says later replies are "rare" without counting them. Only people who got email replies are in the sample, so no no-reply rate can be computed; an unvalidated classifier flags the emails; Careery sells an application service. Its "treat silence after 2 weeks as soft rejection" line is its advice, not something the data shows.

**E3. The only Singapore late-tail figure is old, self-reported and recruiter-run (V-3p, low to medium).** Robert Half Singapore (12 Jul 2018, 500 jobseekers, via HCA): 64% waited more than a month to hear back after an interview; 37% more than 6 weeks; 26% more than 2 months; only 1% got same-day feedback. 90% said waiting up to a month from application to final offer was reasonable. The article does not say whether "waited" includes people who eventually heard back or those who never did; the sample is self-selected and 8 years old; Robert Half is a recruiter with an interest. Read as an indication that long post-interview waits were common in Singapore, not a measured reply distribution.

**E4. Singapore government employers state waits but do not publish a "give up" point (V-site for MOE; 2nd for the rest).** MOE (school-counsellor page, updated 5 Nov 2026): applicants "can expect to hear from us within 4 weeks of the close of the application window"; if nothing within 3 weeks after interview, "your application is still being actively considered". The page does not mention 6 weeks or treat silence as rejection. Search snippets from other MOE pages (not fetched, 2nd) say a high-volume window can take up to 6 weeks. DOS and MHA figures come from snippets only: DOS interview results within 2 to 3 weeks; MHA tentative offer 1 to 2 weeks after interview, formal offer 5 to 6 weeks later; SID security-sensitive roles longer. The MHA page fetched stated no timelines. Implication (I): a silence threshold below about 4 to 7 weeks would conflict with MOE's own wording.

**E5. Hiring timelines by role type differ in direction but are not matched to reply delays (2nd, vendor, low).** Vendor benchmarks from search results, not fetched, differing definitions: retail SmartRecruiters 25-day median, JobScore 19 days, Manatal 29 days; restaurant and food service JobScore 16 days, Manatal 26 days; hospitality SmartRecruiters 39 days (global median 38); professional services Manatal 47 days; technology SmartRecruiters 48 days. Singapore: Glassdoor 2017 (84,000 candidates, 25 countries) measured 25.4 days from application to offer or rejection, the longest in Southeast Asia; an ask.gov.sg snippet gives 2 to 3 weeks application to offer (page blocked). These are time-to-hire or time-to-fill, not time-to-first-reply, and none is Singapore shift or F&B. No Singapore shift, retail or F&B reply-time data found. Reading (I): frontline hiring is probably faster and professional or public-sector slower, but the evidence does not size the gap for replies.

**E6. Tool thresholds are all short and almost none is documented as configurable (V-site where marked).**
- Indeed: "Response seems unlikely" after at least 2 weeks of no activity or when the employer has hired enough; mobile-only; help page does not say whether configurable.
- Wellfound: an application with no company action expires after 2 weeks.
- Workstream (employer-side ATS): the clear case of a changeable default; auto-archives after 30 days of no interaction by default, admins can set 1 to 90 days, archived items can be unarchived.
- Teal: advises manual weekly review and archiving stale jobs after about 3 weeks (2nd); closing with "No Response" moves a job to Archived; no time-based auto-archive found; help page blocked.
- Zapier/Notion template: marks "no response" after 28 days (2nd, snippet).
- Advice, not tool behaviour: Careery 45 days; JobStreet Malaysia reportedly 2 months (2nd, Run D); Jobstreet SG about 2 weeks after follow-up (Run C).

**E7. Defaults change what people do on average, but evidence that people change a default is thin and mostly old (V-3p, medium for the effect, low for transfer).** Jachimowicz et al. 2019 (Behavioural Public Policy): 58 default studies, n = 73,675, d = 0.68 (95% CI 0.53 to 0.83); effects vary a lot, a few studies show none, two are negative; defaults work more through endorsement and endowment (the default signals what the designer wants or the status quo). A critique reported in search results says none of these studies involved substantial or repeated effort (2nd). Spool (UIE, 11 Sep 2011): fewer than 5% of "several hundred" volunteers who emailed their Word settings file had changed any setting (self-selected, Microsoft Word, 2011). No evidence on defaults in job-search tools, on how many users change an archive window, or on how people decide when to stop waiting.

**E8. Counter-signal: a default can read as advice (I).** The endorsement mechanism means a "30 days" default may be taken as "employers usually reply by then". MOE's "still actively considered" wording and Scoutify's 1-in-12 late tail both argue against implying that.

## Response-delay figures

| Stage | Figure | Source | Geography | Date | Sample | Bias |
|---|---|---|---|---|---|---|
| After applying, first human reply | Median about 5 days; 61% within 1 wk, 77% within 2 wks, 92% within 1 month; about 1 in 12 replies after 1 month | Scoutify Data Lab (V-3p) | Skews US, large employers on Workday/Greenhouse | Applications Jun to Sep 2026; post Nov 2026 | 132,127 applications; 45-day window | Auto-apply vendor; cold programmatic applications; own-inbox replies missed |
| After applying, any human reply | 43% replied; 57% none in 45 days | Scoutify (V-3p) | As above | As above | As above | As above |
| Interview invitation | Median about 2 days; 69% within 1 wk; 7% after 1 month | Scoutify (V-3p) | As above | As above | As above | Includes automated first-round screens |
| By ATS | Workday 44% replied, median 4.9 days; Greenhouse 46%, 3.9; SmartRecruiters 18%, 4.7; Ashby 28%, 4.0 | Scoutify (V-3p) | As above | As above | 98,704 / 23,743 / 8,541 / 1,043 | As above |
| After applying, first interview-related email | Median 6.7 days; p25 4.5, p75 8.1 | Careery (V-3p) | Not stated | 2025 data; page Jan 2026 | "1,000+" users; 45 days | Vendor; responders only; unvalidated classifier |
| After interview, wait | 64% waited over 1 month; 37% over 6 wks; 26% over 2 months | Robert Half Singapore via HCA (V-3p) | Singapore | 12 Jul 2018 | 500 jobseekers | Recruiter; old; self-reported; unclear if "waited" includes never heard |
| Acceptable wait | 90% say up to 1 month from application to final offer is reasonable | Robert Half via HCA (V-3p) | Singapore | 2018 | 500 | As above; stated preference |
| Application to offer or rejection | 25.4 days Singapore (longest in SE Asia); 30.9 Japan; about 23 global | Glassdoor 2017 via HCA (V-3p) | Singapore, 25 countries | 15 Aug 2017 | 84,000 candidates | Old; offers and rejections only |
| Government, after window closes | Within 4 weeks; 3 wks after interview "still actively considered" | MOE page (V-site) | Singapore, one agency | Updated 5 Nov 2026 | n/a | Employer policy, not observed |
| Government, high volume | Up to 6 weeks | MOE snippets (2nd) | Singapore | Not confirmed | n/a | Not fetched |
| Government, other | DOS 2 to 3 wks after interview; MHA tentative offer 1 to 2 wks, formal 5 to 6 wks later | Search snippets (2nd) | Singapore | Not confirmed | n/a | DOS/SID pages 404; MHA page fetched did not show it |
| Time to hire, frontline | 16 to 29 days (restaurant/food 16 to 26; retail 19 to 29) | JobScore, Manatal, SmartRecruiters (2nd) | Mostly US | 2025 to 26 | Vendor data | Definitions differ; not reply times |
| Time to hire, professional | Professional services 47 days; tech 48 days; hospitality 39 days | Manatal, SmartRecruiters (2nd) | Mostly US | 2025 to 26 | Vendor data | As above |
| Reply after 6+ weeks | Not found with a measured figure | n/a | n/a | n/a | n/a | n/a |

## Tool archive thresholds

| Tool | Threshold | Fixed or configurable | Source |
|---|---|---|---|
| Indeed (job seeker) | "Response seems unlikely" after at least 2 weeks of no activity or when hired enough; mobile-only | Not documented as configurable; user can also Archive manually | V-site (Indeed SG help) |
| Wellfound | Expires after 2 weeks of no company action | Page silent on configurability | V-site |
| LinkedIn | Review-time badge hidden if average over 21 days (a display rule, not archive) | Fixed, employer-level | V-site (Run D) |
| Teal | Advice to archive after about 3 weeks; "No Response" is a manual status | Manual, no time-based setting found | 2nd (summary; help page blocked) |
| Workstream (employer ATS) | Auto-archives after 30 days of no interaction | Configurable default: 1 to 90 days; unarchive available | V-site |
| Zapier/Notion template | Marks "no response" after 28 days | Editable template | 2nd (snippet) |
| Huntr, Simplify, JobStreet SG | No time-based archive found | n/a | I (Run D plus this search) |
| Careery (advice) | 45 days then assume rejection | Advice | V-3p |
| JobStreet Malaysia (advice) | 2 months | Advice | 2nd (Run D) |

## What could NOT be found

- Any measured share of replies after 6, 8 or 12 weeks; the one big dataset stops at 45 days.
- Singapore reply-time data from MCF, JobStreet, MOM or any named survey (MOM says it does not collect this; Run B).
- Reply delays for Singapore shift, retail or F&B work; only generic time-to-hire vendor figures.
- A fetched Singapore corporate or agency timeline.
- Any study of whether people reopen or revive no-reply applications, or how often employers reply to a dormant application; only anecdotes (Blind, Ask a Manager) and a recruiter claim in a snippet that reversals after a rejection are a single-digit share of hires (not read).
- Any behavioural study of how job seekers decide to stop waiting.
- Any data on how often users change a default archive window.
- Teal's own help text and any documented configurability of Indeed's two-week rule.

## Limitations

- Search summaries are model-written and leads only.
- The two usable reply-time datasets (Scoutify, Careery) are vendor-run, US-leaning and capped at 45 days.
- Singapore figures are old (2017, 2018) or one agency's stated policy.
- Time-to-hire is not time-to-first-reply, and no source separates replies by role type.
- The default-effect literature is mostly opt-out enrolment, not a threshold the user must reason about.
- Desk research: stated expectations are not behaviour; actual wait and reopen behaviour needs the N3 interview and diary test.

## Evidence-based reading of the three designs (no product decisions)

**(a) Fixed value.**
- Supported: tools do use fixed, short windows (Indeed 2 weeks, Wellfound 2 weeks); Scoutify says about 77% of replies come within 2 weeks and 92% within a month.
- Not supported: any single number fits everyone. Scoutify's 8% late tail, the MOE statement (4 weeks plus 3 weeks after interview "still active"), Robert Half Singapore's long post-interview waits, and differing time-to-hire by role type all argue against one fixed value.
- A fixed archive value risks implying "no reply = rejected", contradicting MOE. A fixed 2-week value would archive roughly 23% of eventual replies in Scoutify's data, so reopening would matter.

**(b) User chooses, no default.**
- Supported: no published norm exists for when to stop and Singapore sources give no consensus; Workstream's configurable setting shows tools allow choice.
- Not supported: that users can choose well without a reference point. No evidence on how people decide to stop waiting, or on job seekers specifically. The default literature suggests an empty setting might be left unset or filled with whatever example is shown, but this was not tested for job search.

**(c) Sensible default the user can change.**
- Supported: defaults shift behaviour (d = 0.68) and have a documented analogue (Workstream 30 days, 1 to 90 days, with unarchive). Teal's 3 weeks, Careery's 45 days and Zapier's 28 days sit around a 3 to 6 week range.
- Not supported: which number is right. The data cover only 45 days, so a default beyond 6 weeks has no measured basis; no evidence on how often people change defaults here (Spool's under-5% is old and not comparable). A default also acts as an implicit claim about normal reply times, so its label matters, as MOE's wording shows.

**By role type (weak evidence only).**
- Entry-level and general: the only measured distribution (Scoutify) shows most replies within 2 weeks and a tail to 45 days.
- Shift, retail, F&B: time-to-hire figures are shorter (about 16 to 29 days, 2nd), so a shorter default is plausible; no reply-time or Singapore evidence.
- Professional: longer time-to-hire (about 39 to 48 days, 2nd) and Robert Half's long post-interview waits point to a longer window.
- Public sector: employers state their own windows (MOE 4 weeks after closing, plus 3 weeks after interview), so a default shorter than that would conflict with their own wording.

**Overall.** The evidence supports "reopenable, and not one number for all roles". It does not support a specific number of days. Whichever design is used, the reopen path is what limits the cost of archiving too early. No measured data was found on how often late replies revive a dormant application, only anecdotes.
