# Scoring methodology (v0.3.0)

Deterministic and reproducible: the same evidence always gives the same score. Every number in a report must be traceable to individual checks in `standards-checklist.md`.

## 1. Check statuses

| Status | Meaning | Points | In denominator |
|---|---|---|---|
| PASS | Requirement met, with evidence | 1 | Yes |
| PARTIAL | Met in part (e.g. some sampled pages, some required properties) | 0.5 | Yes |
| FAIL | Verified not met, with evidence | 0 | Yes |
| NOT_CHECKED | No reliable evidence (tool limitation, timeout, not asked, not visible) | 0 | Yes |
| NOT_APPLICABLE | Genuinely does not apply to this site (e.g. OAuth when there is no API) | — | No |

Rules:
- Missing evidence is never PASS. A website's own claim of compliance is not evidence.
- NOT_CHECKED stays in the denominator, so an unknown can never raise a score. The score is therefore a conservative, verified-evidence score.
- NOT_APPLICABLE needs a one-line reason in the report. Never use it for a check that failed or could not be reached.
- PARTIAL across sampled pages: PASS if all sampled pages pass, PARTIAL if at least one but not all pass, FAIL if none pass.

## 2. Check weights by level

| Level | Weight | Effect |
|---|---|---|
| REQUIRED | 2 | Counts fully |
| RECOMMENDED | 1 | Counts |
| OPTIONAL | 0 | Reported, no effect on the score |
| EXPERIMENTAL | 0 | Reported, no effect on the score |

## 3. Category and overall score

Category score (0–10):

    category_score = 10 × Σ(weight × points) / Σ(weight)        over applicable checks with weight > 0

A category with no applicable weighted checks is excluded and its weight removed from the overall denominator (state this).

Category weights: Agent access 15 · Product data 25 · Policies 15 · Feeds 10 · Action path 15 · APIs and protocols 5 · ChatGPT Wallet 15.

Overall score (0–100):

    overall = 100 × Σ(category_weight × category_score / 10) / Σ(applicable category_weight)

## 4. Evidence coverage

    coverage = 100 × Σ(weight of checks with PASS, PARTIAL or FAIL) / Σ(weight of applicable checks)

Report coverage with every score.

| Coverage | Critical checks unknown? | score_status | What to show |
|---|---|---|---|
| ≥ 80 % | none | FINAL | Score |
| ≥ 80 % | one or more | PROVISIONAL | Score, labelled provisional |
| 50–79 % | any | PROVISIONAL | Score, labelled provisional |
| < 50 % | any | INCONCLUSIVE | No overall score (null); category results only |

Critical checks are marked **critical** in `standards-checklist.md`.

## 5. Blockers and purchase capability

The score measures readiness signals, not proven purchase capability. Answer "Can an agent complete a purchase today?" separately:

- **No** — any verified blocker: ACCESS_BLOCKED on catalogue or product pages, CAPTCHA_DETECTED before the payment step, login required before price, app-only payment.
- **Partly** — no verified blocker, but the path to payment could not be observed fully.
- **Not verified** — never "Yes" from a read-only audit; a completed purchase is proven only by an authorised test order.

A blocker overrides any score in the verdict line.

## 6. Rounding

Compute with full precision; round only for display. Category scores to one decimal, overall score and coverage to whole numbers, half up (7.25 → 7.3; 64.5 → 65).

## 7. Worked example

Agent access, applicable weighted checks: ACC-01 robots rules (REQUIRED, 2) PASS; ACC-03 sitemap (RECOMMENDED, 1) FAIL; ACC-04 readable without JavaScript (REQUIRED, 2) NOT_CHECKED; ACC-02 llms.txt (EXPERIMENTAL, 0) FAIL — no effect.

    category_score = 10 × (2×1 + 1×0 + 2×0) / (2 + 1 + 2) = 4.0
    category coverage = 100 × (2 + 1) / 5 = 60 %

If all other categories scored 8.0 (weights 85) and Agent access 4.0 (weight 15):

    overall = 100 × (15×0.40 + 85×0.80) / 100 = 74

With overall coverage of 72 %, the result is **74/100 · PROVISIONAL · coverage 72 %**.
