# Page-type playbooks

Contents: homepage · paid landing page · SaaS pricing · B2B demo/contact · ecommerce PDP · cart/checkout · feature page · blog-to-lead · local service · high-ticket offline close · course/info product

Element priorities and failure patterns below are practitioner consensus, not outputs of a single study. Numbers appear only where a source exists (see [benchmarks-and-evidence](benchmarks-and-evidence.md)). Use each list as an audit order: check items top to bottom and report only real findings.

## Homepage

Goal: route each visitor type to the right next step fast. The primary conversion is a click-through to a money page (pricing, product, demo, category), not a direct sale.

Priority: 1. hero value proposition (what, for whom, outcome) readable in 5 seconds · 2. primary CTA plus one secondary, visible on mobile without scrolling · 3. clear navigation, few labels, pricing/contact reachable · 4. proof near the top · 5. audience routing blocks or category tiles · 6. how it works in 3 steps · 7. objection handling, repeat CTA, footer trust.

Failures: vague or clever headline; stock-photo hero with no product; multiple equal-weight CTAs; carousel hiding the offer; navigation with 8+ items or jargon; page talks about the company, not the visitor; ecommerce home without search, bestsellers, or a visible shipping/returns promise; slow hero image.

KPI: click-through to key pages and assisted conversions. Bounce is not the KPI. No credible public homepage conversion benchmark exists.

Carousels: the evidence is a single-participant NN/g observation (2013) that the offer was visible about 20% of the time and moving content read as ads; no carousel click-through rate was verified. Treat auto-rotating hero carousels as a finding, not a proven loss. On-site AI chat assistants are "needs data, test", not a ship item ([ai-era-cro](ai-era-cro.md)).

## Paid / lead-gen landing page

Goal: one action from message-matched paid traffic.

Priority: 1. message match (ad promise = headline = offer) · 2. single specific headline plus subhead stating the outcome · 3. one CTA repeated, label describes the result, no global nav · 4. form length and friction · 5. proof next to the CTA · 6. offer clarity and risk reducer (guarantee, response time) · 7. mobile layout and speed (most paid traffic is mobile) · 8. hero visual showing the product or outcome.

Failures: paid traffic sent to the homepage; navigation leaks; multiple offers; unneeded required fields (phone); headline does not match the ad; no conversion tracking or thank-you page; no tap-to-call on mobile.

Note: ad-platform conversion benchmarks (for example LocaliQ) use advertiser-defined actions and click denominators, not page conversion. Reading level: Unbounce's 2024 data found pages written at a 5th-7th grade level converted at 11.1% vs 5.3% for professional-level writing (correlational, Unbounce users, M); financial services was the exception. Simple, shorter copy usually wins; test before rewriting everything.

## SaaS pricing page

Goal: help the right buyer self-select a plan and start a trial or checkout, or request a quote for enterprise.

Priority: 1. 3-4 tiers named by audience, one recommended · 2. price visibility and a clear value metric, monthly/annual toggle with savings stated · 3. per-plan CTA with low-commitment wording · 4. 3-5 differentiators per plan, full comparison table below · 5. FAQ (billing, cancel, security, refunds), trial terms, "no card required" only if true · 6. proof near plans · 7. enterprise path.

Failures: "Contact us" only with no price anchor; too many tiers; feature lists in internal jargon; unclear limits; identical unclear CTA labels; no FAQ; mobile comparison table loses headers; no way to tell which plan fits.

Price visibility: NN/g studies observe participants leaving for competitors that show prices (2013, no counts), and 2006 B2B research (79 participants, 179 sites) ranked pricing first of 28 information types (old, qualitative). Hidden pricing may produce more form fills but worse pipeline quality in one vendor dataset (low confidence). A Microsoft test found a price-showing page drew fewer but better-qualified clicks (H), and a starting price on a lead-form page lifted leads about 15% in one 22,000-visitor, 4-week test (vendor-published, M). So: show a price, a starting price, a range, or typical scenarios; if "contact sales" only, say why and what to expect; test price visibility with lead quality as a guardrail. Measure pipeline quality, not form fills alone. One published pricing-page test bundled per-plan feature tables, one trial CTA message, and a demoted quote link for +94% trial clicks over 5 months, click metric only (M); use it as a hypothesis, not an expected lift. Hand off pricing level and packaging to **pricing**.

