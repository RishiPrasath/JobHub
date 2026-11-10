---
id: FEAT-017
title: Initial setup of job preferences
type: feature
scope: candidate
need_level: N0
feasibility_level: T0
result: none
opportunity: [OPP-005]
needs: []
findings: []
riskiest_assumption: ASM-017
decision: null
updated: 2026-11-10
---

# Initial setup of job preferences

Levels are provisional and await owner review. **The field list is a proposal for the owner to confirm.**

## What it does

After the user creates their profile ([FEAT-016](FEAT-016-candidate-profile.md)), a short setup step lets them pick what they are looking for. The choices are mostly taps on options, with little typing. The answers stay private and are used to show why a finding matters to this person. They are not shared with employers.

Origin: owner decision, 2026-11-10, splitting preferences out of the candidate profile. Related: [source idea](source-ideas/03_candidate-profile-and-preferences.md), which says JobHub should explain why a finding matters to the person and should not decide that a job is unsuitable on their behalf.

## Fields captured

Every field is optional, so the setup can be skipped and finished later. "Choice" means the user selects from a fixed list. The option lists are proposals.

| Field | Input | Options or notes |
|---|---|---|
| Target role titles | list of text, up to 10 | Free text with suggestions |
| Seniority | choice | Internship, entry level, junior, mid, senior, lead or manager, director and above |
| Employment type | multi-choice | Full-time, part-time, contract, internship, freelance |
| Work arrangement | multi-choice | Remote, hybrid, on-site (work from office) |
| Preferred locations | list | City or region |
| Maximum commute | number | Minutes each way, if on-site or hybrid |
| Willing to relocate | choice | Yes, no, for the right role |
| Willing to travel | choice | None, occasionally, often |
| Industries of interest | multi-choice | Fixed list |
| Industries to avoid | multi-choice | Same list |
| Company size | multi-choice | Startup, small, mid-size, large |
| Minimum acceptable pay | number and currency, per month or year | Private |
| Notice period or earliest start | choice or date | Immediately, 1 month, 2 months, 3 months or more, or a date |
| Deal-breakers | list of text | Free text, for example "no weekend work" |

## Not included yet

The source idea also describes working-style preferences such as tolerance for overtime or ambiguity, need for structure or training, and management style. No job portal researched captures these, so they are left out until the owner decides they are worth the effort.

## Evidence for

- Preference-first onboarding exists in practice (Welcome to the Jungle asks for role, seniority, location, contract type and a salary floor right after sign-up).
- Indeed, LinkedIn Open to Work and Wellfound all capture target roles, job type, work arrangement and location. Indeed and Welcome to the Jungle keep pay private.
- Indeed also lets users list what they are not interested in, which matches the "avoid" fields above.

## Evidence against

- No user has been asked what they would select. This is N0.
- Portals do not document which preference fields are required or skipped.
- Preferences may feed FEAT-010 (profile comparison), which failed its fixture test (FND-E03-01).

## Open questions for the owner

1. Which of the fields above are essential for a first version, and which can wait?
2. Is the setup shown right after account creation, or offered as a skippable step later?
3. Does the minimum pay field need a currency and period, or can it be a single monthly amount?
4. Should preferences carry importance (must-have, strong preference, nice-to-have), or are they plain choices?

## Research basis

Desk research on 2026-11-10, summarized in [FEAT-016](FEAT-016-candidate-profile.md#research-basis). The raw research notes are not saved in the repository.

## Next test

Riskiest assumption: ASM-017. Have participants complete the setup, time it, and note the options they skip. Then check whether the answers change what they would do with a posting review.
