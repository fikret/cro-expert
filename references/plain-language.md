# Plain language (for non-technical readers)

Contents: the rules · words to avoid · glossary · labels for decisions and sections · scope

The people reading the report are usually business owners and marketers, not developers or analysts. They should understand every line without searching the web. This applies to the chat report, the animated report, and any copy drafts.

## The rules

1. **Say it in everyday words.** If a plain word exists, use it ("main image area at the top" instead of "hero"; "the button" instead of "CTA").
2. **If you must use a technical term, explain it once.** At its first use, put a short explanation in brackets, 15 words or fewer, with no other jargon in it. Afterwards use the term without repeating the explanation. Example: "hero (the big first area people see when the page opens)".
3. **Describe what happened, not the metric code.** Say "the page takes long to show its main picture" instead of "LCP is high". When a number or code is useful for the web developer, put it in the fix line: "Ask your developer to check LCP (loading time of the main picture)".
4. **No unexplained abbreviations.** Spell out or replace: A/B test, CTA, CR, AOV, LTV, SRM, MDE, CUPED, CI, UTM, LCP, INP, CLS, CrUX, GA4, CRM, PDP, UX, UI, SEO. The glossary below gives the replacement.
5. **Short sentences, active voice, one idea per line.** Prefer "Change the button text to X" over "Consider optimizing the CTA copy".
6. **Use the reader's own words.** Name things as they appear on their page ("the green 'Başvur' button"), not by their role in a framework.
7. **Do not explain statistics.** Say what to do and why it matters. If a test cannot be run, say "you do not have enough visitors to test this reliably; make the change and watch the results".
8. **Developer details go last.** Put selectors, code, event names, and tool settings in a final line starting with "For your developer:". Everything above that line must make sense without it.
9. **Write in the user's language, with the same rules.** In Turkish use everyday Turkish; keep a technical term only if people really use it ("buton", "form", "sayfa"), and explain the rest.

## Words to avoid, and what to write instead

| Technical term | Write this (English) | Türkçe karşılık |
|---|---|---|
| CRO, conversion rate optimization | making more visitors take the action you want | ziyaretçilerin istediğiniz adımı atma oranını artırmak |
| conversion | a visitor doing what you want (buying, filling the form, calling) | hedef işlem (satın alma, form doldurma, arama) |
| conversion rate | share of visitors who do it | hedef işlemi yapan ziyaretçi oranı |
| hero / hero section | the big first area people see when the page opens | sayfa açılınca görünen ilk büyük alan |
| above the fold | visible without scrolling | kaydırmadan görünen alan |
| below the fold | only visible after scrolling | kaydırınca görünen alan |
| CTA | the main button or link that asks for the action | ana buton / yönlendirme butonu |
| landing page | the page a visitor first arrives on (often from an ad) | ziyaretçinin ilk geldiği sayfa (genelde reklamdan) |
| PDP | product page | ürün sayfası |
| funnel | the steps from first visit to purchase | ziyaretten satın almaya giden adımlar |
| friction | anything that makes the action harder or more annoying | işlemi zorlaştıran şey |
| drop-off / abandonment | people leaving at this step | bu adımda sayfayı terk edenler |
| bounce rate | people who leave after seeing one page | tek sayfa görüp çıkanlar |
| value proposition | what you offer and why it is worth choosing you | ne sunduğunuz ve neden sizi seçmeli |
| social proof | signs that other people trust you (reviews, client names, numbers) | başkalarının size güvendiğini gösteren işaretler |
| trust signals | things that make a visitor feel safe (reviews, contact details, policies) | güven veren öğeler |
| message match | the page repeats the promise of the ad or link that brought the visitor | sayfanın, ziyaretçiyi getiren reklamın vaadini sürdürmesi |
| visual hierarchy | which things the eye sees first, second, third | gözün önce neye, sonra neye gittiği |
| scannability | can be understood by skimming | göz gezdirerek anlaşılabilirlik |
| A/B test | showing two versions to different visitors to see which works better | iki sürümü farklı ziyaretçilere gösterip karşılaştırma |
| variant | the changed version | değiştirilen sürüm |
| statistical significance | confidence that the difference is not luck | farkın şans olmadığından emin olma düzeyi |
| sample size | how many visitors you need before the result can be trusted | sonuca güvenmek için gereken ziyaretçi sayısı |
| baseline | the current result before any change | değişiklikten önceki mevcut sonuç |
| lift / uplift | increase in results | sonuçtaki artış |
| SRM (sample ratio mismatch) | the test split visitors unevenly, so the result cannot be trusted | testin ziyaretçileri dengesiz bölmesi, sonuç güvenilmez |
| guardrail metric | a number that must not get worse while you improve another | iyileştirirken kötüleşmemesi gereken ikinci ölçü |
| hypothesis | a reasoned guess to check | doğrulanacak varsayım |
| qualitative / quantitative | what people say or do (interviews, recordings) / numbers | görüşmeler ve izlemeler / sayılar |
| heatmap | a picture of where visitors click and look | ziyaretçilerin nereye tıkladığını gösteren renkli harita |
| session recording / replay | a video of a real visit | gerçek bir ziyaretin ekran kaydı |
| analytics (GA4) | the tool that counts your visitors and sales | ziyaretçileri ve satışları sayan araç |
| tracking / event | the setting that counts an action (like a purchase) | bir işlemi sayan ayar |
| UTM | tags in a link that show which campaign sent the visitor | linke eklenen, kampanyayı gösteren etiket |
| attribution | deciding which ad or channel gets credit for a sale | satış için hangi reklama/kanala pay verildiği |
| Core Web Vitals | Google's measures of how fast and stable the page feels | Google'ın sayfa hızı ve kararlılık ölçüleri |
| LCP | how long the main picture or headline takes to appear | ana görsel/başlığın görünme süresi |
| INP | how quickly the page reacts when someone taps or clicks | dokunulunca sayfanın tepki süresi |
| CLS | the page jumping around while it loads | sayfa yüklenirken öğelerin kayması |
| responsive / mobile-first | works well on phones | telefonda düzgün çalışan |
| tap target | the area a finger must hit | parmakla dokunulan alan |
| sticky | stays on screen while scrolling | kaydırırken ekranda kalan |
| modal / popup | a box that appears over the page | sayfanın üstünde açılan kutu |
| accessibility / WCAG | making the page usable for people with disabilities | engelli kullanıcıların da kullanabilmesi |
| contrast | difference between text and background colour | yazı ile arka plan rengi farkı |
| alt text | a text description of an image | görselin yazılı açıklaması |
| placeholder | grey example text inside a form field | form alanındaki soluk örnek yazı |
| validation / inline error | the message that tells people what they typed wrong | yanlış girilen bilgiyi söyleyen uyarı |
| checkout | the steps where the customer pays | ödeme adımları |
| cart abandonment | people who add to cart but do not buy | sepete ekleyip almayanlar |
| AOV | average order value: how much a typical order is worth | ortalama sipariş tutarı |
| LTV | lifetime value: how much a customer spends over time | bir müşterinin zaman içindeki toplam getirisi |
| CRM | the list or tool where you keep leads and customers | müşteri ve potansiyel müşteri kayıt aracı |
| lead | a person who left their details | bilgisini bırakan potansiyel müşteri |
| drip pricing | adding costs late, so the first price looks lower | ek ücretleri geç göstererek ilk fiyatı düşük göstermek |
| dark pattern | a trick design that pushes people to act against their interest | kullanıcıyı yanıltan tasarım hilesi |
| scarcity / urgency | "only 3 left" or "ends today" messages | "son 3 adet" / "bugün bitiyor" mesajları |
| anchor (price anchor) | a higher price shown first so the real price looks cheaper | gerçek fiyatı ucuz göstermek için önce gösterilen yüksek fiyat |
| cohort | a group that starts on the same date | aynı tarihte başlayan grup |
| LLM audit | a review done by an AI, not a human expert | uzman yerine yapay zekanın yaptığı inceleme |
| PXL, ICE, PIE, LIFT | scoring methods; do not name them, just give the order | puanlama yöntemleri; adını anmayın, sıralamayı verin |
| viability | whether you have enough traffic to test properly | düzgün test için yeterli ziyaretçi olup olmadığı |
| pipeline (sales) | the people waiting to become customers | müşteri olmayı bekleyenler |

