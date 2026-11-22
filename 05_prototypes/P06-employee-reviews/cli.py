"""P06 employee reviews (FEAT-008). Standard library only, Python 3.10+.

  python cli.py fetch-tafep                       # one download of the TAFEP list into data/cache/
  python cli.py card --uen 196800306E --name "DBS BANK LTD." --brand DBS [--json]
  python cli.py check-page out.html --uen ... --name ... [--brand ...]   # links for a person to click-check
  python cli.py nodeflair-probe grab dbs-bank     # research only; output is never shown in the product
"""
import argparse
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reviews import nodeflair, tafep  # noqa: E402
from reviews.card import build_card, render_text  # noqa: E402

CACHE = os.path.join(tafep.DEFAULT_CACHE, "tafep_ts_listing.json")
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "fixtures", "tafep_sample.json")


def _load_tafep(path: str | None):
    path = path or (CACHE if os.path.exists(CACHE) else None)
    if not path:
        print("No TAFEP copy yet; run `python cli.py fetch-tafep` (or pass --tafep data/fixtures/tafep_sample.json).",
              file=sys.stderr)
        return None
    return tafep.TafepList.load(path)


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch-tafep")
    for name in ("card", "check-page"):
        p = sub.add_parser(name)
        if name == "check-page":
            p.add_argument("out")
        p.add_argument("--uen", required=True)
        p.add_argument("--name", required=True, help="registered name from ACRA / FEAT-001")
        p.add_argument("--brand", help="brand name people review under, if FEAT-001 found one")
        p.add_argument("--tafep", help="path to a TAFEP list copy (default: data/cache)")
        p.add_argument("--json", action="store_true")
    p = sub.add_parser("nodeflair-probe")
    p.add_argument("slugs", nargs="+")
    a = ap.parse_args(argv)

    if a.cmd == "fetch-tafep":
        path = tafep.fetch()
        t = tafep.TafepList.load(path)
        print(f"Saved {path}: {len(t.index)} employers, list updated to {t.latest_update}")
    elif a.cmd == "card":
        card = build_card(a.uen, a.name, _load_tafep(a.tafep), a.brand)
        print(json.dumps(card, indent=2) if a.json else render_text(card))
    elif a.cmd == "check-page":
        card = build_card(a.uen, a.name, _load_tafep(a.tafep), a.brand)
        rows = "".join(f'<li><a href="{html.escape(l["url"])}" target="_blank">{html.escape(l["label"])}</a> '
                       f'({l["url_status"]}) - does it land on {html.escape(card["search_name"])}?</li>'
                       for l in card["linkouts"])
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(f"<!doctype html><meta charset=utf-8><title>Link check</title>"
                    f"<h1>{html.escape(card['legal_name'])}</h1><ul>{rows}</ul>")
        print(f"Wrote {a.out}")
    elif a.cmd == "nodeflair-probe":
        for slug in a.slugs:
            print(json.dumps(nodeflair.probe(slug)))


if __name__ == "__main__":
    main()
