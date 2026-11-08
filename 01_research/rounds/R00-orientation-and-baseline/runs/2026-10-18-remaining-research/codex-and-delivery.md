# Codex, context and GitHub delivery

Date/access date: 2026-10-18. Coordinator research using the AI SDLC Advisor, Prompt Engineer and Decision Record Keeper responsibilities. Covers R-13 and parts of R-11/R-14/R-15. Recommendations are proposed, not configured or accepted.

## Answer

Keep the portable role library, use Codex's native delegation when independent work warrants it, and give each task explicit context, ownership and verification. Add native project agent definitions only as a separate setup change. Do not build another orchestration framework merely to coordinate this repository.

## Observed local state

- `AGENTS.md` supplies coordinator/specialist rules; `_agents/README.md` lists 16 portable roles. These are instructions, not evidence that 16 custom native agent types are registered.
- `Test-Path .codex` returned `False`. No project-local native configuration was present during this inspection. User/global configuration was not audited.
- The resolved CLI is `C:/Users/prasa/AppData/Roaming/npm/codex.ps1`; `codex --version` returned `codex-cli 0.163.0`. Its help documents `--search`, `--strict-config`, `--worktree`, and the `agents` session browser. Help output alone does not test custom-agent loading.
- This research used real native spawn tools with four independent child agents and disjoint Markdown outputs. Role instructions were supplied in each task; no claim is made that these were custom registered role types.
- `_prompts/00_research-kickoff.md` is a plan/approval template. The user's current instruction authorises this continuation; it is not necessary to ask for the same research approval again. Future external writes and consequential decisions remain separate.

## Official capability findings

**C01 — native subagents.** Current documentation describes built-in `default`, `worker`, and `explorer` agents and project custom agents in `.codex/agents/*.toml`. Required fields are `name`, `description`, and `developer_instructions`. Permissions, provider and MCP servers inherit from the parent; a role's “read-only” prose is not a separate sandbox. Global controls include `agents.enabled` and `agents.max_concurrent_threads_per_session`; `agents.max_threads` remains a legacy alias. Current releases enable subagents by default. Availability in a particular older CLI still requires verification. [Official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

**C02 — configuration/search.** Project `.codex` configuration is loaded only for trusted projects. The current guide documents `cached`, `indexed`, `live` and `disabled` web modes; live is also requested with `--search`. Enabling a search tool does not prove a researcher used it. Require search/open activity and a source register. [Configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic).

