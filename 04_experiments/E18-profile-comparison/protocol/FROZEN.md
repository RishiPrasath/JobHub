# E18 Part A: frozen inputs

Frozen at 2026-11-10T10:00:23Z (UTC), before the first model call on the sample. Never edited after this.

Gold labels (data/gold.json) were written by hand (by the specialist, an AI) from the posting texts and profile fields, before any system under test ran. Thresholds are copied verbatim from README.md. They are not committed to git (the owner has not asked for commits); see FINDINGS.md Deviations.

| file | sha256 |
|---|---|
| protocol/thresholds.md | 9ffc7e028e6b6163cd2d69a878d7a57a3a34ec5b5b87ed29edf4fbe91e23116e |
| protocol/scoring.md | dc790e5763eb629d1df41226e04a7ba96346c4d1524709791d35e65d5be40cc5 |
| protocol/sample-design.md | 1c74223c247d97994f55520c259a5a0b36ee7e7a14670ae993804db70326df79 |
| data/gold.json | 630cd6d754a9b8908dad5e0a11855c55db9f603a743b88fa7543b56127efe161 |
| data/postings.json | 1c7dede8d7acd9341e90a36f0a5795bdd1c86ce928af77d2e16e008839f3287e |
| data/profiles.json | ed2c593ff1aa94ba791dc28c18e052fac6b6e2473e8873e4520f420b04203459 |
| harness/author_data.py | d229c9eae59ce41bd53c41f4d121cad121d7e10ec0d0b5aec1e0afccd8b51800 |
| harness/common.py | c37aaed005d74d28c3d85231e629f78cdd4af753d7d3eacc777f76475fffca58 |
| harness/run_methods.py | 57f0e986e07aa491c9fd8454bb9f9d18fbc5a452be4c3eb8c085e209fd06f59e |

harness/score.py is written after the runs were launched but before any output was read; it implements protocol/scoring.md and is hashed in FINDINGS.md.

## Pre-run harness edit (recorded 2026-11-10T10:06:11Z UTC)

No model call on the sample had completed. Because the shared rate limiter reserves tokens by max_tokens and many specialists were queueing, the max_tokens values in harness/common.py were lowered (free-text single 1900 to 1500, batch 4800 to 3600; extraction single 1500 to 1100, batch 4200 to 3000; evidence proposals 2500 to 1600). Nothing else changed. A dev smoke test on one invented posting (D00, not in the sample, outputs under outputs/dev) was run once per model before this edit to check that the JSON parses. New sha256 of harness/common.py: 856173315c43772a63e9f7a7355d092b985bc7d5c52775527c268d7fd1891da8.
Gold labels, thresholds, scoring definitions, postings and profiles are unchanged (hashes above still hold).

## Second pre-result harness edit (recorded 2026-11-10T10:10:21Z UTC)

The extraction process crashed once on a Windows PermissionError raised by the shared rate-limit lock file in tools/llm_client.py (not edited; reported as a bug). harness/common.py `llm()` now retries on PermissionError, FileNotFoundError and TimeoutError, and harness/supervise.sh reruns a stage until it completes (calls are cached, so reruns only do missing calls). No prompt, schema, code-comparison or scoring change. A few sample calls had already completed; none had been read or scored. New sha256 of harness/common.py: f4ffc9cb6079ec024ad365be3b001b8a503a6fe00aa799b2b3c4e77fa4bb423a.
