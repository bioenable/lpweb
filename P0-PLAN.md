# P0 Plan — www cutover + logo rollout

**Status:** Preferred host is `https://www.launchpadi.com` via HTML `base`/`canonical` + sitemap/robots (Bulk Redirect not required). Deploy via push to `main`.  
**Canonical public host:** `https://www.launchpadi.com`  
**Deep SEO/content replan:** [`docs/SEO-AUDIT-AND-CONTENT-REPLAN.md`](docs/SEO-AUDIT-AND-CONTENT-REPLAN.md)

---

## 1. Domain cutover: `app.launchpadi.com` → `www.launchpadi.com`

> **Note (confirmed):** `www.launchpadi.com` and `app.launchpadi.com` already serve the same Pages site. Bulk Redirects are **optional / not required**. Declaring www in `<base href>`, `rel="canonical"`, `sitemap.xml`, and `robots.txt` is the primary preferred-host fix.

### 1.1 Inventory (updated 2026-07-21)

| Asset | Status |
|-------|--------|
| `index.htm` / `index.html` | `base` + `canonical` → `https://www.launchpadi.com/`; `target="_blank"` removed from `<base>` |
| `sitemap.xml` | Host `www`; **179** URLs (all root `.htm` + `/` homepage); `index.html` not listed |
| `robots.txt` | `Allow: /` + `Sitemap: https://www.launchpadi.com/sitemap.xml`; obsolete `.html` Disallows removed |
| `_redirects` | Path rules only (`/index.html` → `/`). Host `app`→`www` is **optional SEO** (Bulk Redirect / Redirect Rules); both hosts already serve the same Pages site — primary fix is HTML base/canonical/sitemap → www |
| Interior pages | Brand nav → `index.htm`; no mass absolute `app.` left in HTML |
| Cloudflare Pages | Domains: `lpweb.pages.dev`, `app.launchpadi.com`, `www.launchpadi.com` — project `lpweb`, pk@ `9e70b12e26e5162d0ddf160dd8680eeb` |

### 1.2 HTML / SEO changes — **done in repo**

1. Homepage base + canonical → www  
2. Sitemap rebuild on www  
3. robots.txt Sitemap + cleanup  
4. `_redirects` for app→www  
5. Script: `scripts/cutover_www_and_logo.py`

### 1.3 Cloudflare / DNS steps (infra — still open)

| Step | Action | Status |
|------|--------|--------|
| A | Keep both custom domains on Pages during transition | Open (ops) |
| B | Optional **Bulk Redirect** `app`→`www` 301 | **Not required / not configured** — both hosts serve the same site; primary fix is `base` / `canonical` / sitemap / robots declaring www |
| C | GoDaddy CNAMEs `www`/`app` → `lpweb.pages.dev` until NS cutover | Unchanged |
| D | Optional: point registrar NS to Cloudflare | Later |
| E | Push `main` → verify Pages deployment | **Pending user** |
| F | GSC: www property + sitemap submit | Pending |

### 1.4 Cutover order (remaining)

1. Commit HTML + sitemap + robots + path `_redirects`/`_headers` + logos  
2. Push `main` → wait for Pages deploy  
3. Spot-check live `base`/`canonical`/sitemap declare **www** (also when fetched via `app` host)  
4. Update GSC / ads / email footers still pointing at `app.`  
5. Optional later: Bulk Redirect `app`→`www` for a single browser URL — **not** required for Google when HTML already canonicalizes to www

---

## 2. Logo SVG — implemented

- Vector lockup + rocket mark (`#75458E`)
- Approved PNG copied to `images/logo-launchpad.png` and `logo/logo-horizontal-color.png`
- Favicons refreshed from brand-kit mark (ICO / 32 / 96 / apple-touch) + `favicon.svg`

---

## 3. Logo rollout (HTML) — **done in repo**

| Location | Treatment |
|----------|-----------|
| Header brand (~180 `.htm` + `index.html`) | `<img src="images/logo-launchpad.svg" alt="LAUNCHPAD Admissions Intelligence">` |
| Hero (index, contact) | Logo as H1 visual + short supporting line |
| LAUNCHPADi-Q page | Lockup above product title; CTA to `https://q.launchpadi.com` |
| Favicon links | Injected on root + `mcq/` HTML |
| Footer text `LAUNCHPADi` | Kept as text (not logo spam) |
| Nav label `LAUNCHPADi-Q` | Kept as text product name |

---

## 4. P0 checklist

- [x] Correct SVG logo assets (vector lockup + rocket mark + favicon.svg)
- [x] Document architecture + credentials in `.cursor/skills/lpweb-site/`
- [x] **P0-A** Preferred host via HTML `base`/`canonical`/sitemap/robots → www. Bulk Redirect `app`→`www` is **optional / not configured / not required** while both hosts serve the same site.
- [x] **P0-B** Update `index.htm` / `index.html` base + canonical → `www`
- [x] **P0-C** Rewrite `sitemap.xml` host + completeness; drop `index.html` URL
- [x] **P0-D** Fix `robots.txt` (Sitemap line; remove bad `.html` Disallows)
- [ ] **P0-E** Push `main` → verify Pages deploy on pk@ account
- [ ] **P0-F** GSC / analytics property + sitemap submit for `www`
- [x] **P0-G** Header logo `<img>` + favicon `<link>` rollout
- [x] **P0-H** Regenerate favicon ICO / apple-touch from rocket mark
- [x] SEO audit + content replan doc written

### Remaining (content — not P0 HTML chrome)

See [`docs/SEO-AUDIT-AND-CONTENT-REPLAN.md`](docs/SEO-AUDIT-AND-CONTENT-REPLAN.md) P1/P2: merge country doorway clusters, per-page canonicals, fix `.html` nav, E-E-A-T About page, JSON-LD, CTA alignment with `q.launchpadi.com`.

---

## 5. Out of scope / blockers

- Apex `launchpadi.com` still not on Pages; Google hosting remains until DNS redesign.
- GoDaddy remains DNS authority; CF zone unused until NS change.
- Wrangler `pages` CLI easily hits **wrong account** (`93144…` / mg@) unless `CLOUDFLARE_ACCOUNT_ID=9e70b12e26e5162d0ddf160dd8680eeb` — see skill `reference.md`.
- No GitHub Actions; deploy is Pages GitHub integration only.
- **Do not commit/push until explicitly requested** (changes currently on disk).
