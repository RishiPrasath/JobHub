# X2: brand to legal entity

**Question.** Given a brand or trading name from a job posting, how often do we identify the correct registered employer, and how often do we accept a wrong one?

**Why.** The registry cannot match brands to registered names. In experiment 09's agent test, web research found the legal entity behind Ninja Van, and the registry confirmed Grab's Singapore entity once the name was known. Combining the two may close the gap.

## Data (frozen now)
`data/x2_brands.json`: 30 brands (10 large, 10 mid-size, 10 small chains or services) and a reserve of 6. **Ground truth** is the operating entity named in the brand's own privacy policy, terms or footer, confirmed to exist in the registry by company ID. It is gathered by a separate agent working only from the brand's own pages and recorded before Arm B runs. A brand whose ground truth cannot be established from the brand's own pages is dropped and replaced from the reserve in order; the dropped brand is reported.

## Arms
- **Arm A, registry only.** The registry check on the brand name as written.
- **Arm B, registry plus web step.** Search `"<brand>" Singapore Pte Ltd UEN` and `"<brand>" privacy policy Singapore` through OpenSERP; read the top registry-mirror and brand pages with the local fetch service; extract candidate legal names and company IDs; validate each candidate in the registry; accept the best only if it is live, its registered name shares a distinctive word with the brand or its own page names the brand as its trading name, and it is named by at least two independent pages. Otherwise return "unresolved".

## Measures
Correct top-1 (the accepted entity equals ground truth by company ID); **wrong accepted** (a confident answer that is not ground truth); unresolved; searches per brand.

## Pass/fail (set before running)
- **Pass:** Arm B correct on at least 70% of brands, wrong accepted on at most 1 of 30, and Arm B exceeds Arm A by at least 30 percentage points.
- **Fail:** Arm B correct under 50%, or wrong accepted on 3 or more.
- Anything between is inconclusive.

## Limits stated in advance
Brands were chosen by the lead researcher from well-known names, so they are easier than a random sample of postings. A brand whose own site names a parent or foreign entity as operator is recorded as such, and the registry may not contain it.
