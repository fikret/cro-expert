# cro-expert

Evidence-graded conversion rate optimization (CRO) audit for websites. It finds why a page may not turn visitors into customers or enquiries, labels each finding as seen on the page, my judgment, or needs your data, and writes a plain-language report. Turkish and English.

## Three ways to use it

1. **In a browser AI (ChatGPT, Gemini, Claude.ai), no installation.** Send:
   > fikrettozak.com/w1.md dosyasını oku ve talimatı uygula. Sitem: https://sizin-siteniz.com

   The AI reads `web/w1.md` and `web/cro-expert-web.md` from this repository and returns a text report (and an HTML report if it can make files).
2. **In Claude Code, without installing the skill.** Same message. Claude Code opens the links and follows them.
3. **In Claude Code, installed (full version).** Copy this folder to `~/.claude/skills/cro-expert`. The full skill also builds an animated report on top of screenshots of your page (`references/visual-report.md`). Python is optional.

## What is here
- `SKILL.md` and `references/`: the full skill for Claude Code.
- `web/cro-expert-web.md`: self-contained version for browser AIs. `web/w1.md`: the instruction file the user points the AI to. `web/html-report.md`: spec for a one-file HTML report.
- `assets/report-template.html`, `scripts/`: animated screenshot report builder and a sample-size calculator.

## Scope and limits
No review of privacy law (KVKK, GDPR, cookies). Not legal advice. An AI-assisted audit is indicative: it does not replace expert review or testing with real users.

License: MIT.
