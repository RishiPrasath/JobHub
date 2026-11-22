"""Offline tests for P06. Run: python -m unittest discover -s tests"""
import json
import os
import sys
import unittest
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from reviews import tafep  # noqa: E402
from reviews.card import build_card, render_text  # noqa: E402
from reviews.linkouts import build_linkouts  # noqa: E402
from reviews.names import search_name, normalise_uen  # noqa: E402
from reviews.nodeflair import parse_aggregate  # noqa: E402

FIXTURE = os.path.join(ROOT, "data", "fixtures", "tafep_sample.json")

# Expected counts, from E16 run-003 (live list, 2026-11-21), checked again 2026-11-22.
EXPECTED = {
    "196800306E": 8,   # DBS Bank
    "201324745D": 6,   # GrabTaxi
    "199201624D": 10,  # Singtel
    "201300296D": 1,   # Carousell
    "198304925E": 3,   # Sheng Siong Supermarket
    "201503526N": 2,   # Shopee Singapore
    "201412014E": 3,   # Ninja Logistics
    "199304055W": 1,   # Randstad
}


class Names(unittest.TestCase):
    def test_suffixes(self):
        self.assertEqual(search_name("DBS BANK LTD."), "DBS Bank")
        self.assertEqual(search_name("SHOPEE SINGAPORE PRIVATE LIMITED"), "Shopee Singapore")
        self.assertEqual(search_name("RANDSTAD PTE. LIMITED"), "Randstad")
        self.assertEqual(search_name("SHENG SIONG SUPERMARKET PTE LTD"), "Sheng Siong Supermarket")
        self.assertEqual(search_name("Carousell Pte. Ltd."), "Carousell")

    def test_brand_wins(self):
        self.assertEqual(search_name("GRABTAXI PTE. LTD.", brand="Grab"), "Grab")

    def test_uen(self):
        self.assertEqual(normalise_uen(" 196800306e "), "196800306E")


class Linkouts(unittest.TestCase):
    def test_four_providers_and_no_fetch(self):
        links = build_linkouts("DBS Bank")
        self.assertEqual([l["provider"] for l in links], ["glassdoor", "indeed", "jobstreet", "google_maps"])
        for l in links:
            self.assertFalse(l["fetched_by_jobhub"])
            self.assertTrue(l["url"].startswith("https://"))

    def test_query_is_encoded(self):
        links = {l["provider"]: l for l in build_linkouts("Tan & Sons")}
        q = parse_qs(urlparse(links["glassdoor"]["url"]).query)["keyword"][0]
        self.assertEqual(q, "Tan & Sons")
        self.assertEqual(parse_qs(urlparse(links["google_maps"]["url"]).query)["query"][0], "Tan & Sons Singapore")

    def test_override(self):
        links = {l["provider"]: l for l in build_linkouts("Grab", {"glassdoor": "https://www.glassdoor.sg/Overview/x.htm"})}
        self.assertEqual(links["glassdoor"]["url_status"], "checked_by_person")


class Tafep(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = tafep.TafepList.load(FIXTURE)

    def test_counts_match_live_list(self):
        for uen, n in EXPECTED.items():
            r = self.t.lookup(uen)
            self.assertTrue(r["found"], uen)
            self.assertEqual(len(r["standards"]), n, uen)
            self.assertIn(f"Adopted {n} of 10", r["text"])

    def test_not_listed_says_nothing_bad(self):
        r = self.t.lookup("200000000Z")
        self.assertFalse(r["found"])
        self.assertTrue(r["text"].startswith("Not on TAFEP's list"))
        self.assertIn("does not mean poor practice", r["caveat"])

    def test_rescinded_only_is_not_found(self):
        r = self.t.lookup("T20LL1315F")
        self.assertFalse(r["found"])
        self.assertEqual(r["rescinded"], ["MFL"])

    def test_latest_date_and_names(self):
        self.assertEqual(self.t.latest_update, "2024-07-10")
        r = self.t.lookup("201324745d")
        self.assertEqual(r["listed_name"], "GRABTAXI PTE. LTD.")
        self.assertIn("Work-Life Harmony", r["text"])

    def test_wrapped_cache_format(self):
        import tempfile
        rows = json.load(open(FIXTURE, encoding="utf-8"))
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump({"fetched_at": "2026-11-01T00:00:00Z", "rows": rows}, f)
        t = tafep.TafepList.load(f.name)
        os.unlink(f.name)
        card = build_card("196800306E", "DBS BANK LTD.", t, brand="DBS")
        self.assertIn("stale_notice", card["tripartite_standards"])


class Card(unittest.TestCase):
    def test_card_has_no_review_content(self):
        t = tafep.TafepList.load(FIXTURE)
        card = build_card("201324745D", "GRABTAXI PTE. LTD.", t, brand="Grab")
        self.assertEqual(card["search_name"], "Grab")
        blob = json.dumps(card).lower()
        self.assertNotIn("nodeflair", blob)
        self.assertNotIn("ratingvalue", blob)
        self.assertNotIn("review_count", blob)
        self.assertIn("Adopted 6 of 10", render_text(card))


class NodeFlair(unittest.TestCase):
    # Shape copied from the live Grab page's JSON-LD (2026-11-22); numbers only, no review text.
    HTML = ('<html><head><script type="application/ld+json">{"@context":"https://schema.org/",'
            '"@type":"EmployerAggregateRating","reviewCount":556,"ratingCount":556,"ratingValue":4,'
            '"bestRating":5,"worstRating":1,"itemReviewed":{"@type":"Organization","name":"Grab",'
            '"sameAs":"https://grab.careers","url":"https://nodeflair.com/companies/grab"}}</script>'
            '<script type="application/ld+json">{"@type":"BreadcrumbList"}</script></head></html>')

    def test_parse(self):
        a = parse_aggregate(self.HTML)
        self.assertEqual(a["review_count"], 556)
        self.assertEqual(a["company_website"], "https://grab.careers")

    def test_no_block(self):
        self.assertIsNone(parse_aggregate("<html></html>"))


if __name__ == "__main__":
    unittest.main()
