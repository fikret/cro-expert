# Diagnosis playbook

Contents: evidence labels · research order (ResearchXL) · auditing from a URL or screenshot · severity scale · funnel diagnosis · replays and heatmaps · qualitative research · voice-of-customer coding

## Research order (CXL ResearchXL, verified on cxl.com 2026-10)

Eight steps, then a master sheet of issues turned into test hypotheses. Triangulate: an issue seen in two or more methods outranks a single-source issue.
1. **Technical analysis**: cross-browser and cross-device testing, conversion rate by device and browser, speed. CXL's rule: fix technical problems before anything else; bugs are the main conversion killer. Cost a bug by multiplying the affected visitors' missed conversions by order value and comparing with fix time.
2. **Heuristic analysis**: relevancy, clarity, value, friction, distraction. Outputs are "areas of interest" to validate, not truths.
3. **Web analytics**: health check first (is everything measured and accurate; see [measurement-trust](measurement-trust.md)), KPIs, leaks.
4. **Mouse tracking**: heatmaps, scroll maps, session replays.
5. **Qualitative surveys**: customer surveys, on-site surveys, chat logs, interviews.
6. **User testing**: usability and clarity problems.
7. **Copy testing**: put the copy in front of the audience (15-20 interviews, or a copy-testing panel) and ask what the headline makes them feel, which benefits matter, what is unclear.
8. **Sum-up**: categorize, prioritize, and turn each issue into a hypothesis.

With only a URL you can do step 2 and parts of 1. Say which steps were not done.

## Evidence labels

| Tag | Meaning | Example |
|---|---|---|
| 👁️ **Observed** | A fact in the artifact you can point to | "The form has 9 fields, phone is required" |
| 🧠 **Inferred** | Heuristic judgment about behavior; a hypothesis | "The 9 fields likely suppress submissions on mobile" |
| ❓ **Needs data** | Cannot be known without analytics or research | "Which step users abandon" |

Directly observable (state as fact): copy present or absent, CTA count and labels, field count, layout position, contrast ratio, missing alt text, visible load issues, claims made in text.

Always a hypothesis: user behavior or motivation, where drop-off happens, "this causes low conversion", which fix will work, traffic-source fit, mobile behavior from a desktop screenshot, anything below the fold in a single screenshot, competitor conversion rates, anything depending on audience, offer, or traffic quality.

A heuristic audit cannot separate page problems from traffic quality, offer, pricing, or tracking faults. State this once, briefly, and list what would settle it.

Evidence strength, strongest first: randomized test (the only causal evidence) > observed behavior (analytics, recordings, usability tests) > stated opinion (surveys, interviews) > expert heuristic > taste. Issues found by two or more independent methods outrank single-source issues. (This ordering is a defensible convention, not an empirically established hierarchy.)

## Auditing from a URL or screenshot

Evaluate with the dimensions in SKILL.md Step 5. For each issue record: location, observation, heuristic violated, severity 0-4, evidence tag, suggested fix, how to validate.

Heuristic lens (LIFT-style): value proposition at the center; relevance, clarity, urgency drive; anxiety and distraction inhibit. It is a way to find problem areas, not proof of lift.

A single agent pass equals one evaluator, and single-evaluator severity ratings are unreliable (NN/g suggests about three evaluators for practical reliability). Say so and give a confidence rating next to severity.

Check what you actually fetched: JS-rendered, personalized, geo-specific, or A/B-varied content may differ. Ask for mobile and desktop screenshots of the full page when judging layout.

## Severity scale (NN/g, 0-4)

0 not a problem · 1 cosmetic · 2 minor · 3 major, high priority · 4 catastrophe. Judge each issue on frequency (how many users meet it), impact (how hard to overcome), and persistence (one-time or repeated); these are rating factors, not a formula to multiply. Consider market impact too. Heuristic evaluation uses 3-5 evaluators and the mean rating of about three is considered reasonably reliable (NN/g).

## Funnel diagnosis (when analytics exist)

1. Define the macro conversion and micro-steps (landing > key page > form start > submit; or PDP > add to cart > checkout start > purchase).
2. **Validate tracking first** with the checklist in [measurement-trust](measurement-trust.md): reconcile with the backend, duplicates, cross-domain, bots, self-referrals. Surprising numbers are usually wrong (Twyman's law).
3. Find the biggest absolute loss weighted by volume, not only the lowest percentage.
4. Segment: device category, source/medium/campaign, new vs returning, country, landing page, browser and OS (browser-specific bugs are common).
5. Watch for mix shift (Simpson's paradox) when comparing periods or segments; compare like seasons.
6. Report counts with rates; small segments are noisy, and GA4 thresholding or sampling can hide them.
7. Form one hypothesis per leaking step, then use qualitative tools to explain WHY. Analytics says where; qualitative says why.
8. Organic traffic loss with stable rankings: check Search Console impressions vs clicks and whether AI Overviews appear for the query set. The remaining traffic is more bottom-funnel, so conversion rate can move with no page change; compare by landing-intent segment before blaming the page ([ai-era-cro](ai-era-cro.md)).

Closed funnels (GA4 default) drop users who skip steps; open funnels let users enter anywhere. Up to four segments can be compared side by side.

## Replays and heatmaps (Clarity, Hotjar)

- Dead clicks (no response) and rage clicks (rapid repeats) point to broken or misleading elements, slow response, or things that look clickable.
- Pitfalls: more clicks does not mean good; the snapshot may differ from what users saw (dynamic content, variants, popups); analyze mobile and desktop separately; high-traffic data may be sampled; there is no reliable minimum sample to quote, so say low-sample maps are noise.
- Confirm any heatmap signal by watching a set of replays from the relevant segment. Tally patterns (n of N sessions) instead of narrating a dramatic one. Filter by segment and outcome to avoid survivorship.

## Qualitative research

- **Usability tests**: 5 users per round for qualitative problem discovery, then fix and re-test. NN/g's basis is that one user finds about 31% of problems and five find about 85% (Nielsen, 2000); it recommends three rounds of 5 over one round of 15. Quantitative studies need at least 20 users, and about 3-4 per distinct audience group (2012). Five users find problems; they don't measure conversion.
- **On-site surveys**: "What almost stopped you?", "What were you looking for?".
- **Post-purchase surveys**: "What nearly made you not buy?", "What else did you consider?".
- **Interviews**: recent buyers and recent non-converters.
- **Sources already available**: own reviews, G2/Trustpilot/app stores, Reddit, support tickets, sales-call notes.

## Voice-of-customer coding

When the user pastes reviews or tickets: tag each by theme (desired outcome, anxiety, objection, alternative considered, trigger event), count frequency, keep exact phrases for copy. Report counts, not impressions. Never fabricate quotes; mark where each quote came from.
