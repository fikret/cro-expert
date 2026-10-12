# Visual report (animated, on the page)

Contents: what it is · when to run · requirements and fallbacks · capture A (Claude in Chrome) · capture B (browser command line) · capture C (screenshot from the user) · approximate anchors · findings.json · choosing selectors · assemble (with or without Python) · open it · safety

Every audit of a public URL ends with a local HTML report that plays the findings on top of screenshots of the audited page: spotlight, numbered pins, sliding cards, a guided tour, and a side panel. The chat report stays the source of truth; this file is its animated twin.

It uses **screenshots plus element positions**, never a copy of the page's HTML, CSS, or JavaScript. A copy would not work on every site and could fire the site's trackers or forms. Screenshots work everywhere and run no page script.

## When to run

Run it automatically at the end of an audit of a public URL. Skip it, and say why in one line, when the input was pasted copy with no URL, the page needs a login, or nothing below works. **Cover the whole page, top to bottom, in every mode.** A tile is only about 30 KB, so a 14,000 px page is roughly 22 tiles (under 1 MB). The only limit is a safety stop at 60 tiles (about 40,000 px); beyond that, say plainly which part was not captured.

## Requirements and fallbacks (nothing is mandatory)

Check what the machine has before you start, then take the best option available.

| Need | Best | Fallback |
|---|---|---|
| Screenshots | **A.** Claude in Chrome tools (element positions are measured) | **B.** the browser's command line (positions estimated) → **C.** a screenshot the user provides (positions estimated) → none (panel-only report) |
| Building the file | `python3 scripts/build_report.py` (one self-contained file, validates the data) | **No Python:** copy the template and write `data.js` next to the image files (see "Assemble") |

Detect Chrome tools with ToolSearch (`mcp__claude-in-chrome__`). Detect Python with `python3 --version` (also try `python --version` and `py --version` on Windows). Report which route you used in the final message.

A report without any screenshots is still useful: `data.js` or `--no-images` gives the animated tour with verdict, finding cards, severity filter, and the page-level lane.

## Capture A: Claude in Chrome (positions measured)

Load the Chrome tools first. Never click a consent banner, never submit a form, never capture a page behind a login. Leave the banner as it appears.

1. **Window.** `resize_window` to 1440 x 900 on your own tab, open the URL, and read `window.innerWidth`.
2. **Warm up lazy content.** The tool evaluates with top-level `await`; an async function without `await` returns `{}`:
   ```js
   await (async()=>{const h=document.documentElement.scrollHeight;for(let y=0;y<h;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,150));}window.scrollTo(0,0);return document.documentElement.scrollHeight})()
   ```
3. **Measure at scrollY = 0, before hiding anything.** Pass your `[id, selector, visibleText]` list. Each rect carries `t` (its text start) so you can check you hit the intended element; the snippet also marks fixed and sticky elements:
   ```js
   ((items)=>{const sx=scrollX,sy=scrollY;const rects={};
   for(const [id,sel,txt] of items){let els=[];try{els=sel?[...document.querySelectorAll(sel)]:[]}catch(e){}
   if(!els.length&&txt){els=[...document.querySelectorAll('a,button,h1,h2,h3,h4,p,li,label,span,div')].filter(e=>e.children.length<3&&e.textContent.trim().includes(txt)).slice(0,3)}
   rects[id]=els.slice(0,4).map(e=>{const r=e.getBoundingClientRect();return{x:Math.round(r.left+sx),y:Math.round(r.top+sy),w:Math.round(r.width),h:Math.round(r.height),t:e.textContent.trim().slice(0,40)}}).filter(r=>r.w>0&&r.h>0)}
   let n=0;document.querySelectorAll('*').forEach(e=>{const p=getComputedStyle(e).position;if((p==='fixed'||p==='sticky')&&e.getBoundingClientRect().width>0){e.setAttribute('data-cro-fx','1');n++}});
   return JSON.stringify({pageW:innerWidth,pageH:Math.max(document.body.scrollHeight,document.documentElement.scrollHeight),dpr:devicePixelRatio,innerH:innerHeight,fixed:n,rects})})(ITEMS)
   ```
   Replace `ITEMS` with a JSON array such as `[[1,"form#inquire","Gönder"],[2,"h1",""]]`.
