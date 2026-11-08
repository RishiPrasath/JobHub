"""E1a: bulk-download all ACRA entity CSVs from data.gov.sg (no key). Args: output_dir"""
import json, sys, time, urllib.request
from pathlib import Path

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
def get(u, t=60):
    return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "JobHub-research/0.1"}), timeout=t)
ids = json.load(get("https://api-production.data.gov.sg/v2/public/api/collections/2/metadata"))["data"]["collectionMetadata"]["childDatasets"]
log = []
for i in ids:
    dest = out / f"{i}.csv"
    if dest.exists(): continue
    for attempt in range(6):
        try:
            r = json.load(get(f"https://api-open.data.gov.sg/v1/public/api/datasets/{i}/poll-download"))
            if r.get("code") == 0 and r["data"].get("url"):
                t0 = time.time()
                dest.write_bytes(get(r["data"]["url"], 300).read())
                log.append((i, dest.stat().st_size, round(time.time() - t0, 1))); print(log[-1], flush=True)
                break
            print(i, "retry", r.get("name"), flush=True)
        except Exception as e:
            print(i, "err", repr(e)[:100], flush=True)
        time.sleep(12)
    time.sleep(6)
print("done", len(list(out.glob("*.csv"))))
