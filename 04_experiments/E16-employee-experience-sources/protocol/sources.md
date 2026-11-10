# E16 Part A: candidate sources and method

Listed before fetching (extended during the survey: items 9 and 10 were added after the first fetches).

| # | Candidate | Type |
|---|---|---|
| 1 | Glassdoor (reviews, interviews, salaries) | Review site; possible licence/partner route |
| 2 | Indeed company pages (reviews, Q&A) | Review site; API route? |
| 3 | JobStreet by SEEK company reviews | Review site; API route? |
| 4 | Reddit (r/singapore, r/askSingapore, career threads) | Public forum with Data API |
| 5 | Blind (teamblind.com) | Anonymous employee forum/reviews |
| 6 | Google Maps reviews via Places API | Licensed API (paid) |
| 7 | HardwareZone forums (Singapore) | Local public forum |
| 8 | TAFEP and MOM official material | Official sources (also E14) |
| 9 | Licensed or partner data (Glassdoor partner API, third-party dataset resellers) | Licensed data |
| 10 | Job-seeker contributions to JobHub | Own data |
| 11 | Link-out only | No reading |

For each: record terms, API/licence route, robots rules, cost, and what is permitted (read, summarise, quote, store, show) BEFORE any content fetch. Only terms pages, robots.txt and API documentation were fetched. No review page, company page or forum thread was fetched in this experiment.

Classification: A = permitted for the intended use; B = link-out only; C = not permitted for the intended use; D = unresolved, needs a provider conversation.

"Intended use" (defined in thresholds.md): a server-side service reads review text, summarises it with attribution to individual accounts, stores it at least transiently, and shows the summary to a job seeker.

Method limits: pages were read through a fetch tool that returns a model-written extract of the page, not the raw text, so quotes are short phrases reported by that tool. Where the tool could not read a primary page (HTTP 403, 404, or host blocked), the primary text is recorded as NOT READ and any claim rests on secondary reports, labelled as such.
