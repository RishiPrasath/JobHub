# DRAFT: Free and legal Singapore pay data for FEAT-009 (Pay benchmark)

Checked 21 Nov 2026 by reading each live page in a browser. **V** = verified (read directly or pulled live). **I** = inferred. Not legal advice. Nothing committed to git.

## Verdict

**FEAT-009 is feasible at occupation level, using MOM's Occupational Wage data from data.gov.sg.** That copy is under the Singapore Open Data Licence, which allows commercial use and storage with attribution. **MyCareersFuture is not usable** for salary data, either through its API or its website, unless SWDA (the Skills and Workforce Development Agency) gives written permission. The posting's own pay must come from the user's paste (FEAT-005).

**Recommended scope:**
1. Use MOM OWS June 2025 (Occupational Wage Survey, June 2025 reference month) for the 25th percentile, median and 75th percentile of monthly gross wage. That means 523 occupations across all industries, plus a version by industry. The user confirms the occupation from a shortlist that includes "none of these". On "none", show no benchmark.
2. Use the SSOC 2024 (Singapore Standard Occupational Classification) Detailed Definitions from SingStat for the duty text on the choice screen. This fixes the gap found in E17, where the MOM table has no duties.
3. Take the posted range only from text the user pasted. Show where its midpoint falls. Always show the basis and the attribution line.
4. Optional: use MOE's Graduate Employment Survey for fresh graduates (by degree).
5. Out of scope: company-level or job-title-level pay. No free and legal source exists for it. MCF has it but forbids reuse, and Glassdoor and others forbid scraping.

## Sources

