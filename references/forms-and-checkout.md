# Forms and checkout

Contents: lead forms · field rules · field-by-field · layout and flow · submit button and post-submit · form types · errors and validation · cart and checkout · measurement

Evidence comes mainly from Baymard's moderated usability research on large ecommerce sites (US/EU), plus NN/g qualitative studies. It describes usability problems found, share-of-sites benchmarks, and self-reported surveys, not A/B-measured lifts. Baymard pages sometimes disagree with each other; cite the page and date. "Fewer fields" is a heuristic to test, not a law; one vendor claim of "+120% from 11 to 4 fields" has no clear methodology.

## Lead and contact forms

- Ask only for what you use to qualify or route. Every field needs a job. Move the rest to progressive profiling or the follow-up.
- Phone: over 70% of users are reluctant to give it (Baymard), and 49% of sites don't explain why it is asked. Make it optional or explain the benefit ("only to confirm the appointment").
- State what happens next and when ("we reply within 1 working hour").
- Put proof (a quote, a rating, a logo) beside the form, and a privacy reassurance if data is sensitive.
- Separate intents (sales, support, press) so one form doesn't serve three.
- Consider lead quality: shorter forms raise volume but can lower downstream conversion. Track form submit to qualified lead, not submissions alone.
- For multi-step forms, ask the easiest question first, show progress, keep 3-5 fields per step on mobile.

## Field rules (Baymard)

- Mark required fields clearly (asterisk before the label; NN/g 2019). When only optional fields were marked, 32% of participants missed a required field; 61% of sites mark both poorly. Poor optional-input interfaces (32% of sites) made participants 5-30% slower per checkout step.
- Hide "Address line 2" behind a link (only about 20% of benchmarked sites do).
- Labels above fields, visible after typing; no placeholder-only labels (NN/g 2014).
- Correct `type`, `inputmode`, and `autocomplete` tokens; 16px+ font to avoid iOS zoom; address autocomplete.
- Avoid overly complex password rules (65% of sites have them; sign-in trouble causes up to 19% abandonment among existing users).

## Field-by-field

- **Email**: one field, no confirmation field; inline validation; typo hint (gmail.com); email keyboard on mobile.
- **Name**: one "Name" field vs. first/last is a test candidate; split only when personalization needs it.
- **Phone**: optional if possible; if required, say why; format as typed; handle country codes (important for Turkish and international leads).
- **Company**: auto-suggest or enrich after submit instead of asking; or infer from the email domain.
- **Role/title**: dropdown if categories drive routing, free text otherwise; consider optional.
- **Message/free text**: optional, expands on focus, with a short hint of what helps.
- **Dropdowns**: "Select one..." placeholder; searchable if long; radio buttons under about 5 options; "Other" with a text field.
- **Checkboxes**: clear parallel labels; a sensible number of options; say "select all that apply" when true.

## Layout and flow

- Field order: easiest first (name, email), build commitment, sensitive fields last.
- Single column wins on mobile and for completion; two columns only for short related pairs (first/last name).
- Labels visible above fields; placeholders show examples, not labels; help text only when it helps.
- Multi-step when there are more than about 5-6 fields, distinct sections, or conditional paths: progress indicator, one topic per step, back navigation, saved progress, easy fields first. Multi-step reduces perceived complexity but adds interaction cost and isn't easily interruptible; show all steps, use descriptive buttons, allow save and resume (NN/g 2017). No study shows multi-step raises conversion, so treat it as a test candidate.
- Progressive commitment: low-friction start, then detail, then qualifying questions, then contact preferences.
- Mobile: tap targets 44px+, sticky or clearly visible submit, minimal typing.

## Submit button and post-submit

- Button copy: [action] + [what they get] ("Get my free quote", "Request demo", "Send message"). Avoid "Submit". Don't imply payment if none happens.
- Place it right after the last field, aligned with the fields, high contrast.
- States: loading (disable the button, show progress), success (what happens next, who contacts you, when, plus an alternative channel such as WhatsApp), error (clear message, focus on the first problem).
- Success state is part of conversion: track it and make sure the conversion event fires only on real success.

## Form types

