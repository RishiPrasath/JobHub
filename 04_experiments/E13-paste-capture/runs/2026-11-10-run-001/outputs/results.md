# Scored results (2026-11-10-run-001)

Snapshot step: snapshot-step 0.1.0 (E13, deterministic)

## Verdicts

| Threshold | Observed | Verdict |
|---|---|---|
| T1 >=80% of 30 pastes contain all minimum fields | 19/30 = 63.3% (gold labels) | inconclusive |
| T2 >=90% of 10 partial pastes flagged | 10/10 = 100.0% | pass |
| T3 <=2 false flags on 30 complete pastes | 1/30 | pass |
| T4 stale rule correct on 100% of test snapshots | rule table 33/33; end to end 120/120; combined 153/153 | pass |
| T5 100% of snapshots restore to original | 40/40 | pass |

Part A overall: inconclusive

## Completeness of the 30 pastes (gold labels) by board

| Board | n | all fields | % | missing fields |
|---|---|---|---|---|
| mcf | 9 | 8 | 88.9 | {'title': 1, 'employer': 1, 'pay': 1, 'closing': 1} |
| jobstreet | 8 | 3 | 37.5 | {'pay': 3, 'closing': 4} |
| fastjobs | 6 | 3 | 50.0 | {'closing': 3, 'employer': 1} |
| company | 7 | 5 | 71.4 | {'pay': 2, 'closing': 1} |

By job type:

| Job type | n | all fields | % | missing fields |
|---|---|---|---|---|
| professional | 8 | 4 | 50.0 | {'title': 1, 'employer': 1, 'pay': 4, 'closing': 2} |
| clerical | 6 | 2 | 33.3 | {'closing': 4, 'pay': 2, 'employer': 1} |
| manual | 6 | 5 | 83.3 | {'closing': 1} |
| contract | 3 | 3 | 100.0 | {} |
| part-time | 4 | 2 | 50.0 | {'closing': 2} |
| gig | 3 | 3 | 100.0 | {} |

Gold-missing by field (of 30): {'title': 1, 'employer': 2, 'pay': 6, 'duties': 0, 'closing': 9}

## System: deterministic snapshot step

- pastes scored: 30 complete-set, 10 partial-set
- predicted complete: 19/30; gold complete 19/30; agreement on complete/incomplete 30/30
- partial pastes flagged 10/10 (missed: []); by type {'cut_off': {'flagged': 4, 'of': 4}, 'no_body': {'flagged': 3, 'of': 3}, 'cards_nav': {'flagged': 3, 'of': 3}}
- false flags on complete pastes 1/30: {'P29': ['cut_off']}

Field accuracy (3-class state) on the 30:

| Field | correct | % |
|---|---|---|
| title | 30/30 | 100.0 |
| employer | 30/30 | 100.0 |
| pay | 30/30 | 100.0 |
| duties | 30/30 | 100.0 |
| closing | 30/30 | 100.0 |

Field errors:


By board:

| Board | n30 | field correct | false flags | partials flagged |
|---|---|---|---|---|
| company | 7 | {'title': '7/7', 'employer': '7/7', 'pay': '7/7', 'duties': '7/7', 'closing': '7/7'} | 1 | 3/3 |
| fastjobs | 6 | {'title': '6/6', 'employer': '6/6', 'pay': '6/6', 'duties': '6/6', 'closing': '6/6'} | 0 | 1/1 |
| jobstreet | 8 | {'title': '8/8', 'employer': '8/8', 'pay': '8/8', 'duties': '8/8', 'closing': '8/8'} | 0 | 3/3 |
| mcf | 9 | {'title': '9/9', 'employer': '9/9', 'pay': '9/9', 'duties': '9/9', 'closing': '9/9'} | 0 | 3/3 |

## System: LLM check (qwen/qwen3.8-27b)

- pastes scored: 13 complete-set, 5 partial-set
- predicted complete: 10/13; gold complete 10/13; agreement on complete/incomplete 13/13
- partial pastes flagged 5/5 (missed: []); by type {'cut_off': {'flagged': 4, 'of': 4}, 'no_body': {'flagged': 1, 'of': 1}, 'cards_nav': {'flagged': 0, 'of': 0}}
- false flags on complete pastes 0/13: {}

Field accuracy (3-class state) on the 30:

| Field | correct | % |
|---|---|---|
| title | 13/13 | 100.0 |
| employer | 13/13 | 100.0 |
| pay | 13/13 | 100.0 |
| duties | 13/13 | 100.0 |
| closing | 13/13 | 100.0 |

Field errors:


By board:

| Board | n30 | field correct | false flags | partials flagged |
|---|---|---|---|---|
| company | 0 | {'title': '0/0', 'employer': '0/0', 'pay': '0/0', 'duties': '0/0', 'closing': '0/0'} | 0 | 1/1 |
| fastjobs | 0 | {'title': '0/0', 'employer': '0/0', 'pay': '0/0', 'duties': '0/0', 'closing': '0/0'} | 0 | 1/1 |
| jobstreet | 4 | {'title': '4/4', 'employer': '4/4', 'pay': '4/4', 'duties': '4/4', 'closing': '4/4'} | 0 | 1/1 |
| mcf | 9 | {'title': '9/9', 'employer': '9/9', 'pay': '9/9', 'duties': '9/9', 'closing': '9/9'} | 0 | 2/2 |

## Variant: union of partial flags

- partial flagged 5/5 (missed []); false flags 0/13 []

## Stale rule

- rule table: 33/33; failures: []
- end to end: 120/120; failing snapshots: []
- closing date extraction correct on 30/30
- notice includes re-paste prompt: True

## Integrity

{'restore_equals_original': 40, 'stored_equals_original': 40, 'of': 40, 'with_crlf': 3, 'with_nbsp': 3, 'with_zero_width': 2}