"""Method 1: deterministic phrase matching against the rule pack. No model involved."""
import json
import re
from pathlib import Path

NEG = re.compile(r"\b(?:no|not|never|without|regardless of|irrespective of|do not|don't|does not|will not|won't|free of)\b", re.I)


def load_pack(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def source_block(pack, entry):
    out = []
    for sid in entry["source_ids"]:
        s = pack["sources"][sid]
        out.append({"source_id": sid, "name": s["name"], "url": s["url"], "accessed": s["accessed"]})
    return out


def match(pack, text):
    """Return flags: list of dicts with entry_id, category, excerpt, span, sources, texts."""
    flags, seen = [], set()
    for e in pack["entries"]:
        w = e.get("suppress_window", 100)
        for pat in e["patterns"]:
            for m in re.finditer(pat, text, flags=re.I):
                a, b = m.span()
                ctx = text[max(0, a - w): b + w]
                if any(re.search(s, ctx, flags=re.I) for s in e["suppress"]):
                    continue
                if e.get("negation_aware", True) and NEG.search(text[max(0, a - 60): a]):
                    continue
                key = (e["entry_id"], a, b)
                if key in seen:
                    continue
                seen.add(key)
                flags.append({
                    "entry_id": e["entry_id"], "category": e["category"], "excerpt": text[a:b], "span": [a, b],
                    "sources": source_block(pack, e), "source_support": e["source_support"],
                    "why_it_may_matter": e["why_it_may_matter"], "what_is_not_established": e["what_is_not_established"],
                    "suggested_question": e["suggested_question"]})
    # merge overlapping or touching spans of the same entry into one flag (union of the excerpts)
    flags.sort(key=lambda f: (f["entry_id"], f["span"][0]))
    keep = []
    for f in flags:
        k = keep[-1] if keep else None
        if k and k["entry_id"] == f["entry_id"] and f["span"][0] <= k["span"][1] + 1:
            k["span"][1] = max(k["span"][1], f["span"][1])
            k["excerpt"] = text[k["span"][0]:k["span"][1]]
        else:
            keep.append(f)
    return keep


def run(pack, cases):
    res = []
    for c in cases:
        fl = match(pack, c["text"])
        res.append({"case_id": c["case_id"], "method": "deterministic", "flags": fl, "no_reliable_signal": not fl})
    return res
