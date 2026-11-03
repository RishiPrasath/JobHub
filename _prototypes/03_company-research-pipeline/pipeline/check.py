"""Posting-level existence check: does the employer named in a job posting exist in the Singapore company
registry, and is the registry entity the same company the posting names?

This answers existence and identity only. It is not a verdict on the employer: a registered company can still be
a bad employer, and a name that is not registered can still be a real business with a different legal name.

Verdicts (most to least certain):
  confirmed             exact name match (or ID + name agree), the entity is live, no other entity has the same name
  probable              the name is very close but not identical (spelling, punctuation, abbreviation)
  multiple_entities     two or more live entities share this name; the posting needs a company ID or an address
  similar_name_only     no entity has this name; the closest registered name is shown (lookalike risk)
  former_name           the posting uses a name the entity no longer has
  registered_not_active the entity exists but is struck off, in liquidation, ceased, suspended and so on
  uen_name_mismatch     the company ID in the posting belongs to a differently named entity (a trading name, or impersonation)
  uen_not_found         the company ID in the posting is not in the registry
  public_body           a statutory board or ministry; not in the company registry
  not_in_registry       nothing in the registry resembles the name
"""
import re
import sqlite3
from difflib import SequenceMatcher
from pathlib import Path

from . import acra

UEN_RE = re.compile(r"(?<![A-Za-z0-9])(?:\d{8}[A-Za-z]|(?:19|20)\d{7}[A-Za-z]|[TSRtsr]\d{2}[A-Za-z]{2}\d{4}[A-Za-z])(?![A-Za-z0-9])")
NOTE = "This shows whether the company exists and matches the name in the posting. It is not a judgement of the employer."


def uens_in(*texts):
    """Registry IDs found in any of the given strings (page text, a company-page URL slug, a form field)."""
    found = []
    for t in texts:
        for m in UEN_RE.findall(t or ""):
            if m.upper() not in found:
                found.append(m.upper())
    return found


def _is_live(status):
    return (status or "").lower().startswith("live")


def _names_of(db, uen):
    con = sqlite3.connect("file:%s?mode=ro" % Path(db).as_posix(), uri=True)
    try:
        r = con.execute("select uen,name,f1,f2,f3,type,status,inc,ssic from ent where uen=?", (uen,)).fetchone()
    finally:
        con.close()
    return r


def _name_match(posting_name, row):
    """'identical' (same words ignoring Pte/Ltd and punctuation), 'close', or 'different', against the current
    name first, then former names. Returns (level, which_name)."""
    q = acra.toks(posting_name)
    best = ("different", None, 0.0)
    for label, n in (("current", row[1]), ("former", row[2]), ("former", row[3]), ("former", row[4])):
        if not n:
            continue
        t = acra.toks(n)
        if sorted(t) == sorted(q):
            return ("identical", label, 1.0)
        s = SequenceMatcher(None, " ".join(q), " ".join(t)).ratio()
        if s > best[2]:
            best = ("close" if s >= 0.85 else "different", label, s)
    return best


def _entity(row):
    return {"uen": row[0], "name": row[1], "type": row[5], "status": row[6], "incorporated": row[7], "activity": row[8]}


