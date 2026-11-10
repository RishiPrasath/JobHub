# FROZEN

Frozen at 2026-11-10T09:57:56Z (UTC), before any Part B arm or Part C persona call ran. Not committed to git (owner has not asked for commits).

sha256 of frozen files:
```
c331ea69915fd976c2b50880ead891b2d2c62fc0b3a551c746d4dfe24bc5e15f *protocol/thresholds.md
3ec40ba1ff7f9b65f5cf3d3a6c12875f5c0ce2431023db59f4795d458de291d8 *protocol/partB-protocol.md
b028f4e2880fa3cc4d36255e3780bd42a8d588e1e44535d789d14af52a6362c5 *data/partB_groundtruth.json
719c7e38a201bccae48ba1eaed2804405dbcca7faa7756e96b211ec11ebd3ab5 *data/mom_ea_directory_flagged_2026-11-10.json
9f5daacfb2f60fabcb8cbfc583cc9c0fd9b9accb78dba0929cf70776f3dc1dc9 *harness/list_check.py
e8f758cf01c51de50113725aa2195f49812ddf462fdd33320386be5d8d3c6c37  (MOM stop-work-order lines extract, stored outside the repo)
0fbad951372e0a723c709b697937209fbac274c75fcb0d88fc8477a573fb3af9  (MOM stop-work-order PDF, stored outside the repo)
```

Part A (source access) outputs were written before freeze because Part B ground truth depends on them; Part A has no model-run thresholds beyond thresholds.md.
Part C stimuli and coding rubric are frozen separately in protocol/FROZEN-partC.md before the persona calls.
