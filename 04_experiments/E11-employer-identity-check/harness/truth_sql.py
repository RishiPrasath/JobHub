"""Plain-SQL lookup on the raw ACRA table (read-only) for ground truth: no matching logic of the system under test.
Runs inside the P03 registry container via docker exec. Usage: python harness/truth_sql.py "DBS BANK%" "UEN:196800306E" ...
LIKE patterns use % wildcards against the entity name (case-insensitive)."""
import subprocess, sys
CODE = r'''
import sqlite3, sys, glob
db = sorted(glob.glob("/data/registry/acra-*.sqlite"))[-1]
c = sqlite3.connect("file:%s?mode=ro" % db, uri=True)
for p in sys.argv[1:]:
    print("##", p)
    if p.startswith("UEN:"):
        rows = c.execute("select uen,name,type,status,inc from ent where uen=?", (p[4:],)).fetchall()
    else:
        rows = c.execute("select uen,name,type,status,inc from ent where name like ? limit 15", (p,)).fetchall()
    for r in rows:
        print("  ", " | ".join(str(x) for x in r))
'''
if __name__ == "__main__":
    r = subprocess.run(["docker", "exec", "-i", "03_company-research-pipeline-registry-1", "python", "-"] + sys.argv[1:], input=CODE, text=True, capture_output=True, encoding="utf-8")
    print(r.stdout, r.stderr[-1500:])
