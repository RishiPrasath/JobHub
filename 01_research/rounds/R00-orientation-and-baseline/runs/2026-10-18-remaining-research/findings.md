# Integrated findings — remaining desk research

Date: 2026-10-18. Coordinator synthesis of four specialist investigations, the coordinator's official Codex/GitHub review, and two earlier reviewed research runs. Recommendations are **proposed**, not approved product requirements. Review disposition is recorded in [review.md](review.md).

## Main recommendation

Move from broad desk research to a small evidence-led learning cycle: observe a recent job-search episode, compare two plausible workflow concepts, then implement one approved slice with a short behavior brief and independent checks. This addresses the owner's concern about slow specification without outsourcing UX or engineering judgment.

There is enough desk evidence to design that next cycle. There is not enough evidence to select the strongest user segment, prove a durable competitive gap, choose the final surface/stack, or forecast hiring gains. The [coverage matrix](coverage.md) maps every backlog question and both drafts' topic groups to the reports and residual evidence needs.

## Reconciled product findings

The [Singapore friction study](../2026-10-18-job-search-friction/findings.md) supports bounded hypotheses about application uncertainty and practical working conditions; it does not rank the greatest burden. Its assessment-effort hypothesis is weaker. The [AI workflow study](../2026-10-18-ai-job-hunting-workflows/findings.md) describes mixed tool/manual practices and documented product overlap, not universal improvement from AI. Neither validates capture-and-return as the primary problem.

The [product specialist](product-market.md) proposes comparing adjacent-occupation preparation with frontline condition comparison. The [UX specialist](ux-and-accessibility.md) proposes comparing an interruptible responsive journey with a capture companion. These answer different questions: **what problem/people** versus **how to support the journey**. Do the problem check first; do not make phone capture a requirement merely because it is an appealing demo.

The coordinator recommends testing one role at a time: preserve the opportunity, understand requirements and uncertainty, connect truthful experience, choose a next action and return without losing context. This is a coherent experimental slice, not an approved MVP. Include explicit no-build alternatives: an improved manual template, an existing career product or human coaching. If participants mostly need access to opportunities, workable schedules or employer feedback, application drafting may not address the principal problem.

### Candidate product choices

| Choice | Recommendation to test | Alternative / evidence that changes it |
| --- | --- | --- |
| Initial audience | Compare operations/administration transitions and frontline/service contexts; include returners, graduates and varied access needs | Choose by observed consequential friction and reachability, not vacancy counts or simulated personas |
| Value proposition | Evidence-backed understanding and truthful preparation | If existing tools work adequately, improve a workflow/template rather than build another platform |
| Fit guidance | Explain requirement, candidate evidence, uncertainty and possible next action | Do not infer hiring probability; preserve correction and the choice to pursue an opportunity |
| Company analysis | Identity, dated evidence and useful questions | Defer reputation synthesis if source conflicts create unsupported warnings |
| Surface | Compare responsive and capture-companion concepts using the same task | Native/PWA/extension only if necessary capabilities and user benefit justify maintenance; phone-only preparation remains a research need |
| Commercial model | Evaluate free useful access with optional episodic or sponsor-supported value | Subscriptions, pricing and partner demand remain unvalidated; do not sell identifiable candidate information |

Evidence and detailed alternatives: [product/market](product-market.md), [UX/accessibility](ux-and-accessibility.md). Market positioning is a hypothesis. Public JobHub name overlap warrants clearance work before launch, but the user's chosen working name is unchanged. The old idea document's AI-persona naming votes are not human research.

## Reconciled development findings

The [development specialist](development-method.md) reviewed all three supplied playbooks and contrasted their guidance with empirical and practitioner sources. The evidence does not support declaring one method universally fastest. The common useful direction is traceable intent, bounded changes, real verification and measurement of the whole delivery path, including review and repair.

