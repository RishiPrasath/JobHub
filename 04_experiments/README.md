# Experiments

Stage question: **does it work?**

Each experiment should preserve the full chain: question, fixture, prompt, code, raw output, review, findings, limitations.

| ID | Folder | Status | Results |
|---|---|---|---|
| E01-07 | [E01-07-sequential-sdk-run](E01-07-sequential-sdk-run/README.md) | Complete, narrative only | `findings.md` |
| E08 | [E08-user-interface-and-human-review](E08-user-interface-and-human-review/) | Two model runs; no interface or participant test | `runs/*/findings.md` |
| E09 | [E09-openserp-company-research](E09-openserp-company-research/README.md) | Complete | `REPORT.md`, `AGENT-TEST.md` |
| E10 | [E10-market-value-and-red-flag-experiments](E10-market-value-and-red-flag-experiments/README.md) | X0-X3 complete, pre-registered; P1-P3 not run | `FINDINGS.md` |
| E11 | [E11-employer-identity-check](E11-employer-identity-check/README.md) | Run 2026-11-10 (Part A, 39 synthetic postings): fail by the written rule (hidden-employer wrong accepts); Part B not run | `FINDINGS.md` |
| E12 | [E12-single-posting-review](E12-single-posting-review/README.md) | Run 2026-11-10, completed 2026-11-11 (Part A, all 24 postings): fails on gap-finding and questions; simulated Part B pilot only | `FINDINGS.md` |
| E13 | [E13-paste-capture](E13-paste-capture/README.md) | Run 2026-11-10 (Part A): mixed; Part B not run | `FINDINGS.md` |
| E14 | [E14-official-red-flag-evidence](E14-official-red-flag-evidence/README.md) | Run 2026-11-10 (Parts A, B reduced): Part A narrow pass, Part B fail; Part C not run | `FINDINGS.md` |
| E15 | [E15-harmful-signals-fixture-test](E15-harmful-signals-fixture-test/README.md) | Run 2026-11-10, completed 2026-11-11 (Part A, all 40 cases, 3 models): inconclusive; simulated Part B pilot only | `FINDINGS.md` |
| E16 | [E16-employee-experience-sources](E16-employee-experience-sources/README.md) | Run 2026-11-10 (Part A): fail; Parts B and C not run | `FINDINGS.md` |
| E17 | [E17-pay-benchmark-occupation-match](E17-pay-benchmark-occupation-match/README.md) | Run 2026-11-10, extended 2026-11-11 (Part A; qwen 89 of 100, gpt-oss-20b 100, a 7B model 100): inconclusive; Parts B and C not run | `FINDINGS.md` |
| E18 | [E18-profile-comparison](E18-profile-comparison/README.md) | Run 2026-11-10, extended 2026-11-11 (Part A): free-text fail, structured inconclusive, hybrid partial (29 of 45); Part B not run | `FINDINGS.md` |
| E19 | [E19-evidence-linked-resume-suggestions](E19-evidence-linked-resume-suggestions/README.md) | Run 2026-11-10, completed 2026-11-11 (Part A): mixed; Part B not run | `FINDINGS.md` |
| E20 | [E20-offer-completeness-check](E20-offer-completeness-check/README.md) | Run 2026-11-10, one letter added 2026-11-11 (Part B, 11 of 20 letters): inconclusive; Parts A and C not run | `FINDINGS.md` |
| E21 | [E21-interview-preparation-need](E21-interview-preparation-need/README.md) | Run 2026-11-10 (simulated pilot only): Part A not run with participants | `FINDINGS.md` |
| E22 | [E22-sg-company-entity-sources](E22-sg-company-entity-sources/README.md) | Run 2026-11-21 (20 brands, small volume): name-only match fails (2 of 11); domain chain reaches ACRA for 10 of 20; MyCareersFuture blocked by terms | `FINDINGS.md` |

New experiments start from [_template](_template/README.md). Add results to [findings](../02_analysis/findings.md) and update the affected feature. SDK instructions are in [tools/openai-sdk](../tools/openai-sdk/briefing.md).

Use dated run folders (`runs/YYYY-MM-DD-run-001/`). Do not overwrite earlier runs: create a new one when the fixture, prompt, model or method changes.
