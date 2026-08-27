# Bike Stories landing page + blog

Marketing site and blog for the **Bike Stories** iOS app (bike maintenance log,
parts, mileage and cost tracker), deployed via **GitHub Pages** at
**bike-stories.12f.dk**. Built by 12F ApS.

- App Store: <https://apps.apple.com/us/app/bike-stories-maintenance-log/id6783374730>
  (app id `6783374730`, bundle `12f.bike-stories`, Health & Fitness / Sports,
  iOS 17+, **free with a one-time $9.99 Pro unlock**, currently 0 ratings)
- App repo: `12fdk/bike-stories` (local: `/Users/robert/Git/bike-stories`) —
  separate repo; this one is the marketing site only.
- Site repo: `12fdk/bike-stories.12f.dk`

## The one job of this site

**Convert cold traffic into App Store downloads, and downloads into Pro
unlocks.** Every decision — layout, copy, section order, blog topic — is judged
on "does this make someone who owns a bike install the app and start logging?"
There is no other goal: no newsletter, no lead capture, no community, no docs.

Two funnels feed it:

1. **Direct / App Store referral** — the landing page does the whole job in one
   scroll. The app is free, so the ask is small; the page's real work is
   convincing someone that logging is worth the effort at all.
2. **Search + AI answer engines** — the blog earns organic visibility for
   "when to replace X" style maintenance queries and pipes readers into the same
   CTA.

## Hard content rules

- **Get the pricing right, always.** The app is **free to download and free for
  up to two bikes with every logging feature**. **Bike Stories Pro** is a
  **one-time $9.99 in-app purchase** (product `12f.bike_stories.pro`, ASC id
  `6783646913`) unlocking **unlimited bikes, Apple Health ride import, PDF export
  and automatic backups** (`PremiumManager.swift` is the canonical gate list).
  Never call it a subscription; never imply the free tier is a trial.
- **Never claim the app does no tracking.** It ships the PostHog SDK with session
  replay, default-on, with an opt-out in Settings → Privacy
  (`TelemetryManager.swift`). The true and sufficient claims are: **no account,
  no ads, nothing sold, bike data never leaves your devices, analytics can be
  switched off** — plus a link to `/privacy-policy.html`.
- **No invented testimonials or star ratings.** The app has **0 public ratings**.
  Use *personas*, like the sister sites do. No `aggregateRating` in the schema
  until real ratings exist.
- **Never present the app's wear percentage as a measurement.** It counts distance
  ridden since a part was fitted against the expected life the user set. It does
  not measure chain elongation or pad thickness.
- Everything on the page must be true of the shipped app. When in doubt, check
  `/Users/robert/Git/bike-stories/fastlane/metadata/en-US/description.txt`,
  `design.md`, and the models under `bike-stories/Models/`.

## The product, factually (source of truth for all copy)

Bike Stories is an iPhone app that keeps a maintenance log for every bike you
own, and works out what each one actually costs. No account; data lives on the
device (SwiftData in an App Group, shared with the widget and share extension)
and is mirrored to the user's **own iCloud** via CloudKit.

| Feature | The line that sells it |
|---|---|
| Cost of ownership | Purchase + parts + service, and cost per kilometre |
| Maintenance schedules | Due by date, by distance, or both — with reminders |
| Service history | What was done, when, what it cost |
| Parts + wear | 13 categories, remaining life as a bar |
| Rides | Manual, Apple Health import (Pro), or GPX with a route map |
| Documents | Manuals, receipts, warranties, insurance + renewal reminders |
| Insights | Distance per month, riding by weekday, spending over time |
| E-bike battery | Capacity, range and charge cycles over time |
| Tyre pressure + setup | Front/rear log, charted, against a reference sheet |
| Spares & stock | What's on the shelf, deducted when fitted |
| Widget + share extension | The garage on the home screen; file a photo from any app |
| Privacy | No account, own iCloud, analytics you can switch off |

13 bike types, 13 part categories, 10 preset service types. Localized into 49
App Store locales; the *site* ships English-only for now.

## Brand — must match the app

**The site's design and colours are the app's.** Two families, two jobs:

