# X2 result (2026-11-07), n=12 (ground truth could be established for only 12 of 36 brands)
Arm A (registry /check on brand only): correct 1/12 (BreadTalk). Others: similar_name_only or multiple_entities (Shopee, Courts), Grab -> a cancelled sole proprietorship (flagged not active), Old Chang Kee -> listed parent OLD CHANG KEE LTD (200416190W, different entity from the operating subsidiary). Raw: armA.json.
Arm B (registry + web step, Haiku agents, blind to ground truth):
- Correct 9/12 (75%): Shopee, Ninja Van, Jollibee, BreadTalk, Courts, Old Chang Kee, Paris Baguette, Mr Bean, Din Tai Fung.
- Unresolved 2/12: Grab (refused to accept an unverified candidate), Deliveroo (found the entity, correctly refused it because it is in liquidation).
- Wrong accepted 1/12: Ya Kun Kaya Toast -> YA KUN CAFE PTE. LTD. (200208213K); ground truth was YA KUN INTERNATIONAL PTE LTD (200104668W, footer-tier, weaker). Both are real Live companies; which one employs staff is not established.
- Pre-registered pass (B>=70%, wrong<=1, B beats A by >=30 points): MET (75%, 1, +67 points).
Caveats: n=12 not 30; ground truth for Din Tai Fung, BreadTalk, Ya Kun is footer-tier; some Arm B acceptances rest on registry-mirror sites that also fed ground truth, so partly not independent; acceptance does not prove the entity is the employer on a given posting.
