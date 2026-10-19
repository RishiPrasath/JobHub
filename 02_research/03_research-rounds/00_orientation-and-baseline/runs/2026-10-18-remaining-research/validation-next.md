# Empirical validation handoff

Prepared 2026-10-18. These activities are **not executed results**. Desk research cannot establish actual user demand, platform preference, willingness to pay, extraction accuracy or engineering productivity for JobHub. This is the finite follow-on validation queue, not a request to keep browsing indefinitely.

## Common rules

The human owner approves the activity, scope and data handling before any later participant recruitment, purchases, private uploads or external actions. V01 uses public material only; later synthetic or participant-based activities use synthetic or explicitly consented examples. Participation and recording are separate choices. Explain purpose, recipients, storage location, retention/deletion date and withdrawal limits. Remove third-party details. Identifiable notes, resumes, recordings and transcripts do not belong in Git or agent prompts by default.

Recruit for variation rather than claiming statistical representativeness from a tiny pilot. Include non-IT/service/operations work, career transitions/returns, different digital confidence and relevant access needs. Do not infer disability, immigration status or sensitive attributes from a resume. Offer accessible participation and alternative formats. Record barriers individually; a high aggregate success rate must not hide exclusion. Participants can skip sensitive questions and stop.

Before V02–V04, obtain the owner's explicit age-scope decision and verify compatibility with any selected service. V01 uses public material and does not recruit or process participants, but public sources still must not be used to infer age or sensitive attributes. Propose adults only for later product/prototype research; this does not decide eventual product eligibility. If youth participation or likely youth product access is intended, perform a separate provider, safeguarding and consent review. Consent cannot override provider restrictions. Do not collect identity-document copies merely to administer later research.

Use a hypothesis card with: decision, baseline, predicted observation, disconfirming observation, scope, permissions, stop conditions and evidence. Define acceptance before inspecting results, but treat small-sample numeric thresholds as provisional planning aids, not population estimates.

## V01 — public user-insight research

**Primary:** Job-Seeker Practices Researcher. **Support:** Job Domain Researcher. **Review:** Responsible AI Reviewer and Product Strategist.

Question: which recurring job-search problem deserves the first synthetic workflow or low-fidelity prototype, and is interrupted capture/return one of the problems supported by public evidence?

Execute the [web-based user-insight brief](../../../01_public-web-user-insights/runs/2026-10-18-web-based-user-insights/brief.md) using public Reddit/forum material, public product reviews, public survey reports, academic or qualitative studies, public blogs/video transcripts and public support discussions. Search across job-search stages and contrasting contexts. Do not contact authors, enter private groups, profile individuals or infer sensitive attributes. Record short compliant paraphrases, source context, date, method and evidence type in a source register and observation ledger.

Output: recurring themes, friction/workarounds, counterexamples, access needs, AI-use patterns, contradictions and an explicit candidate hypothesis comparison. Continue only if at least two materially independent source families support a leading hypothesis and additional searching is still changing the shortlist. Do not treat post counts as prevalence, public opinions as representative users, or this activity as direct validation. Feed the strongest hypothesis into V02 or a synthetic workflow test.

## V02 — compare continuity and surface options

**Primary:** UX and User-Flow Designer. **Support:** UX Expert. **Review:** Quality and Evaluation Engineer.

Using fictional postings, compare the same capture → interruption → resume → next-action task through a low-fidelity responsive flow and a share-entry/mobile concept, with desktop preparation also available. Run the comparison as an owner-led scenario walkthrough and heuristic review because direct users are unavailable. Counterbalance order where feasible. Prototype only enough capability to test the decision; make simulated capabilities explicit. Later run an actual device/browser capability spike before assuming install, incoming share, notification or offline support.

Check whether the flow makes it possible to recover context, distinguish saved from applied, locate the evidence, correct missing information and explain the next action. Record ambiguities, dead ends, failure recovery and correction effort, not just completion speed. Test keyboard, zoom/reflow and available assistive technology separately from visual preference. Treat this as expert/owner review, not usability evidence; preserve every accessibility concern for later validation.

Decision: choose a product surface only after identifying which capabilities materially change completion and whether the maintenance burden is justified. A failed native-feature spike does not justify excluding that user need; evaluate fallback and another surface.

## V03 — compare existing tools and proposed workflow

**Primary:** AI Tools Expert. **Support:** Competitive Landscape Researcher. **Review:** Evidence Synthesizer and Responsible AI Reviewer.

Reuse the [synthetic workflow fixture](../../../../05_evidence/datasets-and-examples/2026-10-18-synthetic-workflow-check.md). Compare the user's simple baseline (notes/spreadsheet and manual preparation), one accessible general assistant, one career-specific product, and a prototype only if one exists. Record exact date, product/tier/model when disclosed, settings, prompt, sources and output. Free access first; no subscription purchase or real application submission without separate authority.

