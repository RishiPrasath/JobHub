# Development method: small, reversible, human-owned increments

Date/access date: 2026-10-18. Status: reviewed desk-research recommendation; human acceptance pending. One collector applied AI SDLC Advisor, Quality Engineer and Full-Stack Developer perspectives. Subsequent independent reviews and corrections are recorded in `review.md`.

## Scope and evidence discipline

This report addresses R-11, R-12 and engineering-learning aspects of R-15. Stack and scope remain undecided. Codex orchestration belongs to the coordinator; security, privacy and model evaluation belong to the technical workstream.

Inspected repository context: root `AGENTS.md`; `_agents/README.md` and roles 09, 10 and 14; this run's [brief](brief.md); research instructions 00, 01 and 06 and their index; the research backlog; both the [AI-era draft](../../../../../_drafts/ai-era-development-strategy.md) and [strategy](../../../../../01_strategy/03_ai-era-development-strategy.md); and the [earlier workflow findings](../2026-10-18-ai-job-hunting-workflows/findings.md). Earlier findings supply candidate examples, not validated demand. This report avoids repeating job-seeker or competitor research.

Native web searches covered METR productivity, DORA, Cucumber/BDD and canonical TDD; source pages were then opened. **Observed** below means inspected documentary content. **Reported** means a source author's result or experience, not our experiment. **Recommendation** means this report's synthesis. No software, user interviews, method trials or vendor benchmarks were run.

## What the evidence supports

**Observed/reported — supplied playbooks.** Anthropic proposes a traceable chain of intent, specification, implementation and verification artifacts across six nonlinear stages. Its testing guidance emphasizes actual tool output, reproducing failures and preventing a coding agent from weakening its checks. These are vendor practices, not comparative proof that its lifecycle is best. Its assertion that an unchanged regression test proves a bug is gone is too strong: it establishes the tested case, not every manifestation. Recommendation: adopt traceability and early feedback provisionally; retain human inspection of consequential code and test adequacy. [D01](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)

