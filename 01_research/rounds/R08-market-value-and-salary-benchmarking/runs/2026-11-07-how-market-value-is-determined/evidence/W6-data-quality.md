# W6: how reliable salary data is (raw agent note)

*Haiku-model research agent, 2026-11-07. Saved unedited by the lead researcher. Not yet checked; see `findings.md` for what was confirmed.*

A) FINDINGS

1. In a German study linking survey wages to administrative records (SOEP-ADIAB, 59,118 person-years), respondents underreported pay by about 7.3% on average. About 70.5% underreported, 24.5% overreported, and 5% were within ±2.5%. [https://arxiv.org/abs/2411.04751] [PRIMARY]

2. Misreporting is systematic. Low-wage workers tend to overreport and high earners underreport (top ventile about -13.5%). Job and firm characteristics explain about 69% of the explained variance in reporting error. [https://arxiv.org/html/2411.04751v1] [PRIMARY]

3. Bias is much smaller for year-on-year changes than for levels. Survey wages overstate the wage-satisfaction link when wages are a regressor, and changes reduce that bias. [https://arxiv.org/abs/2411.04751] [PRIMARY]

4. Rounding is common but explains little. About 60% of answers were multiples of €50 or €100. Dropping rounded answers barely moved the underreporting share (24.5% to 23.1%). [https://arxiv.org/html/2411.04751v1] [PRIMARY]

5. Outliers distort averages. Overreports above €5,000 are rare but drive the very high relative bias in the bottom income ventile. Trimming to the 1st–99th percentiles changed mean bias only from €186 to €190. [https://arxiv.org/html/2411.04751v1] [PRIMARY]

6. Glassdoor entries matched official aggregates reasonably on average pay. The paper reports the correlation as "fairly high" across metro-industry cells, with within-industry dispersion close to PSID. Industry employment shares differed substantially from QCEW. [https://www.richmondfed.org/publications/research/economic_quarterly/2018/q4/karabarbounis] [PRIMARY]

7. Payscale's methodology page says it draws on voluntary self-reported surveys, employer HRIS "peer" data, and third-party partners. It does not state base versus total pay treatment, minimum sample thresholds, outlier handling, or data recency. [https://www.payscale.com/why-payscale/data-methodology/] [SECONDARY]

8. BLS OEWS (May 2022) draws on about 1.1 million establishments. The response rate was 65.4% by establishment and 62.5% by weighted employment, and BLS warns that low response may hurt quality. [https://www.bls.gov/oes/2022/may/oes_tec.htm] [PRIMARY]

9. Only about 14% of online job posts include pay. Among posts that give pay, more than half give a range, averaging about 28% of the midpoint. Posted wages run about 40% above CPS and OES wages overall, and about 80% higher for low-wage salaried roles. Firms that disclose pay are not representative. [https://www.minneapolisfed.org/research/staff-reports/online-job-posts-contain-very-little-wage-information] [PRIMARY]

10. Indeed postings show a typical low-to-high spread of about 17%. Only 22% of postings that disclose pay gave one exact figure (April 2023). Spreads widened most in California and Washington after transparency rules took effect. [https://hiringlab.indeed.com/2023/05/18/advertised-salary-ranges] [SECONDARY]

11. In Colorado, a difference-in-differences study found the share of postings with pay rose by 30 percentage points. Wages rose 1.3–3.6% across three datasets, with no effect on employment, posting counts, or pay dispersion. [https://www.nber.org/papers/w34480] [PRIMARY]

12. A New York Fed study estimates about 24% of covered ads (January 2025) omit pay. The share of US postings with pay rose from about 15% to about 53%. It does not say whether posted ranges match pay or how wide they are. [https://libertystreeteconomics.newyorkfed.org/2025/10/do-employers-comply-with-pay-transparency-requirements-in-job-postings/] [PRIMARY]

13. The EU Pay Transparency Directive (2023/970) had a 7 June 2026 transposition deadline. A May 2026 law-firm-based article says it will require pay ranges in job adverts and bans asking about current pay. Most member states had not finished transposition by then. [https://remoteworkeurope.eu/news/2026/eu-pay-transparency-most-states-miss-deadline/] [SECONDARY]

14. Uncertainty reporting: the SOEP paper reports sensitivity checks (alternative ±1.25% and ±5% correctness bands, trimming, and dropping rounded answers) and says conclusions held. This is an example of robustness reporting, not a formal uncertainty standard. [https://arxiv.org/html/2411.04751v1] [PRACTICE]

B) WHERE SOURCES DISAGREE OR ARE UNCLEAR

- Colorado realized pay: the NBER paper (claim 11) finds wage gains of 1.3–3.6%. A search summary also mentioned a Feng study finding no realized-wage effect, and a Cullen and Pakzad-Hurson paper predicting about a 2% wage decline. I did not open either, so this is unresolved.
- Range width: Indeed's 17% is a low-to-high percent difference. Minneapolis's 28% is a range as a percent of its midpoint. The definitions differ, so the numbers are not directly comparable.
- EU job-advert rule: vendor sources disagree on whether the range must be in the advert or only disclosed before interview. The directive text on EUR-Lex was not readable, so the wording stays unconfirmed.
- SOEP internal inconsistency: the introduction says about 5,500 individuals, the data section says 6,136.
- No page I opened validated Payscale or any other online salary site against BLS or payroll data. The only validation I opened is Glassdoor vs QCEW (claim 6).

C) WHAT I COULD NOT CONFIRM FROM A PAGE I OPENED

- Title inflation, stale entries, tiny-sample error, and base-versus-total mixing: no page I opened measured these for salary sites. Not confirmed.
- Glassdoor 60%/22% comparison of posted ranges with reported pay (search summary only, not opened).
- Glassdoor correlation of 0.83 (search summary only; the page only says "fairly high").
- Revelio/LinkUp range width 39% to 33% in Colorado (page returned 403).
- Arnold et al. ASU PDF, AAPOR "Margin of Sampling Error" PDF, and Census minimal-reporting standard: unreadable through WebFetch. Their contents are unconfirmed, including AAPOR's 95% convention, the subgroup and design-effect caveats, and the non-probability-panel caution.
- BLS OEWS 90% confidence interval example, the statement that standard errors do not capture nonsampling bias, and the 10–20% relative standard error target (search summaries only).
- Payscale's "65 million" profiles figure and its minimum-profile threshold (unverified third-party claims).
- Deloitte's 5% discrepancy against BLS wages and the Harvard Business Review $38,000 average range (search summaries only).
- The NY Fed 75% compliance ceiling and four-state detail (from a secondary article, not the NY Fed page).
- EU directive Article 5 wording (EUR-Lex returned an empty page).

D) TOP 6 SOURCES

1. https://arxiv.org/abs/2411.04751 (arXiv; 2024 ID, date not shown). SOEP-ADIAB survey vs administrative wage study; best evidence on self-report error size, who misreports, and levels vs changes.
2. https://arxiv.org/html/2411.04751v1 (same authors). Full-text detail on rounding, outliers, bands, and sample.
3. https://www.richmondfed.org/publications/research/economic_quarterly/2018/q4/karabarbounis (Federal Reserve Bank of Richmond, Economic Quarterly, 2018 Q4). Glassdoor vs QCEW and PSID: only opened study comparing an online salary source to official data.
4. https://www.nber.org/papers/w34480 (NBER working paper 34480). Colorado posted-pay share and wage effects; abstract only, not the full paper.
5. https://www.minneapolisfed.org/research/staff-reports/online-job-posts-contain-very-little-wage-information (Federal Reserve Bank of Minneapolis, Staff Report 690, dated 28 September 2026 on the page). Pay disclosure rates, posted vs OES gap, and selection in posted pay.
6. https://libertystreeteconomics.newyorkfed.org/2025/10/do-employers-comply-with-pay-transparency-requirements-in-job-postings/ (NY Fed Liberty Street Economics, October 2025). Compliance and disclosure trends in covered jurisdictions.

Also useful for posting-range width: https://hiringlab.indeed.com/2023/05/18/advertised-salary-ranges (Indeed Hiring Lab, May 2023), a vendor 02_analysis/reports of Indeed postings.
