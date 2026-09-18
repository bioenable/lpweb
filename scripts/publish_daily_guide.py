#!/usr/bin/env python3
"""Publish one high-intent SEO guide per day for launchpadi.com.

Usage:
  python3 scripts/publish_daily_guide.py --next
  python3 scripts/publish_daily_guide.py --slug my-slug --title "..." --keyword "..."
  python3 scripts/publish_daily_guide.py --list

After publish:
  1. Deploy the site so the URL is live
  2. GSC URL Inspection → Request indexing (one hero URL/day)
  3. Add a contextual link from the cluster hub if not auto-injected
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sitegen"))

from seo_schema import (  # noqa: E402
    breadcrumb_schema,
    course_schema,
    faq_html,
    faq_schema,
    json_ld_scripts,
    organization_schema,
    webpage_schema,
)

CANONICAL = "https://www.launchpadi.com"
PHONE = "+91 8855-833-244"
PHONE_TEL = "+918855833244"
WA = "918855833244"
QUEUE_PATH = ROOT / "sitegen" / "data" / "daily_keyword_queue.json"
PUBLISHED_PATH = ROOT / "sitegen" / "data" / "published_guides.json"
LOG_PATH = ROOT / "sitegen" / "data" / "publish_log.jsonl"
TODAY = date.today().isoformat()


def esc(s: str) -> str:
    import html

    return html.escape(s, quote=True)


def load_queue() -> dict:
    if not QUEUE_PATH.exists():
        return {"queue": [], "completed": []}
    return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))


def save_queue(data: dict) -> None:
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_published() -> list[dict]:
    if not PUBLISHED_PATH.exists():
        return []
    return json.loads(PUBLISHED_PATH.read_text(encoding="utf-8"))


def save_published(items: list[dict]) -> None:
    PUBLISHED_PATH.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_log(entry: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def build_faqs(title: str, keyword: str, country: str | None, intent: str) -> list[tuple[str, str]]:
    faqs = [
        (
            f"Who is this guide for?",
            f"Indian students and parents researching “{keyword}” who need fee honesty, eligibility clarity, and a next step — not brochure copy.",
        ),
        (
            "Are the costs final?",
            "No. Figures are indicative planning bands. Always demand university line-item fee sheets before paying booking amounts.",
        ),
        (
            "How do I get personalised counselling?",
            f"WhatsApp LAUNCHPAD or book a free profile evaluation ({PHONE}). Share scores, budget, and target intake year.",
        ),
        (
            "What should I read next on LAUNCHPAD?",
            "Open the linked hub page, compare one peer destination, then education-loan and visa guides if you are close to applying.",
        ),
    ]
    if country:
        faqs.append(
            (
                f"Is {country} a good fit?",
                f"It depends on budget, NEET/English docs, language of instruction, and whether you plan to practise in India. Use the checklist on this page, then confirm with a counsellor.",
            )
        )
    if intent == "regulatory":
        faqs.append(
            (
                "Where do I verify NMC rules?",
                "Use official NMC publications and notices. Treat agent PDFs as secondary; rules change and screenshots go stale.",
            )
        )
    return faqs


def render_guide(
    slug: str,
    title: str,
    keyword: str,
    hub: str,
    country: str | None,
    intent: str,
    cluster: str,
) -> str:
    faqs = build_faqs(title, keyword, country, intent)
    country_bit = f" focused on {country}" if country else ""
    fee_table = f"""
    <h2>Indicative cost worksheet{esc(country_bit)}</h2>
    <div class="table-wrap"><table class="data">
      <thead><tr><th>Cost head</th><th>What to collect</th><th>Parent note</th></tr></thead>
      <tbody>
        <tr><td>Tuition</td><td>Official year-wise circular</td><td>Watch year-2+ increases</td></tr>
        <tr><td>Hostel / mess</td><td>Contract + Indian food options</td><td>Often under-quoted</td></tr>
        <tr><td>Insurance / admin</td><td>Mandatory first-year charges</td><td>Ask for invoice list</td></tr>
        <tr><td>Visa / travel / forex</td><td>Embassy checklist + buffer</td><td>Separate from tuition</td></tr>
        <tr><td>Consultancy</td><td>Written scope &amp; refunds</td><td>Never blend into “package”</td></tr>
      </tbody>
    </table></div>
    """
    nmc_block = ""
    if cluster == "mbbs" or intent in ("regulatory", "eligibility", "licensing"):
        nmc_block = f"""
        <h2>NMC / licensing callout ({TODAY})</h2>
        <p>Before paying any seat booking for an overseas medical pathway, verify the latest National Medical Commission
        notices relevant to foreign medical graduates, internship expectations, and licensing exams (FMGE/NExT as applicable).
        LAUNCHPAD counsellors help you ask the right questions — we do not replace official circulars.</p>
        <ul>
          <li>Confirm medium of instruction and clinical language reality</li>
          <li>Map internship location against your India return plan</li>
          <li>Start FMGE/NExT prep planning during clinical years</li>
          <li>Keep NEET documentation organised even when marketing says otherwise</li>
        </ul>
        """
    comparison = ""
    if intent == "comparison":
        comparison = """
        <h2>How to choose between options</h2>
        <p>Score each option on total 5–6 year cost, English-medium reliability, clinical exposure, and licensing difficulty —
        not on Instagram reels. Prefer the destination where your family can fund without panic deposits.</p>
        """

    crumbs = [("Home", "/"), ("Guides", "resources.htm"), (title[:48], f"{slug}.htm")]
    schemas = json_ld_scripts(
        organization_schema(),
        webpage_schema(title, f"Guide for Indian students: {keyword}", f"{slug}.htm", TODAY),
        breadcrumb_schema(crumbs),
        faq_schema(faqs),
        course_schema(title, f"Admissions guide: {keyword}", f"{slug}.htm") if cluster == "mbbs" else None,
    )

    # Reuse site chrome by reading a generated master and swapping body is fragile;
    # emit a self-contained page that links site CSS/JS like build.py pages.
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.htm">Home</a> / <a href="resources.htm">Guides</a> / {esc(title)}</div>
    <h1>{esc(title)}</h1>
    <p class="lead">High-intent guide for <strong>{esc(keyword)}</strong> — built for Indian students and parents who need actionable fee, eligibility, and counselling next steps.</p>
    <p class="form-note">Published {TODAY} · Part of the LAUNCHPAD daily publishing protocol</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="book-counselling.htm">Free counselling</a>
      <a class="btn btn-secondary" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp now</a>
      <a class="btn btn-ghost" href="{esc(hub)}">Open cluster hub</a>
    </div>
  </div>
</section>
<div class="container layout-split">
  <article class="prose reveal">
    <p>This page exists because Google rewards <em>useful, fresh, unique</em> answers — not thin doorway clones.
    Use it as a worksheet: gather documents, separate real costs from marketing packages, and only then shortlist universities or consultants.</p>
    {fee_table}
    {nmc_block}
    {comparison}
    <h2>Eligibility &amp; documents checklist</h2>
    <ol>
      <li>Academic transcripts and ID proofs ready as PDFs</li>
      <li>NEET / English test status documented (even if exploring waivers)</li>
      <li>Budget ceiling agreed with parents in writing</li>
      <li>Target intake month and Plan-B destination chosen</li>
      <li>Loan pre-conversation started if borrowing</li>
    </ol>
    <h2>Internal topic cluster</h2>
    <div class="chips">
      <a class="chip" href="{esc(hub)}">Cluster hub</a>
      <a class="chip" href="mbbs-abroad.htm">MBBS Abroad</a>
      <a class="chip" href="study-abroad.htm">Study Abroad</a>
      <a class="chip" href="education-loan-abroad.htm">Loans</a>
      <a class="chip" href="fmge.htm">FMGE / NExT</a>
      <a class="chip" href="find-consultants.htm">Consultants</a>
    </div>
    {faq_html(faqs)}
    <h2>Ask LAUNCHPAD</h2>
    <p>Share your scores, budget, and target year on WhatsApp. We will map destinations and services — including AI agents for speed and humans for judgement calls.</p>
  </article>
  <aside>
    <div class="side-cta reveal">
      <h3 style="margin-top:0;color:#fff">Publish-day CTA</h3>
      <p>Free profile evaluation for families actively comparing {esc(country or "abroad")} options.</p>
      <a class="btn btn-primary" href="book-counselling.htm" style="width:100%;margin:0.5rem 0">Book now</a>
      <a class="btn btn-ghost btn-sm" href="tel:{PHONE_TEL}" style="width:100%">{PHONE}</a>
    </div>
  </aside>
</div>
"""

    # Pull header/footer snippets from an existing generated page for brand consistency
    donor = ROOT / "about.htm"
    header = footer = ""
    if donor.exists():
        html = donor.read_text(encoding="utf-8")
        m = re.search(r"(<div class=\"promo-strip\">.*?</header>)", html, re.S)
        if m:
            header = m.group(1)
        m2 = re.search(r"(<footer class=\"site-footer\">.*)</html>", html, re.S)
        if m2:
            footer = m2.group(1)

    page = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | LAUNCHPAD</title>
