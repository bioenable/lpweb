#!/usr/bin/env python3
"""Bulk HTML cutover: www host + header logo + favicons + sitemap/robots helpers.

Run from repo root: python3 scripts/cutover_www_and_logo.py
"""

from __future__ import annotations

import datetime as dt
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WWW = "https://www.launchpadi.com"
TODAY = dt.date.today().isoformat()

FAVICON_SNIPPET = """    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
"""

LOGO_IMG = (
    '<img src="images/logo-launchpad.svg" alt="LAUNCHPAD Admissions Intelligence" '
    'class="h-8 md:h-9 w-auto" width="200" height="40" decoding="async">'
)

# Brand anchor: text LAUNCHPADi → logo img; normalize href to index.htm
BRAND_RE = re.compile(
    r'<a\s+class="flex-none[^"]*"\s+href="[^"]*"\s+aria-label="Brand">\s*LAUNCHPADi\s*</a>',
    re.IGNORECASE,
)
BRAND_RE_ALT = re.compile(
    r'<a\s+class="flex-none[^"]*"\s+href="[^"]*"\s+aria-label="Brand">LAUNCHPADi</a>',
    re.IGNORECASE,
)

BRAND_REPLACEMENT = (
    f'<a class="flex-none focus:outline-hidden focus:opacity-80" '
    f'href="index.htm" aria-label="LAUNCHPAD Admissions Intelligence">{LOGO_IMG}</a>'
)

HERO_H1_RE = re.compile(
    r'(<h1 class="block font-bold text-purple-800 text-4xl md:text-5xl lg:text-6xl">)\s*'
    r"LAUNCHPADi\s*(</h1>)",
    re.IGNORECASE,
)

HERO_REPLACEMENT = (
    r'\1<img src="images/logo-launchpad.svg" alt="LAUNCHPAD Admissions Intelligence" '
    r'class="mx-auto h-14 md:h-16 w-auto" width="320" height="64" decoding="async">\2'
)


def inject_favicons(content: str) -> tuple[str, bool]:
    if 'rel="icon"' in content or "rel='icon'" in content:
        return content, False
    # Insert after viewport meta (or charset if no viewport)
    m = re.search(
        r'(<meta\s+name="viewport"[^>]*>\s*)',
        content,
        re.IGNORECASE,
    )
    if m:
        return content[: m.end()] + FAVICON_SNIPPET + content[m.end() :], True
    m = re.search(r'(<meta\s+charset="[^"]*"\s*/?>\s*)', content, re.IGNORECASE)
    if m:
        return content[: m.end()] + FAVICON_SNIPPET + content[m.end() :], True
    return content, False


def update_base_canonical(content: str, filename: str) -> tuple[str, bool]:
    changed = False
    if filename in ("index.htm", "index.html"):
        new_content, n = re.subn(
            r'<base\s+href="https://app\.launchpadi\.com/"\s*target="_blank"\s*>',
            f'<base href="{WWW}/">',
            content,
            count=1,
            flags=re.IGNORECASE,
        )
        if n:
            content = new_content
            changed = True
        else:
            new_content, n = re.subn(
                r'<base\s+href="https://app\.launchpadi\.com/"\s*>',
                f'<base href="{WWW}/">',
                content,
                count=1,
                flags=re.IGNORECASE,
            )
            if n:
                content = new_content
                changed = True
            new_content, n = re.subn(
                r'<base\s+href="https://www\.launchpadi\.com/"\s*target="_blank"\s*>',
                f'<base href="{WWW}/">',
                content,
                count=1,
                flags=re.IGNORECASE,
            )
            if n:
                content = new_content
                changed = True

        new_content, n = re.subn(
            r'<link\s+rel="canonical"\s+href="https://(?:app|www)\.launchpadi\.com/?\"\s*/?>',
            f'<link rel="canonical" href="{WWW}/" />',
            content,
            count=1,
            flags=re.IGNORECASE,
        )
        if n:
            content = new_content
            changed = True
    return content, changed


def replace_brand(content: str) -> tuple[str, int]:
    content, n1 = BRAND_RE.subn(BRAND_REPLACEMENT, content)
    content, n2 = BRAND_RE_ALT.subn(BRAND_REPLACEMENT, content)
    # Already-logo pages: ensure href is index.htm
    content2, n3 = re.subn(
        r'(<a class="flex-none focus:outline-hidden focus:opacity-80" href=")[^"]*(" aria-label="LAUNCHPAD Admissions Intelligence">)',
        r"\1index.htm\2",
        content,
    )
    return content2, n1 + n2 + (1 if n3 and content2 != content else 0)


