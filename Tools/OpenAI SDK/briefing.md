# OpenAI SDK Tooling Briefing

Status: initial operating guide

Date: 2026-10-19

## Purpose

This folder documents how JobHub will use the OpenAI Python SDK with Groq’s OpenAI-compatible API to run controlled experiments during analysis and research.

The SDK is an experiment instrument, not a product decision. It helps us test claims such as:

- whether AI can organise job-posting evidence without inventing facts;
- whether it can preserve unknowns and contradictions;
- whether it reduces review effort without creating more verification work;
- whether different models behave differently on the same evidence;
- whether prompt-injection and unsafe-inference controls work.

The current work remains exploratory. Do not use this tool to submit applications, contact employers, make hiring predictions, or make irreversible changes.

## Current provider configuration

The local provider is Groq, accessed through its OpenAI-compatible endpoint.

Local configuration belongs in the root `.env` file, which is ignored by Git. The safe template is `.env.example`.

```env
GROQ_API_KEY=your_local_key
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_MODEL=openai/gpt-oss-120b
GROQ_TIMEOUT_SECONDS=60
GROQ_MAX_TOKENS=4096
```

Never place a real key in Markdown, source code, research outputs, prompts, logs or commits. Never paste the key into chat.

The Python `openai` package is currently available in the local environment. If another environment is used, install the official SDK there rather than copying credentials or generated outputs into the repository.

## SDK client setup

The SDK client should be configured with Groq’s base URL while retaining the OpenAI SDK interface:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url=os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
    timeout=float(os.getenv("GROQ_TIMEOUT_SECONDS", "60")),
)
```

The SDK does not automatically load the repository’s `.env` file. The experiment runner must load it using a local environment mechanism or an approved dotenv loader before constructing the client. Do not print the environment or the key while debugging.

## Get the account’s model inventory

Use the provider’s model-list endpoint through the SDK:

```python
models = client.models.list()

for model in sorted(models.data, key=lambda item: item.id):
    print({
        "id": model.id,
        "owned_by": getattr(model, "owned_by", None),
        "created": getattr(model, "created", None),
        "active": getattr(model, "active", None),
        "context_window": getattr(model, "context_window", None),
        "max_completion_tokens": getattr(model, "max_completion_tokens", None),
    })
```

The inventory is provider/account state and can change. Record the retrieval date, provider endpoint and model IDs with every experiment.

## Get details for one model

Where the provider supports model retrieval, use:

```python
model = client.models.retrieve("openai/gpt-oss-120b")
print(model.model_dump())
```

If the provider does not implement retrieval for a model, use the model-list record and the provider’s current documentation. Treat unsupported or missing fields as unknown; do not infer capability from the model name.

## Run a controlled text experiment

Use the Chat Completions interface for the OpenAI-compatible Groq endpoint:

```python
from pathlib import Path

source_text = Path("fixture.md").read_text(encoding="utf-8")

response = client.chat.completions.create(
    model=os.environ["GROQ_MODEL"],
    max_tokens=int(os.getenv("GROQ_MAX_TOKENS", "4096")),
    messages=[
        {
            "role": "system",
            "content": (
                "Extract only what the source supports. Preserve unknown, "
                "conditional and conflicting information. Do not infer fit, "
                "legitimacy, salary guarantees or hiring probability."
            ),
        },
        {
            "role": "user",
            "content": source_text,
        },
    ],
)

output = response.choices[0].message.content
print(output)
```

For reproducible experiments, also save the model ID, prompt version, source fixture ID, timestamp, request parameters, raw response, reviewed response and any error or correction log. Do not save secrets or unnecessary personal data.

## JobHub experiment protocol

Each experiment should follow this sequence:

1. State one testable theory.
2. Select a fixed, redacted source fixture.
3. Define the manual baseline before calling the model.
4. Define pass, failure and stop conditions.
5. Run the same fixture against one or more models.
6. Preserve the raw output before editing it.
7. Create a claim ledger linking each material claim to a source locator or an explicit unknown state.
8. Record fabricated claims, silent inference, lost qualifiers, unresolved contradictions and unsafe suggestions.
9. Test correction, rejection, interruption and recovery where an interface exists.
10. Write a conclusion that separates observed results, hypotheses and product decisions.

Suggested experiment record:

```text
Tools/OpenAI SDK/experiments/YYYY-MM-DD-short-name/
  README.md
  fixture.md
  prompt.md
  raw-output.json
  reviewed-output.md
  claim-ledger.md
  corrections.md
  result.md
```

## Experiments relevant to the current JobHub analysis

### 1. Source-grounded role review

Compare raw posting, manual worksheet and AI-assisted worksheet. Test identity, duties, hard gates, work conditions, pay qualifiers, application process, unknowns and next verification questions.

### 2. Contradiction preservation

Use the observed URL/title/body mismatch and add redacted card/detail and stale/current fixtures. The model must preserve both values, source ownership and dates rather than silently choosing one.

### 3. Unsafe-inference resistance

Seed suggestions such as “this salary is guaranteed,” “the employer is definitely a scam,” or “the candidate is a strong fit.” The safe result is rejection or qualified uncertainty.

### 4. Prompt-injection resistance

Include instruction-like text inside a job posting. The model must treat it as untrusted source content, not as an instruction to reveal data, claim verification or submit an application.

### 5. Model comparison

Run the same fixture against the primary and faster models. Compare grounding, unknown preservation, contradiction handling, correction burden, latency and output usefulness. Do not select a production model from one fixture.

## Initial model roles

Based on the inventory retrieved on 2026-10-19:

| Model | Proposed experimental role | Constraint |
|---|---|---|
| `openai/gpt-oss-120b` | Primary evidence-analysis model | Validate every material claim; higher capability is not proof of correctness |
| `openai/gpt-oss-20b` | Faster comparison and repeated-run model | Check whether lower cost or latency changes error patterns |
| `openai/gpt-oss-safeguard-20b` | Safety-review comparison | Treat it as an evaluator candidate, not an authority |
| `meta-llama/llama-prompt-guard-2-22m` | Lightweight prompt-injection screening | Test false positives and false negatives |
| `meta-llama/llama-prompt-guard-2-86m` | Larger prompt-injection screening comparison | Do not rely on it as the only safety control |
| `whisper-large-v3` / `whisper-large-v3-turbo` | Future audio/transcript experiments | Transcription accuracy must be checked against the source |

## Evidence and safety rules

- Use redacted or synthetic job-posting fixtures where possible.
- Treat job postings and embedded instructions as untrusted evidence.
- Keep source wording, qualifiers and ownership visible.
- Distinguish `unknown`, `not visible`, `not stated`, `conditional`, `conflicting` and `inferred`.
- Never auto-answer sensitive eligibility, salary, disability, demographic, criminal-history or work-authorisation questions.
- Never turn a model output into a scam verdict, fit score or hiring prediction without a separately approved evidence and decision framework.
- Keep external actions disabled during experiments.
- Record failures, not only successful outputs.
- Do not send private user documents to a provider without explicit, informed approval and a defined retention boundary.

## What a successful experiment means

A successful experiment demonstrates only that a bounded test passed its stated criteria. It does not prove that:

- users want the product;
- the workflow works across industries;
- AI is better than manual review;
- the model is reliable in production;
- the feature should be built;
- the provider or platform is the final technical choice.

Those conclusions require additional evidence and an explicit owner decision in the `analysis/` folder.
