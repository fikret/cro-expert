# Viability and statistics

Contents: when to test · traffic gate · calibrating expected effects · sample size · reading results · low-traffic options · what not to say

## When to test and when to ship

Ship without testing: broken UX or bugs, speed fixes, accessibility and legal fixes, removing known friction, reversible low-risk changes, changes backed by several independent evidence sources.

Test: bigger judgment calls (offer, pricing presentation, page structure, headline strategy) where the page has enough traffic to detect an effect worth caring about.

Published win rates are low, and the figure depends on domain, maturity, and who is measured: Optimizely reports about 12% of experiments winning on the primary metric (vendor, 127k tests); Microsoft reports about one third of ideas improving the target metric, and Google and Bing report 10-20% for some metrics (Kohavi et al., primary); an independent 1,001-test sample (Georgiev) found 33.5% significant wins, with a median lift of 0.08% across all tests and 7.5% among winners. Don't quote a single number as a target. Roughly two thirds or more of tests produce no win. Most small tweaks do nothing. Say so, and favor bold, evidence-backed changes over color and microcopy tweaks. Conversion counts used for the traffic gate come from analytics that may undercount, so ask for the backend count ([measurement-trust](measurement-trust.md)).

## Traffic gate

Flat rules of thumb disagree and are mostly folklore. "1,000 conversions per month" has no primary source. "~350 conversions per variation" is attributed to CXL by a vendor blog (original not verified). Do a power calculation instead.

Primary sources give no conversions-per-month threshold. Kohavi, Tang, and Xu recommend "thousands of experimental units" and say small sites should look for big effects (H). Practical guide: under roughly 100 conversions per month on the page, classic A/B testing is not viable. That gate is a judgment call, not a law. Use the low-traffic options below.

## Calibrating expected effects

Typical shipped improvements at mature sites are 0.1-2% (Kohavi et al., H). In the 1,001-test independent sample, the median lift across all tests was near 0%, and significant winners had a median of 7.5%, which overstates true effects because only significant results are selected (M-H). Small tests can only detect large effects, so a surprising 20%+ lift from a small test is more likely inflated or an artifact (Twyman's law). If 9 of 10 tests "win", suspect the process (M). Best-practice or heuristic changes are not shown to win more often than opinion-based ones in any controlled data found, and Kohavi et al. report that experts are poor at predicting winners (H); treat heuristics as hypotheses and ship only for friction and bugs. Never use these figures as forecasts.

## Sample size

Run `python3 scripts/sample_size.py BASELINE RELATIVE_LIFT [--monthly-visitors N]` (alpha 0.05 two-sided, power 0.80, normal approximation). Show the inputs in your answer. Reference outputs from the script:

| Baseline | Detect (relative) | Visitors per arm | Conversions per arm |
|---|---|---|---|
| 3% | 10% | 53,211 | about 1,600 |
| 3% | 20% | 13,914 | about 420 |
| 10% | 10% | 14,751 | about 1,480 |

So roughly 350 conversions per arm is only adequate for ~20%+ relative lifts at a ~3% baseline. These are planning numbers; sequential or Bayesian tools give different answers.

Metric choice: pick the primary metric as far down-funnel as is measurable. If only a click is measurable, label the result "click lift, unconfirmed downstream" (a Microsoft test cut clicks per user by 64% by showing price, because the remaining clickers were better qualified; Kohavi et al., KDD 2014). Extreme results trigger a check: a single test with a double- or triple-digit lift means checking tracking, SRM, and novelty before any claim (Twyman's law). If an arm was shut early or the split was uneven, say so and check SRM.

Plan before launching: one primary metric, guardrail metrics (revenue per visitor, lead quality, errors, page speed), MDE stated as relative or absolute (say which), sample size and duration fixed in advance, whole weeks (usually 2+), stopping rule named, segments pre-declared.

## Reading results

Check in this order:
1. **SRM (sample ratio mismatch)**: chi-square test of observed vs planned split. About 6% of Microsoft experiments (Fabijan et al., KDD 2019) and about 10% of LinkedIn triggered analyses show SRM (H), so check every time; a 50.2/49.8 split on about 1.6M users is already a 1-in-500,000 event. If it fails (thresholds vary; a strict one such as p < 0.001 avoids false alarms, a practitioner convention), results are invalid; find the cause (redirects, bot filtering, performance-driven exits before logging, caching, overlapping experiments, mid-test allocation changes) before reading outcomes.
2. **Duration and sample**: reached the planned sample, whole weeks, covered a business cycle.
3. **Peeking**: repeatedly checking and stopping at significance inflates false positives (Evan Miller: peeking 10 times turns a nominal 1% into roughly 5%). Bayesian methods are not immune. Use a fixed horizon or a valid sequential method.
4. **Effect with confidence interval**, not just a p-value or "chance to beat control".
5. **Novelty/primacy**: returning users react to change; check the effect over time and new vs returning. Don't ship on first-week data if the effect decays: in Dmitriev et al. (KDD 2017) a coach-mark test showed +2% clicks that vanished after first exposure (H); primacy, where effects grow over time, also exists.
6. **Multiple comparisons**: many variants, metrics, or segments inflate false positives. Name one primary metric; treat post-hoc segment cuts as hypotheses for the next test.
7. **Guardrails**: revenue, lead quality, refunds/cancellations, speed.

When the user pastes results, ask for visitors and conversions per arm, runtime, and split. Never call a winner from partial data.

## Low-traffic options

- Test bigger, bolder changes so the effect size is large.
- Use a higher-volume micro-conversion with caution about proxy validity.
- Test fewer variants (usually one challenger).
- Pre/post with a control or holdout page, or geo split, labeled directional. Pre/post alone is confounded by seasonality, campaigns, and traffic mix.
- Sequential rollout with monitoring; qualitative validation (5 users, surveys, replays).
- Accept a higher alpha (for example 10%) with explicit risk framing.
- Variance reduction with pre-experiment data (CUPED) cut variance about 50% at Bing (Deng et al., WSDM 2013, H); it needs users with pre-period history, so it helps little on mostly new-visitor landing pages (Inferred).
- Fix obvious leaks first and skip testing.

## What not to say

- Invented lifts ("will increase conversions by 30%") or sample sizes without showing inputs.
- "Statistically significant" with no sample, duration, and SRM check.
- "Best practice, so no test needed" for judgment-call changes.
