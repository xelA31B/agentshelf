---
name: agent-commerce-audit
description: >
  This skill should be used when the user asks "is my store ready for AI shopping agents", "can ChatGPT
  or Claude buy from my site", "agentic commerce audit", "check my product schema for AI", "is my
  e-commerce site agent-friendly", "audit my API for AI agents", or wants an assessment of how well an
  online store, booking site, SaaS website or API can be discovered, understood and used by AI agents.
  Also triggers on the same requests in Russian ("готов ли магазин к ИИ-агентам", "могут ли агенты
  покупать на сайте") or Hungarian.
metadata:
  version: "0.1.0"
---

# Agent Commerce Audit

Assess, against public standards, whether AI agents can find a business's offers, understand them correctly and complete an action (buy, book, sign up) — and list what to fix.

## Style and evidence rules

- Language of the user's request. Concise, professional, no filler. Tables over paragraphs.
- Every finding follows **standard → what was checked → evidence** (URL, field, snippet of at most one line). No evidence, no finding.
- Mark each check **pass / partial / fail / not checked**. Never guess a result you could not verify; say what is needed to verify it.
- Read-only: do not submit forms, create accounts, add to cart or place orders.
- Standards evolve. For agent payment and checkout protocols, verify the current status with web search before reporting and cite the source.

## Step 1 — Scope

Ask only for what is missing: site URL, type (online store, booking, SaaS, marketplace, local service), 2–3 representative product or service pages, target market (country, currency, language), and whether a public API exists.

## Step 2 — Run the checks

Use `references/standards-checklist.md`. Cover six areas:

1. **Access for agents** — robots.txt rules for AI crawlers and user-triggered agents, llms.txt, sitemap with product URLs, content readable without client-side JavaScript.
2. **Product / offer data** — schema.org `Product` and `Offer` JSON-LD on product pages with required properties; consistency between structured data and the visible page (price, currency, availability).
3. **Policies in machine-readable form** — returns (`MerchantReturnPolicy`), shipping (`OfferShippingDetails`), organization and contact data, warranty, terms.
4. **Feeds** — a product feed following a public merchant-feed specification, linked or discoverable.
5. **Action path** — can an agent reach the action: stable product URLs, guest checkout or clear sign-up, no login wall before price, accessible form labels, price and total visible before payment. Observe only; do not submit.
6. **APIs and protocols** — public API documentation (OpenAPI), standard authentication (OAuth 2.0), rate limits documented, an MCP server or other agent integration, support for current agent checkout/payment protocols (verify status by search).

## Step 3 — Score

Score each area 0–10 using the checklist weights; compute the **Agent-Readiness Score (0–100)**. Exclude areas not checked and re-normalize; say so.

## Step 4 — Report

```
# Agent Commerce Audit — [site] · [date]

**Agent-Readiness Score:** X/100 — one-line verdict
**Can an agent complete a purchase today?** Yes / Partly / No — reason

## Scorecard
| Area | Score | Status | Key finding |

## Findings
| # | Standard | Checked | Evidence | Status | Fix | Effort |

## Top 5 fixes
1. … — impact

## Not checked
- item — what is needed
```

Close with one line offering: run a simulated agent shopping task (`agent-shopping-test`) or generate the fixes (`agent-commerce-fixes`).

## Recurring run

At the end of the report, offer a recurring run. Recommended cadence: monthly, and after any change to the product catalogue template, checkout or platform.

Let the user choose their own schedule. Ask in one short message, with the recommendation pre-filled:

- **Frequency:** daily · weekly · every 2 weeks · monthly · quarterly · custom
- **Day:** e.g. Monday, Friday, 1st of the month
- **Time and time zone:** e.g. 09:00 Europe/Budapest (use the user's time zone if known)
- **Delivery:** in this chat, a new chat, or a document

If the environment offers scheduled tasks (a scheduling tool is available), create the task only after the user confirms these choices. Write the scheduled prompt so it is self-contained: what to check, which skill to run, the report language, and where to deliver the result. Confirm what was scheduled in one line. The user can change or cancel the schedule at any time; when asked, update or remove it.

If no scheduling tool is available, state the chosen or recommended cadence and suggest a calendar reminder.