Propose a lightweight hybrid: one short slice brief; examples for normal, missing and failed/interrupted behavior; a prototype when interaction is uncertain; tests from agreed expectations; a small implementation; review and owner teach-back; a recorded acceptance or rejection. Increase specification when ambiguity repeatedly causes rework or when a choice is expensive to reverse. Reduce documentation that merely restates other artifacts.

Gherkin is a way to express examples; Cucumber can execute mapped scenarios; BDD includes the collaborative discovery of behavior. Trial executable scenarios for stable, important repeated behaviors. Plain-language examples linked to ordinary tests remain a viable lower-overhead alternative. The report includes a minimal specification template, scenario illustration, quality gates, debt/rollback rules and a proposed local comparison—not a completed productivity experiment.

For ownership, the user should be able to explain why the flow is understandable, where data goes, what can fail, what a test establishes and how the change is reversed. Agents can draft alternatives, tutor, implement and challenge assumptions; agreement among agents does not replace a source, test or human decision.

## Reconciled technical and agent findings

The [technical specialist](technical-and-responsible-ai.md) recommends a versioned source/claim contract before a stack choice. Keep captured evidence, user-confirmed experience, inference and unknown/conflicting values distinct. Preserve capture completeness and failure reasons so an extraction failure does not become “the employer did not disclose this.” Let deletion and lawful retention obligations override a desire for permanent historical snapshots.

Local, cloud and hybrid approaches each have meaningful costs. Local storage does not mean data stays local if a remote model is called; cloud continuity requires operational controls; hybrid adds sync/deletion complexity. Test with synthetic material before introducing personal data. Capture rights, provider policies and privacy obligations require source/product-specific review; a user upload, robots permission or “not used for training” label is not a universal authorization or zero-retention guarantee.

Model selection should compare the same tasks against a deterministic/manual baseline. Score supported claims, missing-data handling, usefulness and correction effort; measure full cost and latency including retries. Provider names and benchmark popularity do not establish a winner for JobHub. No model benchmark or production security evaluation ran in this study.

The [coordinator's Codex report](codex-and-delivery.md) distinguishes portable role Markdown from native registration. Live inspection found no project `.codex` directory, although this research successfully used native subagents. Current official setup and local CLI version are documented without installing configuration. Assign disjoint tasks, require actual source/tool evidence, keep shared interfaces coordinator-owned, and check integrated results. Use GitHub controls appropriate to the repo/plan when implemented; no remote settings were changed.

## Conflicts retained and confidence

- Faster AI drafting and higher overall delivery effort can coexist. Older controlled studies and newer limited follow-ups do not establish today's local effect.
- Convenience from more automation competes with truthfulness, verification effort and authority. Prefer explicit states and reversible actions; do not infer submission from preparation.
- Evidence preservation competes with minimization, rights and deletion. Preserve permitted versions with declared lifetimes, not unlimited copies of all source material.
- Mobile capture may help some people, but forcing preparation onto a laptop can exclude others. Device capability documentation does not answer user preference.
- Broad inclusion and a small first scope are compatible only when scope limits and unsupported cases are explicit. Avoid presenting cross-industry aspirations as evaluated coverage.
- A current source publication date does not make an older study's behavior current. Official documentation supports capability/policy claims, not product efficacy.

Confidence is high in narrow inspected documentation and local filesystem/CLI observations, moderate in the proposed process and risk controls, and low/unmeasured for demand, market superiority, usability, willingness to pay and actual operating performance. No human acceptance, legal clearance, model winner, platform selection or launch readiness is inferred.

## Finish disposition

Stop general desk collection for this pass. Use the six bounded [validation activities](validation-next.md), prioritising V01 problem observation and V02 flow comparison; V03 existing-tool comparison can run alongside them with synthetic data. V04 and V05 follow only when a technical experiment or implementation slice is authorised. V06 commercial/launch work is not a prerequisite to drawing a low-fidelity prototype.

This is a decision-ready research package, not a requirement to approve all proposals at once. The smallest next owner decision is which problem hypothesis to test first. The reports and proposed decision register make the trade-offs reviewable without reopening every research topic.
