# Standards checklist

Weights in brackets. Verify each item on real pages; record the URL and field as evidence.

## 1. Access for agents (15%)

| Check | Standard / reference | Pass when |
|---|---|---|
| AI crawlers and user-triggered agents allowed | robots.txt (RFC 9309); published AI user-agent tokens of OpenAI, Anthropic, Perplexity, Google | Search and user-triggered agents not blocked on product, policy and pricing paths |
| llms.txt present | llms.txt proposal (llmstxt.org) | File exists with summary and links to catalogue, policies, contact |
| Sitemap covers products | Sitemaps protocol (sitemaps.org) | Sitemap referenced in robots.txt and lists product/service URLs |
| Readable without JavaScript | — | Fetched HTML contains product name, price and description |

## 2. Product / offer data (30%)

| Check | Standard | Pass when |
|---|---|---|
| Product markup | schema.org `Product` in JSON-LD | Present on every sampled product page |
| Required properties | schema.org `Product`, `Offer` | `name`, `image`, `description`, `brand`, `sku` or `gtin`, `offers.price`, `offers.priceCurrency`, `offers.availability`, `offers.url` |
| Identifiers | GTIN / MPN conventions | GTIN or MPN present where the product has one |
| Variants | schema.org `ProductGroup` / `hasVariant` | Variants (size, colour) described, not only the default |
| Ratings (if shown) | `AggregateRating`, `Review` | Only real, visible reviews marked up |
| Consistency | — | Structured price, currency, availability equal the visible page |

## 3. Policies (20%)

| Check | Standard | Pass when |
|---|---|---|
| Returns | schema.org `MerchantReturnPolicy` | Return window, method, fees stated, in markup or a clear policy page |
| Shipping | schema.org `OfferShippingDetails` | Destinations, cost, delivery time for the target market |
| Organization | schema.org `Organization` / `LocalBusiness` | Legal name, contact, address, `sameAs` profiles |
| Terms, privacy, warranty | — | Public, linked from every page, readable text |

## 4. Feeds (10%)

| Check | Standard | Pass when |
|---|---|---|
| Product feed | Public merchant-feed specifications (e.g. Google Merchant Center product data spec) | Feed exists with id, title, description, link, image, price, availability, brand, GTIN/MPN |

## 5. Action path (15%)

| Check | Pass when |
|---|---|
| Stable URLs | Product and category URLs do not depend on session parameters |
| Price before login | Price and stock visible without an account |
| Guest checkout or clear sign-up | Documented on the site |
| Total cost transparency | Shipping, taxes and fees shown before payment |
| Accessible forms | Inputs have labels; buttons have text (WCAG 2.2 basics) |
| Bot walls | No CAPTCHA on browsing pages (note if present at checkout) |

## 6. APIs and protocols (10%)

| Check | Standard | Pass when |
|---|---|---|
| API documentation | OpenAPI Specification | Public, versioned docs |
| Authentication | OAuth 2.0 | Standard flow documented |
| Limits and errors | — | Rate limits and error codes documented |
| Agent integration | Model Context Protocol (MCP) | MCP server or documented agent integration |
| Agent checkout / payments | Current agent commerce protocols — verify status by web search at audit time | Supported or on the roadmap; cite source |

For non-store businesses (booking, SaaS, services), replace `Product` with the matching schema.org type (`Service`, `Offer`, `Event`, `LodgingBusiness`, `SoftwareApplication`) and the action path with booking, trial or sign-up.
