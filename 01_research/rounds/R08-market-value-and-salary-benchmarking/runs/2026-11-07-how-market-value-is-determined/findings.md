# How a person's market value and salary are actually determined

Research report, 2026-11-07. Desk research by six Haiku-model agents, with the lead researcher opening the primary sources behind the main claims. How much each claim can be trusted is marked throughout (see "Confidence labels" at the end). This is research, not advice about any person's pay.

## The short answer

1. **There is no single "market value".** Professionals combine three things: a **benchmark for the job** (what employers pay for a defined job, at a level, in a place), **adjustments for you** (experience, scarce skills, scope of work), and **what a particular employer can and will pay** (their pay band and budget). A credible answer is a **range with a stated basis**, not one number.
2. **Benchmarks are built from pay data, not from skills lists.** Surveys or datasets of pay are matched to jobs by what the job involves (not the title), cleaned, brought to a common date, and summarised as percentiles (25th, median, 75th). Official examples: the US wage survey pools about 1.1 million establishments; Singapore's Ministry of Manpower publishes median, 25th and 75th percentile wages for 500+ occupations.
3. **Skills matter, but less than people expect and unevenly.** In the best large study found, a posting that lists a new skill pays about 3% more on average than one that doesn't (same occupation, industry, place and year); AI-developer skills show above 8% in the US. These are associations in advertised pay, not proof that learning the skill raises your pay.
4. **Education and experience are still the base of the model.** A global review puts the average private return at about 9% per extra year of schooling.
5. **Who you work for matters as much as who you are.** In US data, nearly all the rise in pay inequality came from differences between employers, and larger firms pay about 35% more on average (partly because they hire differently).
6. **Salary data is biased in known ways.** Posted pay is high and rarely shown; self-reported pay is typically understated; crowd-sourced sites match official data reasonably on averages but not on who is in the sample.
7. **So the sound method is to triangulate:** one official or employer-reported anchor, two sources of different types, put on the same basis (base or total, gross or take-home, same date), adjusted for differences in scope, and shown as a range with confidence. A worked example is in section 7.

## 1. How benchmarks are built

