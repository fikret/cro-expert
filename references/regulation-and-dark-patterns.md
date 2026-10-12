# Regulation and dark patterns

Contents: how to use · auditor checklist · US · EU · UK · Turkey · pipeline (not yet law) · open items

**Out of scope: personal-data and privacy law (KVKK, GDPR, cookie and consent banners, aydınlatma metni, İYS).** Do not audit, raise, or recommend anything about them; if the user asks, say this skill does not cover them and suggest a privacy specialist. Not legal advice. Last verified 2026-10-12. Confidence: **H** regulator or legislation text opened; **M** reputable secondary summary; **L** news, blog, or background knowledge not re-verified. State the tag and the date when you cite a rule, and say "verify with counsel" wherever the law is unsettled. Never state that a rule is in force without a source tag. Re-verify the pipeline rows before relying on them.

## Auditor checklist (apply per page; mark Observed or Needs data)

**Price display**
- Mandatory fees, shipping, VAT (KDV), and installment surcharges appear in or next to the headline price before checkout. "KDV dahil/hariç" explicit in Turkey.
- "From" and "up to" prices state what the typical buyer pays.
- Strike-through, "eski fiyat", and "%X indirim": the reference is the lowest price of the previous 30 days (EU Art. 6a; Turkey per the Feb 2022 amendment) and a price history exists to prove it. Never show a "was" price that was not actually charged.

**Countdowns, deadlines, and counts**
- Countdowns tie to a real server-side end date, don't reset on reload or per visitor, and the offer really ends.
- Deadline CTAs ("Son gün", "12 Ekim") are consistent across the page and not already past.
- "Son N ürün/kontenjan" and "N kişi bakıyor" come from live data; no random or hardcoded numbers. Cohort seats on training pages need one source of truth.

