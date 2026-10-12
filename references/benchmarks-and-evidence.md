# Benchmarks and evidence

Contents: how to use benchmarks · why they conflict · ecommerce · lead-gen · AI search · solid evidence · case studies and test results · treat carefully · gaps

Benchmarks reviewed 2026-10. Re-check Littledata, Baymard, LocaliQ, and Contentsquare yearly.

Confidence: **H** independent or primary source verified · **M** vendor or secondary, consistent across sources · **L** single vendor claim or practitioner convention.

## How to use benchmarks

1. Ask for the user's own baseline first, segmented by device and source, and use their own trend.
2. Confirm numerator, denominator (sessions vs users vs impressions vs clicks), device, traffic mix (paid vs all), median vs mean, period, and who is in the sample before comparing. Quote a range plus its definition, never one average.
3. State the confidence tag, source, and date with every number. If the definition can't be confirmed, say so.
4. A gap versus a benchmark is a hypothesis generator, never a verdict or a target.
5. Never present a vendor lift or case study as an expected outcome.

## Why benchmarks conflict

Different denominators (sessions, visitors, clicks, impressions); mean vs median; purchase vs add-to-cart vs advertiser-defined "conversion actions"; paid-only vs all traffic; platform-specific samples (Shopify stores, Unbounce users, US small-business advertisers); cross-device journeys that distort per-device rates; seasonality; self-selected vendor customers; hidden methodology.

Weak or hidden-method sources (use as L at most): Digital Bloom, First Page Sage (as relayed), Dynamic Yield definitions, Focus Digital, SaaSHero, gated Contentsquare absolutes, blog compilations without a stated method.

## Ecommerce conversion

- **Littledata** (Shopify stores; sessions with a purchase over all sessions, GA4; 426 stores, 90 days to 2026-10-03): median 1.4%, mean 1.9%, top 20% above 2.7%, top 10% above 3.5% [M-H]. Excludes stores under 1,000 sessions or 90 purchases. Industry medians: beauty about 2.8%, health and supplements about 2.5%, food and beverage about 2.3%, fashion about 1.3%, home and furniture about 0.9% [M]. Device median 1.5% on both mobile and desktop.
- **Statista** global visits-to-purchase 1.4% in Q2 2026 [M, not verified at source].
- **Triple Whale** (opened 2026-10; paid-traffic data, 53,000+ brands, Aug 2025-Jul 2026): median conversion 1.69%, top 20% 3.2%+, top 10% 4.7%+, desktop 1.9% vs mobile 1.2%. The same page also quotes a 2.66% "global average" with no source, which shows how definitions drift inside one page [M].
- Older "2-3% planning range" and "food and beverage 5-7%" figures lack a verifiable method; don't use them.
- Device: sources conflict (Littledata parity; Contentsquare reportedly desktop 3.4% vs mobile about 2.0%, relayed second-hand and gated; Unbounce landing pages: desktop converts about 8% better than mobile with 83% of visits on mobile). Mobile is typically about 70-78% of visits. Benchmark per device on the user's own data.
- Contentsquare reports conversion down 6.1% (2025 report) and 5.1% (2026 report) year over year [M].
- Cart abandonment: **70.22%**, the mean of 50 third-party studies (range about 55-84%), list updated 2025-09-22 [H as a meta-average, Baymard]. Not a measured rate for any single store. 42% of US abandoners were just browsing; among the rest the top reasons are extra costs (about 40%), slow delivery (20%), distrust of card handling (19%), forced account (18%), long checkout (17%).
- Add-to-cart: about 4-7% typical in Triple Whale's vendor data [L-M].

## Lead-gen

