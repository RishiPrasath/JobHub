# Singapore job-source coverage registry

Access checks were run through the AgentHub Job Hunt routing on 2026-10-19, using its preferred CloakBrowser path and the `google-agenthub` profile. These checks establish route/readability status only. They do not replace page-level Chrome inventory, prove vacancy prevalence, or prove that a portal is an independent source rather than a syndicator.

## Current inventory versus expanded coverage

The first Chrome inventory covered six ecosystems: Indeed Singapore, MyCareersFuture, FastJobs, Careers@Gov, Jobstreet Singapore and LinkedIn. AgentHub’s catalogue and live probes add broader coverage across general, specialist, recruiter, startup, public-sector and employer-hosted sources.

## General and multi-sector boards

| Source | AgentHub route | Live route result | Coverage role | Next action |
|---|---|---|---|---|
| Indeed Singapore | `indeed-singapore` | already inspected in Chrome | broad commercial board | add comparable detail pages |
| Jobstreet Singapore | `jobstreet-singapore` | already inspected in Chrome | broad commercial board | add comparable detail pages |
| MyCareersFuture | `mycareersfuture` | already inspected in Chrome | government-supported broad board | add detail/page variants |
| FastJobs | `fastjobs` not in current AgentHub catalogue; Chrome inspected | already inspected in Chrome | non-executive/frontline/shift coverage | add detail pages |
| JobsCentral | `jobscentral` | readable, HTTP 200, 23 displayed posts for test query | broad Singapore board | add search/detail pair |
| foundit Singapore | generic `web-page view` | readable, HTTP 200, 3,340 characters | broad board; formerly Monster | add search/detail pair and verify source identity |
| Jobs Lah | generic `web-page view` plus Chrome fallback | root reachable; `/sg` and Singapore search shell readable in Chrome | Singapore-focused/AI-oriented board | count as a readable search/landing source; detail availability remains unknown |
| GrabJobs Singapore | `grabjobs-singapore` | blocked, HTTP 403 | broad/operational candidate source | record as blocked; do not substitute snippets |
| JobsDB Singapore | generic `web-page view` | tested URL returned HTTP 404 | candidate source, route needs confirmation | do not count until a current Singapore route is verified |

## Specialist, recruiter and startup sources

| Source | AgentHub route | Live route result | Coverage role | Next action |
|---|---|---|---|---|
| NodeFlair | `nodeflair` | readable, HTTP 200, 6,553 characters | technology and startup roles | add search/detail pair |
| eFinancialCareers Singapore | `efinancialcareers` | readable, HTTP 200, 2,949 characters | finance/banking specialist | add detail pages |
| Hays Singapore | `hays` | HTTP 301, 1,034 characters, unblocked | professional/recruitment agency | follow redirect and verify detail route |
| Michael Page Singapore | `michael-page` | readable, HTTP 200, 16,933 characters | professional/recruitment agency | add detail pages |
| PERSOL Singapore | `persol-singapore` | HTTP 200 but only 109 characters; Chrome says under maintenance | recruitment agency | record as temporarily unavailable; retry in a later run |
| Wellfound | `wellfound` | readable, HTTP 200, 10,290 characters | startup roles | add search/detail pair; mark Singapore filter semantics |
| YC Jobs | `yc-jobs` | readable, HTTP 200, 8,177 characters | startup roles | add search/detail pair; distinguish remote/location scope |
| Tech in Asia Jobs | `tech-in-asia-jobs` plus Chrome fallback | no structured JSON from probe; Chrome landing readable, detail remained a dynamic shell | Southeast Asian technology/startup source | count landing as readable; detail requires manual/delayed review |

## Public-sector and statutory-board sources

These are separate from general job boards because employer identity, public-service classification and application flows can differ materially.

| Source | AgentHub route | Live route result | Coverage role | Next action |
|---|---|---|---|---|
| Careers@Gov | `careers-gov` | already inspected in Chrome | public-service board | add agency/detail pairs |
| GovTech Careers | `govtech-careers` | readable, HTTP 200, 3,950 characters | statutory/public-sector technology | detail-page sample |
| DSTA Careers | `dsta-careers` | readable, HTTP 200, 3,844 characters | defence technology | detail-page sample where public |
| CSA Careers | `csa-careers` | readable, HTTP 200, 3,455 characters | cybersecurity public sector | detail-page sample |
| MDDI Career Options | `mddi-career-options` | readable, HTTP 200, 1,690 characters | ministry/digital policy | detail-page sample |
| A*STAR Careers | `astar-careers` | readable, HTTP 200, 1,649 characters | science/research | detail-page sample |
| Tech Careers Smart Nation | `tech-careers-smart-nation` | no structured JSON returned | public-sector technology | manual review |
| HTX Careers | `htx-careers` | no structured JSON returned | homeland-security technology | manual review |
| IMDA Careers | `imda-careers` | no structured JSON returned | media/infocomm public sector | manual review |

## Employer and ATS sources

AgentHub’s catalogue also lists direct employer and ATS-style sources. They improve industry depth but should not be counted as independent job boards:

- DBS, OCBC, UOB, Citi, JPMorganChase, HSBC, Maybank, CIMB and Credit Agricole CIB;
- Thoughtworks;
- employer/ATS pages such as Workday, Greenhouse, healthcare employers, statutory boards and recruitment agencies;
- employer-hosted portals already proposed in the sampling specialist’s handoff, including PSA, SingHealth, Micron and People Profilers.

These should form a separate employer/ATS stratum. The same vacancy appearing on a board and an employer site should be linked as one vacancy family where the evidence supports that relationship.

## Status rules

- **Readable:** AgentHub returned a non-blocked page with substantive text; eligible for a Chrome detail-page follow-up.
- **Readable but needs review:** page returned, but redirect, very short text or dynamic behaviour prevents confidence that the listing content is complete.
- **Manual/degraded:** route returned no structured result; use Chrome or generic page-view only if a direct page can be identified.
- **Blocked/unavailable:** access failed or returned a blocking status; record the failure and do not infer page content.

## Coverage decision

For the expanded next pass, treat the following as the primary accessible candidate set:

1. Indeed Singapore;
2. Jobstreet Singapore;
3. MyCareersFuture;
4. FastJobs;
5. Careers@Gov;
6. JobsCentral;
7. foundit Singapore;
8. NodeFlair;
9. eFinancialCareers Singapore;
10. Michael Page Singapore;
11. Wellfound;
12. YC Jobs;
13. GovTech Careers;
14. DSTA Careers;
15. CSA Careers;
16. MDDI Career Options;
17. A*STAR Careers.

Hays, PERSOL, Jobs Lah, Tech in Asia, Tech Careers Smart Nation, HTX and IMDA remain valuable follow-up sources with degraded or partial access status. Chrome confirmed a Cloudflare security-verification page for GrabJobs; JobsDB returned a 404 for the tested Singapore URL. Neither should be treated as a readable vacancy source in this pass.

This source expansion increases coverage by source type and hiring context, not merely by adding duplicated general boards.
