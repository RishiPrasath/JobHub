# Source register

Accessed 2026-10-19 in Chrome. URLs are retained as canonical or stable forms where available. “Visible” means observed in the page accessibility/rendered view; it does not imply that all dynamic content was loaded.

| ID | Ecosystem | Page type | URL | Main use | Access result |
|---|---|---|---|---|---|
| R4-JB-001 | Indeed Singapore | job detail | [Application Developer](https://sg.indeed.com/viewjob?jk=9aba925da6377e2e) | office/technical detail structure | visible; compact detail page |
| R4-JB-002 | Indeed Singapore | job detail | [Software Developer](https://sg.indeed.com/viewjob?jk=7de20d25fb8391e6) | comparison detail; partial content | visible; requirements/benefits not visible in inspected content |
| R4-JB-003 | MyCareersFuture | job detail | [Class 4 Driver – Port Delivery Operations](https://www.mycareersfuture.gov.sg/job/logistics/class-4-driver-%E2%80%93-port-delivery-operations-quantum-forward-6e362b2ae87a50d1fd6608e5109fa020) | shift/logistics/public-supported detail | visible; structured sections and platform panels |
| R4-JB-004 | FastJobs | employer support/lifecycle | [Repost an Expired Job Ad](https://support.fastjobs.sg/how-to-repost-an-expired-job-ad-on-fastjobs) | posting lifecycle and expiry language | visible; support page, not a vacancy |
| R4-JB-005 | FastJobs | search results | [Singapore jobs](https://www.fastjobs.sg/singapore-jobs/en/all-categories-jobs/) | search cards, filters and categories | visible; 7,152 jobs and pagination shown |
| R4-JB-006 | FastJobs | job detail | [Vehicle Mechanic](https://www.fastjobs.sg/singapore-job-ad/2636450/vehicle-mechanic/rexy-management-pte-ltd/) | frontline/trade detail structure | visible; pay, shifts, contact and expiry shown |
| R4-JB-007 | Careers@Gov | career landing | [Careers in Singapore Public Service](https://www.careers.gov.sg/) | public-service context and navigation | visible; landing page |
| R4-JB-008 | Careers@Gov | search results | [Public-service jobs](https://jobs.careers.gov.sg/) | listing cards, filters and closing-date fields | visible; 2,130 results and pagination shown |
| R4-JB-009 | Careers@Gov | job detail | [Lead Product Manager – Ministry of Finance](https://jobs.careers.gov.sg/jobs/greenhouse/4007889201) | public-sector detail and application process | visible; Greenhouse-hosted detail |
| R4-JB-010 | Jobstreet Singapore | search results | [Job search](https://sg.jobstreet.com/jobs) | search filters, cards and platform signals | visible; sample cards and filters |
| R4-JB-011 | Jobstreet Singapore | job detail | [Part-Time Admin Assistant](https://sg.jobstreet.com/job/95357572) | office/part-time detail structure | visible; URL/title mismatch observed |
| R4-JB-012 | LinkedIn | search results | [Singapore software-engineer search](https://www.linkedin.com/jobs/search/?keywords=software%20engineer&location=Singapore) | platform signals and search filters | visible after redirect to search-results |
| R4-JB-013 | LinkedIn | job detail | [Software Engineer, Internal Tooling and Infrastructure](https://www.linkedin.com/jobs/view/4476807634/) | detail metadata and access limitation | header visible; body did not render in inspected view |
| R4-JB-014 | GrabJobs | error/blocked | [Software Engineer search](https://grabjobs.co/singapore/software-engineer-singapore-jobs) | fallback access comparison | Chrome security-verification page; AgentHub returned HTTP 403 |
| R4-JB-015 | Tech in Asia Jobs | career/landing | [Tech in Asia Jobs](https://www.techinasia.com/jobs) | startup/technology source structure | Chrome-readable landing page; AgentHub structured probe returned no JSON |
| R4-JB-016 | Tech in Asia Jobs | job detail | [Event Program Manager](https://www.techinasia.com/jobs/857e0199-2123-4514-9090-e91bae17f27a) | detail-page access test | dynamic shell `Currently making magic…`; substantive detail not visible |
| R4-JB-017 | PERSOL Singapore | error/unavailable | [PERSOL search](https://jobs.persolsingapore.com/?q=software+engineer+Singapore) | agency-source access comparison | Chrome page states portal is under maintenance |
| R4-JB-018 | Jobs Lah | career/landing | [Jobs Lah Singapore](https://www.jobslah.com/sg) | Singapore-focused/AI-oriented source structure | Chrome-readable; locale selection and job-search links visible |
| R4-JB-019 | Jobs Lah | search results shell | [Jobs Lah Singapore Jobs](https://www.jobslah.com/sg/jobsearch/singapore-jobs) | search-page access test | Chrome-readable search shell; no result cards visible in inspected state |
| R4-JB-020 | GovTech | employer career landing | [GovTech Careers](https://www.tech.gov.sg/careers/) | direct public-sector employer context | Chrome-readable; links to Careers@Gov application listings |

## Source ownership note

The register records the page ecosystem, not authorship of every field. Field-level ownership is recorded in [page-inventory.md](page-inventory.md). Display on a board is not evidence that the board authored the employer’s description.

## Page-count note

There are 20 page observations, but only 7 are substantive individual vacancy detail pages. The remainder are search, landing, support, blocked, maintenance or partial pages. The pages are not treated as 20 independent vacancies.