- **Landing pages:** Unbounce 2024 edition (data to mid-2024; 41K Unbounce pages, 464M visitors): median **6.6%**, industry medians 3.8-12.3%. Conversion type is undefined, medians and averages are mixed, and pages belong to Unbounce users [M]. The 2024 edition is the newest I could open; ignore blog claims of a newer median. Never quote a single average.
- **Paid search:** LocaliQ/WordStream (opened 2026-10; 16,446 US campaigns, Apr 2024-Mar 2025, minimum 64 campaigns per category): median conversion **7.52%** ("averages" are medians), from about 2.5% (finance and insurance) to about 14.7% (automotive repair); education and instruction 11.38%. Conversions are advertiser-defined actions, the sample is US small-business skewed, and the denominator is clicks [M]. A 2026 edition exists behind a form (not opened). Not comparable to page-level conversion.
- **Meta lead campaigns:** about 7.7% (726 US campaigns, lead-form events) [M].
- **B2B SaaS:** visitor-to-lead about 0.7-2.2% by channel and 1.1-1.4% blended in compilations with hidden methods; free trial to paid about 18% opt-in vs about 49% card-required (First Page Sage, agency clients, unverified) [L]. Define "lead" (form, MQL, meeting) before comparing.
- **Demo forms:** no credible visitor-to-submit benchmark. RevenueHero's published figure is qualified-lead-to-meeting-booked (median 62%, vendor customers), a different metric [L-M].
- **Email signup popups:** about 2-3% of impressions in ecommerce (Omnisend 2.1%, Klaviyo 2.3%) [L-M]; the denominator is impressions.
- **Local services:** home-services median landing page about 6.7% [L]. Invoca 2026: 52% of callers reach a person and 45% of lead calls convert on the call [M, vendor].
- **Course and info-product pages:** 2-5% typical, 10-15% optimized [L]; traffic temperature dominates.
- **Homepage, feature-page, and blog-CTA conversion:** no credible benchmark found. Say so.

## AI search and click-through

See [ai-era-cro](ai-era-cro.md). Don't quote Semrush "4.4x" or Similarweb "11.4%" as benchmarks (L). AI Overview click effects are measured mostly on informational queries.

## Solid evidence

- Baymard abandonment reasons and form findings [H]. See [forms-and-checkout](forms-and-checkout.md). Baymard pages disagree internally in places (for example 39% vs 40% extra costs; 31% vs 32% no inline validation); cite the page and date.
- NN/g studies are qualitative usability observations. Sample sizes are small (often 1-9 participants in the cited examples) and none report conversion lift. Dates matter: 2005-2013 items are old.
- NN/g scrolling and attention study, 2018 (n=120, 130,000+ fixations): 57% of viewing time above the fold, 74% in the first two screens [H].
- Core Web Vitals thresholds from web.dev [H].
- Peeking inflates false positives (Evan Miller) [M-H].
- Microsoft Office Online test: showing price cut clicks per user by 64% because the remaining clickers were better qualified (Kohavi et al., KDD 2014) [H]. Click lifts are surrogate metrics; report a downstream metric (qualified lead, trial-to-paid, pipeline) beside any click lift.
- Win rate: about 12% (Optimizely, vendor, 127k tests) vs about one third positive at Microsoft (Kohavi et al., H) vs 33.5% significant wins in Georgiev's independent 1,001 tests (median lift 0.08% across all tests, 7.5% among winners). The range depends on domain, maturity, and who is measured; don't quote a single number as a target. Typical shipped improvements at mature sites are 0.1-2% (Kohavi, Tang, Xu 2020, H).
- SRM affects about 6% of Microsoft experiments (Fabijan et al., KDD 2019) and about 10% of LinkedIn triggered analyses [H]. Novelty effects: Dmitriev et al., KDD 2017 [H]. CUPED cut variance about 50% at Bing (Deng et al., WSDM 2013) [H]. Peeking: Evan Miller's "10 peeks turns 1% into 5%" is confirmed; Johari et al., arXiv 1512.04922 is the formal source [H].
- GoodUI "remove coupon fields": 10 tests 2015-2026, median sales +0.8%, pooled +0.5% (p=0.13, not significant) [M-H]. Use as a sanity range for a checkout micro-change: small.
- Free returns (Patel et al. 2021): order value +9.15% and margin per order +9.71%, but returns rose 7.86% and the authors estimate the cost exceeds the gross-profit gain [H-M].
- Reuse/Klaviyo 10% holdout (May-Aug 2026): no detectable order effect on existing customers from cart-recovery messaging; +19% orders from new subscribers [M-H, vendor case]. Platform-attributed "recovered revenue" overstates incrementality.

