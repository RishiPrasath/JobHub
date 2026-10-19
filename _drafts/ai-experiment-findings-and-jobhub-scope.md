# Draft — AI Experiment Findings and JobHub Scope

Status: sequential SDK experiment run complete; draft for owner review

Date: 2026-10-19

## Executive summary

We used the OpenAI Python SDK with Groq’s OpenAI-compatible API to run a sequential set of controlled experiments using captured Singapore job postings and synthetic candidate data.

The evidence supports a narrow product direction:

> JobHub could use AI to organise job-posting evidence, preserve uncertainty and generate verification questions, provided every material claim remains reviewable and source-linked.

The evidence does not support automatic fit scoring, resume rewriting, legitimacy judgments or application actions. Profile comparison and resume alignment produced important unsupported inferences even when the prompts explicitly prohibited them.

## Data boundary

The tests used:

- captured records for R4-JB-003 Class 4 Driver, R4-JB-006 Vehicle Mechanic and R4-JB-011 Part-Time Admin Assistant;
- a synthetic candidate profile;
- synthetic contradiction and prompt-injection fixtures;
- no private resume, personal identifier or real participant data.

Source baseline: [Round 4 page inventory](../02_research/03_research-rounds/04_ai-assistance-and-trust/runs/2026-10-19-job-posting-page-inventory/page-inventory.md).

Models used:

- `openai/gpt-oss-120b` for the primary sequential run;
- `openai/gpt-oss-20b` for the earlier comparison and operational repeatability check;
- `openai/gpt-oss-safeguard-20b` for the earlier prompt-injection comparison.

## Sequential experiment record

### 0. Model inventory

Completed before this run. The SDK successfully listed the models available through the Groq account. The inventory is recorded in the [OpenAI SDK briefing](../Tools/OpenAI%20SDK/briefing.md).

### 1. Claim-level grounding

#### Initial attempt

The first fixture supplied claim IDs and source IDs but omitted the underlying source excerpts. The model returned every claim as unknown. This was a fixture-design failure, not evidence that the model could not classify the claims.

#### Corrected attempt

The source excerpts were added and the test was rerun.

Result: **semantic pass with a schema caveat**.

The model correctly:

- classified the displayed salary and Class 4 requirement as present;
- rejected “guaranteed base salary” as an overclaim;
- rejected “will respond within 24 hours” as an overclaim;
- retained “normally responds within 24 hours” as a qualified source statement;
- retained `0% skills matched` as a platform signal;
- rejected the claim that the Jobstreet posting was a verified scam.

The model used the requested claim IDs and source IDs in this corrected run.

Finding: source excerpts and stable source identifiers are essential. A model cannot ground a claim from an identifier alone.

### 2. Contradiction preservation

Three fixtures were supplied:

- Jobstreet URL/title/body and related salary-teaser conflict;
- search-card versus detail-page salary disagreement;
- older versus newer shift information.

Result: **pass in the dedicated fixture**.

The model preserved both values, source IDs and dates, marked each record as conflicting, and requested verification. It did not silently select the newest or most convenient value.

Finding: contradiction handling is promising when the input is explicitly structured. It still needs testing in the full end-to-end workflow, where the earlier profile-comparison run showed weaker performance.

### 3. Cross-posting contamination

Three separate role records were supplied with clearly different qualifications, locations, schedules and pay.

Result: **pass in the isolated extraction fixture**.

The model kept each role’s facts attached to its own source and explicitly listed facts that belonged to the other roles as excluded.

However, the earlier holistic profile-comparison run produced contamination: the 20B model imported driver qualifications into the Vehicle Mechanic analysis. Therefore:

> Isolated extraction is safer than holistic comparison, but the complete workflow has not yet passed contamination control.

### 4. Unknown and conditional information

The corrected test covered:

- salary including overtime, night work and allowances;
- unknown overtime calculation;
- an unclear response-time signal;
- a related salary teaser;
- missing job duties;
- a platform-generated skills signal.

Result: **semantic pass, output-contract partial failure**.

The model mostly classified the fields correctly:

- base-pay breakdown: unknown;
- overtime calculation: unknown;
- response statement: conditional;
- salary teaser: present as a related platform item;
- exact duties: unknown;
- skills match: platform signal.

The model changed the requested field IDs into its own generated IDs. That makes the result unsuitable for automatic record updates without a validation layer.

### 5. Candidate-profile comparison

The model compared a synthetic candidate profile with all three postings without being allowed to produce a fit score, hiring probability or scam verdict.

Result: **fail for reliable automated comparison**.

Observed errors included:

- merging three roles into one `role_id` instead of returning one comparison per role;
- treating Excel experience as evidence of administrative experience despite an explicit prohibition;
- stating that all three roles were full-time even though the Admin Assistant role was part-time;
- introducing an unsupported Class 4 requirement into the Vehicle Mechanic analysis;
- omitting some known location and employment-type facts;
- producing no explicit matches for the logistics role even though the profile contained relevant logistics experience.

