"""Deterministic validation for guarded JobHub role-review output.

Usage:
    python claim_review_harness.py ../fixtures/sample-ai-output.json

The harness validates structure and safety boundaries only. It does not
determine whether a claim is factually true; a human must review provenance.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ALLOWED_STATES = {
    "present",
    "conditional",
    "conflicting",
    "unknown",
    "not_visible",
    "platform_signal",
}
ALLOWED_OWNERS = {"employer", "platform", "government", "mixed", "unknown"}
ALLOWED_REVIEW_STATUS = {"draft", "accepted", "edited", "rejected", "unresolved"}
ALLOWED_COVERAGE_STATUS = {"covered", "unknown", "not_visible", "conflicting"}

REQUIRED_REVIEW_SECTIONS = {
    "role_identity": ("title", "role", "company", "employer"),
    "duties": ("duty", "duties", "responsibil", "day-to-day", "task"),
    "qualifications": ("qualification", "requirement", "experience", "skill", "licen", "certif", "education"),
    "work_conditions": ("schedule", "hour", "weekday", "shift", "location", "on-site", "onsite", "remote", "work arrangement"),
    "compensation": ("pay", "salary", "wage", "hourly", "compensation", "rate"),
    "compensation_rules": ("rate determined", "rate depends", "base pay", "overtime", "allowance", "bonus", "deduction"),
    "application_process": ("application", "apply", "resume", "interview", "shortlisted", "submit"),
    "employer_context": ("legal employer", "hiring organisation", "hiring organization", "recruiter", "client relationship", "employer context"),
    "contradictions": ("conflict", "contradict", "mismatch", "do not align", "inconsistent"),
    "unknowns": ("unknown", "not established", "not stated", "not visible", "unclear", "missing", "unresolved"),
}


def assess_completeness(payload: dict) -> dict:
    """Report whether the output explicitly covers decision-critical areas.

    This is a conservative lexical gate, not a factual truth evaluator. A
    section is covered only when the output contains a claim or decision
    question that explicitly addresses it. Human review remains required.
    """
    explicit_coverage = payload.get("review_coverage")
    if isinstance(explicit_coverage, dict):
        required_sections = list(REQUIRED_REVIEW_SECTIONS) + ["verification_questions"]
        sections: dict[str, dict] = {}
        coverage_errors: list[str] = []
        questions = payload.get("decision_changing_questions")
        has_questions = isinstance(questions, list) and any(isinstance(item, str) and item.strip() for item in questions)

        for section in required_sections:
            entry = explicit_coverage.get(section)
            if not isinstance(entry, dict):
                sections[section] = {"status": "missing", "claim_ids": []}
                coverage_errors.append(f"review_coverage.{section} is missing or not an object")
                continue

            status = entry.get("status")
            claim_ids = entry.get("claim_ids")
            if status not in ALLOWED_COVERAGE_STATUS:
                coverage_errors.append(f"review_coverage.{section}.status is invalid: {status!r}")
                status = "missing"
            if not isinstance(claim_ids, list) or not all(isinstance(item, str) and item.strip() for item in claim_ids):
                coverage_errors.append(f"review_coverage.{section}.claim_ids must be an array of non-empty strings")
                claim_ids = []
            if section == "verification_questions":
                if status == "covered" and not has_questions:
                    coverage_errors.append("verification_questions is marked covered but decision_changing_questions is empty")
                    status = "missing"
                if status != "covered" and has_questions:
                    coverage_errors.append("decision_changing_questions contains questions but verification_questions is not covered")
            sections[section] = {"status": status, "claim_ids": claim_ids}

        missing_sections = [name for name, value in sections.items() if value["status"] == "missing"]
        return {
            "complete": not missing_sections and not coverage_errors,
            "missing_sections": missing_sections,
            "sections": sections,
            "coverage_errors": coverage_errors,
            "method": "explicit review_coverage statuses; human review still required",
        }

    claims = payload.get("claims") if isinstance(payload.get("claims"), list) else []
    claim_records = [claim for claim in claims if isinstance(claim, dict)]
    claim_texts = [str(claim.get("text", "")).lower() for claim in claim_records]
    questions = payload.get("decision_changing_questions")
    question_text = " ".join(item.lower() for item in questions if isinstance(item, str)) if isinstance(questions, list) else ""

    sections: dict[str, dict] = {}
    for section, markers in REQUIRED_REVIEW_SECTIONS.items():
        matched_ids = []
        for claim, text in zip(claim_records, claim_texts):
            if any(marker in text for marker in markers):
                claim_id = claim.get("claim_id")
                if isinstance(claim_id, str) and claim_id.strip():
                    matched_ids.append(claim_id)

        if section == "unknowns" and any(marker in question_text for marker in REQUIRED_REVIEW_SECTIONS["unknowns"]):
            status = "covered"
        elif matched_ids:
            status = "covered"
        else:
            status = "missing"

        sections[section] = {
            "status": status,
            "claim_ids": matched_ids,
        }

    if isinstance(questions, list) and any(isinstance(item, str) and item.strip() for item in questions):
        sections["verification_questions"] = {
            "status": "covered",
            "claim_ids": [],
        }
    else:
        sections["verification_questions"] = {
            "status": "missing",
            "claim_ids": [],
        }

    missing_sections = [name for name, value in sections.items() if value["status"] == "missing"]
    return {
        "complete": not missing_sections,
        "missing_sections": missing_sections,
        "sections": sections,
        "coverage_errors": [],
        "method": "conservative lexical coverage gate; human review still required",
    }


def validate(payload: dict) -> list[str]:
    errors: list[str] = []

    if not isinstance(payload, dict):
        return ["top-level output must be an object"]

    posting_id = payload.get("posting_id")
    if not isinstance(posting_id, str) or not posting_id.strip():
        errors.append("posting_id must be a non-empty string")

    claims = payload.get("claims")
    if not isinstance(claims, list):
        errors.append("claims must be an array")
        claims = []

    seen_ids: set[str] = set()
    for index, claim in enumerate(claims):
        prefix = f"claims[{index}]"
        if not isinstance(claim, dict):
            errors.append(f"{prefix} must be an object")
            continue

        claim_id = claim.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            errors.append(f"{prefix}.claim_id must be a non-empty string")
        elif claim_id in seen_ids:
            errors.append(f"duplicate claim_id: {claim_id}")
        else:
            seen_ids.add(claim_id)

        if not isinstance(claim.get("text"), str) or not claim["text"].strip():
            errors.append(f"{prefix}.text must be a non-empty string")

        state = claim.get("state")
        if state not in ALLOWED_STATES:
            errors.append(f"{prefix}.state is invalid: {state!r}")

        source_locator = claim.get("source_locator")
        if state in {"present", "conditional", "conflicting", "platform_signal"}:
            if not isinstance(source_locator, str) or not source_locator.strip():
                errors.append(f"{prefix}.source_locator is required for state {state}")
        elif source_locator is not None and not isinstance(source_locator, str):
            errors.append(f"{prefix}.source_locator must be a string or null")

        if claim.get("source_owner") not in ALLOWED_OWNERS:
            errors.append(f"{prefix}.source_owner is invalid: {claim.get('source_owner')!r}")

        if claim.get("review_status") not in ALLOWED_REVIEW_STATUS:
            errors.append(f"{prefix}.review_status is invalid: {claim.get('review_status')!r}")

        question = claim.get("verification_question")
        if question is not None and (not isinstance(question, str) or not question.strip()):
            errors.append(f"{prefix}.verification_question must be a non-empty string or null")

    if payload.get("external_action_allowed") is not False:
        errors.append("external_action_allowed must be false")

    explicit_coverage = payload.get("review_coverage")
    if explicit_coverage is not None and not isinstance(explicit_coverage, dict):
        errors.append("review_coverage must be an object when provided")
    elif isinstance(explicit_coverage, dict):
        for section, entry in explicit_coverage.items():
            if not isinstance(entry, dict):
                errors.append(f"review_coverage.{section} must be an object")
                continue
            if entry.get("status") not in ALLOWED_COVERAGE_STATUS:
                errors.append(f"review_coverage.{section}.status is invalid: {entry.get('status')!r}")
            claim_ids = entry.get("claim_ids")
            if not isinstance(claim_ids, list) or not all(isinstance(item, str) and item.strip() for item in claim_ids):
                errors.append(f"review_coverage.{section}.claim_ids must be an array of non-empty strings")

    questions = payload.get("decision_changing_questions")
    if not isinstance(questions, list) or not all(isinstance(item, str) and item.strip() for item in questions):
        errors.append("decision_changing_questions must be an array of non-empty strings")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python claim_review_harness.py <json-file>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [f"cannot read JSON: {exc}"]}, indent=2))
        return 1

    errors = validate(payload)
    result = {
        "valid": not errors,
        "posting_id": payload.get("posting_id"),
        "claim_count": len(payload.get("claims", [])) if isinstance(payload.get("claims"), list) else 0,
        "errors": errors,
        "completeness": assess_completeness(payload),
        "next_step": (
            "human provenance review required; completeness gaps must be reviewed"
            if not errors
            else "reject output and request correction"
        ),
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