Keep these only when the reader already uses them (for example the user wrote "CTA" first): CRO, A/B test, landing page. Even then, do not assume the others know them.

## Labels for decisions and sections

Use these names in the chat report and the animated report. Icons appear only in section headings; labels in tables and cards are plain text.

| Heading icon | English label | Türkçe etiket | Meaning |
|---|---|---|---|
| | Do now | Hemen yap | Safe to change right away |
| | Try first | Önce dene | Change it for some visitors first and compare |
| | Find out first | Önce araştır | Need more information before changing |
| | Seen on the page | Sayfada görüldü | A fact visible on the page |
| | My judgment | Yorumum | An informed guess about visitor behaviour |
| | Need your numbers | Verinize ihtiyaç var | Cannot know without your data |
| 🎯 | Summary | Özet karar | |
| ⚡ | Do these first | Önce şunları yap | |
| 🧭 | Can you test? | Test yapılabilir mi? | Traffic check |
| 💰 | What it could be worth | Değeri ne olabilir | Simple arithmetic, not a forecast |
| 📊 | How to track results | Sonuçları nasıl izlersiniz | |
| 🚫 | What I could not check | Kontrol edemediklerim | |
| | Main blocker | Ana engel | The biggest thing holding results back |
| | Change (Now → New) | Değişiklik (Şu an → Yeni) | Ready-to-paste wording for a text fix |
| | Smaller notes | Daha küçük notlar | Minor items, one line each |
| | Next step | Sonraki adım | Do the top 3, then run the audit again |
| | Previous audit | Önceki denetim | How many earlier findings are fixed, open, new |

Severity words stay: Critical / Major / Minor / Cosmetic (Kritik / Büyük / Küçük / Kozmetik).

## Scope

This skill does not review personal-data or privacy law (KVKK, GDPR, cookie banners, consent texts, aydınlatma metni). Do not raise it, even as a "worth checking" item. If the user asks, say it is outside this skill and suggest a privacy specialist.
