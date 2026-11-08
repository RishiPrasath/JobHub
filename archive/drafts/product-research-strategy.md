# Research Strategy

## Your Research Ideas

### Product and User Research

- How people currently save, understand, compare, and apply to jobs
- The needs of different job seekers, including:
  - Fresh graduates
  - Mid-career switchers
  - Retrenched or mature workers
  - People returning after career breaks
  - International candidates
  - Non-degree, service, trades, and operational workers
- What information users want from job-posting analysis
- How users define a good fit between themselves and a role
- What users consider useful or harmful career advice
- How users want to track applications and follow-ups
- How users prepare CVs and interviews for specific roles

### Job-Posting and AI Analysis

- Reliable ways to capture postings from URLs
- Browser-based extraction versus copy-and-paste fallback
- How to structure inconsistent job-posting content
- Which job-posting fields can be extracted reliably
- How to distinguish:
  - Facts explicitly stated
  - Reasonable interpretations
  - AI-generated signals
  - Missing or undisclosed information
- How AI should identify skills, responsibilities, qualifications, work arrangements, salary, culture, and requirements
- How to explain AI reasoning without presenting uncertain conclusions as facts

### Candidate-to-Job Matching

- How to represent a user’s skills, preferences, education, experience, and constraints
- How to compare a candidate profile with a job posting
- How to classify strengths, weaknesses, opportunities, and threats
- How to distinguish essential gaps from trainable or minor gaps
- How to help users position themselves truthfully in applications and interviews
- How to avoid unfair or overly simplistic fit scores

### Market and Company Research

- Singapore’s job market and hiring conditions
- How market conditions vary by country, industry, role, seniority, and hiring cycle
- How the system could eventually support the United States and other countries
- Reliable sources for current market information
- How to research companies using public information
- How to assess company background, reputation, size, location, and industry
- How to identify potential red flags in job postings and company information
- How to distinguish a genuine concern from a vague signal, isolated review, or unsupported speculation
- How to cite evidence and recommend questions for candidates to ask

### Cross-Industry Support

- Which sectors and occupations should be supported first
- How sector-specific skills, terminology, qualifications, and career paths differ
- What information can be shared across industries
- What needs to be customizable by sector
- How to avoid applying technology-sector assumptions to every job

### Technical Research

- Which technology stack is appropriate
- How to design a maintainable and extensible architecture
- Which AI models, agents, and workflows are suitable
- How to make AI behavior transparent and testable
- How to handle changing models and evolving requirements
- How to protect personal, career, and application data
- What responsible AI, security, privacy, and data-retention practices are needed
- What development workflow best supports learning and gradual improvement

### Product Surface and Cross-Device Workflow

Research how JobHub should support the journey from discovering a job to preparing an application, without deciding the product surface or technology stack in advance.

- Where users discover job postings
- Where users prefer to perform serious job preparation
- How quickly users need to capture an interesting posting
- How users preserve a posting and its context for later
- How users move between phone, tablet, laptop, and desktop
- How context switching and limited available time affect follow-through
- Whether mobile is best suited to capture, review, reminders, or full preparation
- Whether larger screens are necessary for analysis, CV preparation, and interview work
- Whether JobHub should be:
  - A desktop-focused web application
  - A responsive web application
  - A mobile-first web application
  - A progressive web app
  - A native mobile application
  - A multi-surface product with different responsibilities on each surface
  - A browser extension or share-sheet capture tool combined with a larger workspace
- The trade-offs between product reach, convenience, capability, development cost, and maintenance complexity
- Accessibility, privacy, security, notifications, offline use, and operating-system capabilities
- Whether the product should begin with one surface and expand later

The central research question is:

> Which product surface or combination of surfaces best fits the real job-seeker workflow, and what should each surface be responsible for?

### AI-Assisted Job Hunting and Automation

Research how people currently use AI to automate or accelerate their job hunt, and what they gain, lose, and struggle with when doing so.

- How job seekers use ChatGPT, Claude, Gemini, and other general-purpose AI tools
- How job seekers use dedicated AI career and application products
- How people automate:
  - Job discovery and filtering
  - Job-posting capture and summarisation
  - Resume and cover-letter tailoring
  - Application-form completion
  - Outreach and networking messages
  - Interview preparation and practice
  - Application tracking and follow-up reminders
