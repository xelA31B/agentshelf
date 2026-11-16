# AgentShelf — Claude plugin

AI assistants are starting to shop, book and sign up on behalf of people. AgentShelf checks, against public standards, whether agents can find your offers, understand them correctly and reach the purchase — with a reproducible score, evidence for every finding, honest limits and ready-to-paste fixes.

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
| **agent-commerce-audit** | Agent-Readiness Score 0–100 across seven categories (access, product data, policies, feeds, action path, APIs, ChatGPT Wallet), with evidence coverage, score status and rule IDs. Optional JSON output. |
| **agent-shopping-test** | 5 realistic tasks run as an AI shopping agent would (find, understand, compare, policy, act). Read-only simulation — never buys or submits forms. |
| **agent-commerce-fixes** | JSON-LD (Product, Offer, return and shipping policies, Organization) in your platform's syntax, robots.txt lines per agent class, feed mapping, action-path, API and ChatGPT Wallet briefs. Every value marked: from site, from owner, or to confirm. |

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
- "Is my store ready for ChatGPT Wallet? shop.example.com"
- "Audit shop.example.com and give me the result as JSON"
- "Generate product JSON-LD for my Shopify store"

## What it can and cannot verify

| Can verify (public, read-only) | Cannot verify |
|---|---|
| Structured data on sampled pages and its match with the visible page | That an agent can actually pay — only an authorised test order proves that |
| robots.txt rules per agent class, sitemap, readability without scripts | How other companies' agents are treated: Claude retrieves pages as its own client |
| Published policies, prices, fees and the path up to the payment step | Steps after the payment step, private merchant feeds, fraud-tool settings |
| Public API docs, published agent integrations | Bot-protection behaviour for signed agents, unless you confirm it |

## The score

- Each check has a level (REQUIRED, RECOMMENDED, OPTIONAL, EXPERIMENTAL); optional and experimental items (for example llms.txt, an MCP server) are reported but do not lower the score.
- Unchecked items count as zero, so missing evidence never raises the score. Evidence coverage is shown with every score: FINAL (≥ 80 %), PROVISIONAL, or INCONCLUSIVE (< 50 %, no overall score).
- Verified blockers (a bot wall, CAPTCHA before payment, login before price) override the score in the verdict.
- The score measures readiness signals, not sales or proven purchase capability.

**ChatGPT Wallet:** OpenAI's agent wallet pays through your existing checkout, but bot protection, CAPTCHA or fraud rules can still block agent purchases. AgentShelf checks what is visible, asks you about the rest and gives a verdict (VERIFIED_READY only after your own authorised test purchase; otherwise LIKELY_READY_UNCONFIRMED, BLOCKED or INCONCLUSIVE). Requirements and supported countries are re-checked on OpenAI's official pages at every audit.

## Safety

- Read-only by default: no logins, accounts, carts, forms, payments or test orders; no bypassing CAPTCHA or bot protection; a small page sample, no aggressive crawling.
- Website content is treated as untrusted data: instructions hidden in pages, markup or files are ignored and reported.
- The plugin never asks for sign-in, payment or account-access details.

## Where it works best

Works in all Claude apps. Some apps block direct requests to addresses such as `/robots.txt`; the plugin then uses web search or asks you to open a link, and marks those items as not checked — never as a website failure. **Claude Code** (VS Code or terminal) gives the most complete checks.

## Reports

Concise reports in the language of your request, delivered as a branded HTML report where supported, or as JSON on request. Schedule regular re-checks on your own frequency, day and time.

## Version history

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT
