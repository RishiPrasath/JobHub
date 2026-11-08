# W1: how salary benchmarks are built (raw agent note)

*Haiku-model research agent, 2026-11-07. Saved unedited by the lead researcher. Not yet checked; see `findings.md` for what was confirmed.*

A) FINDINGS

1. OEWS (US government wage survey) draws a probability sample of about 8.8M nonfarm establishments from the QCEW frame, which is built from state unemployment-insurance employer filings. Strata are state, metro/nonmetro, NAICS industry and ownership; large establishments are certainty-selected. Design weights are inverse selection probabilities. [https://www.bls.gov/opub/hom/oews/design.htm] [PRIMARY]

2. OEWS runs a six-panel (three-year) cycle, with two semiannual panels of about 186k-189k establishments per year. Annual estimates pool six panels (about 1.1M establishments). Response for May 2025 was 66.2% of viable establishments. [https://www.bls.gov/opub/hom/oews/design.htm] [PRIMARY]

3. OEWS places non-wage-reporting establishments into 12 wage intervals, uses a model-based method (MB3) to estimate unobserved establishments, and adjusts earlier panels' wages to the reference date with adjustment factors. Donor wages are adjusted for area and industry. [https://www.bls.gov/oes/current/oes_tec.htm] [PRIMARY]

4. The BLS National Compensation Survey measures employer compensation costs (wages, salaries, benefits), feeding ECI and ECEC products. The old handbook chapter has been split, so sample design is in separate chapters I did not open. [https://www.bls.gov/opub/hom/ncs/home.htm] [PRIMARY]

5. Job matching should rest on content and scope, not title. Salary.com treats a match as defensible only if at least 80% of duties align with the survey description, and hybrid roles can be matched to the highest-level role, the most frequent function, or a weighted blend. [https://www.salary.com/resources/comp-101/salary-benchmarking] [SECONDARY]

6. When a survey job does not fit, Mercer advises re-matching, or adjusting with a premium or discount for scope. Its example is a 10% discount where the survey job carries higher responsibility. Rules should be documented. [https://www.imercer.com/articleinsights/market-pricing-101-handling-data-anomalies] [SECONDARY]

7. Outlier handling is judgment-based, not a formal test. Mercer flags points far from other surveys, checks sample size (its example threshold: under 100 observations or under 10 companies, then discard), and flags implausible values such as target total cash below base. [https://www.imercer.com/articleinsights/market-pricing-101-handling-data-anomalies] [SECONDARY]

8. Aging moves data from different effective dates to a common date. Mercer says rolling prior-year data forward with a single factor is no longer suggested because pay movement varies by job. Salary.com recommends an aging factor even for roughly six-month-old data. [https://www.imercer.com/articleinsights/market-pricing-101-handling-data-anomalies] [SECONDARY] and [https://www.salary.com/resources/comp-101/salary-benchmarking] [SECONDARY]

9. Geographic differentials should reflect local labour cost, not cost of living. Organisations often move to tiered geographic zones. [https://www.salary.com/resources/comp-101/salary-benchmarking] [SECONDARY]

10. Weighting: a zero weight excludes a data line, a higher weight (for example an industry-specific survey) gives more influence, and a lower weight (for example a survey dominated by not-for-profits) reduces it. Mercer also notes that a single low-paying employer with many incumbents can skew an incumbent-weighted average, so company-weighting may be preferred. [https://www.imercer.com/articleinsights/market-pricing-101-handling-data-anomalies] [SECONDARY]

11. Percentile choice is a market-position decision: the 25th suits entry-level roles, the 50th (median) is the common anchor, and the 75th is a premium for hard-to-fill roles. Employers can match, lead or lag the market. [https://www.salary.com/resources/comp-101/salary-benchmarking] [SECONDARY]

12. The 1996 health-care Statement 6 safety zone covered written wage and benefit surveys. Per a 2023 Lowenstein alert, it treated data older than three months as unlikely to be competitively sensitive and pointed to five or more participants; a DOJ official disputed both as guarantees. The DOJ withdrew the statements in February 2023. [https://www.lowenstein.com/news-insights/publications/client-alerts/is-it-still-safe-to-exchange-wage-and-other-compensation-related-information-antitrust] [SECONDARY]

13. The 2016 DOJ/FTC HR guidance lists four factors that can make an exchange lawful: a neutral third party manages it, the information is relatively old, it is aggregated, and enough sources are combined that no single source can be identified. [https://www.mintz.com/2016/10/ftc-and-doj-issue-antitrust-guidance-for-human-resource-professionals/] [SECONDARY]

14. Pay definitions: base salary is the fixed pay; variable pay is bonus or incentive; total cash compensation is base plus variable. Salary.com does not define "total compensation". [https://www.salary.com/resources/comp-101/salary-benchmarking] [SECONDARY]

B) WHERE SOURCES DISAGREE OR ARE UNCLEAR

- Withdrawal date: the Lowenstein alert and search snippets say February 2023 (announcement reportedly 3 Feb; a speech on 2 Feb is sometimes cited). Not confirmed on justice.gov.
- FTC: one search snippet says the FTC followed in July 2023. Lowenstein does not say whether the FTC withdrew. Unresolved.
- Current status of the 2016 guidance: Lowenstein (April 2023) says it remained in place. Search snippets say DOJ/FTC replaced it on 16 Jan 2025 with Guidelines for Business Activities Affecting Workers. One commentator said the incoming Commission could revert it. Current status (Nov 2026) unknown.
- Whether any safety zone survives: a search-snippet commentator says the 2025 Guidelines have no safety zone, no participant minimum and no data-age threshold; another says many exchanges would still be fine. Opinion, not confirmed.
- Outlier thresholds differ by vendor; no industry standard was found.

C) WHAT I COULD NOT CONFIRM FROM A PAGE I OPENED

- Statement 6 full text and the "three sources" and "caps on any one contributor's weight" requirements. The FTC archive copy came back empty and the DOJ PDF returned 404. The 25% weight cap in the brief was not found in any source. The "five respondents" and "three months" figures come from Lowenstein's summary, not the original text.
- The DOJ press release (justice.gov) returned empty. The 2025 Guidelines were not opened; their replacement role comes from search summaries only.
- Crowd-sourced data (Payscale, Glassdoor): the Payscale methodology page returned 404; I have no opened source on collection or verification.
- Job-posting data: the Ravio methodology page returned 429. Claims that adverts reflect advertised pay, that duplicates are removed (CIfA), and a 2.5-3.5% annual aging rate (vendor) come from search snippets only.
- The Archbright 2026 methodology PDF returned binary and was not read, so its SD-based outlier method is unverified.
- Mean and percentile calculation details for OEWS (the Calculation section was not opened). The claim that OEWS publishes 10th/25th/median/75th/90th percentiles is from the brief, not a page.
- NCS sample design and any definition of "total compensation".
- FROM MEMORY: none used in the findings.

D) TOP 6 SOURCES

1. https://www.bls.gov/opub/hom/oews/design.htm | BLS, OEWS Handbook of Methods (date not shown) | Government sample design, frame, panels, weights.
2. https://www.bls.gov/oes/current/oes_tec.htm | BLS, OEWS Technical Notes (May 2025 edition per page) | Wage intervals, modelled imputation, aging adjustment.
3. https://www.bls.gov/opub/hom/ncs/home.htm | BLS, NCS overview (archived; date not shown) | Scope of compensation measures and where the detailed chapters sit.
4. https://www.imercer.com/articleinsights/market-pricing-101-handling-data-anomalies | Mercer, Market Pricing 101 (date not shown) | Outliers, weights, premiums, aging practice.
5. https://www.salary.com/resources/comp-101/salary-benchmarking | Salary.com, Comp 101 (date not shown) | Job matching threshold, percentile positioning, pay definitions.
6. https://www.lowenstein.com/news-insights/publications/client-alerts/is-it-still-safe-to-exchange-wage-and-other-compensation-related-information-antitrust | Lowenstein Sandler, client alert (April 2023 per file name) | Statement 6 history, DOJ withdrawal timing, and the enforcement debate. Use for context, not as a primary legal source.
