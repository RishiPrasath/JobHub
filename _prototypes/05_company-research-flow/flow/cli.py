"""python -m flow.cli serve | research <employer> | cases <cases.json> <out_dir>"""
import argparse
import concurrent.futures as cf
import json
import os
import sys
from pathlib import Path

from . import config, orchestrator, server
from .render import render_text


def main():
    ap = argparse.ArgumentParser(prog="flow")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("serve")
    r = sub.add_parser("research", help="run one research and print it")
    r.add_argument("employer")
    r.add_argument("--role", default="")
    r.add_argument("--uen")
    r.add_argument("--url")
    r.add_argument("--json", action="store_true")
    c = sub.add_parser("cases", help="run the pre-registered cases and compare each headline with what was expected")
    c.add_argument("cases_json")
    c.add_argument("out_dir")
    c.add_argument("--only", nargs="*")
    c.add_argument("--workers", type=int, default=2)
    a = ap.parse_args()

    if a.cmd == "serve":
        server.serve(config.PORT)
    elif a.cmd == "research":
        res = orchestrator.research({"employer": a.employer, "role": a.role, "uen": a.uen, "url": a.url})
        print(json.dumps(res, indent=1, ensure_ascii=False) if a.json else render_text(res))
    else:
        spec = json.loads(Path(a.cases_json).read_text(encoding="utf-8"))["cases"]
        todo = [x for x in spec if not a.only or x["id"] in a.only]
        out = Path(a.out_dir)
        out.mkdir(parents=True, exist_ok=True)

        def one(case):
            res = orchestrator.research({"employer": case["employer"], "role": case.get("role"), "uen": case.get("uen")})
            (out / (case["id"] + ".json")).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
            (out / (case["id"] + ".txt")).write_text(render_text(res), encoding="utf-8")
            verdict = "RIGHT" if res["headline"] in case["expect"] else ("DANGEROUS" if res["headline"] in case.get("wrong_if", []) else "OFF")
            print("%s %-9s %-34s expected %-44s got %-32s (%ss)" % (case["id"], verdict, case["employer"][:34], "/".join(case["expect"]), res["headline"], res["seconds"]), flush=True)
            return {"id": case["id"], "seen": case["seen"], "employer": case["employer"], "expected": case["expect"], "got": res["headline"],
                    "verdict": verdict, "reasons": res["reasons"], "degraded": res["degraded"], "seconds": res["seconds"]}

        with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
            rows = list(ex.map(one, todo))
        (out / "summary.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
        for label, flag in (("seen before", True), ("new", False)):
            sel = [x for x in rows if x["seen"] is flag]
            print("%-12s %d cases: %d right, %d off, %d dangerous" % (label, len(sel), sum(x["verdict"] == "RIGHT" for x in sel),
                                                                      sum(x["verdict"] == "OFF" for x in sel), sum(x["verdict"] == "DANGEROUS" for x in sel)))


if __name__ == "__main__":
    main()
