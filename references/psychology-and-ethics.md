# Psychology and ethics

Contents: LIFT · Fogg · Cialdini · information scent · trust and social proof · popups · AI copy · dark patterns and legal limits · common myths

These are lenses for generating hypotheses, not evidence of effect sizes.

## LIFT (WiderFunnel, Chris Goward)

Value proposition is central: perceived benefits minus the costs of taking the action. Drivers: relevance, clarity, urgency. Inhibitors: anxiety, distraction. Use it to ask: is the promise relevant to this visitor, clear at a glance, timely, and free of fear and noise?

CXL's heuristic lens is similar: relevancy, clarity, value, friction, distraction. CXL itself says heuristic findings are "areas of interest" to validate with research, not truths.

## Fogg Behavior Model (B = MAP)

Behavior happens when motivation, ability, and a prompt converge at the same moment. Missing any one means no action.

CRO mapping: motivation = offer, value proposition, urgency; ability = form length, clarity, steps, load speed (time, money, physical and mental effort); prompt = CTA visibility and timing. Raising ability (cutting friction) is the more reliable lever than raising motivation. It is a conceptual model, not a validated predictor of web lift.

## Cialdini, applied honestly

Reciprocity, commitment and consistency, social proof, authority, liking, scarcity, unity. Social proof works best when the reference group resembles the visitor ("customers like you", same industry or city). Use only what is true: real counts, real reviews, real deadlines, real stock. Scarcity and social-proof tactics are legally regulated; see below.

## Information scent

Visitors follow links and headings by estimating how likely each will answer their question and how long it will take (Pirolli and Card; NN/g). Message match between an ad, query, or link and the landing page rests on this principle; no controlled study of ad-to-page message match was found, so don't cite a lift for it.

## Trust and social proof

NN/g qualitative findings (2016, 2019; small samples): users distrust curated on-site testimonials and trust external reviews more; testimonials with job title or affiliation get attention; testimonials that begin with doubt and end in confidence persuaded B2B participants. No conversion data, so test them. Low engagement counts (a few shares) can signal unpopularity (2014). NN/g's four trust factors: design quality, up-front disclosure, comprehensive and current content, and connection to the rest of the web.

## Popups

NN/g (2019; observational, no conversion data): avoid popups before content, delay email capture to a natural moment, show one at a time, never block article content, avoid modal cookie notices. Mind Google's intrusive-interstitial rules on mobile. Hand off popup design to **popups**.

## AI-written copy

No controlled test of AI-written vs human-written copy was found; surveys show lower stated trust when AI content is noticed. Audit generic signals as Inferred and recommend specificity and verifiable proof. Details in [ai-era-cro](ai-era-cro.md).

## Dark patterns and legal limits

Not legal advice. The rules changed in 2024-2026 and differ by jurisdiction; the sources, dates, and confidence tags are in [regulation-and-dark-patterns](regulation-and-dark-patterns.md). Say "verify with counsel" wherever the law is unsettled.

What is law now (as of 2026-10):
- **US:** the FTC Fake Reviews rule is in force (since 21 Oct 2024). The FTC Fees rule covers only live-event tickets and short-term lodging. The "click-to-cancel" rule was vacated in July 2025 and is not in force; cancellation and enrollment are still enforced under ROSCA and FTC Act s.5 (Amazon Prime settlement, Sep 2025). The 2022 dark-patterns report is staff guidance, not a rule.
- **UK:** the DMCC regime has applied since 6 Apr 2025 and the CMA can fine up to 10% of turnover. Fake reviews are banned. The CMA fined StubHub (drip pricing) and Marks Electrical (pre-ticked paid add-ons); Emma Sleep admitted misleading countdown timers, "high demand" messages, and discount claims. The subscription regime is not in force yet.
- **EU:** the UCPD blacklists false limited-time or limited-stock claims and fake reviews; the 30-day lowest-price rule for price cuts has applied since 28 May 2022; the Digital Fairness Act is not yet proposed.
- **Turkey:** advertising claims fall under Law 6502 and the advertising Yönetmelik (30-day lowest-price rule for discounts, per a 2022 amendment). No rule specifically banning countdown timers or stock counters was found, so treat them under the misleading-advertising rule.

Never recommend: fake timers, invented stock or viewer counts, fabricated or purchased reviews, hidden mandatory costs revealed late, pre-ticked paid add-ons, confirm-shaming, hard-to-cancel flows, "was" prices that were not actually charged. When a user already has such elements, flag the trust and legal risk plainly and say which jurisdiction's rule applies to their audience.

Urgency can also backfire: a countdown timer lowered email and SMS opt-ins in one vendor popup test (no numbers, L), and a UK Which? spot check found 5 of 10 "only X left" claims inaccurate (spot check, not a study).

## Common myths

- **Button color**: the often-cited red-over-green result is better explained by contrast and isolation than by hue. No universal best color.
- **"Above the fold is everything"** and **"nobody scrolls"**: both wrong. NN/g (2018; n=120, 130,000+ fixations) found 57% of viewing time above the fold (down from 80% in 2010, on different screen sizes, so the comparison is directional), 74% in the first two screens, and about 81% in the first three. Attention is front-loaded, but people scroll if the top gives them a reason.
- **Long vs short pages**: no NN/g study compares them. Length matters less than scent and ordering; high-commitment offers usually need more content. Don't cite a universal answer.
- **F-pattern**: NN/g (2017, revisited 2026) calls it a default when text has no strong cues, bad for users and businesses, and not a layout to aim for; other patterns (layer-cake, spotted) also occur. Design for scanning: informative first words, structure, headings.
- **"Readable in 5 seconds"**: a 5-second test measures first impression (NN/g). The NN/g attention figure is that the first 10 seconds decide whether visitors stay, and a clear value proposition keeps them longer (2011, from older Microsoft Research dwell-time data).
- **Fewer form fields is always better**: a heuristic to test; weigh lead quality.
- **Carousels**: the evidence is a single-participant NN/g observation (2013) that the offer was visible about 20% of the time and moving content read as ads. No carousel click-through rate was verified.
