# SEO Audit & Content Replan — LAUNCHPADi (lpweb)

**Date:** 2026-07-21  
**Scope:** Static marketing site at Cloudflare Pages project `lpweb`  
**Canonical host (implemented this pass):** `https://www.launchpadi.com`  
**Related plan:** [`P0-PLAN.md`](../P0-PLAN.md)

This document is a Google Search Console–style + crawler audit, plus a content architecture replan. Domain cutover and logo rollout were implemented in-repo; deep article rewrites are planned here, not mass-applied.

---

## 1. Inventory (public surface)

| Asset | Count / status |
|-------|----------------|
| Root `*.htm` | **179** |
| Root `index.html` | 1 (duplicate of `index.htm`; avoid advertising in sitemap) |
| `mcq/*.html` | **17** thin/generated quiz landing pages |
| `sitemap.xml` | **179** URLs on `www` (rebuilt this pass; was 84 on `app`) |
| `robots.txt` | Allow-all + Sitemap line (fixed this pass; was obsolete `.html` Disallows) |
| `_redirects` / `_headers` | Path normalize `/index.html`→`/`; cache hints. Host `app`→`www` = **Bulk Redirects** (Pages cannot do domain-level `_redirects`) |
| Images / logos | `images/`, `logo/`, favicons at root |
| CDN CSS | Tailwind (`cdn.tailwindcss.com`) + Preline CDN on every page |

**Hosts historically serving the same Pages project:** `lpweb.pages.dev`, `app.launchpadi.com`, `www.launchpadi.com`. Apex `launchpadi.com` is still outside Pages (registrar DNS).

---

## 2. URL map (path → SEO signals)

### 2.1 Theme clusters (root `.htm`)

| Theme | Approx. pages | Pattern |
|-------|---------------|---------|
| Country fees | 34 | `mbbs-fees-in-{country}[-for-indian-students].htm` |
| Medical colleges by country | 30 | `medical-colleges-in-{country}-for-indian-students.htm` |
| Study without NEET | 31 | `study-mbbs-in-{country}-without-neet.htm` |
| MBBS in country | 31 | `mbbs-in-{country}.htm` |
| NEET hub pages | 6 | `neet-*.htm` |
| Product / contact | 2 | `LAUNCHPADi-Q-…`, `contact-us.htm` |
| Home | 2 files | `index.htm` + `index.html` |
| Other guides | ~43 | loans, FMGE, scholarships, “best country”, etc. |

**~30 countries** appear in **3–5 near-parallel templates** (e.g. Georgia: fees short, fees “for Indian students”, colleges, mbbs-in, without-neet).

### 2.2 Technical SEO signals (pre- vs post- this pass)

| Signal | Before | After (this pass) |
|--------|--------|-------------------|
| Homepage `base` / `canonical` | `app.launchpadi.com` (+ `target="_blank"` on base) | `https://www.launchpadi.com/` ; blank target removed |
| Interior canonicals | Almost none (2 pages) | Still mostly absent — **P1** |
| Brand header | Text `LAUNCHPADi` | Logo `<img>` → `images/logo-launchpad.svg` sitewide |
| Favicons in `<head>` | Missing | SVG + ICO + PNG + apple-touch on all scanned HTML |
| Sitemap host / coverage | `app` / 84 of 179 | `www` / 179 `.htm` (+ `/` for home) |
| `robots.txt` | Disallow `*.html` paths that don’t match live `.htm` | Allow `/` + Sitemap URL |
| `noindex` meta | **94** pages | Unchanged (content policy decision) |

### 2.3 Internal linking health

| Issue | Severity | Notes |
|-------|----------|-------|
| Nav uses `.html` on some pages while files are `.htm` | High | Homepage nav still mixed; most interiors use `.htm` for main nav |
| `href="index.html"` on Home | Medium | Prefer `index.htm` or `/` (Pages historically empty for `/index.html`) |
| Broken `mbbs-in-phillipines.htm` | Medium | Typo; file is likely `philippines` |
| Brand href was `#` on ~135 pages | Fixed | Now `index.htm` |
| Orphans | Medium | ~96 pages were missing from old sitemap; many `noindex` so intentional non-discovery mixed with accidental omission |
| Cross-links between fee / colleges / without-neet siblings | Low–Med | Weak hub structure; lists often generic |

### 2.4 Duplicate / near-duplicate themes

