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
updated: 2026-11-10
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

Planned in [E11](../04_experiments/E11-employer-identity-check/README.md), in two parts:

- **Part A (technical):** run the P05 flow on 60 real postings, including small employers, hidden-employer agency postings and lookalikes. Ground truth is set before the run, without registry-mirror sites. Thresholds are proposed in E11 and await owner confirmation.
- **Part B (usefulness):** a concierge test with 6 to 8 job seekers, to test the riskiest assumption: knowing the legal entity changes what a job seeker does next.

E11 is a plan only. Nothing has been run.
