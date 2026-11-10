# E21: interview preparation need

Status: run 2026-11-10 (reduced; see [FINDINGS.md](FINDINGS.md)). Thresholds were treated as confirmed by the owner's instruction to run and frozen by hash, not committed to git.
Affects: FEAT-015, ASM-015

## Question

How do job seekers prepare for interviews today, what tools do they already use, and is there an unmet gap that practice inside JobHub could fill better than existing tools?

FEAT-015 is not treated as feasible, or even needed, until this has run. The feature has no recorded evidence (N0, T0), no mapped user stories, and the standalone interview feature is deferred in the [decision log](../../strategy/08_decision-log.md). The related stories are rated weak: S-23 (feel prepared for behavioural and role questions), S-24 (explain a career switch when probed) and S-25 (know the assessment format). R04 lists interview practice among the defensible AI uses, with controls: practice and post-session feedback only, and consent, retention and policy checks. Its failure modes are formulaic feedback, transcription errors and unsafe live assistance. At this stage the riskiest assumption (ASM-015, "practice here beats existing tools") cannot be tested head to head, so this experiment tests the need first.

Scope stays `candidate` (owner decision 2026-11-10: keep it, and plan a need interview).

## Hypotheses

- **H1 (need):** job seekers feel under-prepared for specific parts of interviews and name something concrete they could not get ready for.
- **H2 (existing tools):** the tools they already use leave a gap that practice grounded in the posting and their own profile could fill.
- **H3 (fit):** some would practise inside a job-search tool that knows the posting and their profile, rather than elsewhere.

## Part A: need interviews

Needs 8 to 10 job seekers who had at least one interview in the last 6 months, recruited by the owner. A mix of experience levels, at least two career switchers, and at least two who applied to non-office roles. Can be the same people as other experiments if the sessions are kept separate.

### Design

A structured interview about the most recent interview:

- What the role and the process were (rounds, format, panel or one person)
- How they prepared, how long it took, and what they used (friends, videos, articles, AI assistants, mock-interview tools, nothing)
- What was hardest and which questions they were not ready for
- Whether anything about the format surprised them
- What they would have wanted before the interview, and what stopped them preparing more
- Whether they have used an AI mock interview, what it was like, and why they stopped or continued
- Their feelings about recording voice or video and about where answers are stored
- Whether they would practise inside a tool that knows the posting and their profile

### Measures

- Share who prepared specifically for this role, and how
- Tools and resources used, and cost
- Share who name a concrete thing they could not prepare for
- Share who have tried an AI mock interview, and the reasons for continuing or stopping
- Share who would practise inside a tool that knows the posting and their profile
- Concerns about recording and storage
- Which of S-23, S-24 and S-25 is actually raised by participants

### Proposed thresholds (Part A)

Set before running.

- **Pass:** at least half name a concrete preparation gap that the tools they already use did not meet, and at least a third say they would practise inside a tool that knows the posting and their profile.
- **Fail:** fewer than a quarter name an unmet gap, or most use existing tools and are satisfied with them.
- **Inconclusive:** anything between.

Participants consent to notes. Notes avoid names and employer identities.

## Part B: head-to-head practice test (only if Part A passes)

**Not planned in detail.** If Part A passes, a second step compares practice with an existing assistant against practice grounded in the posting and the participant's profile, with the Part A gaps as the criteria. Its design, thresholds and consent and retention rules for any recording are decided after Part A reports.

## How the result is used

| Outcome | What it does to FEAT-015 |
|---|---|
| Part A pass | Evidence at N3 (direct accounts) for the need. Design Part B and define the feature. The owner sets any levels. |
| Part A inconclusive | Narrow the questions to the gap that appeared, or park. |
| Part A fail | Set to `later` or `out`. Out needs a recorded owner decision. |

## Layout

- `protocol/` interview guide and the committed thresholds
- `data/` notes, coded by theme (no names)
- `FINDINGS.md` results against thresholds, deviations and limitations

None of these exist yet.

## Out of scope

Building any practice tool, live interview assistance (R04 advises against hidden live help), employer verification, and negotiation of offers.

## Decisions for the owner before the run

1. Confirm or change the sample and the thresholds.
2. Decide who recruits participants, and whether they overlap with other experiments.
3. Confirm consent and note-taking rules.

## Deviations

None yet.

## Limitations

- 8 to 10 interviews support direction, not statistics.
- Participants are self-selected and recall may be imperfect.
- Stated willingness to use a tool is not behaviour.
- Singapore-specific interview formats are not covered beyond what participants describe.
- This does not test whether practice improves interview outcomes.
