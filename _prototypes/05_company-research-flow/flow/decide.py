"""The headline: one of a small set of plain statements, derived from the registry verdict and the web evidence.
Pure function, no network, so every row of the table is unit-tested. The model's own rating is an input, never the answer.

Headlines
  exists_and_consistent           registered and the web evidence agrees (several independent sources)
  exists_limited_evidence         registered, but the web evidence is thin, or it could not be gathered
  brand_legal_entity_unconfirmed  the registry cannot confirm this exact name, but the web clearly describes a company with this name
                                  (Grab, Ninja Van, KPMG here: brand names that are not a registered legal name)
  likely_lookalike                the registry's closest name is a different entity and the web never uses this exact name
  could_not_confirm_company       nothing in the registry or on the web confirms it
  ambiguous_entity                two or more live entities share the name; the posting needs a company ID or address
  not_active                      the entity exists but is struck off, in liquidation, ceased, suspended and so on
  identity_mismatch               the company ID in the posting belongs to a different name, or does not exist
  public_body                     a statutory board or ministry; not in the company registry
  web_evidence_only               the registry could not be reached; public sources do use the exact name, but existence as a registered company is unchecked
  unavailable                     the registry could not be reached and the web evidence does not settle it
"""

SUPPRESS_POSITIVES = {"likely_lookalike", "could_not_confirm_company", "identity_mismatch", "ambiguous_entity", "not_active"}

MEANING = {
    "exists_and_consistent": "Registered in Singapore, and public sources agree it is the company named.",
    "exists_limited_evidence": "Registered in Singapore, but there is little public evidence beyond the registry.",
    "brand_legal_entity_unconfirmed": "Public sources describe a company by this name, but the registry has no entity with this exact name. It may trade under a brand name; the legal employer is not confirmed.",
    "likely_lookalike": "No registered company has this exact name and no source uses it. The closest registered name belongs to a different company. Treat the posting with caution.",
    "could_not_confirm_company": "Neither the registry nor the web confirms this company exists under this name.",
    "ambiguous_entity": "More than one live company is registered with this exact name. A company ID or address is needed to say which one.",
    "not_active": "A company with this name is registered, but its status is not live.",
    "identity_mismatch": "The company ID in the posting does not match the name in the posting.",
    "public_body": "A government body or statutory board. These are not in the company registry; check the agency's own .gov.sg site.",
    "web_evidence_only": "The company registry could not be reached, so existence as a registered company is unchecked. Public sources do use this exact name.",
    "unavailable": "The company registry could not be reached and the web evidence does not settle it.",
}


def headline(registry, gate, web):
    """registry: the /check answer, or None when the registry was unreachable.
    gate: flow.gate.run(...) result. web: {'available': bool, 'pages_ok': int, 'model_status': str|None}.
    Returns (headline, [reasons])."""
    why = []
    if registry is None:
        if gate and gate["strong"]:
            return "web_evidence_only", ["registry unreachable", "web evidence uses the exact name %d times" % (gate["pages_with_exact_name"] + gate["snippets_with_exact_name"])]
        return "unavailable", ["registry unreachable", "web evidence does not settle it"]
    v = registry["verdict"]
    if v in ("uen_name_mismatch", "uen_not_found"):
        return "identity_mismatch", ["registry: " + v]
    if v == "registered_not_active":
        return "not_active", ["registry: " + v]
    if v == "multiple_entities":
        return "ambiguous_entity", ["registry: " + v]
    if v == "public_body":
        return "public_body", ["registry: " + v]
    if v in ("confirmed", "probable", "former_name"):
        why.append("registry: " + v)
        if not web["available"]:
            return "exists_limited_evidence", why + ["web research unavailable"]
        if gate["none"] and web["pages_ok"] > 0:
            # registered, yet every page read is about something else: do not call it consistent
            return "exists_limited_evidence", why + ["no page or search result uses the exact name"]
        if web["model_status"] == "appears_real_and_consistent" and web["pages_ok"] >= 2 and not gate["none"]:
            return "exists_and_consistent", why + ["model: consistent across %d pages" % web["pages_ok"]]
        return "exists_limited_evidence", why + ["web evidence thin (%d pages read, model: %s)" % (web["pages_ok"], web["model_status"])]
    # similar_name_only, not_in_registry
    why.append("registry: " + v)
    if gate["strong"]:
        return "brand_legal_entity_unconfirmed", why + ["exact name seen %d times in sources" % (gate["pages_with_exact_name"] + gate["snippets_with_exact_name"])]
    if v == "similar_name_only" and gate["none"]:
        return "likely_lookalike", why + ["closest registered name is a different entity", "exact name appears in no source"]
    return "could_not_confirm_company", why + ["exact name seen %d times" % (gate["pages_with_exact_name"] + gate["snippets_with_exact_name"])]
