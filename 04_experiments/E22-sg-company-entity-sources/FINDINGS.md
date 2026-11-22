# E22 findings: Singapore company entity sources (run 2026-11-21-run-001)

Small, single run by the agent. 20 real brands, 6 constructed lookalikes. The agent set truth and ran the matcher, so they are not independent. Read the numbers as directions, not rates.

## Headline

- **Name-only matching fails.** The naive rule picked the site-stated entity for **2 of 11** brands with known truth (18%); a post-hoc "companies only" variant got 3 of 11. The protocol's bar was 90%. The true entity was in the name search results for only 8 of 11, because legal names often do not contain the brand (Singtel is Singapore Telecommunications Limited; foodpanda is Delivery Hero (Singapore) Pte. Ltd.).
- **Brands map to groups, not one entity.** Median 12 live ACRA entities share a brand token; CapitaLand has 108, Grab 29. 11 of 20 brands had more than 10.
- **The domain chain reached an ACRA entity for 10 of 20 domains** (bar was 70%). It agreed with the site-stated entity for 3 of 6 where both existed. The 3 disagreements were all *other real entities of the same group* (Sheng Siong Supermarket versus Sheng Siong Group; ST Engineering Management Services versus Singapore Technologies Engineering Ltd; CapitaLand Business Services versus CapitaLand Group). So each source finds the group but not the employing entity.
- **No lookalike was accepted by exact match (0 of 6).** But "DBS Bank Pte Ltd" differs from the real "DBS BANK LTD." only by suffix, so any suffix-insensitive matcher, which is needed to handle real renames, would accept it.
- **The Gazette is fresher than the open data.** All 5 UENs checked from a notice of companies struck off on 20 Nov 2026 still showed "Registered" in the data.gov.sg dataset (updated monthly).
- **MyCareersFuture: blocked by terms.** Not called.

## Per part

### Step 0: terms and robots (Patchright, real Chrome, headed)

All 6 JS-rendered terms pages rendered (HTTP 200, no CAPTCHA). Assessment in `outputs/terms/terms_assessment.json`.

| Source | Automate? | Why |
|---|---|---|
| data.gov.sg ACRA | Yes | API terms: "use ... commercially or non-commercially"; attribution required |
| eGazette | Yes, browse pages and notice PDFs | Clause 11 allows non-abusive automated extraction. `/search` disallowed by robots.txt; not used |
| Bizfile | No | "personal non-commercial use"; written permission needed for any other use |
| MyCareersFuture | No | No automation clause, but "No part ... may be reproduced, stored in a retrieval system ... without written permission from SWDA". robots.txt allows crawling; the terms still bar storage |

### Part A: ACRA name to UEN (data.gov.sg datastore API, no key)

88 calls in the final pass at 3 s spacing, no 429s. Two earlier passes are kept (`acra_pass1_or-search-bug`, `acra_pass2_suffix-search-bug`): a plain `q` search ORs the words, so multi-word brands returned thousands of unrelated rows; a field-scoped `q={"entity_name": ...}` ANDs them.

| Measure | Result |
|---|---|
| Brands with truth found in ACRA | 11 of 20 |
| Naive top-1 correct | 2 of 11 |
| Truth among name search results | 8 of 11 |
| Live entities per brand token | median 12, max 108 |
| Lookalikes accepted by exact match | 0 of 6 |

Other things the run showed:
- **Names drift; UENs do not.** CapitaLand's site gives "CapitaLand Limited (Reg. No. 198900036N)"; ACRA now names that UEN "CAPITALAND GROUP PTE. LTD.". BreadTalk Group Limited (RDAP) is now "BREADTALK GROUP PTE. LTD.".
- **Co-operatives are missing.** NTUC FairPrice Co-operative Limited is not in "Entities Registered with ACRA". Inference: co-ops get UENs from another agency. That needs a second dataset.
- **Sole proprietorships are noise.** "GRAB A PC" and "RAZER CLEAN" were the naive picks. Filter by entity type.
- **The registered address finds the group.** Grab's privacy notice names only its Cayman parent, "c/o 3 Media Close Singapore 138498". Filtering ACRA by that postal code returned 15 Grab entities (GrabTaxi Holdings, GrabCar, GrabInvest and others).

### Part B: Government Gazette

Browse pages rendered with Patchright, with no block or CAPTCHA. Three notices fetched (Companies Act s344A, two notices with 122 and 113 companies struck off; s344, notice of intended strike-off, 2 companies). Each notice lists **UEN plus name**, so it joins to ACRA exactly. One s344 entity is a known brand's subsidiary (Tupperware Brands Asia Pacific Pte. Ltd.), which shows the signal is relevant to employers.