- **Lead capture (gated content)**: minimum fields, often email only; clear value above the form; ask enrichment questions after the download.
- **Contact form**: name or email plus message; phone optional; response-time expectation; alternatives (chat, phone, WhatsApp).
- **Demo request**: name, work email, company; phone optional with a preferred-contact choice; use-case question helps routing; calendar embed can raise show rate. When enrichment decides the next step, keep valid submissions, bound the lookup wait, and give a fallback if qualification is unknown (see **revops** for inbound routing).
- **Quote or estimate**: multi-step with easy questions first; technical detail later; save progress.
- **Application form**: explain why each answer is needed and what happens after; stay short.
- **Survey**: progress indicator, skip logic, one question per screen when long.

## Errors and validation

- Inline validation after the field is left or at the correct length, not while typing; clear the error as soon as the input is fixed; show positive checkmarks. About 31-32% of sites had none (Baymard pages differ slightly).
- Say what is wrong and how to fix it, next to the field. About 94% of sites lack adaptive, specific error messages (Baymard 2024-25; other pages say 93-98%), so generic "Invalid [field]" is the norm to beat. Never wipe the form on error.
- Preserve entered data on back, refresh, and failed payment.

## Cart and checkout

Baymard figures (cart abandonment list, updated Sept 2025, 70.22% average across 50 studies; 42% of US abandoners were "just browsing", so not all of it is recoverable). Reasons among the rest: extra costs 40%, slow delivery 20%, distrust of card entry 19%, account required 18%, too long or complicated 17%, errors or crashes 17%, returns policy 13%, couldn't see total upfront 12%, card declined 10%, too few payment methods 9%. Multi-select; sample size not stated. Baymard's other pages quote slightly different figures (for example 39% extra costs), so treat these as plus or minus a few points.

Checklist, in order:
1. **Total cost early**: shipping, tax, and fees visible before checkout; estimate in the cart. Mandatory fees belong in the headline price where the law requires it (UK CMA fined StubHub for drip pricing; [regulation-and-dark-patterns](regulation-and-dark-patterns.md)). Delivery and returns on the page: 48% of sites don't show delivery dates, 44% lack returns info on the PDP, 67% lack a total-cost estimate (Baymard 2026); 60% of respondents (n=1,032) look for returns info on the PDP.
2. **Guest checkout** shown most prominently (62% of sites don't; in a survey of 1,026 US adults 18-19% abandoned to avoid creating an account); offer account creation after purchase.
3. **Form size**: Baymard's June 2024 benchmark puts the average checkout at 5.1 steps and 11.3 form fields (11.8 in 2021, 12.7 in 2019) and says most sites need about 8. Older material quotes 23.48 default elements vs an ideal 12, and a 2026 guide says 19.9 vs 12; the metrics are undefined and inconsistent, so cite the direction (cut unneeded fields), not a precise count.
4. **Payment options**: wallets (Apple/Google Pay), local methods, installments where relevant. Surface express buttons in the cart as well as checkout. Realistic effect size is unknown: Shopify's published case shows about +1.6% store-wide orders (+4.1% only for returning Shop Pay users); agency claims of +35% are single-merchant 2-week tests. Ship if missing; measure purchase conversion and revenue per visitor.
5. **Trust at payment**: accepted payments, return policy, support contact, security cues. 19% abandoned from card distrust (n=1,026, 2025). Visually set off the card fields and put one or two icons inside; any visible seal beats none and the brand of seal matters little (self-reported 2023 study). Badge preference surveys overstate behavioral effect; don't promise lift from a seal.
6. **Order summary** always visible; promo code field collapsed behind a link to avoid coupon hunting. GoodUI's 10 tests give a median +0.8% sales and a non-significant pooled +0.5%, so this is low priority and low risk; don't remove the field entirely if coupons drive traffic you want.
7. **Error recovery**: card decline messaging with retry and alternative payment; 3-D Secure failures with a fallback.
8. **Cart persistence** and recovery (email, SMS, WhatsApp). On mobile, the cart is often a wishlist; support saving items.

Failures: forced registration; surprise fees at the last step; ambiguous labels; no autofill; generic errors; distracting header and nav; no express checkout.

## Measurement

Track: form view, first field interaction, each step, submit, validation errors per field, payment errors, abandonment by device. Field-level error rates point to the exact friction. If events are missing, that comes first, and validate the numbers with [measurement-trust](measurement-trust.md).

For cart and checkout recovery emails, SMS, and wallets, report revenue per visitor and orders against a holdout; platform-attributed "recovered revenue" overstates incrementality (a Klaviyo holdout found no detectable effect on existing customers).

Hand-offs: account creation and signup flows go to **signup**; popup forms go to **popups**.
