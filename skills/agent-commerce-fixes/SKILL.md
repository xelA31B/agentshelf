---
name: agent-commerce-fixes
description: >
  This skill should be used when the user asks to "fix my store for AI agents", "generate product
  schema", "create JSON-LD for my products", "write a return policy schema", "make my product feed",
  "add llms.txt for my shop", or after an agent-commerce-audit or agent-shopping-test when the user
  wants the fixes prepared. Also triggers on the same requests in Russian ("исправь магазин для
  ИИ-агентов", "сделай разметку товаров") or Hungarian.
metadata:
  version: "0.1.0"
---

# Agent Commerce Fixes

Turn audit findings into ready-to-use, standards-valid assets.

## Rules

- Language of the user's request for explanations; code and field names as the standard defines them.
- Use only facts from the site or the user. Ask to confirm any value not found (GTIN, return window, shipping cost). Never invent reviews, ratings, prices or stock.
- Output valid JSON-LD and feed fields per the referenced standard; note the standard next to each asset.
- Do not change the website yourself unless the user gives access and confirms; by default deliver copy-paste assets with placement instructions.

## Assets

Offer what the findings require (default: the first four):

1. **Product JSON-LD template** — `Product` + `Offer` (+ `ProductGroup` for variants, `AggregateRating` only for real visible reviews), with the platform variables to fill (e.g. Shopify Liquid, WooCommerce fields) when the platform is known.
2. **Policy markup** — `MerchantReturnPolicy`, `OfferShippingDetails`, `Organization` / `LocalBusiness`.
3. **robots.txt lines** — allow search and user-triggered AI agents on catalogue, policy and pricing paths; the user decides on training crawlers.
4. **llms.txt** — summary, catalogue structure, policies, contact, API docs link.
5. **Product feed field mapping** — site data → merchant-feed fields, with gaps listed.
6. **Action-path fixes** — prioritized list (price before login, guest checkout, form labels, fee transparency).
7. **API / agent integration brief** — what to document (OpenAPI, OAuth 2.0, limits), and options for an MCP server or agent checkout protocols, with sources checked by web search.

## Output

For each asset: the code or text block, where to put it, who usually does it (admin, developer, app/plugin for the platform) and how to validate it (e.g. a public structured-data testing tool, feed diagnostics).

Close with one line offering to re-run `agent-commerce-audit` after the changes are live.

## Branded document

Start the deliverable with a header block, translated into the document language: plugin name with ✦, document title, then subject · version · date · owner · status (draft or current). Follow with a 2–3 line summary and numbered sections; use tables for structured content and code blocks for anything to paste.

If the environment can render HTML artifacts or files, present it as a static HTML page (no scripts) in the house style: header band with a navy #1C1E4E to teal #0E7480 gradient and white text, meta details as small rounded pills, light background #F6F7FB, white rounded cards with a #E3E6EF border, summary card with a gold #FFC448 left accent, dark code blocks. Otherwise deliver the same structure as a document artifact or markdown.
