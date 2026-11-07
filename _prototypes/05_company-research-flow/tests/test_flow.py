"""No-network tests: every headline row, and each kind of outage. Run in the image:
docker run --rm --entrypoint python -e PYTHONPATH=/app jobhub-company-research-flow:dev -m unittest discover -s /app/tests -v"""
import unittest

from flow import config, decide, gate, orchestrator
from flow.http import Unavailable


def reg(verdict, entity=True, closest=False):
    e = {"name": "ACME PTE. LTD.", "uen": "201234567A", "status": "Live Company", "type": "Local Company", "incorporated": "2012-01-01", "activity": "Retail"}
    return {"verdict": verdict, "summary": verdict, "entity": e if entity else None, "closest": e if closest else None, "flags": [],
            "registry_as_of": "2026-10-14T17:21:16+08:00", "registry_stale": False, "basis": "name only"}


def g(pages=0, snips=0):
    return {"phrases": ["acme"], "pages_with_exact_name": pages, "snippets_with_exact_name": snips, "none": pages + snips == 0, "strong": pages + snips >= gate.STRONG_TOTAL}


def web(ok=True, pages=3, status="appears_real_and_consistent"):
    return {"available": ok, "pages_ok": pages, "model_status": status}


class HeadlineTable(unittest.TestCase):
    def h(self, r, gt, w):
        return decide.headline(r, gt, w)[0]

    def test_registered_and_consistent(self):
        self.assertEqual(self.h(reg("confirmed"), g(3, 5), web()), "exists_and_consistent")

    def test_registered_but_model_unsure(self):
        self.assertEqual(self.h(reg("confirmed"), g(1, 1), web(status="appears_real_limited_evidence")), "exists_limited_evidence")

    def test_registered_but_one_page(self):
        self.assertEqual(self.h(reg("probable"), g(1, 1), web(pages=1)), "exists_limited_evidence")

    def test_registered_but_pages_never_use_the_name(self):
        self.assertEqual(self.h(reg("confirmed"), g(0, 0), web()), "exists_limited_evidence")

    def test_registered_web_down(self):
        self.assertEqual(self.h(reg("confirmed"), g(), web(ok=False, pages=0, status=None)), "exists_limited_evidence")

    def test_brand_only(self):
        self.assertEqual(self.h(reg("similar_name_only", False, True), g(0, 4), web()), "brand_legal_entity_unconfirmed")

    def test_lookalike(self):
        self.assertEqual(self.h(reg("similar_name_only", False, True), g(0, 0), web()), "likely_lookalike")

    def test_fictitious(self):
        self.assertEqual(self.h(reg("not_in_registry", False), g(0, 0), web(ok=True, pages=0, status=None)), "could_not_confirm_company")

    def test_weak_exact_name_is_not_enough_for_brand(self):
        self.assertEqual(self.h(reg("similar_name_only", False, True), g(0, 2), web()), "could_not_confirm_company")

    def test_registry_settled(self):
        for v, want in (("uen_name_mismatch", "identity_mismatch"), ("uen_not_found", "identity_mismatch"), ("registered_not_active", "not_active"),
                        ("multiple_entities", "ambiguous_entity"), ("public_body", "public_body")):
            self.assertEqual(self.h(reg(v, False), g(), web(False, 0, None)), want)

    def test_registry_down(self):
        self.assertEqual(self.h(None, g(1, 5), web()), "web_evidence_only")
        self.assertEqual(self.h(None, g(0, 0), web()), "unavailable")
        self.assertEqual(self.h(None, g(), web(False, 0, None)), "unavailable")

    def test_every_headline_has_a_plain_meaning(self):
        for h in ("exists_and_consistent", "exists_limited_evidence", "brand_legal_entity_unconfirmed", "likely_lookalike", "could_not_confirm_company",
                  "ambiguous_entity", "not_active", "identity_mismatch", "public_body", "web_evidence_only", "unavailable"):
            self.assertIn(h, decide.MEANING)


