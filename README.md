# National Electrification Plans Tracker

Static tracker of national electrification plans, roadmaps and strategies published in the run-up to COP31.
Password-gated, sortable, searchable, with a source and PDF link on every entry.

Live: https://electrifysimon.github.io/electrification-plans-tracker/

## What is in it

18 entries, as of 20 November 2026:

- 10 countries with a published 2026 national plan, roadmap or strategy
- 3 of those are energy access plans (Zambia, Ethiopia, Mozambique)
- 1 regional bloc instrument (EU Electrification Action Plan)
- 6 watchlist entries (Korea, Indonesia, Philippines, Peru, Rwanda, Kenya) flagged as in preparation, existing but not new, or no plan found

Every entry carries the publisher, publication date, scope, a one-paragraph summary, the source URL, and a PDF link where a public PDF exists. Entries built from trade or press reporting rather than the publisher's own document are marked `Secondary` in the detail panel.

## How the password works

`data.enc.json` holds the dataset encrypted with AES-GCM 256. The key is derived from the password with PBKDF2-SHA256, 310,000 iterations, a random salt and a random IV. Nothing renders until the browser decrypts the payload.

This is a client-side gate. The HTML shell is public, and anyone who obtains the password can read the data. It is proportionate for a research tracker of public documents, not for confidential material. If the data ever becomes sensitive, move to a host with server-side auth.

## Update the data

```bash
# edit the plaintext dataset (never committed)
$EDITOR src/data.json

# re-encrypt with the password
TRACKER_PASSWORD="$(cat ~/.config/electrification-tracker/password)" python3 build.py

git add data.enc.json && git commit -m "update data" && git push
```

The plaintext `src/data.json` is gitignored on purpose. Only the ciphertext ships.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole app: lock screen, list, filters, detail panel. No dependencies. |
| `data.enc.json` | Encrypted dataset. |
| `build.py` | Encrypts `src/data.json` into `data.enc.json`. |
| `DESIGN.md` | Design token spec the UI is built from. |
| `src/data.json` | Plaintext dataset, local only. |

## Design

Tokens live in `DESIGN.md` (design-md spec). Surface archetype is Explore: filters, ordered rows, a detail sheet. No hero, no marketing framing. Iowan Old Style for country names, system sans for body, one accent colour.
