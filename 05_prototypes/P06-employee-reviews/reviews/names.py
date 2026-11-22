"""Turn a registered entity name into a short search name for link-outs."""
import re

# Longest first, so "PTE. LTD." is removed before "LTD.".
_SUFFIXES = [
    r"PRIVATE LIMITED", r"PTE\.? LTD\.?", r"PTE\.? LIMITED", r"SDN\.? BHD\.?",
    r"LIMITED LIABILITY PARTNERSHIP", r"LIMITED", r"LTD\.?", r"LLP", r"INC\.?",
    r"CORPORATION", r"CORP\.?", r"\(S\)", r"\(SINGAPORE\)",
]
_SUFFIX_RE = re.compile(r"(?:[\s,]+(?:" + "|".join(_SUFFIXES) + r"))+\s*$", re.I)


def normalise_uen(uen: str) -> str:
    """Upper-case a UEN and drop spaces. Does not check the format."""
    return re.sub(r"\s+", "", uen or "").upper()


def search_name(legal_name: str, brand: str | None = None) -> str:
    """Name to search on review sites.

    A brand from the employer identity check (FEAT-001) wins, because legal
    names often differ from the name people review under
    (GRABTAXI PTE. LTD. is reviewed as "Grab").
    """
    if brand and brand.strip():
        return brand.strip()
    name = _SUFFIX_RE.sub("", (legal_name or "").strip()).strip(" ,.")
    if name.isupper():
        # Keep short all-caps words such as DBS or UOB as they are.
        name = " ".join(w if len(w) <= 3 else w.capitalize() for w in name.split())
    return name