| # | Source | Data and granularity | Licence or terms | Access | Updates | V/I |
|---|---|---|---|---|---|---|
| 1 | **MOM OWS on data.gov.sg**: [Resident Occupational Wages, June 2025](https://data.gov.sg/datasets/d_9917e751f7498502f70052a940a3f312/view) | 523 occupations. Basic and gross wage at the 25th percentile, median and 75th percentile. Title text only, with no SSOC code column | The dataset page links the [Open Data Licence](https://data.gov.sg/open-data-licence): you may "use, access, download, copy, distribute... whether commercially or non-commercially". Requires a "conspicuous notice acknowledging the source" and must not suggest official endorsement | `datastore_search` API without a key (4 calls per 10 s) or the `poll-download` CSV ([limits](https://guide.data.gov.sg/developer-guide/api-overview/api-rate-limits)) | Annual. Coverage is June 2025. Last updated 18 Nov 2026 | V |
| 1a | Same series, other cuts: [by industry](https://data.gov.sg/datasets/d_523d376ff1d501a338add925f3313fd1/view) (1,579 rows), [by sex](https://data.gov.sg/datasets/d_d1e7ac04e9e121c9bbced9cb4a7e91d5/view), [by establishment size](https://data.gov.sg/datasets/d_7d528712f1fd454ac6ca32fe06fe8f12/view), [by age and size](https://data.gov.sg/datasets/d_db0e6e9b54364552dd9d2fc6a28f14f0/view), [within major groups](https://data.gov.sg/datasets/d_670c3c6cecbcd24e48034a3428bd306e/view) | Industry cut has percentiles. The other cuts give the median only | Same licence | Same | Same | V |
| 2 | **MOM stats site**: [OWS 2025 tables](https://stats.mom.gov.sg/publications/statistical-tables-occupational-wages-2025/) (XLSX, released 30 Jun 2026) | Same figures **plus SSOC 2024 codes** | [MOM terms](https://www.mom.gov.sg/terms-of-use): "no part of The Website may be reproduced or reused for any commercial purposes whatsoever without our prior written permission". Caching is prohibited | Direct XLSX; robots.txt allows everything except /search | Annual | V |
| 2a | MOM [Salary Comparison tool](https://eservices.mom.gov.sg/statshare/benchmarking/salary-comparison/individual) | Job title, salary and industry give a position against OWS | Has a terms checkbox and falls under MOM terms. Link-out only | Interactive | Annual | V |
| 3 | **Labour Force Survey** on data.gov.sg: [income by occupation and sex](https://data.gov.sg/datasets/d_16fdf439f84527f2ecfcee193a8ea567/view) | 9 major occupation groups × income bands × sex, 2010 to 2025 (counts, not percentiles) | ODL | API or CSV | Annual. Updated 27 Mar 2026 | V |
| 4 | **SingStat Table Builder**: for example [M920131](https://tablebuilder.singstat.gov.sg/table/TS/M920131) (median income by occupation group and sex) and M182941 (average earnings) | Major occupation groups or the whole economy only | [SingStat terms](https://www.singstat.gov.sg/terms-of-use) allow copying and building products "for sale or otherwise" with credit, and datasets fall under the ODL. **But** clause 25 requires written permission even to hyperlink | Open JSON API `/api/table/resourceid` and `/api/table/tabledata/{id}`. robots.txt allows all | Annual or quarterly | V |
| 5 | **SSOC 2024** from [SingStat](https://www.singstat.gov.sg/standard-classifications/national-classifications/singapore-standard-occupational-classification-ssoc): Detailed Definitions XLSX, Alphabetical Index, and SSOC 2020 correspondence | Per 5-digit code: title, definition, tasks, examples, and "see code" exclusions (for example, "Data analyst, see 21231") | SingStat terms, as above | XLSX download | Per edition | V |
| 6 | **MOE Graduate Employment Survey** on [data.gov.sg](https://data.gov.sg/datasets/d_3c55210de27fcccda2ed0c63fdd2b352/view) | 1,550 rows: university, school, degree. Gross 25th percentile, median and 75th percentile, and employment rate, 2013 to 2024 | ODL | API or CSV | Annual. Updated 5 Mar 2026 | V |
| 7 | **MyCareersFuture** (site and `api.mycareersfuture.gov.sg/v2/jobs`) | Per posting: `salary {minimum, maximum, type}`, `ssocCode` (SSOC 2020), position level, employer. Company-level posted pay | **Barred**: see below | Undocumented and public. No key, no published API terms | Live | V |

## MyCareersFuture: exactly what is and isn't allowed

The [terms](https://www.mycareersfuture.gov.sg/terms-of-use) (last updated 19 Nov 2026) were read in full **(V)**:
- **Clause 7:** visitors get a "personal, non-transferable... licence to access and use the Services... solely within the scope of your status as a Visitor".
- **Clause 5:** you will not "reproduce, distribute, publicly display... communicate to the public, create derivative works from or otherwise use and exploit any Website Content".
- **Clause 15:** no part "may be reproduced, stored in a retrieval system, or transmitted in any form... without written permission from SWDA".
- **Clause 11:** "caching and links to, and the framing of this website... is strictly prohibited". Written permission is needed even to hyperlink.
- **Clause 16:** content may not be "reproduced, republished... transmitted, adapted... without the prior written permission of SWDA".

The [robots.txt](https://www.mycareersfuture.gov.sg/robots.txt) blocks only `meta-externalagent` and allows everything else **(V)**. The API host has no robots.txt (it returns 404) **(V)**. robots.txt only controls crawling. It does not grant a licence, so the terms still govern use.

**What this means (I):**
- **Storage or bulk harvest:** barred by clause 15 (no storing in a retrieval system).
- **On-demand lookups through the API, shown to a JobHub user:** still barred. Displaying or transmitting salary fields to someone else is "publicly display", "communicate" or "transmit", and that goes beyond a visitor's personal licence. Calling the API without storing anything does not get around this.
- **Salary fields specifically:** the terms make no exception for them.
- **The user's own copy:** a user who reads a posting and pastes it into JobHub is supplying their own input, and JobHub only analyses it. This is the route the project already uses (FEAT-005) and the one this report recommends.
- **Link-outs:** even linking needs written permission under clauses 11 and 33. MOM's terms say the same for internal pages, and so does SingStat's clause 25. The earlier "link-out only" rule therefore carries a small risk. Showing the URL as plain text instead of a clickable link, or asking for permission, would lower it.
- **Path to unlock:** ask SWDA in writing. The contact on the terms page is 6669 7932. The data would be valuable: one live call showed each posting carries an `ssocCode` (for example `21222`, SSOC `2020v3`), which would make automatic occupation matching close to exact.

## Test pulls (live, 21 Nov 2026, V)

- `datastore_search` on `d_9917e751…` returned total 523. All percentile cells were numeric, with none suppressed. Sample rows:
  - Statistical officer/data analyst: gross 25th percentile 4,561, median 5,869, 75th percentile 7,375.
  - Software developer: gross 25th percentile 5,994, median 7,808, 75th percentile 11,092.
- `poll-download` returned `DOWNLOAD_SUCCESS` with a signed CSV URL valid for 1 hour.
- Full-text `q=` search is **not** supported on this dataset. Use `filters={"occ_desc": …}` or pull all 523 rows.
- The sorted, lowercased data.gov.sg titles have the same SHA-256 as the 523 titles in the local MOM XLSX extract (`73d8199a…`). The two sources match 1:1, so SSOC codes can be joined by title.
- SSOC 2024 Detailed Definitions XLSX was parsed in the browser. It has 7,176 strings, with Title, Definition, Tasks and Notes per code.
- MCF: one read-only call during normal browsing confirmed the field names, and nothing was stored. No bulk calls were made.
- The Python sketch is at `strategy/evidence/external/pay-sources/DRAFT_ows_benchmark_sketch.py`. It was run offline against the E10 snapshot and gave the same numbers as the live API, plus "none" returning no benchmark and the attribution line. Online mode was **not** run, because this machine's shell has no internet access.

## Data limits to show as the basis (V, from the dataset notes)

- Covers full-time **resident** employees only, in private establishments with **at least 25 employees**.
- Gross wage **excludes bonuses** and employer CPF (Central Provident Fund) contributions.
- Reference month June 2025, so about 1 to 1.5 years old when shown.
- Occupation level only: no seniority, no company, no job title.
- Covers 523 common occupations, so some jobs will get "none of these".

## Changes since earlier project notes

- The old MOM URLs (`stats.mom.gov.sg/Pages/Occupational-Wages-Tables2025.aspx` and the `/SL/` page) now return 404. The site was redesigned and the tables are at the new publications URL above **(V)**.
- MOM's OWS is now on data.gov.sg under the ODL, last updated 18 Nov 2026. This removes the MOM-terms barrier that applied to the XLSX **(V)**.
- The MCF terms have now been read, which closes the open question in `DRAFT_sg-company-data-free-legal-sources.md`.
