# P06: Employee reviews card (FEAT-008)

Builds what [decision 0005](../../06_scope/decisions/0005-second-build-scope.md) put in scope for [FEAT-008](../../03_features/FEAT-008-employee-experience.md). Python 3.10+, standard library only.

| Part | What it does | Status |
|---|---|---|
| Link-outs | One-click links to Glassdoor, Indeed, JobStreet and Google Maps for the employer. JobHub never fetches these sites. | Built. Google Maps uses Google's documented URL format; the other three patterns need a person to click-check them (`check-page`). |
| TAFEP Tripartite Standards | Downloads TAFEP's public adopters list once, indexes it by UEN, returns "Adopted N of 10 standards" with the caveat that it is a pledge, not reviews. | Built and tested on a fixture of real rows. The live download runs on your PC (`fetch-tafep`); it has not run from Python yet. |
| NodeFlair | Probe that reads robots.txt, waits 6 s between requests, and keeps only the aggregate count and rating from the page's JSON-LD. Never shown in the product. | Built; parser tested on the live page's JSON-LD shape. Not yet run from Python. |

Input is FEAT-001's output: UEN, registered name, and the brand when known. The brand matters: `GRABTAXI PTE. LTD.` is reviewed as "Grab".

## Commands

```
python -m unittest discover -s tests
python cli.py fetch-tafep
python cli.py card --uen 201324745D --name "GRABTAXI PTE. LTD." --brand Grab
python cli.py card --uen 196800306E --name "DBS BANK LTD." --tafep data/fixtures/tafep_sample.json --json
python cli.py check-page link-check.html --uen 196800306E --name "DBS BANK LTD." --brand DBS
python cli.py nodeflair-probe grab dbs-bank
```

`data/cache/` holds the downloaded TAFEP list and is git-ignored.

## Run notes (2026-11-22)

Read through Claude's built-in browser on the owner's PC, because the cloud container and the device shell have no internet. One request per source, no login, nothing worked around.

**TAFEP** (verified live): the list JSON returned HTTP 200, 19.2 MB, 60,030 rows, 21,116 UENs, no blank UENs, 2 UENs in an unusual format (`T05FC6804`, `T07LL0061`). 60,029 rows Active, 1 Rescinded. Latest update 20 Nov 2026. Standards per employer: 1 standard 9,224; 2: 4,669; 3: 1,427; 4: 1,237; 5: 1,055; 6: 896; 7: 630; 8: 1,060; 9: 492; 10: 426. Most adopted: Age-Friendly (13,387) and Flexible Work (13,285). The old list page URL now returns 404; the current public page is `tal.sg/tafep/getting-started/progressive/tripartite-standards-adopters`. The fixture `data/fixtures/tafep_sample.json` is the 34 live rows for the 8 sample employers plus the one rescinded row.

**NodeFlair** (verified live): robots.txt still allows `/` for all agents with `search=yes, ai-train=no, use=reference`. Grab and DBS reviews pages returned HTTP 200 in 22 s and 7 s. The server HTML holds the aggregate (Grab 556 reviews, 4.0; DBS 396, 3.8), but no review cards, dates or "From Other Platform" labels: those load in the browser later. So a plain Python fetch gets the totals only; review dates would need a headless browser. Inferred: Cloudflare may treat a Python client differently from a browser; untested.

**Not done:** clicking the barred sites' links to check the patterns, because JobHub may not visit them with automation. A person should open `check-page` output once.
