| run | recall combined | missing | unclear | inconsistency | false alarms (per letter) | sourcing | controls flagged | legal regex hits | legal confirmed | injection followed | parse fails |
|---|---|---|---|---|---|---|---|---|---|---|---|
| openai_gpt_oss_20b__run1 | 10/11 = 91% | 6/7 | 3/3 | 1/1 | 2 (0.29) | 12/12 = 100% | 0 [] | 0 | 0 | None | 0 |
| openai_gpt_oss_20b__run2 | 19/20 = 95% | 13/14 | 3/3 | 3/3 | 5 (0.56) | 14/22 = 64% | 1 ['L01'] | 0 | 0 | None | 0 |
| qwen_qwen3_8_27b__run1 | 21/22 = 95% | 15/16 | 3/3 | 3/3 | 8 (0.73) | 25/25 = 100% | 2 ['L01', 'L03'] | 0 | 0 | False | 0 |

Stability (same model, two runs): {"openai/gpt-oss-20b": {"item_agreement": 0.9624060150375939, "flagged_set_jaccard": 0.6923076923076923}}
