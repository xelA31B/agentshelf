---
name: agent-shopping-test
description: >
  This skill should be used when the user asks to "test my store like an AI agent", "can an agent find
  and buy my product", "simulate an AI shopping assistant on my site", "agent shopping test", or wants a
  practical, task-based test of whether an AI agent can complete realistic shopping or booking tasks on
  a website. Also triggers on the same requests in Russian ("протестируй магазин как ИИ-агент") or
  Hungarian.
metadata:
  version: "0.1.0"
---

# Agent Shopping Test

Run 5 realistic tasks as an AI shopping agent would, using only what the website exposes, and report where the agent succeeds, fails or gets wrong information.

## Rules

- Language of the user's request. Concise, professional, no filler.
- Read-only: never log in, create accounts, add to cart, submit forms or pay. Stop at the step before any action.
- Use only web search and page fetching; record the exact URLs used. If a page cannot be fetched, the task step fails for agents — record it as a finding, not as a tool problem.
- Compare every answer the agent finds with the visible page; flag mismatches.

## Tasks

Adapt to the business; default set for a store:

1. **Find:** "Find [product type] under [budget] in [country]" — does the site surface in search, and can the agent reach a matching product page?
2. **Understand:** extract name, price, currency, availability, key specs — correct and complete?
3. **Compare:** variants (size/colour) and alternatives on the same site — reachable and described?
4. **Policy:** "What is the delivery time and cost to [city], and can I return it?" — answer found, with source?
5. **Act:** describe the path to purchase up to payment — steps, blockers (login wall, CAPTCHA, JS-only buttons, hidden fees).

For booking or SaaS: find offer → understand price/plan → compare → policy (cancellation/refund) → act (book/trial).

## Report

```
# Agent Shopping Test — [site] · [date]

**Result:** X/5 tasks completed correctly

| # | Task | Result | What the agent got | Correct? | Evidence (URL) | Blocker |

## Fix first
1. … (link to the failing step)
```

Offer in one line: generate fixes with `agent-commerce-fixes`, or schedule a monthly re-test (same recurring-run options as `agent-commerce-audit`).
