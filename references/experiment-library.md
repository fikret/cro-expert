# Experiment library

Contents: how to use it · structural tests · page-type ideas · ship, don't test · low-value tweaks · AI personalization tools

A list of ideas is not a plan. Before proposing any of these: pass the traffic gate ([viability-and-stats](viability-and-stats.md)), tie the idea to evidence from the audit, and score it ([prioritization-and-experiments](prioritization-and-experiments.md)). Published win rates are low (roughly 10-35% depending on domain; two thirds or more of tests don't win), so favor structural changes over tweaks. Use **ab-testing** for test design and program management.

Each line is a hypothesis to test, not a recommendation.

## Structural tests (most likely worth the traffic)

- Offer or packaging presentation (what is included, bundles, order of plans).
- Page structure: short vs. long, section order, proof placement, objection section position.
- Primary CTA strategy: one action vs. two, high-commitment vs. low-commitment first step.
- Lead step: form vs. calendar embed vs. WhatsApp/phone; single-step vs. multi-step.
- Pricing presentation: show vs. hide price, tier count, recommended plan, annual toggle default.
- Hero concept: outcome-led vs. mechanism-led message; product visual vs. outcome visual.
- Risk reversal: guarantee, trial terms, cancellation clarity (only real terms).
- Offer-in-headline vs generic headline (Highrise 2009: a free-trial headline beat a generic one by 30% on about 4,000 views, small and old [M]; test, don't assume).
- Image or product visual vs video in the hero: don't assume video wins (in the Obama splash-page test all three videos lost to images at about 13,000 visitors per combination [M]).
- Starting price or price range on a lead page, with lead quality as a guardrail.

Expect most structural tests not to win: roughly 10-35% do, depending on domain (Optimizely, Kohavi, Georgiev; [viability-and-stats](viability-and-stats.md)).

## Page-type ideas

**Homepage**
- Audience routing blocks vs. single-path hero.
- Proof in hero (logos, a quantified result, a short testimonial) vs. below the first screen.
- Nav CTA present vs. absent; reduced nav labels.
- Comparison vs. status quo or alternatives section.
- Demo or product visual: static screenshot vs. short loop vs. interactive demo.

**Landing / paid page**
- Exact message match with ad vs. generic headline; audience-specific pages per segment.
- Navigation removed vs. kept.
- Proof density and placement near the CTA.
- Video explaining the offer vs. text.
- Genuine urgency messaging (only if true).

**Pricing**
- Annual vs. monthly default and savings framing.
- "Most popular" plan highlighted vs. none; 3 vs. 4 tiers.
- Comparison table vs. expandable sections; plan recommendation quiz.
- FAQ or ROI calculator near plans; guarantee placement.
- Per-seat breakdowns for team plans; custom tier shown vs. "contact us".

**Demo / contact**
- Phone field optional vs. required; fewer fields; enrichment instead of asking.
- Inline calendar vs. form then email.
- "What you'll learn / what happens next" block; testimonials beside the form; FAQ below.
- On-demand option next to live; qualification routing (self-serve vs. sales).

**Blog / resource**
- Contextual inline CTA vs. end-of-post only; topic-specific content upgrade vs. generic banner.
- Related-resource block; featured resources; gated vs. open for specific assets.

**Feature page**
- Real product demo vs. illustration; before/after; use-case examples.
- Feature-specific trial CTA; link to the relevant plan; related-feature links; case-study link.

**Ecommerce PDP / checkout**
- Delivery cost and date near the CTA; returns summary near the CTA.
- Sticky add-to-cart on mobile; review summary placement; size guide visibility.
- Guest checkout prominence; express payment options; collapsed promo code field.
- Free-shipping threshold level and message type (static vs dynamic progress bar); primary metric revenue per visitor, guardrail margin.
- Mobile search bar visible vs icon; filter default state (agency tests report large lifts in 1-2 weeks; treat as hypotheses).
- Redesign vs old-site holdout before a full launch (a vendor case reported the new site initially lost).
- A persistent 5-10% holdout on abandoned-cart flows to measure incrementality.

**High-ticket offline close**
- "What happens next" under the form vs. none; installment or payment info vs. none.
- Reply channel: WhatsApp-first vs. form-first; stated response time.
- Free intro call vs. direct enrolment as the primary CTA.

## Ship, don't test

These are fixes, not experiments. Do them, then measure before and after.
- Page speed and Core Web Vitals problems; layout shift; broken or slow third-party scripts.
- Accessibility defects (contrast, labels, focus, alt text).
- Broken tracking, dead links, form bugs, error handling that wipes input.
- Mobile layout bugs and unreachable CTAs.
- Stale dates, contradicting scarcity counts, or claims you cannot support.

## Low-value tweaks (usually flat; test only with lots of traffic)

Button color in isolation, small copy swaps, price endings ($99 vs. $97) without a reason, icon style, minor spacing, trust-badge swaps, and promo-field removal (public evidence is small or underpowered: GoodUI's median +0.8%). Contrast and visual hierarchy matter more than hue.

## AI personalization and auto-allocation tools

Vendor claims for Unbounce Smart Traffic, Mutiny, Optimizely Opal, and VWO Copilot have no independent measured-lift evidence (L). Bandit and auto-routing tools don't remove the need for a baseline and a holdout; keep a no-AI control. AI-generated variants are cheap hypotheses, not evidence, and low-traffic sites can't validate them either ([ai-era-cro](ai-era-cro.md)).
