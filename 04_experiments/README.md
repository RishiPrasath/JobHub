# Experiments

Stage question: **does it work?**

Each experiment should preserve the full chain: question, fixture, prompt, code, raw output, review, findings, limitations.

| ID | Folder | Status | Results |
|---|---|---|---|
| E01-07 | [E01-07-sequential-sdk-run](E01-07-sequential-sdk-run/README.md) | Complete, narrative only | `findings.md` |
| E08 | [E08-user-interface-and-human-review](E08-user-interface-and-human-review/) | Two model runs; no interface or participant test | `runs/*/findings.md` |
| E09 | [E09-openserp-company-research](E09-openserp-company-research/README.md) | Complete | `REPORT.md`, `AGENT-TEST.md` |
| E10 | [E10-market-value-and-red-flag-experiments](E10-market-value-and-red-flag-experiments/README.md) | X0-X3 complete, pre-registered; P1-P3 not run | `FINDINGS.md` |

New experiments start from [_template](_template/README.md). Add results to [findings](../02_analysis/findings.md) and update the affected feature. SDK instructions are in [tools/openai-sdk](../tools/openai-sdk/briefing.md).

Use dated run folders (`runs/YYYY-MM-DD-run-001/`). Do not overwrite earlier runs: create a new one when the fixture, prompt, model or method changes.
