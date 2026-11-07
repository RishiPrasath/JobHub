# W4: Singapore salary context (raw agent note)

*Haiku-model research agent, 2026-11-07. Saved unedited by the lead researcher. Not yet checked; see `findings.md` for what was confirmed.*

A) FINDINGS

1. MOM's Occupational Wages 2025 tables were released 30 June 2026, with reference month June 2025. They cover over 500 occupations for full-time resident employees, in basic and gross monthly wages excluding bonuses. [https://stats.mom.gov.sg/Pages/Occupational-Wages-Tables2025.aspx] [PRIMARY]
2. The released tables give median, 25th and 75th percentile monthly wages for common occupations by industry. Medians are also given by occupation group, sex, establishment size and age. [https://stats.mom.gov.sg/Pages/Occupational-Wages-Tables2025.aspx] [PRIMARY]
3. The 2025 page links a methodology PDF, "Coverage and Methodology of Occupational Wage Survey, 2025". The PDF was binary and I could not read its text. [https://stats.mom.gov.sg/Pages/Occupational-Wages-Tables2025.aspx] [PRIMARY]
4. The OWS data-resources page gives no release frequency, no wage definitions and no methodology link. It points to a Benchmarking Tool ("find out where your salary ranks within your occupation"). [https://stats.mom.gov.sg/SL/Pages/Occupational-Wages-Data-and-Other-Resources.aspx] [PRIMARY]
5. MOM's 2025 page says data collection processes were assessed by an external firm, Ernst and Young Advisory. [https://stats.mom.gov.sg/Pages/Occupational-Wages-Tables2025.aspx] [PRIMARY]
6. The data.gov.sg MOM dataset gives median gross monthly income from employment by occupation, sex and year (2010 to 2025). It is based on the Comprehensive Labour Force Survey, covers residents and excludes full-time National Servicemen, and uses SSOC 2024 with earlier data mapped where possible. Last updated 27 March 2026; Open Data Licence. [https://data.gov.sg/datasets/d_16fdf439f84527f2ecfcee193a8ea567/view] [PRIMARY]
7. The data.gov.sg median is labelled as excluding employer and platform-operator CPF contributions. It is therefore not on the same basis as a CPF-inclusive wage figure. [https://data.gov.sg/datasets/d_16fdf439f84527f2ecfcee193a8ea567/view] [PRIMARY]
8. MOM's Progressive Wage Model index lists sector pages (cleaning, security, landscape, lift and escalator, retail, food services, waste management, and occupational pages for administrators and drivers). It also covers the Local Qualifying Salary. The index itself gives no wage amounts. Last updated 12 October 2026. [https://www.mom.gov.sg/employment-practices/progressive-wage-model] [PRIMARY]
9. The MOM EP eligibility page (updated 3 November 2026) gives monthly qualifying salaries by age. Outside financial services they run from $5,600 (age 23 or below) to $10,700 (45+). From 1 January 2027 for new applications they rise to $6,000 to $11,500. Financial services is $6,200 to $11,800 now, rising to $6,600 to $12,700. [https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility] [PRIMARY]
10. MOM's job-advertising page (updated 5 January 2026) says any advertised salary range must be visible, must not exceed twice the minimum, and must include the offered EP salary. Ads must stay open at least 14 consecutive days, and changing the salary requires a new advertisement. The page does not say every job ad must state a salary. [https://www.mom.gov.sg/passes-and-permits/employment-pass/consider-all-candidates-fairly] [PRIMARY]
11. The CPF Board page "CPF Contribution Changes from 1 January 2027" (updated 9 June 2026) gives rates for employees earning over $750 a month. From 2027: 55 and below 37% (employer 17, employee 20); above 55 to 60 35.5%; above 60 to 65 26%; above 65 to 70 16.5%; above 70 12.5%. [https://www.cpf.gov.sg/conrate2023] [PRIMARY]
12. The same CPF page states the 2026 totals for above 55 to 60 (34%) and above 60 to 65 (25%). Subtracting the stated 2027 increases gives a 2026 split of 16% employer and 18% employee for above 55 to 60, and 12.5% each for above 60 to 65. This split is my derivation. [https://www.cpf.gov.sg/conrate2023] [PRIMARY]
13. A vendor methodology paper for Glassdoor Local Pay Reports (dated 29 December 2016, US-focused) says the data are anonymous user-submitted salary reports, modelled with a proprietary machine-learning model. It does not claim a representative sample. [https://api.glassdoor.com/blog/glassdoor-local-pay-reports-methodology/] [SECONDARY]

B) WHERE SOURCES DISAGREE OR ARE UNCLEAR

- CPF Ordinary Wage ceiling: secondary guides say $8,000 from 1 January 2026 (up from $7,400). The official CPF page I opened does not state it. Unresolved.
- 2026 employer/employee split for above 55 to 60: guides disagree on which side is 16% and which is 18%. The official 2027 table, read with its increments, supports 16% employer and 18% employee.
- Job-ad posting period: MOM says 14 consecutive days. A 2020 KPMG note and one law firm say 28 days. The MOM page (January 2026) is the more current source.
- Job-ad salary exemption: the MOM EP page I opened gives a $22,500 threshold for COMPASS exemption, which is a different rule. Older sources cite $12,000 for job-ad exemption. Current job-ad exemption rule not confirmed from an opened page.
- MOM occupational data use different SSOC versions: the data.gov.sg dataset uses SSOC 2024. The OWS 2025 version is not confirmed from an opened page.
- Glassdoor's only methodology page I could open is from 2016 and covers the US. Treat it as dated.

C) WHAT I COULD NOT CONFIRM FROM A PAGE I OPENED

- OWS 2025 coverage and exclusions (private sector only? CPF-contributing residents only?), bonus treatment and wage-type definitions. Only the PDF's binary was returned. Search snippets, not opened, suggested private-sector establishments and full-time residents with CPF contributions.
- OWS SSOC version for 2025 (search snippet, not opened, said 2021 used SSOC 2020 and 2018 used SSOC 2015).
- OWS release frequency. The 2023, 2024 and 2025 table pages suggest an annual cycle, but no page states it (inference).
- Whether the CLFS wage series is "pre-deduction" for employees (search snippet only).
- Progressive Wage Model wage amounts and Local Qualifying Salary values. The sector pages I tried returned 404. A search snippet said the LQS rises to $1,800 from 1 July 2026, not opened.
- Jobs-Skills Portal wage content and "transition pathways" pay increments. The official site would not load. Secondary articles (search only) describe this.
- NodeFlair methodology (search snippets, not opened): user submissions checked against payslips or offer letters, supplemented by job listings and MyCareersFuture, with a 200-data-point minimum per category in the 2025 report.
- Michael Page 2026 guide methodology. Search snippets, not opened, say the 2024 guide used about 280,000 data points from its own sources. Nothing confirmed for 2026.
- Payscale methodology (search snippets only): crowdsourced, with cost-of-living normalisation. No Payscale page opened.
- CPF Ordinary Wage and Additional Wage ceilings and the $102,000 total wage ceiling (secondary sources only).
- Total compensation elements (13th-month wage, variable bonus, allowances, equity) and how CPF applies to each: FROM MEMORY, not checked against any opened page.

D) TOP 6 SOURCES

1. https://stats.mom.gov.sg/Pages/Occupational-Wages-Tables2025.aspx - MOM / MRSD, released 30 June 2026 - Best official source for OWS 2025 table types, reference period and wage definitions. Links to the methodology PDF.
2. https://stats.mom.gov.sg/SL/Pages/Occupational-Wages-Data-and-Other-Resources.aspx - MOM, undated - Points to the Benchmarking Tool. Says nothing on frequency or definitions.
3. https://data.gov.sg/datasets/d_16fdf439f84527f2ecfcee193a8ea567/view - MOM via data.gov.sg, updated 27 March 2026 - Machine-readable CLFS income-by-occupation series (SSOC 2024). Note its CPF basis.
4. https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility - MOM, updated 3 November 2026 - Authoritative EP qualifying salary tables and 2027 changes.
5. https://www.mom.gov.sg/passes-and-permits/employment-pass/consider-all-candidates-fairly - MOM, updated 5 January 2026 - Rules for salary ranges and posting periods in EP-linked job ads.
6. https://www.cpf.gov.sg/conrate2023 - CPF Board, updated 9 June 2026 - Age-band contribution rates from 2027, with 2026 totals. Does not include the ceilings.