<meta name="description" content="{esc('Guide for Indian students: ' + keyword + '. Fees, eligibility, NMC-aware notes, and counselling next steps.')}">
<meta name="keywords" content="{esc(keyword)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="last-reviewed" content="{TODAY}">
<link rel="canonical" href="{CANONICAL}/{slug}.htm">
<base href="{CANONICAL}/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="LAUNCHPAD">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc('High-intent guide: ' + keyword)}">
<meta property="og:url" content="{CANONICAL}/{slug}.htm">
<meta property="og:image" content="{CANONICAL}/images/logo-launchpad.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/site.css">
{schemas}
</head>
<body>
{header}
{body}
{footer}
"""
    return page


def upsert_sitemap(slug: str) -> None:
    sm_path = ROOT / "sitemap.xml"
    if not sm_path.exists():
        return
    text = sm_path.read_text(encoding="utf-8")
    loc = f"{CANONICAL}/{slug}.htm"
    entry = (
        f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>0.8</priority></url>"
    )
    if loc in text:
        text = re.sub(
            rf"  <url><loc>{re.escape(loc)}</loc>.*?</url>",
            entry,
            text,
            count=1,
            flags=re.S,
        )
    else:
        text = text.replace("</urlset>", entry + "\n</urlset>")
    sm_path.write_text(text, encoding="utf-8")


def inject_hub_link(hub: str, slug: str, title: str) -> None:
    hub_path = ROOT / hub
    if not hub_path.exists():
        return
    html = hub_path.read_text(encoding="utf-8")
    marker = '<!-- daily-publish-links -->'
    chip = f'<a class="chip" href="{slug}.htm">{esc(title[:42])}</a>'
    if f'href="{slug}.htm"' in html:
        return
    if marker in html:
        html = html.replace(marker, marker + "\n" + chip)
    elif 'class="chips"' in html:
        html = html.replace('<div class="chips">', f'<div class="chips">\n{marker}\n{chip}', 1)
    else:
        html += f'\n<!-- auto hub link --><p><a href="{slug}.htm">{esc(title)}</a></p>\n'
    hub_path.write_text(html, encoding="utf-8")


def publish_item(item: dict) -> Path:
    slug = item["slug"]
    title = item["title"]
    keyword = item["keyword"]
    hub = item.get("hub") or "resources.htm"
    country = item.get("country")
    intent = item.get("intent") or "guide"
    cluster = item.get("cluster") or "general"

    out = ROOT / f"{slug}.htm"
    out.write_text(
        render_guide(slug, title, keyword, hub, country, intent, cluster),
        encoding="utf-8",
    )
    upsert_sitemap(slug)
    inject_hub_link(hub, slug, title)

    published = load_published()
    published = [p for p in published if p.get("slug") != slug]
    published.append(
        {
            "slug": slug,
            "date": TODAY,
            "keyword": keyword,
            "title": title,
            "hub": hub,
            "url": f"{CANONICAL}/{slug}.htm",
        }
    )
    save_published(published)
    append_log(
        {
            "date": TODAY,
            "slug": slug,
            "keyword": keyword,
            "url": f"{CANONICAL}/{slug}.htm",
            "action": "published",
            "gsc_next": "URL Inspection → Request indexing after deploy",
        }
    )
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="LAUNCHPAD daily SEO publisher")
    ap.add_argument("--next", action="store_true", help="Publish next queued keyword")
    ap.add_argument("--list", action="store_true", help="Show queue")
    ap.add_argument("--slug")
    ap.add_argument("--title")
    ap.add_argument("--keyword")
    ap.add_argument("--hub", default="resources.htm")
    ap.add_argument("--country")
    ap.add_argument("--intent", default="guide")
    ap.add_argument("--cluster", default="general")
    args = ap.parse_args()

    data = load_queue()

    if args.list:
        print(f"Queued: {len(data.get('queue', []))} | Completed: {len(data.get('completed', []))}")
        for i, q in enumerate(data.get("queue", []), 1):
            print(f"  {i}. {q['slug']} — {q['keyword']}")
        return

    if args.next:
        if not data.get("queue"):
            print("Queue empty. Add keywords to sitegen/data/daily_keyword_queue.json")
            sys.exit(1)
        item = data["queue"].pop(0)
        path = publish_item(item)
        data.setdefault("completed", []).append({**item, "published_on": TODAY})
        save_queue(data)
        print(f"Published {path.name}")
        print(f"Live URL after deploy: {CANONICAL}/{item['slug']}.htm")
        print("Next: deploy → GSC URL Inspection → Request indexing")
        return

    if args.slug and args.title and args.keyword:
        item = {
            "slug": args.slug,
            "title": args.title,
            "keyword": args.keyword,
            "hub": args.hub,
            "country": args.country,
            "intent": args.intent,
            "cluster": args.cluster,
        }
        path = publish_item(item)
        print(f"Published {path.name}")
        return

    ap.print_help()
    sys.exit(2)


if __name__ == "__main__":
    main()
