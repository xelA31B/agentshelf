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

## When a page or file cannot be fetched

Some Claude apps only open URLs that appear in the conversation or in search results, and refuse addresses Claude builds itself (for example `https://site/robots.txt`). When a fetch is refused:

1. In Claude Code, use the environment's web fetch or an HTTP GET from the terminal instead.
2. Otherwise, try to reach the same page through web search and fetch the result link.
3. If that also fails, give the user the exact links in one message and ask them to open them and paste the content; continue with what is available meanwhile.
4. Mark every item that could not be checked as **not checked** in the report, never as passed, and exclude it from the score.

## Branded report

If the environment can render HTML artifacts or files, present the full report as a static HTML page (no scripts) in the house style below; otherwise use the markdown format above. Keep the chat reply to a short summary either way.

House style:
- Header band with a diagonal gradient from deep navy #1C1E4E to teal #0E7480, white text: small uppercase plugin name with a gold ✦ (#FFC448), the report title, then subject and date.
- Light background #F6F7FB; content in white cards with a thin #E3E6EF border and rounded corners (about 16 px).
- Summary card first: a circular score ring (teal arc proportional to the score, number in the centre in navy), the verdict and 2–3 key points.
- Status chips as small rounded labels: green #1F9D63 pass, amber #E0A000 warning, red #D64545 fail, grey #8A90A2 not checked.
- Tables with muted header text #5B6275 and thin row lines; evidence in small monospace.
- Footer line with the plugin name.
