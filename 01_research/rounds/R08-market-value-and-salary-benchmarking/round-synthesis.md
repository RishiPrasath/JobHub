# Round 08 synthesis

Status: draft synthesis written during the 2026-11 reorganization; owner review pending

Research date: 2026-11-07, Singapore.

## Question

How do professionals determine a person's market value and a salary benchmark from their skills and experience? What data is used, how are the numbers calculated, which variables matter, and how reliable are the results? ([Round brief](round-brief.md))

## What was done

One desk-research [run](runs/2026-11-07-how-market-value-is-determined/README.md). Six Haiku-model agents each researched one question, and the lead researcher re-opened sources behind some main claims and wrote the [report](runs/2026-11-07-how-market-value-is-determined/findings.md). No product was built or tested and no salary sites were scraped.

## Key findings

All entries come from the [run findings](runs/2026-11-07-how-market-value-is-determined/findings.md) unless linked otherwise. Labels are the report's own: **Confirmed** (lead opened the primary source), **Agent-read**, **Vendor or practice**, and strength wording in its tables.

| Finding | Confidence as stated |
|---|---|
| There is no single market value: a job benchmark, personal adjustments and what an employer can pay combine, so a credible answer is a range with a stated basis | None stated (report's short answer) |
| Benchmarks are matched to jobs by duties, cleaned, aged to one date and reported as percentiles | Vendor practice, 1 to 2 sources per step |
| The US OEWS design pools about 1.1 million establishments; May 2025 response was 66.2% | Confirmed |
| Job content and level decide which benchmark applies | Strong (how official surveys work) |
| A review of 1,120 estimates puts the private return at about 9% per year of schooling | Strong for the average; size varies. [Limitations](runs/2026-11-07-how-market-value-is-determined/limitations.md) say this was checked through search results summarising the abstract |
| Experience matters; the size was not verified | Strong that it matters; size not verified |
| Nearly all the rise in US earnings dispersion came from differences between employers; large employers pay about 35% more on average | Strong (primary, agent-read) |
| A posting listing a new skill advertises about 3 to 3.4% more; AI-developer skills above 8% in the US. These are associations in advertised pay | Confirmed; strength "Moderate; associational" |
| Industry and location matter, with no verified size | Moderate (industry unresolved; location from practice) |
| Talent supply affects where employers pay against the market | Weak for size; plausible for direction |
| Stating that pay is negotiable removed the gender gap in negotiating in one field experiment of about 2,500 job seekers | Moderate (one large field study; lab evidence from students) |
| About 14% of US online posts contain pay, and advertised wages run about 40% above official wages overall | Confirmed |
| Self-reported pay is about 7.3% below administrative records in one German study | Confirmed in the abstract; distribution details Agent-read |
| Glassdoor averages correlate "fairly high" with official data, but industry employment shares differ substantially | Confirmed in the abstract |
| MOM's occupational wage tables (June 2025, full-time residents, excluding bonuses) are the main Singapore anchor and are about a year old on release | Confirmed |
| Employment Pass filings require 14 consecutive days on MyCareersFuture, with any advertised range no wider than 2 to 1. This does not apply to all Singapore job ads | Confirmed |
| Lightcast's 28% AI premium has no stated method and mostly compares different jobs | None stated for the 28%; the method gap is the report's own observation |
| Triangulate one official anchor and two other source types on one basis, and show a range | None stated; "a synthesis of the practices above, not a method found whole in one source". The worked example is made up |

## What remains unknown

- How much of pay each variable explains, and the size of the experience, location, union or labour-market-tightness effects.
- The causal effect of a skill on a person's pay.
- Whether posted ranges match what is paid, and how far salary surveys disagree for the same job.
- Whether MOM's survey covers only private-sector establishments; its methodology PDF could not be read.
- Private salary guides' methods, and any validation of Payscale or Indeed against payroll data.
- Singapore treatment of 13th-month pay, bonuses, allowances and equity under CPF.
- Current antitrust guidance on exchanging pay data, and how many employers target which percentile.

## Limits

- "Confirmed" has a narrower meaning than it sounds: pages were read through a tool that returns a model-written summary, so figures were checked against that summary ([limitations](runs/2026-11-07-how-market-value-is-determined/limitations.md)).
- First-pass work came from Haiku-model agents, and several of their claims were corrected or dropped. Only some primary sources were re-opened.
- United States evidence dominates. Singapore evidence is mainly official statistics, not research on how Singapore pay is set.
- One pass, one day, with no second reviewer and no compensation professional.
- This is research, not advice. No salary figure is a fact about any person or role, and the report's JobHub implications are not accepted product decisions.
