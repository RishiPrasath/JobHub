# JobHub

Exploratory research for a job-search intelligence and application-preparation product. No product scope, platform or architecture has been finalized.

**Start here: [06_scope/SCOPE.md](06_scope/SCOPE.md)**, the current feature board and the decisions still open.

## How the repo flows

| Stage | Question | Key file |
|---|---|---|
| [01_research](01_research/README.md) | What is out there? | Each round's `round-synthesis.md` |
| [02_analysis](02_analysis/README.md) | What does it mean? | `findings.md`, `needs.md`, `opportunities.md` |
| [03_features](03_features/README.md) | What could we build? | One `FEAT-` file per candidate |
| [04_experiments](04_experiments/README.md) | Does it work? | Each experiment's findings |
| [05_prototypes](05_prototypes/README.md) | What does it look like in use? | Status table in the README |
| [06_scope](06_scope/SCOPE.md) | What are we building? | `SCOPE.md`, `decisions/` |

Experiment results feed back into `02_analysis/findings.md`.

Supporting folders: `strategy/` (principles), `agents/` (role definitions and prompts), `tools/` (validator and path map), `generated/` (validator output), `archive/` (superseded material).

## Working here

Run `python tools/validate.py` after changing features, findings or links. It checks links and evidence gates, then regenerates the board.

Files moved in the 2026 reorganization: see `tools/path-map.csv`. The earlier layout is at git tag `pre-reorg`. Older decks and raw outputs keep their original plain-text paths.
