"""Posting-level existence check: expected verdicts for real, lookalike, mismatched and inactive employers.
Run inside the image with the registry volume mounted read-only:
docker run --rm -v 03_company-research-pipeline_acra-data:/data:ro -v <abs path to tests>:/t:ro -e PYTHONPATH=/app \
  --entrypoint python jobhub-company-research:dev /t/check_cases.py"""
import json, sqlite3, sys
from pathlib import Path

from pipeline import acra, check, registry

DB = registry.db_path("/data")
con = sqlite3.connect("file:%s?mode=ro" % Path(DB).as_posix(), uri=True)
ok = True
rows = []


def case(label, expected, employer, **kw):
    global ok
    r = check.check(DB, employer, **kw)
    good = r["verdict"] in (expected if isinstance(expected, tuple) else (expected,))
    ok = ok and good
    rows.append((good, label, r["verdict"], employer, (r["entity"] or r["closest"] or {}).get("name", "-")))
    return r


# --- real employers written the way postings write them
case("exact registered name", "confirmed", "RANDSTAD PTE. LIMITED")
case("punctuation and case differ", "confirmed", "randstad pte limited")
case("legal suffix left off", "confirmed", "Singapore Airlines")
case("'&' vs 'and' style punctuation", "confirmed", "Oversea Chinese Banking Corporation Limited")
case("sibling entities exist, posting names the real one", "confirmed", "Recruit Express Pte Ltd")

# --- lookalikes: must never come back as confirmed
case("extra word makes a lookalike of a bank", ("similar_name_only", "multiple_entities"), "DBS Bank Singapore Recruitment Pte Ltd")
case("lookalike of an airline", ("similar_name_only", "not_in_registry"), "Singapore Airlines Careers Hub Pte Ltd")
case("one-letter typo of a real employer", ("similar_name_only", "probable", "not_in_registry"), "Randstat Pte Ltd")
case("made-up name", "not_in_registry", "Zzqxv Qwlmt Holdings Pte Ltd")

# --- company ID in the posting
case("ID agrees with name", "confirmed", "Singapore Telecommunications Limited", uen="199201624D")
case("ID taken from a URL slug", "confirmed", "Singapore Telecommunications Limited", url="https://www.mycareersfuture.gov.sg/company/singapore-telecommunications-199201624D")
r = case("ID belongs to a different company", "uen_name_mismatch", "Randstad Pte Limited", uen="199201624D")
case("ID does not exist", "uen_not_found", "Randstad Pte Limited", uen="199999999Z")
case("brand name with the right ID", ("uen_name_mismatch", "probable", "confirmed"), "Singtel", uen="199201624D")

# --- inactive and duplicate entities, found in the registry itself
dead = con.execute("""select name,uen,status from ent e where status like 'Struck Off%' and type='Local Company'
                      and not exists (select 1 from ent o where o.name=e.name and o.uen<>e.uen) limit 1""").fetchone()
case("only a struck-off entity has this name", "registered_not_active", dead[0])
dup = con.execute("""select name from ent where status like 'Live%' group by name having count(*)>1 limit 1""").fetchone()
if dup:
    case("two live entities share the exact name", "multiple_entities", dup[0])
former = con.execute("""select f1,name from ent e where status like 'Live%' and f1<>'' and length(f1)>12
                        and not exists (select 1 from ent o where o.name=e.f1) limit 1""").fetchone()
case("posting uses a former name", ("former_name", "similar_name_only"), former[0])

# --- not companies
case("statutory board", "public_body", "Central Provident Fund Board")
case("government agency", "public_body", "Land Transport Authority")

for good, label, verdict, employer, ent in rows:
    print(("PASS " if good else "FAIL ") + label.ljust(56), verdict.ljust(22), employer[:36].ljust(36), "->", ent[:36])
print()
print("example summaries:")
for e, kw in (("DBS Bank Singapore Recruitment Pte Ltd", {}), ("Randstad Pte Limited", {"uen": "199201624D"}), (dead[0], {})):
    print("  -", check.check(DB, e, **kw)["summary"])
sys.exit(0 if ok else 1)
