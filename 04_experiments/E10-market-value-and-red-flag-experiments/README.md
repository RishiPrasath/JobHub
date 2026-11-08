# Experiments 10: market-value and red-flag experiments (X0 to X3)

Date: 2026-11-07 (Singapore). Follows [research round 08](../../01_research/rounds/R08-market-value-and-salary-benchmarking/runs/2026-11-07-how-market-value-is-determined/findings.md) (how market value is determined) and [experiment 09](../E09-openserp-company-research/AGENT-TEST.md) (OpenSERP for company research).

| ID | Experiment | Question | Protocol |
|---|---|---|---|
| X0 | Official source access audit | Which official sources can be checked for red flags, and are we permitted to? | [protocols/X0](protocols/X0-source-access-audit.md) |
| X1 | Fixed red-flag sweep versus free-form research | Does a fixed set of searches find known public problems more often than free-form research? | [protocols/X1](protocols/X1-red-flag-sweep.md) |
| X2 | Brand to legal entity | Can a brand name be resolved to the registered employer without accepting a wrong one? | [protocols/X2](protocols/X2-brand-to-legal-entity.md) |
| X3 | Posting pay versus the official wage table | Can postings be matched reliably to an official occupation, and how does advertised pay compare? | [protocols/X3](protocols/X3-posting-pay-vs-official.md) |

**Pre-registration.** The protocols, pass/fail thresholds, the X2 brand list and the X1 search pack were written and committed before any experiment ran. The X1 company list is committed after X0 and before the X1 arms run. Anything changed after seeing results is listed under "Deviations" in `FINDINGS.md`.

**Not in this experiment (need participants):** P1 real-shortlist employer check, P2 "open these yourself, paste back", P3 fair offer comparison. These need people recruited by the product owner.

**Rules.** Public information only; search through the local OpenSERP service at low rates; pages read by the local fetch service (robots.txt checked, honest identity); no logins, no CAPTCHA handling, no restricted review sites; no claim about any company beyond what an official source or a cited page says.

Layout: `protocols/`, `data/`, `harness/`, `outputs/x0` to `x3`, `FINDINGS.md` (written at the end).