class FakeDeps:
    """Stand-ins for the outside services. Counts calls so a test can prove a step was skipped."""
    def __init__(self, registry=None, registry_down=False, results=None, search_down=False, read=None, brief=None, brief_error=None):
        self.calls = {"registry": 0, "search": 0, "read": 0, "brief": 0}
        self._registry, self._registry_down, self._results, self._search_down = registry, registry_down, results or [], search_down
        self._read, self._brief, self._brief_error = read, brief, brief_error

    def registry_check(self, name, uen=None, url=None):
        self.calls["registry"] += 1
        if self._registry_down:
            raise Unavailable("ConnectionRefusedError: registry")
        return self._registry

    def web_search(self, q, limit=8):
        self.calls["search"] += 1
        if self._search_down:
            return {"query": q, "ok": False, "unavailable": True, "results": [], "engine": None, "error": "ConnectionRefusedError: search"}
        return {"query": q, "ok": True, "unavailable": False, "results": self._results, "engine": ["duckduckgo"], "error": None}

    def read_page(self, url, tokens):
        self.calls["read"] += 1
        if self._read:
            return self._read(url)
        return {"url": url, "status": "ok", "chars": 900, "text": "ACME is a retailer. " * 50, "note": None, "tier": "plain"}

    def write_brief(self, sources, header, posture=None):
        self.calls["brief"] += 1
        if self._brief_error:
            raise RuntimeError(self._brief_error)
        return self._brief or {"validity_status": "appears_real_and_consistent", "validity_reasoning": "x", "confidence": "medium", "could_not_verify": [],
                               "key_facts": [{"claim": "sells things", "evidence": [], "status": "verified"}],
                               "positive_signals": [{"claim": "good", "evidence": [], "status": "verified"}],
                               "red_flags": [{"claim": "late pay", "evidence": [], "status": "unverified"}]}, 100


def hit(i, domain="news.example.com", title="ACME Pte Ltd opens store", snippet="ACME is a retailer"):
    return {"rank": i, "engine": "duckduckgo", "title": title, "url": "https://%s/a%d" % (domain, i), "domain": domain, "snippet": snippet}


RESULTS = [hit(i, "site%d.example.com" % i) for i in range(1, 6)]


