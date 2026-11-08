# Round 04 synthesis

Status: draft synthesis written during the 2026-11 reorganization; owner review pending

Research date: 2026-10-19, Singapore time.

## Question

How might JobHub support truthful, role-specific job preparation across a wider range of industries while keeping AI assistance understandable, reviewable and under the job seeker's control? (From the [draft round brief](round-brief-draft.md), which still describes its wider plan as a draft.)

## What was done

- [Job-posting page inventory](runs/2026-10-19-job-posting-page-inventory/README.md): 20 page observations across search, detail, public-service, support, shell, maintenance and blocked states. Seven were substantive vacancy detail pages.
- [Remaining-objectives run](runs/2026-10-19-round4-remaining-objectives/README.md): Singapore-first public-web research on industry profiles, truthful tailoring, role fit and market value, ATS and accessibility, and AI trust controls.

No participants were contacted, and no live applications or paid-tool benchmarks were run.

## Key findings

Neither run's `findings.md` labels individual findings by confidence. The remaining-objectives [README](runs/2026-10-19-round4-remaining-objectives/README.md) gives only general tiers by evidence type: high for official requirements, documented guidance and directly stated tool policies; medium for convergent practical guidance and bounded empirical findings; low for vendor success claims, anecdotes, prevalence and outcome predictions. It does not assign the findings below to those tiers.

**Job-posting pages** ([findings](runs/2026-10-19-job-posting-page-inventory/findings.md))

| Finding | Confidence |
|---|---|
| A layered posting record (identity and access, provenance, raw sections, normalized fields, missingness, relationships) fits the sample better than a fixed list of headings | None stated |
| Original labels and wording should be kept, with normalization added only when justified | None stated |
| Platform signals such as match scores, badges and applicant counts are a separate layer, not employer-authored fact | None stated |
| The pages justify distinct states for present, partial, conditional, contradictory, not present, not visible, blocked, not applicable and unknown | None stated |
| Search cards lack enough context for fit, tailoring or credibility review, and differences from detail pages should be reported | None stated |
| Industry and occupation are separate dimensions; differences may come from occupation, seniority, arrangement or regulation | None stated |

**Remaining objectives** ([findings](runs/2026-10-19-round4-remaining-objectives/findings.md))

| Finding | Confidence |
|---|---|
| Industry fit is contextual: hard gates, transferable bridges, trainable gaps and preferences should not collapse into one score | None stated |
| Truthful tailoring means selecting, translating and explaining real evidence, not inventing metrics, dates, credentials or outcomes | None stated |
| "ATS-friendly" is not one universal format; parser behaviour varies by system | None stated; the run README says "strong guidance and vendor-specific evidence; no universal ATS rule established" |
| Market value is contextual and not human worth; wage tables can inform occupational benchmarks only | None stated |
| AI reduces writing and organising effort, but outcome evidence is mixed and adoption estimates vary. An explainable assistant with provenance, editing and explicit approval is the most defensible role | None stated |
| Public accounts describe spreadsheets or trackers for applications ([practices note](runs/2026-10-19-round4-remaining-objectives/job-seeker-practices.md)) | "Low-to-medium"; not prevalence |

## What remains unknown

- Which role-fit fields are hard gates, strong signals, trainable gaps or preferences in each context.
- How residents, migrants, returners and career switchers actually discover roles.
- Whether users can identify and correct every AI change, and what "personal voice" means to candidates.
- What automation boundary job seekers consider useful, safe and explainable.
- How wage evidence should handle part-time, live-in, agency-mediated, overtime and non-resident arrangements.
- Whether any AI tool, format, match score or resume practice improves an individual's hiring outcome.

The full list is in the [remaining-objectives limitations](runs/2026-10-19-round4-remaining-objectives/limitations.md).

## Limits

- The page inventory is a dated convenience sample. It cannot establish whether a posting is genuine, whether a badge is accurate, or whether a pattern is prevalent ([limitations](runs/2026-10-19-job-posting-page-inventory/limitations.md)).
- The inventory's taxonomy has not had the two independent reviewers that its own next actions call for. No document here shows that its other next actions were done.
- The remaining-objectives README says `findings.md` contains evidence strength, but that file gives no per-finding strength.
- Public sources overrepresent official programmes, regulated sectors and vendor guidance, and user reports are self-selected.
- Findings are research inputs. No product scope, platform, architecture or AI-provider decision is made by this round.
