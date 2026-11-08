"""Name gate: a deterministic check applied AFTER the language model, over the saved Phase 3 outputs.

The model rated a lookalike employer 'appears real, high confidence' because pages about the real parent brand were
read as evidence about the lookalike. A prompt rule did not stop it. This gate asks a simpler, checkable question:
does the exact name from the posting (minus Pte/Ltd and punctuation) appear in any page text or in any search-result
title or snippet? If never, the evidence cannot be about this entity. Brand names that pages shorten (Ninja Van
Singapore -> Ninja Van) are still caught as present because search titles and snippets usually use the full name.

Run:  python rescore_gate.py        (reads /outputs/phase3, writes brief_gated.json per agent and gate_summary.json)
NOTE: the gate was designed after seeing these eight results, so its numbers here are a repair, not an unbiased test."""
import glob, json, os, re

OUT = "/outputs/phase3"
SUFFIX = re.compile(r"\b(pte|ltd|limited|private|inc|llc|co)\b\.?", re.I)
ORDER = ["cannot_verify", "inconsistent_or_suspicious", "appears_real_limited_evidence", "appears_real_and_consistent"]
CONF = ["low", "medium", "high"]


def squash(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s or "").lower()).strip()


def gate(company, page_texts, snippets):
    phrase = squash(SUFFIX.sub("", company))
    in_pages = sum(1 for t in page_texts if phrase in squash(t))
    in_snippets = sum(1 for t in snippets if phrase in squash(t))
    return {"phrase": phrase, "pages_with_exact_name": in_pages, "snippets_with_exact_name": in_snippets}


def apply(brief, g, pages_read):
    status, conf = brief["validity_status"], brief["confidence"]
    claims_real = status.startswith("appears_real")
    note = None
    if g["pages_with_exact_name"] + g["snippets_with_exact_name"] == 0 and claims_real:
        status = "inconsistent_or_suspicious" if pages_read else "cannot_verify"
        conf = "low"
        note = ("The exact name '%s' appears in no page and no search result. The evidence describes a similarly named entity, "
                "so it cannot confirm this one." % g["phrase"])
    elif g["pages_with_exact_name"] == 0 and status == "appears_real_and_consistent":
        status = "appears_real_limited_evidence"
        conf = "medium" if conf == "high" else conf
        note = "The exact name appears only in search snippets, never in a page that was read; evidence capped."
    return status, conf, note


if __name__ == "__main__":
    personas = {}
    src = open("/work/phase3_agents.py", encoding="utf-8").read()
    ns = {}
    exec(src.split("BLOCK =")[0].split("PERSONAS = ")[0] and "PERSONAS = " + src.split("PERSONAS = ")[1].split("\n]\n")[0] + "\n]", {}, ns)
    rows = []
    for p in ns["PERSONAS"]:
        d = f"{OUT}/{p['id']}"
        brief = json.load(open(d + "/brief.json", encoding="utf-8"))
        pages = [open(f, encoding="utf-8").read() for f in sorted(glob.glob(d + "/pages/*.md"))]
        snips = [(r.get("title") or "") + " " + (r.get("snippet") or "") for s in json.load(open(d + "/search_results.json", encoding="utf-8")) for r in s["results"]]
        g = gate(p["company"], pages, snips)
        status, conf, note = apply(brief, g, len(pages))
        out = {**brief, "llm_validity_status": brief["validity_status"], "llm_confidence": brief["confidence"],
               "validity_status": status, "confidence": conf, "name_gate": {**g, "note": note}}
        json.dump(out, open(d + "/brief_gated.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        rows.append({"persona": p["id"], "company": p["company"], "truth": p["truth"], "llm": f"{brief['validity_status']} / {brief['confidence']}",
                     "after_gate": f"{status} / {conf}", "changed": (status, conf) != (brief["validity_status"], brief["confidence"]), **g})
        print(f"{p['id']:16} LLM: {rows[-1]['llm']:48} gate: exact name in {g['pages_with_exact_name']} pages, {g['snippets_with_exact_name']} snippets -> {rows[-1]['after_gate']}")
    json.dump(rows, open(f"{OUT}/gate_summary.json", "w", encoding="utf-8"), indent=1)
