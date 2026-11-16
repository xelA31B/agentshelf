# ChatGPT Wallet readiness — reference

Launched by OpenAI on 13 November 2026 with American Express, Mastercard and Visa; first available through the dots agent for ChatGPT Pro subscribers in the US. Agents buy on the merchant's own site, through the existing checkout; the card network supplies a one-time payment number instead of the customer's real card number. The merchant's payment and refund flows stay the same.

Status, availability, countries and requirements change. Before every audit, verify on OpenAI's official pages (the "Introducing ChatGPT Wallet" announcement and the developer guides: Commerce Partner Playbook, agent access, accept payments, product feeds, Business Hub) and cite them with the retrieval date. If an official page cannot be opened, use web search and mark the item **not checked** rather than relying on this file.

## What the merchant needs (as last known)

| Area | Requirement | How to check from outside | Status if unknown |
|---|---|---|---|
| Agent access | Bot protection must not block ChatGPT's cloud browser. OpenAI signs agent requests with Web Bot Auth (HTTP Message Signatures, RFC 9421) from chatgpt.com. Akamai, Cloudflare, HUMAN and Vercel verify these signatures automatically; others must verify them before adding an exception. Agent visits are separate from crawlers such as OAI-SearchBot. | Identify the CDN / bot-management provider from public response headers (e.g. `server`, `cf-ray`, `x-vercel-id`, Akamai headers). Note whether it is one that verifies signed agents automatically. A signed request cannot be simulated; say so. | Partial / not checked |
| Checkout form | The standard card form can be completed without steps an agent cannot pass (CAPTCHA, forced account creation, app-only payment, non-standard widgets). | Observe the path up to the payment step without submitting; note CAPTCHA, login walls, iframes without labels. | Not checked beyond the last observable step |
| Card acceptance | Card payments accepted (credit cards from the supported networks). Wallet sits alongside existing card-on-file flows. | Payment logos and methods on the site or in the checkout. | Partial |
| Subscriptions | Recurring charges need the customer's consent and the processor's merchant-initiated transaction practice. | Policy pages; ask the user. | Ask |
| Fraud rules | Risk systems should recognise legitimate agent purchases and read the `Forwarded` header OpenAI is rolling out (asn, for, ip-country, ip-prefix, locale, tz, user-agent). Named partners: Forter, Riskified, Sardine, Signifyd; payment providers Adyen, Checkout.com, Stripe. | Cannot be checked from outside. Ask the user which payment provider and fraud tool they use. | Ask |
| Product feed and Business Hub | Optional for Wallet (the browser works without a feed) but helps discovery: claim the business, verify identity, choose countries and currencies, format the feed to OpenAI's schema with stable item IDs, deliver by upload, HTTPS URL or SFTP; verify the Business Profile. The schema currently targets the US. | Ask whether the business is claimed; check that product IDs on the site are stable. | Ask |

## Verdict for the report

- **Ready** — no blocking bot wall observed, checkout reachable without agent-blocking steps, cards accepted, provider verifies signed agents (or an exception is configured), fraud tool confirmed.
- **Likely ready, unconfirmed** — nothing blocking observed, but fraud rules or bot settings not confirmed.
- **Not ready** — CAPTCHA or login wall before payment, app-only payment, or bot protection that blocks agents.

Always add: a real Wallet purchase can only be confirmed by an authorised test order on the live site; an outside audit cannot prove it. Wallet is US-only at launch — for other markets, report it as preparation, not as a current sales channel.
