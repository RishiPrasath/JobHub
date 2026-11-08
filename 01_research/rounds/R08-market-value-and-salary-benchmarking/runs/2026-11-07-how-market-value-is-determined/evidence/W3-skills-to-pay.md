# W3: how skills translate into pay (raw agent note)

*Haiku-model research agent, 2026-11-07. Saved unedited by the lead researcher. Not yet checked; see `findings.md` for what was confirmed.*

A) FINDINGS

1. Posted-wage skill premium method (IMF staff note): log posted hourly wage is regressed on an indicator for any "new" skill, with fixed effects for 4-digit ISCO x 6-digit NAICS x county x year cells. Controls include salary type interacted with year and the number of skills listed. Standard errors are clustered by occupation. [https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md] [PRIMARY]

2. In that IMF note, a new skill in a vacancy is associated with about 3 to 3.4% higher posted wages (US and UK, postings 2020-2024; 54.3m US postings, 5.6m UK). Postings with four or more new skills show 15.1% (UK) and 8.5% (US). Comparison is against postings listing only existing skills. [https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md] [PRIMARY]

3. AI-specific premiums in the same IMF note, within occupations: UK AI-developer and AI-user skills about 7.5-8%; US AI-developer above 8%, AI-user about 2%, non-AI new skills about 2.5%. [https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md] [PRIMARY]

4. Lightcast (vendor, July 2025, from job postings, over 1.3 billion): postings requiring AI skills show about 28% higher salaries, roughly $18,000 a year more, than postings without them. The release does not state how the premium was calculated. [https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23] [SECONDARY]

5. Lightcast's compensation model uses OEWS (BLS) as the wage base and job postings to add wage observations that can be linked to skills and certifications. The page does not describe how skill premiums are estimated or what controls are used. [https://kb.lightcast.io/en/articles/7932720-compensation-model] [SECONDARY]

6. Levels.fyi (self-description) collects self-reported pay in tiers. Tier 1 uses offer letters, W-2s or pay stubs, checked field by field. Tier 2 uses account history and verified work email. Tier 3 covers anonymous submissions, which get anomaly detection and human review when flagged. Unverified data is weighted less. [https://levels.fyi/about/] [SECONDARY]

7. Levels.fyi says published figures are altered slightly for anonymity, and company names are withheld for small companies. The page gives no share of verified data. [https://levels.fyi/verified] [SECONDARY]

8. O*NET 22.3 data dictionary: skill records use Importance (IM) and Level (LV) scales, and ratings are sourced from analysts. The dictionary file contains no wage or pay fields. Numeric scale ranges are not stated on this page. [https://www.onetcenter.org/dictionary/22.3/excel/skills.html] [PRIMARY]

9. ESCO: the occupations pillar is built on ISCO-08, and each occupation maps to exactly one ISCO-08 code. Skill-to-occupation links are marked essential or optional. The page states neither proficiency levels nor wage data. [https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/two-pillar-structure-esco] [PRIMARY]

10. Posted wages are not realized wages. The IMF note says its premiums use offers in postings, not actual pay. [https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md] [PRIMARY]

11. Sample bias: the IMF note says Lightcast over-represents formal, professional, technical and higher-skill occupations, and the bias is larger in emerging markets. Coverage also starts at different years by country. [https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md] [PRIMARY]

12. Causation and decay: the IMF note calls its macro task-creation result a prediction, not a causal estimate. It also finds workers in high-exposure, low-complementarity occupations see modestly lower wages 2-3 years after AI skill entry, so premiums may fade. [https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md] [PRIMARY]

13. Bundling: because the baseline controls for the number of skills listed, the new-skill premium is estimated conditional on posting length. Skill premiums are therefore not separable from bundle size in this design. This is an inference from the specification. [https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md] [PRACTICE]

B) WHERE SOURCES DISAGREE OR ARE UNCLEAR

- Size of the AI premium: Lightcast's roughly 28% compares postings with and without AI skills, with no stated controls. The IMF note's within-occupation AI premiums are roughly 2-8%, depending on AI-developer versus AI-user skills. The gap reflects different comparisons and controls, not a clear contradiction.
- Lightcast's premium is for AI skills overall; the IMF's 3-3.4% is for any new skill. These are different outcomes.
- Levels.fyi calls itself the only major site verifying against offer letters and W-2s. This is self-description; no independent audit was found.

C) WHAT I COULD NOT CONFIRM FROM A PAGE I OPENED

- PwC AI Jobs Barometer 2025 (56% AI wage premium, up from 25%; same-job comparison; about a billion ads): PwC pages returned HTTP 403. Only search snippets were seen, so these figures are unverified.
- Koll, Li and Tavares (IMF-linked working paper): baseline 4.4% and 2.3% saturated-FE premium, and the new-skill definition (under 1% of postings in 2010-11). The slides PDF was unreadable. Source is a search snippet.
- Burning Glass Institute / Alliance for Decision Education (Nov 2025): decision-skill premiums of up to 23%, with 17% for strategic decision-making. Search snippets only.
- Labussiere and Bol (Sociological Science 2026, skill bundles and wages); Rony (UNU-MERIT 2026, ICT ~7% premium); Deming and Kahn (job-ad skills and local wages); Ternikov (Economics Bulletin 2023). All from search snippets; none opened.
- SkillsFuture Jobs-Skills Portal (launched January 2025) and Skills Framework job roles with skill lists but no proficiency levels or wages. The ICT framework page returned only a title. Snippet only.
- O*NET 1-5 importance and 1-7 level numeric ranges: from search snippets, not confirmed on the dictionary page.
- Not searched or opened: Stack Overflow Developer Survey, Indeed Hiring Lab, LinkedIn Economic Graph methodology.
- Not found on any opened page: whether postings listing skills that are not used cause measurement error (a common concern, unconfirmed here); scarcity versus ubiquity beyond the IMF's new-skill definition; any ESCO proficiency or wage data outside the page read.
- Levels.fyi: share of verified data (not stated on pages read).

D) TOP 6 SOURCES

1. https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf.md. IMF, staff discussion note SDN/2026/001 (2026; exact date not shown in the text fetched). Best method and caveat source for posted-wage skill premiums.
2. https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23. Lightcast, 23 July 2025. Vendor headline AI premium (28%); method not disclosed.
3. https://kb.lightcast.io/en/articles/7932720-compensation-model. Lightcast knowledge base, undated. Shows the data inputs (OEWS plus postings); premium method absent.
4. https://levels.fyi/about/. Levels.fyi, undated. Clearest description of tiered verification.
5. https://www.onetcenter.org/dictionary/22.3/excel/skills.html. O*NET Program, release 22.3. Skill rating scales and absence of pay fields.
6. https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/two-pillar-structure-esco. European Commission, ESCO, undated. Pillar structure; no proficiency or wage data on this page.