Block recorded: `assets.egazette.gov.sg/robots.txt` returns HTTP 403 (S3 AccessDenied). The reader first treated that as disallow-all and skipped the PDFs. RFC 9309 treats a 4xx robots response as "no rules", and the terms allow extraction, so the 3 PDFs were then fetched once each (deviation 2).

Open point: clause 11 is headed "Reproduction of legislation-Gazettes" but its body says "any e-Gazettes". Get a legal read before storing notices.

### Part C: domain chain (one lookup per domain per service)

| Source | Coverage | Gave an ACRA entity |
|---|---|---|
| SGNIC RDAP | 12 of 12 `.sg` domains returned a registrant (8 of 20 domains are not `.sg`) | 8 |
| Live TLS certificate | 1 EV (DBS: serial number equals UEN 196800306E), 4 OV, 15 DV | 3 |
| crt.sh | 16 ok, 4 HTTP 502. The JSON has issuer and names, not subject organisation, so it added nothing the live certificate did not | 0 |
| Wayback CDX | 20 of 20 gave a first capture (1996 to 2016) | n/a (age signal) |

RDAP failures: foreign registrant (FOODPANDA GMBH), a department label ("GV IT"), renamed entity (BreadTalk), and one registrant that was a **person's name** (redacted, see deviation 3). One OV certificate named a foreign parent (Lazada: Alibaba (China) Technology Co., Ltd.).

### Part D: MyCareersFuture job API

Not tested. The terms were read in a real browser (they render only with JavaScript). They give no permission for automated or API use and bar storage "in a retrieval system" without SWDA's written permission. Whether the API exposes `employer_uen` therefore stays unverified (third-party report only). Next step: ask SWDA for written permission.

### Part E: Patchright on permitted JS pages

Patchright with real Chrome (headed, throwaway profile) rendered every permitted page it was pointed at: 6 terms pages, 18 company home pages, 15 policy pages and 3 eGazette pages. There were no CAPTCHAs, login walls or 429s. 2 company sites (SATS, PropertyGuru) disallow generic agents in robots.txt and were skipped. 14 of 20 sites named some legal entity; 4 named only a foreign parent or a group label (Grab, Razer, Ninja Van).

## Recommended pipeline for confirming the employing entity

1. **Start from a UEN, not a name.** Take the UEN from the posting itself, the offer letter or the company site footer (as Singtel and CapitaLand show). Look up the UEN in ACRA and show its *current* name and status. Accept name drift when the UEN matches.
2. **If there is no UEN, resolve the brand to a group, not an entity.** Use the brand token search (companies only, live only) plus the domain chain: `.sg` RDAP registrant, OV or EV certificate organisation (EV serial = UEN), and the registered postal code from the site's privacy notice. Show the group's entities and say plainly that the employing entity is not confirmed.
3. **Pin the employer with a document from the company's own domain.** Use a privacy policy, footer or offer letter that names the entity, plus a recruiter email on the same domain. Name-only and suffix-only matches never confirm.
4. **Check freshness against the Gazette.** Match the UEN against recent s344, s344A and winding-up notices, because the open data can be a month stale.
5. **Add age and continuity signals.** RDAP registration date and Wayback first capture.
6. **Link out, do not automate:** Bizfile (paid profile), MyCareersFuture (until SWDA permits), MOM and IRAS checks.

## Deviations

1. Docker plus Xvfb was not used: the Docker engine was not running on the host. Patchright ran headed on Windows with installed Chrome instead.
2. eGazette notice PDFs were fetched after a robots.txt HTTP 403, on the reasoning above. The first skip is kept in `gazette/reads.jsonl`.
3. Privacy: one RDAP registrant was an individual's name. It was redacted in `domain_chain/chain_results.json` after the run, and the harness now drops person-like registrants. Admin, technical and billing contacts were never stored.
4. Part A was rerun twice after harness bugs (search semantics, suffix words). The earlier outputs are kept, not overwritten.
5. A "companies only" naive variant was added after seeing results. It is labelled post hoc.

## Limitations

- 20 brands, mostly large and well known; small employers are under-tested. The lookalikes were constructed, not taken from real scams.
- Truth is "the entity the brand's own site names", which may be a parent or data controller rather than the employer for a given job.
- Single run; the agent set the truth and wrote the matcher.
- Not legal advice. The terms readings need review before any data is stored in a product.
