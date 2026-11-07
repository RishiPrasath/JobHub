"""Plain-text view of a research result, for the command line and for pasting into a review."""
import textwrap


def _w(s, indent="  ", cont=None):
    return textwrap.fill(s, 100, initial_indent=indent, subsequent_indent=cont if cont is not None else " " * len(indent))


def render_text(r):
    L = ["%s" % r["employer"] + ("  (role: %s)" % r["role"] if r["role"] else ""),
         "HEADLINE: %s" % r["headline"], _w(r["headline_meaning"]), _w("because: " + "; ".join(r["reasons"]))]
    reg = r["registry"]
    L.append("REGISTRY: " + ("unavailable" if not reg["available"] else "%s. %s" % (reg.get("verdict"), reg.get("summary") or "")))
    if reg.get("flags"):
        L += [_w("flag: " + f) for f in reg["flags"]]
    w = r["web"]
    if w["skipped_reason"]:
        L.append("WEB: skipped, " + w["skipped_reason"])
    else:
        ok = sum(1 for p in w["pages"] if p["status"] == "ok")
        g = w["gate"]
        L.append("WEB: %d queries (%s), %d of %d pages read, exact name seen in %d pages and %d search results" % (
            len(w["queries"]), ", ".join(w["engines_used"]) or "no engine answered", ok, len(w["pages"]), g["pages_with_exact_name"], g["snippets_with_exact_name"]))
    b = r.get("brief")
    if b:
        L.append("BRIEF (model rating: %s, confidence %s; %d claims verified, %d unverified)" % (b["model_validity_status"], b["confidence"], b["claims_verified"], b["claims_unverified"]))
        if b.get("suppressed"):
            L.append(_w(b["suppressed"]))
        if b.get("about"):
            L.append(_w("about: " + b["about"]))
        for title, key in (("Facts", "key_facts"), ("Positive signals", "positive_signals"), ("Red flags", "red_flags")):
            if b[key]:
                L.append("  " + title + ":")
                L += [_w("[%s] %s" % ("verified" if c["status"] == "verified" else "UNVERIFIED", c["claim"]), "    ") for c in b[key]]
    if r.get("link_out"):
        L.append("OPEN THESE YOURSELF (review and job sites we do not read automatically, %d):" % len(r["link_out"]))
        L += [_w("%s  %s" % ((x.get("title") or "")[:50], x["url"][:80]), "  - ") for x in r["link_out"][:6]]
    if r["could_not_read"]:
        L.append("COULD NOT READ (%d):" % len(r["could_not_read"]))
        L += [_w("%s  (%s)" % (x["url"][:70], x["why"][:80]), "  - ") for x in r["could_not_read"][:8]]
    if r["could_not_verify"]:
        L.append("COULD NOT VERIFY:")
        L += [_w(x, "  - ") for x in r["could_not_verify"]]
    if r["degraded"]:
        L.append("DEGRADED: " + " | ".join(r["degraded"]))
    if r["partial"]:
        L.append("PARTIAL: the time budget ran out before every step finished")
    L += ["(%ss) %s" % (r["seconds"], r["disclaimer"])]
    return "\n".join(L)
