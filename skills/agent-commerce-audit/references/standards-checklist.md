# Standards checklist (v0.3.0)

Each check has a rule ID, a level and a source. Levels: **REQUIRED** (required by the named standard or integration for the purpose stated), **RECOMMENDED** (beneficial, not mandatory), **OPTIONAL** (advanced or context-dependent), **EXPERIMENTAL** (emerging, not standardised). OPTIONAL and EXPERIMENTAL checks are reported but carry no score weight (see `scoring.md`). **critical** marks checks that decide the score status when unknown.

Record for every check: the URL, the field or observed value, the expected value and the status (PASS / PARTIAL / FAIL / NOT_CHECKED / NOT_APPLICABLE).

## 1. Agent access — weight 15

| ID | Check | Level | Source | PASS when |
|---|---|---|---|---|
| ACC-01 | Search and user-triggered agents not blocked on catalogue, product, policy and pricing paths | REQUIRED · critical | robots.txt (RFC 9309); providers' published crawler and agent documentation | Rules for search crawlers and user-triggered agents allow these paths. Training crawlers are a separate business choice and are not scored |
| ACC-02 | llms.txt | EXPERIMENTAL | llms.txt proposal (llmstxt.org) | File present with summary and key links. Absence is not a failure |
| ACC-03 | Sitemap lists product or service URLs | RECOMMENDED | Sitemaps protocol (sitemaps.org) | Sitemap referenced in robots.txt or at a standard path, listing product URLs |
| ACC-04 | Core content readable without client-side JavaScript | REQUIRED · critical | — | Retrieved HTML contains product name, price and description |
| ACC-05 | No bot wall on browsing pages | REQUIRED · critical | — | No CAPTCHA or verified access block (ACCESS_BLOCKED) on sampled browsing pages |

robots.txt distinguishes three classes: search crawlers, training crawlers, user-triggered browser agents. Never recommend allowing all AI bots indiscriminately.

## 2. Product data — weight 25

| ID | Check | Level | Source | PASS when |
|---|---|---|---|---|
| PRD-01 | Product markup present | REQUIRED · critical | schema.org `Product` (JSON-LD, Microdata or RDFa) | Present on every sampled product page |
| PRD-02 | Core offer properties | REQUIRED · critical | schema.org `Product`, `Offer` | `name`, `offers.price`, `offers.priceCurrency`, `offers.availability` present |
| PRD-03 | Descriptive properties | RECOMMENDED | schema.org; Google product structured data guidelines | `image`, `description`, `brand`, `offers.url` present |
| PRD-04 | Identifiers | RECOMMENDED | GTIN / MPN conventions | GTIN or MPN present where the product has one; NOT_APPLICABLE for handmade or custom goods |
| PRD-05 | Variants described | RECOMMENDED | schema.org `ProductGroup`, `hasVariant` | Variants described where the product has them; otherwise NOT_APPLICABLE |
| PRD-06 | Ratings markup honest | RECOMMENDED | schema.org `AggregateRating`, `Review` | Only real, visible reviews marked up; NOT_APPLICABLE if no reviews shown |
| PRD-07 | Structured data equals visible page | REQUIRED · critical | — | Price, currency and availability in markup match the visible page |

Keep three layers apart in findings: schema.org validity, Google Merchant Center requirements, OpenAI feed requirements. A property required by one is not automatically required by the others.

## 3. Policies — weight 15

| ID | Check | Level | Source | PASS when |
|---|---|---|---|---|
| POL-01 | Return policy stated | REQUIRED | Consumer-law disclosure; schema.org `MerchantReturnPolicy` | Window, method and fees stated on a reachable page |
| POL-02 | Return policy in markup | RECOMMENDED | schema.org `MerchantReturnPolicy` | Present in structured data |
| POL-03 | Shipping stated for the target market | REQUIRED | Consumer-law disclosure; schema.org `OfferShippingDetails` | Destinations, cost and time stated on a reachable page |
| POL-04 | Shipping in markup | RECOMMENDED | schema.org `OfferShippingDetails` | Present in structured data |
| POL-05 | Business identity | REQUIRED | Consumer-law disclosure; schema.org `Organization` / `LocalBusiness` | Legal name, contact and address published |
| POL-06 | Terms and privacy reachable | REQUIRED | — | Linked from sampled pages, readable text |

## 4. Feeds — weight 10

