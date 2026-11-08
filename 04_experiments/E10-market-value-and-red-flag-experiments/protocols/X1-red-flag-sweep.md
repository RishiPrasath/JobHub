# X1: fixed red-flag sweep versus free-form research

**Question.** Does running the same fixed set of searches for every company find known public problems more often than a researcher who chooses their own queries?

**Why.** In experiment 09's agent test, one run found a regulator fine against an insurer's adviser arm with a specific query and a repeat run, with a generic query, missed it. The result depended on query wording.

**Hypothesis.** The fixed sweep finds more known problems than free-form research.

## Data (frozen before the arms run)
- **Known-problem companies (target 20).** Singapore organisations (not individuals) with an issue documented on an official list in the last five years, taken from the sources X0 marks go. Selection rule, to avoid cherry-picking: from each go source, take the most recent qualifying entries as of 2026-11-07, skipping individuals, organisations no longer operating, and non-Singapore entities, until about 7 per source. For each, record: company name as the official source gives it, authority, action type, year, official URL. The list is committed before any arm runs.
- **Controls (8).** Companies chosen before looking: Sheng Siong, Koufu, Persol Singapore, Charterhouse Resources, Randstad Singapore, Kyndryl Singapore, Activate Interactive, Temp-Team. Any control found on an official list in X0 is dropped and noted. Controls are used only to see what the sweep returns; absence from the lists does not prove a company is clean.

## Arms
- **Arm A, fixed sweep.** Six queries per company, exactly these templates (no OR, no boolean), name in double quotes, each run once through OpenSERP (DuckDuckGo first, Bing second), top 8 organic results kept (title, URL, snippet):
  1. `"<name>" Singapore regulator penalty fine`
  2. `"<name>" enforcement action Singapore`
  3. `"<name>" court judgment Singapore`
  4. `"<name>" complaints Singapore`
  5. `"<name>" retrenchment layoffs Singapore`
  6. `"<name>" scam fraud warning Singapore`

  A Haiku-model reader then receives only the saved results (titles, URLs, snippets) for that company and writes a list of red flags with the source URL for each. It does no searching.
- **Arm B, free-form.** A fresh Haiku-model agent receives only the company name and the instruction to find any red flags a job seeker should know about, with a budget of 8 searches and 4 page reads through OpenSERP. Wording is its own.
- Neither arm is told the official issue, authority or year. Arm A's query templates are fixed here and do not name any particular authority.

## Scoring (blind)
An issue is **found** by an arm if its report names the company and the action in substance: the authority or the type of action, and approximately when. The lead researcher scores with the arm label and company hidden from the scoring sheet where possible. Also recorded: for Arm A, whether the issue's official page or a page reporting it appeared among the retrieved results at all (**surfaced**); for the controls, every red flag each arm reports, checked by hand as supported, unsupported or about another company (**false alarms**); searches and time per company.

## Pass/fail (set before running)
- **Pass:** Arm A finds at least 60% of the known problems and exceeds Arm B by at least 15 percentage points.
- **Fail:** Arm A finds under 40%, or does not exceed Arm B.
- **Anything between** is inconclusive and reported as such.

## Limits stated in advance
Small sample (about 20). Known-problem lists favour serious public issues. Search results vary by day. Engines may throttle; if an engine's circuit breaker opens, the run pauses and the interruption is recorded.
