---
name: lpweb-site
description: >-
  Manages the LAUNCHPADi static marketing site (lpweb): edit .htm pages,
  SEO/sitemap/robots, Cloudflare Pages deploys via GitHub, logo assets, and
  www.launchpadi.com cutover. Use when working in the lpweb repo, publishing
  launchpadi.com Pages content, or touching app/www domain, favicons, or brand
  logos for this site.
---

# lpweb site management

## What this is

Static HTML site for **LAUNCHPAD / LAUNCHPADi** admissions marketing.

- Repo: `https://github.com/bioenable/lpweb` (public, branch `main`)
- Host: Cloudflare Pages project **`lpweb`**
- Account: **Pk@bioenabletech.com** `9e70b12e26e5162d0ddf160dd8680eeb` (not mg@)
- Live hosts: `lpweb.pages.dev`, `www.launchpadi.com`, `app.launchpadi.com`
- **Canonical host:** `https://www.launchpadi.com` (HTML/sitemap); force `app`→`www` via **Bulk Redirects** (not Pages `_redirects`)

No build step. Tailwind + Preline via CDN. ~179 `.htm` files + `index.html`, `mcq/`, `images/`, favicons.

## Deploy pipeline

```text
git push origin main  →  Cloudflare Pages GitHub App (github:push)  →  production
```

- No GitHub Actions workflows; no GH secrets required for deploy.
- Pages: production branch `main`, empty `build_command` / `destination_dir`.
- Prefer verifying deploys with CF API + **`lpweb` wrangler OAuth profile** and explicit `CLOUDFLARE_ACCOUNT_ID` (see [reference.md](reference.md)).

## Credentials (status)

| Cred | Status |
|------|--------|
| GitHub CLI (`bioenable`) | OK — repo admin/push |
| CF OAuth pk@ (`lpweb` / `lpquiz` wrangler profile) | OK — owns Pages project |
| CF OAuth mg@ (`default` profile) | Wrong account — do **not** use for lpweb |
| GH Actions secrets | N/A |
| `CLOUDFLARE_API_TOKEN` env | Usually unset; OAuth profiles used |
| DNS registrar (GoDaddy) | Still authoritative; CF zone pending NS cutover |
| Pages ↔ GitHub App | Working (deploys on push) |
| Cursor MCP `cloudflare-bindings` | OK — sees pk@ + mg@; pass `account_id` `9e70b12e…` for lpweb/lpquiz |
| Cursor MCP `cloudflare-docs` | OK |
| Cursor MCP `cloudflare-observability` | Auth OK (re-auth if `needsAuth`) |
| Cursor MCP `cloudflare-builds` | Often `needsAuth` — user must approve `mcp_auth` in Cursor |

Never print OAuth tokens from `~/Library/Preferences/.wrangler/config/*.toml`.

## Editing content

1. Edit `.htm` / `index.html` in place; keep Tailwind class patterns consistent.
2. Brand chrome uses **logo image** in the header (`images/logo-launchpad.svg`); footer may keep text `LAUNCHPADi`.
3. Bulk domain/logo/favicon updates: `python3 scripts/cutover_www_and_logo.py` (idempotent-ish; review diff before re-run).
4. After meaningful site changes: commit (Conventional Commits) only when the user asks; push triggers Pages.

## Domain / SEO rules

- Canonical host: **`www.launchpadi.com`**.
- `app.launchpadi.com` should 301 to www via **Bulk Redirects** / Redirect Rules (Pages `_redirects` is path-only).
- Do not reintroduce `app.` in base/canonical/sitemap.
- Prefer `.htm` URLs; `/index.html` on Pages has been unreliable (`_redirects` maps `/index.html` → `/`).
- When changing hosts: update base, canonical, sitemap, and robots Sitemap line together.
- Content/IA replan (doorway country clusters, noindex audit): [`docs/SEO-AUDIT-AND-CONTENT-REPLAN.md`](../../../docs/SEO-AUDIT-AND-CONTENT-REPLAN.md) and root `P0-PLAN.md`.

## Logo assets (canonical)

| File | Use |
|------|-----|
| `logo/logo-horizontal-color.svg` / `images/logo-launchpad.svg` | Full lockup (header + heroes) |
| `logo/logo-horizontal-color.png` / `images/logo-launchpad.png` | Raster from approved artwork |
| `logo/logo-horizontal-white.svg` | On dark backgrounds |
| `logo/logo-mark-rocket.svg` | Icon / favicon source |
| `favicon.svg` | Rocket mark (vector) |
| `favicon.ico`, `favicon-32x32.png`, `apple-touch-icon.png` | Raster favicons |

Sibling brand kit: `../brand-kit/02-logo/` (png/svg/source). Purple from artwork: `#75458E`.

## Quick commands

```bash
# Repo status
gh repo view bioenable/lpweb

# Pages project (pk@ account — required)
export CLOUDFLARE_ACCOUNT_ID=9e70b12e26e5162d0ddf160dd8680eeb
# Prefer API via lpweb OAuth profile; see reference.md if wrangler hits mg@ account

# Local preview (any static server)
python3 -m http.server 8080

# Re-run domain + logo bulk pass (review git diff)
python3 scripts/cutover_www_and_logo.py
```

## Do / don't

- **Do** read `P0-PLAN.md` and `docs/SEO-AUDIT-AND-CONTENT-REPLAN.md` before large SEO/content changes.
- **Do** set `CLOUDFLARE_ACCOUNT_ID` to the pk@ id when using wrangler Pages.
- **Don't** use wrangler profile `default` (mg@) for this project.
- **Don't** invent GH Actions deploy unless explicitly requested.
- **Don't** commit secrets or dump wrangler OAuth tokens into chat/docs.
- **Don't** mass-regenerate all country articles in one AI pass (doorway risk).

## Progressive disclosure

- Architecture, CF API verify, DNS notes → [reference.md](reference.md)
- Cutover checklist status → repo root `P0-PLAN.md`
- Full SEO audit + IA replan → `docs/SEO-AUDIT-AND-CONTENT-REPLAN.md`
