# Agent Assignment and Coordination

## Core rule

Assign agents by the type of uncertainty they are qualified to investigate, not by the general topic label. A research team should have one accountable primary agent and distinct supporting roles.

## Role responsibilities

| Role | Use it for |
| --- | --- |
| Research Planner | Scoping questions, priority, method, evidence requirements, and stopping rules |
| Research Query Strategist | Search vocabulary, balanced query portfolios, source-seeking plans, retrieval risks, query logs, and search stopping rules |
| Job Domain Researcher | Job-search workflows, postings, sectors, labour-market context, and domain terminology |
| Job-Seeker Practices Researcher | Actual user behavior, daily routines, AI use, workarounds, stress, and abandonment |
| Competitive Landscape Researcher | Existing products, capabilities, positioning, pricing, and competitor gaps |
| Evidence Synthesizer | Source comparison, provenance, confidence, contradictions, and decision-ready synthesis |
| Product Strategist | Product implications, outcomes, scope, non-goals, and roadmap options |
| UX and User-Flow Designer | End-to-end flows, information architecture, cross-device continuity, and interaction risks |
| UX Expert | Usability, accessibility, content, cognitive load, and design critique/mentorship |
| Technical Architect | Architecture, data, integrations, privacy boundaries, reversibility, and technical trade-offs |
| AI SDLC Advisor | Development approach, agent workflow, specification, testing, and human-AI process |
| Quality and Evaluation Engineer | Acceptance criteria, evaluation datasets, testability, regression, and measurement |
| Responsible AI Reviewer | Privacy, fairness, safety, uncertainty, user control, and consequential-action risks |
| AI Tools Expert | Tool/model comparisons, workflow fit, cost, latency, privacy, portability, and lock-in |
| Prompt Engineer | Reusable prompts, context design, handoffs, and prompt evaluation |
| Decision Record Keeper | Decision provenance, rationale, consequences, dissent, and revisit conditions |
| Full-Stack Developer | Technical feasibility experiments and implementation-informed constraints after scope is approved |

## Research team matrix

| Task type | Primary | Support | Synthesis | Review |
| --- | --- | --- | --- | --- |
| Job-seeker workflow | Job Domain Researcher | Research Query Strategist, Job-Seeker Practices Researcher, UX and User-Flow Designer | Evidence Synthesizer | Product Strategist |
| Real-world AI use | Job-Seeker Practices Researcher | Research Query Strategist, AI Tools Expert, Job Domain Researcher | Evidence Synthesizer | Responsible AI Reviewer |
| Competition and positioning | Competitive Landscape Researcher | Research Query Strategist, AI Tools Expert, Job Domain Researcher | Evidence Synthesizer | Product Strategist |
| Product surface and cross-device behavior | UX and User-Flow Designer | Research Query Strategist, Job-Seeker Practices Researcher, Job Domain Researcher | Evidence Synthesizer | UX Expert, Product Strategist |
| Accessibility and intuitiveness | UX Expert | Research Query Strategist, UX and User-Flow Designer, Job-Seeker Practices Researcher | Evidence Synthesizer | Quality and Evaluation Engineer |
| Job-posting and company evidence | Job Domain Researcher | Research Query Strategist, Technical Architect, Responsible AI Reviewer | Evidence Synthesizer | Quality and Evaluation Engineer |
| Candidate fit and recommendations | Product Strategist | Research Query Strategist, Job Domain Researcher, UX Expert | Evidence Synthesizer | Responsible AI Reviewer |
| AI-era development approach | AI SDLC Advisor | Research Query Strategist, Technical Architect, Quality and Evaluation Engineer | Evidence Synthesizer | Product Strategist, Decision Record Keeper |
| Gherkin and Cucumber | AI SDLC Advisor | Research Query Strategist, Quality and Evaluation Engineer, Full-Stack Developer | Evidence Synthesizer | Technical Architect |
| Codex and parallel agents | AI SDLC Advisor | Research Query Strategist, Prompt Engineer, Technical Architect, Decision Record Keeper | Evidence Synthesizer | Quality and Evaluation Engineer |
| AI tool/model selection | AI Tools Expert | Research Query Strategist, Technical Architect, AI SDLC Advisor | Evidence Synthesizer | Responsible AI Reviewer, Quality and Evaluation Engineer |
| Privacy, security, and responsible AI | Responsible AI Reviewer | Research Query Strategist, Technical Architect, Quality and Evaluation Engineer | Evidence Synthesizer | Product Strategist |
| Technical architecture | Technical Architect | Research Query Strategist, Full-Stack Developer, AI SDLC Advisor | Evidence Synthesizer | Responsible AI Reviewer, Quality and Evaluation Engineer |

## Coordination rules

- Parallelize only independent evidence collection. Do not parallelize conflicting edits to the same result file.
- Give each agent a bounded sub-question and a separate output location.
- Supporting agents must contribute a named angle; they should not repeat the primary agent's work.
- The Research Query Strategist normally works before or alongside evidence-collection specialists. It designs the retrieval plan and query log; it does not replace the primary researcher or Evidence Synthesizer.
- For the prepared public-web user-insight run, the order is strict: Research Planner → Research Query Strategist → bounded evidence collectors → Evidence Synthesizer → review. The Query Strategist is first after the Planner even when the Job-Seeker Practices Researcher remains the substantive primary role.
- In a solo-founder run, one person may perform several roles sequentially, but must keep the query plan, query log, source ledger, observation ledger, synthesis, and limitations as separate outputs. Do not create parallel searches that duplicate the same query family.
- The Evidence Synthesizer reconciles claims after parallel work. It does not erase disagreement.
- Product Strategist owns product implications; Technical Architect owns technical implications; Responsible AI Reviewer owns risk findings. None may silently override source evidence.
- Decision Record Keeper records the final human decision, not an AI recommendation as if it were approval.
- Prompt Engineer is added when the task will become repeatable or when prompt failure is itself under study.
- Full-Stack Developer is added for feasibility spikes, not as the default researcher for product questions.

## Minimum and maximum team sizes

- Small exploratory question: Research Planner + one primary agent.
- Normal research run: Research Planner + primary + one or two supports + Evidence Synthesizer.
- High-risk or cross-domain run: add the relevant specialist reviewer and Decision Record Keeper.
- Avoid assigning all agents by default. More agents increase coordination cost and can reduce clarity.

