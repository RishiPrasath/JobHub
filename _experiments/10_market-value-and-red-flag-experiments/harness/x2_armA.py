import json, urllib.request, urllib.parse, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
d = json.load(open(R / "data/x2_groundtruth.json", encoding="utf-8"))
out = {}; correct = 0
for b in d["brands"]:
    j = json.load(urllib.request.urlopen("http://localhost:8090/check?name=" + urllib.parse.quote(b["brand"]), timeout=30))
    e = j.get("entity") or {}
    ok = e.get("uen") in b["uens"]
    correct += ok
    out[b["brand"]] = dict(verdict=j["verdict"], uen=e.get("uen"), name=e.get("name"), status=e.get("status"), correct=ok)
    print(b["brand"], "|", j["verdict"], "|", e.get("uen"), e.get("name"), "|", "CORRECT" if ok else "no")
print("correct", correct, "of", len(d["brands"]))
json.dump(out, open(R / "outputs/x2/armA.json", "w"), indent=1)
