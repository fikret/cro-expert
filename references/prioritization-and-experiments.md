# Prioritization and experiments

Contents: scoring rubric · ship/test/research · hypothesis format · experiment plan · result log

## Why not plain ICE/PIE

ICE (Impact, Confidence, Ease) and PIE (Potential, Importance, Ease) use subjective 1-10 scores. Two analysts disagree, and an idea's owner inflates Confidence. PXL (CXL; verified on cxl.com 2026-10) uses binary yes/no questions: above the fold, noticeable within 5 seconds (weighted 2 or 0), adds or removes an element, runs on a high-traffic page, plus four evidence questions (user testing, qualitative feedback, mouse tracking or eye tracking, digital analytics) and ease of implementation bracketed by estimated dev time. Ideas from opinion score lower. CXL says PXL is meant to be customized (for example add "doesn't interfere with SEO") and that a high score does not predict a win; it only ranks which hypotheses to test first. There is no independent evidence PXL is more reproducible, so treat the scores as ordering aids, not forecasts.

## Scoring rubric (fill per idea)

Score 0 or 1. Each "1" needs a one-line reason that cites specific evidence; unsupported means 0.

| Criterion | 1 if... |
|---|---|
| Above the fold / noticeable in ~5 seconds (weight 2) | The change is seen without scrolling or effort |
| Adds or removes an element (not a tweak) | Substantive change |
| High-traffic page | Reaches a large share of the funnel |
| Backed by analytics | Funnel or segment data shows the problem |
| Backed by qualitative evidence | Survey, interview, support tickets, reviews |
| Backed by behavior evidence | Replays, heatmaps, usability tests |
| Addresses a known blocker (bug, speed, accessibility, legal) | Yes |

Then add:
- **Evidence tier**: 3 = quantitative and qualitative converge; 2 = one data source; 1 = heuristic only; 0 = opinion.
- **Reach**: monthly users who see the element.
- **Effort**: dev-days or hours.
- **Testability**: can it reach the needed sample in 4-6 weeks? If not, flag **ship, don't test**.

Rank by weighted PXL total, break ties with reach divided by effort. Show the table.

## Ship / test / research

| Decision | When |
|---|---|
| Ship | Bug, speed, accessibility, legal, strong multi-source friction fix, easy to reverse |
| Test | Judgment call, enough traffic, measurable primary metric |
| Research | Cause is unknown; need replays, survey, interviews, or tracking fix first |

## Hypothesis format

"Because [evidence], we believe [change] for [segment/page] will [behavioral outcome], measured by [primary metric]. We will know we're wrong if [falsifier]."

Require: evidence source, segment, single primary metric, minimum detectable effect, guardrail metrics, falsifiable prediction.

## Experiment plan fields

ID, owner, date · page/URL, device scope, audience, split · variants (screenshots) · primary metric (exact event definition and unit) · secondary metrics · guardrails (revenue per visitor, lead quality, error rate, page speed, refunds/cancellations, support tickets) · baseline · MDE (relative and absolute) · alpha, power · required sample per arm · duration in whole weeks · stopping rule · QA (flicker, tracking, cross-browser, SRM check) · analysis plan with pre-declared segments · decision rule (ship, iterate, kill thresholds).

## Result log

Dates · visitors and conversions per arm · SRM p-value · effect with CI · guardrail results · segment notes (labeled exploratory) · novelty check · decision · learnings · follow-up ideas. Log losers and inconclusive tests too; they stop the team repeating them.

For experiment program design, test calendars, and statistics depth, hand off to **ab-testing**.
