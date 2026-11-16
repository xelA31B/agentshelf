# Structured result (JSON) — v1.0

Produce it when the user asks for JSON or machine-readable output, alongside or instead of the human report. When raw JSON is requested, output only the JSON object, without Markdown fences or text around it. The human-readable report and the branded HTML report stay the default.

## Top level

| Field | Type | Notes |
|---|---|---|
| schema_version | string | "1.0" |
| plugin_version | string | "0.3.0" |
| target_url | string | Audited site |
| audit_date | string | ISO date |
| sample | array of strings | URLs retrieved |
| overall_score | number or null | null when score_status is INCONCLUSIVE |
| score_status | string | FINAL, PROVISIONAL or INCONCLUSIVE |
| evidence_coverage | number | 0–100 |
| purchase_capability | string | NO, PARTLY or NOT_VERIFIED |
| categories | array | id, name, weight, score (number or null), coverage, applicable (boolean) |
| findings | array | See below |
| wallet_readiness | object | status (VERIFIED_READY, LIKELY_READY_UNCONFIRMED, BLOCKED, INCONCLUSIVE), market_note, evidence (array of finding IDs) |
| limitations | array of strings | Tool limits, sample limits, unverifiable items |
| recommendations | array | rank, rule_id, action, effort (S, M, L) |

## Finding

| Field | Type | Values |
|---|---|---|
| rule_id | string | From `standards-checklist.md`, e.g. PRD-02; SEC-01 for embedded instructions |
| category | string | access, product_data, policies, feeds, action_path, apis, wallet, security |
| check | string | Short description |
| standard | string | Source and level, e.g. "schema.org Offer · REQUIRED" |
| status | string | PASS, PARTIAL, FAIL, NOT_CHECKED, NOT_APPLICABLE |
| retrieval | string | ACCESSIBLE, ACCESS_BLOCKED, PAGE_NOT_FOUND, TOOL_LIMITATION, TIMEOUT_UNCONFIRMED, NETWORK_ERROR, CAPTCHA_DETECTED, NOT_CHECKED |
| evidence_url | string or null | |
| observed | string or null | One line at most |
| expected | string or null | |
| confidence | string | OBSERVED, MERCHANT_CONFIRMED, DOCUMENTED, INFERRED, NOT_VERIFIED |
| severity | string | critical, high, medium, low, info |
| fix | string or null | |
| verification | string | How to confirm the fix |
| reason | string or null | Required for NOT_APPLICABLE and NOT_CHECKED |

## Example

```json
{
  "schema_version": "1.0",
  "plugin_version": "0.3.0",
  "target_url": "https://shop.example.com",
  "audit_date": "2026-11-16",
  "sample": ["https://shop.example.com/", "https://shop.example.com/products/blue-mug"],
  "overall_score": null,
  "score_status": "INCONCLUSIVE",
  "evidence_coverage": 42,
  "purchase_capability": "NOT_VERIFIED",
  "categories": [
    {"id": "product_data", "name": "Product data", "weight": 25, "score": 7.5, "coverage": 100, "applicable": true},
    {"id": "apis", "name": "APIs and protocols", "weight": 5, "score": null, "coverage": 0, "applicable": false}
  ],
  "findings": [
    {
      "rule_id": "PRD-07",
      "category": "product_data",
      "check": "Structured data equals visible page",
      "standard": "schema.org Offer · REQUIRED",
      "status": "FAIL",
      "retrieval": "ACCESSIBLE",
      "evidence_url": "https://shop.example.com/products/blue-mug",
      "observed": "JSON-LD price 12.00 EUR; page shows 14.00 EUR",
      "expected": "Equal price and currency",
      "confidence": "OBSERVED",
      "severity": "critical",
      "fix": "Generate offers.price from the same field the page displays",
      "verification": "Re-fetch the page and compare markup with the visible price",
      "reason": null
    }
  ],
  "wallet_readiness": {"status": "INCONCLUSIVE", "market_note": "Wallet availability verified on OpenAI pages at audit time", "evidence": ["WAL-01", "WAL-02"]},
  "limitations": ["robots.txt refused by the fetch tool (TOOL_LIMITATION); ACC-01 not checked"],
  "recommendations": [{"rank": 1, "rule_id": "PRD-07", "action": "Fix price mismatch in product markup", "effort": "S"}]
}
```
