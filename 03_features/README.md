# Features

Stage question: **what could we build?**

Each candidate has one `FEAT-NNN-slug.md` file. The original proposals are in [source-ideas/](source-ideas/README.md). The current board is in [SCOPE.md](../06_scope/SCOPE.md).

## Evidence levels

| Level | Need: do people have this problem? | Level | Feasibility: can we do it reliably? |
|---|---|---|---|
| N0 | Opinion or AI reasoning | T0 | Untested |
| N1 | Desk research: vendors, snippets, single creators | T1 | Narrative only, outputs not saved |
| N2 | Authoritative data: official statistics or primary documents | T2 | Saved outputs from fixtures or a single run |
| N3 | Direct accounts from target users | T3 | Pre-registered test on real data |
| N4 | Observed behaviour of real users | T4 | Works end to end with real users |

A failed test keeps its level and records the outcome in `result`. AI-gathered research is capped at N2, and only when the source was checked.

## Scope values and gates

| Value | Requires |
|---|---|
| `candidate` | A file |
| `testing` | One finding and one riskiest assumption |
| `in` | At least N3 and T2, a finding, an assumption, and a recorded owner decision |
| `later` | A recorded reason |
| `out` | A recorded owner decision |

Only the owner sets `in` or `out`. Run `python tools/validate.py` after any change.
