# HTML report spec (for browser AIs)

Produce ONE self-contained HTML file with the same findings and wording as the text report. Do not fetch anything from the internet: no external scripts, fonts, images, or trackers. Nothing in the file may send data anywhere.

## Content
- Header: site address, date, one-line summary, "Main blocker", what you checked / could not check.
- "Do these first": up to 3 lines linked to findings.
- Findings list (cards) shown as an open list by default; the tour is optional, not automatic.
- A "Print / PDF" button (`window.print()`) with print styles that fit the summary, the findings table, the changes, and the next step on one page.
- Findings list (cards). Each card: number, title, evidence label (Seen on the page / My judgment / Need your numbers), severity (Critical, Major, Minor, Cosmetic, Not rated), decision (Do now / Try first / Find out first), What I saw, Why it matters, Fix, a "Now → New" box when the finding has a Change, For your developer (if any).
- Smaller notes, Next step, What works, Copy drafts, How to track results, What I could not check, the closing disclaimer line.

## Behaviour
- Severity filter chips (All / Critical / Major / Minor / Cosmetic) that hide and show cards.
- Cards expand with a short fade. Keep dwell times short (about 4 to 9 seconds). A "Start tour" button walks through findings in severity order, with next, back, and pause. Keys: left and right arrows move, Space plays or pauses, Esc stops.
- Respect `prefers-reduced-motion`: no animation, manual tour only.
- Light and dark colors with `prefers-color-scheme`; set `body` background explicitly. Works at 360 px phone width with no horizontal scroll.
- Colors for severity: red, orange, yellow, green, grey. Always keep the text label next to a color. Use icons only in section headings.

## Safety
- Insert text with `textContent` (or escape it). Never copy page text into HTML unescaped.
- Do not embed screenshots or any copy of the audited page's code.

## Delivery
Give the file as a download or as a code block the user can save as `rapor.html`. Tell the user how to open it (double-click).
