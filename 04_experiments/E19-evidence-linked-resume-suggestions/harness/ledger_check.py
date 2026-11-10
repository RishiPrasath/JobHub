"""Method 2 code check: test one suggestion against the ledger entries it cites.

Uses only the suggestion text and the cited entries. It knows nothing about the gold labels.
A suggestion passes only if every number, name, tool, credential, level word and outcome word it
contains also appears in a cited entry, it has no intent wording, and it cites at least one entry.
"""
from __future__ import annotations

import re

from common import entry_text, numbers_in

INTENT = re.compile(
    r"\b(will|would|shall|going to|plan(s|ning)? to|intend(s|ing)? to|aim(s|ing)? to|committed to|commit(s)? to|"
    r"willing(ness)? to|ready to|prepared to|eager to|open to|currently (pursuing|studying|working towards|obtaining)|"
    r"in progress|working towards|expected to|looking to|able to obtain|to obtain|to acquire|to get a)\b", re.I)

# credential / tool / topic lexicon: each stem found in the suggestion must appear in the cited text
LEXICON = [
    r"licen[cs]\w*", r"class\s*\d", r"certif\w*", r"diploma", r"degree", r"bachelor", r"nitec", r"forklift", r"hazmat",
    r"\bpsa\b", r"rigger", r"signalman", r"first aid", r"\bcpr\b", r"\baed\b", r"\bwsq\b", r"food", r"hygiene", r"safety",
    r"qualified", r"accredited", r"graduat\w*", r"\bexcel\b", r"\bword\b", r"powerpoint", r"\bsap\b", r"\berp\b", r"\bwms\b",
    r"\bpos\b", r"scanner", r"whatsapp", r"canva", r"xero", r"quickbooks", r"zendesk", r"\bcrm\b", r"\bsql\b", r"python",
    r"tableau", r"pivot", r"vlookup", r"macro", r"formula", r"social media", r"marketing", r"account(s|ing)", r"invoic\w*",
    r"bookkeep\w*", r"retail", r"\bcash\b", r"\btill\b", r"appointment", r"filing", r"\bfile[sd]?\b", r"phone", r"e-?mail",
    r"\bchat\b", r"driving", r"driver", r"deliver\w*", r"warehouse", r"inventory", r"stock", r"route", r"dispatch",
    r"admin\w*", r"clerical", r"reception\w*", r"data entry", r"front.?desk", r"sales", r"mandarin", r"tamil", r"english", r"budget\w*", r"event\w*", r"customer\w*", r"patient\w*", r"clinic", r"mechanic\w*",
    r"automotive", r"vehicle\w*", r"workshop", r"team\w*", r"complaint\w*", r"cold", r"chilled", r"frozen", r"pallet\w*",
]
LEVEL_OUTCOME = re.compile(
    r"\b(advanced|expert\w*|proficien\w*|extensive\w*|strong\w*|senior|lead\w*|led|supervis\w*|skilled|proven|deep|"
    r"specialist|intermediate|seasoned|master\w*|highly|excellent|outstanding|manag\w*|oversaw|oversee\w*|"
    r"reduc\w*|improv\w*|increas\w*|accura\w*|efficien\w*|sav(ed|ing|ings)|boost\w*|streamlin\w*|on-time|error-free|"
    r"eliminat\w*|optimi[sz]\w*|enhanc\w*|success\w*|strengthen\w*|minimi[sz]\w*|decreas\w*|cut|satisf\w*|record|"
    r"achiev\w*|exceed\w*|award\w*|fast|quick\w*|top|best|key)\b", re.I)
EMPLOY_WORDS = r"(worked|work|employed|employment|experience|role|position|joined|internship|job|years?)"
STOP_CAP = {"I"}


def _tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9&'\-]+", text.lower())}


def _stem_present(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.I) is not None