class Outages(unittest.TestCase):
    def run_flow(self, deps, employer="ACME Pte Ltd"):
        return orchestrator.research({"employer": employer, "role": "Clerk"}, deps)

    def test_registry_down_is_reported_and_not_called_confirmed(self):
        r = self.run_flow(FakeDeps(registry_down=True, results=RESULTS))
        self.assertTrue(any(d.startswith("registry_unavailable") for d in r["degraded"]))
        self.assertFalse(r["registry"]["available"])
        self.assertNotIn(r["headline"], ("exists_and_consistent", "exists_limited_evidence"))

    def test_search_down_is_not_reported_as_nothing_found(self):
        r = self.run_flow(FakeDeps(registry=reg("confirmed"), search_down=True))
        self.assertTrue(any(d.startswith("search_unavailable") for d in r["degraded"]))
        self.assertEqual(r["headline"], "exists_limited_evidence")
        self.assertTrue(any("not evidence that nothing is wrong" in x for x in r["could_not_verify"]))
        self.assertIsNone(r["brief"])

    def test_reader_down_falls_back_to_snippets_and_says_so(self):
        down = lambda url: {"url": url, "status": "unavailable", "chars": 0, "text": "", "note": "ConnectionRefusedError: reader", "tier": None}
        d = FakeDeps(registry=reg("confirmed"), results=RESULTS, read=down)
        r = self.run_flow(d)
        self.assertTrue(any(x.startswith("page_reader_unavailable") for x in r["degraded"]))
        self.assertLessEqual(d.calls["read"], 2)                       # stopped after two failures, did not hammer a dead service
        self.assertEqual(r["headline"], "exists_limited_evidence")
        self.assertTrue(r["could_not_read"])

    def test_model_failure_still_gives_a_headline_and_the_sources(self):
        r = self.run_flow(FakeDeps(registry=reg("confirmed"), results=RESULTS, brief_error="model service HTTP 500"))
        self.assertIsNone(r["brief"])
        self.assertTrue(any(x.startswith("summary_unavailable") for x in r["degraded"]))
        self.assertEqual(r["headline"], "exists_limited_evidence")
        self.assertTrue(r["web"]["pages"])

    def test_nothing_readable_and_no_snippets(self):
        fail = lambda url: {"url": url, "status": "error", "chars": 0, "text": "", "note": "HTTP 502", "tier": None}
        r = self.run_flow(FakeDeps(registry=reg("confirmed"), results=[hit(1, snippet="")], read=fail))
        self.assertTrue(any(x.startswith("no_web_sources") for x in r["degraded"]))
        self.assertEqual(r["headline"], "exists_limited_evidence")

    def test_time_budget(self):
        old = config.DEADLINE_SECONDS
        config.DEADLINE_SECONDS = -1
        try:
            d = FakeDeps(registry=reg("confirmed"), results=RESULTS)
            r = self.run_flow(d)
        finally:
            config.DEADLINE_SECONDS = old
        self.assertTrue(r["partial"])
        self.assertEqual(d.calls["search"], 0)

    def test_registry_settled_skips_the_web(self):
        for v in ("registered_not_active", "uen_name_mismatch", "public_body", "multiple_entities"):
            d = FakeDeps(registry=reg(v, False), results=RESULTS)
            r = self.run_flow(d)
            self.assertEqual(d.calls["search"], 0, v)
            self.assertIn("settled", r["web"]["skipped_reason"])

    def test_lookalike_hides_positives(self):
        r = self.run_flow(FakeDeps(registry=reg("similar_name_only", False, True), results=RESULTS),
                          "ACME Recruitment Pte Ltd")
        self.assertEqual(r["headline"], "likely_lookalike")
        self.assertEqual(r["brief"]["key_facts"], [])
        self.assertEqual(r["brief"]["positive_signals"], [])
        self.assertTrue(r["brief"]["red_flags"])
        self.assertIn("suppressed", r["brief"])

    def test_off_topic_results_are_not_read(self):
        res = [hit(i, "d%d.example.com" % i, "Scam awareness tips", "report a scam") for i in range(1, 6)] + [hit(9, "acme-news.example.com")]
        d = FakeDeps(registry=reg("confirmed"), results=res)
        r = self.run_flow(d)
        self.assertEqual(d.calls["read"], 1)                           # only the result that mentions ACME
        self.assertEqual(r["web"]["not_read_off_topic"], 5)

    def test_registry_mirror_pages_are_not_independent_evidence(self):
        res = [hit(1, "www.sgpbusiness.com"), hit(2, "recordowl.com"), hit(3, "www.companies.sg"), hit(4, "acme-news.example.com")]
        r = self.run_flow(FakeDeps(registry=reg("confirmed"), results=res))
        self.assertEqual(r["web"]["registry_mirror_pages"], 3)
        self.assertEqual(r["headline"], "exists_limited_evidence")      # the model says consistent, but only one page is independent

    def test_link_out_sites_are_never_read(self):
        urls = ["https://www.glassdoor.sg/Reviews/Acme-1", "https://www.reddit.com/r/x/1", "https://sg.indeed.com/cmp/Acme", "https://www.linkedin.com/company/acme",
                "https://sg.jobstreet.com/companies/acme"]
        res = [dict(hit(i), url=u, domain=u.split("/")[2]) for i, u in enumerate(urls, 1)] + [hit(9, "acme-news.example.com")]
        d = FakeDeps(registry=reg("confirmed"), results=res)
        r = self.run_flow(d)
        self.assertEqual(d.calls["read"], 1)                           # only the news site
        self.assertEqual(len(r["web"]["skipped_by_policy"]), 5); self.assertEqual(len(r["link_out"]), 5)

    def test_permissive_policy_reads_indeed_and_jobstreet_only(self):
        config.READ_POLICY = "permissive"
        try:
            res = [dict(hit(1), url="https://sg.indeed.com/cmp/Acme", domain="sg.indeed.com"), dict(hit(2), url="https://www.glassdoor.sg/x", domain="www.glassdoor.sg")]
            d = FakeDeps(registry=reg("confirmed"), results=res)
            self.run_flow(d)
            self.assertEqual(d.calls["read"], 1)
        finally:
            config.READ_POLICY = "conservative"


if __name__ == "__main__":
    unittest.main()
