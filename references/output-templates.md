# Output templates

Contents: icon legend · layout rules · report order · verdict · do first · overview table · finding cards · what works · action buckets · form audit · copy drafts · measurement plan · could-not-assess · quick mode · results review

The report is read in a terminal or chat window. Make it scannable: short table cells, long text in cards, one consistent icon system. Write in the user's language; translate the labels, keep the icons. Follow [plain-language](plain-language.md): everyday words, a short bracketed explanation at the first use of any technical term, and developer details only in a final "For your developer:" line. Evidence, decision, and section labels are the ones in the legend above and in plain-language.md.

## Icon legend (single source; use exactly these)

| Concept | Icon and label |
|---|---|
| Evidence | 👁️ Seen on the page · 🧠 My judgment · ❓ Need your numbers |
| Severity (NN/g 0-4) | 🔴 4 critical · 🟠 3 major · 🟡 2 minor · 🟢 1 cosmetic · ⚪ not rated |
| Decision | 🚀 Do now · 🧪 Try first · 🔎 Find out first |
| Confidence | ▰▰▰ high · ▰▰▱ medium · ▰▱▱ low |
| Can you trust your numbers? | ✅ Yes · ⚠️ Yes, with caveats · ⛔ No |
| Sections | 🎯 summary · ⚡ do these first · 📋 overview · 🔍 detail · ✅ what works · 📊 measurement · ✍️ copy drafts · 🧭 can you test? · 💰 what it could be worth · 🚫 what I could not check |
| Card fields | 👁️ evidence · 💥 impact · 🛠️ fix · 🔎 how to verify |

Rules:
- Icons are scan aids. Always keep the text label next to the icon (for example "🔴 Critical"), so the report still reads correctly when copied or when emoji don't render.
- One icon per concept, at the start of a heading, label, or cell. No decorative piles or repeated icons in running text.
- Use the colored circles only for severity. Don't reuse them for confidence or status.

## Layout rules

- Short table cells (a title of about 8 words, an icon, a label). Anything longer goes into a finding card. Wide tables with long cells wrap badly in a terminal.
- Separate major sections with a horizontal rule (`---`) and a heading that starts with its icon.
- Bold the first words of each card field. Keep cards to 4-5 lines.
- Lead with the verdict and the top 3 actions. The reader should know what to do first without scrolling.
- Omit any section with nothing real in it. Padding is a defect.

## Report order (Standard mode)

🎯 Summary → ⚡ Do these first → 📋 Overview table → 🔍 Finding cards → ✅ What works → 🧭 Can you test? → 💰 What it could be worth (when volume and value are known) → ✍️ Copy drafts → 📊 Measurement plan → 🚫 Could not assess.

## 🎯 Summary

```
## 🎯 Summary
- **Main blocker:** [traffic mismatch | offer | clarity | trust | friction | technical | tracking | unknown]
- **Confidence:** ▰▰▱ medium, because [one line of evidence]
- **Can you trust your numbers?** ⚠️ Yes, with caveats [or ✅ / ⛔ / "not checked"]
- **What I checked:** [page, screenshot, phone or computer]
- **What I could not check:** [analytics, mobile, below the fold, traffic quality, ...]
```

## ⚡ Do these first

Three lines at most, in priority order. Each is one action, the finding number, and its decision icon.

```
## ⚡ Do these first
1. 🚀 Fire conversion events only after the server confirms the lead (finding 1)
2. 🚀 Generate all dates and seat counts from one data file (finding 3)
3. 🔎 Reconcile ad-platform conversions with CRM records (finding 2)
```

## 📋 Overview table

| # | Finding | Evidence | Severity | Decision |
|---|---|---|---|---|
| 1 | Conversion fires before success | 👁️ Seen on the page | 🔴 4 | 🚀 Do now |
| 2 | Phone required, 9 fields | 👁️ Observed | 🟠 3 | 🧪 Try first |
| 3 | Unknown mobile drop-off | ❓ Need your numbers | ⚪ | 🔎 Find out first |

Add a Confidence column (▰▰▱) in Deep mode.

## 🔍 Finding cards

One card per finding, in the same order as the table.

