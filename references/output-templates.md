# Output templates

Contents: icons · layout rules · report order · summary · do first · overview table · finding cards · what works · action buckets · form audit · copy drafts · tracking plan · could-not-assess · quick mode · results review

The report is read in a terminal or chat window. Make it scannable: short table cells, long text in cards, one consistent icon system. Write in the user's language; translate the labels. Follow [plain-language](plain-language.md): everyday words, a short bracketed explanation at the first use of any technical term, and developer details only in a final "For your developer:" line. Evidence, decision, and section labels are the ones above and in plain-language.md.

## Icons: headings only

Icons appear only at the start of section headings. In tables, cards, and running text use plain text labels, with no icons.

| Concept | Label (text only) |
|---|---|
| Evidence | Seen on the page · My judgment · Need your numbers |
| Severity (NN/g 0-4) | Critical · Major · Minor · Cosmetic · Not rated |
| Decision | Do now · Try first · Find out first |
| Section headings | 🎯 Summary · ⚡ Do these first · 📋 Overview · 🔍 Details · ✅ What works · ✍️ Copy drafts · 📊 How to track results · 🧭 Can you test? · 💰 What it could be worth · 🚫 What I could not check |

Rules:
- One icon per heading, at its start. No icons in table cells, card fields, bullets, or sentences.
- A finding card title may carry its severity circle (🔴 🟠 🟡 🟢 ⚪) as its only icon, always next to the text label.
- Keep the main list to 7 findings at most (Quick mode: 5). Merge findings that share a root cause. Put small items in **Smaller notes**, one line each.
- Do not add a confidence rating or a "can you trust your numbers" line. They are not part of the report.

## Layout rules

- Short table cells (a title of about 8 words, an icon, a label). Anything longer goes into a finding card. Wide tables with long cells wrap badly in a terminal.
- Separate major sections with a horizontal rule (`---`) and a heading that starts with its icon (icons only in headings).
- Bold the first words of each card field. Keep cards to 4-5 lines.
- Lead with the verdict and the top 3 actions. The reader should know what to do first without scrolling.
- Omit any section with nothing real in it. Padding is a defect.

## Report order (Standard mode)

🎯 Summary → ⚡ Do these first → 📋 Overview table → 🔍 Finding cards → ✅ What works → 🧭 Can you test? → 💰 What it could be worth (when volume and value are known) → ✍️ Copy drafts → 📊 How to track results → 🚫 What I could not check.

## 🎯 Summary

```
## 🎯 Summary
- **Main blocker:** [traffic mismatch | offer | clarity | trust | friction | technical | tracking | unknown]
- **What I checked:** [page, screenshot, phone or computer]
- **What I could not check:** [analytics, mobile, below the fold, traffic quality, ...]
```

## ⚡ Do these first

Three lines at most, in priority order. Each is one action, its decision label, and the finding number.

```
## ⚡ Do these first
1. Do now: fire conversion events only after the server confirms the lead (finding 1)
2. Do now: generate all dates and seat counts from one data file (finding 3)
3. Find out first: reconcile ad-platform conversions with CRM records (finding 2)
```

## 📋 Overview table

| # | Finding | Evidence | Severity | Decision |
|---|---|---|---|---|
| 1 | Conversion fires before success | Seen on the page | Critical | Do now |
| 2 | Phone required, 9 fields | Seen on the page | Major | Try first |
| 3 | Unknown mobile drop-off | Need your numbers | Not rated | Find out first |

## 🔍 Finding cards

One card per finding, in the same order as the table.

```
### 1 · 🔴 Conversion fires before success · Do now
- **What I saw:** [what you saw, with the exact place; say if it is a fact or your judgment]
- **Impact:** [qualitative effect and why; label it a judgment if it is one; no invented percentages]
- **Fix:** [specific change in plain words]
- **Change:** (only when the fix is a text change) Now: "[current text]" → New: "[ready-to-paste text; [brackets] for facts only the owner knows]"
- **For your developer:** [technical details, only if needed]
```

## ✅ What works

Three to five bullets of things to keep, so the reader doesn't "fix" them. Each is concrete (for example "Comparison table with real specs on the product page").

## Action buckets (optional grouping of the cards)

- **Quick wins (do now):** bugs, speed, accessibility, clear friction removals, label and copy fixes with a stated reason.
- **High-impact changes:** structural changes with evidence.
- **Test backlog** (only when viable per [viability-and-stats](viability-and-stats.md)):

```
Because [what we saw], we think [change] for [group of visitors] will [result], which we will count by [main number].
We are wrong if: [what would disprove it]. Must not get worse: [numbers]. Needs about [n] visitors per version.
```

## Form audit (when the page has a form)

Use the same card layout for each issue (what I saw, impact, fix, plus Priority High / Medium / Low), then a **recommended form design**: required fields with a one-line justification each, optional fields with rationale, field order, copy (labels, helper text, button), error messages for the main fields, layout notes (mobile first), and the success state (next step, who replies, when).

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

Bullet list of the missing inputs and the cheapest way to get each (for example "GA4 funnel exploration by device, last 28 days"). Always close with:

> This is an AI-assisted audit. Severity ratings are indicative, and it is not a substitute for human expert review or user testing.

When citing a case study or benchmark, include source, date, what was measured, and how reliable the source is; for a headline lift of +30% or more, say it is unlikely to transfer.

## Smaller notes, next step, previous audit

After What works, add (omit any that is empty):
- **Smaller notes:** one line each, for minor or unsure items that did not earn a card.
- **Next step:** one sentence: do the top 3, then run the audit again.
- **Previous audit:** only when an earlier `findings.json` for the same site exists. "12 earlier findings: 7 fixed, 3 still open, 2 new." Re-check each old finding on the live page first.

## Findings JSON (for the animated visual report)

The chat report is the source of truth. `findings.json` is its structured copy, with the same ids and text; the schema and capture steps are in [visual-report](visual-report.md). Card field to JSON key: id → `id`, title → `title`, evidence label → `evidence_tag` (`observed|inferred|needs_data`), severity label → `severity` (0-4), decision label → `decision` (`ship|test|research`), What I saw → `evidence`, Impact → `impact`, Fix → `fix`, plus `change` (`{"from": ..., "to": ...}`), plus `anchor` (selector, text, measured rects, or a page-level fallback). Report level: `notes[]` (smaller notes), `next_step`, and `comparison` (`{date, previous_total, resolved, still_open, new}`).

## Quick mode

🎯 Summary (2 lines) + ⚡ Do these first + a 5-row 📋 overview table. Nothing else.

## Results review (user pasted test data)

```
## Results review
- **Inputs received:** visitors/conversions per arm, runtime, split, primary metric
- **Were visitors split evenly between versions?** yes | no, so the result cannot be trusted
- **Sample and duration:** [reached plan? whole weeks?]
- **Effect:** [relative and absolute, 95% CI]
- **Guardrails:** [...]
- **Decision:** use the new version | keep running | result not valid | no clear winner, and why
- **Caveats:** peeking, novelty, multiple metrics or segments
```

If the split was uneven or inputs are missing, stop and say the results can't be read yet.
