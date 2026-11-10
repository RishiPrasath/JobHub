# E15 freeze record

Frozen at 2026-11-10T09:58:16Z (UTC), before any system under test (the deterministic matcher, any model call, any persona call) was run on the cases.

| File | sha256 |
|---|---|
| `protocol/thresholds.md` | `5f9355f4fb2d5a048f8335118af6a1ad961524ddead370dd2affbf93e2e3b47a` |
| `protocol/question_rubric.md` | `1d2c3dbbfb93117df06dd686a1ea30c0baba9bc2f2333183863c628ae2969658` |
| `data/pack.json` | `ae52f69635ab57b0a09af9a7376edb6463c20217f8828633c98cd52d44bfea7b` |
| `data/cases.json` | `8b57b76cd471cadedf539ce1e56d6d37c5a37b3f816f4f111e69b9387cb97ce8` |
| `data/gold.json` | `180831af7f42fa2855fa82c25199fcf8a50c533d6f8a896f27752603a4cd9689` |

What was frozen and by whom: the thresholds (copied verbatim from the README), the question rubric, the rule pack (version 0.1), the 40 synthetic cases and the gold labels. All were written by the E15 specialist, an AI. Gold labels were written without running any system on the cases. The builders (`data/build_pack.py`, `data/build_cases.py`) regenerate the pack and cases; the pack patterns were only checked against TAFEP's published example phrases (not the cases) before freezing.

Not committed to git: the owner has not asked for commits, so the order is shown by this record and by file times, not by git history. Recorded under Deviations in FINDINGS.md.

Any later change to the pack, cases, gold, rubric or prompts is a new run folder labelled post hoc.
