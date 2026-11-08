# Research brief: public user insight study

Date prepared: 2026-10-18. Status: used for a bounded first public-web pass on 2026-10-18; its full stopping rule was **not** certified. The [findings](findings.md) and [limitations](limitations.md) record what was actually achieved. This brief is aligned to the [canonical product research strategy](../../../../../01_strategy/02_product-research-strategy.md).

## Decision

Which job-search problem should JobHub investigate first with a synthetic workflow or low-fidelity prototype?

## Primary question

Across publicly available accounts and research, which recurring job-search difficulties appear consequential enough to test further, and how do they differ across job-search stages, occupations, employment situations, digital confidence, device access, and access needs?

This run compares three unranked candidate hypotheses carried forward from earlier research:

1. application or role uncertainty creates repeated preparation or checking effort;
2. practical working-condition or role-fit uncertainty makes some opportunities difficult to assess or pursue;
3. interrupted capture, return, and loss of context make otherwise useful job-search work harder to complete.

These are hypotheses for retrieval and comparison, not findings or product requirements.

## Questions in scope

- Where do people lose time, confidence, context, or opportunity?
- How do people discover, save, compare, prepare for, apply to, and follow up on jobs?
- How do they use AI tools, career tools, spreadsheets, notes, browser tools, or manual workarounds?
- Which tasks do they automate, review, reject, or keep personal?
- What workarounds appear when tools fail or when people have limited time, money, device access, or digital confidence?
- What causes abandonment, repeated effort, confusion, correction, or distrust?
- Which observations recur across independent source families, and which are isolated, contradictory, or missing?

## Scope and exclusions

- **Geography:** Singapore first where credible public evidence exists; broader English-language evidence may provide labelled comparison or vocabulary.
- **Audience:** job seekers across sectors, including graduates, career changers, retrenched or mature workers, returners, service/trades/operations workers, and people discussing accessibility needs. Do not infer sensitive attributes from public text.
- **Time:** prioritise material published or accessed from 2023 through 2026 for current tool and workflow language. Retain older foundational work only when its date and transfer limits are explicit.
- **Sources:** openly accessible academic or qualitative studies, official statistics and reports, transparent public surveys, public firsthand accounts, public Reddit/forum material, public comments or posts, product reviews, public support discussions, and public blog or video transcripts.
- **Exclusions:** private groups or accounts, doxxing, author contact, profiling, sensitive inference, direct interviews, participant observation, purchases, live applications, private uploads, external writes, and claims of population prevalence from convenience material.

The private Job Hunt workspace is excluded from this run. Earlier internal process observations remain historical internal evidence and must not be placed in this run's public source ledger.

## Required role order and bounded responsibilities

1. **Research Planner:** confirms the decision, scope, evidence standard, exclusions, pass budget, and stopping decision.
2. **Research Query Strategist:** works first after the Planner. Produces `query-plan.md`, including the vocabulary map, balanced query portfolio, source-family plan, retrieval risks, query-log schema, and stopping rule. Does not synthesize findings.
3. **Job-Seeker Practices Researcher:** executes public firsthand-experience, workflow, workaround, abandonment, checking, correction, and day-to-day AI-use query families.
4. **Job Domain Researcher:** executes job-search-stage, occupation, Singapore/context, labour-market, and practical-condition query families.
5. **UX Expert or UX and User-Flow Designer:** executes public device, interruption, accessibility, cognitive-load, and interaction-friction query families only; it must not present this as usability validation.
6. **Evidence Synthesizer:** reconciles source families, contradictions, confidence, transfer limits, and the candidate hypothesis comparison.
7. **Product Strategist, if used:** proposes a synthetic test from the result; does not accept product scope.

One solo founder may perform several roles sequentially. The handoffs and files remain separate. If parallel agents are used, each receives one query family and one non-overlapping output responsibility.

## Query-planning deliverable

Before browsing for evidence, the Research Query Strategist writes `query-plan.md` with:

- decision context, primary/supporting questions, audience, geography, time window, exclusions, and unresolved scope choices;
- a concept and vocabulary map with canonical, user-language, academic, official, Singapore, occupation, stage, AI, positive, failure, workaround, and contradiction terms;
- a small query portfolio grouped by intent: discovery, firsthand workflow, academic/qualitative, official/context, AI-use and control, device/accessibility, workaround/failure, and disconfirmation;
- the intended evidence type and executing role for every query family;
- preferred source families, acceptable supporting sources, weak signals requiring careful labels, and source-independence rules;
- portable query intent separated from optional search-system syntax;
- known retrieval risks, likely gaps, and terms that should not be used for profiling;
- the `query-log.md` fields and the stopping rule.

