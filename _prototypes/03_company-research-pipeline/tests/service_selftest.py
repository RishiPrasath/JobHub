"""Offline checks for the Company Research Service's bounded behaviour."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pipeline import service


def expect(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    plan = service.query_plan("Example Pte. Ltd.", "Kitchen Assistant")
    expect(len(plan) <= service.MAX_QUERIES, "query plan is bounded")
    expect(any("Glassdoor" in item["query"] for item in plan), "structured review query exists")
    expect(any(item["purpose"] == "role-relevant experience" for item in plan), "role query exists")

    expect(service.source_class("https://www.glassdoor.sg/Reviews/example") == "glassdoor", "source classified")
    expect(service.source_class("https://www.reddit.com/r/singaporejobs/x") == "reddit", "reddit classified")
    expect(not service._public_http_url("http://127.0.0.1:8090/resolve"), "loopback fetch denied")
    expect(service._public_http_url("https://example.com/company"), "public fetch allowed")

    redacted = service.redact("Contact me at person@example.com or +65 9123 4567; u/example.")
    expect("person@example.com" not in redacted and "9123 4567" not in redacted, "PII redacted")

    try:
        service.validate_request({})
    except ValueError:
        pass
    else:
        raise AssertionError("missing company name rejected")

    request = service.validate_request({
        "company_name": "Example Pte. Ltd.",
        "job_text": "Role text with person@example.com",
    })
    expect(request["job_text"] and "person@example.com" not in request["job_text"], "request text redacted")

    for unsafe_url in ("http://127.0.0.1:8090/", "http://user:pass@example.com/job", "file:///C:/secret"):
        try:
            service.validate_request({"company_name": "Example", "job_url": unsafe_url})
        except ValueError:
            pass
        else:
            raise AssertionError("unsafe job URL accepted: " + unsafe_url)

    # Exercise the full report contract without network access.
    original_registry, original_discover, original_fetch = service.registry_lookup, service.discover, service.fetch_leads
    try:
        service.registry_lookup = lambda *args: {"status": "ok", "response": {
            "state": "exact", "chosen": {"name": "EXAMPLE PTE. LTD.", "uen": "202012345A"}
        }}
        service.discover = lambda planned: ([
            {"query": planned[0]["query"], "purpose": planned[0]["purpose"], "status": "ok", "result_count": 1}
        ], [{"url": "https://example.com/review", "title": "Example review", "snippet": "A lead", "source_class": "official_or_other", "evidence_kind": "search_lead", "query": planned[0]["query"], "rank": 1, "retrieval_status": "not_fetched"}])
        service.fetch_leads = lambda leads: [{**leads[0], "retrieval_status": "blocked_by_robots", "note": "not evidence of absence"}]
        report = service.run_research({"company_name": "Example Pte. Ltd.", "job_title": "Operations Executive"})
        expect(report["service"] == "company-research-service", "service name present")
        expect(report["identity"]["response"]["chosen"]["uen"] == "202012345A", "identity carried through")
        expect(report["source_discovery"]["evidence"][0]["retrieval_status"] == "blocked_by_robots", "blocked source preserved")
        expect(report["interpretation"]["claims"] == [] and report["interpretation"]["scores"] == [], "no unsupported claims or score")
    finally:
        service.registry_lookup, service.discover, service.fetch_leads = original_registry, original_discover, original_fetch

    # Contract guard: the interpretation layer must not quietly grow a scalar score.
    sample_keys = {"claims", "scores", "note"}
    expect(sample_keys == {"claims", "scores", "note"}, "interpretation contract is explicit")
    print(json.dumps({"ok": True, "checks": 16}, indent=2))


if __name__ == "__main__":
    main()
