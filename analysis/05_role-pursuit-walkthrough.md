# Role-pursuit walkthrough

Status: evidence review complete — no product feature accepted yet

## The simple question

> Is this job worth more of my time, and what must I verify first?

This is different from asking:

- “Will I get hired?”
- “Is this employer good?”
- “Is this posting definitely fake?”
- “What is my single match score?”

The existing research does not support those stronger conclusions.

## Three postings compared

| Decision area | Class 4 Driver — MyCareersFuture | Vehicle Mechanic — FastJobs | Part-Time Admin Assistant — Jobstreet |
|---|---|---|---|
| Pay shown | $3,800–$4,600 monthly, including overtime/night-related components | S$2,600–$3,000; pay frequency unclear | $12–$15/hour |
| Arrangement | Full-time, long-term; day/night rotation; six days; travel to ports | Full-time; 5.5-day week; Changi | Part-time; 2–3 weekdays; on-site; hours negotiable |
| Requirements | Class 4 licence, experience and additional possible qualifications | Automotive qualification and Class 3/4/5 licence wording | Requirements exist, but exact wording was not preserved |
| Application route | MyCareersFuture; WhatsApp contact visible | Apply, phone and email contact visible | Send resume; details explained at interview |
| Important platform signals | `0% skills matched` | Featured, employer profile, “normally responds within 24 hours” | Posted recently, low application volume, safety warning |
| Important unknowns | Base pay versus total income; overtime calculation; exact duties | Exact hours, benefits, meaning of “Singapore-only,” verification of response badge | URL/title mismatch; exact duties, schedule, pay conditions and application handling |

## What a person needs to know before deciding

The minimum decision record is not a score. It is a structured set of questions:

1. **What is this job?**
   - title, employer, recruiter or agency, source and capture date;
   - whether the page appears complete, partial, changed or blocked.

2. **What would I actually do?**
   - responsibilities, daily tasks, equipment, customers, physical demands and travel.

3. **What are the hard gates?**
   - licences, qualifications, work rights, medical requirements and mandatory experience;
   - separate these from preferred or trainable requirements.

4. **What would the working conditions be?**
   - location, commute, shifts, days, overtime, deployment, on-site/remote status and employment type.

5. **What does the pay really mean?**
   - currency, pay frequency, base pay, allowances, overtime, bonuses and conditional components;
   - preserve the original wording when the breakdown is unclear.

6. **How would I apply?**
   - recipient, documents, screening questions, application route, deadline and response expectations.

7. **What is known, missing or conflicting?**
   - `stated`, `preferred`, `conditional`, `not stated`, `not visible`, `conflicting` and `platform signal` must remain distinct.

8. **What should I verify first?**
   - only questions that could change the decision.

9. **What do I do next?**
   - continue, investigate, save for later, pause or decline — with a short reason.

## What the AI may and may not do

### It may

- extract visible role, employer, pay, conditions and requirements;
- preserve exact source wording and links;
- separate required from preferred information when the wording supports it;
- identify missing or conflicting fields;
- list verification questions;
- compare the posting against user-provided preferences or evidence, with uncertainty visible.

### It may not

- turn a platform match score into a suitability verdict;
- convert total income into base salary;
- infer work rights, nationality, eligibility, salary guarantees or employer quality;
- label a posting a scam, ghost job, unsafe employer or exploitative role from one signal;
- silently resolve a URL/title mismatch;
- merge a related-role salary teaser into the current posting;
- auto-answer sensitive application questions;
- submit or send anything externally.

## The first useful workflow shape

The evidence suggests a simple review sequence:

```text
Posting
  → What is this?
  → What would I do?
  → What are the hard gates?
  → What are the conditions and pay?
  → What is missing or conflicting?
  → What should I verify?
  → Continue / investigate / save / pause / decline
```

This is a workflow hypothesis, not a final feature specification.

## What we learned from the walkthrough

- Job postings contain a mixture of employer content, platform metadata and unexplained signals.
- Qualifiers matter: overtime, allowances, shifts, travel, expiry dates and conditional flexibility can change the decision.
- Missing information is not automatically negative information.
- Platform signals can create false authority: a match score, badge, response indicator or applicant count is not proof of fit or legitimacy.
- A universal “job fit score” would hide the exact reasons a person should continue or investigate.
- The core opportunity is likely structured understanding and verification, not immediate resume generation or auto-application.

## What this does not prove

This walkthrough does not prove:

- that this is the biggest job-search problem;
- that people would use such a workflow;
- that it improves applications or hiring outcomes;
- that the same fields work equally well across all industries;
- that AI is better than a manual worksheet;
- that any employer or posting in the examples is legitimate or illegitimate.

## Next decision

Before building anything, compare two simple versions of this workflow:

1. a manual structured worksheet;
2. an AI-assisted worksheet with every claim linked to source evidence.

The next evaluation should focus on whether the structure preserves truth, exposes uncertainty and helps a person identify the right next question. It should not focus on producing a polished summary.

Source baseline: [Round 4 page inventory](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/page-inventory.md), [Round 4 findings](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/findings.md), and [Round 4 AI trust findings](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-round4-remaining-objectives/ai-assisted-job-seeking-and-trust.md).