| Step | What happens | Evidence |
|---|---|---|
| Collect | Employers report pay for defined jobs (employer-reported surveys); governments run mandatory or sampled surveys; sites collect self-reported pay; vendors scrape advertised pay | Confirmed (see below) |
| Match | Each survey job is matched to a real job by duties and scope, not by title. One vendor treats a match as defensible only if at least 80% of duties align; scope differences are handled by re-matching or an adjustment (Mercer's example: a 10% discount where the survey job carries more responsibility) | Vendor practice, 2 sources |
| Clean | Outliers are flagged by judgment, not a formal test (far from other surveys, tiny samples, implausible values). One example threshold: discard a data line with fewer than 100 observations or 10 companies | Vendor practice, 1 source |
| Age | Data from different dates is moved to one date. Mercer no longer recommends a single factor for all jobs because pay moves differently by job | Vendor practice, 2 sources |
| Adjust | Geographic differentials reflect local labour cost, not cost of living | Vendor practice, 1 source |
| Weight | Data lines can be excluded, up-weighted (an industry-specific survey) or down-weighted. One low-paying employer with many staff can skew an average weighted by staff | Vendor practice, 1 source |
| Summarise | Report percentiles. The median is the usual anchor; the 25th suits entry-level roles and the 75th is a premium for hard-to-fill ones | Vendor practice, 1 source |

**A real official example (US OEWS), confirmed on the BLS method page:** it samples from a frame of about 8.8 million establishments, runs a six-panel, three-year cycle of two panels a year (about 186,000 to 189,000 establishments each), pools six panels (about 1.1 million establishments) for each annual estimate, and weights each by the inverse of its chance of selection. May 2025 response was 66.2%, so one in three sampled establishments did not answer. Non-responders are estimated by a model, and older panels' wages are adjusted forward to the reference date.

**Why published surveys aggregate so heavily:** in the US, competitors exchanging pay data raises antitrust questions, so surveys are run by third parties and aggregated. The Department of Justice withdrew its health-care "safety zone" statements, which covered wage and benefit surveys, on 3 February 2023 (confirmed across several law-firm summaries). The FTC's position and the current status of the 2016 HR guidance were not confirmed. This explains why survey vendors publish minimum-participant rules, but I found no verified current numeric rule, so none is stated here.

**Base, cash, total.** Reports separate base salary (fixed), variable pay (bonus, incentive), total cash (base plus variable) and total compensation (adds equity, benefits). Comparing a "salary" from one source with "total compensation" from another is a common error.

## 2. What determines pay

| Variable | What the evidence says | Strength |
|---|---|---|
| **Job content and level** | Benchmarks are keyed on occupation and level, so this is the first thing that decides which number you look at | Strong (how official surveys work) |
| **Education** | The standard model (Mincer) regresses log pay on years of schooling and experience. A review of 1,120 estimates in 139 countries finds an average private return of about 9% per year of schooling, stable over decades. Studies using natural experiments find returns 20 to 40% above the simple estimate, and twin studies suggest roughly a 10% upward bias from unmeasured ability | Strong for the average; the size varies by country and period |
| **Experience** | Part of the standard model, usually with diminishing returns (the quadratic form is from memory; no source opened gave the shape or per-year figure) | Strong that it matters; size not verified |
| **Employer** | Using US administrative data for 1978 to 2012, nearly all of the rise in earnings dispersion comes from differences in average pay between employers. Large employers pay about 35% more on average, explained partly by higher-quality hires and partly by organisation of work and rent sharing | Strong (primary, agent-read) |
| **Industry** | Matters, but the studies found for this run gave mixed splits between industry and within-industry differences, so no figure is stated | Moderate; unresolved |
| **Location** | Benchmarks apply geographic differentials for local labour cost. No verified size found | Moderate (practice) |
| **Skills** | See section 3. About +3% for any new skill in postings; much larger for a few skill groups | Moderate; associational |
| **Demand and supply for your skills** | Employers say talent supply affects where they pay against the market (more for hard-to-fill roles). No measured effect size found in the sources opened | Weak for size; plausible for direction |
| **Your negotiation** | In a field experiment with about 2,500 job seekers, men negotiated more than women when pay was not stated as negotiable; when negotiability was stated, the gap disappeared. Anchoring: students acting as hiring managers gave higher starting salaries after seeing an extreme first number | Moderate (one large field study; lab evidence from students) |

How much of the variation in pay such models explain was not established: no opened source gave a figure.

## 3. How skills become pay

- **Method.** The IMF's 2026 staff note regresses the log of the advertised hourly wage on whether the posting lists a "new" skill, comparing postings within the same occupation, industry, county and year, controlling for how many skills are listed. Data: Lightcast postings, 2020 to 2024, 54.3 million US and 5.6 million UK. **Confirmed on the page.**
- **Findings.** Any new skill: about +3 to 3.4% in posted wages. Four or more new skills: +15.1% (UK) and +8.5% (US). AI-developer skills: above 8% (US) and about 7.5 to 8% (UK); AI-user skills about 2% (US). The largest premiums are in IT, business and data analysis, and engineering. **Confirmed.**
- **Vendor figures differ because the comparison differs.** Lightcast's press release says postings requiring AI skills advertise salaries about 28% higher, with no method stated. The IMF's within-occupation figures are 2 to 8%. A 28% gap between "postings with AI skills" and "all other postings" mostly compares different jobs. PwC's AI Jobs Barometer was reported by the agent to show a larger premium, but its pages could not be opened, so it is not used here.
- **Limits stated or implied by the sources.** Advertised pay is not paid pay. The sample over-represents professional and technical jobs. The note's language is "associated with", not "causes". Because it controls for the number of skills listed, a skill's premium is not separable from the bundle it comes with. Another finding from the note: workers in some highly exposed occupations see modestly lower wages two to three years after AI skills enter, so premiums may fade.
- **Skills taxonomies do not contain pay.** O*NET records skill importance and level ratings, and the opened ESCO page links skills to occupations as essential or optional; neither carries wages (agent-read). Singapore's Skills Framework and Jobs-Skills Portal could not be checked.
- **Pay-by-level sites.** Levels.fyi describes tiered checking of self-reported pay: offer letters or pay slips checked field by field, then verified accounts, then anonymous entries with anomaly checks, with unverified data weighted less. This is its own description; no independent audit was found.

## 4. Singapore

- **The main official anchor.** MOM's Occupational Wage tables (2025 edition): reference month **June 2025, released 30 June 2026**; **full-time resident employees**; over 500 occupations; **basic and gross monthly wages, excluding bonuses**; median, 25th and 75th percentiles by industry; medians also by occupation group, sex, establishment size and age; data collection assessed by an external firm. **Confirmed on the MOM page.** Two practical consequences: the figures are about a year old when released, and they leave out bonuses and non-residents (so Employment Pass holders are not in them). Whether the survey covers only private-sector establishments is **not confirmed**: the methodology PDF could not be read.
- **Open data.** data.gov.sg publishes median gross monthly income by occupation and sex (2010 to 2025) from the Comprehensive Labour Force Survey, residents only, excluding employer CPF contributions (agent-read).
- **Private salary guides** (recruiters' annual guides, NodeFlair, Glassdoor, Payscale) rarely publish a full method. Claims found about their data (for example a 200-observation minimum, or 280,000 data points) came from search snippets and are **not verified**.
- **Rules that shape the data.** MOM requires Employment Pass applicants to advertise on MyCareersFuture for at least 14 consecutive days, with any advertised salary range no wider than 2 to 1 (top at most twice the bottom) and containing the offered salary. **Confirmed**; it applies to employers filing Employment Pass applications, with exemptions such as firms under 10 employees and monthly salaries of $22,500 or more. It does **not** require salaries in all Singapore job ads. Employment Pass minimum qualifying salaries (from $5,600 for the youngest applicants outside financial services, rising from 1 January 2027) were read by the agent from MOM's page.
- **Take-home versus gross.** CPF contributions sit between gross pay and take-home pay (employer 17% and employee 20% of wages for employees aged 55 and below, per the agent's reading of the CPF Board page). Check whether a figure is gross wage, wage plus employer CPF, or take-home before comparing.

## 5. How an employer turns a benchmark into your offer

- **Pay bands.** Jobs sit in grades with a minimum, midpoint and maximum; the midpoint is the target for a fully competent person. **Compa-ratio** is pay divided by the midpoint (1.0 means at midpoint). **Range penetration** is (pay minus minimum) divided by (maximum minus minimum). Range spread has no single definition (a common one is (max minus min) divided by min), so check which convention a company uses.
- **Market position.** WorldatWork says many employers pay around the median (50th percentile) with some targeting the 75th for high performers or scarce skills, and that positioning should weigh stability, talent supply and productivity. Figures on how many employers target which percentile were seen only in snippets and are not used.
- **What else decides your offer.** Budget, internal pay equity and competing offers are commonly cited; only talent supply was confirmed in a page the agent opened.
- **Total rewards.** Two offers with the same base can differ in value through bonus, equity, benefits and retirement contributions. No opened source explained how to compare them; annualising each component is a sensible practice but not source-confirmed.

## 6. Where salary data goes wrong

| Problem | Evidence |
|---|---|
| **Advertised pay is rare and runs high** | Only about 14% of US online job posts contain any pay. Where given, more than half are ranges averaging 28% of the midpoint. Advertised wages are about 40% above CPS and OES wages overall, about 80% for low-wage salaried jobs. Firms that post pay are unrepresentative, and the missingness is not random: high-wage jobs are less likely to post, and use wider ranges when they do. **Confirmed on the Minneapolis Fed page** |
| **Transparency laws change the data** | In Colorado, the share of postings with pay rose 30 percentage points and wages rose 1.3 to 3.6% (NBER abstract, agent-read). The US share of postings with pay rose from about 15% to about 53% (NY Fed, agent-read). Whether posted ranges match what is paid was not established |
| **Self-reported pay is understated and the error is not random** | A German study linking survey wages to tax and social-security records found respondents report about 7.3% less than their administrative wages on average. **Confirmed in the abstract.** The agent, reading the full paper, reports that low earners tend to overreport and the top tenth underreport by about 13.5%, and that year-on-year changes are much less biased than levels (the abstract confirms the last point) |
| **Crowd-sourced sites are partly right** | A Richmond Fed study of millions of Glassdoor entries found a "fairly high" correlation of average salaries with official data across industries and regions, and within-industry dispersion "fairly close" to a household survey, but employment shares by industry "differ substantially". **Confirmed in the abstract.** No opened study validated Payscale or similar sites against payroll data |
| **Surveys differ from each other** | Different definitions (asking, offered, paid; base or total; time period), different mixes of employers, different matching. The sources found did not quantify how much surveys disagree |
| **Official data has non-response too** | One in three OEWS establishments did not respond; MOM's tables are about a year old when released |

## 7. A method a job seeker can follow

*This is a synthesis of the practices above, not a method found whole in one source. The numbers in the example are made up to show the steps.*

1. **Define the job by what you would do**, not its title: duties, level, industry, company size, location. If the job straddles two levels, price both.
2. **Get an official anchor.** For Singapore, the MOM occupational table: median, 25th and 75th percentile for the closest occupation and industry. Note that it excludes bonuses and is about a year old.
3. **Get two sources of different types**, for example an employer-reported salary guide, advertised ranges for similar jobs, and a crowd-sourced site. They have different biases (advertised pay runs high; self-reported pay runs low and is not random), so compare them rather than averaging blindly.
4. **Put everything on the same basis**: monthly or annual, base or total cash, gross or after CPF, same date. Bring older figures forward only with a stated, modest factor.
5. **Adjust for scope and skills.** If the job you are pricing has more scope than the benchmark job, adjust up; employers apply such adjustments of the order of 10% (Mercer's example). Treat a scarce skill as a reason to look at the 75th percentile, not as a fixed percentage; the measured premium for a typical new skill is about 3%.
6. **State the range and the basis.** For example (made up): *Official median S$5,000, 25th to 75th percentile S$4,200 to S$6,200 (basic, excludes bonus, June 2025). Advertised ranges for similar jobs run S$4,800 to S$6,500. A crowd-sourced site shows S$5,300 from 14 reports. Adjusting for a larger scope than the benchmark job, a reasonable base-pay range is about S$5,000 to S$6,300, centred nearer S$5,600; confidence moderate, because the sources agree on the middle but the official data is a year old and excludes bonus.*
7. **Check against the employer.** A specific employer's band, budget and the total package (bonus, equity, benefits) decide the actual offer. Check whether the posting says pay is negotiable: in one large field experiment, the difference in who negotiated disappeared when the posting said so. If it is unclear, asking is the way to find out (this last step is practical advice, not a research finding).

## 8. What this means for JobHub

- Show a **range with its basis**, not a single "your worth" number: which source type, which occupation match, date of data, base or total, and sample size where known.
- Prefer an **official anchor** where one exists (for Singapore, MOM's table), and label private and crowd sources by their bias direction.
- Keep **advertised, offered and actual pay** separate; never present a posted salary as what people are paid.
- Treat **skills as adjustments with stated, modest sizes**, not as a calculator that adds a percentage per skill; the evidence is associational.
- Say **how old the data is and what it leaves out** (bonus, non-residents, employer CPF).
- Do not use vendor headline premiums (for example a 28% AI premium) without their method.

## Confidence labels used

- **Confirmed**: the lead researcher opened the primary source and checked the figure.
- **Agent-read**: a research agent opened the source and reported it; not re-opened by the lead.
- **Vendor or practice**: a company's or professional's statement of how it works; accurate as a description of practice, not independent evidence.
- **Unverified**: seen only in a search snippet or from memory; not used as a finding.

See `sources.md` for which source falls under which label, and `limitations.md` for what this run could not establish.
