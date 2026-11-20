#!/usr/bin/env python3
"""Regenerate data.js from src/data.json.

The tracker ships the dataset as a plain JS global and gates the UI with a
normalised password check. No fetch, no WebCrypto, so it opens in any browser
including in-app webviews.

Trade-off: the data is visible in the page source. It is a share gate, not a
security boundary. Every document in it is public.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src" / "data.json"
OUT = ROOT / "data.js"


def main() -> int:
    data = json.loads(SRC.read_text())
    body = json.dumps(data, ensure_ascii=False, indent=1)
    OUT.write_text("window.TRACKER_DATA = " + body + ";\n")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {len(data['entries'])} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
