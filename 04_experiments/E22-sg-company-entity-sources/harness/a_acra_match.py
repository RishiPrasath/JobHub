"""E22 Part A: brand name -> ACRA entity matching via the data.gov.sg datastore API (no key).

Contains information from "Entities Registered with ACRA" accessed on 2026-11-21 from data.gov.sg, which is made available under the terms of the Singapore Open Data Licence version 1.0 (https://data.gov.sg/open-data-licence).
"""
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "runs/2026-11-21-run-001/outputs/acra"
OUT.mkdir(parents=True, exist_ok=True)
RID = "d_3f960c10fed6145404ca7b821f263b87"
BASE = "https://data.gov.sg/api/action/datastore_search"
GAP = 3.0  # seconds between calls; documented limit is about 4 calls per 10 s without a key
LOG = OUT / "calls.jsonl"
_last = [0.0]
ATTRIBUTION = __doc__.split("\n\n")[1].strip()


def call(params):
    status, body = None, None
    for attempt in range(3):
        wait = _last[0] + GAP - time.time()
        if wait > 0:
            time.sleep(wait)
        url = BASE + "?" + urllib.parse.urlencode({"resource_id": RID, **params})
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "JobHubResearch"})
            with urllib.request.urlopen(req, timeout=60) as r:
                body = json.loads(r.read())
            status = 200
        except urllib.error.HTTPError as e:
            status = e.code
        _last[0] = time.time()
        with LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "params": params, "status": status,
                                "n": len(body["result"]["records"]) if body else None}) + "\n")
        if status == 429:
            time.sleep(15 * (attempt + 1))  # slow down, then retry
            continue
        break
    return body["result"] if body else {"records": [], "error": status}


def norm(s):
    s = s.upper().replace("&", " AND ")
    s = re.sub(r"[^A-Z0-9 ]", " ", s)
    s = re.sub(r"\bPRIVATE LIMITED\b", "PTE LTD", s)
    s = re.sub(r"\bLIMITED\b", "LTD", s)
    return re.sub(r"\s+", " ", s).strip()


LIVE = {"REGISTERED", "LIVE", "LIVE COMPANY", "EXISTING"}


def is_live(r):
    return (r.get("uen_status_desc") or "").upper() in LIVE


def search_token(token, cap=1500):
    recs, offset, full = [], 0, 0
    while True:
        res = call({"q": json.dumps({"entity_name": token}), "limit": 500, "offset": offset})  # field-scoped q = AND of words
        batch = res.get("records", [])
        if batch:
            full = int(batch[0]["_full_count"])
        recs += batch
        offset += 500
        if not batch or offset >= full or offset >= cap:
            break
    tk = norm(token)
    hits = [r for r in recs if re.search(r"\b" + re.escape(tk) + r"\b", norm(r["entity_name"]))]
    return recs, hits, full


def exact(name):
    """Exact filter on the name as written in upper case, then a field-scoped search with normalised equality."""
    res = call({"filters": json.dumps({"entity_name": name.upper()})})
    recs = res.get("records", [])
    if recs:
        return recs
    core = re.sub(r"(PTE|LTD|PRIVATE|LIMITED)", " ", norm(name)).strip()  # suffix words vary, search on the core
    res = call({"q": json.dumps({"entity_name": core}), "limit": 500})
    return [r for r in res.get("records", []) if norm(r["entity_name"]) == norm(name)]


def slim(r):
    return {k: r.get(k) for k in ("uen", "entity_name", "uen_status_desc", "entity_type_desc", "uen_issue_date", "reg_postal_code")}


def main():
    sample = json.loads((ROOT / "data/sample.json").read_text(encoding="utf-8"))
    truth = json.loads((ROOT / "data/truth.json").read_text(encoding="utf-8"))

    rows = []
    for b in sample["brands"]:
        raw, hits, full = search_token(b["token"])
        live = [r for r in hits if is_live(r)]
        tk = norm(b["token"])
        exact_brand = [r for r in live if norm(r["entity_name"]) in (tk + " PTE LTD", tk + " LTD")]
        naive = exact_brand[0] if exact_brand else (min(live, key=lambda r: len(r["entity_name"])) if live else None)
        # post-hoc variant (not pre-registered): same rule but companies only, no sole proprietorships
        comp = [r for r in live if "Sole Proprietorship" not in (r.get("entity_type_desc") or "")]
        naive_co = exact_brand[0] if exact_brand else (min(comp, key=lambda r: len(r["entity_name"])) if comp else None)
        t = truth[b["id"]]
        truth_recs = []
        if t.get("sg_truth_uen"):
            truth_recs = call({"filters": json.dumps({"uen": t["sg_truth_uen"]})}).get("records", [])
        elif t.get("sg_truth_name"):
            truth_recs = exact(t["sg_truth_name"])
        truth_uen = truth_recs[0]["uen"] if truth_recs else None
        alt_uens = []
        for a in t.get("alt", []):
            alt_uens += [r["uen"] for r in exact(a)]
        postal = []
        if t.get("postal"):
            res = call({"filters": json.dumps({"reg_postal_code": t["postal"]}), "limit": 500})
            postal = [slim(r) for r in res.get("records", []) if tk in norm(r["entity_name"])]
        row = {
            "id": b["id"], "brand": b["brand"], "kind": b["kind"], "q_full_count": full,
            "q_records_fetched": len(raw), "token_hits": len(hits), "token_hits_live": len(live),
            "naive_top1": slim(naive) if naive else None,
            "naive_company_top1": slim(naive_co) if naive_co else None,
            "token_hits_live_companies": len(comp),
            "truth_name": t.get("sg_truth_name"), "truth_found_in_acra": bool(truth_recs),
            "truth": slim(truth_recs[0]) if truth_recs else None, "alt_uens": alt_uens,
            "truth_in_token_hits": bool(truth_uen) and any(r["uen"] == truth_uen for r in hits),
            "naive_correct": (naive is not None and naive["uen"] in [truth_uen] + alt_uens) if truth_uen else None,
            "naive_company_correct": (naive_co is not None and naive_co["uen"] in [truth_uen] + alt_uens) if truth_uen else None,
            "postal_brand_entities": postal,
            "live_hits_sample": [slim(r) for r in sorted(live, key=lambda r: len(r["entity_name"]))[:30]],
        }
        rows.append(row)
        print(b["brand"], full, len(hits), len(live), "| naive:", naive and naive["entity_name"],
              "| co:", naive_co and naive_co["entity_name"], "| truth:", truth_uen, "| ok:", row["naive_correct"], row["naive_company_correct"], flush=True)

    looks = []
    for lk in sample["lookalikes"]:
        ex = exact(lk["name"])
        looks.append({"id": lk["id"], "name": lk["name"], "exact_matches": [slim(r) for r in ex],
                      "accepted_by_exact_match": any(is_live(r) for r in ex)})
        print(lk["name"], "->", [r["entity_name"] + " " + r["uen_status_desc"] for r in ex], flush=True)

    (OUT / "match_results.json").write_text(json.dumps({"attribution": ATTRIBUTION, "brands": rows, "lookalikes": looks},
                                                       indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
