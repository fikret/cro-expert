#!/usr/bin/env python3
"""Build the animated, single-file CRO report from audit findings and page screenshots.

Usage:
  build_report.py --findings findings.json --shots DIR [--out report.html]
                  [--template T] [--max-mb 25] [--no-images]

  findings.json  report-level fields plus findings[] (see references/visual-report.md)
  DIR            holds tiles.json and the screenshot files it lists
  --no-images    build a panel-only report (also the fallback when no screenshots exist)

Standard library only. The output is one local HTML file with the screenshots embedded.
"""
import argparse
import base64
import json
import os
import struct
import sys

EVIDENCE = {"observed", "inferred", "needs_data"}
DECISION = {"ship", "test", "research"}
FALLBACK = {"page", "head"}
DEVICES = ("desktop", "mobile")
MARKER = "/*__DATA__*/null"


def fail(msg):
    sys.exit("error: " + msg)


def warn(msg):
    print("warning: " + msg, file=sys.stderr)


def image_info(path):
    """Return (mime, width_px, height_px) for a PNG or JPEG file."""
    with open(path, "rb") as fh:
        head = fh.read(32)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", head[16:24])
            return "image/png", w, h
        if head[:2] == b"\xff\xd8":
            fh.seek(2)
            while True:
                b = fh.read(1)
                if not b:
                    break
                if b != b"\xff":
                    continue
                marker = fh.read(1)
                while marker == b"\xff":
                    marker = fh.read(1)
                if not marker:
                    break
                m = marker[0]
                if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                    continue
                size = struct.unpack(">H", fh.read(2))[0]
                if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                    fh.read(1)
                    h, w = struct.unpack(">HH", fh.read(4))
                    return "image/jpeg", w, h
                fh.seek(size - 2, 1)
    fail("unsupported or unreadable image (PNG and JPEG only): " + path)


def load_json(path, what):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        fail(what + " not found: " + path)
    except json.JSONDecodeError as e:
        fail("invalid JSON in %s: %s" % (what, e))


def num(v, name):
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        fail(name + " must be a number")
    return float(v)


def validate(data):
    if not isinstance(data, dict):
        fail("findings file must be a JSON object")
    fs = data.get("findings")
    if not isinstance(fs, list) or not fs:
        fail("findings[] is required and must not be empty")
    seen = set()
    for f in fs:
        if not isinstance(f, dict):
            fail("every finding must be an object")
        fid = f.get("id")
        if isinstance(fid, bool) or not isinstance(fid, int):
            fail("finding id must be an integer: %r" % (fid,))
        if fid in seen:
            fail("duplicate finding id: %d" % fid)
        seen.add(fid)
        if not f.get("title"):
            fail("finding %d has no title" % fid)
        if f.get("evidence_tag") not in EVIDENCE:
            fail("finding %d: evidence_tag must be one of %s" % (fid, sorted(EVIDENCE)))
        sev = f.get("severity")
        if isinstance(sev, bool) or not isinstance(sev, int) or not 0 <= sev <= 4:
            fail("finding %d: severity must be an integer 0-4" % fid)
        if f.get("decision") not in DECISION:
            fail("finding %d: decision must be one of %s" % (fid, sorted(DECISION)))
        a = f.get("anchor")
        if a is not None:
            if not isinstance(a, dict):
                fail("finding %d: anchor must be an object" % fid)
            if a.get("fallback", "page") not in FALLBACK:
                fail("finding %d: anchor.fallback must be one of %s" % (fid, sorted(FALLBACK)))
    do_first = data.get("do_first") or []
    if len(do_first) > 3:
        fail("do_first may have at most 3 entries")
    for d in do_first:
        if not isinstance(d, dict) or not d.get("action"):
            fail("each do_first entry needs an action")
        if d.get("finding") is not None and d["finding"] not in seen:
            fail("do_first refers to unknown finding id: %r" % (d["finding"],))
    works = data.get("works") or []
    if works and not 3 <= len(works) <= 5:
        warn("works has %d items; 3-5 is recommended" % len(works))
    return fs


