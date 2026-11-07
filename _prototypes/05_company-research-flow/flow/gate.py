"""Name gate: does the exact name from the posting appear in any page or search result?

If it never does, the evidence cannot be about this entity (the experiment's lookalike case: the model used a real bank's
reviews as evidence about a fake 'Bank Recruitment' company). A prompt rule did not stop that, so this is code.
Counts are kept so the output can say how strong the evidence is. Thresholds were set from experiment 09's eight companies,
so they are not an unbiased estimate; the six new cases in tests/cases.json are the check."""
import re

SUFFIX = re.compile(r"\b(pte|ltd|limited|private|inc|llc|co)\b\.?", re.I)
STRONG_TOTAL = 3        # exact name seen at least this many times across pages and snippets = strong


def squash(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s or "").lower()).strip()


def phrase(name):
    return squash(SUFFIX.sub("", name))


def run(names, page_texts, snippets):
    """names: the name in the posting and, if known, the registered legal name. Either counts as the exact name."""
    phrases = [p for p in dict.fromkeys(phrase(n) for n in names if n) if p]
    pages = sum(1 for t in page_texts if any(p in squash(t) for p in phrases))
    snips = sum(1 for t in snippets if any(p in squash(t) for p in phrases))
    return {"phrases": phrases, "pages_with_exact_name": pages, "snippets_with_exact_name": snips,
            "none": pages + snips == 0, "strong": pages + snips >= STRONG_TOTAL}
