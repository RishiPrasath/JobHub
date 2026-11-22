# DRAFT: Free and legal ways to research a Singapore company

> **Status: draft, not reviewed.** Not a scope or architecture decision. Nothing here has been checked by a lawyer.
> Interpret it into `05_technical-direction.md` or `08_decision-log.md` before treating it as a requirement.

| Field | Value |
| --- | --- |
| Source | Research doc [Researching a company in Singapore: sources and entity verification](https://claude.ai/artifact/55zVs9TY3XSYaUmiXqDxPV) |
| Date | 21 Nov 2026 (pages opened by research agents that day) |
| Question | Which company-research sources can JobHub use for free, by API or scraping, without breaching terms? |
| Informs | Employer verification features (entity match, conduct signals) and any data-ingest design |
| Scope | Free options only. Paid routes (ACRA API Marketplace, resellers, Google Places) are left out. |

**Verification key** (from the source doc): **V** = the linked page was opened and read. **I** = rests on search results, a third-party source or reasoning.

## 1. Safe to automate and store

| Source | What you get | Access | Terms | Status |
| --- | --- | --- | --- | --- |
| [ACRA: Entities Registered with ACRA](https://data.gov.sg/datasets/d_3f960c10fed6145404ca7b821f263b87/view) | About 2.1M rows: UEN, status, name, type, issue date, street, postal code | One 224 MB CSV, updated monthly on the 16th | [Singapore Open Data Licence](https://data.gov.sg/open-data-licence): commercial use allowed with attribution; no rights over personal data | V |
| [ACRA Information on Corporate Entities](https://data.gov.sg/collections/2/view) | 53 columns: SSIC codes, full address, annual return and accounts dates, officer count, up to 15 former names, auditors. **No officer names.** | 27 CSVs, monthly. Datastore API with no key at about 4 calls per 10 s, or 20 with a free production key ([limits](https://guide.data.gov.sg/developer-guide/api-overview/api-rate-limits)) | Same licence. [API terms](https://data.gov.sg/privacy-and-terms) forbid disrupting the servers | V |
| [Government Gazette](https://www.egazette.gov.sg) | Winding-up and strike-off notices | Notices | [Terms](https://www.egazette.gov.sg/terms-of-use/) cl. 11 allow reproduction with credit and non-abusive automated extraction | V |

## 2. Single on-demand lookups only (do not bulk-harvest)

| Source | What you get | Limits | Status |
| --- | --- | --- | --- |
| [SGNIC RDAP](https://rdap.sgnic.sg/rdap/) | Registrant name and domain registration date (domain age). Not the UEN. | [WHOIS policy](https://prod.sgnic.sg/docs/default-source/policies-and-agreements/whois-policy.pdf) 5.1 bans bulk access and marketing use | V |
| Certificate Transparency logs (e.g. crt.sh) | OV and EV certificates carry the verified legal name; EV also carries a registration number, which in Singapore is the UEN | Open. Most sites use DV certs with no organisation name (I) | Fields V ([CA/B Forum](https://cabforum.org/working-groups/server/extended-validation/certificate-contents/)) |
| [Wayback Machine](https://archive.org/help/wayback_api.php) | Old About pages; whether the site existed earlier | Free Availability and CDX APIs. No usage terms stated, so keep the rate polite. Coverage is patchy | V |

Note on `.com.sg`: [SGNIC rules](https://prod.sgnic.sg/docs/default-source/policies-and-agreements/rules-of-registration.pdf) 8.2 expect applicants to be registered with ACRA or similar, so a `.com.sg` domain suggests, but does not prove, a registered business (V).

## 3. Unconfirmed

| Source | Finding | Status |
| --- | --- | --- |
| [MyCareersFuture](https://www.mycareersfuture.gov.sg/) | No documented public API. Third-party scrapers report `api.mycareersfuture.gov.sg/v2/jobs` is open and returns `employer_uen` and `hiring_company_uen` ([Apify listing](https://apify.com/jungle_synthesizer/mycareersfuture-jobs-scraper.md)). The [terms page](https://www.mycareersfuture.gov.sg/terms-of-use) renders only with JavaScript and has not been read. | UEN field: I (strong). Terms: not verified. **Do not automate until terms are read in a browser.** |

## 4. Link out only (no scraping, no storing)

| Source | Why not automate | Status |
| --- | --- | --- |
| [MOM EA Directory](https://service2.mom.gov.sg/eadirectory/) | [MOM terms](https://www.mom.gov.sg/terms-of-use) cl. 6 to 7 bar caching, framing, deep links without permission and commercial reuse | V |
| [MOM work pass check](https://www.mom.gov.sg/check-wp) | CAPTCHA "to prevent data harvesting" | V |
| [IRAS GST search](https://mytax.iras.gov.sg/ESVWeb/default.aspx?target=GSTListingSearch) | CAPTCHA on every search; [IRAS terms](https://www.iras.gov.sg/IRASHome/terms-of-use/) bar reproduction and caching | V |
| [MAS Financial Institutions Directory](https://www.mas.gov.sg/directories) | [MAS terms](https://www.mas.gov.sg/terms-of-use): personal, non-commercial use only | V |
| LinkedIn | Most API access needs partner approval; hiQ v. LinkedIn ended with an injunction and data deletion ([ZwillGen](https://www.zwillgen.com/alternative-data/hiq-v-linkedin-wrapped-up-web-scraping-lessons-learned/)) | API and case V; [User Agreement](https://www.linkedin.com/legal/user-agreement) not opened |
| [Glassdoor](https://www.glassdoor.sg/about/terms.htm) | Section 4.3(16) bars scraping without written permission | V |
| [JobStreet / SEEK](https://sg.jobstreet.com/terms) | Clause 7(d) bans data mining, robots and screen scraping | V |
| [Indeed](https://www.indeed.com/legal) | Publisher job-search API closed; terms ban some automation | Partly V |
| [Glints](https://glints.com/sg/about/terms) | Terms bar automated collection (per source doc) | See source doc |
| Reddit | Public data use now requires a contract ([TechCrunch](https://techcrunch.com/2024/05/09/reddit-locks-down-its-public-data-in-new-content-policy-says-use-now-requires-a-contract)) | Data API terms not read |
| HardwareZone | Terms not read; treat as link-out | Not verified |

## 5. Ask permission first

| Source | What it has | Why ask | Status |
| --- | --- | --- | --- |
| [MOM WSH demerit list](https://www.mom.gov.sg/orca/list-of-companies-with-demerits) and [Business Under Surveillance list](https://www.mom.gov.sg/-/media/mom/documents/safety-health/reports-stats/list-of-companies-under-bus.pdf) | Firms with safety demerits or under surveillance, keyed by UEN | Restricted by MOM terms | V |
| [CPF convicted employers PDF](https://www.cpf.gov.sg/content/dam/web/employer/compliance-and-rectifications/documents/Employers%20Convicted%20under%20the%20Central%20Provident%20Fund%20Act.pdf) | 116 employers convicted on CPF payment, no UEN (name match only) | Terms not checked | V (content) |
| [MAS Investor Alert List](https://www.mas.gov.sg/ial) | 924 unregulated entities | Terms restrict reproduction; robots.txt crawl delay 2. [OpenSanctions mirror](https://www.opensanctions.org/datasets/sg_mas_investor_alert/) is CC BY-NC (non-commercial) | V |

## Caveats

- **Free means no officer names.** Officers and shareholders come only from the paid ACRA API Marketplace or a licensed reseller.
- **A UEN match alone is not proof.** Scammers copy real names, UENs and EA licence numbers. The strongest check is the UEN on a document served from the company's own domain, plus a recruiter email on that same domain.
- **Get legal review** before storing any content from sites whose terms bar reproduction.

## Open questions

- Do the MyCareersFuture terms permit use of its job API?
- Would MOM grant permission to reuse the WSH and EA data?
- Read the LinkedIn User Agreement, Reddit Data API terms and HardwareZone terms in a browser.
