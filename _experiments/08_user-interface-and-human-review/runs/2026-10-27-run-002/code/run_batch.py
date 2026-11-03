"""Run the completeness-required role review once per fixture."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI


RUN_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = RUN_DIR.parents[3]
PROMPT_PATH = RUN_DIR / "prompts" / "guarded-role-review-v2.md"
FIXTURE_DIR = RUN_DIR / "fixtures"
OUTPUT_DIR = RUN_DIR / "outputs"


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


def run_one(client: OpenAI, model: str, max_tokens: int, system_prompt: str, fixture_path: Path) -> dict:
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    posting_id = payload["posting_id"]
    output_dir = OUTPUT_DIR / posting_id
    output_dir.mkdir(parents=True, exist_ok=True)

    user_prompt = (
        "Review exactly this one posting input. Return only the required JSON object.\n\n"
        + json.dumps(payload, ensure_ascii=False, indent=2)
    )
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    content = response.choices[0].message.content or ""
    (output_dir / "raw-output.txt").write_text(content, encoding="utf-8")

    parsed = None
    parse_error = None
    try:
        parsed = extract_json(content)
    except (json.JSONDecodeError, ValueError) as exc:
        parse_error = str(exc)
    if parsed is not None:
        (output_dir / "model-output.json").write_text(json.dumps(parsed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    usage = getattr(response, "usage", None)
    metadata = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "provider_base_url": os.environ.get("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
        "model": model,
        "posting_id": posting_id,
        "fixture": str(fixture_path.relative_to(REPO_ROOT)),
        "prompt": str(PROMPT_PATH.relative_to(REPO_ROOT)),
        "max_tokens": max_tokens,
        "json_parse_error": parse_error,
        "usage": usage.model_dump() if usage is not None else None,
    }
    (output_dir / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "posting_id": posting_id,
        "json_output_saved": parsed is not None,
        "json_parse_error": parse_error,
        "output_dir": str(output_dir.relative_to(REPO_ROOT)),
    }


def main() -> int:
    load_local_env(REPO_ROOT / ".env")
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured in the local .env")

    model = os.environ.get("GROQ_MODEL") or "openai/gpt-oss-120b"
    timeout = float(os.environ.get("GROQ_TIMEOUT_SECONDS", "60"))
    max_tokens = int(os.environ.get("GROQ_MAX_TOKENS", "4096"))
    client = OpenAI(
        api_key=api_key,
        base_url=os.environ.get("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
        timeout=timeout,
    )
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    requested_ids = set(sys.argv[1:])
    fixture_paths = sorted(FIXTURE_DIR.glob("r4-jb-*-input.json"))
    if requested_ids:
        fixture_paths = [path for path in fixture_paths if path.stem.removesuffix("-input").upper() in {item.upper() for item in requested_ids}]
    results = []
    for fixture_path in fixture_paths:
        results.append(run_one(client, model, max_tokens, system_prompt, fixture_path))

    print(json.dumps({"model": model, "results": results}, indent=2))
    return 0 if all(item["json_output_saved"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
