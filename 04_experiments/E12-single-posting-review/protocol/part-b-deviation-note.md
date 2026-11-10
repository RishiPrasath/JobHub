# Part B deviation note (written 2026-11-10 before any Part B persona call; protocol/part-b-simulated-pilot.md stays as frozen)

Cause: the org-wide daily token limit (TPD, 200,000 per model, shared by all specialists) was reached for openai/gpt-oss-120b and openai/gpt-oss-20b during this run; the shared per-minute queue for qwen/qwen3.8-27b also allows about one call every 3 to 7 minutes for this experiment. The 6 personas had already been created with gpt-oss-20b.

Changes to the frozen Part B design (made before any persona answered, not in response to any persona result):
1. Persona answers come from qwen/qwen3.8-27b, not gpt-oss-20b.
2. Each persona reviews ONE posting (rotated: persona i gets posting i mod 3), not three. 6 personas x 2 steps = 12 calls. Each posting is seen by 2 personas, so 6 persona-posting pairs, not 18.
3. Posting E12-P08 (part-time retail, which has a real pay contradiction) replaces E12-P10 because no model output exists for E12-P10 to build a worksheet from. Planted wrong item for E12-P08: the unsupported claim "The employer makes CPF contributions on the hourly pay." (the posting says nothing about CPF).
4. Worksheets for E12-P04, E12-P07 and E12-P08 are built from the gpt-oss-120b run-1 output of Part A.
Everything else (RAW step then WORKSHEET step, one unflagged planted item, measures, labels) is as frozen.