- **The identity is the app icon** — a white chainring + wrench on a deep
  steel-blue gradient, sampled from the shipped artwork: `#095B89 → #00436B`,
  deepened to `#002E4C` for the closing band. Unlike a bright ramp it carries
  **white** copy (7.4:1), so it does every full-bleed band.
- **The interface is Garmin Blue**, `AccentColor` = `#007CC3`, with
  `#00689F` for link text on white and `#2A9FD6` on dark. Same job here as in the
  app: buttons, links, active states.

Functional colours are fixed: **green `#4CAF50`** = serviced/OK ·
**orange `#F0A030`** = due soon · **red `#E5402A`** = overdue. Cost-breakdown
segments (accent / teal `#2EA8E0` / orange / violet `#9B59B6`) appear **only** in
the cost breakdown. Never decorate with any of them.

- System font stack; metrics get `font-stretch: 88%` + tabular figures, the web
  equivalent of the app's condensed monospaced numerals.
- **Buttons are rectangles with a 10px radius**, like `PrimaryButtonStyle` — not
  pills.
- Light **and** dark mode via CSS custom properties + `prefers-color-scheme`.
- Depth is a tone step + a hairline, not a shadow; only floating things get one.
- The app's liquid-glass language translates to a `.glass` treatment on the
  header, feature cards and the hero panel.

**The full spec — every token, component, breakpoint and the page anatomy — is in
`DESIGN.md`. Read it before writing any CSS or HTML.** `css/style.css` is the
source of truth for the token *values*.

## Structure

```
CLAUDE.md             this file — what the project is and the rules
DESIGN.md             the design system: tokens, components, page anatomy
index.html            landing page
posts/<slug>.md       BLOG SOURCE OF TRUTH — frontmatter + markdown, one per post
prompt.md             the brief the automated blog job follows
blog/index.html       GENERATED from posts/ by tools/build.py
blog/<slug>/index.html GENERATED — never hand-edit
about.html            who built it and why
privacy-policy.html   accurate to what the app actually does
404.html
css/style.css         the whole design system (tokens → components → responsive)
js/main.js            scroll reveals, sticky-header state, mobile nav
images/               icon, favicons, OG image, App Store badge,
                      screenshots/en-US/, blog/<slug>.png
tools/build.py        renders the blog + every file that lists posts
tools/make-cover.py   branded gradient cover card (Pillow) — ComfyUI-down fallback
tools/og-image.html   source for images/og-image.jpg (render at 1200x630)
tools/reddit-topics.py what riders are actually asking, ranked
feed.xml              RSS (generated)
CNAME                 bike-stories.12f.dk
robots.txt sitemap.xml llms.txt llms-full.txt   SEO + AI crawlers (blog parts generated)
b0b687723d7b1c12e407c2dfb52947d1.txt            IndexNow key
.github/workflows/indexnow.yml                  IndexNow submit on deploy
```

Use **absolute paths** (`/css/style.css`, `/images/...`) so blog subfolders
resolve.

## Blog — `posts/*.md` is the source of truth

The blog exists to **buy organic visibility**, and it is written by an **external
LLM job**, not by hand. The contract:

- Write markdown to `posts/<slug>.md` (frontmatter schema documented in
  `prompt.md` §5 and **enforced by the build**), generate a cover, then build.
- **Never hand-edit `blog/<slug>/index.html`** — it is overwritten.

```bash
python3 tools/make-cover.py <slug> "<Title>" <tag>   # → images/blog/<slug>.png
python3 tools/build.py --check                        # validate (schema, links, lengths)
python3 tools/build.py                                # write everything
python3 -m http.server 8000                           # preview
```

`tools/build.py` rewrites every derived file: post pages, the blog index grid +
schema.org, the homepage teaser, `feed.xml`, blog URLs in `sitemap.xml`, and the
`## Blog` sections of `llms.txt` / `llms-full.txt`. Generated regions inside
hand-written files are fenced with `BLOG:*:START` / `BLOG:*:END` markers — leave
them in place.

Tags (edit `TAGS` in `build.py` to change the set): `maintenance`,
`parts-and-wear`, `costs`, `riding`, `kids`. `kids` is load-bearing, not
decorative: `prompt.md` §1 step 0 counts `tag: kids` posts to keep roughly one
post in three about children's bikes, so a kid post filed under any other tag
is invisible to that rotation.

