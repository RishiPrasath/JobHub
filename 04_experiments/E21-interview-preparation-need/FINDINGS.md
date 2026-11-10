# E21 findings: interview preparation need

Run: `runs/2026-11-10-run-001`, 2026-11-10. Affects FEAT-015, ASM-015.
Written by the coordinator from the specialist's final report (8 personas), because the specialist could not save report files. This replaces an earlier 5-persona draft that had been written into this folder by another session.

Status: **Part A not run with participants.** Only a SIMULATED instrument pilot ran, with 8 personas. Simulated figures are not evidence about job seekers.

## Thresholds

| Threshold (verbatim from README, frozen in `protocol/thresholds.md`) | Observed with participants | Verdict |
|---|---|---|
| Pass: at least half name a concrete preparation gap the tools they already use did not meet, and at least a third say they would practise inside a tool that knows the posting and their profile | none | **Inconclusive: not run with participants** |
| Fail: fewer than a quarter name an unmet gap, or most use existing tools and are satisfied with them | none | **Inconclusive: not run with participants** |
| Inconclusive: anything between | none | Part A not run |

No verdict is computed from the simulated figures below.

## What ran

- The protocol was written and frozen with sha256 hashes in `protocol/FROZEN.md` before the first model call: thresholds verbatim, the interview guide and the coding scheme. There are no gold labels in an interview study, so the scheme and the keyword coder were frozen instead.
- 8 simulated personas (creator `openai/gpt-oss-120b`, answers `openai/gpt-oss-20b`): 2 career switchers, 2 non-office workers, 1 foreign professional, 1 older low-digital-comfort person, 1 intended "never prepares", 1 heavy-AI graduate. Three calls per persona, 30 calls, 34,640 tokens.

## Simulated figures (n = 8; hypotheses only; the specialist's reading)

- 6 of 8 prepared specifically for the role; all used free resources.
- 8 of 8 named a concrete gap, and 8 of 8 named one that the tools they used did not meet.
- 7 of 8 were only partly satisfied with the tools they used; 1 used none.
- 4 of 8 had tried an AI mock interview, and all 4 stopped ("generic" or "scripted").
- On question 8 as worded: 1 clear yes, 2 conditional, 1 unsure, 4 no. On the neutral version (8N): 2 of 8 wanted practice or a tool.
- 8 of 8 raised recording or storage worries.
- S-23 was raised 6 times, S-24 once, S-25 once.
- The keyword coder agreed with the specialist's reading on 60% of codes, so it is not usable as the real coder.

## Instrument problems (the most useful output)

- Question 3 makes a "gap" nearly certain, which is why all 8 named one.
- Question 8 describes the feature. It did not inflate answers here, but the personas were sceptical, so this says nothing about real people.
- Question 1 stacks three questions. Question 5 presumes the person wanted to prepare more.
- S-23 is too broad to discriminate between stories.
- Question 9 (personas critiquing the guide) produced invented complaints.
- Persona fidelity failed twice: the "never prepares" persona did prepare, and the warehouse persona degenerated into repeated sentences.
- The persona set clusters on privacy worry and partial satisfaction.

## Deviations

1. The brief caps pilots at 6 personas; this one used 8 because the task needed them. The owner has not confirmed that.
2. Another process stopped the runner at 5 of 8 personas, and `answers.json`, `usage.json` and a draft FINDINGS appeared in the folder. The 5-persona versions were kept as `*_partial_5of8.json`, and the run resumed from the cache. The first 5 personas' answers are identical in both versions.
3. A bug in `tools/llm_client.py` (a Windows `PermissionError` under lock contention) crashed the runner once. The runner was rerun from the cache. The coordinator has since fixed the client.
4. Nothing is committed to git.

## Limitations

- Simulated personas share a model, have no real interviews and no stakes.
- 8 personas support nothing about prevalence.

## Feasibility recommendation for FEAT-015

**Inconclusive.** Keep scope `candidate`, need level N0, proposed feasibility T0. The pilot makes the feature neither more nor less worth testing, and it is not evidence of need. It does sharpen what to ask real people:

- Is role-specific preparation, especially for non-office and technical roles, under-served?
- Does anyone use an app, or do they use a person?
- Ask about recording early.
- Ask what people did, not what they would do. Ask the tool question last, after the neutral version.
- Include people who never prepare and people with low digital comfort.
- Reword questions 1, 3 and 5, and split S-23.

## Next actions

1. Revise the interview guide as above, then recruit 8 to 10 real job seekers for Part A.
2. Decide whether to keep FEAT-015 as `candidate` or set it to `later`.
