"""Self-test and rollback paths, using a copy of the live index as the 'good' one and a tiny index as the 'bad' one.
docker run --rm --tmpfs /work:size=3g,uid=10001 -v 03_company-research-pipeline_acra-data:/live:ro \
  -v <abs path to tests>:/t:ro -e PYTHONPATH=/app -e JOBHUB_DATA=/work --entrypoint python jobhub-company-research:dev /t/selftest_stubs.py"""
import json, pathlib, shutil, sys

from pipeline import acra, registry, selftest

live = json.loads(pathlib.Path("/live/registry.json").read_text())
work = pathlib.Path("/work")
(work / "registry").mkdir(parents=True)
shutil.copy("/live/" + live["db"], work / "registry" / "good.sqlite")

HEADER = ("uen,entity_name,entity_type_description,entity_status_description,registration_incorporation_date,"
          "primary_ssic_description,former_entity_name1,former_entity_name2,former_entity_name3\n")
csv_dir = work / "tiny"
csv_dir.mkdir()
(csv_dir / "d_x.csv").write_text(HEADER + "1,X PTE LTD,Local Company,Live Company,2000-01-01,Retail,,,\n")
acra.build_index(csv_dir, work / "registry" / "bad.sqlite")

ok = True


def check(label, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + label, detail)
    ok = ok and bool(cond)


good = selftest.run(work / "registry" / "good.sqlite", work, live["as_of"])
check("good index passes", good["ok"], "(%d checks, %.1fs)" % (len(good["checks"]), good["seconds"]))
bad = selftest.run(work / "registry" / "bad.sqlite", work, live["as_of"])
check("tiny index fails", not bad["ok"], "failed: " + ", ".join(c["name"] for c in bad["checks"] if not c["ok"] and c["level"] == "fail"))

# a stale release only warns
old = selftest.run(work / "registry" / "good.sqlite", work, "2026-01-01T00:00:00+08:00")
check("stale release warns but passes", old["ok"] and "freshness" in old["warnings"], "warnings: %s" % old["warnings"])
# a corrupted file is reported, not raised
(work / "registry" / "corrupt.sqlite").write_bytes(b"not a database" * 100)
cor = selftest.run(work / "registry" / "corrupt.sqlite", work, None)
check("corrupt file fails cleanly", not cor["ok"] and cor["checks"][0]["name"] == "index_opens", cor["checks"][0]["detail"][:60])

# rollback: pointer names the bad index, previous is the good one
prev = {"db": "registry/good.sqlite", "as_of": live["as_of"], "built_at": live["built_at"], "rows": live["rows"]}
ptr = work / "registry.json"
ptr.write_text(json.dumps({"db": "registry/bad.sqlite", "as_of": "2026-11-14T00:00:00+08:00", "built_at": "now", "rows": 1, "previous": prev}))
check("verify_after_refresh rolls back", registry.verify_after_refresh(work) == "rolled_back")
after = json.loads(ptr.read_text())
check("pointer is back on the good index", after["db"] == "registry/good.sqlite", after["db"])
check("bad release is remembered as rejected", after.get("rejected") == "2026-11-14T00:00:00+08:00", str(after.get("rejected")))
check("rollback error is reported", "rolled back" in (registry._state["last_error"] or ""), registry._state["last_error"][:70])

# the rejected release is skipped, a newer one is not
registry.remote_release = lambda: {"updated_at": "2026-11-14T00:00:00+08:00", "ids": ["d_x"], "frequency": "monthly"}
check("rejected release is skipped", registry.refresh(work) == "rejected_release")

# no previous index: report, do not pretend
ptr.write_text(json.dumps({"db": "registry/bad.sqlite", "as_of": "2026-11-14T00:00:00+08:00", "built_at": "now", "rows": 1, "previous": None}))
check("no previous index -> 'failed'", registry.verify_after_refresh(work) == "failed", registry._state["last_error"][:60])
sys.exit(0 if ok else 1)
