---
id: FEAT-011
title: Evidence-linked resume suggestions
type: feature
scope: candidate
need_level: N1
feasibility_level: T1
result: inconclusive
opportunity: [OPP-006]
needs: []
findings: [FND-E04-01, FND-R02-03, FND-E19-01]
riskiest_assumption: ASM-011
decision: null
updated: 2026-11-10
---

# Evidence-linked resume suggestions

Levels are provisional and await owner review.

## What it does

Suggests resume changes tied to evidence.

Covered in the first test (owner decision 2026-11-10): selecting and reordering the user's existing evidence for a posting, rephrasing existing bullets without adding any fact, flagging gaps without filling them, and a scoped format and accessibility check with no "ATS-safe" claim. The user's evidence ledger is their FEAT-016 profile entries, and every suggestion cites one.

## Evidence for

Tailoring by selection is a recognized need.

## Evidence against

Failed factuality.

## Where documents disagree

Deferred, though `AGENTS.md` names application preparation.

## Next test

Planned in [E19](../04_experiments/E19-evidence-linked-resume-suggestions/README.md), in two parts. Feasibility is not claimed until it has run.

- **Part A (fixture test, runs now):** 18 hand-collected postings against 3 synthetic profiles in the FEAT-016 format (54 suggestion sets), with the E04 failure types included. Three methods are compared: instruction only (as in E04), ledger-constrained with a code check on facts, and selection only. A separate set of 16 resume files tests the format check. Gold labels are written beforehand by a human. Proposed pass: zero fabricated credentials, employers or metrics reaching the user, unsupported claims 1% or less, every suggestion citing a ledger entry and a posting requirement, gaps shown as gaps at least 90% of the time, format check finding at least 90% of planted problems with no ATS promise. Proposed fail: any fabrication reaching the user, or unsupported claims over 5%.
- **Part B (with people, waits for a real profile):** 6 to 8 job seekers tailor a resume by hand and review suggestions, with one planted unsupported item. Proposed pass: planted item caught at least 75% of the time and effort no more than by hand. Proposed fail: caught under 50%.

Riskiest assumption (ASM-011): suggestions can be kept factual with a sentence-level ledger. Thresholds were treated as confirmed by the owner's instruction to run (2026-11-10) and frozen by file hash; see the result below.

## Result of the first run (2026-11-10)

E19 (reduced, daily limit): the ledger-constrained method put no fabricated credential, employer or metric on 20 sets, but the baseline and selection-only methods barely ran, so the check cannot be credited. A read-through found one unsupported role relabelling per model and true facts attached to requirements they do not answer. The format check found 12 of 12 planted problems with no ATS promise. **Narrow to selecting and ordering the user's own entries with citations**; free rewording not supported by this run. Part B not run. See [E19 findings](../04_experiments/E19-evidence-linked-resume-suggestions/FINDINGS.md).

Thresholds were treated as confirmed by the owner's instruction to run. Samples were reduced and mostly synthetic, labels were written by an AI, and the Groq daily token limit cut several runs short. Levels are provisional and await owner review. Nothing here sets `in` or `out`.
