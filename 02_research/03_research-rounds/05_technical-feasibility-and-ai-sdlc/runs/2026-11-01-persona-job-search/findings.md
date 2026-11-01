# Findings

**Short answer:** the pipeline works end to end on real, unfamiliar employers, and gives usable results for roughly two thirds of them. It also produced confident wrong answers that only a human check caught, and its search source throttles after about two dozen queries. It is a promising prototype, not a reliable service.

## 1. Persona search (Kimi WebBridge)

- Seven persona agents ran in parallel, each in its own browser tab group, three searches each. All finished without a block or CAPTCHA. Each kept 5 links (one persona kept 4 after de-duplication): **35 picked, 34 unique** in `links_all.json`.
- Mix by the agents' own guess: 20 direct employers, 12 recruitment agencies, 2 unclear.
- One bug: job titles with emoji crashed the helper under Windows' default encoding. Every agent noticed, retried with UTF-8 and reported it; fixed in the helper.
- Agents picked relevant roles by title. Search results often contained off-topic padding, so judging relevance did need an agent, not just a script.

## 2. Job details

- **27 of 34 detail pages read** after three passes. Seven timed out every time (J10, J15, J21, J22, J23, J26, J28), while the same method worked for the rest; the cause was not found. A first pass read only 17.
- Median 4,300 characters per page; all contain responsibilities, requirements, skills, posting and closing dates, and an "about the company" block. Pay and working hours appear in under a third.
- The pages print the workplace address with postal code (for example "47 MEYER ROAD 438662"). **Only 1 of 27 printed a UEN and none linked to a company page**, so the job page cannot supply the registry key. A useful side finding: MyCareersFuture company pages that appear in search results carry the UEN in their address (for example `sunnyhill-ace-202227941Z`), which could verify registry matches.

## 3. Company research service (34 unique employers)

The final run replayed the saved search results through the corrected rules (see section 4 for why).

| Step | Result |
|---|---|
| Registry (ACRA) | **28 exact**, 5 needs-confirmation (Recruit Express, Coffee Club, Kyndryl, Randstad, Singtel: sibling entities share the name), **1 unresolved** (CPF Board is a statutory board, not in the corporate datasets) |
| Official site found | **23 of 34** (20 verified, 1 probable, 2 found but unreadable). 11 not found |
| Page readable | 21 (19 fully, 2 thin); 2 sites refused our fetch (Tiong Bahru Bakery returned 429; China Construction failed) |
| Site history (Wayback first year) | 20 of 23 |
| Cited answers (5 questions each) | 20 employers answered: **73 supported**, **3 rejected** for unverifiable quotes, 24 not found, of 100 |
| Time | about 7.5 seconds per employer, excluding the Groq pacing pause |

By persona (employers / site found / page read): technology 5/4/4, service 5/4/4, career change 5/4/4, culinary 5/3/2, office admin 5/3/2, trade 5/3/3, healthcare 4/2/2. Small employers (clinics, kitchens, small agencies) are the hardest, as expected.

### Where it worked
- Large and mid-size employers and agencies: Persol, NUHS, Randstad, Activate Interactive, Kyndryl, Temp-Team, Charterhouse, Paris Baguette, Recruit Express, Ban Leong Pawnshop. Right site, readable page, mostly 3 to 5 supported answers, employer-type answers that match the job card (agency or direct).
- Correct refusals: Avanguarde, Capen Marketing and Sunnyhill Ace were not matched to similarly named companies (Avant-garde Services, Kele pineapple tarts, SunnyHills cakes). Their results are "registry record only", which is the honest outcome.
- Tiong Bahru Bakery: site found, fetch refused (429), reported as found-but-unread rather than as a company with nothing to say.

### Where it failed or is doubtful (hand review)
- **Singtel: site missed.** The top five results were finance and news pages, so no official site was found for one of Singapore's best-known employers.
- **Possible wrong sites that passed:** Coffee Club (`ocoffeeclub.com`, probably a different chain), Recruit Avenue (`searchavenue.com.sg`, a different name), AIM Recruit (`aimrecruit.sg`, the site describes connecting artists), Aber Care (`abercare.sg`, the answer says it is a recruitment agency, which does not fit a senior-care centre job), China Construction (the parent group's site, not the Singapore entity).
- **Citation checking cannot catch a wrong site.** A real quote from the wrong company still passes. The 3 rejected quotes show the check works for fabrication; the wrong-site cases show what it does not cover.
- **Five of 34 registry matches** needed user confirmation. That is the intended behaviour, but a user flow for confirming has not been built.

## 4. Problems found while running, and what changed

1. **Name matching was too weak.** The first rule accepted any page where the company's name words appeared, which let through a Business Times article, Yahoo Finance for Singtel, two directories, a booking page and an industry-body profile. Adding domains to a skip list just moved the problem (the next results were a Brex page, a mall directory, a CNA video and a broker note). The replacement is structural: the URL must look like a homepage (no `/news/`, `/shop/`, `/company-details/` and similar), and either a distinctive name word is in the domain or the path is shallow.
2. **The cache was poisoned.** The weak rule had saved five non-company pages as "verified" sites keyed by company ID. They were purged and the cache rebuilt. A cache of wrong answers is worse than none.
3. **Unreadable pages were discarded** (Tiong Bahru Bakery), then over-accepted (Kele for Capen Marketing, a Practo listing). Now accepted only when the search title carries the full name and the domain carries a name word.
4. **SearXNG throttled.** On a second full pass of 34 queries (about 80 queries in the hour), Brave, DuckDuckGo and Google custom search were all suspended and the service returned no results for the last 11 employers. The final run therefore replayed saved search results instead of querying again. Search is a budget, which makes the cache essential.
5. **Windows path conversion** broke Docker volume paths in Git Bash; solved with `MSYS_NO_PATHCONV=1`.

The replay means the final site-discovery numbers come from search results saved earlier, using only the top five per query.

## 5. Does the experiment work?

- **Yes, for the shape of the service:** persona agents found real jobs; the employer pipeline produced a registry match, a site, a history signal and cited answers, in a container, with no paid service.
- **Not yet, for trust:** site discovery is the weak link. About 4 of 23 found sites are doubtful, and wrong sites produce fluent wrong answers. Registry matching is the strongest part.
- **Cheapest improvements, in order:** (1) use the MyCareersFuture company page's UEN to confirm the registry match and its address and postal code to confirm the site; (2) show the user the site and the registry entry together and ask them to confirm before answers are shown; (3) add a second page per site (about, careers); (4) cache every confirmed pair and treat search as a limited budget.