## Case studies and test results

Published ecommerce UI tests with disclosed data cluster at low single-digit effects; treat headlines above +20% as survivorship or definition artifacts until the method is shown. When citing a case, state who published it, the date, what was measured (conversion vs revenue per visitor), whether baseline, sample, duration, and significance were disclosed, and whether several changes were bundled. If not, say "headline claim only". If the headline is +30% or more, say it is unlikely to transfer.

Reported examples, all to be quoted as "reported", never as an expected lift:
- Speed: Rakuten 24 (conversion +33%, revenue per visitor +53%, one page, one month, N not reported) and Vodafone (+8% sales, bundled changes) [M].
- Express checkout: a merchant cart-drawer wallet test reported +35% in 2 weeks, N not given [M-L]; Shopify's own Princess Polly case shows +4.1% for returning Shop Pay users but about +1.6% store-wide [M]. "Up to 50%" claims have no method [L].
- Sticky add-to-cart: agency tests range from about +7% to +16% conversion to a test where add-to-cart rose 6.8% but conversion fell 7.7% and revenue per visitor fell 22.1% (inconclusive) [L-M]. Judge on purchase and revenue per visitor.
- Free-shipping threshold: one agency test found a static banner moved conversion (+3.1%) but not order value, while a dynamic "X more" bar moved order value about 10% (14 days each, no significance reported) [M].
- Starting price on a lead-form page: about +15% leads in one 22,000-visitor, 4-week test (iProspect via Convert, vendor-published; uneven split) [M]. A high anchor underperformed in some categories.
- Pricing-page bundle (feature tables, one trial CTA message, demoted quote link): +94% clicks to trial in a 5-month test, click metric only [M]. Hypothesis, not an expected lift.
- Highrise 2009 (free-trial headline +30%, about 4,000 views) and the Obama splash page (24 combinations, about 13K visitors each; every video lost to an image) are small or old [M].
- Agency and vendor lifts of +54% to +363% (GetUplift/Teamwork, Conversion Rate Experts/Crazy Egg, Wynter/Appcues) omit baseline, sample, duration, and significance and bundle several changes [L].

## Treat carefully

- Deloitte/Google speed study: sponsored and observational [M]. Portent speed data: correlational [M].
- "1,000 conversions a month" and "350 per variation" testing rules: folklore or vendor attribution [L]. CXL's own page on stopping tests could not be opened.
- Hotjar and Clarity minimum sample sizes: none verified.
- Baymard's "+35% conversion from checkout fixes": its own estimate (35.26% for large sites, method unpublished), not a measured outcome.
- Sticky CTA, installment-display, and WhatsApp lifts: no controlled data found [L].
- Amazon "100 ms = 1% of sales" and Walmart "+2% per second": repeated second-hand with no primary source located [L]. Guest-checkout lifts (+45%, +180%) have no located primary source; justify guest checkout with Baymard's 18% "account required" reason instead.
- Estimated-delivery-date lifts (2.5-22.4%) come only from tool vendors [L].
- Think with Google speed statistics: not opened [L]. The "84-user accessibility study / 306%" figure appeared only in a search snippet [L].

## Gaps

No primary source for: homepage conversion, feature-page conversion, blog CTA conversion, message-match lift, an empirical hierarchy of CRO research methods. No Wolfgang Digital report after 2017; Adobe and Salesforce publish spend and traffic share, not conversion rate; no independent lead-form or free-trial benchmark. No Turkish retailer test with a disclosed method was found (Hepsiburada's 2017 Optimizely redesign case, +22% conversion, vendor-published, where the new site initially lost, is the only datapoint [L]). CXL, GoodUI (paywalled), Conversion.com, and several other practitioner sources could not be fully verified.
