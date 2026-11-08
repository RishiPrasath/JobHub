# ACRA recheck, 2026-11-03

Re-ran the registry matcher on the 34 persona-run employers with the local index (2,124,508 entities, still present in the `acra-data` volume), then changed three rules.

| Persona | Before (28 exact, 5 confirm, 1 unresolved) | After |
|---|---|---|
| career-change | 4 exact, 1 unresolved | 4 exact, 1 public body (CPF Board) |
| culinary-food-service | 5 exact | 5 exact |
| healthcare-care | 3 exact, 1 confirm | 4 exact |
| office-admin | 5 exact | 5 exact |
| service-frontline | 4 exact, 1 confirm | 5 exact |
| technology-digital | 2 exact, 3 confirm | 5 exact |
| trade-operations | 5 exact | 5 exact |

Changes in `05_prototypes/P03-company-research-pipeline/pipeline/acra.py`:
1. A posted name that equals a registered name exactly is `exact` even when other entities only add words to it (Recruit Express, Coffee Club, Kyndryl, Randstad, Singtel). Two live entities with the identical name are still flagged.
2. Names with "board", "authority", "ministry" and similar words that find nothing, or only unrelated partial matches, return `public_body` instead of a wrong candidate.
3. Matches through a former name, or to a registered name with extra words ("Grab Holdings" to "Grab Geo Holdings"), now need confirmation instead of `likely`.

Raw results: `acra_recheck_2026-11-03.json` (before) and `acra_recheck_after_fix.json` (after).

Limits: the 34 employers were used to find these issues, so their result is a repair, not a test. The two samples drawn from the registry itself (300 names; 211 shortened names) were not used for tuning. In the shortened-name sample 17 of 211 were accepted automatically with no clearly wrong match; 13 of those 17 were another real company whose registered name equals the shortened name, which the resolver cannot tell apart without more information. The site-finding step was not re-run for the five newly exact employers.
