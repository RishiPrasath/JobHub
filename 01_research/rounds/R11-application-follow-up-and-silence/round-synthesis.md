# Round 11 synthesis: Application follow-up and silence

Status: **draft, owner review pending.** Written by the round lead from the four specialist runs and the Responsible AI review. Specialist findings are in the run folders; this file is the lead's reading of them. It changes no scope and decides nothing.

Evidence is AI-gathered desk research, capped at N2. Run letters: A tracking habits, B silence and reply times, C following up and moving on, D how tools handle silence. "F" numbers refer to findings in the run files.

## Answer in brief

1. **Silence is real, and in Singapore it is tolerated by policy.** No law requires an employer to reply. MOM says it does not collect data on post-interview updates and does not track complaints about it. The Tripartite Standard asks adopters to inform unsuccessful candidates, but it is voluntary, and MOM declined to require reasons for rejection (B F1, F10).
2. **No usable Singapore numbers exist for how common silence is or how long replies take.** The figures that exist are vendor or recruiter surveys, mostly US, with different definitions (31% of applications never answered, 53% to 61% of respondents ghosted, 88% "ignored"). None gives days-to-reply or drop-off by stage for Singapore (B F2 to F4, reply-time table).
3. **A tracker cannot supply the information employers withhold.** This confirms the FEAT-012 file's S-20 note. What a user-side tool can give is memory (what did I apply to, when, where) and closure (I decided to stop). It cannot say where an application stands (A F11, D gaps).
4. **People record a small, consistent set of things, and abandon trackers because upkeep is manual.** Company, role, link, date, status, notes; sometimes the resume version used (A F2, F4). Evidence is small-sample and US or tech-skewed.
5. **Follow-up advice converges on "one polite email, then move on", but the timings disagree and no evidence shows it works.** Post-application advice is about 1 to 2 weeks; post-interview advice ranges from 3 days to 2 weeks; no study measures an effect on replies or hires (C F1 to F3, F6).
6. **No consensus give-up point exists.** Thresholds in sources range from 2 weeks to 2 months, mostly from advice or snippets. One employer (MOE) states that silence 3 weeks after an interview still means active consideration (B F5, conflicts below).
7. **"Expected wait" signals exist but only at employer level, and all come from employer behaviour.** MyCareersFuture ("typically replies in N days"), LinkedIn (review time, hidden above 21 days) and Indeed (response-rate badge) show them. None is personalised, and LinkedIn counts any "review" action as a response (B F6, D patterns).
8. **Evidence on the emotional side is thin and mixed.** One 554-person experiment found ghosting no worse than rejection on psychological needs, using a hypothetical task (C F7). US surveys name silence a top frustration (C F8, A F11). Singapore evidence is anecdote.
9. **Lower-wage, shift and gig workers are a blank.** No run found how they track or follow up; contact is likely phone or WhatsApp, and the advice found assumes email and professional hiring (A F10, C).
10. **No existing tool links "I gave up on this" to a recorded decision.** Closure exists as an archive state (Indeed, Workday, Teal advice) but not as a reasoned record (D gaps).

## What the evidence says about each candidate approach

Evidence labels only; whether to build any of them is the owner's decision (see [decision-gate.md](decision-gate.md)). Guardrails come from the Responsible AI review.

| # | Approach | Supported by | Undermined or unproven | Guardrails the review set |
|---|---|---|---|---|
| 1 | Plain status list the user updates | Consistent fields (A F2); user is the only party who knows the status (B F1); every tracker has it (D) | No evidence it would be kept up (A F4); cannot supply employer information | Neutral, user-chosen labels; no auto-status; no inferred statuses; privacy warning on notes; export and delete |
| 2 | Expected-wait signal | Pattern exists at three portals (B F6, D) | Method for MCF undocumented; LinkedIn hides it above 21 days; advice ranges conflict; none personalised; MOE says silence at 3 weeks is still consideration | Quote a named third-party figure with source and date only; show "no information" explicitly; never say overdue, late or unlikely; no employer ranking |
| 3 | User-set give-up-after-N rule | A user-set N fits the lack of any validated threshold (C F3) | No tracker does this (D); defaults contradict MOE; harm of missing a late reply | A reminder, not a status change; no default N; confirm with the user; wording "I'm stopping here", never "ghosted" or "closed by employer"; reopenable |
| 4 | Follow-up templates the user sends | Singapore career sites already publish them (C, D); fits "JobHub never messages employers" | No evidence follow-up works (C F6); email only, WhatsApp and phone unserved (A F10) | Editable static text; no claims the user did not enter; no promise of results; JobHub never sends or schedules |
| 5 | Closure step feeding the decision record | Nobody closes the loop for the user (B F1, F10); users want a reply of any kind (A F11, C F9); archive states exist (D) | No evidence recording closure helps (C); no tool does it, so untested; FEAT-004 has no real-user evidence | Neutral label ("No reply by [date], I'm moving on"); optional reason; never produce a verdict; editable; no pooling |