Atlassian emphasizes context, measurement and changes across planning, design, development, review and maintenance. It reports internal issue-cycle improvement from 11.5 to 6.7 days. The inspected article does not provide a controlled design establishing attribution, and enterprise context infrastructure is not evidence that JobHub needs an organizational graph. Recommendation: measure the whole path to accepted work and maintain relevant context; do not import its platform investment as a prerequisite. [D02](https://www.atlassian.com/blog/ai-at-work/ai-sdlc-transformation-playbook)

Ran Isenberg advocates structured artifacts and repeated planning, stakeholder validation and execution, while acknowledging specification overhead, nondeterminism and disproportionate process for small changes. His governance architecture is practitioner guidance with enterprise assumptions, not a demonstrated productivity intervention. Recommendation: retain bounded tasks and human acceptance; scale documentation to uncertainty and consequences. All three supplied articles exposed substantive text, including LinkedIn's governance, challenges and conclusion; no login workaround was needed. Embedded visual examples were not independently inspected. [D03](https://www.linkedin.com/pulse/ai-driven-sdlc-how-build-secure-governed-scalable-withai-ran-isenberg-99nuf/)

**Reported — independent counterweight.** METR's randomized study involved 16 experienced maintainers and 246 tasks in familiar open-source repositories. AI-allowed work took 19% longer, despite participants perceiving a speedup. That supports skepticism about perceived speed, not a universal claim about novices, new projects or current models. [D04](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

METR's February 2026 update reports later estimates suggesting improvement, but explicitly calls the signal unreliable: participant/task selection, changed compensation and concurrent-agent timing complicate interpretation. Both reported subgroup intervals include no effect. Do not turn this into either a permanent slowdown claim or a confirmed current speedup percentage. [D05](https://metr.org/blog/2026-02-24-uplift-update/)

DORA's March 2026 analysis reports verification overhead and learning concerns from 1,110 open-ended Google-engineer survey responses collected in Q3 2025. It also reports the 2025 association between higher AI adoption, increased throughput and increased instability. These are different evidence streams, not randomized causal findings. Google Cloud runs DORA, so it is complementary primary research, not vendor-independent corroboration. Its public questionnaire clarifies that delivery outcomes include respondent estimates. [D06](https://dora.dev/insights/balancing-ai-tensions/)

**Synthesis — moderate confidence:** faster drafting can coexist with slower acceptance or poorer understanding. None of these studies decides the fastest process for this owner. The appropriate target is accepted, maintainable behavior per unit of total effort, with owner comprehension protected.

## Compare approaches by uncertainty and risk

These approaches can be combined.

| Approach | Useful application in JobHub | Main cost or failure mode | Recommended use |
| --- | --- | --- | --- |
| Heavyweight specification | Stable cross-component contracts, difficult migrations, consequential rules | Premature certainty, duplicated documents and review burden | Add detail for a particular high-consequence change after the owner resolves choices |
| Lightweight/hybrid | One agreed user outcome with a few explicit examples | Unrecorded assumptions if “lightweight” means vague | Default experiment: short spec, narrow implementation, proportional verification |
| Prototype-first | Uncertain interaction or feasibility | A convincing demo becomes production by accident | Time-box a learning question, use synthetic data, label disposable code and record a promotion decision |
| TDD | Deterministic transformations, state transitions, reproducible defects | Tests encode the same wrong assumption as code | Start with expected cases, run one failing test, implement, then refactor |
| BDD | Ambiguous domain behavior needing shared agreement | Ceremony without stakeholder conversation | Discuss concrete examples first; automate selected stable examples |

Böckeler's firsthand SDD exploration distinguishes spec-first, spec-anchored and spec-as-source, and reports excessive artifacts for small tasks. It is a dated practitioner exploration, not a controlled tool ranking. Maintaining a small behavioral specification does not require treating generated code as untouchable. [D09](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

Beck describes TDD as an iterative programming workflow, not writing every test upfront. He explicitly cautions against deriving expected test values by copying actual output. This supports independent expectations; it does not establish TDD's superiority for every task. [D10](https://newsletter.kentbeck.com/p/canon-tdd)

## Gherkin is not Cucumber, and neither is BDD

**Observed — high confidence:** BDD concerns collaborative discovery, formulation and automation of behavior examples. Gherkin is a structured language for those examples. Cucumber connects scenario steps to executable step definitions; readable text alone does not exercise software or assert correctness. BDD does not require reducing every conversation to syntax, and using Cucumber does not demonstrate shared understanding. [D07](https://cucumber.io/docs/bdd/), [D08](https://cucumber.io/docs/gherkin/reference/)

**Recommendation:** begin with plain-language examples. Trial executable scenarios when a rule is stable, consequential, repeatedly checked, understandable to the owner and supported by deterministic assertions. Candidate examples include preserving the source on save, recovering an interrupted operation and distinguishing missing evidence from a negative finding. These remain candidate behaviors pending scope approval.

Illustration, not an executed test:

```gherkin
Feature: Preserve uncertainty in a saved posting
  Scenario: Salary is absent from the supplied source
    Given a synthetic posting with no salary information
    When I save and reopen the posting
    Then the salary is shown as "Not provided"
    And the source URL is preserved
```

A useful implementation must check persisted/reopened state and the exact fixture URL, not merely find a success message. Keep the scenario about behavior; avoid button coordinates and chains of page-specific clicks. Prefer lower-level checks for many input combinations, with a small workflow check across real boundaries.

Skip the extra executable-language layer for volatile layouts, disposable prototypes, trivial formatting and rules already clearly maintained in ordinary tests. An alternative is a Markdown example table linked to normal automated tests. Retain Cucumber only if the owner actually reviews scenarios and their agreement/regression value exceeds step-definition upkeep. Track scenario repair time, duplicate steps, flaky runs and defects detected; remove redundant scenarios without removing needed behavioral coverage.

## Proposed lifecycle, responsibilities and gates

1. **Explore:** the owner chooses the problem and learning question; AI offers alternatives and uncertainties. If desired behavior is unsettled, make a disposable prototype. Exit with an owner-selected slice or a documented reason to stop.
2. **Specify:** AI drafts the short template below; the owner corrects outcomes and examples. A reviewer challenges missing/failure cases. Exit when behavior and exclusions are understandable. Material scope, architecture and privacy choices remain human decisions.
3. **Implement:** one bounded change exercises the relevant interface, logic and data boundaries. AI may draft code/tests and explain trade-offs. Exit with a reviewable diff, actual verification results and declared omissions; limit concurrent work to review capacity.
4. **Verify:** review against agreed examples independently of the implementation narrative. Inspect boundary behavior, failure recovery and applicable accessibility checks. Any specification change receives explicit behavioral review; silently rewriting expectations to obtain green tests fails the gate.
5. **Accept and learn:** the owner demonstrates the outcome, explains important behavior and accepts or rejects it. Record debt and recovery instructions. Commits, external writes, deployment and releases require the repository's explicit human authorization. Observe later defects and correction effort before expanding automation.

### Minimal slice specification

```text
Slice ID / date / owner / status:
User outcome and evidence supporting it:
In scope / explicitly out of scope:
Inputs and source-of-truth; relevant existing decisions:
Expected behavior: normal, missing/invalid, interrupted/failure:
2-4 concrete examples with expected results:
Affected boundaries and constraints; unresolved human decisions:
Verification: assertion, fixture, method and evidence to retain:
Recovery: how to disable/revert; data compatibility considerations:
Acceptance owner; learning question; links to tests and decision record:
```

Keep one behavior record per slice, linking shared constraints. Update it with behavior changes and explain superseded decisions. For tiny defects, a failing example and fix note may suffice. Expand design for material choices or interface contracts.

### Test independence and proportionate quality

Expected outcomes should originate in human-reviewed requirements, controlled fixtures or external contracts. AI may propose cases, but implementation output must not become its own oracle. Ask a separate review pass to derive missing cases from the spec before inspecting implementation; a fresh agent context reduces shared narrative but does not establish statistical independence or guarantee correctness.

For meaningful defect fixes, demonstrate failure before repair and success afterward. Keep acceptance expectations stable during repair, while allowing reviewed corrections to genuinely wrong tests. On critical logic, try a deliberate wrong value or removed check to confirm the assertion detects the fault; do not add mutation machinery for every low-risk change.

Use focused logic tests for rules; integration tests for storage and service boundaries; a few realistic workflow checks for continuity; manual exploratory and accessibility checks for interactions. For probabilistic features, deterministic UI/schema assertions need separate human-reviewed content evaluation; an exact generated sentence is usually a poor contract. Record commands, fixture/version, observed results, failures and untested areas. Green checks demonstrate covered behavior, not usefulness or production readiness.

### Debt and recovery

Before acceptance, record each deliberate shortcut: affected behavior, reason, owner, consequence, repair trigger and verification needed. Repeated repairs or an unexplained abstraction trigger simplification before another feature. Review new dependencies and duplicated logic for necessity, without choosing a stack here.

Document the last known working state and a scoped revert/disable procedure. Code rollback may not reverse stored-data changes; compatibility and recovery need explicit design before such changes. For the initial experiment, favor isolated synthetic fixtures and changes removable without migration. A failed acceptance check means repair or withdraw the slice, not accumulate follow-on work on an uncertain foundation.

## Workflow experiment and owner engineering learning

**Recommendation, not an executed study:** choose six small, comparable tasks in three pairs: a deterministic rule, a workflow boundary and a UI/error-state change. Compare minimal acceptance notes plus ordinary tests against the short hybrid spec plus selected scenarios. Randomize order within pairs; keep model/tool version, review criteria and task complexity recorded. Do not solve the identical task twice and attribute familiarity gains to method. Add one heavier-spec comparison only if an actual cross-cutting change warrants it.

Record per task:

| Measure | Operational definition |
| --- | --- |
| Accepted value | Owner-accepted behavior meeting the same gates; exclude unfinished drafts |
| Total effort and elapsed time | Specification, prompting, coding, review, repair and verification minutes separately; distinguish waiting and overlapping agent time |
| Review/rework | First-review findings by severity, review minutes, revision rounds, and repairs within seven days |
| Maintenance | Scenario/test/document repair minutes after one planned behavior change; flaky failures and escaped defects |
| Owner explainability | Without AI, explain input-to-output flow, one failure path, test rationale and rollback; score each 0 absent, 1 partial, 2 accurate |
| Experience and cost | Friction notes, predicted versus actual completion time, tool cost and reasons for abandoned tasks |

Proposed continuation rule: keep the hybrid if comprehension and correctness hold and effort improves or resolves consequential ambiguity. Retain scenarios that aid review or detect regressions with acceptable upkeep. Serious regressions, weakened expectations or unexplained recovery override speed gains. Six tasks provide local learning, not statistical proof; publish individual outcomes and differences.

Build owner capability through the same slices: trace one input through interface, validation, logic and storage; predict a test result before execution; reproduce and diagnose one failure; explain why a dependency exists; rehearse a scoped rollback on synthetic work. Ask AI for hints before solutions and use teach-back afterward. Revisit weak concepts on the next slice. The objective is practical judgment and debugging ownership, not memorizing generated code or personally typing every line.

## Source register and limitations

All URLs were opened on 2026-10-18. Dates are displayed publication/update dates; unversioned pages may change. Primary-source provenance does not establish effectiveness.

| ID | Source, date/version and inspected scope | Confidence and limitation |
| --- | --- | --- |
| D01 | [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), Louis Claxton, 2026-08-21; lifecycle/artifact overview, intent, verification and review passages | High for stated advice; low for transferable effectiveness; vendor, selected sections |
| D02 | [Atlassian playbook](https://www.atlassian.com/blog/ai-at-work/ai-sdlc-transformation-playbook), 2026-10-01; context, measurement and planning-through-maintenance sections | Internal outcomes reported; causal attribution and JobHub transfer unverified |
| D03 | [Isenberg article](https://www.linkedin.com/pulse/ai-driven-sdlc-how-build-secure-governed-scalable-withai-ran-isenberg-99nuf/), 2026-02-06; accessible article through references, especially governance and limitations | Practitioner proposal; embedded screenshot details uninspected |
| D04 | [METR original study summary](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 2025-07-10; method, results, caveats and FAQ | Strong bounded randomized evidence; paper/raw data not reanalyzed |
| D05 | [METR update](https://metr.org/blog/2026-02-24-uplift-update/), 2026-02-24; results, selection issues and redesign | High confidence in authors' stated limitations; weak current effect estimate |
| D06 | [DORA analysis](https://dora.dev/insights/balancing-ai-tensions/), 2026-03-10; method, trade-offs and recommendations; [2025 questionnaire](https://dora.dev/research/2025/questions/) delivery-outcome items | Observational/self-report evidence; enterprise population and Google affiliation limit transfer |
| D07 | [Cucumber BDD](https://cucumber.io/docs/bdd/), displayed update 2026-10-17; discovery/formulation/automation | High definitional confidence; advocacy, not comparative outcome evidence |
| D08 | [Gherkin reference](https://cucumber.io/docs/gherkin/reference/), displayed update 2026-10-17; syntax, examples, steps and metadata | High syntax confidence; no runner installed or example executed |
| D09 | [Böckeler SDD exploration](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html), 2025-10-15; taxonomy and observations on overhead | Firsthand but limited trials, dated tool versions; no current ranking |
| D10 | [Beck, Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd), 2023-12-11; workflow and assertion pitfalls | Primary method explanation; not an AI productivity experiment |

Additional DORA access trail: opened the [report index](https://dora.dev/research/2025/dora-report/), [overview](https://dora.dev/research/2025/) and [Google Cloud download page](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report?hl=en&region=US). The full-report link led to a contact form; no form was submitted and no full PDF is claimed inspected. D06's accessible primary analysis and questionnaire are the alternate evidence. No supplied playbook was blocked at article-text level.

Missing evidence: the owner's measured baseline, longitudinal maintenance cost, actual scenario readership, current-model causal productivity on comparable tasks, and production recovery performance. No source resolves these locally. Recommended next action is human review of this bounded experiment, followed by authorized implementation; desk-research completion is not final acceptance.

Verification: all four local Markdown targets resolve; D01-D10 are present; no trailing whitespace found. Only this report was created. No subagents, commits, external mutations, software tests or usability tests occurred.
