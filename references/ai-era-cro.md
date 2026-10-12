# AI-era CRO

Contents: AI-referred traffic · AI Overviews and click loss · on-site AI assistants · AI testing tools · AI-written copy and trust · agent-readable pages · limits of LLM audits

Fast-moving area. Put a date next to every figure and prefer peer-reviewed or independent data. Rows from search summaries are marked; re-open primaries before quoting numbers. Confidence: H independent or peer-reviewed, M vendor or secondary but consistent, L single or unverified.

## AI-referred traffic

- AI assistant referrals are a small share of traffic: ChatGPT referrals were under 0.2% of transactions across 973 sites in a peer-reviewed Marketing Science study, and below 1% in Microsoft Clarity's publisher data (M). They converted above paid social but below organic, email, paid search, and affiliate in that study (H).
- Their conversion versus other channels is contested and has moved. Adobe reported AI-referred retail visits converting 9% worse in Mar 2025, then better in later 2025-26 reports (M). Vendor figures such as "4.4x" (Semrush) and "11.4% vs 5.3%" (Similarweb) are single-vendor panels (L); don't quote them as benchmarks. Microsoft Clarity found 1.66% sign-up conversion for LLM referrals vs 0.15% for search, on one month of publisher data (M).
- Never assume AI traffic converts better. Segment it in the user's own analytics and compare on the user's baseline.
- Many AI visits arrive without a referrer, so GA4 "AI" counts are likely a floor (verify; unsourced).
- Landing implication (Inferred): AI-referred visitors arrive pre-informed and at the comparison stage. Audit for answer-first specifics (price, specs, availability, comparisons, policies) above the fold, and deep-link to the specific answer or product, not the homepage.
- Setup: create an "AI assistants" channel group in GA4 (referrers such as chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai; verify the list) and read it as undercounted.

## AI Overviews and click loss

- Pew found a result-click rate of 8% with an AI summary vs 15% without (H). Ahrefs reports about 34.5% lower position-1 click-through on AI Overview keywords (Apr 2025, M). Effects are measured mostly on informational queries; commercial, transactional, and branded queries are less exposed (L-M).
- Don't apply these drops to a user's page. Ask for Search Console data. Organic traffic loss with stable rankings: check impressions vs clicks and whether AI Overviews appear for the query set. The remaining traffic is more bottom-funnel, so conversion rate can change with no page change; compare by landing-intent segment before blaming the page.

## On-site AI assistants

- No independent holdout evidence of a conversion lift for on-site shopping assistants was found. Vendor and Amazon-attributed figures are self-selected engagers (L). The only randomized field experiment found was a livestream-platform assistant (+3.0% sales, -12.6% returns), not a web-store chat widget.
- Risks: a merchant can be held liable for its chatbot's wrong answers (Air Canada, 2024 BCCRT 149); Klarna reversed an AI-first support approach citing quality. NN/g's qualitative studies (7-9 users, 2026) found low discoverability, vague welcome messages, and sales-first answers that eroded trust. None report conversion lift.
- Rule: don't recommend adding a chatbot as a conversion lever. If one exists, audit discoverability, scope, human handoff, AI-identity disclosure, and wrong-answer logging, and test it against a holdout measuring conversion and support-contact or refund rate.

## AI testing and personalization tools

Vendor claims for Unbounce Smart Traffic, Mutiny, Optimizely Opal, and VWO Copilot have no independent measured-lift evidence (L). Auto-routing and bandit tools don't remove the need for a baseline and a no-AI control. AI-generated variants are cheap hypotheses, not evidence; the low win rate still applies. Low-traffic sites can't validate them either.

## AI-written copy and trust

No controlled conversion test of AI-written vs human-written page copy was found. Surveys show lower stated trust when AI content is noticed (Gartner 2026, Klaviyo 2025; stated attitudes, L-M), and one experiment found "artificial intelligence" in product descriptions lowered purchase intent, more for high-risk products (WSU 2024, M). Audit generic signals as Inferred: interchangeable superlatives, stock-style imagery, fabricated-looking testimonials, no named humans. Don't claim AI copy "hurts conversion"; recommend specificity and verifiable proof, and test AI-feature mentions in headlines. Never produce fabricated testimonials or review counts even though AI makes them cheap ([regulation-and-dark-patterns](regulation-and-dark-patterns.md)).

## Agent-readable pages (keep modest)

- Agentic checkout is early. OpenAI's Instant Checkout (Sep 2025) was scaled back by Mar 2026 (trade press, L-M); Google AP2 and UCP checkout are phased (M). Treat as monitoring items, not CRO priorities.
- Low-regret items already relevant to CRO: accurate Product and Offer structured data and feeds matching on-page price and stock, clear shipping and returns text, crawlable HTML (not JS-only), guest checkout, no CAPTCHA walls on core flows (Inferred).
- llms.txt showed no measurable citation effect in a ~300k-domain study, and Google says it doesn't use it (M). Don't recommend it as a conversion fix.

## Limits of LLM audits (this skill is one)

Published studies show LLM heuristic audits find plausible issues but are noisy. GPT-4o recalled 21% of expert-found issues in one study and 73-77% of a pooled issue set in another, with many false positives (65% of "severity 0" non-issues), moderate run-to-run agreement on detection (kappa about 0.50), and near-zero agreement on severity (M). Persona panels did not beat a no-persona baseline in a headline-click validation (preprint, L-M). Therefore:
- Tag every LLM-derived finding Observed or Inferred; treat severity as indicative.
- Flag single-screenshot limits (models misread UI components and miss cross-screen issues).
- Re-run or self-check borderline items.
- Never present simulated users or persona feedback as evidence of what customers will do.
- Say the audit is not a substitute for human expert review or user testing.
