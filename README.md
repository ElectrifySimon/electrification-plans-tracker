# National Electrification Plans Tracker

Static tracker of national electrification plans, roadmaps and strategies published in the run-up to COP31.
Password-gated, sortable, searchable, with a source and PDF link on every entry.

Live: https://electrifysimon.github.io/electrification-plans-tracker/

## What is in it

17 entries, as of 20 November 2026:

- 10 countries with a published 2026 national plan, roadmap or strategy
- 3 of those are energy access plans (Zambia, Ethiopia, Mozambique)
- 1 regional bloc instrument (EU Electrification Action Plan)
- 6 watchlist entries (Korea, Indonesia, Philippines, Peru, Rwanda, Kenya) flagged as in preparation, existing but not new, or no plan found

Every entry carries the publisher, publication date, scope, a one-paragraph summary, the source URL, and a PDF link where a public PDF exists. Entries built from trade or press reporting rather than the publisher's own document are marked `Secondary` in the detail panel.

## How the password works

The live gated page is `gated/index.html`, a **Staticrypt** build: the whole app is encrypted into one self-contained HTML file and decrypted in the page by the password form. Passphrase: `antalya-grid-2026`.

Build it in two steps:

```bash
# 1. gate-free single file: inline data.js, drop the lock markup, call start()
python3 make_dist.py

# 2. encrypt it
npx -y staticrypt@3.5.4 dist/index.html -p "antalya-grid-2026" -d site --remember false --short
cp site/index.html gated/index.html
```

Do not split a gated deployment into `index.html` + `data.js` + a fetch. The second request can fail silently in an in-app webview, and that failure looks exactly like a wrong password. Keep everything in the one document.

`plain.html` is the no-script fallback: every entry, no gate, no JS.

This is a share gate. Staticrypt encrypts the payload, so the passphrase is not stored in the repo, but anyone with the passphrase reads everything. The documents are public; do not put non-public material here.

## Update the data

```bash
# edit the plaintext dataset (never committed)
$EDITOR src/data.json

# rebuild the JS dataset
python3 build.py

git add data.js && git commit -m "update data" && git push
```

`src/data.json` is gitignored; `data.js` is generated from it.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole app: lock screen, list, filters, detail panel. No dependencies. |
| `data.js` | Dataset as a JS global. |
| `build.py` | Regenerates `data.js` from `src/data.json`. |
| `DESIGN.md` | Design token spec the UI is built from. |
| `src/data.json` | Plaintext dataset, local only. |

## Design

Tokens live in `DESIGN.md` (design-md spec). Surface archetype is Explore: filters, ordered rows, a detail sheet. No hero, no marketing framing. Iowan Old Style for country names, system sans for body, one accent colour.