## Time-box and pass structure

Use a small first pass. The following are planning limits, not prevalence or quality thresholds:

- **Pass A — vocabulary and orientation, up to 30 minutes:** run discovery queries, add only terms that materially improve retrieval, and record noisy or failed searches.
- **Pass B — focused evidence, up to three 45-minute blocks:** collect sources for the three hypotheses. Cover firsthand/workflow evidence, Singapore or contextual evidence, and one contrast such as AI/control, device/accessibility, or practical conditions where material exists.
- **Pass C — contradiction and stop check, up to 30 minutes:** search positive cases, workarounds, failure modes, and disconfirming terms; deduplicate source families; assess whether another block can change the shortlist.

Stop earlier when a central question has an explicit evidence gap and a synthetic workflow is the cheaper next step. Do not expand into a broad competitor, pricing, legal, platform, or stack review during this run.

## Recording and exact output files

The executed run must create or update exactly these files in this run folder:

- `README.md` — status, purpose, role order, and relationship to later work;
- `brief.md` — this approved scope and method;
- `query-plan.md` — Query Strategist deliverable;
- `query-log.md` — every attempted query family, venue, date, result quality, useful source IDs, redundancy, failed access, and follow-up term;
- `sources.md` — source ledger;
- `observations.md` — observation ledger;
- `findings.md` — theme matrix, contradictions, leading/rejected hypotheses, confidence, and proposed synthetic test;
- `limitations.md` — coverage, source dependence, transfer limits, access failures, and claims withheld.

The source ledger must record: source ID; URL or stable location; title/publisher; publication date; access date; venue; geography; population/context as disclosed; method as disclosed; source family; evidence type; relevant scope; access limitation; and whether the material is firsthand, survey-reported, official, academic, vendor-reported, or researcher-observed.

The observation ledger must record: observation ID; source ID; job-search stage; context; concise compliant paraphrase; direct source statement versus researcher observation; interpretation if any; supporting or disconfirming status; confidence; and unresolved question. Do not copy long quotations, usernames, or personal details.

## Evidence-quality rules

- Open and inspect the source before recording it. Search snippets, autocomplete, rankings, result counts, AI summaries, and inaccessible pages are not evidence.
- Prefer disclosed-method academic or qualitative work, official statistics/reports, transparent surveys, and detailed firsthand accounts with enough context to interpret them.
- Treat anonymous posts, reviews, influencer material, vendor surveys, marketing pages, and support discussions as limited evidence. A review describes an experience, not a general product property.
- Count materially independent source families rather than posts. The same author, thread, publisher, survey, dataset, press release, or republished story is not independent corroboration.
- Record positive cases, negative cases, workarounds, contradictions, and failed searches. Never search only for confirming language.
- Label Singapore evidence separately from international evidence and state transfer limits. Recent publication does not make older underlying behaviour current.
- Record only sensitive characteristics explicitly disclosed by a source when relevant to the approved question; never infer age, disability, immigration status, health, income, ethnicity, or similar attributes.
- Do not claim prevalence, comparative burden, demand, usability, willingness to pay, hiring impact, or causality from this convenience corpus.
- Preserve unknown, inaccessible, conflicting, and outdated information rather than filling gaps with model inference.

## Stopping rule and handoff

Stop when:

1. each hypothesis has recurring evidence or an explicit gap;
2. any hypothesis proposed for the next synthetic test has at least two materially independent source families, including a disclosed-method or otherwise well-contextualized source where available;
3. at least one contradiction, positive case, failure mode, or disconfirming search is recorded for each leading hypothesis;
4. the major job-search stages in scope are represented or marked unresolved; and
5. another 30-minute block is unlikely to change the shortlist, source-quality assessment, or next test.

If the rule is not met within the time box, stop with the gap documented. Move to a synthetic workflow or low-fidelity prototype when the remaining uncertainty concerns flow, recovery, evidence presentation, or surface capability. Do not continue browsing to simulate user validation. Direct research remains a separately authorized future option and is not part of this run.

## Required handoff

Return the source ledger, observation ledger, query log, theme matrix, leading and rejected hypotheses, evidence confidence, contradictions, limitations, and one recommended next synthetic test. State clearly that no direct user validation occurred and that product scope, platform, stack, automation level, pricing, and final decisions remain open.
