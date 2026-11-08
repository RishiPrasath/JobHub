"""Self-test for a registry index: does it still behave like the real ACRA registry?

Checks are either 'fail' (the index should not be served) or 'warn' (worth knowing, still usable).
Canaries are large, long-lived companies whose registry IDs were read from the live index on 2026-11-03.
A canary can legitimately change (a rename, a merger), so the name check passes at CANARY_PASS_RATIO, and the
failing names are listed so a person can retire a canary instead of chasing a phantom outage."""
import shutil, sqlite3, statistics, time
from datetime import datetime, timezone
from pathlib import Path

from . import acra

CANARIES = [
    ("DBS BANK LTD", "196800306E"),
    ("Singapore Airlines Limited", "197200078R"),
    ("Singapore Telecommunications Limited", "199201624D"),
    ("Randstad Pte. Limited", "199304055W"),
    ("Singapore General Hospital Pte Ltd", "198703907Z"),
    ("Tan Tock Seng Hospital Pte Ltd", "199003683N"),
    ("Koufu Pte Ltd", "199602661M"),
    ("National University Health System Pte. Ltd.", "200801778C"),
    ("Kyndryl (Singapore) Pte. Ltd.", "202101462E"),
    ("Natureland Care Pte. Ltd.", "201219975K"),
    ("Oversea-Chinese Banking Corporation Limited", "193200032W"),
    ("Sembcorp Industries Ltd", "199802418D"),
]
CANARY_PASS_RATIO = 0.8
MEDIAN_LOOKUP_MS = 250


def _c(name, ok, detail, level="fail"):
    return {"name": name, "ok": bool(ok), "level": level, "detail": detail}


def run(db, data_dir=None, as_of=None, min_rows=1_000_000, max_age_days=45, min_free_gb=1.5):
    """Run every check against one index file. Returns {'ok', 'ran_at', 'seconds', 'checks'}."""
    t0 = time.time()
    checks = []
    db = Path(db)

    # 1. the file opens and its tables agree
    try:
        con = sqlite3.connect("file:%s?mode=ro" % db.as_posix(), uri=True)
        n = con.execute("select count(*) from ent").fetchone()[0]
        f = con.execute("select count(*) from fts").fetchone()[0]
        live = con.execute("select count(*) from ent where status like 'Live%'").fetchone()[0]
        con.close()
        checks.append(_c("index_counts", n >= min_rows and n == f, "%d entities, %d in the search table, %d live" % (n, f, live)))
        checks.append(_c("live_share", 0.05 < live / max(n, 1) < 0.6, "%.0f%% of entities are live (expected roughly 15 to 40%%)" % (100 * live / max(n, 1))))
    except Exception as e:
        return {"ok": False, "ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "seconds": round(time.time() - t0, 2),
                "checks": [_c("index_opens", False, "%s: %s" % (type(e).__name__, str(e)[:120]))]}

    # 2. canaries by name and by registry ID
    bad_name, bad_uen, times = [], [], []
    for name, uen in CANARIES:
        t = time.time()
        r = acra.resolve(db, name)
        times.append((time.time() - t) * 1000)
        if not (r["state"] in ("exact", "likely") and (r["chosen"] or {}).get("uen") == uen):
            bad_name.append("%s -> %s %s" % (name, r["state"], (r["chosen"] or {}).get("name")))
        r2 = acra.resolve(db, "", uen=uen)
        if r2["state"] != "exact_by_uen":
            bad_uen.append(uen)
    ok_names = len(CANARIES) - len(bad_name)
    checks.append(_c("canary_names", ok_names / len(CANARIES) >= CANARY_PASS_RATIO,
                     "%d of %d resolved to the expected ID%s" % (ok_names, len(CANARIES), "; failed: " + "; ".join(bad_name) if bad_name else "")))
    checks.append(_c("canary_uens", not bad_uen, "all %d IDs found" % len(CANARIES) if not bad_uen else "not found: " + ", ".join(bad_uen)))

    # 3. behaviours that must hold
    nonsense = acra.resolve(db, "Zzqxv Qwlmt Holdings")
    checks.append(_c("nonsense_is_unresolved", nonsense["state"] == "unresolved", "state = %s" % nonsense["state"]))
    pb = acra.resolve(db, "Central Provident Fund Board")
    checks.append(_c("public_body_detected", pb["state"] == "public_body", "state = %s" % pb["state"]))

    # 4. speed
    med = statistics.median(times)
    checks.append(_c("lookup_speed", med < MEDIAN_LOOKUP_MS, "median %.0f ms over %d lookups (limit %d ms)" % (med, len(times), MEDIAN_LOOKUP_MS)))

    # 5. warnings: age and disk
    if as_of:
        age = (datetime.now(timezone.utc) - datetime.fromisoformat(as_of)).days
        checks.append(_c("freshness", age <= max_age_days, "registry release is %d days old (warn after %d)" % (age, max_age_days), "warn"))
    else:
        checks.append(_c("freshness", False, "release date unknown (index recovered or built by the older flow)", "warn"))
    if data_dir:
        free = shutil.disk_usage(data_dir).free / 1e9
        checks.append(_c("disk_space", free >= min_free_gb, "%.1f GB free (a refresh needs %.1f)" % (free, min_free_gb), "warn"))

    return {"ok": all(c["ok"] for c in checks if c["level"] == "fail"),
            "warnings": [c["name"] for c in checks if not c["ok"] and c["level"] == "warn"],
            "ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "seconds": round(time.time() - t0, 2), "checks": checks}