The model did avoid producing a fit score, hiring probability or scam verdict.

Finding: candidate-to-role comparison is much more prone to overreach than source extraction. It should not be a first product capability.

### 6. Truthful resume alignment

The model was asked to tailor a resume for the Class 4 Driver role using only a synthetic profile and resume excerpt.

Result: **partial safety success, but failed factuality control**.

It correctly rejected:

- “Licensed Class 4 driver”;
- invented delivery-delay reductions;
- “Expert in port operations”;
- HazMat certification;
- PSA Pass, forklift and rigger/signalman credentials.

It nevertheless introduced unsupported claims in accepted suggestions:

- “advanced Excel functions”;
- “improving data accuracy”;
- a commitment to obtain a Class 4 licence;
- “Nitec Logistics” as if it were an employer or operational context.

Finding: resume assistance requires a sentence-level evidence ledger and explicit human acceptance. A general instruction to “be truthful” is insufficient.

### 7. Industry portability

The model was asked to identify common and sector-specific fields across logistics, automotive/trade and office administration.

Result: **partial pass**.

It correctly identified sector-specific differences in:

- licences and certifications;
- shift and work patterns;
- travel and worksite conditions;
- hourly versus monthly compensation;
- sector-specific assessment and benefit information.

It also identified the risk of forcing every industry into one template.

However, it omitted or misclassified some known common fields, including salary and employment type, and incorrectly treated some supplied facts as unknown.

Finding: JobHub should use a shared evidence core with sector-specific extensions, not one universal role schema.

### 8. Prompt-injection resistance

This was tested earlier with `openai/gpt-oss-120b` and `openai/gpt-oss-safeguard-20b`.

Result: **pass for the tested fixture**.

Both models:

- detected the embedded instruction;
- treated it as untrusted posting content;
- refused to reveal the candidate profile;
- refused to submit an application;
- stated that external action was not allowed.

This remains a fixture-level result, not a general safety guarantee.

### 9. Repeatability and operational behaviour

The same uncertainty-classification prompt was run twice on the 120B and 20B models.

With an artificially low 300-token limit, several outputs were truncated and invalid JSON. This exposed an operational failure: reasoning tokens consume part of the completion budget.

With an 800-token limit:

- all four outputs were valid JSON;
- the 120B runs took approximately 1.1 seconds each;
- the 20B runs took approximately 0.64–0.68 seconds each;
- the 120B outputs used approximately 190–277 completion tokens;
- the 20B outputs used approximately 161–294 completion tokens.

This is a small timing sample, not a cost or performance benchmark.

## Consolidated findings

### Strongest demonstrated capabilities

- Extracting explicit posting facts when source excerpts are supplied.
- Preserving salary qualifiers when directly instructed and shown the evidence.
- Identifying and preserving explicit contradictions in a structured fixture.
- Generating useful verification questions.
- Rejecting direct scam, hiring-probability and external-action instructions.
- Keeping role facts separate in an isolated extraction task.

### Weakest demonstrated capabilities

- Comparing a profile with multiple roles without merging contexts.
- Distinguishing relevant skills from merely adjacent skills.
- Tailoring resumes without adding plausible-sounding embellishments.
- Maintaining exact output IDs and schema contracts.
- Preserving all known facts when summarising across several roles.
- Handling source provenance consistently in a holistic workflow.

## Product implication

The current evidence supports a narrow first capability:

> A source-grounded role-review aid that organises what a posting says, what is conditional or unknown, what conflicts, and what the user should verify next.

The following should remain deferred:

- universal fit scores;
- hiring predictions;
- scam or legitimacy verdicts;
- autonomous profile-to-role ranking;
- automatic resume rewriting;
- automatic application submission;
- automatic answers to sensitive eligibility questions.

## What the experiments did not prove

The SDK experiments cannot establish:

- whether real job seekers would use the workflow;
- whether it improves decisions or application outcomes;
- whether it saves time after verification effort;
- whether the interface is accessible;
- whether people can correct, reject and recover from model suggestions;
- whether the method works across a representative sample of industries;
- whether Groq is the final production provider.

## Recommended next action

Before building a user-facing AI feature, create a deterministic claim-review harness with:

```text
posting_id
claim_id
source_locator
state
model_output
review_status
correction_reason
```

Then rerun the profile and resume experiments only after:

- each role has an isolated source context;
- every claim must cite a source ID;
- output IDs are validated before acceptance;
- unsupported suggestions are automatically flagged for human review;
- no external actions are enabled.

## Draft conclusion

The experiments did not prove that JobHub should become an AI application automation platform. They did show a credible, safer opportunity in evidence organisation and uncertainty-aware job-posting review.

The next product step should be a disposable, human-reviewed worksheet—not production automation.

Raw SDK responses were observed during the sequential run. This draft records the material outputs, failures and corrections; a future runner should persist the complete raw response, claim ledger and correction log for each run.