## Conflicts between the specialist reports

- **Give-up thresholds disagree:** Indeed 2 weeks (D); Jobstreet 2 weeks after a follow-up (C F3); Teal about 3 weeks (D, snippet); MCF about a month (A F9, C F3, snippet; one summary attributed it to a non-MCF source); JobStreet Malaysia 2 months (D, snippet); MOE: 3 weeks after interview still under consideration (B F5). The lack of agreement is itself the finding.
- **Post-interview follow-up timing:** 3 to 5 days, 5 to 10 business days and 1 to 2 weeks appear on different Jobstreet pages (C F2).
- **Interview silence rates:** 37% (Huntr, A F11) versus 61% (Greenhouse, B F4); different bases, not comparable.
- **Harm of silence:** the experiment that found ghosting no worse than rejection (C F7) sits against surveys naming silence a top frustration (C F8, A F11). They measure different things.
- **Huntr's Pro price** differs between two of its own pages (D); not material to scope.
- **R10 correction check:** run B confirmed the MOM responsiveness-filter statement (14 Oct 2025). A search summary that denied the MCF "typically replies in 30 days" label was not accepted over R10's direct reading.

## Claims not to rely on for a design decision

Search-summary or unverified items flagged by the specialists and the reviewer: the MCF "a month after follow-up" rule; the Teal "3 weeks" and JobStreet Malaysia "2 months" rules; the MOE "6 weeks, assume unsuccessful" line; the Robert Walters 88% figure (sample unconfirmed, percentages sum to 101); the Resume Genius 86% employer figure (no method); the 25.4-day interview figure; the Dev.to "day 7 beats day 2" and "3x response" claims; the Indeed 2 to 4 week drop-out figure (second-hand, no sample); the 4% Greenhouse figure (via Axios, not fetched); the MCF status list and "Under Review" wording.

## Gaps (what this round could not establish)

- Singapore days-to-first-reply and drop-off by stage; the MCF label method; whether MOM's responsiveness filter has launched.
- Whether following up changes replies or hires, and whether it ever harms.
- How people actually decide to give up; how often people check; any Singapore self-blame or motivation measure.
- Anything about lower-wage, shift and gig workers, and about WhatsApp, phone or walk-in follow-up.
- Whether SkillsFuture Jobseeker Support requires proof of applications, and in what form (A F8).
- Whether recording "no reply" would be used or valued. All of these need real people; see the [interview and diary guide](interview-and-diary-guide.md).

## Responsible AI review: points for the owner

The review (Responsible AI Reviewer, 2026-11-22) did not decide anything. Its main points:

- **Verdicts by another name.** "Ghosted", "dead", "closed by employer" or "overdue" turn silence into an outcome the employer never gave. Any status JobHub sets itself, or any default give-up rule, risks that. MOE's own statement shows silence is not rejection.
- **False precision and employer risk.** A JobHub-computed wait figure reads as a promise, can be wrong for small, shift and agency employers, and publishing responsiveness about a named employer raises reputational and defamation exposure.
- **Pooling user data is a separate, unresolved question.** Aggregating recorded reply times into an expected wait faces self-selection, no agreed definition of "reply", small cohorts, re-identification, and PDPA questions on anonymisation, purpose and consent. The review frames this as a question for the owner, not a conclusion.
- **The decision record is sensitive.** It holds the user's reasoning; it should not be pooled by default or used to profile the user or rank employers.

## Evidence limits

AI-gathered, desk-only, capped at N2. The Singapore evidence base for behaviour is very thin. Several findings rest on search summaries of pages that could not be fetched, and most numbers come from vendor or recruiter surveys with a possible interest. Nothing here shows what Singapore job seekers actually do.
