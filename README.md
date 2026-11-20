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

`data.js` holds the dataset as a plain JS global. The entry screen compares a normalised password (lowercase, spaces and hyphens stripped) before rendering the list. No fetch, no WebCrypto, so it works in any browser, including in-app webviews.

`antalya2026` is the password. Case, spaces and hyphens are ignored.

This is a share gate, not a security boundary. The dataset is visible in the page source to anyone who looks. Every document in it is public, so that is an accepted trade-off. If the tracker ever holds anything non-public, move it behind Cloudflare Access or a host with server-side auth.

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
