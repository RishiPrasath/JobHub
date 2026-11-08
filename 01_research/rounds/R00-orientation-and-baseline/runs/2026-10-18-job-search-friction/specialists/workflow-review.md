# R-01 UX and workflow review

Date: 2026-10-18. Status: supplied evidence reviewed; suitable for synthesis with the qualifications below. This is specialist review, not human acceptance of conclusions.

## Task, scope and inspected material

Review workflow transitions, effort, uncertainty, interruptions and access without choosing a platform or feature. Read `_agents/README.md`, `_agents/07_ux-and-user-flow-designer.md`, [approved brief](../brief.md), [domain handoff](domain.md) (D01–D06), [practices handoff](practices.md) (P01–P05), and [targeted pass](targeted-gap-pass.md) (G01–G02). No new external collection or independent reinspection of original sources was performed; source confidence is inherited from those handoffs. No observed portal session or directly observed seeker behaviour is present in the supplied evidence.

## Workflow scaffold and loops

This is an analytical scaffold, not a measured sequence shared by all seekers. Referrals may bypass discovery; several applications may run concurrently; pauses need not indicate failure.

| Moment and possible transition | Evidence-supported issue | Unresolved distinction |
| --- | --- | --- |
| Decide whether work is currently wanted and feasible → search, defer or seek support | Care and income constraints reported in P05/G02; non-participation context in D04/G01 | Desire, availability and ongoing care differ. Non-searching caregivers are not established prospective users. |
| Discover → evaluate requirements and working conditions → proceed or discard | Occupational conditions in employer reports D01; reported exclusion in advertisements D05; unclear expectations P02 | Actual unattractive/incompatible conditions versus unavailable information versus difficulty interpreting available information |
| Prepare → submit → assessments/interviews → continue or withdraw | Repeated preparation/assessments in P02/P04; application volume and stated discouragement in P01 | Necessary assessment versus avoidable rework; duration, reuse and actual abandonment remain unmeasured |
| Await response → follow up, revise approach, continue other searches or pause | Reported silence and uncertainty P01/P03; confidence burden P03/P04 | Employer intent, rejection reason and vacancy status cannot be recovered from silence alone |
| Offer/start → reassess feasibility or continue search | Supported employment conditions P05; temporary work not becoming permanent in P04 | Whether conditions changed, were undisclosed, misunderstood or were knowingly accepted |

Reported loops include generic applications → coaching/tailoring → further applications (P03), and interviews/tasks → rejection → continued search (P04). A broader loop from uncertainty to repeated ineffective effort is a hypothesis, not an observed causal mechanism. D03/D06 describe employment outcomes; they cannot identify which transition caused delay or loss.

## Findings, evidence and confidence

Separate three kinds of difficulty throughout synthesis:

- **Conditions or exclusion:** schedules, pay, strenuous work, care demands and reported discriminatory treatment (D01/D05/P05/G02). Better information might expose incompatibility earlier; it does not change the condition. D05 records reported discrimination, not adjudicated employer wrongdoing.
- **Information uncertainty:** unclear expectations and weak response signals (P01–P03). These reports support investigating uncertainty, but not a claim that job listings systematically omit decisive facts or that an AI system could infer hidden hiring criteria.
- **Process effort:** preparation, repeated assessments and presentations (P02/P04). Effort is reported; its size, avoidability and comparison with other stages are unknown. P01's stated discouragement is not measured abandonment.

Confidence is moderate that these distinct experiences occur within the sampled/reported groups; low for ranking their population burden or attributing outcomes to them. The same person may experience all three, so coding episodes should permit multiple causes while preserving their separate evidence.

Source-supported workarounds are coaching and changed application materials (P03), mentors for confidence (P03), friends' leads/professional contacts (P04), and employment support associated with workable hours, location and training in selected cases (P05). P02 reports a portfolio-building attempt initially without replies. These are reported actions or programme cases, not proven interventions; temporal success after help is insufficient evidence of effectiveness.

## Interruptions, accessibility and gaps

