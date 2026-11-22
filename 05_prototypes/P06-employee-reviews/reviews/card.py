"""The employee-experience card for one employer (FEAT-008, decision 0005).

Input comes from the employer identity check (FEAT-001): a UEN, the registered
name and, when known, the brand people use. The card holds:
- link-outs the user opens to read reviews themselves,
- the TAFEP Tripartite Standards entry for that UEN.
It never holds review text or ratings from any site.
"""
from .linkouts import build_linkouts
from .names import normalise_uen, search_name
from .tafep import TafepList

HEADLINE = "What employees say: read it at the source"
NOTE = ("JobHub does not copy or summarise reviews from these sites, because their terms bar it. "
        "Reviews are individual accounts and may be old, one-sided or about a different team or office.")


def build_card(uen: str, legal_name: str, tafep: TafepList | None, brand: str | None = None,
               overrides: dict[str, str] | None = None) -> dict:
    name = search_name(legal_name, brand)
    card = {
        "feature": "FEAT-008",
        "uen": normalise_uen(uen),
        "legal_name": legal_name,
        "search_name": name,
        "headline": HEADLINE,
        "linkouts": build_linkouts(name, overrides),
        "note": NOTE,
    }
    if tafep is not None:
        card["tripartite_standards"] = tafep.lookup(uen)
        age = tafep.age_days()
        if age is not None and age > 7:
            card["tripartite_standards"]["stale_notice"] = (
                f"TAFEP list copy is {age:.0f} days old; refresh with `python cli.py fetch-tafep`.")
    else:
        card["tripartite_standards"] = None
    return card


def render_text(card: dict) -> str:
    out = [f"{card['headline']}  ({card['legal_name']}, UEN {card['uen']})", ""]
    for l in card["linkouts"]:
        flag = "" if l["url_status"] != "unverified" else "  [link pattern not yet click-checked]"
        out.append(f"- {l['label']}: {l['url']}{flag}")
        out.append(f"    {l['what']}")
    out += ["", card["note"], ""]
    ts = card.get("tripartite_standards")
    if ts:
        out.append("Tripartite Standards (TAFEP): " + ts["text"])
        out.append("  " + ts["caveat"])
        out.append("  Source: " + ts["source_url"])
        if ts.get("stale_notice"):
            out.append("  " + ts["stale_notice"])
    return "\n".join(out)
