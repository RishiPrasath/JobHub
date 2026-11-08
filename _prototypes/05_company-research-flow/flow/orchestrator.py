"""One research run: registry check -> (only if the registry has not settled it) search -> read -> name gate -> cited brief -> headline.

Every outside call can fail. Failures are recorded in `degraded` and in the output wording; they are never turned into
'nothing found'. Services are passed in as `deps` so the failure paths are tested with stand-ins (tests/test_failures.py)."""
import time
import urllib.parse

from . import brief as briefmod
from . import config, decide, gate as gatemod, sources as src
from .http import Unavailable

REGISTRY_SETTLES = {"uen_name_mismatch", "uen_not_found", "public_body", "registered_not_active", "multiple_entities"}
MATCHED = {"confirmed", "probable", "former_name"}


class Deps:
    registry_check = staticmethod(src.registry_check)
    web_search = staticmethod(src.web_search)
    read_page = staticmethod(src.read_page)
    write_brief = staticmethod(briefmod.write)


def _registry_source(reg):
    e = reg["entity"]
    lines = ["Legal name: %s" % e["name"], "Company ID: %s" % e["uen"], "Status: %s" % e["status"], "Entity type: %s" % e["type"],
             "Registered: %s" % e["incorporated"], "Registered business activity: %s" % (e.get("activity") or "not stated")]
    lines += ["Note: " + f for f in reg.get("flags", [])]
    return {"url": "company registry (as of %s)" % (reg.get("registry_as_of") or "unknown date")[:10], "kind": "registry", "text": "\n".join(lines)}


def _rank_candidates(searches):
    seen, order = {}, []
    for s in searches:
        for r in s["results"]:
            u = r.get("url") or ""
            p = urllib.parse.urlparse(u)
            k = (p.netloc.lower().removeprefix("www.") + p.path.rstrip("/")).lower()
            if not k:
                continue
            if k not in seen:
                seen[k] = {**r, "hits": 0}
                order.append(k)
            seen[k]["hits"] += 1
    return [seen[k] for k in sorted(order, key=lambda k: (-seen[k]["hits"], order.index(k)))]


