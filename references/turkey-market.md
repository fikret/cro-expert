# Turkey market

Contents: payments · installments · payment rails · trust and legal · WhatsApp · lead response speed · copy conventions · gaps

Payment, card, and e-commerce volume figures below come from Ticaret Bakanlığı, BKM, and TÜİK (H/M). Installment-by-basket data comes from iyzico merchants (M). Everything on UX, copy, WhatsApp practice is convention (L). Legal rows are tagged in [regulation-and-dark-patterns](regulation-and-dark-patterns.md) and need verification with counsel. No published Turkish brand experiment with a disclosed method was found (searched Trendyol, Hepsiburada, n11, Getir, Boyner); Hepsiburada's 2017 Optimizely redesign case (+22% conversion, vendor-published, new site initially lost) is the only datapoint [L].

## Payments

- Ticaret Bakanlığı 2025 report (12 May 2026): cards 62.5%, havale/EFT 29.2%, kapıda ödeme 3.5%, other 4.8%; 64.1% of card payments went through 3-D Secure [H]. The scope includes services and B2B, and whether shares are by count or value isn't stated. An older blog-reported 90.6% card share (KPMG/ideasoft) couldn't be verified and conflicts with this; don't cite it.
- Bank transfer is a material share, so keep havale/EFT with a clear IBAN and confirmation flow for higher-ticket and consulting sales. COD adds return and fraud risk. Check the shop's own data.
- iyzico and PayTR are common SMB gateways (hosted or iFrame, installment tables, 3-D Secure). No conversion data found [L].
- Audit points: 3-D Secure SMS failures, bank decline messages with retry and an alternative payment, BIN-based installment display, wallets where supported.

## Installments (taksit)

- BKM-based GÖSAŞ 2025 analysis (16 Jan 2026): 34.4% of credit-card e-commerce spend was installment [M]. Another reported 57.8% has an unclear denominator; don't quote it.
- iyzico 2025 data [M, iyzico merchants only]: baskets under 2,500 TL are 98.9% single payment; above 10,000 TL most card transactions are installments (20,000 TL and up: 66.5% installment, 24.2% at 7 or more). The average education-category basket is 4,510 TL. So installments matter for course prices above roughly 5,000 TL; verify on the client's own gateway data.
- Practitioner convention [L]: show "N taksitle aylık X TL" on the PDP, cart, and sales page for higher-ticket items, with a bank-specific table and clear "taksit" vs "peşin" prices. Make sure the displayed plan matches the actual POS or gateway agreement. BDDK restricts installments for some categories (confirm education and services terms with the bank or POS agreement).
- Trendyol's +11% conversion / +21% order value with Tabby pay-in-4 is a Middle East launch case (vendor page, no control, undated); it isn't evidence for Turkish taksit display. No controlled Turkish taksit-display test was found.

## Payment rails and market context

Troy had about 90M cards and 25.3% of card spend in 2025; TR Karekod works on 95% of POS terminals; internet payments were 30% of card payments (7.3 trillion TL) [H, BKM 2025 annual report]. TÜİK 2026: 60% of individuals bought online (55.7% in 2025); WhatsApp is used by 90% of internet users [M, via press]. ideasoft platform data: about two thirds of orders on mobile (64.8%) [M-]. Papara, Apple Pay, FAST, and BNPL adoption: no verified data; don't assert wallet or BNPL lift. Unsourced blog numbers on Turkish conversion rate (1.8-2.5%) or mobile abandonment (78%) are not reliable.

## Trust and legal

- Visible company info (unvan, MERSIS or vergi no, address, phone), return policy, delivery cost and time on the PDP, "güvenli ödeme" marks [L, vendor guidance]. Hidden shipping cost matches Baymard's top abandonment reason [M].
- Consumer-law items belong in checkout: mesafeli satış sözleşmesi, ön bilgilendirme formu, cayma hakkı text. From 1 Jan 2026 the ön bilgilendirme must name the seller-designated return carrier, and the consumer can't be charged return shipping when that carrier is used (RG 24 May 2025, no. 32909) [M, verify]. Discount and "önceki fiyat" claims must use the lowest price of the previous 30 days [M-L, verify]; no timers or stock counters unless true.
- Training, workshops, and digital content: there is no separate "eğitim" exception to the 14-day cayma right. Relevant exceptions are in Mesafeli Sözleşmeler Yönetmeliği m.15(1): (ğ) electronically instant-performed services, (h) services begun with the consumer's consent before the cayma period ends (the seller must prove consent), (g) dated recreation or entertainment services. Whether a given course or live workshop qualifies is unsettled; don't tell users "no refund" copy is lawful [L-M, verify with counsel].
- Influencer and testimonial content must be labelled as advertising; no purchased or fake reviews [L].
- Prices in TL with "KDV dahil/hariç" explicit. High inflation makes price and installment display matter.

## WhatsApp

No controlled click-to-WhatsApp conversion data found, and no Türkiye-specific preference percentage (the Meta/Kantar survey of 22 markets doesn't break Türkiye out in what could be retrieved). Practitioner consensus [L]: for local services, clinics, B2C quotes, and high-consideration purchases, a floating WhatsApp button with a prefilled message, stated hours, and a fast reply promise often beats a form. Track clicks with an event or UTM. Cloud API became available for Turkish numbers on 15 May 2024 (Zoho notice).

## Lead response speed

- HBR 2011 (Oldroyd et al.): in an audit of 2,241 US firms, 37% replied within an hour and 23% never did; the 42-hour average counts responders only [M]. In a 1.25M-lead analysis, contacting within an hour was about 7x as likely to reach a decision maker as waiting one more hour and over 60x vs waiting 24 hours or more [M]. These are ratios with no baseline rate and no revenue outcome.
- The "5 minutes / 21x / 100x" figures come from a vendor (InsideSales) study, not HBR or MIT, and measured contact and qualification, not sales [L]. "78% buy from the first responder" has no traceable source.
- No Turkish or WhatsApp-specific data. Use as direction only; measure the client's own first-reply time against paid enrolment.

## Copy conventions [L]

- "Siz" for B2B, finance, and health; "sen" can fit youth and DTC brands.
- CTA verbs: "Hemen İncele", "Sepete Ekle", "Ücretsiz Teklif Al", "Hemen Ara".
- Avoid literal translations of English hype. Keep correct diacritics (ğ, ş, ı, İ) in headlines and form validation. Uppercase CSS transforms on Turkish text can break dotted/dotless i; check `text-transform` and `lang="tr"`.
- Free-shipping thresholds and same-day shipping cues are worth surfacing near the CTA.

## Gaps

No credible Turkish cart-abandonment or conversion-rate benchmarks; no Turkish online-education pricing or conversion norms; no tests of siz/sen or CTA wording; no call-vs-form or WhatsApp-vs-form evidence for high-ticket services.

Hand off copy writing to **copywriting**.
