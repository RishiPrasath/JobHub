# Round 07 synthesis — Competitive landscape

Research date: 2026-10-28

## Executive summary

The competitive market is not one thing called “AI job search.” It is a set of connected workflows:

1. Job discovery and recommendations.
2. Resume-to-job comparison and tailoring.
3. Application tracking and follow-up.
4. Application autofill.
5. Autonomous application submission.

Most products use a combination of resume/profile data, explicit preferences and behavioural signals. Most expose a keyword, skills, ATS or fit score. Public evidence does not establish that these scores predict interview or hiring outcomes.

The clearest competitive boundary is user control over external action:

```text
Recommend → draft → autofill → user reviews → user submits → system submits
```

The market is strongest at generating documents and speeding up repetitive workflows. It is weaker at preserving evidence, explaining uncertainty, representing cross-industry context, verifying employer/role information and supporting Singapore-specific job seekers.

## How competitors capture profiles

Common profile inputs:

- Resume upload or paste
- LinkedIn import
- Manual experience and education entry
- Skills, licences and certifications
- Target roles and industries
- Location and commute preferences
- Work arrangement and schedule preferences
- Salary expectations
- Work authorisation
- Application answers and reusable documents
- Search, save, click, dismiss and application behaviour
- In some cases, recruiter response or application outcome signals

The strongest reusable-profile pattern appears in Simplify: one profile supports matching, tailored documents, application answers, autofill and tracking. The strongest structured tracker pattern appears in Teal and Huntr. LinkedIn adds a professional network and recruiter graph that is difficult to reproduce.

## How matching generally works

The documented matching process is usually:

```text
Candidate profile/resume
    + job description
    + preferences
    + behaviour
    + sometimes network or recruiter signals
        ↓
Keyword, skill, title, location, salary or ATS-style comparison
        ↓
Recommendation, score, missing-keyword list or tailored content
```

MyCareersFuture is the clearest local example of a profile-to-job skills comparison. Indeed documents a broad preference and behaviour loop. LinkedIn adds network and recruiter-response signals. Teal, Jobscan, Rezi and similar products mainly compare a chosen resume with a specific posting.

This is useful for prioritisation, but it does not answer all of the questions a job seeker may care about:

- Is the employer legitimate or actively hiring?
- Are the duties clear?
- Does the work suit the person’s preferences?
- Are the role conditions acceptable?
- Are the missing details important?
- Is the score based on actual capability or only terminology overlap?

## Pricing patterns

### Free-first job boards

LinkedIn, Indeed, MyCareersFuture and Jobstreet make core job discovery available without a clearly documented candidate subscription in the reviewed sources. They monetise employer access, sponsored listings, recruiter tools, premium visibility or premium candidate insights.

### Paid resume and application tools

Observed public prices ranged approximately from:

- US$13–29 for shorter Teal periods or monthly access;
- US$23.99–44.99/month for Careerflow tiers shown on public pages;
- US$24–96 for Kickresume billing periods;
- US$29/month or US$149 lifetime for Rezi;
- US$40/month for Huntr Pro;
- approximately US$49.95/month for Jobscan based on official published content, with checkout unverified;
- US$39.99/month for Simplify+;
- unclear consumer pricing for Jobright and Sonara.

Prices are not directly comparable because limits, billing cadence, geography, promotions and included automation differ.

### What users are actually paying for

The paid boundary commonly covers:

- more AI generations;
- full keyword or match visibility;
- more tailored resumes and cover letters;
- interview practice;
- networking or recruiter tools;
- higher tracker limits;
- autofill and application automation;
- access to premium insights or outreach.

## Competitor strengths

- LinkedIn: professional identity, network and recruiter discovery.
- Indeed: broad distribution, resume parsing and behavioural recommendations.
- MyCareersFuture: Singapore-specific eligibility, salary and skills context.
- Jobstreet: regional profile schema, credential verification and visibility controls.
- Teal: transparent, human-controlled job/resume tracker.
- Huntr: strong job, document, contact and follow-up linkage.
- Jobscan: focused job-specific ATS comparison.
- Rezi: resume versioning and interview practice.
- Simplify: reusable profile plus the clearest Copilot/Autopilot distinction.
- Sonara: maximum apparent search and application automation.
- Careerflow: broad profile, LinkedIn, networking, tracker and interview toolkit.
- Kickresume: polished document and presentation workflow.

## Competitor weaknesses and trade-offs

### Scores can create false confidence

ATS, keyword and fit scores are easy to understand but can reward terminology matching instead of capability, context or truthful evidence. No independent study in this round validated the vendors’ outcome claims.

### External application handoffs break continuity

When a product redirects to an employer ATS, it may lose confirmation, status, exact submitted fields and later outcome evidence.

### Automation increases factual and control risk

Automatic applications can use stale answers, duplicate applications, incorrect eligibility details or generic documents. Sonara and Jobright publicly suggest high automation, while Simplify explicitly separates reviewed Copilot from no-review Autopilot.

### Profile visibility is not the same as user control

Searchable profiles may be copied by employers or third parties. Recruiter matching may expose profile information even when the user has not separately applied. Data deletion may not remove earlier copies.

### Regional support is uneven

Several AI-first products are explicitly U.S.-focused or do not publicly establish Singapore coverage. This creates a practical opening for a Singapore-first product, but it must be validated rather than assumed.

### Pricing is difficult to compare

Some prices are weekly, some monthly, some quarterly, some promotional and some only visible at checkout. Jobright and Sonara did not expose a clear consumer price in the reviewed public sources.

## What JobHub should learn

These are research implications, not final scope decisions:

1. Treat the candidate profile as a versioned evidence object, separate from the resume and separate from the user’s preferences.
2. Show the source and confidence behind every important profile fact and job comparison.
3. Keep document/keyword alignment separate from candidate fit, eligibility, employer research, compensation and unknowns.
4. Store the original job posting, generated output, user edits and exact submitted materials separately.
5. Make review-before-submit the default for any future automation.
6. Make user preferences explicit, prioritised and editable instead of inferring a permanent career identity.
7. Preserve the job’s source, capture status and application route so external ATS gaps are visible.
8. Focus differentiation on evidence, correction, context and local relevance rather than generic AI resume writing.
9. Make privacy state visible: private profile, recruiter discovery, submitted resume, external sharing and AI processing should not be one setting.
10. Do not copy competitors’ match scores without a human-reviewed test showing that they help users make better decisions.

## Recommended next validation

Run a controlled comparison using the same three synthetic cases:

- Singapore graduate or career changer;
- Singapore service/operations worker;
- technical professional applying across adjacent roles.

Measure:

- profile extraction completeness and correction time;
- match explanation quality;
- false-positive and false-negative examples;
- factuality of tailored resumes and application answers;
- export/re-import fidelity;
- application-state accuracy versus actual confirmation;
- user-selected versus automatic submission;
- data visibility, deletion and portability paths;
- whether the output helps the user identify meaningful unknowns and red flags.

This validation is more valuable than comparing feature counts.