4. **Choose the primary rect.** The report spotlights the **first** rect of each finding. Matches come in DOM order, so reorder `rects` so the element that really shows the problem is first (check `t` and the screenshot). Drop the others, or keep them as extras.
5. **Tiles.** Use `window.scrollTo({top:Y,behavior:'instant'})` (smooth scrolling makes the position unreliable), wait about 350 ms, read back `window.scrollY`, and take `screenshot` with `save_to_disk: true` and `scale: 0.7` (about 30 KB per tile). Tile `i` is at `Y = i*(innerHeight-80)`; the last tile is clamped, so record the read-back value. After the first tile, hide the fixed elements: `document.querySelectorAll('[data-cro-fx]').forEach(e=>e.style.visibility='hidden')`. Tile count = `ceil((pageH-innerHeight)/(innerHeight-80))+1`, up to the 60-tile safety stop. Do not stop early because the page is long. The tool lets you batch scroll plus screenshot pairs in one call.
6. **Copy the files.** The tool saves screenshots in a temporary folder and prints each path; copy them into the report folder in capture order as `desktop-01.jpg`, `desktop-02.jpg`, ...
7. **Drift check and restore.** If `scrollHeight` changed by more than 3%, measure again. Reload the page to undo the hiding, then close your tab.
8. **Mobile (optional).** Only if `resize_window` to about 390 px really gives `innerWidth <= 480` (it often doesn't), repeat with the same full-page tiling under `mobile`; otherwise skip it and add it to `could_not_assess`.
9. **Page longer than the safety stop (rare).** Keep the captured tiles and set `pageH` to the covered height. Findings below the cut go to the page-level lane (the script does this for you). Also list the uncovered part under "What I could not check".

The Chrome extension cannot open `file://` pages. To preview a report with the Chrome tools yourself, serve the folder on `127.0.0.1` with a temporary local server and stop it afterwards. Users simply open the file.

## Capture B: the browser's command line (positions estimated)

No Chrome extension, but Chrome, Edge, or Chromium is installed. One tall screenshot, no scrolling:

```bash
# macOS
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1440,6000 --virtual-time-budget=8000 --screenshot=desktop-01.png "https://example.com/"
# Linux: google-chrome or chromium   Windows: "C:\Program Files\Google\Chrome\Application\chrome.exe" (or msedge.exe)
```

- macOS has no `timeout` command; run without it.
- Use a window height equal to the page height (read it first, for example with `--dump-dom` or from the measured page). If a very tall height fails, lower it until it works and say which lower part of the page the image does not cover; take a second image of that part only if the machine allows it. The image is a single tile: `tiles.json` has one tile with `y: 0`, `pageW: 1440`, `pageH` = the image height (PNG size in the header bytes 16-24). Shorter pages leave white space at the bottom, so set `pageH` where the content ends.
- Open the image with the Read tool to see it, then estimate positions (below). Mark every anchor `"approx": true`.

## Capture C: a screenshot from the user

If the user attaches a full-page screenshot, treat it like capture B: one tile, positions estimated, `approx: true`. Ask for a desktop-width, full-page screenshot when it is missing; otherwise note the limit.

## Approximate anchors

Without measurement, look at the image, find the element for each finding, and estimate its box in image pixels. Convert to CSS pixels: `css = image_px * pageW / image_width_px`. Give rects as `{x, y, w, h}` in those CSS pixels and set `"approx": true`. The report draws these pins with a dashed ring and a "position is approximate" note on the card. When you can't locate the element, leave it page-level (`"fallback": "page"`, no rects). Never present estimated positions as measured.

## findings.json

```json
{
  "url": "https://example.com/", "title": "example.com audit", "captured_at": "2026-10-12",
  "language": "tr",
  "verdict": {"primary_constraint": "...", "confidence": "▰▰▱ medium, because ...",
              "measurement": "⚠️ Trusted with caveats", "assessed": "...", "not_assessed": "..."},
  "do_first": [{"action": "Fix the conversion event", "finding": 1}],
  "works": ["Short form", "Real proof", "Clear FAQ"],
  "could_not_assess": ["Speed (API quota)", "Mobile layout"],
  "disclaimer": "AI-assisted audit; severity is indicative; not a substitute for expert review.",
  "findings": [{
    "id": 1, "title": "Conversion fires before success",
    "evidence_tag": "observed", "severity": 4, "decision": "ship", "confidence": "▰▰▱",
    "evidence": "...", "impact": "...", "fix": "...", "verify": "...",
    "anchor": {"selector": "form#inquire", "text": "Gönder", "approx": false,
               "rects": {"desktop": [{"x": 700, "y": 1200, "w": 420, "h": 380}]},
               "fallback": "page"}
  }]
}
```

Rules:
- Same ids, titles, tags, severity, and text as the chat report. Keep the plain-language rules ([plain-language](plain-language.md)): the animated report is read by non-technical people. `evidence_tag`: `observed | inferred | needs_data`. `severity`: 0-4. `decision`: `ship | test | research`. At most 3 `do_first` entries, each pointing to an existing finding id.
- The first rect of a finding is its spotlight and pin position.
- Findings that aren't a visible element (title tag, `lang` attribute, tracking code, anything about a script) get `"anchor": {"fallback": "page"}` and no rects. They appear in the page-level lane, not as pins.
- Elements created only by JavaScript after the first view (pop-ups, chat widgets) may not exist at capture time. Anchor them to the nearest stable element or leave them page-level, and say so in the evidence text.

## Choosing selectors

- Prefer stable hooks: an `id`, a form `id`, `a[href^="tel:"]`, `h1`, `button[type=submit]`. Avoid long positional chains.
- Always add `anchor.text` (short, unique visible text) as a fallback.
- Anchor the smallest element that shows the problem (the button, not the section). A rect covering more than 60% of the page is treated as a mistake and moved to the page-level lane.
- Check `t` in the measured rects against the element you meant. An empty result means a wrong selector or an element that isn't rendered.

## Assemble (with or without Python)

Folder: `./cro-reports/<domain>-<YYYYMMDD>/` holding the images, `tiles.json`, `findings.json`, and the output.

**With Python** (one self-contained file, validates the data, moves unusable rects to the page-level lane, warns on size):
```bash
python3 scripts/build_report.py --findings cro-reports/<dir>/findings.json --shots cro-reports/<dir>
```

**Without Python** (works with any text editor and a browser):
1. Copy `assets/report-template.html` into the folder as `report.html` (`cp` on macOS/Linux, `copy` on Windows; or read the file and write it out).
2. Write `data.js` in the same folder: `window.CRO_DATA = { ...the findings.json content..., "tiles": {"desktop": {"pageW": 1440, "pageH": 7527, "tiles": [{"file": "desktop-01.jpg", "y": 0}, ...]}} };`
3. Keep the image files next to `report.html` (relative names) and don't move the folder's files apart.
4. Do by hand what the script would: unique ids, valid enums, at most 3 `do_first`, `pageH` equal to the covered height, and no rects below that height (put those findings page-level).
Sharing the no-Python version means sharing the whole folder (zip it).

## Open it

Tell the user the full path of `report.html`, how it was made (route and whether positions are measured or approximate), and the keys: ← → move between findings, Space play or pause, Esc close, 1-4 filter by severity, D switch desktop and mobile. Open it with `open` (macOS), `xdg-open` (Linux), or `start` (Windows). Mention script warnings (rects outside the page, too broad) in one line.

## Safety and privacy

The report holds screenshots of a third-party page and stays on the user's machine; don't upload or publish it. It runs only its own script, makes no network requests, and executes nothing from the audited site. Don't capture pages that show personal or logged-in data.
