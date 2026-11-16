# AgentShelf QA (branch `qa`, not part of the published plugin)

- `scenarios.md` — 10 scenarios and 5 embedded-instruction cases with expected statuses, evidence and outcomes.
- `fixtures/*.json` — check-level inputs and expected scores for the 10 scenarios.
- `score.py` — reference implementation of `skills/agent-commerce-audit/references/scoring.md`.
- `validate.py` — manifest, frontmatter, version, JSON example, wording and scoring checks.

Run from a checkout of `main`: `python3 qa/validate.py .` (needs Python 3 and PyYAML). Then `claude plugin validate .`.
