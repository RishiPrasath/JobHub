"""E22 Part C: domain -> legal entity chain. One polite lookup per domain per service.

- SGNIC RDAP (.sg domains only): registrant organisation name and registration date.
  Only the registrant role and dates are kept. Admin, technical and billing contacts can
  hold personal names and emails, so they are dropped before anything is written.
- Live TLS certificate from the site itself: subject O (organisation), serialNumber and
  jurisdiction fields (OV/EV certs carry these; DV certs do not).
- crt.sh: one JSON query per domain, to see if any certificate ever logged for the
  exact host has an organisation in the issuer-visible subject. crt.sh is flaky; one try.
- Wayback CDX: first capture date (limit 1).
Then any legal name found is looked up in ACRA (data.gov.sg, 3 s gap).
"""
import json
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "runs/2026-11-21-run-001/outputs/domain_chain"
OUT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(Path(__file__).resolve().parent))
UA = {"User-Agent": "JobHubResearch"}
GAP = 5.0
_last = {}


def polite_get(url, timeout=40):
    host = urllib.parse.urlparse(url).netloc
    wait = _last.get(host, 0) + GAP - time.time()
    if wait > 0:
        time.sleep(wait)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:
        return type(e).__name__, b""
    finally:
        _last[host] = time.time()


def rdap(domain):
    if not domain.endswith(".sg"):
        return {"outcome": "not_sg_domain"}
    st, body = polite_get(f"https://rdap.sgnic.sg/rdap/domain/{domain}")
    if st != 200:
        return {"outcome": f"http_{st}"}
    d = json.loads(body)
    reg = None
    for e in d.get("entities", []):
        if "registrant" in e.get("roles", []):
            for f in e.get("vcardArray", [None, []])[1]:
                if f[0] == "fn":
                    reg = f[3]
    if reg and not re.search(r"(PTE|LTD|LIMITED|LLP|INC|GMBH|CO|CORP|GROUP|HOLDINGS|BHD|IT)", reg, re.I):
        reg = None  # registrant looks like a person: personal data, not kept (redacted)
    ev = {e["eventAction"]: e["eventDate"] for e in d.get("events", [])}
    return {"outcome": "ok", "registrant": reg, "registered": ev.get("registration")}


def live_cert(host):
    ctx = ssl.create_default_context()
    try:
        with socket.create_connection((host, 443), timeout=20) as s:
            with ctx.wrap_socket(s, server_hostname=host) as t:
                c = t.getpeercert()
        subj = {k: v for rdn in c.get("subject", ()) for k, v in rdn}
        iss = {k: v for rdn in c.get("issuer", ()) for k, v in rdn}
        return {"outcome": "ok", "subject_O": subj.get("organizationName"),
                "subject_serialNumber": subj.get("serialNumber"),
                "jurisdiction": subj.get("jurisdictionCountryName"),
                "businessCategory": subj.get("businessCategory"),
                "issuer_O": iss.get("organizationName"),
                "type": "EV" if subj.get("serialNumber") and subj.get("businessCategory") else ("OV" if subj.get("organizationName") else "DV")}
    except Exception as e:
        return {"outcome": f"error {type(e).__name__}: {str(e)[:120]}"}


def crtsh(host):
    st, body = polite_get(f"https://crt.sh/?q={host}&output=json&exclude=expired", timeout=60)
    if st != 200:
        return {"outcome": f"http_{st}"}
    try:
        rows = json.loads(body)
    except Exception:
        return {"outcome": "bad_json"}
    issuers = sorted({r.get("issuer_name", "")[:80] for r in rows})
    return {"outcome": "ok", "unexpired_certs": len(rows), "issuers": issuers[:8],
            "note": "crt.sh JSON gives issuer and names, not the subject O field"}


def wayback(domain):
    st, body = polite_get(f"https://web.archive.org/cdx/search/cdx?url={domain}&limit=1&output=json&fl=timestamp,original")
    if st != 200:
        return {"outcome": f"http_{st}"}
    try:
        rows = json.loads(body or b"[]")
    except Exception:
        return {"outcome": "bad_json"}
    return {"outcome": "ok", "first_capture": rows[1][0] if len(rows) > 1 else None}


from a_acra_match import call, exact, slim  # noqa: E402  (reuses ACRA client and its 3 s gap)

sample = json.loads((ROOT / "data/sample.json").read_text(encoding="utf-8"))
rows = []
for b in sample["brands"]:
    dom = b["domain"]
    host = urllib.parse.urlparse(b["home"]).netloc
    row = {"id": b["id"], "brand": b["brand"], "domain": dom,
           "rdap": rdap(dom), "cert": live_cert(host), "crtsh": crtsh(host), "wayback": wayback(dom)}
    names = []
    if row["rdap"].get("registrant"):
        names.append(("rdap", row["rdap"]["registrant"]))
    if row["cert"].get("subject_O"):
        names.append(("cert", row["cert"]["subject_O"]))
    acra = []
    for src, n in names:
        hits = exact(n)
        acra.append({"source": src, "name": n, "acra": [slim(h) for h in hits]})
    if row["cert"].get("subject_serialNumber"):
        recs = call({"filters": json.dumps({"uen": row["cert"]["subject_serialNumber"]})}).get("records", [])
        acra.append({"source": "cert_serial", "name": row["cert"]["subject_serialNumber"], "acra": [slim(h) for h in recs]})
    row["acra_links"] = acra
    rows.append(row)
    print(b["brand"], "| rdap:", row["rdap"].get("registrant"), row["rdap"].get("registered"),
          "| cert:", row["cert"].get("type"), row["cert"].get("subject_O"), row["cert"].get("subject_serialNumber"),
          "| crt:", row["crtsh"]["outcome"], "| wb:", row["wayback"].get("first_capture"),
          "| acra:", [(a["source"], [h["uen"] for h in a["acra"]]) for a in acra], flush=True)

(OUT / "chain_results.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
