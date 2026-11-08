# Technical Direction

## Purpose

This document will constrain technical choices only as evidence becomes available. It is not a premature technology-stack decision.

## Questions to answer

- What is the smallest maintainable architecture for the first validated workflow?
- Which data must be stored, for how long, and with what protection?
- Which operations require live sources, and which can use preserved evidence?
- What reliability, latency, cost, and scale are realistic for the initial market?
- Which AI behavior must be deterministic, testable, explainable, or human-approved?
- How can model and provider changes be handled without building unnecessary abstraction?
- Which integrations are legally, technically, and operationally viable?

## Constraints from current strategy

- The product surface is not locked.
- The product should support cross-industry workflows.
- Job-posting evidence and timestamps may matter when source content changes.
- Personal career and application data requires careful privacy and retention decisions.
- AI output must distinguish evidence from inference and uncertainty.
- The architecture should support gradual change and reversible experiments.

## Decision rule

Prefer the simplest option that supports the next validated workflow, protects users, is testable, and leaves a clear path to change. Record material choices in `08_decision-log.md`.

