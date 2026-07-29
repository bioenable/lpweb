# LAUNCHPAD (lpweb) — Admissions Intelligence Marketplace

Static marketing site for **www.launchpadi.com**.

## What it is

India-focused **admissions marketplace**: destinations, courses (MBBS → MS/MBA/engineering and more), consultants, services (loans/visas/SOP), AI agents, and resources — with WhatsApp-first inquiry flows.

## Stack

- Static HTML (`.htm`) + shared `assets/css/site.css` + `assets/js/site.js`
- No build step for Cloudflare Pages (empty build command)
- Pages generated from `sitegen/build.py` (re-run after content model changes)

## Deploy

```text
git push origin main  →  Cloudflare Pages project `lpweb`  →  production
```

- Account: Pk@bioenabletech.com `9e70b12e26e5162d0ddf160dd8680eeb`
- Canonical host: `https://www.launchpadi.com`

## Regenerate site

```bash
python3 sitegen/build.py
```

Legacy MBBS pages live in `_archive_legacy/`; `_redirects` maps old URLs to the new IA.

## Brand

- Logo: `images/logo-launchpad.png` (source: `logo/launchpad-new-logo-transparent.png`)
- Purple `#8058A0` · Ink `#281C37` · Fonts: Montserrat + Source Sans 3

## Local preview

```bash
python3 -m http.server 8080
```