**Reviews and testimonials**
- Real buyers, no purchased or AI-fabricated reviews, incentives disclosed, negatives not suppressed, aggregate ratings calculated honestly.
- Testimonials have real names, permission, and real outcomes; influencer or partner content is labelled as advertising (Reklam/İş birliği in Turkey, #ad in US/UK).
- Never write placeholder testimonials or review counts that could be published.

**Cancellation and subscriptions**
- Online sign-up has equally easy online cancel; price, renewal date, and cancel route stated before checkout; free-trial terms show the post-trial price at the point of consent; no guilt-tripping on cancel.

**Installments (taksit)**
- "N taksit" matches the actual gateway or POS agreement and the banks shown; "faizsiz" claims verified; installment and cash prices both shown.

**Refund and withdrawal**
- Standard distance sales: 14-day cayma stated in the ön bilgilendirme form, return carrier named (Turkey from 1 Jan 2026). No blanket "iade yok" that overrides statutory rights.
- Online training, courses, workshops, digital content: do not assert "cayma hakkı yoktur" unless a specific exception applies, the consent mechanism is built into checkout (separate, timestamped), and counsel has signed off.
- Money-back guarantees are described as separate from statutory rights.

**Checkout**
- The order button states the payment obligation. Pre-selected paid add-ons are off by default.

**Accessibility**
- EU-facing e-commerce: keyboard-operable checkout, labelled forms, accessible errors (European Accessibility Act from 28 Jun 2025; microenterprise exemption for services).

## United States

| Rule | Status (2026-10-12) | Page implication | Conf. |
|---|---|---|---|
| FTC Fees rule, 16 CFR 464 | Effective 12 May 2025. Covers only live-event tickets and short-term lodging. | Total price in advertised price for those sectors. Elsewhere drip pricing is still attackable under FTC Act s.5 and state law. | H text |
| FTC Fake Reviews rule, 16 CFR 465 | In force since 21 Oct 2024. | Bans fake or AI-generated reviews, buying sentiment, undisclosed insider reviews, review-suppression threats, fake followers. | H text |
| FTC "click-to-cancel" Negative Option rule | 2024 amendments vacated by the 8th Circuit on 8 Jul 2025; FTC opened a new rulemaking (ANPRM 11 Mar 2026). No NPRM found. | No federal click-to-cancel rule in force. ROSCA and FTC Act s.5 still apply (Amazon Prime settlement 25 Sep 2025, $2.5B). | H (ANPRM), M (vacatur) |
| FTC "Bringing Dark Patterns to Light" (2022) | Staff report, not law. | Taxonomy: false urgency, fake countdowns, hidden fees, cancel obstruction, confirmshaming, pre-checked boxes, fake social proof. Liability follows net impression. | H existence |

## European Union

| Rule | Status | Page implication | Conf. |
|---|---|---|---|
| UCPD 2005/29/EC Annex I and Omnibus 2019/2161 | Omnibus applied from 28 May 2022. | False limited-time or limited-stock claims and fake reviews are blacklisted per se. | M |
| Price Indication Directive Art. 6a | From 28 May 2022. | Price cuts reference the lowest price of the previous 30 days. | M |
| Consumer Rights Directive 2011/83/EU | In force. | 14-day withdrawal; digital content and services exception needs express consent and acknowledgement; order button must state payment obligation (Art. 8(2)). | L |
| DSA Art. 25 | Applies to online platforms from 17 Feb 2024. | Platforms, not ordinary single-brand shops. | L |
| European Accessibility Act | Applies from 28 Jun 2025. | E-commerce services in scope; microenterprise exemption for services (verify). | M |

## United Kingdom

| Rule | Status | Page implication | Conf. |
|---|---|---|---|
| DMCC Act 2024, consumer provisions | In force from 6 Apr 2025; CMA can fine up to 10% of global turnover. Sched. 20 para 13 bans fake or undisclosed-incentive reviews. | Review collection and display. Drip pricing is enforced as misleading action or omission. | H (para 13) |
| CMA enforcement | StubHub GBP 889,200 (drip pricing); Marks Electrical GBP 720,000 (pre-ticked paid add-ons); AA settled April 2026 (amounts conflict, don't quote). | Mandatory fees in the headline price; no pre-selected paid extras. | M |
| CMA v Emma Sleep | Court-confirmed settlement 22 May 2026; judgment 30 Jul 2026 on admitted breaches. | Countdown timers, "high demand" messages, and discount claims must be true. | H (CMA page) |
| Subscription contracts regime | Not in force; expected spring 2027. | Pipeline: design to the standard, don't call it law. | M |

## Turkey

| Rule | Status | Page implication | Conf. |
|---|---|---|---|
| Law 6502 and Mesafeli Sözleşmeler Yönetmeliği | In force; fines revalued yearly (don't quote amounts). | 14-day cayma, ön bilgilendirme, mesafeli satış sözleşmesi. | L-M (text not opened) |
| 24 May 2025 amendment (RG 32909), effective 1 Jan 2026 | Ön bilgilendirme must name the seller-designated return carrier; the consumer isn't charged return shipping when that carrier is used. | Return policy and pre-info text. "İade kargo bedeli alıcıya aittir" is risky. | M, verify |
| Cayma exceptions, Yönetmelik m.15(1) | No separate "eğitim" exception. Relevant: (ğ) electronically instant-performed services and instantly delivered intangible goods, (h) services begun with the consumer's consent before the cayma period ends (seller must prove consent), (g) dated recreation or entertainment services. | Whether a given course or live workshop qualifies is unsettled. Don't tell users "no refund" copy is lawful. | L-M, verify with counsel |
| Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği m.14 (Feb 2022 amendment) | Discount reference = lowest price in the previous 30 days; burden of proof on the advertiser. | Strike-through prices and "%X indirim" claims. | M-L, verify |
| Misleading advertising (6502 m.61-62) | No rule specifically banning countdown timers or stock counters found; no dedicated fake-review rule found. | Treat timers, stock counters, and fake reviews under the misleading-advertising rule. | L |
| Reklam Kurulu and influencers | Fines on influencers reported (news, not official). | Label paid endorsements and testimonials as advertising. | L |

## Pipeline (not law yet)

EU Digital Fairness Act (proposal targeted Q4 2026, adoption realistically 2027+); UK subscription regime (spring 2027); a possible new US negative-option rule; Turkish Danıştay challenges to some cayma exceptions (unverified).

## Open items

Whether the FTC issued an NPRM after the March 2026 ANPRM; DSA Art. 25 and CRD Art. 8(2) verbatim text; current consolidated Turkish Yönetmelik texts and 2026 fine amounts; BDDK installment limits by category; online review-manipulation rules in Turkey.
