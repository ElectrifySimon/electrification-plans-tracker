---
version: alpha
name: Antalya Tracker
description: An institutional research catalogue. Dense, quiet, built for scanning 18 documents, not for selling anything.
colors:
  ink: "#101614"
  paper: "#F7F6F2"
  surface: "#FFFFFF"
  muted: "#6B736E"
  border: "#DEDCD2"
  accent: "#1F6F5C"
  accent-weak: "#E7EFEB"
  flag: "#8A5A00"
typography:
  display:
    fontFamily: Iowan Old Style
    fontSize: 1.6rem
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  h2:
    fontFamily: Iowan Old Style
    fontSize: 1.25rem
    fontWeight: 600
    lineHeight: 1.25
  body-md:
    fontFamily: system-ui
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: system-ui
    fontSize: 0.72rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.08em"
rounded:
  sm: 2px
  md: 4px
  lg: 8px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "#FFFFFF"
  field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 10px
  chip-active:
    backgroundColor: "{colors.accent}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 6px
  chip-idle:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 6px
---

## Overview

A working catalogue for institutional staff. The surface is **Explore**: the user arrives to find a document, filter it down, and open the source. Every element either narrows the set, orders it, or describes one entry.

No hero. No feature cards. The counts strip is generated from the data, never written by hand.

## Colors

- **Ink (#101614):** text and the top rule.
- **Paper (#F7F6F2):** page field, warmer than grey so long reading sessions do not glare.
- **Accent (#1F6F5C):** deep teal-green. Used for the active filter, links and the focus ring. One accent only.
- **Flag (#8A5A00):** amber for the watchlist and secondary-sourced entries. Never used for decoration.

## Typography

Iowan Old Style (falling back to Palatino, Georgia) for the wordmark and country names. System sans for everything else. Dates set in tabular numerals so the column aligns.

## Layout

A single column capped at 1180px. Sticky control bar above a list. Rows on desktop with fixed columns; the same rows stack into cards below 720px. Detail opens in a right-side panel on desktop and a full-height sheet on mobile.

## Elevation & Depth

No shadows except the detail sheet. Borders carry structure.

## Shapes

2px radii. Institutional, not soft. Chips and fields share the same radius.

## Components

`button-primary` is the unlock action. Chips are filters, never navigation. Rows have a hover tint, not a left accent rail.

## Do's and Don'ts

- Do let the data drive every number on the page.
- Do keep the source link visible on every row.
- Don't add logos, flags, gradients or icon toppers.
- Don't describe a document as a country plan when it is a bloc or a transport strategy.
