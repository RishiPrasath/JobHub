# Limitations

## The source report was missing

The 4-agent options report this run was meant to check was not in the repository. Claims were re-checked from first principles, so the claim table in `findings.md` is this run's own check. The report's six proposed experiments and four open decisions were also unavailable; the six experiments here (E1 to E6) and the questions asked to the user are this run's own.

## Sample

- 15 postings, 5 industry groups, Singapore only. Not representative of employers or industries generally.
- Eight postings were added by the assistant, not taken from real captured postings, and only their employer names and titles were used. Posting text was not part of any test.
- Employer-specific numbers (for example Wayback years) describe those employers on one day.

## Pricing and terms evidence

- Pricing and terms were read through page fetches and web searches, several of which returned only secondary summaries. These claims rest on secondary sources: GitHub Models retirement, Cerebras trial credits, Serper expiry, Glassdoor/Indeed/JobStreet terms (not checked), the exact Groq free-plan tier of the existing key, and Cloud Run's card requirement.
- Pricing pages change often. Re-check before committing money or architecture.

## Not tested

- **Tavily and Serper**: need a user-created account and key.
- **Brave, Cloud Run deployment, Groq paid tier**: need a card.
- **News, layoffs, turnover, reposting**: GDELT returned 429 for 14 of 15 requests; no substitute was run.
- **Careers and about pages**: only one page per site was read, so hiring questions were mostly unanswered.
- **Answer correctness**: E5 verifies that a quote exists in the page, not that the answer is right. No gold answers or human review were prepared.

## Method weaknesses

- **E1 ground truth**: only four UENs (P01, P02, P07, and P09's neighbouring entity) were cross-checked against an independent web result. The other matches were judged by name and industry. The P11 sibling concern comes from the posting URL slug, not a captured posting.
- **E1 fixes** (live preference, joined tokens, dropping unmatched tokens) were checked by direct lookups, not by re-running the matcher.
- **E2 and E3**: Playwright's extra text was compared by character count only. DHL and Marina Bay Sands may serve different results from another network or with an approved access arrangement; they are "blocked here", not "closed to everyone".
- **E4**: GDELT throttling may be partly caused by repeated probes from the same IP earlier in the session. The first Wayback query form was wrong and was rerun, so Wayback timings include a cleaned-up version of the query.
- **E5**: nine pages, one model, one prompt, `reasoning_effort` low, 30 and 32 claims. The 28% versus 7% difference is suggestive, not statistically tested. The excerpt text was cut to about 6,000 characters, which could drop relevant content.
- A first E1 run against the live ACRA API was abandoned (rate limits, poor matches) and the stray process caused extra 429s for the bulk download until it was stopped. Its console log (`outputs/e1_console.log`) is kept as evidence of that failure.

## Boundaries

- Employer observations are about the entities' public pages and registry records. Nothing here is a statement about any employer's conduct, safety or legitimacy.
- Nothing was published, sent or purchased. Nothing was committed to git.