def check(db, employer, uen=None, hint=None, url=None, text=None):
    """Check one posting's employer. `uen`, `url` and `text` are optional extra evidence; any registry ID found in
    them is used as a cross-check on the name."""
    ids = uens_in(uen, url, text)
    evidence = []
    out = {"employer_in_posting": employer, "uen_used": None, "basis": "name only", "entity": None, "closest": None,
           "status_ok": None, "flags": [], "evidence": evidence, "note": NOTE}

    if ids:
        for cand in ids:
            row = _names_of(db, cand)
            if not row:
                continue
            level, which, score = _name_match(employer, row)
            out["uen_used"] = cand
            out["basis"] = "company ID and name"
            out["entity"] = _entity(row)
            out["status_ok"] = _is_live(row[6])
            evidence.append("company ID %s is registered to %s" % (cand, row[1]))
            if level == "different":
                out["verdict"] = "uen_name_mismatch"
                out["summary"] = ("The company ID %s in the posting belongs to %s, which is not the name used in the posting (%s). "
                                  "This also happens when a posting uses a trading or brand name; otherwise it is a reason to be careful." % (cand, row[1], employer))
                return out
            evidence.append("posting name and registered name are %s" % ("identical" if level == "identical" else "close but not identical"))
            if which == "former":
                out["flags"].append("posting uses a former name of this entity")
            return _finish_matched(out, row, level == "identical")
        out["verdict"] = "uen_not_found"
        out["uen_used"] = ids[0]
        out["summary"] = "The company ID %s in the posting is not in the registry." % ids[0]
        return out

    exact_rows = acra.exact_name_rows(db, employer, hint)
    live_rows = [r for r in exact_rows if _is_live(r[6])]
    dead_rows = [r for r in exact_rows if not _is_live(r[6])]
    if len(live_rows) > 1:
        out["closest"] = _entity(live_rows[0])
        out["closest"]["alternatives"] = ["%s (%s)" % (r[1], r[0]) for r in live_rows[1:4]]
        out["verdict"] = "multiple_entities"
        out["summary"] = "%d live entities are registered with this exact name (%s). A company ID or an address is needed to say which one the posting means." % (
            len(live_rows), ", ".join(r[0] for r in live_rows[:4]))
        return out
    if dead_rows and not live_rows:
        row = sorted(dead_rows, key=lambda r: r[7] or "", reverse=True)[0]
        out["entity"] = _entity(row)
        out["status_ok"] = False
        if len(dead_rows) > 1:
            out["flags"].append("%d inactive entities have this name; the most recently registered is shown" % len(dead_rows))
        evidence.append("an entity named exactly this exists but is not live")
        return _finish_matched(out, row, True)
    if len(live_rows) == 1 and dead_rows:
        out["flags"].append("an earlier entity with the same name is now %s" % dead_rows[0][6])
    res = acra.resolve(db, employer, hint=hint)
    state, ch, why = res["state"], res["chosen"], res["why"]
    cands = [c["name"] for c in res.get("candidates", [])[:3]]
    if state == "public_body":
        out["verdict"] = "public_body"
        out["summary"] = "%s looks like a statutory board or government body. These are not in the company registry, so existence has to be checked on the agency's own .gov.sg site." % employer
        return out
    if state == "unresolved" or not ch:
        out["verdict"] = "not_in_registry"
        out["summary"] = "No registered entity in Singapore resembles '%s'." % employer
        return out

    row = _names_of(db, ch["uen"])
    out["entity"] = _entity(row)
    out["status_ok"] = _is_live(row[6])
    if state in ("exact", "likely"):
        evidence.append("registered name: %s" % row[1])
        if res.get("siblings"):
            out["flags"].append("other entities start with this name: " + ", ".join(res["siblings"][:3]))
        if state == "likely":
            out["flags"].append("the name in the posting is not identical to the registered name")
        return _finish_matched(out, row, state == "exact")
    out["entity"], out["status_ok"] = None, None
    out["closest"] = _entity(row)
    out["closest"]["alternatives"] = cands[1:]
    if "share the name stem" in why or "other live" in why:
        out["verdict"] = "multiple_entities"
        out["summary"] = "More than one live entity matches '%s' (%s). A company ID or an address is needed to say which one the posting means." % (employer, ", ".join(cands[:3]))
    elif "former or alternate" in why:
        out["verdict"] = "former_name"
        out["summary"] = "'%s' is a former name. The entity is now registered as %s." % (employer, row[1])
    else:
        out["verdict"] = "similar_name_only"
        out["summary"] = "No registered entity is named '%s'. The closest registered name is %s, which may be a different company." % (employer, row[1])
    evidence.append(why)
    return out


def _finish_matched(out, row, identical):
    live = _is_live(row[6])
    if "(" in (row[6] or "") and live:
        out["flags"].append("status carries a qualifier: " + row[6])
    if not live:
        out["verdict"] = "registered_not_active"
        out["summary"] = "%s exists in the registry but its status is '%s'." % (row[1], row[6])
    elif identical:
        out["verdict"] = "confirmed"
        out["summary"] = "%s is registered in Singapore (status: %s, registered %s)." % (row[1], row[6], row[7])
    else:
        out["verdict"] = "probable"
        out["summary"] = "The posting's name is very close to %s (status: %s) but not identical." % (row[1], row[6])
    return out
