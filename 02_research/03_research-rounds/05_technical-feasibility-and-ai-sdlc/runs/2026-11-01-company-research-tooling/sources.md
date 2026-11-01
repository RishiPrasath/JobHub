# Sources

Accessed 2026-11-01. "Primary" means the vendor or publisher's own page; "secondary" means a third-party summary.

## Pricing and terms

| Topic | Source | Type | Use |
|---|---|---|---|
| Tavily credits | [docs.tavily.com API credits](https://docs.tavily.com/documentation/api-credits) | primary | 1,000 free credits a month, no card, per-call costs |
| Serper | [serper.dev](https://serper.dev) | primary | 2,500 free queries, no card |
| Serper expiry | [apiserpent.com Serper pricing](https://apiserpent.com/blog/serper-pricing-credits-explained), [costbench Serper](https://www.costbench.com/software/web-scraping/serper/free-plan/) | secondary | paid credits expire in 6 months; free expiry unclear |
| Groq limits | [console.groq.com rate limits](https://console.groq.com/docs/rate-limits) | primary | gpt-oss-120b 30 RPM, 1K RPD, 8K TPM, 200K TPD (labelled Developer plan base limits) |
| Groq free plan | [pricepertoken Groq](https://pricepertoken.com/endpoints/groq/free), [benchlm Groq](https://benchlm.ai/free-tier/groq) | secondary | no card on the free plan |
| Cloud Run pricing | [cloud.google.com/run/pricing](https://cloud.google.com/run/pricing) | primary (page body did not load) | Singapore is Tier 2 pricing |
| Cloud Run billing | [Cloud Run setup](https://docs.cloud.google.com/run/docs/setup) | primary | billing must be enabled |
| ACRA open data | [data.gov.sg ACRA dataset](https://data.gov.sg/datasets/d_c0650f23e94c42e7a20921f4c5b75c24/view), [collection metadata API](https://api-production.data.gov.sg/v2/public/api/collections/2/metadata) | primary | Open Data Licence, 27 datasets |
| data.gov.sg rate limits | [guide.data.gov.sg API rate limits](https://guide.data.gov.sg/developer-guide/api-overview/api-rate-limits) | primary (named in the API's 429 message) | unauthenticated limit; key gives more |
| Brave Search API | [Brave quickstart](https://api-dashboard.search.brave.com/documentation/quickstart), [implicator.ai](https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/) | primary and secondary | card required, $5 credit, attribution |
| Bing retirement | [Microsoft lifecycle notice](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement) | primary | retired 11 Aug 2025 |
| Google Custom Search | [firecrawl summary](https://www.firecrawl.dev/blog/google-search-json-api-alternative) | secondary | closed to new customers, transition by 1 Jan 2027 |
| Gemini free tier | [ai.google.dev terms](https://ai.google.dev/gemini-api/terms_preview) | primary | unpaid use may train products; human review |
| GitHub Models | [klymentiev.com](https://klymentiev.com/blog/github-models-shutdown), [developersdigest](https://www.developersdigest.tech/models/free-api/github-models) | secondary | retired July 2026 |
| Cerebras | [benchlm Cerebras](https://benchlm.ai/md/free-tier/cerebras.md), [developersdigest](https://www.developersdigest.tech/rate-limits/cerebras) | secondary | trial credit needs a payment method |
| LinkedIn automation | [LinkedIn prohibited software](https://www.linkedin.com/help/linkedin/answer/a1341387) | primary | crawlers and bots not permitted |
| GDELT | [GDELT API response text](https://api.gdeltproject.org/api/v2/doc/doc), [hackernoon write-up](https://hackernoon.com/lang/zh/building-a-pipeline-to-study-war-coverage-using-gdelt) | primary and secondary | one request per 5 seconds; heavy throttling reported |
| Wayback CDX | [archive.org Wayback API help](https://archive.org/help/wayback_api.php) | primary (not opened; endpoint tested directly) | CDX endpoint behaviour |
| Tavily plans | [tavily.com/pricing](https://www.tavily.com/pricing) | primary | Researcher plan free, 1,000 credits/month, resets monthly, no card |
| Wikidata | [wikidata.org API](https://www.wikidata.org/w/api.php) | primary | `wbsearchentities`, official-website property P856 |
| Free search API landscape | [parallel.ai free search APIs](https://parallel.ai/articles/best-free-web-search-api), [firecrawl free tiers](https://www.firecrawl.dev/glossary/web-search-apis/search-apis-free-tiers-testing) | secondary | Exa and others credit-based; SearXNG engine suspension |

## Pages fetched for the retrieval tests (E2 and E3)

Official sites found by web search, 2026-11-01: palo-it.com, grab.com/sg, amkh.org.sg, sgh.com.sg, hrnetgroup.com, dhl.com/sg-en (blocked), marinabaysands.com (blocked), natureland.com.sg, fairprice.com.sg, littleskoolhouse.com, randstad.com.sg. Raw captures are in `outputs/pages/`.

## Registry data

ACRA Information on Corporate Entities, 26 CSV files, 2,066,468 rows, downloaded 2026-11-01 from data.gov.sg. The files (641 MB) are held outside the repository, in the session scratchpad. Cite as ACRA / data.gov.sg per the dataset page.

## Internal sources

- [Company and role research service idea](../../../../../04_feature-ideas/01_company-and-role-research-service.md)
- [Decision log](../../../../../01_strategy/08_decision-log.md)
- [Open questions](../../../../../01_strategy/09_open-questions.md)
- Prototype 02 link set: `_prototypes/02_persona-job-review-v3/data/job-links.json`