```
### 1 · 🔴 Conversion fires before success · 🚀 Do now
- 👁️ **What I saw:** [what you saw, with the exact place; say if it is a fact or your judgment]
- 💥 **Impact:** [qualitative effect and why; label Inferred if it is a judgment; no invented percentages]
- 🛠️ **Fix:** [specific change in plain words]
- 🔎 **How to check it worked:** [the cheapest check]
- 🧑‍💻 **For your developer:** [technical details, only if needed]
```

## ✅ What works

Three to five bullets of things to keep, so the reader doesn't "fix" them. Each is concrete (for example "✅ Comparison table with real specs on the product page").

## Action buckets (optional grouping of the cards)

- 🚀 **Quick wins (do now):** bugs, speed, accessibility, clear friction removals, label and copy fixes with a stated reason.
- 🏗️ **High-impact changes:** structural changes with evidence; say what would show it worked.
- 🧪 **Test backlog** (only when viable per [viability-and-stats](viability-and-stats.md)):

```
Because [what we saw], we think [change] for [group of visitors] will [result], which we will count by [main number].
We are wrong if: [what would disprove it]. Must not get worse: [numbers]. Needs about [n] visitors per version.
```

## 📝 Form audit (when the page has a form)

Use the same card layout for each issue (evidence, impact, fix, verify, plus Priority High / Medium / Low), then a **recommended form design**: required fields with a one-line justification each, optional fields with rationale, field order, copy (labels, helper text, button), error messages for the main fields, layout notes (mobile first), and the success state (next step, who replies, when).

## ✍️ Copy drafts (headline, CTA, button)

```
**Element:** [current text]
- **A:** [text]  → why: [principle, e.g. outcome-led]
- **B:** [text]  → why: [...]
- **C:** [text]  → why: [...]
*Status: draft; ship or test candidate; needs the user's confirmation of the facts used.*
```

Never invent proof, numbers, testimonials, or guarantees in options.

## 📊 How to track results

- **The main result to count:** exactly what counts as a win (a paid order, a qualified enquiry).
- **Smaller steps to count:** started the form, reached step N, payment error, button clicks.
- **Things that must not get worse:** revenue per visitor, lead quality, refunds, page speed.
- **Groups to compare:** phone vs computer, where visitors came from, new vs returning.
- **When to look:** after a set number of whole weeks, and first check the visitors were split evenly.
- If tracking is missing or untrustworthy, say that this blocks everything else.

## 🚫 Could not assess / data needed

Bullet list of the missing inputs and the cheapest way to get each (for example "GA4 funnel exploration by device, last 28 days"). Add the measurement line (✅ / ⚠️ / ⛔) from [measurement-trust](measurement-trust.md) when any analytics number was used. Always close with:

> 🤖 This is an AI-assisted audit. Severity ratings are indicative, and it is not a substitute for human expert review or user testing.

When citing a case study or benchmark, include source, date, what was measured, and the confidence tag; for a headline lift of +30% or more, say it is unlikely to transfer.

## Findings JSON (for the animated visual report)

The chat report is the source of truth. `findings.json` is its structured copy, with the same ids and text; the schema and capture steps are in [visual-report](visual-report.md). Card field to JSON key: id → `id`, title → `title`, 👁️/🧠/❓ → `evidence_tag` (`observed|inferred|needs_data`), severity icon → `severity` (0-4), 🚀/🧪/🔎 → `decision` (`ship|test|research`), ▰ bars → `confidence`, 👁️ Evidence → `evidence`, 💥 Impact → `impact`, 🛠️ Fix → `fix`, 🔎 Verify → `verify`, plus `anchor` (selector, text, measured rects, or a page-level fallback).

## Quick mode

🎯 Summary (2 lines) + ⚡ Do these first + a 5-row 📋 overview table. Nothing else.

## 🧪 Results review (user pasted test data)

```
## 🧪 Results review
- **Inputs received:** visitors/conversions per arm, runtime, split, primary metric
- **Were visitors split evenly between versions?** ✅ yes | ⛔ no, so the result cannot be trusted
- **Sample and duration:** [reached plan? whole weeks?]
- **Effect:** [relative and absolute, 95% CI]
- **Guardrails:** [...]
- **Decision:** 🚀 use the new version | ⏳ keep running | ⛔ result not valid | ⚪ no clear winner, and why
- **Caveats:** peeking, novelty, multiple metrics or segments
```

If the split was uneven or inputs are missing, stop and say the results can't be read yet.
