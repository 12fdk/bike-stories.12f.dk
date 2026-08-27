# Design system — bike-stories.12f.dk

This is the single source of truth for how the site looks. Every decision here
comes from the **app's own design system** (`/Users/robert/Git/bike-stories/design.md`
and `bike-stories/DesignSystem.swift`) — the site is the app's cockpit rendered
in HTML, not a separate brand. `css/style.css` holds the implemented token
values; if the two ever disagree, the CSS is what ships and this file is the bug.

Read this before writing any CSS or HTML for this site.

---

## 1. The one idea

The app is a **data cockpit**: the number is the hero, the label is a quiet
uppercase whisper above it, data is packed densely but always ruled by a card
edge or a hairline, and meaning is carried by typography weight and *functional*
colour — never decoration. The structure is adapted from Garmin Connect and
rendered on iOS's adaptive, translucent surfaces.

The site inherits all of that. Concretely, that means the page is built from the
same parts the app is built from — stat cells, stat grids, wear bars, status
pills, a cost-breakdown bar — rebuilt in HTML and shown *next to* the real
screenshots. A visitor who downloads the app should recognise the screen they
already saw on the website.

---

## 2. Colour

Three families, three jobs. Nothing else is invented.

### 2.1 Brand — the app icon

The icon is a **white chainring and wrench on a deep steel-blue gradient**,
sampled from the shipped 1024px artwork:

| Token | Value | Where it comes from |
|---|---|---|
| `--brand-1` | `#095B89` | icon gradient, top |
| `--brand-2` | `#00436B` | icon gradient, bottom |
| `--brand-3` | `#002E4C` | deepened one step, for the closing band |
| `--brand` | `linear-gradient(160deg, #095B89, #00436B)` | the icon, verbatim |
| `--on-brand` | `#FFFFFF` | 7.4:1 on `--brand-1` |

Unlike a bright gradient, this one **carries white copy comfortably**, which is
why the full-bleed bands (proof strip, Pro plan card, closing CTA, blog cover
cards, OG image) are brand blue with white text. There is no second "deep ramp"
family — the icon already is the dark end.

### 2.2 Accent — Garmin Blue, the app's `AccentColor`

| Token | Value | Job |
|---|---|---|
| `--accent` | `#007CC3` | buttons, active states, chart fills — the single interactive hue |
| `--accent-ink` | `#00689F` | the app's `accentPressed`; **link and small-text colour on white** (6.0:1 — `--accent` itself is only 4.55:1) |
| `--accent-bright` | `#2A9FD6` | the app's `accentOnDark`; accent glyphs on dark surfaces |
| `--accent-wash` | `rgba(0,124,195,.10)` | icon tiles, chips, the `.mark` highlight |

In dark mode `--accent-ink` flips to `#4FB4E4` so link text stays AA on the
near-black canvas.

### 2.3 Functional colours — fixed meaning, never decoration

Straight from the app. **These encode a status and that meaning never changes.**

| Token | Value | Means |
|---|---|---|
| `--ok` | `#4CAF50` | serviced, OK, life remaining |
| `--caution` | `#F0A030` | due soon, low remaining life |
| `--overdue` | `#E5402A` | overdue, error, destructive |

Each has an `-ink` variant for text (the raw hue fails contrast as small text)
and a `-wash` for chip and tile backgrounds.

**Cost-breakdown segments** are the app's four fixed data-viz hues and appear
*only* in the cost breakdown: purchase = `--accent`, parts = `#2EA8E0` teal,
maintenance = `--caution`, expenses = `#9B59B6` violet.

**Never use a functional colour to decorate.** An amber icon tile on a feature
card is only allowed where that feature is genuinely about "due soon".

### 2.4 Surfaces

The app's grouped-background family: a grey canvas with white cards on it.

| Token | Light | Dark | From |
|---|---|---|---|
| `--bg` | `#FFFFFF` | `#0A0B0E` | the page |
| `--bg-grouped` | `#F2F2F7` | `#000000` | `systemGroupedBackground` — banded sections |
| `--surface` | `#FFFFFF` | `#16181D` | `secondarySystemGroupedBackground` — cards |
| `--surface-raised` | `#F7F7FA` | `#1E2027` | `tertiarySystemGroupedBackground` |
| `--track` | `#E4E4EA` | `#26282F` | `quaternarySystemFill` — the unfilled part of a bar |
| `--line` | `#D8D8E0` | `#2E313A` | `separator` — the stat-grid "mortar" |
| `--ink` / `--ink-2` / `--ink-3` | | | `label` / `secondaryLabel` / `tertiaryLabel` |

Sections alternate white and `--bg-grouped`, which is what makes the page read
as iOS rather than as a landing page with a grey stripe.

Light and dark are **equal citizens** (app design.md §2). Everything is defined
as a token on `:root` and overridden in `prefers-color-scheme: dark`.

---

## 3. Typography

System font, no web fonts, no build step.

- **Prose, labels, headings:** `-apple-system` stack, normal width.
- **Metrics and numerals:** the same stack with `font-stretch: 88%`,
  `font-variant-numeric: tabular-nums` and `letter-spacing: -0.03em`. This is the
  web equivalent of the app's "condensed width + monospaced digits" rule: dense
  values fit a narrow stat cell and columns of numbers align. Applied via
  `.metric`, `.stat-value`, `.hero-metric-value`, `.strip-num`, `.plan-price`.
- **The unit is not the value.** `.unit` renders `km`, `mi`, `$`, `days` at
  0.52em, weight 600, in `--ink-3`, inline after the number — exactly as the app
  does it.
- **The eyebrow is a whisper:** `.eyebrow` and `.stat-label` are ~0.7rem, weight
  700, uppercase, tracked 0.08–0.1em, in a secondary colour.