| ID | Check | Level | Source | PASS when |
|---|---|---|---|---|
| FED-01 | Publicly discoverable product feed | OPTIONAL | Public merchant-feed specifications (e.g. Google Merchant Center product data spec) | A public feed URL exists with core fields |
| FED-02 | Merchant feed submitted to shopping surfaces | RECOMMENDED | Google Merchant Center; OpenAI product feed spec | Merchant confirms a feed is submitted (MERCHANT_CONFIRMED); otherwise NOT_CHECKED |
| FED-03 | Stable product identifiers | RECOMMENDED | OpenAI product feed spec (stable item IDs) | Product URLs and IDs stable across sampled pages |

Absence of a public feed URL does not prove there is no feed: FED-01 FAIL never implies FED-02 FAIL.

## 5. Action path — weight 15

| ID | Check | Level | Source | PASS when |
|---|---|---|---|---|
| ACT-01 | Stable product URLs | REQUIRED | — | No session parameters required |
| ACT-02 | Price and stock visible without an account | REQUIRED · critical | — | Visible on sampled pages |
| ACT-03 | Guest checkout or documented sign-up | RECOMMENDED | — | Stated on the site |
| ACT-04 | Total cost before payment | REQUIRED | Consumer-law price transparency | Shipping, taxes and fees stated before the payment step |
| ACT-05 | Accessible forms and buttons | RECOMMENDED | WCAG 2.2 (labels, names) | Observed inputs labelled, buttons have text |
| ACT-06 | No CAPTCHA before the payment step | REQUIRED · critical | — | None observed on the observable path; beyond the last observable step → NOT_CHECKED |

Observe only. Never add to cart, submit forms or pay (see `security.md`).

## 6. APIs and protocols — weight 5

| ID | Check | Level | Source | PASS when |
|---|---|---|---|---|
| API-01 | Public API documentation | OPTIONAL | OpenAPI Specification | Public, versioned docs |
| API-02 | Standard authentication documented | RECOMMENDED if a public API exists, else NOT_APPLICABLE | OAuth 2.0 (RFC 6749) where the API uses delegated access | Flow documented |
| API-03 | Rate limits and errors documented | RECOMMENDED if a public API exists, else NOT_APPLICABLE | — | Documented |
| API-04 | MCP server or agent integration | OPTIONAL | Model Context Protocol | Present and documented. Not needed for agents to browse and buy |
| API-05 | Agent checkout protocols | OPTIONAL | Current agent commerce protocols — verify status by search at audit time | Supported or on the roadmap; cite source |

For an ordinary web store without a public API, APIs and protocols usually has no weighted applicable checks and is excluded from the overall score.

## 7. ChatGPT Wallet — weight 15

Details, evidence levels and verdicts: `chatgpt-wallet.md`.

| ID | Check | Level | Source | PASS when |
|---|---|---|---|---|
| WAL-01 | Signed-agent access | REQUIRED · critical | Web Bot Auth (HTTP Message Signatures, RFC 9421); OpenAI agent access guide | Merchant confirms bot protection verifies signed ChatGPT agent requests or an exception is configured. Provider identification alone → NOT_CHECKED |
| WAL-02 | No agent-blocking steps before the card form | REQUIRED · critical | OpenAI accept payments guide | Observable path shows none; unobservable part → NOT_CHECKED |
| WAL-03 | Card payments accepted | REQUIRED | OpenAI accept payments guide | Card payment documented or merchant-confirmed. Logos alone → PARTIAL |
| WAL-04 | Fraud rules handle agent purchases | RECOMMENDED | OpenAI Commerce Partner Playbook | Merchant confirms risk tool or provider recognises agent purchases and reads the `Forwarded` header |
| WAL-05 | Business Hub profile and feed | OPTIONAL | OpenAI Business Hub, product feed spec | Merchant confirms; market supported |
| WAL-06 | Market eligibility | — (context) | Official OpenAI pages at audit time | Record supported countries; outside them, the category is reported as preparation and excluded from the score with a reason |

## Non-store businesses

For booking, SaaS and services, use the matching schema.org type (`Service`, `Offer`, `Event`, `LodgingBusiness`, `SoftwareApplication`), map PRD checks to it, and treat the action path as booking, trial or sign-up. Mark store-only checks (shipping, returns of goods, GTIN) NOT_APPLICABLE with a reason.
