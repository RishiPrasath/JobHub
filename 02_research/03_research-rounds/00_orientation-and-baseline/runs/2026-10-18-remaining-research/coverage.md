# Research coverage and residual uncertainty

2026-10-18. Coverage includes this run, the [earlier reviewed workflow findings](../2026-10-18-ai-job-hunting-workflows/findings.md), and the [reviewed Singapore friction findings](../2026-10-18-job-search-friction/findings.md). The friction study distinguishes practical conditions, information uncertainty and process effort; it does not rank their burden. “Desk addressed” means evidence/options have been investigated and the remaining uncertainty is bounded. It does **not** mean a product assumption is validated, a tool is benchmarked or a human decision is accepted.

Report keys: [P — product](product-market.md), [U — UX](ux-and-accessibility.md), [D — development](development-method.md), [T — technical/risk](technical-and-responsible-ai.md), [C — Codex/delivery](codex-and-delivery.md), [A — earlier AI workflows](../2026-10-18-ai-job-hunting-workflows/findings.md). Validation IDs refer to the [finite empirical queue](validation-next.md).

## Backlog R-01 through R-15

| ID | Desk-research coverage | What is not established | Next evidence / owner |
| --- | --- | --- | --- |
| R-01 friction and lost opportunity | A, P, U: workflow evidence, candidate pain points and interruptible journey | Ranking of consequential pain for intended users | V01 / Job-Seeker Practices Researcher |
| R-02 unmet need and inclusion | A, P, U: contrasting segments and inclusive recruitment | Strongest segment or representative prevalence | V01 / Practices Researcher, Responsible AI Reviewer |
| R-03 actual AI use | A: empirical studies, first-person reports, internal documented workflow and six-tool matrix | Current representative Singapore use; tools' actual comparative performance | V01/V03 / Practices Researcher, AI Tools Expert |
| R-04 automation boundaries | A, T: assist/review/action distinction, risks and proposed controls | Which boundaries target users prefer; operational enforcement | V01/V03/V04 / Practices Researcher, Responsible AI Reviewer |
| R-05 trust and evidence | P, U, T: claim provenance, uncertainty, correction and company-source hierarchy | User comprehension and justified trust | V02/V04 / UX Expert, Quality Engineer |
| R-06 device/surface | U: realistic surface options, capability constraints and flow alternatives | Best product platform or desktop/mobile split | V02 / UX and User-Flow Designer |
| R-07 competition/gaps | A, P: documented offerings, crowded capabilities and differentiation hypotheses | Durable gap, superior outcomes or willingness to switch | V03/V06 / Competitive Landscape Researcher |
| R-08 industry/market | P and A: Singapore context, non-IT inclusion, phased-market options | Initial segment/scope acceptance or US readiness | V01/V06 / Product Strategist |
| R-09 capture/preservation | T, P: capture options, source/version schema, rights and evidence constraints | Site-by-site permission and real extraction accuracy | V04 / Technical Architect, Quality Engineer |
| R-10 privacy/security/fairness | T, A, U: risks, controls and correction/accessibility safeguards | Legal compliance, production safety, fairness across all groups | V04/V06 / Responsible AI Reviewer |
| R-11 development approach | D: uncertainty-scaled workflow, gates, trade-offs and productivity evidence | Fastest method for this owner/product | V05 / AI SDLC Advisor |
| R-12 Gherkin/Cucumber | D: distinction, selective adoption and maintenance criteria | Net maintenance benefit in JobHub | V05 / AI SDLC Advisor, Quality Engineer |
| R-13 parallel Codex | C: current official mechanism, local gap, context, ownership and GitHub integration | Native custom config smoke test or measured productivity gain | V05 / Prompt Engineer, Quality Engineer |
| R-14 tools/models | T, A, C: task-based comparison, deterministic baseline, privacy/cost and runtime distinctions | Best model/provider or cost/latency at real load | V03/V04 / AI Tools Expert |
| R-15 owner learning | U, D, C: UX exercises, engineering explanation and review responsibilities | Owner mastery demonstrated in a delivered slice | V02/V05 / UX Expert, AI SDLC Advisor |

All fifteen questions have a desk-research treatment. None is marked universally resolved; the column above identifies the exact form of evidence that desk work cannot supply.

## Product draft — user-proposed topics

