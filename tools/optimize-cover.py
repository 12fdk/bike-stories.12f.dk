#!/usr/bin/env python3
"""optimize-cover.py — make the WebP variant of a post cover.

`build.py` already prefers `images/blog/<slug>.webp` over the PNG when one
exists (see `Post.card_image`) — but nothing ever wrote one, so every post
shipped its raw PNG. The first ComfyUI-generated cover was **885 KB**, served
eagerly with `fetchpriority="high"`: it is the LCP element on the post page, and
a photograph in PNG is simply the wrong format. The branded fallback card from
`make-cover.py` is flat colour and compresses fine either way; a photograph does
not.

    python3 tools/optimize-cover.py <slug>      # one post
    python3 tools/optimize-cover.py --all       # every cover missing a .webp

Run it after generating a cover and before `build.py`. Needs Pillow, which the
agent container already has. The PNG stays on disk: it is the source of truth
for the cover's dimensions (`build.py` reads them from its header) and the
fallback for anything that cannot take WebP.
"""

import argparse
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BLOG_IMAGES = ROOT / "images" / "blog"
QUALITY = 82
TARGET_KB = 200


def convert(png: Path, force: bool) -> bool:
    webp = png.with_suffix(".webp")
    if webp.exists() and not force:
        print(f"  {webp.name}: exists, skipped")
        return False
    im = Image.open(png).convert("RGB")
    im.save(webp, "WEBP", quality=QUALITY, method=6)
    before, after = png.stat().st_size // 1024, webp.stat().st_size // 1024
    note = "" if after <= TARGET_KB else f"  (still over {TARGET_KB} KB — check the source)"
    print(f"  {webp.name}: {before} KB PNG -> {after} KB WebP{note}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?", help="post slug (without .png)")
    ap.add_argument("--all", action="store_true", help="every cover without a .webp")
    ap.add_argument("--force", action="store_true", help="rewrite an existing .webp")
    a = ap.parse_args()

    if a.all:
        pngs = sorted(BLOG_IMAGES.glob("*.png"))
    elif a.slug:
        pngs = [BLOG_IMAGES / f"{a.slug}.png"]
    else:
        ap.error("give a slug or --all")

    missing = [p for p in pngs if not p.exists()]
    if missing:
        print(f"no such cover: {', '.join(str(p) for p in missing)}", file=sys.stderr)
        return 2

    print(f"Optimizing {len(pngs)} cover(s):")
    for png in pngs:
        convert(png, a.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
