# App Ideas

## Idea 1

**Name:** Job Posting Capture App

**One-line description:** Capture and structure job postings from URLs or pasted text.

**Who it’s for:** Users who want to collect and organize job postings.

**Problem it solves:** Job postings can be difficult to capture consistently from different websites, especially when browser-based extraction fails.

**How it works:**

1. A user provides a job-posting URL.
2. The app uses a browser to adaptively capture the posting.
3. If URL/browser capture cannot retrieve the posting, the app clearly tells the user.
4. The user can copy and paste the job posting directly into the app as a fallback.
5. AI formats the captured or pasted content and makes sense of its structure and meaning.
6. Additional AI behavior and formatting requirements will be described later.

### AI Analysis

After a job posting is captured, AI should read and analyze it to identify:

- Required and preferred skills
- Basic job details
- Responsibilities and qualifications
- Work arrangement, such as remote, hybrid, or on-site
- Salary or compensation information
- Work culture and stated company values
- Candidate preferences and requirements
- Potential red flags or concerns
- Other useful information that can be inferred from the posting

The app should recognize that many job portals and postings omit important details. It should clearly distinguish between:

- Information explicitly stated in the posting
- Reasonable interpretations or signals detected by AI
- Information that is unavailable or not disclosed

The goal is to help the user understand what can actually be learned from each captured job posting without presenting missing information as fact.

### User Profile

Users should be able to create and maintain a personal profile containing:

- Skills and areas of expertise
- Search or job-search preferences
- Education and qualifications
- Work experience and other relevant background
- Preferred salary range
- Preferred work arrangements, such as remote, hybrid, or on-site
- Personal preferences about roles, companies, industries, and working conditions
- Personal red flags and deal-breakers
- Other details that help evaluate whether a job is a good fit

Users should be able to update these details over time. The profile can later be compared with the information extracted from each job posting.

### Candidate-to-Job Fit Analysis

The app should compare the user’s profile with each captured job posting and generate a clear analysis, including:

- **Strengths:** Where the candidate aligns well with the role
- **Weaknesses:** Areas where the candidate may be less competitive
- **Opportunities:** Skills, experiences, or qualifications the candidate could develop or emphasize
- **Threats:** Potential concerns, risks, deal-breakers, or competing requirements
- What suits the candidate about the role
- The most important gaps between the candidate and the job requirements
- Which gaps are essential versus trainable or less important
- How the candidate could position themselves in an application or interview
- Which existing skills, experiences, or achievements should be highlighted

The analysis should explain its reasoning and distinguish between evidence from the job posting, information from the user profile, and AI-generated interpretation.

### Job-Market Context

The app should account for the broader job market when evaluating opportunities, especially in Singapore and the United States. It should reflect research into how competitive and difficult the market is, while recognizing that conditions vary by:

- Country and location
- Industry and role type
- Seniority level
- Skills and qualifications
- Hiring cycle and current market conditions

Market context should help the user interpret their chances and make practical decisions, but it should be presented as contextual evidence rather than a guaranteed prediction. The research and its sources should be kept current and clearly identified.

The long-term vision is to support job markets worldwide. For the first iteration, the initial market slice should focus on Singapore, with the architecture designed so additional countries—such as the United States—can be added later.

### Job Application Tracking

The app should save the original job-posting URL or link so the user can return to it and apply. Users should be able to mark a job as applied and maintain a list of job applications.

The application list should eventually support details such as:

- Job title and company
- Original posting URL
- Date saved and date applied
- Application status
- Notes and follow-up actions
- Relevant fit analysis and job-posting details

Users should be able to refer back to a clear overview of the jobs they have applied to, including their current statuses and key details. They should be able to review, search, filter, and update this application history as it changes.

### Cross-Industry Support

The application should be flexible across industries and sectors, not limited to IT, software engineering, or AI. It should be designed to help people navigating difficult job markets across many types of work.

The product should:

- Support profiles for different sectors, occupations, and career paths
- Group jobs into useful industry and sector categories
- Accommodate sector-specific skills, qualifications, terminology, requirements, and career paths
- Recognize both technical and non-technical experience
- Adapt its fit analysis, skills-gap assessment, and positioning advice to the relevant sector
- Avoid assuming that technology-sector criteria apply to every candidate or job
- Allow new sectors and custom categories to be added over time

Potential sector groups should be researched and designed thoughtfully, with appropriate fields and analysis for each group while preserving a common core profile and application-tracking experience.

### Company Research and Red-Flag Detection

AI should be able to research the hiring company and combine that research with the captured job posting. The analysis should look for:

- Company background, industry, size, location, and reputation
- Publicly available information relevant to the role and workplace
- Repeated patterns in job postings or employee-facing information
- Potential concerns involving compensation, workload, management, turnover, stability, or hiring practices
- Wording and techniques that may signal risks or obscure important conditions
- Phrases such as “fast-paced environment” and other coded or vague language that may warrant closer examination
- Missing details that a candidate should ask about before applying or accepting an offer

The app should not treat a phrase or a negative review as proof of misconduct. It should explain why something may be a concern, show the supporting evidence and source, distinguish facts from signals and speculation, and recommend questions the user can ask.

This feature will require extensive research into reliable sources, job-posting language, company research methods, sector-specific red flags, and suitable AI agents or analysis techniques. Research findings should inform the design of the appropriate agents, workflows, and safeguards.

### Technical Direction

The project should be used as an opportunity to explore modern technologies and choose a strong, practical stack that is enjoyable to learn and suitable for a real application.

Technology decisions should prioritize:

- Good software-engineering practices
- Clear architecture and maintainable code
- Strong testing and documentation
- Security, privacy, and responsible handling of user data
- Useful AI integration without making the system opaque or unreliable
- A development workflow that supports learning and gradual improvement
- Sensible choices for the first iteration while leaving room to scale

The stack should be selected deliberately, with the trade-offs documented so the project builds both a useful product and a solid foundation in software engineering.

### Competitive Landscape and Naming

Initial web research shows several adjacent categories:

- **Job tracking and search workspaces:** Teal and Huntr focus on saving jobs, organizing application stages, resumes, documents, contacts, and follow-ups.
- **AI job-search and application automation:** Simplify and JobCopilot emphasize matching, resume customization, autofill, and/or high-volume applications.
- **Singapore career coaching and job matching:** NTUC AI Career Coach and Career Kaki provide AI-guided career support and job-search help tailored to Singapore.
- **Job insight platforms:** Cake presents job insights, company information, salary information, and fit-oriented guidance.

The product should avoid sounding like another generic auto-apply tool. Its distinctive position is a job-posting intelligence and decision-support system that:

- Reads and structures postings
- Investigates companies and market context
- Detects signals, omissions, and possible red flags carefully
- Compares the role with the user’s profile
- Explains strengths, gaps, suitability, and positioning
- Helps the user track the application afterward

Potential names researched at a preliminary web-search level:

1. **RoleUnfold** — suggests revealing what is underneath a job posting.
2. **RoleMosaic** — reflects the combination of skills, preferences, market signals, and company information.
3. **RoleThread** — suggests connecting scattered details into one understandable story.
4. **ApplyLens** — communicates a lens for examining an opportunity before applying.
5. **JobUnfold** — direct and easy to understand, but less distinctive than RoleUnfold.
6. **FitWeave** — emphasizes weaving together the candidate and the opportunity.

The strongest current candidates are **RoleUnfold**, **RoleMosaic**, and **RoleThread**. This is only preliminary name research, not trademark, company-name, domain, app-store, or social-handle clearance. Any finalist must go through those checks before adoption.

### Revised Naming Direction: The Job Seeker's Reality

The name should reflect the emotional reality of searching in a brutal job market: uncertainty, silence after applying, rejection, confusing requirements, hidden expectations, and the exhaustion of making important decisions with incomplete information. It should feel human and honest, not like an automation bot or a corporate recruiting platform.

New directions to explore:

- **The Job Beneath** — the reality underneath the polished listing
- **Role Unmasked** — revealing what a posting may not say directly
- **Read Between Roles** — understanding signals, omissions, and fit
- **The Better Bet** — helping the seeker decide where effort is worth spending
- **Worth the Reach** — deciding whether an opportunity deserves an application
- **Seen in the Noise** — reflecting the desire to be understood beyond a CV
- **The Next Try** — acknowledging persistence without pretending the search is easy
- **No More Guessing** — promising clarity in a confusing process
- **A Fairer Search** — expressing the product’s purpose for people facing an uneven market

The strongest emotional directions are currently **The Job Beneath**, **Read Between Roles**, and **A Fairer Search**. Preliminary searches surfaced existing use of names such as Roleward, WorthApply, and RoleTruth, so those should not be used. The remaining ideas still require full trademark, company, domain, app-store, and social-handle checks.

Research references:

- [Teal job tracker](https://www.tealhq.com/tools/job-tracker)
- [Huntr job tracker](https://huntr.co/product/job-tracker)
- [Simplify](https://simplify.jobs)
- [JobCopilot](https://www.jobcopilot.com)
- [NTUC AI Career Coach](https://aicareercoach.ntuc.org.sg)
- [Career Kaki](https://careerkaki.gov.sg)
- [Cake job insights](https://www.cake.me)

**Must-have features:**

- 

**Nice-to-have features:**

- 

**Questions / risks:**

- 

**Next steps:**

- Describe the desired AI formatting and interpretation in more detail.
- Define what information should be extracted from each job posting.
- Decide how captured postings should be stored and organized.

## Scratch Notes

- 

### One-Word Naming Direction

The name should be short, easy to pronounce, and emotionally connected to the job seeker’s reality. New one-word candidates:

- **Vettly** — vet the opportunity before investing time in it
- **Sifta** — sift through noise, requirements, and hidden signals
- **Fitora** — a warmer, brandable take on fit and direction
- **Mettle** — resilience through a difficult search
- **Footing** — helping the user regain confidence and stability
- **Unveil** — revealing what the job posting does not say plainly
- **Sift** — direct, memorable, and aligned with the product’s core action

The strongest current candidates are **Vettly**, **Sift**, and **Footing**. **Vettly** is now on the official shortlist. A preliminary search found existing use of Roleo, Lentra, Jobra, and TruEra, so those types of collisions must be screened out. These candidates are not legally or commercially cleared yet.

### Research Round: Hunt, Tune, Prepare

Further research shows that the adjacent market is converging around an end-to-end workflow: finding jobs, matching them to a profile, tailoring a CV, tracking applications, and preparing for interviews. Examples include JobMatch, Jobflow, JobTailor, Applique, and Singapore-focused Career Kaki. [JobMatch](https://usejobmatch.com/) explicitly combines search, resume tailoring, interview preparation, and coaching; [Jobflow](https://www.myjobflow.com/) emphasizes fit explanations and authentic tailoring; [JobTailor](https://www.jobtailor.app/) connects ATS analysis, truthful CV changes, interview questions, and tracking; and [Career Kaki](https://careerkaki.gov.sg/) provides Singapore-focused job search, resume preparation, and interview guidance.

This reinforces a product position based on an **informed job hunt**: help the user decide what to pursue, tune their CV from their real evidence, and prepare for the specific company and role. The product should help the user become more prepared and more truthful, not simply generate more applications.

Names screened out during this round because they already appear in the relevant space include RoleBrief, Scoutly, Prepwise, Prepora, Applyra, Tailora, Vettora, and Siftora. Examples: [RoleBrief](https://rolebrief.co/), [Scoutly](https://www.jobscoutly.tech/), [Prepora](https://prepora.ai/), [Applyra](https://www.applyra.fr/), [Tailora](https://tailora.se/), [Vettora](https://vettora.ai/), and [Siftora](https://www.siftora.com/).

One-word naming directions to keep exploring:

- **Vettly** — vet the role, company, fit, and application before committing
- **Mettle** — resilience and confidence in a difficult search
- **Sift** — reduce noise and find the roles worth pursuing
- **Gauge** — understand fit, gaps, readiness, and risk
- **Brief** — receive a clear, informed brief before applying or interviewing
- **Steady** — bring structure and calm to a chaotic search

The official shortlist now includes:

1. **Vettly**
2. **Sift**
3. **Mettle**

These names are still exploratory and require trademark, company, domain, app-store, and social-handle checks.

### Job-Hunt Naming Pass

The next naming direction should feel like the act of hunting for work: searching through noise, pursuing a better opportunity, finding a route forward, and staying in motion despite rejection.

New exploratory one-word directions:

- **Pursua** — a coined form inspired by pursuing the next opportunity
- **Rove** — searching broadly until the right direction appears
- **Trek** — the difficult journey toward the next role
- **Trail** — following leads and building a path forward
- **Rally** — regaining energy and support during the search
- **Nudge** — small, informed next actions that keep the search moving
- **Morrow** — a more hopeful name focused on the next day and next chapter
- **Waymark** — signals and markers that help the user navigate the search

Research shows that names such as Huntly, Seekr, Pathly, Questly, and Scoutly already have job-search or career products associated with them, so they should be avoided. [Huntly](https://huntlylabs.com/) combines job discovery, CV tailoring, mock interviews, and salary data; [Seekr](https://seekrjobs.com/) combines job matching, CV tailoring, salary insights, and interview preparation; and [Pathly](https://pathly.com/) provides AI career guidance and career matching.

The official shortlist remains **Vettly**, **Sift**, and **Mettle**. The new job-hunt directions are exploratory candidates only.

### Naming Reset: Clearer, Less Cringe, More Job-Relevant

The previous naming direction leaned too hard into abstract brand names. A better rule for this product is: use a short, pronounceable, easy-to-spell name that gives a job seeker an immediate clue about the product. Naming guidance consistently favors memorability, meaning, distinctiveness, and ease of pronunciation; descriptive or indirectly descriptive names are acceptable when they are still distinctive. See [Better Launch's naming guidance](https://www.betterlaunch.co/blog/how-to-name-a-startup), [Amazon's Brand Naming Guide](https://m.media-amazon.com/images/G/01/bx-marketing/Brand_Naming_Guide_2025.pdf), and [TIME's product-naming rules](https://time.com/3517142/rules-naming-product/).

The competitive scan also shows that literal names in this category are crowded. Products already using close territory include [JobPrep](https://jobprep.tech/), [JobLens](https://www.usejoblens.com/), [JobBrief](https://www.jobbrief.co/), [RoleReader](https://www.rolereader.com/), [RoleCheck](https://www.rolecheck.app/support), [RoleGuide](https://roleguide.in/), [RolePrep](https://apps.apple.com/tr/app/roleprep/id6744122444), and [ApplyReady](https://www.applyreadyai.com/en/jobs/). These are useful market signals, but they should not be copied.

New, clearer one-word candidates:

- **JobReader** — the app reads the posting, explains what it really asks for, identifies gaps and signals, then helps tune the application. Most directly connected to the product's differentiator.
- **JobGuide** — broad and immediately understandable; positions the app as a guide from discovery through application and interview. It is clear but likely too generic for final use.
- **JobPlan** — emphasizes turning a posting into a practical application and preparation plan. Clear, but less distinctive.
- **ApplyPlan** — makes the application workflow obvious: assess, tailor, prepare, apply, and track. Strong for the execution side, weaker for job discovery.
- **RoleView** — suggests a clearer view of the role, company, fit, risks, and expectations. Simple and more sector-neutral, though it may be less immediately obvious than a name containing “job.”
- **RoleMap** — communicates mapping the user's evidence and skills to a role, including strengths, gaps, and positioning. Simple, but slightly more analytical.

The strongest new candidates are **JobReader**, **JobGuide**, and **RoleView**. My current recommendation is **JobReader** because it sounds like a useful action rather than a promise: the user brings a job posting, and the app helps them understand it before investing time in an application. These candidates are not legally, commercially, domain, or app-store cleared yet.

### Naming Direction: The Helpful Job-Search Assistant

The product should feel like a calm, capable person on the user's side: someone who reads the posting carefully, explains whether the role is actually a fit, points out gaps and warning signs, helps position the user's real experience, and prepares them for the interview. The emotional promise is **"you don't have to figure this job out alone."**

The obvious assistant-style names are already crowded. **JobMate**, **ApplyMate**, **JobPal**, **JobAlly**, **CareerAlly**, **RoleBuddy**, **JobPartner**, and **RoleAid** all have current products or services in the relevant space. In particular, [RoleAid](https://roleaid.com/) is very close to the intended product concept, while [JobMate](https://joinjobmate.com/), [JobAlly](https://www.jobally.fr/en), and [JobPartner](https://jobpartner.com/) confirm that “mate,” “ally,” and “partner” are heavily used naming patterns.

New exploratory names for this direction:

- **FitGuide** — a guide who helps the user decide whether a role fits before helping them prepare for it.
- **ApplyGuide** — makes the assistant role clear across assessment, CV tailoring, application, and interview preparation.
- **JobReader** — the assistant reads the posting and translates it into a clear fit and preparation plan.
- **RoleCoach** — a role-specific coach for gaps, positioning, and interview practice; friendly but more coaching-oriented.
- **JobCounsel** — emphasizes thoughtful advice and informed decisions; credible, but more formal.
- **RoleView** — gives the user a clear view of the role, company, fit, risks, and preparation needs.

The strongest conceptual fit is **FitGuide**. It captures the most important promise: helping someone understand whether a job is right for them and what to do next. **JobReader** remains the clearest functional option, while **ApplyGuide** is the clearest end-to-end workflow option. These are exploratory only and still require full trademark, domain, app-store, and social-handle checks.

### Naming Direction: Application and Interview Preparation

The naming emphasis is now narrower: the product helps the user decide how to apply, build a truthful role-specific application, understand the story they should tell, and rehearse for the interview. It is not merely a job board or a generic career chatbot.

The most obvious names in this territory are already crowded. **ApplyBrief** is an active application product, **PrepBrief** creates company and role-specific interview briefs, and **ApplyWise** combines job-posting analysis, CV tailoring, tracking, and interview preparation. See [ApplyBrief](https://www.applybrief.com/), [PrepBrief](https://prepbrief.io/), and [ApplyWise](https://www.applywisehq.com/).

New exploratory candidates:

- **ApplyCraft** — carefully craft the application and the interview story for the specific role.
- **ApplyPlan** — turn the job posting into a clear application and interview plan.
- **RoleCraft** — shape the user's real experience around the role without inventing anything.
- **StoryPrep** — prepare the candidate's evidence, talking points, and interview answers.
- **PitchPrep** — help the candidate present their value clearly in the application and interview.
- **ApplyCoach** — a straightforward assistant that guides the user through applying and preparing.
- **AnswerKit** — a practical kit of tailored application answers, talking points, and interview questions.
- **RoleBrief** — a concise brief for applying and interviewing; likely too close to existing names and should remain low priority.

The strongest direction from this round is **ApplyCraft**. It feels active and helpful, clearly relates to making an application, and can naturally extend to crafting the candidate's interview story. **ApplyPlan** is the plainest and easiest to understand. **StoryPrep** is the warmest option, but it puts more emphasis on interviews than job applications. These remain exploratory and require proper trademark, domain, app-store, and handle checks.

### Naming Direction: Job + Help / Guidance

The naming constraint is now explicit: retain **Job** as the first word and pair it with something that communicates aid, support, advice, or direction. The most obvious combinations are already crowded: **JobAssist**, **JobGuide**, **JobMentor**, **JobHelper**, **JobSage**, **JobCare**, and **JobCompass** all have current products, services, or platforms associated with job search, applications, career advice, or interview preparation. Examples include [JobAssist](https://jobassist.com/), [JobMentor](https://dinkin.ru/jobmentor/podgotovka-k-sobesedovaniyu), [JobHelper](https://www.jobhelper.cc/), [JobSage](https://jobsage.co/), and [JobCompassAI](https://jobcompassai.com/).

Less obvious exploratory options:

- **JobLift** — helps lift the quality and confidence of an application.
- **JobBeacon** — provides a signal and direction through a confusing search.
- **JobBridge** — bridges the gap between a job posting, a strong application, and interview readiness.
- **JobNorth** — gives the user a clear direction before applying.
- **JobSupport** — extremely plain and trustworthy, though generic.
- **JobHand** — inspired by “a helping hand”; simple, but needs careful cultural and trademark checks.

The best semantic fit from this round is **JobBridge** because the product bridges several difficult steps: understanding the role, preparing the application, and getting ready for the interview. **JobLift** is warmer and more encouraging. **JobBeacon** is the clearest guidance metaphor. All remain exploratory and are not availability-cleared.

### More Job + Support Names

Another search ruled out **JobPath**, **JobSignal**, and **JobWing**, which are already associated with job-search, application, or interview products. [JobPath](https://jobpath.world/en), [JobSignal](https://jobsignal.tech/), and [JobWing](https://jobwing.co/) should therefore stay out of the shortlist.

Additional exploratory candidates:

- **JobCue** — gives the user the right cue for the application and the interview.
- **JobStep** — helps the user take the next practical step.
- **JobNudge** — keeps the user moving through applications, follow-ups, and preparation.
- **JobSteer** — helps steer the search and application in the right direction.
- **JobFrame** — helps frame the user's experience for the role and interview.
- **JobDesk** — feels like a personal desk for applications, notes, and interview preparation.
- **JobFocus** — helps focus effort on roles worth pursuing and preparing for.
- **JobSpring** — suggests support, momentum, and a fresh start; less literal.
- **JobAnchor** — gives stability during a stressful search; already has some job-platform use, so low priority.
- **JobHand** — suggests a helping hand; simple, but has unrelated existing use.

The most promising from this batch are **JobCue**, **JobStep**, and **JobFrame**. **JobCue** is the best fit for the assistant concept because it can help with both what to do and what to say. **JobStep** is the clearest and friendliest. **JobFrame** best expresses tailoring a truthful application and interview story to a specific role.

### JobDesk: Always-Available Job Application Workspace

The user responded positively to **JobDesk**, and the desired meaning is now clearer: a personal, always-available place where the user can bring in a job posting, understand the fit, prepare the application, rehearse for the interview, and return whenever needed.

The name does not need to literally say “anytime.” **Desk** already implies a dependable home base and workspace. The accessibility promise can come through the product language:

- **JobDesk** — Your job application desk, whenever you need it.
- **JobDesk** — Understand the role. Prepare the application. Walk in ready.
- **JobDesk** — Your personal workspace for better applications and interviews.
- **JobDesk** — A clearer way to apply and prepare.

Related alternatives were screened but are less suitable: **JobDock** is already an application tracker and AI application copilot ([JobDock](https://www.jobdock.app/), [JobDock Pro](https://jobdock.pro/)); **JobTap** is already an AI interview assistant ([JobTap](https://www.jobtap.app/)); and **JobPocket** has an existing job-search browser-extension project. This strengthens the case for keeping **JobDesk** rather than forcing a more literal but crowded name.

Current naming recommendation: **JobDesk**. The brand should position it as an always-available personal job-search desk, with a warm assistant inside it.

### JobDesk-Like Alternatives: Personal Job Workspace

The user clarified that they want other names similar to **JobDesk**: a simple, accessible home base for job applications, CV preparation, and interview practice.

Closest alternatives:

- **JobBase** — your home base for every application and interview; probably the closest semantic alternative to JobDesk.
- **JobStudio** — a place to build, refine, and practise; stronger for CV and interview preparation.
- **JobHub** — one central place for postings, applications, research, and preparation; clear but generic.
- **JobCorner** — a personal, approachable place to work on the job search; warmer, but less powerful.
- **JobSpace** — a personal space for the whole job-search workflow; already used by JobSpace AI, which combines CV, application, and interview tools ([JobSpace AI](https://jobspaceai.com/)).
- **JobOffice** — an always-available personal office for applications; clear, but somewhat formal.
- **JobNest** — a supportive home base; friendly, but less immediately professional.
- **JobSuite** — a complete set of tools for applying and preparing; more software-like.
- **JobRoom** — a dedicated room for applications and interviews; simple, but already has employment-platform associations.

The strongest alternatives to **JobDesk** are **JobBase**, **JobStudio**, and **JobHub**. **JobBase** is the clearest “always-accessible home base.” **JobStudio** best captures creating applications and practising interviews. **JobHub** best communicates that all tools live in one place. **JobStation** was not retained because it is already used by a Singapore recruitment agency ([Jobstation Singapore](https://jobstation.com.sg/job-application/)).

### JobHub vs JobDesk: Job-Seeker Panel Research

The final two contenders are **JobHub** and **JobDesk**. Native web research identified several relevant job-seeker groups for the comparison: fresh graduates, mid-career switchers, retrenched or mature workers, people returning after career breaks, international candidates, non-degree/service/trades workers, and professionals in different sectors. Singapore career-support resources specifically discuss fresh graduates, mid-career professionals, career switchers, retrenched workers, mature workers, and returners, with recurring needs around job matching, customised resumes, and interview preparation. See [SkillsFuture Singapore](https://www.myskillsfuture.gov.sg/content/portal/en/career-resources/career-resources/education-career-personal-development/How-to-maximise-your-job-search-and-interview.html), [Singapore mid-career support](https://www.togetherforbetter.gov.sg/lifestage/midcareerworkers/), and [SkillsFuture career transition support](https://www.skillsfuture.gov.sg/initiatives/individuals).

The first five simulated job-seeker agents returned these views:

- **Fresh graduate in tech/business analytics:** preferred **JobDesk**; it sounds like a practical workspace for applications and interview preparation. Suggested CareerDesk, RoleDesk, and ApplyDesk.
- **Mid-career industry/function switcher:** preferred **JobHub**; it feels broader and more supportive for skills mapping, gap planning, and career transition. Suggested CareerBridge, PivotPath, and NextRole.
- **Retrenched or returning professional:** preferred **JobHub**; it feels more welcoming and confidence-building than an administrative desk. Suggested CareerBridge, ReturnReady, and NextChapter.
- **Non-degree/service/trades worker:** preferred **JobHub**; it feels more inclusive across retail, hospitality, logistics, facilities, and trades. Suggested JobGuide, WorkReady, and JobHelper.
- **International or relocating job seeker:** preferred **JobHub**; it sounds like a central place for jobs, salary, relocation, work-authorisation, and cultural guidance. Suggested CareerBridge, WorkWay, and GlobalPath.

The early panel leans **JobHub** for emotional accessibility and breadth, while **JobDesk** is stronger for users who think of the product as a focused application and interview workspace. The main trade-off is:

| Name | What it communicates best | Main risk |
| --- | --- | --- |
| **JobHub** | One welcoming centre for jobs, applications, research, and support | Sounds like a job board or generic marketplace |
| **JobDesk** | A practical personal workspace for applications and preparation | Sounds administrative, recruiter-facing, or office-oriented |

Important availability warning: **JobHub** is already used by multiple employment platforms, including [GetJobHub](https://www.getjobhub.com/) and [Jobhub Malaysia](https://jobhub.center/home). **jobdesk®** is an established Swiss recruiting platform with a mobile app and recruitment software ([jobdesk.com](https://www.jobdesk.com/en), [Google Play](https://play.google.com/store/apps/details?hl=en&id=com.jobdesk.jd)). The panel preference is therefore a product-positioning signal, not a clearance result.

Provisional naming conclusion: **JobHub** is the stronger user-facing feeling; **JobDesk** is the stronger workflow description. If the product is meant to feel like a supportive destination for all kinds of job seekers, JobHub currently wins. If it is meant to feel like a private, role-by-role application preparation workspace, JobDesk currently wins. Both require a serious trademark, domain, app-store, and market-confusion check before commitment.

### Product Name Locked In

The chosen working name for the application is:

# JobHub

JobHub is the selected product name for the current app concept: an accessible, supportive workspace that helps job seekers understand job postings, assess fit, tailor applications, track progress, and prepare for interviews.

This is a product decision, not legal or commercial clearance. Trademark, domain, app-store, and market-confusion checks remain required before public launch.
