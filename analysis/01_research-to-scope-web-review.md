# Web research review: turning research into scope

Date: 2026-10-19 (Singapore time)

Status: complete — bounded methods review

## Question

What is the most responsible and effective way for a solo product owner to convert JobHub’s existing research into meaningful product opportunities, features and scope while working with AI agents?

## Research method

The coordinator created an initial draft first, then ran a planner and query-strategy pass followed by four parallel web-research specialists:

- Evidence Synthesizer
- Product Strategist
- UX and research-to-scope specialist
- Quality and AI-evaluation specialist

All specialists performed read-only public-web research and returned structured handoffs. No specialist edited repository files or made product, platform, stack or provider decisions.

## Main findings

### 1. Start with a decision, not a topic or feature

Research should state what decision it needs to inform, what is uncertain, and what would change the decision. Discovery is allowed to conclude that more research, a prototype, a different solution or no product is the right next step.

### 2. Keep the analytical chain visible

The robust chain is:

```text
Observation → interpretation → need → desired outcome
→ opportunity → competing hypothesis
→ smallest coherent learning slice
→ experiment → evaluation → human scope decision
```

Evidence should not jump directly from “people do X” to “build feature Y.”

### 3. Provenance belongs at source and claim level

The source register should identify canonical studies, datasets, reports, pages and syndicated copies. The claim ledger should show the exact source, context, method, supporting and contradicting evidence, limitations, relevance and next test. Repeated webpages are not independent corroboration.

### 4. Contradictions and uncertainty are useful outputs

Triangulation means comparing independent methods, populations and contexts—not accumulating agreeing sentences. Contradictions should remain visible with their possible cause: different population, period, method, measure, source lineage or genuine disagreement.

### 5. Prioritise consequences and uncertainty, not a magic score

Use transparent categories:

- **Must learn** — could invalidate the opportunity.
- **Must test** — desk research cannot answer the behavioural or performance question.
- **Must control** — privacy, accessibility, fairness, factuality, safety or irreversible-action risk.
- **Safe to defer** — useful but reversible, dependent or low consequence.
- **Out of scope** — unsupported or intentionally excluded.

Numbers may expose disagreement, but should not pretend to replace owner judgment.

### 6. The smallest slice must be a complete user episode

It is not simply the fewest screens. It includes context, input, output, explanation, uncertainty, missing/conflicting/stale states, interruption, recovery, correction, accessibility, user control and evaluation.

### 7. AI should accelerate analysis, not become the authority

Appropriate bounded uses include extraction, clustering, duplicate detection, contradiction flags, candidate themes, draft opportunity statements and test preparation. AI must not silently determine prevalence, user priority, final confidence, scope or risk acceptability.

### 8. Move from traces to repeatable evaluation

During exploration, retain traces of sources, prompts, tool calls, outputs, handoffs and human corrections. Once expected behaviour is understood, create a versioned evaluation set containing ordinary, ambiguous, incomplete, contradictory, cross-industry, sensitive, adversarial and “unknown” cases. Re-run evaluations when the prompt, model, retrieval, tool, source data or rubric changes.

## Recommended JobHub operating model

```text
1. Decision brief
2. Context-and-journey episode
3. Source register and evidence ledger
4. Needs and desired outcomes
5. Opportunity map with competing hypotheses
6. Assumption and risk map
7. Prototype/experiment card
8. Evaluation and decision record
9. Scope option and non-goals
10. Implementation slice and regression set
```

### Minimum evidence-to-scope gate

Do not accept a capability into scope until it has:

- a named user/context and desired outcome;
- source-linked evidence and explicit uncertainty;
- at least one competing interpretation or solution;
- a stated riskiest assumption;
- a smallest credible test or baseline;
- success, harm, stop and revisit conditions;
- review, correction, recovery and accessibility considerations;
- an owner-approved non-goal and decision record.

## Key trade-offs

| Trade-off | Recommended handling |
|---|---|
| Traceability vs speed | Full claim-level records for consequential decisions; lightweight links for routine notes. |
| Narrow slice vs complete journey | Keep the slice small, but include the user episode’s critical handoffs and failure states. |
| Framework consistency vs context fit | Reuse the artefacts, adapt the method to the question and evidence. |
| AI speed vs human ownership | Let AI accelerate bounded work; require human verification at evidence, opportunity and scope transitions. |
| Prototype realism vs cost | Increase fidelity only where interaction, trust, accessibility or AI interpretation is the uncertainty. |
| Quantitative score vs judgment | Use categories and rationale; do not hide decisions behind a composite score. |

## Recommended next action for JobHub

Do not begin by writing a feature backlog. Use the completed research to produce two or three traceable opportunity statements, each with competing hypotheses. Select one high-consequence user episode and test two low-fidelity concepts or a manual baseline. Then create the first scope decision record.

The first decision should be: **which user episode is important and uncertain enough to test next?** It should not yet be: **which full application should we build?**

## Source register

### Official service and discovery guidance

- [GOV.UK: Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service)
- [GOV.UK: Analyse a research session](https://www.gov.uk/service-manual/user-research/analyse-a-research-session)
- [GOV.UK: User research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery)
- [GOV.UK: How discovery works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)
- [GOV.UK: How alpha works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works)
- [GOV.UK: Making prototypes](https://www.gov.uk/service-manual/design/making-prototypes)
- [GOV.UK: Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories)
- [GOV.UK: AI Playbook](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html)

### Evidence and synthesis methods

- [Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14)
- [NIH mixed-methods best practices](https://obssr.od.nih.gov/sites/g/files/mnhszr296/files/Best_Practices_for_Mixed_Methods_Research.pdf)
- [GRADE-CERQual](https://www.cerqual.org/overall-confidence-in-the-evidence/)
- [PRISMA 2020](https://www.prisma-statement.org/prisma-2020)
- [W3C PROV](https://www.w3.org/TR/prov-primer/)
- [EQUATOR COREQ](https://www.equator-network.org/reporting-guidelines/coreq/)

### Product discovery and prioritisation

- [Design Council Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond)
- [Strategyzer Assumptions Mapping](https://www.strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter)
- [Product Talk Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/)

### AI evaluation, governance and accessibility

- [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OpenAI agent evaluations](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [OpenAI guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)
- [W3C involving users in accessibility evaluation](https://www.w3.org/WAI/test-evaluate/involving-users/)
- [W3C WCAG 2.2](https://www.w3.org/TR/wcag/)

## Limitations

These methods sources do not establish JobHub demand, the first segment, the greatest burden, willingness to use, willingness to pay or the correct first workflow. Formal evidence-synthesis methods transfer to traceability and uncertainty management, but not every rule is a universal product-discovery law. Participant and prototype testing remain necessary before accepting a product scope.