def process_html_file(path: str, hero_logo: bool) -> dict:
    filename = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    stats = {
        "file": filename,
        "brand": 0,
        "favicon": False,
        "domain": False,
        "hero": False,
        "app_replaced": 0,
    }

    content, domain_changed = update_base_canonical(content, filename)
    stats["domain"] = domain_changed

    # Absolute app host → www (safe for marketing site HTML)
    content, n_app = re.subn(
        r"https://app\.launchpadi\.com",
        WWW,
        content,
    )
    stats["app_replaced"] = n_app

    content, n_brand = replace_brand(content)
    stats["brand"] = n_brand

    content, fav = inject_favicons(content)
    stats["favicon"] = fav

    if hero_logo:
        content2, n_hero = HERO_H1_RE.subn(HERO_REPLACEMENT, content, count=1)
        if n_hero:
            content = content2
            stats["hero"] = True

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        stats["written"] = True
    else:
        stats["written"] = False
    return stats


def rebuild_sitemap() -> int:
    """List public .htm pages; prefer index.htm as homepage; skip index.html."""
    pages = sorted(
        f
        for f in os.listdir(ROOT)
        if f.endswith(".htm") and os.path.isfile(os.path.join(ROOT, f))
    )
    # Prefer single homepage entry as /
    locs: list[tuple[str, str]] = []
    for page in pages:
        if page == "index.htm":
            locs.insert(0, (f"{WWW}/", "1.0"))
        else:
            locs.append((f"{WWW}/{page}", "0.7"))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, priority in locs:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")

    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return len(locs)


def write_robots() -> None:
    """Allow all; point Sitemap at www; drop obsolete .html Disallows."""
    text = f"""User-agent: *
Allow: /

Sitemap: {WWW}/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def write_redirects() -> None:
    """Cloudflare Pages path redirects only (no host-level support)."""
    text = """# Cloudflare Pages path redirects (host-level redirects are NOT supported here).
# See: https://developers.cloudflare.com/pages/configuration/redirects/
# Domain-level app → www must use Bulk Redirects or Dynamic Redirect Rules.
#
# Optional: normalize index.html → site root (Pages has served empty /index.html before)
/index.html / 301
"""
    with open(os.path.join(ROOT, "_redirects"), "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    os.chdir(ROOT)
    hero_files = {
        "index.htm",
        "index.html",
        "contact-us.htm",
        "LAUNCHPADi-Q-MCQ-quiz-web-application.htm",
    }

    files = sorted(glob.glob(os.path.join(ROOT, "*.htm"))) + sorted(
        glob.glob(os.path.join(ROOT, "*.html"))
    )
    # mcq pages if they have brand headers
    files += sorted(glob.glob(os.path.join(ROOT, "mcq", "*.htm*")))

    written = 0
    brand_pages = 0
    domain_pages = 0
    favicon_pages = 0
    hero_pages = 0

    for path in files:
        stats = process_html_file(path, os.path.basename(path) in hero_files)
        if stats.get("written"):
            written += 1
        if stats["brand"]:
            brand_pages += 1
        if stats["domain"] or stats["app_replaced"]:
            domain_pages += 1
        if stats["favicon"]:
            favicon_pages += 1
        if stats["hero"]:
            hero_pages += 1
        print(
            f"{stats['file']}: brand={stats['brand']} fav={stats['favicon']} "
            f"domain={stats['domain']} app_n={stats['app_replaced']} "
            f"hero={stats['hero']} written={stats['written']}"
        )

    n_sitemap = rebuild_sitemap()
    write_robots()
    write_redirects()

    print("\n--- summary ---")
    print(f"html_files_scanned: {len(files)}")
    print(f"html_files_written: {written}")
    print(f"pages_with_logo_brand: {brand_pages}")
    print(f"pages_domain_touched: {domain_pages}")
    print(f"pages_favicon_added: {favicon_pages}")
    print(f"pages_hero_logo: {hero_pages}")
    print(f"sitemap_urls: {n_sitemap}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
