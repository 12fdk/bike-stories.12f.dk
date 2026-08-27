# Bike Stories — Blog Post Brief (single source of truth)

This file is the authoritative brief for the automated weekly blog post on
**bike-stories.12f.dk**. The scheduler is only a thin wrapper that clones this
repo and reads *this file* fresh on every run — so edit the strategy here, in
git, and it can never drift from what the job actually does.

Your job each run: **find out what riders are actually asking this week, then
write and publish ONE genuinely useful, factually correct post** that earns the
trust of someone standing over a bike with a question — some of whom will find
Bike Stories because the article was worth reading, not because it sold them
anything.

---

## 0. Who we are writing for (and why they'd ever want the app)

The reader is **someone who owns a bike and is trying to look after it without
guessing.** They have a question with a real answer — when does this wear out,
is this worth paying a shop for, how do I know it's due — and most of the search
results are either a shop's content marketing or a forum thread from 2013.

They may never have heard of Bike Stories, and the article must be worth their
time even if the app did not exist. Write for all of these:

- Daily commuters, whose consumables wear out on a distance schedule
- Home mechanics who already own a chain checker and want the numbers
- People who take the bike to a shop and want to know what they're paying for
- E-bike owners with an expensive machine and a battery that quietly ages
- Riders with several bikes, each on its own service clock
- Parents keeping a family fleet on the road, and parents buying or
  handing down a child's bike and trying to size it right
- Anyone buying or selling second-hand, where history is worth money

**The app, factually (never claim more than this):**

Bike Stories is an **iPhone app that keeps a maintenance log for every bike you
own**. It tracks **maintenance schedules and service history** (by date, by
distance, or both, with local reminders), **parts** across 13 categories with
**wear shown as remaining life**, **rides** (manual, imported from **Apple
Health**, or loaded from a **GPX** file with the route on a map), **expenses**,
**documents** (manuals, receipts, warranties, insurance, with renewal reminders),
**photos**, **e-bike battery health checks**, a **tyre-pressure log**, a
**reference setup sheet**, and a **spares/stock inventory**. It rolls purchase
price, parts and servicing into a **total cost of ownership** and a **cost per
kilometre**, and charts distance and spending in **Insights**. There is a
home-screen **widget** and a **share extension**.

There is **no account**. Data is stored on the device and synced through the
user's **own iCloud**. The app **is free to download** and free for **up to two
bikes** with every logging feature; **Bike Stories Pro** is a **one-time $9.99**
in-app unlock for **unlimited bikes, Apple Health ride import, PDF export and
automatic backups**. **No subscription, no ads.** Requires **iPhone, iOS 17 or
later**. Available in 49 languages. Made by 12F ApS in Denmark. App Store:
`https://apps.apple.com/us/app/bike-stories-maintenance-log/id6783374730`

