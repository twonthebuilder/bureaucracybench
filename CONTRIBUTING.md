# Contributing

Read AGENTS.md and docs/roadmap.md. Pick one small implementation milestone.
Keep upstream observations separate from benchmark adaptations and raw generation separate
from evaluation. Propose rubric changes before seeing which model wins.

Run `python -m unittest discover -s tests -v` and `python scripts/validate_foundation.py`.
Paid/live inference is opt-in. Include test evidence, provenance, scope limits and applicable
schema/version changes in a pull request. Never include keys or real government/user data.

New cases, providers and evaluators must meet the definitions of done in AGENTS.md.
