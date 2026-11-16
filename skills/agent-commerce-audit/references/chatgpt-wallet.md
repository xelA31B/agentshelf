# ChatGPT Wallet readiness — reference (v0.3.0)

## Verify first

Status, availability and requirements change. At the start of every audit, check OpenAI's official pages (the "Introducing ChatGPT Wallet" announcement and the developer guides: Commerce Partner Playbook, agent access, accept payments, product feeds, Business Hub). Cite each time-sensitive statement with its source and retrieval date. If an official page cannot be opened, use web search for it; if that fails, mark dependent items NOT_VERIFIED. Never rely on this file alone.

As last documented (launch 13 November 2026, with American Express, Mastercard and Visa): first available through the dots agent for eligible ChatGPT Pro subscribers in the US; agents buy on the merchant's own site through the existing checkout; the card network supplies a one-time payment number instead of the customer's real card number. Re-check all of this at audit time.

## Evidence levels

| Level | Meaning |
|---|---|
| OBSERVED | Seen directly on the public site in this audit (URL recorded) |
| MERCHANT_CONFIRMED | Stated by the site owner in this conversation |
| DOCUMENTED | Stated in the merchant's or provider's official documentation (URL recorded) |
| INFERRED | Reasoned from indirect signals; never enough for PASS |
| NOT_VERIFIED | No reliable evidence |

## Confirmed requirements vs recommendations

| Item | Type (per OpenAI docs, verify) | Publicly observable signal | Needs merchant confirmation |
|---|---|---|---|
| Signed-agent access (Web Bot Auth, signature agent chatgpt.com) | Requirement for agent access | Bot-protection provider from public response headers (e.g. `server`, `cf-ray`, `x-vercel-id`) — INFERRED only | Whether signed agents are verified or an exception is set |
| No agent-blocking steps before the card form | Requirement | Path up to the last observable step | Steps after it |
| Card payments | Requirement | Payment options shown or documented | Card types and issuing country rules |
| Fraud rules recognise agent purchases; `Forwarded` header read | Recommendation | None | Risk tool and provider configuration |
| Business Hub claim, verified profile, feed with stable IDs | Recommendation for discovery (not needed for browser purchases) | Stable IDs on the site | Claim, profile, feed submission |
| Subscriptions: consent and merchant-initiated practice | Requirement where recurring billing is used | Terms pages | Processor setup |

Do not infer:
- successful signed-agent verification from the CDN or hosting provider;
- correct fraud handling from the payment provider;
- checkout compatibility from card logos;
- payment readiness from anything when the payment step was not tested.

## Market eligibility

Record the countries and customer eligibility stated by OpenAI at audit time. If the merchant sells outside them, report Wallet as preparation, not as a current channel, and exclude the Wallet category from the overall score with that reason.

## Verdicts

| Verdict | When |
|---|---|
| VERIFIED_READY | Only after an authorised, successful end-to-end test purchase reported by the merchant. Never from a read-only audit |
| LIKELY_READY_UNCONFIRMED | No known blocker; WAL-01 and WAL-02 at least MERCHANT_CONFIRMED or OBSERVED; other conditions still unverified |
| BLOCKED | A specific, verified blocker (OBSERVED or MERCHANT_CONFIRMED): CAPTCHA before the card form, login wall, app-only payment, bot protection rejecting agents |
| INCONCLUSIVE | Insufficient evidence for the above |

Always state in the report: an outside, read-only audit cannot confirm a Wallet purchase; only an authorised test order on the live site can.