## B2B demo / contact page

Goal: a qualified meeting booked, not just a form fill.

Priority: 1. field choices (name, work email, company; extras only if used for routing) · 2. instant scheduling and a clear "what happens next / response time" · 3. headline saying what the demo covers and its length · 4. proof beside the form · 5. separate paths by intent (sales, trial, support) · 6. explicit trade-off between qualification and volume, progressive profiling · 7. thank-you page with booking, prep info, and a tracking event.

Failures: 8+ fields; mandatory phone with no reason; support and sales on one form; no calendar; generic confirmation; nav leaks; no proof; form fails on mobile; free-email blocking with no explanation.

Counterpoint: fewer fields can lower lead quality. Optimize for pipeline, not submissions.

## Ecommerce product detail page (PDP)

Goal: add to cart by resolving "is it right for me, will it arrive, can I trust you".

Priority: 1. image gallery (angles, zoom, in-context, video, variant-linked) · 2. price clarity with delivery cost/date and return terms near the CTA · 3. prominent add-to-cart, sticky on mobile, clear variant selection with inline stock/size errors · 4. reviews (count, distribution, photos, filter by attribute) · 5. concise benefits, scannable specs, size/fit help · 6. trust: returns, warranty, secure payment, payment methods and installments where relevant · 7. cross-sell below the main CTA · 8. stock urgency only if true.

Failures: variant must be chosen before price or availability shows; errors only after click; shipping revealed only at cart; reviews with no filtering; low-res or few images; wall-of-text description; CTA below the fold on mobile; out-of-stock dead end; sticky bar that hides content or breaks with variant selection; fake urgency.

Evidence: Baymard cart-abandonment reasons (extra costs, slow delivery, returns, card trust) justify showing cost, delivery, and returns on the PDP. Baymard's 2026 PDP benchmark of large sites found 44% lack returns info, 67% lack a total-cost estimate, 57% lack size buttons, 81% miss price per unit, and 89% don't respond to negative reviews; these are shares of sites with usability gaps, not lift data. Sticky add-to-cart evidence is mixed and agency-only: results range from conversion gains to one test where add-to-cart rose 6.8% but conversion fell 7.7% and revenue per visitor fell 22.1% (inconclusive). Test it with purchase and revenue per visitor as primary, add-to-cart as diagnostic, and QA that it doesn't cover variant errors or content. Delivery-date lifts (2.5-22.4%) are all tool-vendor claims; make dates accurate or omit them. Size and fit help should be measured on returns as well as conversion. On-site AI shopping assistants have no independent lift evidence and carry liability risk ([ai-era-cro](ai-era-cro.md)).

## Cart / checkout

See [forms-and-checkout](forms-and-checkout.md). Priority: total cost early, guest checkout, form simplicity, payment options, trust at payment, visible order summary with de-emphasized promo field, error recovery, cart persistence and recovery. Free-shipping threshold: message type matters (in one disclosed agency test a static banner moved conversion and a dynamic "X more" bar moved order value); check margin, revenue per visitor, and what share of orders already qualify.

## Feature / product page

Goal: convince an interested visitor to take the next step and pass intent signals.

Priority: 1. headline naming the job or outcome for a persona, not a feature name · 2. real product visual (screenshot, loop, interactive demo) · 3. how it works in 3 steps and a quantified or before/after benefit · 4. proof specific to this feature · 5. FAQ, integrations, security as relevant · 6. repeated CTA with a path to pricing · 7. links to related features and comparisons.

Failures: feature list with no outcome; abstract illustrations instead of the real product; no CTA after a long scroll; same proof on every page; copy duplicated across pages; heavy autoplay video hurting LCP. No credible conversion benchmark; use engagement and assisted-conversion paths.

## Blog / content page built to lead

Goal: move a qualified reader to a next step without wrecking the reading experience.

