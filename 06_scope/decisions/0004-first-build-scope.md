# 0004: First build scope

Status: accepted
Date: 2026-11-22
Decided by: owner

Drafted as 0002 and renumbered on 2026-11-22 before it reached main, because 0002 (round-10 must-have review) and 0003 (v1 scope answers) were already recorded there.

## Context

[SCOPE.md](../SCOPE.md) had no feature in build scope. On 2026-11-22 the owner went through the candidates one by one and chose which to build. This settles decision 1 in SCOPE.md (first slice) and part of decision 3 (company research sources).

The `in` gate in [03_features/README.md](../../03_features/README.md) needs at least N3 and T2. None of the chosen features has N3 (direct accounts from target users) yet, so their `scope` is set to `testing` and points at this decision. Moving them to `in` needs N3 evidence or a change to the gate, and is the owner's call.

## Options considered

Each candidate on the board, one at a time: add to build scope, or leave as a candidate for later review.

## Decision

Seven features are in build scope, with these conditions.

| Feature | Condition |
|---|---|
| [FEAT-001 Employer identity check](../../03_features/FEAT-001-employer-identity-check.md) | Start from a UEN or company domain. A bare brand name is treated as a group of possible entities, not resolved to one. |
| [FEAT-002 Single-posting review](../../03_features/FEAT-002-single-posting-review.md) | Thin version that reuses FEAT-001's output. |
| [FEAT-003 Verification questions](../../03_features/FEAT-003-verification-questions.md) | In scope, but the approach must be reworked, because the last result was fail. |
| [FEAT-006 Red-flag evidence from official sources](../../03_features/FEAT-006-official-red-flag-evidence.md) | Gazette notices plus ACRA status. Restricted sources are link-outs only. |
| [FEAT-007 Harmful signals pack (Singapore)](../../03_features/FEAT-007-harmful-signals-pack.md) | Allowed free sources only. |
| [FEAT-009 Pay benchmark](../../03_features/FEAT-009-pay-benchmark.md) | Occupation level. MOM wage tables on data.gov.sg under the Singapore Open Data Licence, plus pay text the user pastes from the posting. MyCareersFuture data only with written permission from SWDA, whose terms bar storing or showing its content otherwise. |
| [FEAT-013 Offer and contract checks](../../03_features/FEAT-013-offer-and-contract-check.md) | Entity verification plus a checklist. No legal judgement on clauses. |

Not yet decided, in this review order: FEAT-005, FEAT-008, FEAT-011, FEAT-004, FEAT-010, FEAT-015, FEAT-016, FEAT-017, FEAT-012, FEAT-014. They keep their current scope values.

Project-wide rules that apply: free and legal sources only, in Python. Sites that forbid automation are link-outs only, and their blocks are not evaded.

## Evidence (finding IDs)

FEAT-001: FND-E10X2-01, FND-P05-01, FND-E11-01. FEAT-002: FND-E01-01, FND-E12-01. FEAT-003: FND-R09-02, FND-E12-02. FEAT-006: FND-E10X0-01, FND-E10X1-01, FND-E14-01. FEAT-007: FND-R09-02, FND-E15-01. FEAT-009: FND-E10X3-01, FND-R08-01, FND-E17-01. FEAT-013: FND-R09-03, FND-E20-01.

## Consequences

- The seven features move from `candidate` to `testing`, with `decision: 0004`.
- FEAT-003 needs a new approach and a new test before it is built.
- FEAT-009 uses no MyCareersFuture data unless SWDA gives written permission.
- Lived-experience reviews (FEAT-008) are not chosen yet, so official sources come first for company research.
- [0001](0001-profile-comparison-after-profile.md) still holds: FEAT-010 follows the candidate profile.