| Draft topic | Coverage |
| --- | --- |
| Product/user research and differing job seekers | A, P, U; V01 observations and segmentation |
| Job-posting analysis and facts/inference/signals/missing data | T, P, A; V04 field/claim evaluation |
| Candidate matching, transferable skills, essential/trainable gaps | P, T; evidence-backed comparison rather than deterministic hiring scores |
| Market/company research, current sources, Singapore and later US | P, A; dated scoped evidence, contradiction handling, expansion conditions |
| Cross-industry support and sector differences | P, A; common evidence core plus verified sector-specific requirements |
| Technical stack/architecture/model/security questions | T, C, D; alternatives and selection criteria, no final stack |
| Surface and cross-device workflow | U; desktop, responsive/mobile web, PWA, native, extension and combined options |
| AI automation across discovery/preparation/outreach/interviews/tracking | A, P, T; sourcing/networking/follow-up effectiveness remains thin, explicitly part of V01/V03 |
| Real-world daily planning, prompts, corrections, pressure and coping | A, U; limited public accounts/internal process, not representative observation |
| Competition and positioning | P, A; current offerings separated from performance and durable-gap claims |
| Naming/brand | P; JobHub retained, public confusion screening distinct from launch clearance; synthetic persona votes excluded as human evidence |
| Internal Job Hunt reference | A and prior internal evidence register; bounded process scan already completed, not a whole-vault behavior audit |

## Product draft — recommended topics

| Draft topic | Coverage |
| --- | --- |
| Problem validation and meaningful outcomes | A, P, U; V01/V02 outcomes beyond application volume |
| User segments and inclusion | P, U, T; V01 recruitment and individual barriers |
| Capture/source reliability/rights | T, P; V04 permissioned fixtures and source-specific review |
| Evidence/trust/explainability/override | P, T, U; V02 comprehension and V04 grounding |
| Mobile/web/product shape | U; V02 matched tasks and device capability checks |
| Candidate profile/fit | P, T; confirmed evidence, uncertainty and user correction |
| Company/red-flag evidence | P, T; no misconduct inference from a single review or generic phrase |
| AI-assisted job hunting, affordability and control | A, P, T; free/manual baseline and task comparison |
| Technical/privacy/operating constraints | T; data lifecycle, retention choices, reliability, cost and latency measurement |
| Market position/sustainability/partnerships | P; V06 behavior-based validation, no pricing decision |
| Research operations/versioning/stopping | Brief, sources, this coverage register and V01–V06; dated evidence, concise synthesis, explicit revisit triggers |

## AI-era draft — user-proposed topics

| Draft topic cluster | Coverage |
| --- | --- |
| Selective Gherkin/Cucumber and other specifications/tests | D; executable behavior only where stability/risk/reuse justify it |
| Responsible development without over-specification | D, C, T; uncertainty-scaled process and human authority |
| User-flow thinking and AI as a design partner | U; task/state/exception mapping, real-user validation |
| Intuitive UI, information architecture, labels, hierarchy and feedback | U; concrete design exercises and review criteria |
| Empty/loading/error/undo, cognitive load and humane language | U; interruption/recovery flow and evidence presentation |
| Accessibility across abilities/devices/languages | U; standards-based checks and inclusive evaluation; no compliance claim |
| Keyboard/screen reader/focus/contrast/scaling/motion | U; manual plus automated evaluation, not a final-stage checklist |
| Evaluate AI-generated design versus attractive but unsuitable UI | U and V02; owner critique and observed tasks |
| Three supplied development playbooks | D; each assessed or access limitation documented separately |

## AI-era draft — recommended topics

| Draft topic | Coverage |
| --- | --- |
| AI-assisted development model and human responsibility | D, T; lightweight/hybrid comparison and gates |
| Codex/agent workflows | C; native runtime, ownership, sequential versus parallel and verification |
| Context/knowledge management | C; separate durable rules, portable roles, task prompts and dated evidence |
| Evaluation-driven development | T, D, C; factuality, workflow/tool behavior, regression and holdout fixtures |
| Secure/responsible AI lifecycle | T and C; data/injection/permissions/supply-chain and CI boundaries |
| Software quality and technical debt | D, C; independent acceptance, review, rollback and integration |
| UX/design learning with AI | U; personally owned research/critique/accessibility skills |
| Tool/model selection | T, A; task-level trials, privacy, cost, latency, portability and deterministic alternatives |
| Delivery and collaboration | C, D; branches/worktrees/checks/acceptance with user-controlled external writes |
| Personal skill development | U, D, C; teach-back and evidence-based review rather than memorising AI explanations |

## Scope of completion

Source access failures, unperformed live comparisons and legal/market uncertainty remain visible in the workstream limitations. More browsing is not a substitute for V01–V06. Source refresh is required if the relevant provider, law, market, browser capability or product changes before a decision is taken.
