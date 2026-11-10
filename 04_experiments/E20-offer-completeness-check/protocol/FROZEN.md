# FROZEN

Frozen at 2026-11-10T10:01:57Z (UTC), before any model call of this experiment had completed. Nothing below is changed after this time. A change to any of these files is a new run folder labelled post hoc.

Re-freeze note: a first freeze was made at 2026-11-10T09:58:15Z. The first launch of run_check.py then waited more than 8 minutes at the shared rate limiter without completing a single call (no raw output existed and no result had been seen), because the first prompt was too large to fit the shared 8,000 tokens-per-minute window while other specialists were running. The processes were stopped, the prompt was shortened (source URLs removed from the prompt, rules condensed; the checklist items and their guidance sentences are unchanged), and everything was frozen again here. Thresholds, checklist, letters and gold labels are byte-identical to the first freeze (the hashes of those files are unchanged). Only prompt.py differs.

Nothing in this experiment is committed to git, because the owner has not asked for commits. The order (labels before results) is shown only by this file and the file timestamps. See Deviations in FINDINGS.md.

| file | sha256 |
|---|---|
| protocol/thresholds.md | d89d897cb444de429a1495ab6efd7a48f09ccbc782faf3c0974df107f9b6408d |
| protocol/checklist.json | b8e5fff2c06a3faaea36ed566c55c93d31887cd20bcd5f746950a16b02a7d033 |
| protocol/checklist.md | 64adb1f4ce2f46356a14863f79ebe8fe095094884a3ac76ca1a05860cb53d92b |
| data/gold/gold.json | c0aa39b6f45f9d3b5ca0d65518025abce796022365fd6378066062b3b12e26e1 |
| data/letters.json | f520bcb546c8a143dc9018468e1904b74ecdf106505ef7e681a42b84ccb7b7eb |
| harness/prompt.py | 134a6c388c8e32fc2fb3f9c43aac6737d3521c2f552bef6eaffe774e08b3ee70 |
| harness/score.py | a2af1242f030c864fb9a0d46d800ea7db7fa0965d427f356780b5dc4cc684b9f |
| harness/build_letters.py | ab04ddadc0077e037bbb954320837d2164ebb39ae6b7a26414a4c4b7c3d347e5 |
| harness/run_check.py | 566d99527cc45e5078c1e08cd1a90ad734a0810dc23e4e02d261b36c555be540 |
| harness/render_report.py | 91c6aaefe07f3841da6dccb032c6f1e7634912d3201640c42176ce6e01aebdee |
| harness/persona_pilot.py | 769e8388144bf89727e8a11c6ba02c3d2e2d4527e4a8c7c9628f4b366dc8119d |
| data/letters\L01.txt | b114eda542f5ffa43ee3f899614b9f5910e75424b28cda02894c5e8b1f978ef5 |
| data/letters\L02.txt | 3452a41a791fad4e5fc58204d397ccd0e68a62b73cb8929308844e9e97025cd3 |
| data/letters\L03.txt | cda924b83b550dadf9b353191988847d6470ca2b7e8b9b22435241ad0b589927 |
| data/letters\L04.txt | 24cf0bfd6fd1723706e1b38ebf1972c4833391ff53e473a7e51c40733759ef12 |
| data/letters\L05.txt | b2308a51572cd379e28ee343c36bf7f6eecd6d8e67e2d62025897505d211d0c9 |
| data/letters\L06.txt | b7b3097dc3ebea0fb0a3eacf572f6925ace515fb774406921231c9a49d0ecca5 |
| data/letters\L07.txt | 467b88c058b283a65879711b63fa378ce76d0547877dcf557d95720928abdd31 |
| data/letters\L08.txt | cdbac934b74b88295afe6921371996319af1aeff8b9c7e08ac059175fffac335 |
| data/letters\L09.txt | c1de9d60438b77ebcd817766c29903c6076d7736cb2207c3c25f51693d3a2d11 |
| data/letters\L10.txt | dcccee1deb6e0ca03cbd57c7e34f2adb03e0ddeaaa778fd779fe3e53aa228956 |
| data/letters\L11.txt | 2a1a24a39ca988b862c54250b3e225b66f328250593fe6690807b380b49cb044 |
| data/letters\L12.txt | fcf64820b2a586a1a1a7e2e3d34d8ec8d63ae08667029358737bae25a475f134 |
| data/letters\L13.txt | 70b46c00d84a610da353cd8ec8a89f990abcf7dd6f82eb27bb46af0224ef54dd |
| data/letters\L14.txt | d4df9fe4ed2cfc1e8d98d422092686c3d888b5221132b31d91e3aca165974323 |
| data/letters\L15.txt | c8a6ec2b32151885ab8c4a3f111cb0eaea4298301f31aa324de55ea996412d8f |
| data/letters\L16.txt | 1ccdc31ace4e6ebc26ff36693cc224dd774e26299dded85c0920707cf112538c |
| data/letters\L17.txt | 0b7830ab5d1e9cdaf8570e8233aefd6821da043ec60179b0ae3cfdf62175e2b9 |
| data/letters\L18.txt | db63fa476ab3789bd1c60d5f82bbc99b9db3fa6848cab9f9e630ea76190296fe |
| data/letters\L19.txt | 4d6a9945eb080fb27d3b45addf15dfdd4a0efc0c601f9a677e91e9f95c448362 |
| data/letters\L20.txt | 2a6b556ee94c5842636b072b4e3c0b7346289244d3a9060127f69071f7ad15ba |

Frozen design decisions
- Models: openai/gpt-oss-20b (runs 1 and 2), qwen/qwen3.8-27b (run 1). reasoning_effort=low for gpt-oss; temperature 0.2; json_mode on. max_tokens 1500 (gpt-oss-20b) and 2000 (qwen).
- Simulated pilot: 6 personas via tools/persona_creator.py (creator openai/gpt-oss-120b, answering agents openai/gpt-oss-20b); every persona sees the check report of letter L17 from gpt-oss-20b run 1 (chosen now, before any output exists).
- The 4 template-styled synthetic letters (L17 to L20) replace the 4 consented real letters of the README. L20 holds the hidden instruction.
- Source ids in the output are resolved to the named source and URL by harness/render_report.py; the model is not asked to write URLs.