**C03 — instructions.** Codex discovers global and project `AGENTS.md` guidance, with closer directory guidance overriding earlier guidance; the documented default combined budget is 32 KiB. This is instruction discovery, not specialist registration. [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

**C04 — skills.** Skills progressively expose their description and then their full instructions when selected. That supports reusable procedures without placing every procedure into root instructions. [Skills documentation](https://developers.openai.com/codex/skills/).

## Proposed context ownership

| Artifact | Keep here | Avoid |
| --- | --- | --- |
| Root `AGENTS.md` | Stable boundaries, source precedence, validation conventions | Whole strategy, every specialist definition, temporary task status |
| `_agents/` | Portable responsibilities and handoff contracts | Claims of tool availability or executable permissions |
| Future `.codex/agents/` | Thin runtime-specific identity/configuration referring to relevant role | Full duplicated role text that drifts independently |
| `_prompts/` | Bounded repeatable task, context paths, non-goals, evidence and checks | Secrets, copied private resumes, implicit external-write permission |
| Dated research run | Sources, claims, dissent and executed work | Unlabelled future plans represented as findings |
| Strategy / decision log | Accepted choices and rationale, linked to evidence | Promoting an agent recommendation into user approval |

These are coordinator recommendations based on this repository's existing separation, not a required OpenAI folder taxonomy. Add an owner, last-verification date and revisit trigger to volatile guidance. Supersede important decisions with a new linked record rather than silently rewriting their rationale. Load only the role and source sections required for the current question.

## Proposed handoff contract

Before delegation, record: question; input paths/version; required sources; output path; permitted actions; protected files; acceptance checks; time/source budget; and escalation boundary. Require the child to return findings, evidence, uncertainty, commands/tests actually executed, files changed, and next action.

Use a single agent for short tasks or dependent decisions. Use parallel specialists for independent evidence collection, disjoint implementation slices, or distinct review angles. Use sequential handoffs for scope → design → implementation → review when the next step depends on the previous result. Start with 3–5 only where justified by the repository policy; it is a coordination budget, not a documented platform limit.

The coordinator owns shared contracts and final integration. Assign one writer per file; also identify semantic dependencies such as shared data schemas even when files differ. A second model agreeing is not independent evidence. Reviewers should check sources/tests or attempt a counterexample, not merely endorse prose.

## GitHub delivery proposal

**C05 — worktrees.** Git supports several working trees attached to one repository, each with its own checked-out state and index; repository data is still shared. Worktrees separate edits but do not remove semantic integration conflicts. [Git worktree manual](https://git-scm.com/docs/git-worktree).

For future implementation, use one scoped branch/worktree per independent change when isolation helps. Record the base commit and handoff artifact; integrate in dependency order. Check the combined result, not just each worker's patch. Do not create worktrees for every read-only researcher. Preserve existing uncommitted changes; do not use destructive resets for coordination.

**C06 — merge controls.** GitHub documents required checks/reviews, stale-review handling, and bypass controls; availability depends on repository visibility and plan. These mechanisms are not evidence they are enabled here. [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

Propose a small PR contract: user outcome, linked acceptance cases, scope/non-goals, evidence for behavior, test output, risk/rollback, and owner explanation. Human approval remains required for commits/pushes/PR changes/releases in this repository. For a solo owner, avoid configuring a second-person review requirement they cannot satisfy; choose feasible checks and explicit owner acceptance.

**C07 — CI safety.** GitHub recommends least-privilege tokens, careful secret handling and avoidance of untrusted code in privileged workflow contexts. Its current secure-use guide recommends dependency lockfiles where supported, with full-commit SHA pinning as a fallback. [Secure use of Actions](https://docs.github.com/en/actions/reference/security/secure-use).

Propose CI without production credentials for untrusted changes, reviewed workflow/dependency changes, synthetic fixtures, and redacted logs. An AI-generated test or CI file must not acquire deployment authority implicitly. These are future controls, not an audit of an existing application or hosted repository settings.

## How to evaluate this workflow

Compare one representative task performed sequentially with a similar bounded parallel task. Record elapsed delivery time, owner review time, rework, duplicated investigation, conflicting edits, missed acceptance cases, total usage/cost when observable, and whether the owner can explain the resulting decision. Do not credit parallelism for merely producing more text. A small pilot is diagnostic, not a causal productivity estimate.

For prompt/context regression, prepare a normal case, missing-evidence case, conflicting-source case, malicious-source instruction, and an attempted out-of-scope edit. Check that the output preserves uncertainty and authority boundaries. Test context changes as well as model changes. These tests are proposed; this run did not execute a coding benchmark or configuration smoke test.

## Sources and limitations

| ID | Source inspected | Date/version and scope | Limitation |
| --- | --- | --- | --- |
| C01 | Official subagents page linked above; custom schema, availability, permissions | Living docs; publication date not shown; accessed 2026-10-18 | Current docs can differ from installed CLI; no configuration installed/tested |
| C02 | Official config basics; project trust and web modes | Living docs, date not shown | Defaults do not prove effective settings or tool usage |
| C03 | Official AGENTS.md discovery | Living docs, date not shown | No audit of global instructions/configuration |
| C04 | Official skills introduction/progressive disclosure | Living docs, date not shown | Mechanism guidance, not a measured context-quality benefit |
| C05 | Git worktree description and commands | Living manual; version-specific feature history not audited | Isolation is not merge correctness |
| C06 | GitHub protected-branches overview/review requirements | Living docs, date not shown | Repo plan and settings not inspected remotely |
| C07 | GitHub secure-use reference, secrets/untrusted code/dependencies | Living docs, date not shown | Future design guidance, not security certification |

Search initially returned OpenAI API multi-agent pages; those were not substituted for Codex CLI configuration. A Markdown rendition of AGENTS.md docs failed with unsupported content type; the HTML page was opened instead. Source content was read through native web tools. The OpenAI Docs skill guided official-source verification. Local commands were read-only; no credentials or personal configuration contents were printed.

Confidence: high for observed files/CLI output and the cited documentation at access time; moderate for the proposed operating model; unmeasured for productivity. Revisit after CLI upgrades, permission changes, repeated context failures, or two delivery slices showing coordination overhead outweighs benefit.