Headings use tight negative tracking (-0.022 to -0.032em) and weight 700. Do not
go to 800 — the app's titles are `.bold`, not black.

---

## 4. Shape, depth and motion

- **Radii:** buttons `10px` (the app's `CornerRadius.sm` = 8, one step up for the
  larger canvas), cards `14px`, big cards `18px`, pills only for status chips.
  **Buttons are rectangles, not pills** — `PrimaryButtonStyle` is a solid accent
  rectangle with a white label, and the site's `.btn--primary` matches it.
- **Depth is a tone step plus a hairline, not a shadow.** Flat cards get
  `1px solid var(--line-soft)` and no shadow. Only genuinely floating things get
  one: the phone frames, the hero panel, the Pro plan card, the closing CTA.
- **Glass** (`.glass`) is the web translation of `.ultraThinMaterial`: translucent
  fill, 20px backdrop blur, a gradient hairline border and a 40px top shine. Use
  it **only over something** — a grouped band, a gradient — never over flat
  white, where there is nothing to blur. There is a `@supports` fallback to a
  solid surface.
- **Motion is small.** Fade-and-rise reveals at 0.55s, hover lifts of 2–3px,
  everything disabled under `prefers-reduced-motion`. The `.fade-in` initial
  state is inside `@media (scripting: enabled)` so a blocked `main.js` can never
  leave the page blank.

---

## 5. Components (the ones that carry the app's identity)

| Class | What it is |
|---|---|
| `.statgrid` / `.stat` | The app's stat grid. Cells sit on `--surface` with a **1px gap** over a `--line` background — that gap *is* the separator mortar. `.statgrid--3` / `--4` for wider grids. |
| `.hero-metric` | The single lead value on a dashboard: eyebrow above, big condensed number below. |
| `.wear` | A part's remaining life: label, percentage, a `--track` bar with an `--ok` / `--caution` / `--overdue` fill, and a sub-line. |
| `.costbar` + `.cost-legend` | The four fixed cost segments, always with an itemised legend carrying the amount. |
| `.pill` | Status chip — `--ok` / `--caution` / `--overdue` / `--info`, always with an icon. |
| `.phone` | CSS device frame around a 640px WebP screenshot. |
| `.feature` / `.feature-icon` | Feature card; the icon tile takes the colour the app gives that concept. |
| `.plans` / `.plan--premium` | Free versus Pro. The Pro card is the brand gradient with white copy. |
| `.vs` | Comparison table; collapses to stacked cards under 768px via `data-col` labels. |

---

## 6. Page anatomy (index.html, in order — the order is the argument)

1. **Hero** — headline, subhead, App Store badge, trust line; a phone showing the
   bike dashboard with a **glass stat panel floating over its right edge**, built
   from the same numbers. This is the site's signature image and the clearest
   statement that the site and the app are one thing.
2. **Proof strip** — brand band, four numbers.
3. **What is Bike Stories** — the plain definition an answer engine can lift,
   plus three question-shaped answers (`.answer-grid`).
4. **Features** — six cards on a grouped band, plus eight secondary items.
5. **How it works** — three steps, three phones.
6. **Cost of ownership** — copy + a rebuilt cost breakdown (`.split-demo`).
7. **Maintenance** — copy + the Maintenance screenshot.
8. **Parts & wear** — copy + rebuilt wear bars.
9. **Rides** — copy + two phones.
10. **Compare** — notebook in the shed vs. the app.
11. **Who it's for** — six personas. **Not testimonials** — the app has no public
    ratings, and inventing one is both a lie and a structured-data violation.
12. **Pricing** — Free and Pro side by side, honestly.
13. **Privacy** — what stays on the device, and the analytics opt-out.
14. **Blog teaser** — generated between the `BLOG:TEASER` markers.
15. **FAQ** — `<details>` items that mirror the `FAQPage` schema exactly.
16. **Closing CTA** — brand band.

A CTA is always within one screen of the reader: header, hero, pricing (×2),
closing, footer. Every page carries the Apple Smart App Banner.

---

## 7. Accessibility (non-negotiable, and inherited from the app)

- **Never convey status by colour alone.** Every wear bar carries its percentage,
  every cost segment carries its amount in the legend, every status pill carries
  an icon and a word. This is the app's §10 rule and it applies here.
- Contrast: body text and links meet AA. `--accent` is **not** used for small
  text on white (4.55:1) — `--accent-ink` is.
- Focus is always visible: a 3px `--accent` outline with 3px offset.
- One `<h1>` per page, headings in order, a skip link, `aria-current` on the
  active nav item, real `<table>` semantics with a `<caption>` for the comparison,
  and alt text that describes what a screenshot actually shows.
- Decorative rebuilt components (the hero panel) are `aria-hidden` — they repeat
  what the screenshot beside them already says.
- Tap targets are ≥44px (`.btn` has `min-height: 48px`).

---

## 8. Assets

- Screenshots: the **raw device captures** from
  `/Users/robert/Git/bike-stories/fastlane/screenshots/en-US/*.png` (not the
  framed store versions — the site supplies its own frame), resized to **640px
  WebP** at quality 82 into `images/screenshots/en-US/`. Never ship the 1206×2622
  PNGs to a browser.
- App icon → `images/icon.png` (512), `apple-touch-icon.png` (180), favicons.
- OG image: `tools/og-image.html` rendered at 1200×630 and saved as
  `images/og-image.jpg`.
- App Store badge is **self-hosted** at `/images/app-store-badge.svg`.
- Blog covers: ComfyUI photographs where possible, otherwise the branded gradient
  card from `tools/make-cover.py` (brand blue, white type).

Use **absolute paths** (`/css/style.css`, `/images/...`) everywhere, so pages in
`/blog/<slug>/` resolve correctly.
