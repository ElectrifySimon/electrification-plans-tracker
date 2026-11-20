#!/usr/bin/env python3
"""Build dist/index.html: the gate-free single file that Staticrypt encrypts.

Steps: inline data.js, drop the lock section, show #app, replace the gate
wiring block with a direct start().
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
html = (ROOT / "index.html").read_text()
data = (ROOT / "data.js").read_text()

html = html.replace('<script src="data.js"></script>', "<script>" + data + "</script>")
html = re.sub(r'<section id="lock".*?</section>\s*', "", html, flags=re.S)
html = html.replace('<div id="app" hidden>', '<div id="app">')
html = re.sub(
    r"  /\* GATE-START \*/.*?/\* GATE-END \*/",
    "  DATA = window.TRACKER_DATA;\n  start();",
    html,
    flags=re.S,
)

for needle in ("GATE-START", '<section id="lock"', "window.TRACKER_DATA"):
    if needle in html and needle != "window.TRACKER_DATA":
        raise SystemExit(f"build failed, leftover: {needle}")

(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "index.html").write_text(html)
print(f"wrote dist/index.html ({len(html)} bytes)")