Priority: 1. intent match and a clear answer on the first screen · 2. contextual in-content CTA tied to the topic · 3. relevant content upgrade or lead magnet · 4. internal links to product pages with intent-matched anchors · 5. end-of-post CTA and related routing · 6. author credibility and last-updated date · 7. non-intrusive capture, mobile-safe (watch Google intrusive-interstitial rules) · 8. speed and stable layout (ads and embeds cause CLS).

Failures: one generic sitewide CTA; product pitch to a top-of-funnel reader; popups on load on mobile; no links to money pages; outdated content; no attribution. Measure assisted conversions and CTA clicks per post. Hand off popup design to **popups**.

## Local service / small business site

Goal: phone call, WhatsApp/message, or quote request from a mobile searcher with immediate need.

Priority: 1. tappable phone and, where relevant, WhatsApp, sticky on mobile · 2. service and location in the H1, clear service area · 3. trust: Google rating and review count, licenses, years, real photos, guarantees · 4. short quote form (3-4 fields) plus a response-time promise · 5. pricing cues ("from X", free estimate, financing) · 6. a page per service/area with local proof · 7. consistent name/address/phone, map, hours.

Failures: phone number as an image or not tappable; form-only contact; stock photos; no reviews; unclear hours; no call tracking; generic "Welcome" hero; slow mobile page; leads left unanswered. Answer rate and speed are part of conversion, so check operations, not only the page.

## High-ticket offer closed offline (form, call, or WhatsApp, then payment)

Applies to workshops, coaching, consulting, agencies, and B2C services where the page captures a lead and the sale closes in a conversation. Often combined with the course and local-service playbooks.

Goal: a lead who gets a reply, trusts the process, and pays. The page conversion is a proxy; the real KPI is paid enrolment.

Priority: 1. a short lead step (name and phone or WhatsApp is often enough) · 2. "what happens next" under the form: who contacts you, how fast, how payment works · 3. price shown with VAT stated, and installment or payment-plan info if offered · 4. refund, cancellation, or guarantee terms stated (only terms the seller truly offers) · 5. the reply channel works (WhatsApp link with a prefilled message, hours, response-time promise) · 6. proof of outcomes from people like the visitor · 7. an honest "who this is not for" section, which filters and builds trust · 8. true dates and seat counts (see Step 5 dimension 11).

Failures: price shown but no payment, installment, invoice, or refund information; form with no stated next step; dates and counts that are stale or contradict each other; leads that wait hours for a reply; one date repeated in every CTA so all expire together; conversion tracked on form submit only.

Response speed is a lever, with weak evidence: HBR 2011 found contacting a lead within an hour far likelier to qualify it than waiting longer (ratios only, no revenue outcome; M), while the popular "5 minutes / 21x" figures come from a vendor study (L). Use as direction and measure the client's own first-reply time against paid enrolment ([turkey-market](turkey-market.md) has the details). Check legal copy for refund and withdrawal wording before recommending "no refund" text ([regulation-and-dark-patterns](regulation-and-dark-patterns.md)).

Measure the whole chain: page view, lead, first reply (time), conversation, payment, and where leads drop. Count leads by source and by how long the first reply took. Page fixes cannot help if replies are slow, so check operations first. Don't A/B test when cohort volume is small (a few seats per cohort); ship evidence-backed fixes instead.

## Course / info-product sales page

Goal: purchase of a considered, trust-heavy offer, often warmed by email or a launch.

Priority: 1. transformation-led headline and who it is and isn't for · 2. offer stack: outcomes, curriculum, format, bonuses, delivery · 3. specific social proof (named, with results, video) · 4. instructor credibility tied to the outcome · 5. price framing, payment plan, clear total · 6. concrete guarantee with terms · 7. objection FAQ (time, skill level, refund, access) · 8. real urgency (cohort start, cart close) with repeated CTAs.

Failures: no CTA until the bottom; vague outcomes; generic testimonials; fake countdown timers; no installment option at high price; no curriculum preview; weak guarantee; checkout friction on a high-intent step. Traffic temperature dominates conversion; compare like for like only.
