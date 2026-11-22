# Note, 2026-11-11

A completion launch on 2026-11-11 used `python -I`, which hides the user-site `openai` package. Every call failed with "No module named 'openai'" before any request was sent, and the harness wrote 86 failure files into `raw/_failures/`. One of them overwrote the original record `free_P2_S11_run1.txt` (the real API error `json_validate_failed` from 2026-11-10, which is quoted in FINDINGS).

None of the 86 files holds a real model failure. A deletion was attempted and refused by a safety check, so they remain and are listed here for a person to remove if wanted. The scorer treats a failure file as a failed free-text cell only when no result exists for that cell, so cells filled by the relaunch are unaffected; any cell still lacking a result at scoring time is checked by hand and stated in FINDINGS. No model output was touched.
