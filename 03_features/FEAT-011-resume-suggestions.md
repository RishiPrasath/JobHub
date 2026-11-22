---
id: FEAT-011
title: Evidence-linked resume suggestions
type: feature
scope: testing
need_level: N1
feasibility_level: T2
result: mixed
opportunity: [OPP-006]
needs: []
findings: [FND-E04-01, FND-R02-03, FND-E19-01]
riskiest_assumption: ASM-011
decision: 0005
updated: 2026-11-22
---

# Evidence-linked resume suggestions

In build scope ([decision 0005](../06_scope/decisions/0005-second-build-scope.md)), using the user's own text only: suggestions cite the user's profile entries, a code check blocks new facts, gaps stay gaps, and the user confirms each entry. Scope is `testing` until the `in` gate is met.

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

## Completion run (E19, 2026-11-11)

The cells cut off by the token limit were filled in. See the addendum in [E19 FINDINGS](../04_experiments/E19-evidence-linked-resume-suggestions/FINDINGS.md).

- The "be truthful" instruction (M1) put 8 to 14 fabricated credentials, employers or metrics in front of the user on each model, with 29 to 45% unsupported claims.
- The ledger with a code check (M2) produced none, on three models and two runs: 0 fabricated, 0% unsupported (displayed), 100% citations, no intent commitments, no injection followed. Gaps shown as gaps: 100% for gpt-oss-20b and gpt-oss-120b, but 88.5% and 86.5% for qwen (bar 90%).
- Selection only (M3) was clean for gpt-oss-20b and 13% unsupported for qwen.
- The relevance blind spot (true but unrelated facts for requirements the profile cannot meet) was not re-checked and still needs a human confirming each entry.

**Feasibility call (for the owner to confirm):** supported at fixture level for ledger-cited rewording with a code check and a human confirming that each entry answers its requirement. Instruction-only ("be truthful") is not supported. Level T2. Still needs real participants (Part B).
