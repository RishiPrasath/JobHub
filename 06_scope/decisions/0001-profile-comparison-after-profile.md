# 0001: Profile comparison follows the candidate profile

Status: accepted
Date: 2026-11-10
Decided by: owner

## Context

[SCOPE.md](../SCOPE.md) listed decision 2: should profile comparison ([FEAT-010](../../03_features/FEAT-010-profile-comparison.md)) come first, or later? Comparison needs candidate facts to compare against role requirements. Those facts are now defined in [FEAT-016](../../03_features/FEAT-016-candidate-profile.md) (profile at sign-up) and [FEAT-017](../../03_features/FEAT-017-initial-setup-job-preferences.md) (preferences). FEAT-010 failed its last fixture run.

## Options considered

1. Later, after the profile is built.
2. First slice, alongside posting review.
3. Leave open until the first user test.

## Decision

Option 1. Profile comparison follows the candidate profile and the preferences setup. It is not part of the first slice.

This sets the order of work only. It does not change the scope value of FEAT-010, which stays `candidate`.

## Evidence (finding IDs)

FND-E03-01, FND-R03-02 (profile comparison failed in the fixture run).

## Consequences

- FEAT-010 depends on FEAT-016 and FEAT-017 and should be retested with a real profile as its input.
- Posting review (FEAT-002) does not need a profile for the first slice.