- Which parts of the job hunt people genuinely want to automate
- Which parts require personal judgment, reflection, or human control
- The trade-offs between speed, convenience, quality, authenticity, and user effort
- Whether automation increases the number of applications without improving their relevance
- How users verify AI-generated claims, skills, achievements, and application content
- Problems involving inaccurate, generic, exaggerated, or fabricated content
- Difficulties preserving the user’s authentic voice and experience
- Risks of over-optimising applications for applicant-tracking systems
- Risks of spam, duplicate applications, poor employer experiences, and damage to reputation
- Privacy and security risks when uploading resumes, personal information, and job-search history
- Platform terms, employer expectations, and ethical boundaries around automated applications
- Whether users understand what AI tools are doing on their behalf
- Gaps in current tools, including:
  - Weak evidence grounding
  - Poor understanding of the individual candidate
  - Limited company and market context
  - Weak support for uncertainty and missing information
  - Little continuity across job discovery, preparation, application, and follow-up
  - Limited support for non-standard careers and industries
  - Poor cross-device and interrupted-workflow support
  - Insufficient explanation of recommendations and decisions
- Where current tools create more work, anxiety, or confusion instead of reducing it
- What users still need to review, correct, or complete manually after using AI

The central research question is:

> How can JobHub use AI to reduce the burden of a job hunt while preserving relevance, authenticity, user control, privacy, and responsible decision-making?

### Real-World Job-Seeker Practices

Research how ordinary job seekers actually use AI tools in their day-to-day search, including people who are struggling, under time pressure, or unfamiliar with advanced AI workflows.

- How job seekers plan and organise a job search
- How they decide which jobs to pursue and which to ignore
- How they search for jobs across job boards, company sites, professional networks, and referrals
- How they save, revisit, compare, and prioritise opportunities
- How they use AI to understand unfamiliar job descriptions
- How they prompt AI to refine or rewrite resumes
- How they tailor resumes without inventing experience or qualifications
- How they use AI to write, adapt, and review cover letters
- How they use AI to prepare for interviews and predict likely questions
- How they practise answers, explain career gaps, and build confidence
- How they research companies and decide whether a role is worth pursuing
- How they use AI to identify skills gaps and plan learning or career changes
- How they track applications, deadlines, follow-ups, and outcomes
- How they combine AI tools with spreadsheets, notes, browser bookmarks, email, and messaging apps
- What prompts, templates, personal workflows, and informal strategies they develop
- What users do when AI gives an unhelpful, inaccurate, generic, or overly confident answer
- How much time users spend checking, correcting, and personalising AI output
- How practices differ by experience, industry, education, language ability, confidence, and access to technology
- How unemployed, underemployed, retrenched, career-switching, and time-constrained users experience these workflows
- What causes users to abandon an AI-assisted job-search process
- What successful users do differently from users who remain stuck despite using AI
- Whether AI reduces stress and uncertainty or creates additional decision fatigue

The central research question is:

> How do real job seekers use AI to plan, search, prepare, apply, and cope with the difficulties of finding work, and where does that process still break down?

### Market, Competition, and Positioning

- Existing job-search, application-tracking, CV, interview, and career-coaching products
- Where comparable products are strong or weak
- Whether JobHub should focus on job discovery, job intelligence, application preparation, or the complete workflow
- How to avoid becoming another generic auto-apply product
- What unique product position JobHub should occupy

### Naming and Brand Research

- Whether proposed names are distinctive and understandable
- Existing products with similar names
- Trademark, domain, app-store, and social-handle availability
- How different job-seeker groups respond to names such as JobHub and JobDesk
- Whether the chosen name communicates a supportive workspace rather than a job board or recruiter tool

### Main Research Themes

1. Understand the job seeker’s real workflow and difficulties.
2. Make AI analysis evidence-based and responsible.
3. Research companies and identify risks without overclaiming.
4. Support different industries and types of workers fairly.
5. Choose a technically responsible but adaptable architecture.
6. Position JobHub distinctly from existing job-search tools.

## Recommended Research Topics