### The brief lives in `prompt.md`

`prompt.md` is the **authoritative brief** the automated job reads fresh on every
run. Change strategy by editing `prompt.md` here, in git — never by editing the
job. Same pattern as neareats.12f.dk, snapdeck.12f.dk, wrnty.12f.dk.

Non-negotiables encoded there: the post must be worth reading even if the app did
not exist; at most one natural mention + the automatic CTA; never state a service
interval as universal; give both km and miles; safety-critical work gets an
honest caveat; never quote a named shop's prices or an unverified manufacturer
spec.

Topic research: `python3 tools/reddit-topics.py` (Atom feeds, not the JSON API —
it 403s; paces, backs off on 429, caches to `.cache/` for a day, fails
gracefully). r/bikewrench first. `prompt.md` falls back to a ranked topic bank
when the scrape fails.

## SEO / GEO / AEO

- `sitemap.xml`, `robots.txt`, canonical URLs, OG + Twitter cards on every page.
- Schema.org: `SoftwareApplication` on the homepage (with **two `offers`** — the
  free app and the $9.99 Pro unlock — and **no** `aggregateRating` until real
  ratings exist), `HowTo`, `FAQPage`, `Organization`, plus `Article` +
  `BreadcrumbList` on posts.
- `llms.txt` / `llms-full.txt` for AI answer engines — this is where the app's
  factual description lives for LLM citation.
- **IndexNow** on every deploy: shared public key
  `b0b687723d7b1c12e407c2dfb52947d1` at the site root, plus the universal
  `.github/workflows/indexnow.yml`. Submits to Bing/Yandex/Seznam/Naver/Yep
  (Google doesn't participate — Search Console + sitemap covers it).
- The `seo-geo-aeo` skill audits the live site; run it after any significant
  content change.

## Development & deployment

```bash
python3 -m http.server 8000     # no build tools for the static pages
```

Push to `main` → GitHub Pages auto-deploys → IndexNow workflow submits changed
URLs. Per repo convention: **branch per task, GitHub issues are the task
tracker** (`gh issue list`), keep issue bodies updated as work progresses.

## Status

**The site is built** (2026-08-27): design system, assets, the full landing page,
about, privacy policy, 404, SEO plumbing, IndexNow, the blog engine with one seed
post, `prompt.md`, and the topic-research tool.

Open, and worth knowing about:

- **HSTS** — no `strict-transport-security` header. It is a Cloudflare edge
  setting, not a repo change.
- **Content volume is the constraint.** Five indexable URLs and one blog post.
  The weekly blog job (`prompt.md`) is written and ready; the cron on the spark
  is not set up yet. Nothing else on this site moves the needle as much.
- **App Store Connect** has no privacy-policy URL set for the app; point it at
  `https://bike-stories.12f.dk/privacy-policy.html`.
- Verify the property in Google Search Console and Bing Webmaster Tools and
  submit `sitemap.xml` (IndexNow covers Bing/Yandex/Seznam/Naver/Yep on deploy,
  but not Google).

Done since launch (SEO/GEO/AEO audit, 2026-08-27 — issues #2–#8):

- Umami is live on all six page templates (website id
  `851074a3-d8a2-4c1d-929a-138eea1f9161`), so the `data-umami-event`
  CTA instrumentation actually records.
- DNS resolves (Cloudflare-proxied) and HTTPS serves with Brotli.
- The H1 carries the target term; titles ≤60 and descriptions ≤155 sitewide.
- `hero: false` on gradient-card covers, so a post never prints its title twice.
- `build.py` gives blog cover images real alt text (`coverAlt`, falling back to
  the title) instead of `alt=""`.
- Optional `howtoName` / `howtoDescription` / `howtoSteps` frontmatter emits
  `HowTo` schema for posts containing a genuine procedure. Only use it when the
  steps match visible on-page text.
- `WebSite`, `Person` and `ContactPoint` entities added; `Organization.sameAs`
  lists only profiles 12F genuinely controls — never pad it.
- The hero WebP is preloaded (it is the LCP element).
