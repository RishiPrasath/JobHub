# E21 coding scheme (v1, frozen before the simulated pilot)

One row per participant. Codes are assigned per participant from the whole transcript. Two coders were intended for real data; for the pilot the coder is (a) the keyword script `harness/code_answers.py` and (b) the specialist's reading. Disagreements are listed, not hidden.

## Codes

| Code | Values | Rule |
|---|---|---|
| `prep_for_role` | `specific`, `generic`, `none` | `specific`: researched this employer, role or posting and prepared answers to it. `generic`: general question lists, videos or advice, not tied to this role. `none`: did not prepare. |
| `prep_methods` | multi: `friends_family`, `videos`, `articles`, `ai_assistant`, `mock_tool`, `coach_agency`, `own_notes`, `none` | Everything the participant says they used. |
| `prep_cost` | `free`, `paid`, `unstated` | `paid` only if money was spent. |
| `gap_named` | `yes`, `no` | `yes` only if the participant names a concrete thing they could not prepare for or were not ready for (a question type, a format, a part of the process). A feeling alone ("I was nervous") is `no`. |
| `gap_type` | multi: `behavioural`, `role_technical`, `switch_story`, `assessment_format`, `process_unknown`, `other`, `none` | What the gap was about. Used only when `gap_named` is `yes`. |
| `tool_satisfaction` | `satisfied`, `partial`, `dissatisfied`, `no_tools` | How the participant describes the resources they used, for what they needed. `no_tools` if they used none. |
| `gap_unmet` | `yes`, `no` | Matches the Part A measure. `yes` = `gap_named` is `yes` AND (`tool_satisfaction` is `partial`, `dissatisfied` or `no_tools`). A gap named but described as met by the tools used is `no`. |
| `tried_ai_mock` | `yes`, `no` | Has used an AI mock interview or similar practice tool (not a general chat assistant for tips). |
| `ai_mock_outcome` | `continued`, `stopped`, `na` | And the stated reason, written in free text. |
| `would_use_posting_tool` | `yes`, `conditional`, `no`, `unsure` | Answer to question 8 as asked. `yes`: clear willingness with a reason that is not just agreement. `conditional`: yes only under a stated condition (free, no recording, short). |
| `would_use_neutral` | `named_tool_or_practice`, `other_help`, `nothing` | Pilot only. From question 8N: whether, unprompted, they would want practice or a tool for it. |
| `recording_concern` | `none`, `voice_video`, `storage`, `both`, `unstated` | Question 7. |
| `story_raised` | multi: `S-23`, `S-24`, `S-25`, `none` | Raised BY THE PARTICIPANT before any probe. `S-23`: feeling prepared for behavioural and role questions, or knowing who will interview. `S-24`: explaining a career switch when probed. `S-25`: knowing an assessment's format before taking it. |

## Part A measures computed (simulated pilot figures, labelled)

- Share `prep_for_role` = `specific`.
- Share `gap_named` = `yes`; share `gap_unmet` = `yes`.
- Share `tried_ai_mock` = `yes`; counts of `continued` and `stopped`.
- Share `would_use_posting_tool` = `yes` (strict) and `yes` or `conditional` (loose).
- Count of each `recording_concern`; count of each `story_raised`.

No verdict (pass, fail, inconclusive) is computed from the simulated figures. Part A is "not run with participants".
