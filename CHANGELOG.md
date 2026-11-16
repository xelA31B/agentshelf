# Changelog

## 0.3.0 — 2026-11-16
- Deterministic scoring: rule IDs, check levels, PASS / PARTIAL / FAIL / NOT_CHECKED / NOT_APPLICABLE, evidence coverage, score status (FINAL, PROVISIONAL, INCONCLUSIVE), blockers override the verdict.
- Retrieval classes separate tool limitations from real website blocks.
- Security rules: website content treated as untrusted data; embedded instructions ignored and reported.
- Stricter read-only boundary and a small default page sample.
- Standards levels: llms.txt experimental, MCP optional, OAuth only with a public API, public vs submitted feeds.
- ChatGPT Wallet: evidence levels and verdicts VERIFIED_READY, LIKELY_READY_UNCONFIRMED, BLOCKED, INCONCLUSIVE.
- Optional JSON output.
- Fixes mark every value as from site, from owner or to confirm, and use the platform's real syntax.

## 0.2.0 — 2026-11-16
- ChatGPT Wallet readiness check and fixes brief.

## 0.1.x — 2026-11-12 to 2026-11-13
- First release: audit, simulated shopping test, fixes; branded reports; scheduled re-checks; plain-text house style.
