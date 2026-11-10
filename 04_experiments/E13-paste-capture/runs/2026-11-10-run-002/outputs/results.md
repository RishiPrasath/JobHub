# Run-002 (POST HOC) held-out robustness check

Snapshot step: snapshot-step 0.1.0 (E13, deterministic), unchanged from run-001.

## deterministic snapshot step

- title: 7/10
- employer: 8/10
- pay: 9/10
- duties: 8/10
- closing: 8/10
- all five fields right on 2/10 pastes
- partial pastes flagged: 2/3  ([('HP1', ['cut_off']), ('HP2', ['no_body']), ('HP3', [])])
- false flags on the 10 full pastes: 3/10  ([('H02', ['cards_nav']), ('H07', ['no_body']), ('H10', ['no_body'])])
- field errors:
  - H01 pay: gold missing, got present, value 'SGD 3,800'
  - H02 closing: gold present, got missing, value None
  - H03 title: gold present, got missing, value None
  - H03 employer: gold hidden_labelled, got missing, value None
  - H05 title: gold present, got missing, value None
  - H06 title: gold present, got missing, value None
  - H06 closing: gold explicit_absence, got missing, value None
  - H07 duties: gold present, got missing, value None
  - H09 employer: gold hidden_labelled, got present, value 'Private Advertiser'
  - H10 duties: gold present, got missing, value None
- closing date value errors (id, got, gold): [('H02', None, '2026-11-28')]

## LLM check (qwen/qwen3.8-27b)

- title: 10/10
- employer: 10/10
- pay: 10/10
- duties: 10/10
- closing: 10/10
- all five fields right on 10/10 pastes
- partial pastes flagged: 3/3  ([('HP1', ['cut_off']), ('HP2', ['no_body']), ('HP3', ['cards_nav'])])
- false flags on the 10 full pastes: 1/10  ([('H01', ['cards_nav'])])
- field errors:
- closing date value errors (id, got, gold): []