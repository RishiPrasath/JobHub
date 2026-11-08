---
id: FEAT-001
title: Employer identity check
type: feature
scope: candidate
need_level: N2
feasibility_level: T3
result: pass-small-sample
opportunity: [OPP-001]
needs: [S-05, S-35]
findings: [FND-E10X2-01, FND-P05-01, FND-E09-02, FND-R09-01]
riskiest_assumption: ASM-001
decision: null
updated: 2026-11-09
---

# Employer identity check

Levels are provisional and await owner review.

## What it does

Resolves a brand to a legal entity using the registry plus a web step.

## Evidence for

Strongest test result in the repo (X2), and prototype P05 caught a lookalike.

## Evidence against

Only 12 brands; 1 wrong answer; small employers fail discovery. Scam statistics do not show that this would prevent scams.

## Where documents disagree

In the deck plan first slice but absent from `reports/13`.

## Next test

Concierge test with real postings. Riskiest assumption: knowing the legal entity changes what a job seeker does next.