1. **Template doorway set:** For each country, 3–5 pages share chrome + similar H2 outlines (“Overview”, “Fees”, “Eligibility”, “Why … for Indian students”).
2. **Explicit short/long pairs:** e.g. `mbbs-fees-in-georgia.htm` ↔ `mbbs-fees-in-georgia-for-indian-students.htm` (also China, Philippines, Russia).
3. **UK / United Kingdom / USA / United States** naming collisions (`mbbs-in-uk` vs `united-kingdom`, etc.).
4. **Hero H1 = “LAUNCHPADi” on most article pages** while true topic H1 sits lower — confuses relevance and looks template-generated.
5. **`mcq/` pages** — prompt-like filenames, thin utility, weak brand context.

### 2.5 Soft-spam / quality risks (how this can look in GSC)

| Risk | Why Google may downrank / ignore |
|------|----------------------------------|
| Doorway / scaled content | Dozens of near-identical country URLs targeting slight keyword variants |
| Host inconsistency | `app` vs `www` vs apex split signals (mitigated by www cutover + 301) |
| Misleading robots | Disallowing `.html` while serving `.htm` looked like broken SEO hygiene |
| Thin / noindex sprawl | 94 `noindex` pages still crawl-budget + trust noise if linked |
| CDN Tailwind on every page | Not a spam signal alone, but hurts CWV vs self-hosted CSS |
| Missing E-E-A-T | Almost no author, org schema, dated “last reviewed”, or primary-source citations |
| Product mismatch | Marketing site talks generic MBBS consulting; product `q.launchpadi.com` / LAUNCHPADi-Q under-linked from country pages |
| Inflated word counts | Shared nav/footer dominate token count; unique body value is lower than raw WC suggests |

---

## 3. Content review — visitor needs vs delivery

### What visitors need

1. **Decision clarity:** Can I study MBBS here? NEET / FMGE / licensing path?
2. **True cost:** Tuition + living + hidden fees in INR, with year/source.
3. **College shortlist:** Named universities, recognition status, language of instruction.
4. **Trust:** Who is LAUNCHPADi / Lpad Intelligence; how counselling works; contact CTA.
5. **Next step:** Talk to counsellor / start quiz / compare 2–3 countries.

### What pages mostly deliver today

- Keyword-shaped long articles with repeated section recipes.
- Generic “affordable / popular for Indian students” claims without unique local proof.
- Weak conversion path (Contact in nav; little mid-article CTA; Q product isolated).
- Hero branding that does not name the page topic.

### Gap summary

| Need | Current | Desired |
|------|---------|---------|
| Country decision | 4 near-dup URLs | 1 hub + optional deep dives |
| Fee truth | Ranges without citation year | Dated table + sources |
| Trust | Footer company name only | About / team / methodology |
| Product | Separate Q page | Q + counselling CTAs on hubs |
| Navigation | Flat keyword dump | Topic hubs → country → CTA |

---

## 4. Recommended information architecture

```text
www.launchpadi.com/
├── /                         Home — brand, problem, solutions, CTA
├── /about.htm                Org, E-E-A-T, methodology (NEW)
├── /contact-us.htm           Conversion
├── /LAUNCHPADi-Q-….htm       Product → q.launchpadi.com
├── /mbbs-abroad.htm          Hub: how to choose a country
├── /mbbs-fees-comparison.htm Hub: fees matrix (keep & strengthen)
├── /neet-counselling.htm     Hub: India NEET path
├── /countries/{slug}.htm     ONE strong page per priority country
│                             (fees + colleges + NEET/FMGE + CTA)
├── /guides/…                 Unique evergreen (FMGE, loans, scholarships)
└── /mcq/                     noindex or fold into Q product docs
```

**Keep (rewrite in place):** Home, Contact, LAUNCHPADi-Q, NEET counselling hub, fees comparison, best-country guide, FMGE, education loan, scholarship pages with distinct intent.

**Merge → single country URL (301 rest):** For each priority country, collapse `mbbs-in-*`, `mbbs-fees-in-*`, `medical-colleges-in-*`, `study-mbbs-in-*-without-neet` into one page with unique sections. Start with top demand: Georgia, Russia, Philippines, China, Bangladesh, Uzbekistan, Kazakhstan, Kyrgyzstan (if present), Nepal, Egypt.

**Kill / noindex / redirect:** Duplicate short fee pages; UK/USA naming doubles; thin `mcq/` HTML; any page still `noindex` that is also linked from nav (either index properly or unlink).

**Rewrite requirements (per country page):** Unique intro (≥150 words not shared), local university table, licensing note for India return, living-cost band, last-reviewed date, counsellor CTA, related internal links to hubs + Q.