def capital_phrases(text: str):
    """Capitalised word sequences and acronyms, with a flag for sentence-initial single words.

    The first word of a sentence is capitalised by position, so it is dropped from a multi-word
    sequence before the contiguity test. Limitation: a name at the very start of a sentence is
    only checked word by word.
    """
    out = []
    toks = [(m.start(), m.end(), m.group().strip(".")) for m in re.finditer(r"[A-Za-z][A-Za-z&'\-\.]*|\d+", text)]
    toks = [(a, b, w) for a, b, w in toks if w]
    i = 0
    while i < len(toks):
        a, b, w = toks[i]
        initial = (a == 0) or re.search(r"[.!?;:]\s*$|^\W*$", text[:a]) is not None
        if w[:1].isupper() and w not in STOP_CAP:
            j = i
            seq = [w]
            while j + 1 < len(toks) and toks[j + 1][2][:1].isupper() and re.fullmatch(r"\s+", text[toks[j][1]:toks[j + 1][0]] or " "):
                j += 1
                seq.append(toks[j][2])
            if initial and len(seq) >= 2:
                seq = seq[1:]
                out.append((seq, False) if len(seq) >= 2 else (seq, False))
                out.append(([w], True))
            else:
                out.append((seq, initial and len(seq) == 1 and not w.isupper()))
            i = j + 1
        else:
            i += 1
    return out


def check_suggestion(text: str, cited: list[dict], known_ids: set[str], entry_ids: list[str], requirement: str | None,
                     valid_requirements: set[str]) -> list[str]:
    """Return a list of failure codes. Empty list means the suggestion passes."""
    fails: list[str] = []
    if not entry_ids:
        fails.append("no_citation")
    if any(i not in known_ids for i in entry_ids):
        fails.append("unknown_entry_id")
    if requirement not in valid_requirements:
        fails.append("no_requirement")
    if not text or not text.strip():
        fails.append("empty")
        return fails
    if not cited:
        return fails
    ctext = " | ".join(entry_text(e) for e in cited)
    cl = ctext.lower()
    ctoks = _tokens(ctext)

    if INTENT.search(text):
        fails.append("intent_commitment")

    # numbers
    snums = numbers_in(text)
    cnums = numbers_in(ctext)
    bad = sorted(snums - cnums)
    if bad:
        fails.append("number_not_in_entry:" + ",".join(bad))
    if re.search(r"%|percent", text, flags=re.I):
        fails.append("percent_sign")

    # names: multi-word capitalised phrases must appear contiguously; single words must appear in entries
    for seq, skip in capital_phrases(text):
        phrase = " ".join(seq)
        if len(seq) >= 2:
            if phrase.lower() not in cl:
                fails.append("name_not_in_entry:" + phrase)
        else:
            w = seq[0]
            if skip:
                continue
            base = re.sub(r"[^A-Za-z0-9&]", "", w).lower()
            if base and base not in ctoks and not any(t.startswith(base) for t in ctoks):
                fails.append("name_not_in_entry:" + w)

    # lexicon
    for pat in LEXICON:
        if _stem_present(pat, text) and not _stem_present(pat, ctext):
            m = re.search(pat, text, flags=re.I)
            fails.append("term_not_in_entry:" + m.group().strip())
    # level and outcome words
    for m in LEVEL_OUTCOME.finditer(text):
        w = m.group().lower()
        present = (re.search(rf"\b{re.escape(w)}\b", cl) is not None) if len(w) <= 4 else (w[:5] in cl)
        if not present:
            fails.append("level_or_outcome_word:" + w)

    # organisation of a non-work entry used as an employer
    for e in cited:
        if e["type"] == "work":
            continue
        for key in ("institution", "issuing_body", "title", "name"):
            org = e.get(key)
            if org and len(org) > 4 and org.lower() in text.lower():
                if re.search(rf"{EMPLOY_WORDS}\W+(\w+\W+){{0,3}}(at|with|for)\W+(\w+\W+){{0,2}}{re.escape(org.lower())}", text.lower()) or \
                        re.search(rf"{re.escape(org.lower())}\W+(\w+\W+){{0,1}}(experience|role|position|employee|employer)", text.lower()):
                    fails.append("non_employer_used_as_employer:" + org)
    return sorted(set(fails))