def research(req, deps=None):
    deps = deps or Deps()
    t0 = time.time()
    deadline = t0 + config.DEADLINE_SECONDS
    employer, role = req["employer"].strip(), (req.get("role") or "").strip()
    out = {"employer": employer, "role": role, "degraded": [], "partial": False}

    # 1. registry: existence and identity
    reg = None
    try:
        reg = deps.registry_check(employer, req.get("uen"), req.get("url"))
    except Unavailable as e:
        out["degraded"].append("registry_unavailable: %s" % e)
    verdict = (reg or {}).get("verdict")
    entity = (reg or {}).get("entity") if verdict in MATCHED else None
    names = [employer] + ([entity["name"]] if entity and entity["name"].lower() != employer.lower() else [])
    out["registry"] = {"available": reg is not None, **({k: reg.get(k) for k in ("verdict", "summary", "basis", "entity", "closest", "flags", "registry_as_of", "registry_stale")} if reg else {})}

    # 2. does the registry already settle it? then web research would not change the answer
    web = {"skipped_reason": None, "available": False, "queries": [], "pages": [], "skipped_by_policy": [], "gate": None, "engines_used": []}
    pages, searches, brief, sources = [], [], None, {}
    g = gatemod.run(names, [], [])
    model_status = None
    if verdict in REGISTRY_SETTLES:
        web["skipped_reason"] = "the registry settled it (%s); web research would not change the headline" % verdict
    else:
        # 3. search (OpenSERP, search only)
        for q in src.build_queries(names, role):
            if time.time() > deadline:
                out["partial"] = True
                break
            s = deps.web_search(q)
            searches.append(s)
            if s["unavailable"]:
                out["degraded"].append("search_unavailable: %s" % s["error"])
                break
        web["available"] = any(s["ok"] for s in searches)
        web["queries"] = [{"query": s["query"], "ok": s["ok"], "engine": s["engine"], "results": len(s["results"]), "error": s["error"]} for s in searches]
        web["engines_used"] = sorted({e for s in searches for e in (s["engine"] or [])})
        if searches and not web["available"] and not any("search_unavailable" in d for d in out["degraded"]):
            out["degraded"].append("search_failed: every query returned an error")

        # 4. choose and read pages: readable sites first; restricted sites are linked out, not fetched
        tokens = src.name_tokens(*names)
        reading, unavailable_reads = [], 0
        not_read_irrelevant = 0
        for c in _rank_candidates(searches):
            if len(reading) >= config.MAX_PAGES:
                break
            # spend the read budget on results whose title, snippet or address mention the company (first run: 40 of 88 reads were off-topic)
            if tokens and not any(t in ((c.get("title") or "") + " " + (c.get("snippet") or "") + " " + (c.get("url") or "")).lower() for t in tokens):
                not_read_irrelevant += 1
                continue
            if src.link_out_reason(c["url"]):
                if not any(x["url"] == c["url"] for x in web["skipped_by_policy"]):
                    web["skipped_by_policy"].append({"url": c["url"], "title": c.get("title"), "why": src.link_out_reason(c["url"])})
                continue
            if sum(1 for r in reading if r["domain"] == c["domain"]) >= config.PER_DOMAIN:
                continue
            reading.append(c)
        for c in reading:
            if time.time() > deadline:
                out["partial"] = True
                break
            rec = deps.read_page(c["url"], tokens)
            rec["search_snippet"] = c.get("snippet")
            pages.append(rec)
            if rec["status"] == "unavailable":
                unavailable_reads += 1
                if unavailable_reads >= 2:
                    out["degraded"].append("page_reader_unavailable: %s" % rec["note"])
                    break
        web["pages"] = [{k: v for k, v in p.items() if k not in ("text", "search_snippet")} for p in pages]
        web["not_read_off_topic"] = not_read_irrelevant

        # 5. numbered sources: registry record, pages that were read, and snippets of pages that could not be read
        n = 1
        if entity:
            sources[0] = _registry_source(reg)
        for p in pages:
            if p["status"] == "ok":
                sources[n] = {"url": p["url"], "kind": "page", "text": p["text"][:config.PAGE_CHARS]}
                n += 1
            elif p.get("search_snippet"):
                sources[n] = {"url": p["url"], "kind": "snippet_only", "text": p["search_snippet"]}
                n += 1
        all_snips = [(r.get("title") or "") + " " + (r.get("snippet") or "") for s in searches for r in s["results"]]
        g = gatemod.run(names, [p["text"] for p in pages if p["status"] == "ok"], all_snips)

        # 6. cited brief
        if len([s for s in sources.values() if s["kind"] != "registry"]) == 0:
            out["degraded"].append("no_web_sources: nothing could be read or found, so no summary was written")
        else:
            posture = None if verdict in MATCHED else (
                "The company registry did NOT confirm a company with this exact name. Report only scam, fraud, complaint or lookalike evidence and red flags. "
                "Do not describe working conditions as if the company were confirmed.")
            header = "Company named in the job posting: %s (Singapore). Role considered: %s." % (employer, role or "not given")
            try:
                brief, _ = deps.write_brief(sources, header, posture)
                model_status = brief["validity_status"]
            except RuntimeError as e:
                out["degraded"].append("summary_unavailable: %s" % e)

    out["web"] = {**web, "gate": g}

    # 7. headline from the registry and the gated web evidence
    independent = sum(1 for p in pages if p["status"] == "ok" and not src.is_registry_mirror(p["url"]))
    out["web"]["registry_mirror_pages"] = sum(1 for p in pages if p["status"] == "ok" and src.is_registry_mirror(p["url"]))
    h, reasons = decide.headline(reg, g, {"available": web["available"], "pages_ok": independent, "model_status": model_status})
    out.update(headline=h, headline_meaning=decide.MEANING[h], reasons=reasons)

    # 8. what to show from the brief
    if brief:
        keep_positive = h not in decide.SUPPRESS_POSITIVES
        brief["key_facts"] = brief["key_facts"] if keep_positive else []
        brief["positive_signals"] = brief["positive_signals"] if keep_positive else []
        brief["claims_verified"] = sum(1 for k in ("key_facts", "positive_signals", "red_flags") for c in brief[k] if c["status"] == "verified")
        brief["claims_unverified"] = sum(1 for k in ("key_facts", "positive_signals", "red_flags") for c in brief[k] if c["status"] == "unverified")
        brief["model_validity_status"] = brief.pop("validity_status")
        if not keep_positive:
            brief["suppressed"] = "facts and positive signals hidden: the company was not confirmed under this exact name"
        elif h == "brand_legal_entity_unconfirmed":
            brief["about"] = "the brand named in the posting; the registered legal employer is not confirmed"
    out["brief"] = brief

    out["could_not_read"] = [{"url": p["url"], "why": "%s: %s" % (p["status"], p["note"])} for p in pages if p["status"] != "ok"]
    out["link_out"] = web["skipped_by_policy"]            # restricted sites we do not fetch; the user can open these themselves
    cnv = list((brief or {}).get("could_not_verify", []))
    if h == "brand_legal_entity_unconfirmed":
        cnv.append("Which registered company is the legal employer behind this brand.")
    if not web["available"] and not web["skipped_reason"]:
        cnv.append("Anything from the web: search was unavailable or returned nothing usable. This is not evidence that nothing is wrong.")
    out["could_not_verify"] = cnv
    out["seconds"] = round(time.time() - t0, 1)
    out["disclaimer"] = config.DISCLAIMER
    return out