### Problem Validation and Outcomes

- Whether the core problem is important enough for people to change their current job-search habits
- Which moments in the job-search journey create the greatest loss of time, confidence, or opportunity
- What successful outcomes should mean beyond the number of applications submitted
- How to measure better decisions, better preparation, reduced uncertainty, and improved follow-through
- Which problem should be solved first for the Singapore-focused initial product

### User Segments and Inclusion

- Which user segments have the strongest unmet need and are reachable for research
- How job-search needs differ by employment status, career stage, industry, language, disability, and digital confidence
- How financial pressure, immigration status, caregiving, health, and time constraints affect the workflow
- Which users may be harmed or excluded by automated fit analysis or application advice
- How to recruit representative users without overgeneralising from a small sample

### Job-Posting Capture and Source Reliability

- Which job-posting sources are reliable, current, accessible, and legally usable
- How often postings disappear, change, duplicate, or contain incomplete information
- How browser capture, pasted text, screenshots, email forwarding, and manual entry compare
- How to preserve the original posting, timestamp, URL, and evidence when content changes
- How terms of service, robots rules, copyright, and privacy affect capture and storage

### Evidence, Trust, and Explainability

- What evidence users need before trusting a job analysis or company warning
- How to show source excerpts, missing data, confidence, and uncertainty without overwhelming users
- How users interpret fit scores, rankings, red flags, and AI recommendations
- How to support correction, disagreement, appeal, and user override
- How to prevent users from treating signals or inferences as established facts

### Mobile, Web, and Cross-Device Product Shape

- Where job discovery occurs and where serious preparation occurs
- Whether capture, review, analysis, resume work, interview preparation, and tracking belong on the same surface
- How interruptions and delayed return affect saved jobs and application completion
- Whether a responsive web application, native application, progressive web application, browser capture tool, or multi-surface approach best fits the evidence
- What product surface can deliver useful value with the least long-term complexity

### Candidate Profile and Fit Analysis

- What information users are willing and able to maintain in a personal profile
- How to represent transferable skills, evidence, preferences, constraints, and uncertainty
- Whether users prefer explanations, comparisons, recommendations, or scores
- How to distinguish essential requirements from trainable or negotiable gaps
- How to avoid discriminatory, deterministic, or overly confident suitability judgments

### Company Research and Red-Flag Analysis

- Which public sources are reliable for company research in Singapore and other markets
- How to distinguish company facts, employee experiences, patterns, signals, and allegations
- Which red flags are useful and which create unnecessary fear or false certainty
- How to handle conflicting, outdated, anonymous, or potentially manipulated sources
- What questions users actually want to ask employers after seeing a concern

### AI-Assisted Job Hunting

- Which job-search tasks users genuinely want to automate and which they want to control personally
- How ChatGPT, Claude, Gemini, dedicated career tools, and automation services differ in real workflows
- Whether AI improves relevance and outcomes or mainly increases application volume
- How users verify, edit, and personalise AI-generated resumes, cover letters, and interview answers
- How employers perceive AI-assisted applications and where authenticity or disclosure matters
- How to design for users who cannot afford multiple paid AI tools

### Technical, Privacy, and Operating Constraints

- What personal, career, application, and company data JobHub must store and for how long
- Which data should remain local, be encrypted, or be excluded from model input
- Expected latency, cost, reliability, and scale for capture, research, and AI analysis
- Which functions require live information and which can use stored evidence
- What legal, regulatory, platform, and employment-context constraints apply to the initial market

### Market Position and Sustainability

- Whether JobHub is primarily job intelligence, application preparation, career support, or a combined workspace
- Which competitor gaps are real and durable rather than temporary feature gaps
- Who would pay, what they would pay for, and which value can be delivered without a subscription
- Whether partnerships with career services, training providers, or community organisations are appropriate
- What would make JobHub meaningfully useful before the full vision is built

### Research Operations

- How to maintain a durable research repository without creating documentation overhead
- How internal Job Hunt materials should be combined with external research
- How to version findings as markets, tools, and user behaviour change
- How to record source quality, confidence, contradictions, and revisit dates
- How to decide when research is sufficient and when a prototype or user test is the better next step
