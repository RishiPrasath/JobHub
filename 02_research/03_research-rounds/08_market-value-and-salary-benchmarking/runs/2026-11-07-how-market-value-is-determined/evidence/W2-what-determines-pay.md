# W2: what determines pay, labour economics (raw agent note)

*Haiku-model research agent, 2026-11-07. Saved unedited by the lead researcher. Not yet checked; see `findings.md` for what was confirmed.*

RESEARCH NOTES: what determines pay (labour economics). Sources marked "opened" were fetched; others were seen only as search snippets and are flagged.

A) FINDINGS

1. The Mincer human capital earnings function regresses log earnings on years of schooling and post-school labour-market experience. Becker and Chiswick (1966) first regressed log earnings linearly on schooling; Mincer (1974) added post-school experience. [https://iza.org/publications/dp/16668] [PRIMARY]

2. Large firms hire workers with higher observable quality (more education, longer tenure, more full-time status). Oi and Idson's Handbook chapter puts the firm-size wage gap at about 35%, which they compare with a 36% gender gap for men over women. [https://ideas.repec.org/h/eee/labchp/3-33.html] [PRIMARY]

3. Oi and Idson review three behavioural explanations for the firm-size premium: matching productive workers with able entrepreneurs, efficiency wages that deter shirking, and managerial rent sharing. They conclude that the organisation of work and the selection of employees largely explain the link between pay and firm size. [https://ideas.repec.org/h/eee/labchp/3-33.html] [PRIMARY]

4. Using US administrative matched employer-employee data for 1978 to 2012, Song, Price, Guvenen, Bloom and von Wachter find that nearly all of the rise in earnings dispersion comes from growing differences in average pay between employers. Pay differences within firms stayed roughly constant across industries, regions and firm-size groups. [https://econpapers.repec.org/RePEc:nbr:nberwo:21199] [PRIMARY]

5. Card's survey of the causal return to schooling finds that the average marginal return is not much below what a standard OLS human capital earnings function gives. Instrumental-variable estimates based on education-system changes run 20 to 40% above OLS, and twin studies suggest an upward ability bias of about 10%. [https://econpapers.repec.org/RePEc:eee:labchp:3-30] [PRIMARY]

6. Compensating differentials (Rosen's equalising-differences model) have faced persistent credibility problems. Moving from cross-sectional to panel models reduced bias from unobserved human capital but exposed biases from labour-market frictions and endogenous job mobility. Newer work uses matched employer-employee data and quasi-random variation in amenities. [https://ideas.repec.org/a/aea/jecper/v37y2023i3p189-212.html] [PRIMARY]

7. Wellfound's method page says its salary estimates compare recent listings for comparable roles, matched on role name, geography and experience level, drawn from thousands of employers and third-party sources. It does not name a statistical model. The page was last updated 22 February 2023. [https://help.wellfound.com/article/744-candidates-employers-how-are-salary-estimates-calculated] [PRIMARY]

8. PayScale's methodology explainer describes its figures as coming from its online salary survey, and it names survey products such as a 2026-27 Salary Budget Survey covering 1,266 organisations, cut by industry, company size and employee type. Its benchmarking product is described as "AI-guided data" with no method given, and the page does not describe how the calculator produces an estimate. [https://www.payscale.com/research-and-insights/payscale-methodology-explained] [SECONDARY]

9. Oi and Idson's review describes large-firm pay as partly a rent-sharing channel, not only worker quality or working-conditions compensation, so the firm-size premium is not explained by worker quality alone. [https://ideas.repec.org/h/eee/labchp/3-33.html] [PRIMARY]

10. Card's OLS estimates rest on a standard Mincer-type specification with schooling and experience, so the IV and twin results apply to that specification's return. Card's own summary does not give an absolute percent-per-year return. [https://econpapers.repec.org/RePEc:eee:labchp:3-30] [PRIMARY]

B) WHERE SOURCES DISAGREE OR ARE UNCLEAR

- Firm-size premium trend: Bloom et al.'s 2018 AEA preliminary draft (search snippet, not opened) says the large-firm premium held until about 2013 and then fell. Its industry-versus-within-industry split differs between versions (about half and half in one, about 20/80 in another). Treat the split as unresolved.
- Mincer explained variance: a Serbian proceedings paper (search snippet, not opened) says schooling alone explains about 7% of wage variation and schooling plus experience and experience-squared about 30%. No opened source confirms this.
- Glassdoor: the methodology PDF and a mirror failed to load (DNS error and HTTP 403). Snippets describe a log-scale model with job title, company, industry, seniority, company size and metro area as inputs, validated against BLS medians. A competing vendor (Ravio) criticises Glassdoor's transparency, so treat that critique with caution.
- Indeed: no official methodology page was found. Third-party sites say it uses "proprietary estimation models" with job title, experience, education and location, and that hourly figures are multiplied by 2,080 hours. These are unconfirmed.

C) WHAT I COULD NOT CONFIRM FROM A PAGE I OPENED

- Numeric returns to a year of schooling and to experience: the Chiswick (IZA) and Card pages I opened give no percent-per-year figure. FROM MEMORY: a commonly cited range is roughly 6 to 10% per year of schooling. FROM MEMORY: the Mincer specification includes a quadratic in experience.
- Share of wage variance explained by Mincer models: no opened source gives an R-squared. Only the search-snippet figures above exist.
- Union wage premium: search snippets cite Hirsch and Schumacher at about 20% (2001, down from 26% in 1984) and Blanchflower and Bryson at about 16.5% (2002), via a think-tank summary. Not opened, so unverified.
- Cost of living and location: a Moretti (2013) snippet says cost-of-living changes explain about a quarter of the rise in the nominal college premium over 1980 to 2000. Not opened.
- Local labour-market tightness and wage Phillips curves: no source found.
- Efficiency wages in Shapiro and Stiglitz (1984): the AER abstract page returned 404, so the unemployment-as-discipline mechanism is from snippets only.
- Rosen (1986) binary clean/dirty job model: from lecture-note snippets only.
- Glassdoor and Indeed method details: see B. PayScale's 2009 methodology PDF was unreadable (binary), so its calculator inputs and any model are unknown.
- Tenure and hours effects on pay beyond the Oi and Idson summary: not checked.

D) TOP 6 SOURCES (opened)

1. https://ideas.repec.org/h/eee/labchp/3-33.html. Oi and Idson (1999), "Firm size and wages", Handbook of Labor Economics vol. 3, ch. 33. Good for firm-size premium size and mechanisms.
2. https://econpapers.repec.org/RePEc:nbr:nberwo:21199. Song et al., "Firming Up Inequality" (NBER WP 21199, 2015; QJE 2019). Good for the firm share of earnings inequality.
3. https://ideas.repec.org/a/aea/jecper/v37y2023i3p189-212.html. Lavetti (2023), JEP. Good for compensating differentials and their identification problems.
4. https://econpapers.repec.org/RePEc:eee:labchp:3-30. Card (1999), Handbook ch. 30. Good for the schooling-return IV gap and ability bias.
5. https://iza.org/publications/dp/16668 (IZA DP 16668, Chiswick). Good for the history of the Becker, Chiswick and Mincer equations.
6. https://help.wellfound.com/article/744-candidates-employers-how-are-salary-estimates-calculated. Wellfound method page (2023). Good as an example of a vendor's stated inputs for salary estimates.
