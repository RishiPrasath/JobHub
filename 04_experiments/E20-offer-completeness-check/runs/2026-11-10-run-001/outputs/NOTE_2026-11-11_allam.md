# 2026-11-11 completion attempt (note, not a result file)

- qwen3.8-27b run 1: letter L02 was run (it hit the daily limit on L04). Earlier results were kept; the new letter was merged into `parsed/qwen_qwen3_8_27b__run1.json` (previous file copy in `pre_2026-11-11/`).
- gpt-oss-20b run 1: the daily limit stopped it after L01. The `parsed/` run-1 file was twice overwritten by a partial run and restored from the copy in `pre_2026-11-11/`; its content is the 2026-11-10 content.
- allam-2-7b (a 7B model, added as a floor check): the API returned "Failed to generate JSON" on every attempt for L01 to L07 (three attempts on L01, one or more on the others). The run was stopped by hand after L07 to avoid wasting tokens. No parsed output exists. Log: `log_allam_r1_2026-11-11.txt`.
