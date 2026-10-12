# Mobile, speed, accessibility

Contents: mobile checks · speed and Core Web Vitals · what the speed studies show · accessibility

Confidence tags: H primary verified, M secondary or vendor consistent, L single or unverified.

## Mobile checks

- Mobile is roughly 70-78% of ecommerce visits, but converts lower than desktop in several vendor panels (Contentsquare 2026 reportedly 2.0% vs 3.4%; Littledata shows parity; sources disagree; M/L). Use as context only and ask for the user's own device split. Wallets were about 53% of global ecommerce spend in 2024 (Worldpay, M), not a per-merchant forecast.
- Primary CTA visible without hunting. Sticky CTAs: published agency A/B tests on mobile product pages range from about -8% to +16% conversion, sample sizes undisclosed and winners over-published (L); one test lifted add-to-cart but cut revenue per visitor. Test, and judge on revenue per visitor, not add-to-cart. It must not cover content or break with the keyboard, and should respect safe-area insets.
- Touch targets: WCAG 2.2 SC 2.5.8 (AA) requires 24x24 CSS px, or a 24px circle around each undersized target that touches no other target (W3C Understanding doc). SC 2.5.5 (AAA) asks for 44x44 CSS px. Apple HIG recommends 44x44 pt; Android accessibility help recommends 48x48 dp with 8dp spacing (the 8dp is Android guidance, not WCAG). A tiny text link as the only CTA is a finding.
- Inputs: correct `type`/`inputmode`/`autocomplete`, 16px+ font to avoid iOS zoom, don't disable pinch-zoom, labels above fields, wallet pay. A touch keyboard takes a large share of the viewport (check on a real device which fields stay visible).
- Sticky headers: keep them small and opaque with touch targets of about 1 cm (NN/g 2021). Tables (pricing, specs): keep headers visible or lock the first column (NN/g 2017); horizontal scroll that loses context is a finding. Don't attribute thumb-zone research to NN/g.
- No intrusive interstitials; fixed headers that eat the viewport; tap-to-call and WhatsApp links work.
- Judge mobile from a mobile screenshot or device emulation, never from a desktop screenshot.

## Speed and Core Web Vitals

Thresholds are unchanged (web.dev, updated 2024-10-31; INP page 2025-09-02), assessed at the 75th percentile of field loads, mobile and desktop separately: LCP at or under 2.5 s, INP at or under 200 ms, CLS at or under 0.1. A page passes only if all three are good. Lighthouse cannot measure INP (uses TBT as a lab proxy); real data comes from CrUX, PageSpeed Insights, and Search Console. Web Almanac 2025 (CrUX, July 2025): 48% of mobile sites and 56% of desktop sites pass all three; mobile LCP is the weak metric (62% good), INP 77% good on mobile (M-H).

Google says Core Web Vitals feed its ranking systems but don't guarantee ranking and relevance still dominates, so speed's SEO effect is a modest tiebreaker, not a main lever.

Audit points: LCP image prioritized and not lazy-loaded, explicit image dimensions, render-blocking resources, image weight, third-party scripts (tag bloat, chat widgets, popups), layout shift culprits (ads, embeds, fonts), INP on variant selectors and filters.

Report field vs lab data when available, link the largest LCP element, and state that the conversion effect of fixing it is uncertain and hypothesis-level. Verify with before/after analytics or an A/B test. Speed fixes are usually shippable without a test. If the PageSpeed API quota is exhausted, say speed could not be measured and ask for CrUX or Search Console data.

## What the speed studies show

| Study | What it found | Caveat |
|---|---|---|
| Deloitte/Google "Milliseconds Make Millions" (2020) | A 0.1 s gain across all four metrics on every page in the journey correlated with retail progression and spend increases (commonly quoted 8.4% retail conversion) | Google-commissioned, observational, 2019 data, 0.1 s on every page is hard. Don't say "0.1 s faster = +8.4% for you" |
| Portent (2022) | Ecommerce conversion 3.05% at 1 s, 1.68% at 2 s, 1.12% at 3 s | Correlational, small site sample, load metric undefined |
| Vodafone (2021) | 31% better LCP gave +8% sales in an A/B test | One company; the optimized page also changed other things; stats not published |
| Rakuten 24 | A/B test of an optimized page: +33% conversion | Single page; web.dev warns field correlation is not causation |
| QuintoAndar INP case (web.dev, 2025) | INP -80%; conversion volume +36% year over year | The 36% is year over year, not the test delta; no duration, sample, or significance |
| Trendyol INP case (web.dev) | INP -50%, +1% listing-to-detail click-through | Test mentioned, no stats; the metric is click-through, not revenue |

No 2024-2026 case study with fully disclosed randomized methodology was found. Treat all as hypothesis-generating; use them to justify looking at speed, not to forecast.

## Accessibility

- Check basics: color contrast, form labels, keyboard focus visibility, alt text, heading structure, tap targets.
- WebAIM Million (Feb 2026): 95.9% of one million home pages had detectable WCAG failures, 56.1 errors per page (2025: 94.8%, about 51). Most common: low contrast, missing alt text, missing form labels, empty links and buttons. Automated scans and screenshots catch only part of the issues; never assert WCAG conformance from them.
- Legal exposure: US federal website accessibility suits were 3,117 in 2025 (Seyfarth), up from 2,452 in 2024; counts including state courts exceed 5,000 (UsableNet). The European Accessibility Act applies since 28 Jun 2025 to in-scope services including e-commerce, with a microenterprise exemption for services (fewer than 10 staff and turnover or balance sheet up to EUR 2m); penalties are national. Flag for legal verification; don't give legal advice.
- Overlays: the FTC acted against accessiBe (USD 1m, 2025) over unsubstantiated claims that its tool makes sites WCAG-compliant automatically (proposed order January 2025; final date unconfirmed). Don't recommend an overlay as a fix; fix the underlying code.
- Click-Away Pound (UK; 2016: 71%, 2019: 69%; no newer edition found) is stated behavior from a survey, not a lift estimate. No controlled evidence links accessibility work to conversion or revenue. Frame accessibility as risk, legal exposure, inclusion, and addressable audience.
