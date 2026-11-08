# Findings: experiments X0 to X3 (2026-11-07)

Protocols and thresholds were committed before running (see protocols/). Deviations are listed at the end.

## Summary
| ID | Result against the pre-registered bar |
|---|---|
| X0 source audit | Only 2 of 7 official sources were readable by machine (MAS, CASE). 12 known-problem organisations, not 20. |
| X1 fixed sweep vs free-form | FAIL. Both arms found 12 of 12. The sweep did not beat free-form by 15 points, so the hypothesis is not supported. The test was too easy to separate them. |
| X2 brand to legal entity | PASS. Registry plus web step: 9 of 12 correct (75%), 1 wrong, 2 unresolved. Registry alone: 1 of 12. |
| X3 pay vs official table | INCONCLUSIVE. 46 of 60 postings got a real occupation (77%, bar 80%); 42 of 60 (70%) judged good fits (bar 70%). |

## X0 (outputs/x0/source-audit.md)
MAS enforcement actions and CASE alerts are readable and not prohibited for plain reads (MAS asks for no more than one request per 2 seconds and bars reproduction). PDPC, SGX and the judiciary pages did not load a list; the MOM directories were not found; eLitigation was down for maintenance. Consequence: a red-flag check built on official lists today covers financial regulation (MAS) and consumer complaints (CASE) only, not employment (no MOM employer list, no PDPC list). Retry PDPC with a rendering fetch, and the MOM and court sources, later.

## X1 (data/x1_companies.json, outputs/x1/)
- Known problems found: Arm A (6 fixed queries, then a reader) 12 of 12; Arm B (free-form agents, up to 8 searches) 12 of 12. In Arm A the official page itself came up in the results for 9 of 12 companies, and a news or regulator report for all 12.
- Pre-registered pass needed Arm A to beat Arm B by 15 points. It did not (0 points). Hypothesis not supported.
- Why this is weak evidence: all 12 issues are recent (2022 to 2026) and heavily reported, and the companies were taken from the newest entries on the official lists, so any reasonable search finds them. The earlier agent test showed a miss on a harder case (an insurer's adviser arm); this set had none. A harder test would use older, less-reported or smaller-company entries.
- Controls (not on the lists, so not proven clean): both arms found real, supported items for Koufu (police probe of its app, food-safety complaints) and Sheng Siong (laundering misuse of its teller machines, a civil suit); these are not employment findings. Arm B also reported US-parent legal matters for Kyndryl Singapore, where Arm A showed nothing. Scam-impersonation warnings appeared for Temp-Team, Randstad and Persol; those are warnings about the brand being impersonated, not misconduct. No unsupported claim was found in either arm, but a reader could misread these as red flags about the employer, so presentation matters more than search method.
- Cost: Arm A 120 searches at about 30 seconds each (about 65 minutes in sequence, within OpenSERP's rate limit); Arm B about 30 to 40 searches per 5 companies, with several failed page reads.
- Caveats: Arm A readers saw only titles and snippets; Arm B agents read some pages, and some Arm B facts came from snippets because the fetch step failed. Sir Money Changer and Bsquared had licences revoked, so they may no longer employ anyone.

## X2 (data/x2_groundtruth.json, outputs/x2/RESULT.md)
- Ground truth could be established for only 12 of 36 brands (the rest: operator not named on reachable own pages, blocked pages, or no registry match). For a job seeker this means the brand's own site often cannot answer "who is my employer".
- Registry alone: 1 of 12 correct. Wrong or misleading: Grab matched a cancelled sole proprietorship; Old Chang Kee matched the listed parent, not the operating subsidiary.
- Registry plus web step: 9 of 12 correct; wrong accepted 1 (Ya Kun: chose Ya Kun Cafe, ground truth Ya Kun International, both real and live, so the label is itself weak); unresolved 2 (Grab, whose terms name three entities; Deliveroo, whose only entity is in liquidation). Both unresolved answers were reasonable refusals. Passes all three thresholds, on a smaller and easier sample than planned.
- Operators often have unrelated names (Ninja Logistics, Golden Beeworks, Taster Food, Super Bean), so name matching cannot find them; the web step can.
- Caveat: web-step acceptances partly use registry-mirror sites that were also used to confirm ground truth.

## X3 (outputs/x3/RESULT.md)
- All three matchers agreed on 45 of 60 postings; a majority code existed for all 60, but 14 of those were "no good fit". Real occupation by majority: 46 of 60 (77%). After my judgement of fit: 42 of 60 (70%).
- What failed to match: promotional-style postings with emoji titles and travel promises, generic "sales and marketing" titles, and warehouse supervisor (no such occupation in MOM's table; the Haiku matcher mapped all five to warehouse manager, a more senior job). So an automatic benchmark would sometimes pick the wrong job; user confirmation of the occupation looks necessary, or the tool should say "no benchmark".
- Pay comparison (descriptive, 46 postings): 25 within the official 25th to 75th percentile, 18 below, 3 above. Many below-range postings are junior or entry-level roles compared with an all-seniority table, so a gap is not evidence of underpayment. No advertised range was wider than 2 to 1.
- My labels and the default-model agent's agreed on 59 of 60; we are the same model family, so this is not independent confirmation.

## What this means for the product ideas
1. Brand to legal entity (X2) is the most solid: build the web step, always refuse when ambiguous or not live, and show the user what was chosen.
2. Red-flag sweep (X1): both approaches work for well-reported recent cases; do not claim a fixed sweep beats free-form. A fixed sweep is cheaper to audit and show; test it again on harder cases before building.
3. Official lists for employment issues are not machine-readable today (X0): coverage would be financial regulation and consumer complaints.
4. Pay benchmark (X3): ask the user to confirm the occupation; label the figure as June 2025, residents, full-time, excluding bonuses.

## Deviations from the protocols
- X1: 12 known-problem organisations, not 20 (only two readable sources). A rerun is needed for a discriminating test.
- X2: 12 brands, not 30, because ground truth could not be established for the rest; one reserve brand (Mr Bean) used.
- X3: the first collection run mis-parsed 15 postings; the parser was fixed and the postings recollected before any matcher saw them. The "good fit" judgement was applied after seeing majority codes.
- Ground truth and arm results come from Haiku agents; I spot-checked four UENs in the registry, not every claim.
