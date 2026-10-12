# Measurement trust

Run this before any funnel diagnosis, benchmark comparison, or test readout. Output one of: ✅ **Trusted**, ⚠️ **Trusted with caveats** (list them), or ⛔ **Not trusted**. A "Not trusted" item becomes finding #1.

Analytics undercounts and is biased in ways nobody can quantify for you. Vendor blogs claim GA4 misses 10-30% of orders compared with the backend, but no independent study was found (L). Measure the user's own gap; never quote a gap or a recovery percentage as fact for their site.

## Checklist

1. **Reconcile with the source of truth.** Compare analytics purchases or leads against the order system, CRM, or payment processor for the same dates and timezone, and state the ratio. A gap above about 10% (a judgment threshold, not a standard) means investigate before analysis. The conversion counts used for the traffic gate should come from the backend if possible.
2. **Visitors the tool cannot see.** Some visitors are never counted (for example when a cookie banner blocks the counter). Ask whether the numbers look lower than the real orders or leads, and whether the gap differs by device or country. Do not comment on whether the banner itself is lawful; that is out of scope.
3. **Blocking and browsers.** Segment by browser (Safari and Firefox vs Chrome). About 30% of internet users report using an ad blocker at least sometimes (GWI 2025, M), but the share of this site's sessions blocked is unknown.
4. **Duplicates and missing events.** The purchase event fires once per order; thank-you page reloads; payment redirects and wallet flows (Shop Pay, Apple Pay, 3-D Secure, separate checkout domain) don't drop the session or referrer; cross-domain linking works; payment gateways and self-referrals are excluded from referral reports.
5. **Bots and internal traffic.** Automated traffic is about 51-53% of web traffic in Imperva telemetry (vendor, includes good bots; M), though analytics filters known bots. Check spikes with 100% bounce, one city or ISP, identical user agents, or zero-second sessions. Exclude internal and agency traffic.
6. **GA4 limits.** Explorations sample above standard limits, data thresholds can hide small segments, and the data-quality icon matters. Report counts with rates.
7. **Event definitions.** Is the primary conversion the real outcome (qualified lead, paid order), not a click or thank-you view? Is the definition the same in analytics, the A/B tool, and the ad platforms?
8. **Attribution.** Compare the same model and lookback across tools. Ad platforms and GA4 disagree by design.
9. **A/B tool QA before reading a result.** Run an SRM chi-square on planned vs actual split with a strict alpha (such as 0.001). SRM affects roughly 6-10% of experiments (Microsoft, LinkedIn; secondary citations, M), so check every time. Typical causes: bot filtering, redirects, flicker timeouts, caching, slow variants losing logged events, overlapping experiments. Run an A/A check or QA each variant on mobile, desktop, and each major browser; confirm the goal fires in every variant; check revenue outliers.
10. **Server-side tagging** can recover some blocked or short-lived-cookie traffic, but published recovery figures (10-30%, one 46% case) are agency or vendor claims.

iOS privacy impact: no sourced numbers were found; don't add any.
