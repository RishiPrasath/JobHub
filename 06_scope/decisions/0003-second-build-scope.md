# 0003: Second build scope (paste capture, employee reviews, resume suggestions)

Status: accepted
Date: 2026-11-22
Decided by: owner

## Context

[0002](0002-first-build-scope.md) left FEAT-005, FEAT-008 and FEAT-011 first in the review order. On 2026-11-22 the owner added all three to build scope (for FEAT-011, owner's words: "build scope please").

For FEAT-008, E16 found no source that both allows automated reading and holds recent first-hand reviews of Singapore employers ([run-003 notes](../../04_experiments/E16-employee-experience-sources/runs/2026-11-21-run-003/RUN-NOTES.md)). The owner chose from the options listed there. Owner's words: "Link-outs: show the user a one-click link to the company's page on Glassdoor, Indeed, JobStreet and Google Maps. No scraping, no terms risk, and the user reads the reviews themselves. and also attempt scraping that is my final decision."

As in 0002, none of the three has N3 evidence, so they are `testing`, not `in`.

## Options considered

FEAT-005 and FEAT-011: add to build scope, or leave as a candidate.

FEAT-008 (from E16 run-003, section 4): link-out cards; TAFEP Tripartite Standards badge by UEN; user-pasted reviews; asking NodeFlair or others for a licence; JobHub's own contributions.

## Decision

| Feature | Condition |
|---|---|
| [FEAT-005 Paste capture](../../03_features/FEAT-005-paste-capture.md) | As narrowed by E13: dated snapshot, partial-paste check, field-gap notice and the stale rule. The notice states its reason. |
| [FEAT-011 Evidence-linked resume suggestions](../../03_features/FEAT-011-resume-suggestions.md) | The user's own text only, as supported by E19: suggestions select, order or reword the user's own profile entries, each citing its entry, with a code check that blocks any new fact. Gaps are shown as gaps. The user confirms that each entry answers its requirement. No instruction-only ("be truthful") generation. |
| [FEAT-008 Employee experience and reviews](../../03_features/FEAT-008-employee-experience.md) | (1) One-click link-outs to the employer's page or search on Glassdoor, Indeed, JobStreet and Google Maps. JobHub fetches nothing from them and copies no rating or text. (2) Ingest sources whose terms permit it: the TAFEP Tripartite Standards adopter list, keyed by UEN and shown as a pledge, not as reviews. (3) Attempt NodeFlair and record the technical result, but do not show its content in the product, because its terms need a licence for commercial use and its reviews are over 2 years old. |

Project-wide rules still apply: free and legal sources only, in Python. Sites that bar automation (Glassdoor, Indeed, JobStreet, Reddit, Google Maps, LinkedIn, Glints, Great Place to Work, Blind, HardwareZone) are link-outs only, and their blocks are not evaded.

Still not decided, in review order: FEAT-004, FEAT-010, FEAT-015, FEAT-016, FEAT-017, FEAT-012, FEAT-014.

## Evidence (finding IDs)

FEAT-005: FND-P01-01, FND-R01-01, FND-E13-01. FEAT-011: FND-E04-01, FND-R02-03, FND-E19-01. FEAT-008: FND-E09-01, FND-E09-02, FND-P05-01, FND-E16-01, plus E16 run-003 (terms read live 2026-11-21).

## Consequences

- FEAT-005, FEAT-008 and FEAT-011 move from `candidate` to `testing`, with `decision: 0003`.
- FEAT-011 reads the user's evidence from the candidate profile (FEAT-016), which is not in build scope yet. Until it is, the build needs another way for the user to give their entries, or FEAT-016 needs a decision.
- FEAT-008 is no longer a review summary. Its riskiest assumption (ASM-008, lawful review content) stays failed for review text; the build is link-outs plus an official pledge signal.
- FEAT-008's Tripartite Standards lookup depends on a UEN, so it follows FEAT-001.
- Showing NodeFlair content would need a licence from NodeFlair and a new owner decision.
- This settles decision 3 in SCOPE.md (company research sources) for lived-experience reviews.
