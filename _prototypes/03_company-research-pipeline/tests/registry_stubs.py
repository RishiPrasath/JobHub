"""Exercise refresh() failure paths that cannot be triggered with real ACRA data. Run inside the image:
docker run --rm --tmpfs /data:size=3g,uid=10001 -v <abs path to tests>:/t:ro -e PYTHONPATH=/app --entrypoint python jobhub-company-research:dev /t/registry_stubs.py"""
import pathlib, sys

from pipeline import acra, registry

data = pathlib.Path("/data")
ok = True
HEADER = ("uen,entity_name,entity_type_description,entity_status_description,registration_incorporation_date,"
          "primary_ssic_description,former_entity_name1,former_entity_name2,former_entity_name3\n")


def expect(label, fn, needle):
    global ok
    try:
        fn()
        print("FAIL", label, "- no error raised")
        ok = False
    except RuntimeError as e:
        hit = needle in str(e)
        print(("PASS " if hit else "FAIL ") + label + " ->", str(e)[:110])
        ok = ok and hit


def fake_download(content):
    def dl(d, ids=None, on_progress=None):
        d = pathlib.Path(d)
        d.mkdir(parents=True, exist_ok=True)
        for i in ids:
            (d / f"{i}.csv").write_text(content)
        return len(ids)
    return dl


# 1. a new release is published while the files are downloading
calls = {"n": 0}


def moving_release():
    calls["n"] += 1
    return {"updated_at": "2026-10-14T00:00:00+08:00" if calls["n"] == 1 else "2026-11-14T00:00:00+08:00",
            "ids": ["d_a", "d_b"], "frequency": "monthly"}


registry.remote_release = moving_release
acra.download = fake_download("uen,entity_name\n1,X\n")
expect("release changes during download", lambda: registry.refresh(data), "new release while downloading")
print("     staging removed after a changed release:", not list((data / "registry").glob("staging-*")))

# 2. not enough free space
registry.MIN_FREE_GB = 1e6
registry.remote_release = lambda: {"updated_at": "2026-10-14T00:00:00+08:00", "ids": ["d_a"], "frequency": "monthly"}
expect("free-space pre-check", lambda: registry.refresh(data), "free on the data volume")
registry.MIN_FREE_GB = 0.0

# 3. a file in an unexpected format
acra.download = fake_download("uen,entity_name\n1,X\n")
expect("unexpected file format", lambda: registry.refresh(data), "may have changed the file format")

# 4. a well-formed but far too small index is refused and nothing goes live
acra.download = fake_download(HEADER + "1,X PTE LTD,Local Company,Live Company,2000-01-01,Retail,,,\n")
expect("index below the row floor", lambda: registry.refresh(data), "rows")
print("     live pointer untouched:", not (data / "registry.json").exists(),
      "| leftover .building files:", list((data / "registry").glob("*.building")))
sys.exit(0 if ok else 1)
