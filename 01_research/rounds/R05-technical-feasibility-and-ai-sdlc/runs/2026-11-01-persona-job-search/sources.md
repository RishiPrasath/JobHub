# Sources

Accessed 2026-11-01.

| Source | Use |
|---|---|
| [MyCareersFuture search](https://www.mycareersfuture.gov.sg/search) | Public job search pages read by the seven persona agents; job detail pages read for the collated links |
| ACRA corporate-entity datasets, data.gov.sg | Registry match (27 CSVs, 2,124,508 rows in the container index) |
| Local SearXNG 2026.10.30 (Docker) | Web search for each employer; engines that answered: Google custom search and Brave, until suspended |
| Wayback Machine CDX API | First-capture year for each found site |
| Groq `openai/gpt-oss-120b` | Cited answers to five fixed questions about each readable site |
| Employer websites listed in `research/results.json` | Public pages fetched after a robots.txt check |
| Persona definitions | `_prototypes/02_persona-job-review-v3/data/personas.json` |
| Kimi WebBridge | Local daemon and browser extension used to control the user's browser |

Per-job and per-employer records are in `links/`, `details/` and `research/`.
