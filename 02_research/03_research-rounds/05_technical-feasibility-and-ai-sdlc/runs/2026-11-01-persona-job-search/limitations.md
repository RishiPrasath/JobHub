# Limitations

## Sample
- 34 postings from one job board (MyCareersFuture) on one day, from seven persona searches of three terms each. Not representative of the job market, of Singapore employers, or of what a real job seeker would search.
- Agents chose their own search terms and which five results to keep, so selection reflects model judgement. Sorting was by newest posting.
- Employers were small and mid-size on purpose; large employers are under-represented.

## Browser access
- Only MyCareersFuture was used. LinkedIn, Indeed, Glassdoor and JobStreet were deliberately left out.
- Seven job-detail pages timed out on every attempt with no cause found, so detail coverage is 27 of 34.
- The browser tabs opened by the agents were left open.

## Company research
- **Hand review is mine.** Which sites are "official" and which are "doubtful" is my judgement from the URL, page title and answers. It was not confirmed with the employers or from the registry. No gold answers exist.
- **Final site numbers use replayed search results**, saved from an earlier pass and limited to the top five per query. The live search could not be rerun because SearXNG's engines were suspended.
- **Rules were tuned on these same 34 employers** after seeing failures, so the final numbers are a repair, not an unbiased estimate.
- SearXNG depends on Google's custom-search endpoint and Brave answering; both throttled quickly, and Google has said its Custom Search JSON API closes on 1 January 2027.
- One page per site was read, so hiring and careers questions were mostly "not found".
- Answers were spot-checked for employer type and description only. A verified quote proves the text exists on the page, not that the page belongs to the right company.
- Groq calls were paced to stay under the free-tier token limit; no cost was incurred.

## Not done
- No user confirmation flow for the five ambiguous registry matches.
- No postal-code or UEN cross-check between the job page, the registry and the company site.
- No news, layoff or turnover research.
- Nothing about whether any employer is good or bad was concluded, and nothing here is a verdict on any employer.