Caregiving constrains feasible work in P05/G02. Neither establishes that interruptions during an application cause lost form input, restart costs or abandonment. Those are research questions. No supplied evidence evaluates keyboard access, screen readers, text scaling, language comprehension, mobile constraints, device handoffs or low digital confidence. D05's insufficient disability responses cannot establish absence of barriers. No interface was inspected, and no accessibility compliance judgment is possible.

For future research planning, include assisted and offline steps and permit accessible participation modes. Ask how people resume an interrupted search and who helps them, without presuming digital self-service is their preferred or feasible route. Current collection remains weighted toward graduates and professionals; supported non-office cases add context but do not represent all service, trades or operational workers.

## Bounded validation hypotheses and questions

These are candidate explanations for direct study, not feature requirements or an ordered priority list.

| Hypothesis | Support and evidential limit | Specific questions and next method |
| --- | --- | --- |
| H1: Some active seekers repeat preparation without enough feedback to decide what to change. | P01–P03 support reported silence/uncertainty and changed tactics. P01 is a vendor poll; P02/P03 share publisher. Repetition caused by feedback gaps remains unproven. | Reconstruct two recent applications: what information was available at each decision, what changed, why, and what effort was repeated? Use a consented episode interview with optional redacted artifacts; distinguish recalled estimates from timestamped evidence. |
| H2: Some applicants accumulate substantial assessment effort before learning that an opportunity will not proceed. | P02 and independent publisher P04 illustrate repeated assessment and late rejection; neither measures burden or avoidability. A late rejection alone does not establish earlier feasibility could have been known. | Build a stage timeline for a progressed and a stopped application: active work versus waiting, requested tasks, expectations, feedback and decision points. Ask what could reasonably have been known earlier, and what would have changed the applicant's choice. A short prospective diary could reduce recall error in a later approved study. |
| H3: For some active seekers/people intending to return, feasible work is constrained by conditions that application preparation cannot resolve. | D01 employer reports, P05 selected programme evaluation and G02 qualitative caregiver study provide distinct perspectives. G01/D04 prevent equating non-participation with failed search. Timing of constraint discovery is unknown. | First establish intention and availability. Compare one pursued and one declined role: which conditions mattered, when/how were they learned, and was the problem incompatibility or missing information? Use episode interviews and an optional walkthrough of the participant's usual process; record care/income context only at the level necessary. |

Methods above are recommendations only. No recruitment, participant contact, prototype or implementation was performed or authorised by this review. A comparative ranking requires directly comparable burden evidence; no numerical priority score is justified now.

## Review disposition, risks and next action

Approved as an evidence-aware input to synthesis, with these required qualifications: preserve the three-way distinction above; retain source/publisher dependencies; label reported behaviour versus interpretation; do not infer missing listing information, actual abandonment, ghost vacancies, discrimination causes for outcome statistics, or a prospective-user population from caregiver totals. Keep accessibility/interruptions as gaps, and maintain the absence of a greatest-burden ranking. These are synthesis wording requirements, not a new approval gate.

The chief trade-off is that qualitative reports reveal possible mechanisms while official statistics clarify denominators but rarely explain the workflow. Combining them can inform questions, not establish causal or population-wide conclusions. Product decisions would be premature. The Evidence Synthesizer should reconcile this review with the collectors' handoffs and retain up to three explicitly provisional hypotheses for human consideration.

Files changed: only `specialists/workflow-review.md`. Validation: checked all cited IDs against supplied records; checked claims for causal overreach, population substitution, source dependence and unsupported UI observations. No software tests apply.

## Post-synthesis consistency check — 2026-10-18

Read [Evidence Synthesizer handoff](synthesis.md). It satisfies the prior UX qualifications: conditions, information uncertainty and effort remain distinct; H1's reported uncertainty is separated from its unproven repetition mechanism; H2 is explicitly below the burden-evidence threshold; and H3 retains bounded feasibility support without treating caregiver totals as users. It preserves source dependence, outcome/cause separation, unknown accessibility and interruptions, reported workarounds without causal effectiveness claims, and the unresolved greatest-burden question. No UX wording changes are required before the planned Product Strategist review and integration. Retain these qualifications in promoted results; this consistency check is not human acceptance or approval of product scope. Only this addendum was changed; no browsing or additional evidence collection occurred.
