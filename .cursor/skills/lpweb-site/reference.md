# lpweb — architecture & ops reference

## Stack

| Layer | Detail |
|-------|--------|
| Site type | Static HTML (`.htm` primary), no bundler |
| CSS/JS | Tailwind + Preline CDN |
| Images | `images/` (JPEG stock + logo SVG/PNG) |
| Quiz teaser | `LAUNCHPADi-Q-MCQ-quiz-web-application.htm`, `mcq/` |
| Related product | Sibling `lpquiz` (separate CF Workers app) — not this deploy |

## GitHub

- Org/user push identity: **`bioenable`**
- Repo: `bioenable/lpweb`, default branch `main`, visibility public
- Deploy trigger: Cloudflare Pages GitHub integration (`source.type = github`), not Actions

## Cloudflare Pages

| Field | Value |
|-------|--------|
| Project name | `lpweb` |
| Account | Pk@bioenabletech.com / `9e70b12e26e5162d0ddf160dd8680eeb` |
| Wrong account | Mg@ / `93144d8f3a4ed77d399df6bf4006f5ae` — ignore for lpweb |
| Subdomain | `lpweb.pages.dev` |
| Custom domains | `www.launchpadi.com` (canonical), `app.launchpadi.com` (301 → www via `_redirects`) |
| Production branch | `main` |
| Build command | _(empty)_ |
| Destination dir | _(empty)_ |

Latest production deployment historically matched commit `7b515b7` (“Update sitemap and index files with new domain”). Re-verify after each push.

### Wrangler account bug

`wrangler pages *` may call the **mg@** account even with profile `lpweb` unless:

```bash
export CLOUDFLARE_ACCOUNT_ID=9e70b12e26e5162d0ddf160dd8680eeb
```

OAuth tokens live in (do not print):

- `~/Library/Preferences/.wrangler/config/lpweb.toml` — use for this site
- `~/Library/Preferences/.wrangler/config/lpquiz.toml` — same pk@ account family
- `~/Library/Preferences/.wrangler/config/default.toml` — **mg@, wrong**

### Verify project via API (safe pattern)

Use Python/`curl` with Bearer from `lpweb.toml` `oauth_token`, GET:

`/accounts/9e70b12e26e5162d0ddf160dd8680eeb/pages/projects/lpweb`

Print only `name`, `domains`, `production_branch`, `source.config`, latest deployment commit — never the token.

## DNS

| Item | Status |
|------|--------|
| Registrar NS | GoDaddy `ns21`/`ns22.domaincontrol.com` (authoritative) |
| CF zone `launchpadi.com` | Exists on pk@; NS `dane`/`paloma` — **not** cut over at registrar |
| `www` / `app` | CNAME → `lpweb.pages.dev` via GoDaddy |
| Apex | Still Google (`ghs.googlehosted.com` / related) — not Pages |

## SEO files

| File | Notes |
|------|-------|
| `sitemap.xml` | Host `www`; 179 loc entries (`/` + all root `.htm`) |
| `robots.txt` | `Allow: /` + Sitemap line on www |
| `_redirects` | Path-only (e.g. `/index.html` → `/`); host `app`→`www` = Bulk Redirects |
| Canonical/base | Homepage on www; interior per-page canonicals still P1 |
| Audit / replan | `docs/SEO-AUDIT-AND-CONTENT-REPLAN.md` |

See root `P0-PLAN.md` for cutover status.

## Logo / brand

- Wordmark art: **LAUNCHPAD** + “Admissions Intelligence” + rocket/star
- Header uses SVG lockup; site copy often still says **LAUNCHPADi**
- Master SVG: `logo/logo-horizontal-color.svg` / `images/logo-launchpad.svg` (`#75458E`)
- Approved PNG: `images/logo-launchpad.png`
- Brand kit sibling: `../brand-kit/` (colors, fonts, stationery)
- Bulk script: `scripts/cutover_www_and_logo.py`

## Local preview

```bash
cd /path/to/lpweb
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

## Related paths outside repo

- Brand kit: `/Volumes/sdcard/pkmac_inactive_60d/launchpadi/brand-kit`
- Quiz app: `/Volumes/sdcard/pkmac_inactive_60d/launchpadi/lpquiz`