Evaluate capture fidelity, unsupported candidate claims, changed/missing posting facts, evidence visibility, correction time, export/recovery and state accuracy. Repeat generative tasks to expose variability. Do not generalize from one lucky answer or provider marketing. A proposed JobHub flow earns priority only if it improves a meaningful outcome without unacceptable review burden, exclusion or loss of control.

## V04 — capture, privacy and model feasibility

**Primary:** Technical Architect. **Support:** Quality and Evaluation Engineer and AI Tools Expert. **Review:** Responsible AI Reviewer.

Use synthetic or permissioned fixtures across ordinary HTML, dynamic/blocked pages, duplicate/changed/expired jobs, pasted text and OCR errors. Include malicious instructions, ambiguous salary currency/period, mandatory-versus-preferred requirements, credential uncertainty, and contradictory company evidence. The pipeline should preserve an honest failure state and usable fallback rather than invent missing fields. Do not bypass access controls or scrape at scale.

Compare deterministic/manual baselines with candidate models on identical inputs. Measure field-level accuracy, supported-claim precision, abstention/missing handling, correction burden, latency distributions, total cost per accepted result including retries, and rate-limit recovery. Report counts and denominators. Keep ground-truth labels reviewable; calibrate model graders against human judgments and reserve holdout cases. Structural JSON validity alone is insufficient.

For any future working prototype, test cross-user access, deletion propagation (including derived data and declared backup lag), exports, redacted logs and approval enforcement. Proposed hard stop: unauthorized external action, fabricated candidate claim presented as confirmed, or private-data exposure in a controlled test. Zero observed failures is necessary for those fixtures, not proof of safety in deployment.

Test raw-original expiry separately from authorised evidence excerpts/crops and derived claims. A citation must resolve to retained evidence with an approved purpose/expiry, or explicitly show that verification evidence is unavailable; never treat a hash or image coordinates as a substitute for deleted content. For any provider's grounded retrieval, review feature-specific display, storage, reuse and evaluation permissions before building a reusable evidence ledger or sharing outputs with another model.

## V05 — try the lightweight development method

**Primary:** AI SDLC Advisor. **Support:** Prompt Engineer and Full-Stack Developer. **Review:** Quality and Evaluation Engineer; owner explains the result.

After a slice is approved, use the canonical six-task protocol in [the development report](development-method.md): three comparable task pairs contrasting minimal acceptance notes/ordinary tests with a short hybrid specification/selected scenarios. Randomize order within pairs, do not repeat an identical solved task, and record task differences and learning effects. A specification-heavy comparison is optional only when a real cross-cutting change warrants it; it is not the main comparator. Record specification, implementation, review, test and rework time separately. Try executable Gherkin only where behavior is stable and repeated; track scenario maintenance rather than counting scenarios.

The owner should explain the data flow, key trade-off, failure handling, tests and rollback without reciting generated text. If explanation or verification is weak, improve the slice and tutoring before increasing autonomy. Continue the method if accepted quality and understanding improve relative to total effort; increase specification for recurring ambiguity, security-sensitive boundaries or expensive reversals.

Keep two Codex follow-ups separate from that method comparison:

- **V05a — conditional setup verification.** Only after a native-agent setup change is authorised, validate configuration against the installed CLI and start a fresh test session. Confirm the intended custom role is actually loaded, follows its designated task/output boundary and uses its expected available tools. Inspect concrete activity and output; the presence of a TOML file or a model's self-report is insufficient. Include a harmless conflicting-source/out-of-scope instruction to test the boundary. This is a setup smoke test, not proof of security isolation or a productivity gain. No configuration is changed by this research run.
- **V05b — orchestration comparison.** Following the [Codex report](codex-and-delivery.md), compare reasonably similar independent tasks under sequential and bounded parallel coordination while holding the chosen specification approach and acceptance checks stable. Measure total elapsed and owner review time, rework, duplicated investigation, semantic/edit conflicts, usage/cost where observable and missed acceptance cases. Do not simultaneously change models, scope and methodology and attribute the difference to parallelism. Small samples provide local diagnostic evidence only.

## V06 — sustainability, naming and launch constraints

**Primary:** Product Strategist with Competitive Landscape Researcher. **Review:** Decision Record Keeper; qualified legal/privacy advice where needed.

Test willingness to use and willingness to pay separately; hypothetical price approval is not payment behavior. Explore user-paid, time-bounded preparation packages and partner-supported access without giving partners identifiable candidate information. No outreach, payment experiment or public landing page is authorised by this research document.

Before public launch, perform scoped trademark/professional advice, domain/app-store/handle checks, source licence/terms review, provider/data-transfer review and a defined data-retention policy. Record date, jurisdiction, relevant goods/services and unresolved conflicts. Keep JobHub as the current working name unless the owner reopens it. Public name usage is a confusion signal, not a legal infringement finding.

## Handoff completion

Each executed activity creates its own dated run with source/artifact register, method, consent handling where applicable, observations, contradictions, limitations, review and proposed decision. The owner accepts or rejects the decision. Research documents alone do not authorise participants, paid tools, private uploads, implementation or release.
