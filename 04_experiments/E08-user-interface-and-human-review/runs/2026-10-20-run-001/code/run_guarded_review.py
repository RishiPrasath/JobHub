"""Run the guarded single-posting review against the local Groq configuration.

This runner loads the local root .env without printing secrets, preserves the
raw model response, and writes a parsed JSON copy only when the response is
valid JSON. It does not perform any external action beyond the model request.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI


RUN_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = RUN_DIR.parents[3]
PROMPT_PATH = RUN_DIR / "prompts" / "guarded-role-review.md"
INPUT_PATH = RUN_DIR / "fixtures" / "sample-review-input.json"
RAW_OUTPUT_PATH = RUN_DIR / "raw-model-output.txt"
JSON_OUTPUT_PATH = RUN_DIR / "model-output.json"
METADATA_PATH = RUN_DIR / "model-run-metadata.json"


def load_local_env(path: Path) -> None:
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        os.environ.setdefault(name.strip(), value.strip())


def extract_json(text: str) -> dict:
    candidate = text.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", candidate, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        candidate = fenced.group(1).strip()
    value = json.loads(candidate)
    if not isinstance(value, dict):
        raise ValueError("model JSON must be an object")
    return value


def main() -> int:
    load_local_env(REPO_ROOT / ".env")
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured in the local .env")

    model = os.environ.get("GROQ_MODEL") or "openai/gpt-oss-120b"
    base_url = os.environ.get("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
    timeout = float(os.environ.get("GROQ_TIMEOUT_SECONDS", "60"))
    max_tokens = int(os.environ.get("GROQ_MAX_TOKENS", "4096"))

    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")
    input_payload = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    user_prompt = (
        "Review exactly this one posting input. Return only the required JSON object.\n\n"
        + json.dumps(input_payload, ensure_ascii=False, indent=2)
    )

    client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    content = response.choices[0].message.content or ""
    RAW_OUTPUT_PATH.write_text(content, encoding="utf-8")

    parsed = None
    parse_error = None
    try:
        parsed = extract_json(content)
    except (json.JSONDecodeError, ValueError) as exc:
        parse_error = str(exc)
    if parsed is not None:
        JSON_OUTPUT_PATH.write_text(json.dumps(parsed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    usage = getattr(response, "usage", None)
    metadata = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "provider_base_url": base_url,
        "model": model,
        "posting_id": input_payload.get("posting_id"),
        "max_tokens": max_tokens,
        "raw_output_path": str(RAW_OUTPUT_PATH.relative_to(REPO_ROOT)),
        "parsed_json_path": str(JSON_OUTPUT_PATH.relative_to(REPO_ROOT)) if parsed is not None else None,
        "json_parse_error": parse_error,
        "usage": usage.model_dump() if usage is not None else None,
    }
    METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "model": model,
        "posting_id": input_payload.get("posting_id"),
        "raw_output_saved": RAW_OUTPUT_PATH.exists(),
        "json_output_saved": parsed is not None,
        "json_parse_error": parse_error,
        "metadata_saved": METADATA_PATH.exists(),
    }, indent=2))
    return 0 if parsed is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