def load_tiles(shots_dir, tiles_file):
    tiles = load_json(tiles_file or os.path.join(shots_dir, "tiles.json"), "tiles.json")
    out = {}
    total = 0
    for dev in DEVICES:
        t = tiles.get(dev)
        if not t or not t.get("tiles"):
            continue
        page_w = num(t.get("pageW"), dev + ".pageW")
        page_h = num(t.get("pageH"), dev + ".pageH")
        if page_w <= 0 or page_h <= 0:
            fail(dev + ": pageW and pageH must be positive")
        built = []
        covered = 0.0
        for tile in t["tiles"]:
            path = os.path.join(shots_dir, tile.get("file", ""))
            if not os.path.isfile(path):
                fail("screenshot not found: " + path)
            mime, w, h = image_info(path)
            css_h = page_w * h / w
            with open(path, "rb") as fh:
                raw = fh.read()
            total += len(raw)
            y = num(tile.get("y"), dev + " tile y")
            built.append({"src": "data:%s;base64,%s" % (mime, base64.b64encode(raw).decode("ascii")),
                          "y": y, "h": round(css_h, 2)})
            covered = max(covered, y + css_h)
        if covered + 2 < page_h:
            warn("%s: screenshots cover %.0f of %.0f px; clipping the page height" % (dev, covered, page_h))
            page_h = covered
        out[dev] = {"pageW": page_w, "pageH": round(page_h, 2), "tiles": built}
    return out, total


def clean_rects(f, tiles):
    """Keep only usable rects per device. Unusable anchors become page-level findings."""
    a = f.get("anchor")
    if not a:
        return
    rects = a.get("rects") or {}
    cleaned = {}
    for dev in DEVICES:
        t = tiles.get(dev)
        keep = []
        for r in rects.get(dev) or []:
            try:
                x, y, w, h = (num(r[k], "rect") for k in ("x", "y", "w", "h"))
            except (KeyError, SystemExit):
                warn("finding %d: malformed rect ignored" % f["id"])
                continue
            if not t:
                continue
            if w <= 0 or h <= 0:
                warn("finding %d (%s): zero-size rect ignored" % (f["id"], dev))
                continue
            if x + w < 0 or y + h < 0 or x > t["pageW"] or y > t["pageH"]:
                warn("finding %d (%s): rect outside the captured page; moved to the page-level lane" % (f["id"], dev))
                continue
            if w * h > 0.6 * t["pageW"] * t["pageH"]:
                warn("finding %d (%s): rect covers over 60%% of the page (selector too broad?); moved to the page-level lane" % (f["id"], dev))
                continue
            keep.append({"x": x, "y": y, "w": w, "h": h})
        cleaned[dev] = keep
    a["rects"] = cleaned


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--findings", required=True)
    ap.add_argument("--shots", required=True, help="directory with tiles.json and screenshots")
    ap.add_argument("--tiles", help="path to tiles.json if it is not in --shots")
    ap.add_argument("--template", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "report-template.html"))
    ap.add_argument("--out", help="output file (default: <shots>/report.html)")
    ap.add_argument("--max-mb", type=float, default=25.0, help="fail if the report is larger (default 25)")
    ap.add_argument("--no-images", action="store_true", help="panel-only report without screenshots")
    a = ap.parse_args()

    data = load_json(a.findings, "findings file")
    fs = validate(data)

    tiles, raw_bytes = {}, 0
    if not a.no_images:
        tiles_path = a.tiles or os.path.join(a.shots, "tiles.json")
        if os.path.isfile(tiles_path):
            tiles, raw_bytes = load_tiles(a.shots, a.tiles)
        else:
            warn("no tiles.json found; building a panel-only report")
    for f in fs:
        clean_rects(f, tiles)
    pinned = sum(1 for f in fs if any((f.get("anchor") or {}).get("rects", {}).get(d) for d in DEVICES))

    data["tiles"] = tiles or None
    try:
        with open(a.template, encoding="utf-8") as fh:
            html = fh.read()
    except OSError as e:
        fail("cannot read template: %s" % e)
    if html.count(MARKER) != 1:
        fail("template must contain the data marker exactly once: " + MARKER)
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    blob = (blob.replace("</", "<\\/").replace("<!--", "<\\!--")
                .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))
    html = html.replace(MARKER, blob)
    title = data.get("title") or data.get("url") or "CRO report"
    html = html.replace("<title>CRO raporu</title>", "<title>%s</title>" % title.replace("&", "&amp;").replace("<", "&lt;"))

    out = a.out or os.path.join(a.shots, "report.html")
    size_mb = len(html.encode("utf-8")) / 1048576
    if size_mb > a.max_mb:
        fail("report is %.1f MB, over --max-mb %.0f; capture fewer tiles or use smaller screenshots" % (size_mb, a.max_mb))
    if size_mb > 12:
        warn("report is %.1f MB; it will open slowly on some machines" % size_mb)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote %s (%.1f MB): %d findings, %d pinned on the page, %d in the page-level lane, devices: %s"
          % (out, size_mb, len(fs), pinned, len(fs) - pinned, ", ".join(tiles) or "none (panel-only)"))


if __name__ == "__main__":
    main()