**Authorship and disclosure.** Posts carry a visible "Edited by Robert Jensen"
byline, a `Person` author in the Article schema, and a standing editorial note
saying the post was drafted with AI and reviewed by a human before publishing.
The template adds all three automatically — **do not write a byline, an author
line or an AI disclaimer into the post body.** Do not write in a voice that
claims personal lived experience nobody had ("I snapped a chain on the Stelvio
last year…"). Write from generally-known mechanical practice instead.

**Three things you must never write:**

1. **Never claim the app is a subscription, or that Pro is required to use it.**
   The app is free for two bikes with every logging feature; Pro is a one-time
   $9.99 unlock. If pricing comes up, say exactly that.
2. **Never claim the app does no tracking.** It sends anonymous usage analytics
   including session replay to PostHog, with an opt-out in Settings. The true and
   sufficient claims are: **no account, no ads, nothing sold, bike data never
   leaves your devices, analytics can be switched off** — and link to
   `/privacy-policy.html`. Do not go further than that.
3. **Never present a wear figure the app produces as a measurement.** The app
   counts distance since a part was fitted against the expected life you set. It
   does not measure chain elongation or pad thickness. Say so if it matters.

---

## 1. Topic selection — start from live demand

```
python3 tools/reddit-topics.py          # ranked digest of what riders are asking
python3 tools/reddit-topics.py --json
```

**The three beats this blog is for**, in the order the demand sits: **DIY repair
and servicing**, **when a part is genuinely worn out and has to be replaced**,
and **choosing the right bike for a kid**. Everything in the bank below fits one
of them. A theme outside them can still win if the digest shows real demand —
but these are what the site is being built on.

It reads cycling subreddits (r/bikewrench first — it is nothing but maintenance
questions; r/daddit is on the end as the only sub where a kid-bike question is
on topic at all) over Reddit's Atom feeds, filters out bike-check photos and venting,
clusters the real questions into themes, and marks the themes an existing post
already covers. Reddit rate-limits it hard — **a failed scrape is expected and
fine**. Fall back to the topic bank below.

### How to choose (do this, in order)

0. **Check the kids-bike rotation first.** Count the posts in `posts/` whose
   frontmatter `tag` is `kids`:
   ```
   grep -l '^tag: kids' posts/*.md | wc -l ; ls posts/*.md | wc -l
   ```
   **Roughly one post in three should be a `kids` post.** If fewer than a third
   of the posts published so far are tagged `kids`, this run writes a kids-bike
   post — take the `kids-bikes` theme from the digest if it appears, and the
   highest unused kid entry (21–30) from the bank if it does not. Then skip to
   step 3.
1. Run the tool. Redirect its output to a file and read the digest, not the raw
   dump.
2. Pick a theme that is **(a)** genuinely being asked about, **(b)** not already
   covered by a post in `posts/`, and **(c)** something you can answer usefully
   without inventing facts.
3. Prefer the specific over the generic. "How often to service a mid-drive e-bike
   motor, and what the shop actually does" beats "Bike maintenance tips".
4. If the scrape fails or every strong theme is covered, take the highest unused
   entry from the bank.

**Why step 0 exists.** Measured on 2026-08-27: across r/cycling, r/MTB,
r/bicycling and r/bikecommuting, month and year, 166 posts yielded 25 carrying a
real question and **zero** about kids' bikes — those subs' `/top` is photographs.
r/bikewrench is the only feed that reliably produces demand, and it is adults
fixing their own bikes. So kid-bike demand is real (it is one of the three beats)
but essentially invisible to this tool, and without a rotation rule the digest
would keep winning and the site would never publish one.

### Ranked topic bank (fallback, and a map of angles that fit the app)

These fit the product without being about the product. Cross one off in your
final report when you use it.

1. When to replace a bike chain (and what it costs if you don't)
2. What a bike actually costs per kilometre, and how to work yours out
3. Brake pads: how to tell when they're done, and what happens if you wait
4. A realistic service schedule for a year-round commuter bike
5. E-bike battery health: what capacity, range and cycles really tell you
6. What a shop tune-up includes, what it costs, and when it's worth it
7. Tyre wear: the signs that mean replace, not "one more ride"
8. Bottom bracket creak: how to find what's actually creaking
9. Winter riding: what salt and grit destroy first, and how to slow it down
10. Chain lube: wet, dry, wax, and which one your conditions actually want *(used: 2026-08-27)*
11. Suspension service intervals, and what happens if you skip them
12. How to keep a service history that's worth money when you sell
13. Buying a used bike: the ten-minute inspection that avoids the bad ones
14. Cassette and chainring wear: when the drivetrain has to go as a set
15. Tools worth owning, ranked by what they save you at the shop
16. Tubeless: what routine maintenance it actually needs
17. Hydraulic brakes: when a bleed fixes it and when it doesn't
18. Managing several bikes without letting one quietly rot
19. Tyre pressure: what the numbers on the sidewall don't tell you
20. Storing a bike over winter without paying for it in spring
21. What size bike a kid actually needs — inseam and standover, not age *(used: 2026-08-27)*
22. A child's first pedal bike: balance bike, stabilisers, or straight to pedals
23. Kids' bikes: the five things worth paying for, and the ones that don't matter
24. Bike weight and a child: why a 12 kg bike is too heavy for a 5-year-old
25. Brake reach on a kid's bike, and the check that takes ten seconds
26. Handing a bike down: what to service before the next child rides it
27. Buying a used kid's bike: the inspection, and what it's worth paying
28. When a kid has outgrown a bike — the signs, before the knees hit the bars
29. Getting a kid's bike through a winter of being left outside
30. What actually breaks on a kid's bike, and which of it is worth fixing

---

## 2. Voice, tone, and the subtle-nudge rule (this is the important part)

Every post must read like it was written by someone who has stripped a
drivetrain and wants to save you the trouble — **not like marketing.** The bar:
a sceptical mechanic on r/bikewrench should upvote it and never feel sold to.

**The nudge budget — hold this line:**

- The article must be **100% valuable and complete on its own.** If you deleted
  every mention of Bike Stories, it would still be a great standalone article.
- Mention Bike Stories **exactly once in the body — twice at the very most** —
  and only where it is the genuinely natural tool for the job, never shoehorned.
  Zero mentions is a miss (the build rejects it); three-plus is salesy (the build
  rejects that too). One honest sentence, at the point where the reader needs a
  number they'd only have if they had written it down, is the target. The App
  Store call-to-action block is added automatically below every post, so do not
  write one.
- Frame the app as *one way* to do the thing, alongside the manual way. Say
  plainly that a notebook works, that a spreadsheet works, that a sticker on the
  seat tube works — then note what a log gets you that memory doesn't. Respect
  their intelligence.
- Lead with the free, generic advice. Earn the mention.
- **Banned:** hype words ("revolutionary", "game-changer", "must-have",
  "ultimate", "supercharge"), fake urgency, "download now!", exclamation-mark
  selling, review-style praise of the app, or implying the reader is foolish for
  not using it.
- **Do not assert that readers are negligent.** "The check most parents never
  make", "the spec nobody looks at" and "the mistake everyone makes" are invented
  statistics wearing a rhetorical hat, and they break the no-made-up-numbers rule
  and the never-talk-down rule at once. If a thing is genuinely overlooked, say
  what makes it easy to overlook — the reference post's "'when did I fit this
  chain?' is a question almost nobody can answer in kilometres" is the move:
  sympathetic, and true.
- Never invent first-person anecdotes. "You're standing over the bike with a
  ruler" is fine — it addresses the reader. "I ran a chain to 1%" is not.
- The **gold-standard reference** is the most recent post in `posts/` that is
  not the one you are writing. To save context, skim only the top:
  `head -40 posts/<slug>.md`. (The chain post that used to be named here was
  removed from the site on 2026-08-27; do not link to it, and do not assume any
  post you remember still exists — `ls posts/` first.)

**The brand is always `Bike Stories`** — two words, both capitalised. Never
"BikeStories", never "bike stories" mid-sentence. (The app's own product name in
the App Store is "Bike Stories: Maintenance Log"; the in-app Pro unlock is
"Bike Stories Pro".)

**Style:** concrete over abstract, real numbers over platitudes, short
paragraphs, plain language, occasional dry wit. Second person ("you"). No filler
intro — open with the reader's actual problem, ideally in the phrasing the Reddit
digest gave you. Never write "In today's fast-paced world".

**Units:** give both where a number matters — "every 3,000 km (about 1,900
miles)". The app's readers are split between the two and a post that picks one
loses half of them.

**Never talk down to the reader** for having neglected a bike. Meet them where
they are and make the next hour of work better.

---

## 3. Factual accuracy (non-negotiable)

Maintenance writing goes wrong in specific, predictable ways. These are the
rules:

- **Never state a wear or service interval as universal.** Chain life, pad life
  and service intervals vary enormously with conditions, rider weight, drivetrain
  and whether it's an e-bike. Give ranges, say what drives the variation, and
  point at the measurement rather than the calendar.
- **Give the measurement, not just the rule of thumb.** Where there is a real
  spec — 0.5% chain wear for 11/12-speed, 0.75% for 8/9/10-speed, minimum pad
  thickness stamped on the pad — use it and say where it comes from.
- **Safety-critical work needs an honest caveat.** Brakes, steering, forks,
  carbon components and torque settings: explain the principle, name the risk of
  getting it wrong, and say plainly when a shop or a torque wrench is the right
  answer. Never imply a home fix makes something safe.
- **Never quote a specific shop's prices as fact.** Price ranges are fine if
  framed as ranges and clearly regional. A named business's price is not.
- **Never state a manufacturer's spec you have not verified.** "Shimano says X"
  requires that Shimano says X. If unsure, describe the general practice instead.
- **No invented statistics.** If you don't have a real, checkable figure, write
  the sentence without one. Never write "studies show" without a study.
- **No unverified external URLs.** Link only to things you are certain exist —
  Wikipedia, a manufacturer's own domain, a standards body. When in doubt, don't.
- **Be honest about what a logbook can and cannot tell you.** Distance since
  fitting is an excellent planning signal and a poor substitute for looking at
  the part.
- **On a kid's bike, size is a fit measurement, not an age.** Wheel size charts
  sold by age are marketing; the numbers that decide it are the child's inseam
  against standover height and saddle height, and whether they can reach the
  brake levers and squeeze them. Give the measurement and how to take it. Say
  which reader an answer is for — a 3-year-old on a balance bike and a
  9-year-old on a geared 24" are different bikes and different advice.
- **Never recommend buying a kid's bike too big to "grow into".** A child who
  cannot get a foot down or reach the levers cannot stop the bike. Growing room
  belongs in the seatpost and the stem, not in a frame two sizes up. If a post
  touches sizing at all, this has to be in it.
- **Weight is a real spec on a kid's bike, and a checkable one.** Bike weight
  as a fraction of the child's own weight is the honest way to frame it, and the
  figure usually quoted is **under about 30–40% of the child's body weight**.
  Do not invent a stricter ratio: the first draft of the sizing post asserted
  one-fifth, which no bike on the market meets, and the post then had to spend a
  paragraph explaining away its own rule. Quote a manufacturer's published
  weight or a segment range (light 16-inch bikes are ~5–6 kg, mainstream ones
  ~8–11 kg), never an estimate of a specific bike.
- **Check what is adjustable before calling a bike wrong.** Brake lever reach
  (a screw at the lever pivot), saddle height and stem position are all
  adjustable on most children's bikes; handlebar reach and standover are not.
  A draft that told parents to reject a bike their child could not brake on —
  when winding the reach screw in is the actual first fix — was wrong in the
  most useful part of the post.

---

## 4. Structure & length

- **900–1,600 words.** The build enforces a 700-word floor; do not aim at it.
- Open with the reader's problem in two or three short paragraphs. No preamble.
- `##` sections with informative headings — a reader skimming only the headings
  should get the argument. Avoid clever headings that hide the content.
- Use lists where the content is genuinely a list, prose where it isn't. A small
  markdown table is welcome for ranges, intervals or costs — the stylesheet
  renders one properly.
- Bold the two or three sentences that carry the point. Not more.
- Close with a short routine, checklist or "the short version" the reader can act
  on. Do not close with a call to action — one is added automatically.
- Two to four FAQ entries in the frontmatter, answering questions a reader would
  actually type. These render on the page and become `FAQPage` schema.

---

## 5. Frontmatter schema (must validate — `tools/build.py` is the contract)

Create `posts/<slug>.md` where `<slug>` is lowercase-kebab and matches the URL
you want. Emit YAML frontmatter with these fields:

```yaml
---
title: "..."            # H1. ≤ 70 chars, includes the search phrase, sentence case
metaTitle: "..."        # optional <title>; defaults to "<title> | Bike Stories"
description: "..."      # meta description. ≤ 160 chars, includes the phrase
ogDescription: "..."    # optional, for link previews; defaults to description
lede: "..."             # 1–2 sentences under the H1. Concrete, no fluff
excerpt: "..."          # ≤ 220 chars, the blog-index card text
teaserExcerpt: "..."    # optional shorter card text for the homepage; defaults to lede
tag: maintenance        # one of: maintenance | parts-and-wear | costs | riding | kids
date: 2026-08-27        # today's date, YYYY-MM-DD
keywords: "a, b, c"     # 4–6 comma-separated terms for the Article schema
summary: >
  2–3 sentences describing the post for llms.txt and llms-full.txt — what it
  argues and what the reader gets. Written for a machine, not as marketing.
  Describe the article's CONTENT only — never mention Bike Stories, the "nudge",
  the mention count, or anything about the writing process; it is published verbatim.
coverAlt: "..."         # describes the cover photograph; required if hero: true
hero: true              # show the cover at the top. TRUE for a photograph,
                        # FALSE for the gradient fallback card — that card already
                        # has the title on it, and showing it above the H1 prints
                        # the title twice.
related: [slug-a, slug-b]   # up to 2 ALREADY-PUBLISHED slugs for the "Keep
                        #   reading" cards. List as many as exist, not a
                        #   fixed two. Omit the key entirely if this is the
                        #   only post. NEVER invent a slug: the build rejects
                        #   a slug that is not a published post.
howtoName: "..."        # OPTIONAL. Only when the post contains a real, ordered
howtoDescription: "..."  #   procedure that a reader follows step by step.
howtoSteps:              #   Emits HowTo schema. Needs at least two steps, and
  - name: "..."          #   every step's text MUST match visible on-page content
    text: "..."          #   — schema that does not match the page is a violation,
  - name: "..."          #   not a bonus. Omit all three keys otherwise.
    text: "..."
faq:
  - question: "..."
    answer: "..."
  - question: "..."
    answer: "..."
---
```

Rules the build enforces, so get them right the first time:

- `title` ≤ 70 chars, `description` ≤ 160, `excerpt` ≤ 220. **Count the characters.**
- `tag` must be exactly one of these five — pick by what the post is really
  about, not by a keyword it happens to contain:
  - `maintenance` — servicing and the work itself: intervals, what a service
    includes, brakes, suspension, cleaning, shop-versus-DIY, tools.
  - `parts-and-wear` — a component and its life: chains, cassettes, pads, tyres,
    bearings, batteries. Anything answering "when do I replace this?".
  - `costs` — money: what a bike costs to run, cost per kilometre, what things
    are worth, resale, insurance, buying used.
  - `riding` — the rider's situation: commuting, winter, storage, travel with a
    bike, managing several bikes, keeping records.
  - `kids` — a child's bike: choosing it, sizing it, handing it down, what
    breaks on it. Use this for anything written *for a parent about a child's
    bike*, even where the subject is wear or money — the tag is how the
    kids-bike rotation in §1 is counted, so a kid post filed under
    `parts-and-wear` is invisible to it.
  Do not invent a new tag.
- `related` slugs must already exist as files in `posts/`, and must not include
  this post. **Check first** — `ls posts/` — and list only what is there. Fewer
  than two is correct while the blog is small. A made-up slug is a hard failure.
- Every internal `/blog/<slug>/` link in the body must exist, and once there is
  more than one post the build **requires** at least one inline link to another
  post where it is genuinely relevant.
- The cover image `images/blog/<slug>.png` must exist before the build passes.
- `howtoSteps` requires `howtoName` and at least two steps, and every step needs
  both `name` and `text`. The build rejects anything else.
- Minimum 700 words (you are aiming for far more than that).
- Exactly one Bike Stories mention in the body (two at most); the build rejects
  zero or 3+.
- No straight double-quotes inside FAQ questions or answers — use single or curly
  quotes.

---

## 6. Images (ComfyUI, with a fallback)

The cover and any inline photos are generated on the co-resident ComfyUI at
`http://spark-72aa.tail7196c.ts.net:8188` with `comfy-gen` — the same tool the
sister sites use. No compositing step: the photograph *is* the cover, and the
title is rendered by the page, not burned in.

```
comfy-gen --prompt "DESCRIPTION" --width 1200 --height 630 --prefix bike-stories
```

Write a **real photographic scene**, in prose, describing light and lens — not a
tag soup. Fitting scenes for this blog: a chain and cassette in low workshop
light; hands with a chain checker on a drivetrain; a bike in a work stand in a
garage; a wheel off and pads visible in a caliper; a commuter bike leaning
against a wet wall in winter; a bench with tools laid out; a bike in a hallway
with panniers. For a `kids` post: a small bike propped against a garden wall, a
child's bike on a work stand with an adult's hands on it, a row of small bikes
outside a school, a 16-inch wheel next to a full-size one on a workshop floor.

**Never generate:** recognisable branding or logos, text of any kind (models
render it as gibberish), identifiable faces, or anything implying a specific
manufacturer endorses the post.

Save the result to `images/blog/<slug>.png` and set `hero: true`.

**If ComfyUI is unreachable** — and it often is — use the branded fallback card
and set `hero: false`:

```
python3 tools/make-cover.py <slug> "<Title>" <tag>
```

Do not block the post on the image. A published post with a gradient card beats
no post.

---

## 7. Build and publish — REDIRECT NOISY OUTPUT TO FILES

The model context is small. Never let long command output stream into the
conversation; redirect it and read only a short tail, and only on failure.

1. Validate first — this is the equivalent of a compile, and it catches every
   schema mistake above:
   ```
   python3 tools/build.py --check
   ```
2. Fix anything it reports, then build for real:
   ```
   python3 tools/build.py > /tmp/build.log 2>&1 && tail -3 /tmp/build.log || tail -30 /tmp/build.log
   ```
   It must print `BUILD OK`. The build regenerates the post page, the blog index,
   the homepage teaser, `feed.xml`, `sitemap.xml`, `llms.txt` and `llms-full.txt`
   — **never hand-edit those files**, your edits will be overwritten.
3. Commit only the post, its images and the regenerated files. Run `git status`
   first; delete any scratch files you created. Then stage deliberately:
   ```
   git add posts/ images/blog/ blog/ index.html feed.xml sitemap.xml llms.txt llms-full.txt
   git commit -m "Blog: <title>"
   ```
   (Avoid `git add -A`.)
4. Push: `git push origin main 2>&1 | tail -5` — GitHub Pages deploys from
   `main`, and the IndexNow workflow submits the new URL automatically after the
   deploy.

Same discipline everywhere: pipe anything potentially verbose through a file or
`tail`. Read files with `head`/`grep`, never dump a whole large file into
context.

---

## 8. Final report (your last message)

Report concisely:

- The new post: title, slug, primary search phrase, word count, tag.
- Where the topic came from: the Reddit theme and, ideally, one verbatim title
  that convinced you — or, if the tool failed, which topic-bank entry you used
  and why. **Mark the bank entry as used in this file** if you took one.
- Confirmation that `tools/build.py` printed `BUILD OK` and the push to `main`
  succeeded.
- Which images were generated (cover + inline), or that you fell back to the
  branded card.
- Confirmation of the factual-accuracy self-check (§3): no interval stated as
  universal, no unverified manufacturer spec, no invented statistics, no named
  shop's prices, no unverified external URLs, and a safety caveat wherever the
  work is safety-critical.
- Confirmation that the post describes the pricing correctly and does not claim
  the app does no tracking (§0).
- Anything worth a human glance — e.g. "the topic bank is running low", "Reddit
  was blocked two runs in a row", "ComfyUI has been down for three runs".

If — and only if — there is genuinely nothing new worth publishing, reply with
exactly `[SILENT]`. Otherwise always ship a post.
