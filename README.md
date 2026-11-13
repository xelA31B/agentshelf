# AgentShelf — Claude plugin

AI assistants are starting to shop, book and sign up on behalf of people. AgentShelf checks, against public standards, whether agents can find your offers, understand them correctly and complete the purchase — and gives you the fixes.

## Install

**Claude app (web, desktop):** Plugins → add a marketplace from a GitHub repository → `xelA31B/agentshelf` → install **AgentShelf**. Once approved in the Claude directory, search for **AgentShelf** in Plugins.

**Claude Code (VS Code or terminal):**

```
/plugin marketplace add xelA31B/agentshelf
/plugin install agentshelf@agentshelf
```

## Skills

| Skill | What you get |
|-------|--------------|
| **agent-commerce-audit** | Agent-Readiness Score 0–100 across access, product data, policies, feeds, action path and APIs. Every finding: standard → what was checked → evidence. |
| **agent-shopping-test** | 5 realistic tasks run as an AI shopping agent would (find, understand, compare, policy, act). Read-only — never buys or submits forms. |
| **agent-commerce-fixes** | Valid JSON-LD (Product, Offer, return and shipping policies, Organization), robots.txt lines, llms.txt, feed mapping, action-path and API recommendations. |

Standards used: schema.org, robots.txt (RFC 9309), Sitemaps protocol, llms.txt, public merchant-feed specifications, OpenAPI, OAuth 2.0, Model Context Protocol, WCAG basics. Agent payment protocols are checked against current sources at audit time.

## Commands

Type `/` in Claude and pick a command:

| Command | What it does |
|---|---|
| `/agent-shop-audit [website] [market]` | Is a store, site or API ready for AI shopping agents |
| `/agent-shop-fixes [website or audit]` | Ready-to-paste fixes for AI shopping agents |
| `/agent-shop-test [website] [product or task]` | Test a store as an AI shopping agent (read-only) |

## How to use

- "Is my store ready for AI shopping agents? shop.example.com"
- "Проверь, сможет ли ИИ-агент купить товар на моём сайте"
- "Generate product JSON-LD for my Shopify store"

Concise reports in the language of your request, with an option to schedule regular re-checks on your own frequency, day and time.

## License

MIT
