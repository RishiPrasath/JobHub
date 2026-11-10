import hashlib, datetime
fs = ["protocol/thresholds.md", "data/ground_truth.json", "data/run_input.json"]
L = ["# FROZEN", "UTC: " + datetime.datetime.now(datetime.timezone.utc).isoformat(),
     "Frozen before any call to the system under test. Not committed to git (owner has not asked for commits).", ""]
L += ["%s  %s" % (hashlib.sha256(open(f, "rb").read()).hexdigest(), f) for f in fs]
open("protocol/FROZEN.md", "w").write("\n".join(L) + "\n")
print("\n".join(L))