---

## 5. Prioritized recommendations

### P0 — Shipping / trust hygiene (domain + crawl)

| ID | Action | Status |
|----|--------|--------|
| P0-A | 301 `app` → `www` via **Bulk Redirects** / Redirect Rules | **Ops pending** (Pages `_redirects` cannot match host; see setup below) |
| P0-B | Homepage base + canonical → www | **Done** |
| P0-C | Rebuild sitemap on www; drop `index.html` loc | **Done** |
| P0-D | Fix robots (Sitemap; remove bad Disallows) | **Done** |
| P0-E | Commit + push `main` → Pages deploy | **Pending user** |
| P0-F | GSC: verify www property; submit sitemap; monitor Coverage | Pending |
| P0-G | Header logo + favicons sitewide | **Done** |
| P0-H | Favicon set from brand-kit mark | **Done** (SVG/ICO/PNG/apple-touch) |

### P1 — Reduce doorway risk without rewriting everything

1. Pick **8–12 priority countries**; merge templates; 301 losers.
2. Add **per-page canonical** on all indexable pages.
3. Fix nav: all `.htm` / `/`; remove `#` leftovers; fix Philippines typo links.
4. Audit **94 `noindex`**: either make indexable after merge or stop linking them.
5. Replace article-page hero “LAUNCHPADi” H1 with **topic H1 only** (brand stays in header logo).
6. Add **Organization + WebSite JSON-LD** on home; **Article** or **FAQ** on hubs.
7. Mid-article CTA: Contact + LAUNCHPADi-Q on country hubs.
8. Self-host or purge unused Tailwind for CWV (optional but helpful).

### P2 — Depth, E-E-A-T, conversion

1. New About / methodology / counsellor profiles.
2. Cite NMC / FMGE / embassy sources with dates.
3. Comparison tools or tables that aren’t copy-paste across countries.
4. OG/Twitter default image from lockup (`images/og-default.png`).
5. Align ads/email footers to www; retire `app` in GSC after redirect settles.
6. Decide fate of `mcq/` (noindex + robots, or migrate into Q app).

---

## 6. Next content implementation batch (recommended)

**Batch 1 (1–2 days):**  
Georgia, Russia, Philippines, China — merge each into one indexable URL; 301 siblings; unique intros + fee table + CTA; fix nav `.htm`.

**Batch 2:**  
Bangladesh, Uzbekistan, Kazakhstan, Nepal — same pattern; strengthen `mbbs-fees-comparison.htm` as hub.

**Batch 3:**  
NEET hub cleanup; About page; JSON-LD; remove or noindex leftover thin MCQ HTML.

Do **not** mass-regenerate all 179 bodies with AI in one pass — that recreates the doorway problem.

---

## 7. Implementation notes (this pass)

| Change | Detail |
|--------|--------|
| Script | `scripts/cutover_www_and_logo.py` |
| Logo PNG | `images/logo-launchpad.png`, `logo/logo-horizontal-color.png` (from approved attachment) |
| Logo SVG | `images/logo-launchpad.svg` / `logo/logo-horizontal-color.svg` (`#75458E`) |
| Hero logo | `index.htm` / `index.html`, `contact-us.htm`, plus lockup on `LAUNCHPADi-Q-…` |
| Remaining `app.launchpadi.com` | Intentional only in docs / ops notes (not in HTML/sitemap) |

### 7.1 Bulk Redirect setup (app → www)

Cloudflare Pages `_redirects` **does not support domain-level** sources. After HTML deploy, in pk@ account (`9e70b12e…`):

1. Create a Bulk Redirect List with items:
   - Source: `https://app.launchpadi.com/` → Target: `https://www.launchpadi.com/` (include subpath / preserve path if using wildcard list items)
   - Or use a Dynamic Redirect Rule on the zone once NS is on Cloudflare:  
     `(http.host eq "app.launchpadi.com")` → `concat("https://www.launchpadi.com", http.request.uri.path)` status 301
2. Until Bulk Redirect exists, both hosts still serve the same Pages content; HTML canonicals already point to www (soft consolidation).

---

## 8. Verification checklist (after push)

- [ ] `curl -I https://app.launchpadi.com/` → 301 to www  
- [ ] `curl -sI https://www.launchpadi.com/` → 200; HTML has www canonical  
- [ ] Sitemap loads; sample URLs 200  
- [ ] Header logo visible desktop/mobile  
- [ ] GSC sitemap submit for www property  
