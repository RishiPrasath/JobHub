Letters scored by every run (common set): L01, L03, L05, L08, L11, L12, L13

| run | letters | recall (planted found/planted) | false alarms | strict sourcing | controls flagged |
|---|---|---|---|---|---|
| openai_gpt_oss_20b__run1 | 7 | 10/11 | 2 | 12/12 | [] |
| openai_gpt_oss_20b__run2 | 7 | 10/11 | 3 | 7/11 | ['L01'] |
| qwen_qwen3_8_27b__run1 | 7 | 11/11 | 5 | 14/14 | ['L01', 'L03'] |

POST HOC sensitivity (not a verdict; gold labels unchanged). False alarms after removing (a) flags on an item that is part of a planted inconsistency in the same letter and (b) all C14 (leave) flags, where the letters list leave types incompletely in some profiles:

| run | letters | false alarms as scored | after removing (a) | after removing (a) and (b) |
|---|---|---|---|---|
| openai_gpt_oss_20b__run1 | 7 | 2 | 1 | 1 |
| openai_gpt_oss_20b__run2 | 9 | 5 | 3 | 3 |
| qwen_qwen3_8_27b__run1 | 10 | 8 | 6 | 1 |

Token use (new calls only, from run logs):
- openai_gpt_oss_20b__run1: {'prompt': 4585, 'completion': 932, 'total': 5517}
- openai_gpt_oss_20b__run2: {'prompt': 8841, 'completion': 3148, 'total': 11989}
- qwen_qwen3_8_27b__run1: {'prompt': 17939, 'completion': 3871, 'total': 21810}
- total of the three scored runs: 39316
