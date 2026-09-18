# LAUNCHPAD (launchpadi.com) — SEO Growth Plan Log

**Property:** `sc-domain:launchpadi.com`  
**Canonical host:** `https://www.launchpadi.com`  
**Cloudflare Pages project:** `lpweb`  
**Site root:** `/Users/pkmac/website-designing/launchpadi.com`  
**Log owner:** Webmaster & SEO Growth Lead  
**Baseline date:** 18 September 2026

---

## 1. Current Baseline Metrics (18 Sept 2026)

| Metric | Value | Source / notes |
|--------|------:|----------------|
| Clicks | **2** | GSC Performance (long window / skill baseline) |
| Impressions | **984** | GSC Performance |
| CTR | 0.2% | Derived |
| Avg. position | ~14.7 | Skill baseline |
| Pages Indexed | **1** | GSC Page indexing (homepage `/`) |
| Pages Not Indexed | **149** | GSC Page indexing |
| — Page with redirect | 4 | Validation: Not Started → see actions log |
| — Alternative page with proper canonical tag | 2 | Validation **Started** 18/09/2026 |
| — Discovered – currently not indexed | 142 | Validation **Started** 18/09/2026 |
| — Crawled – currently not indexed | 1 | Still Not Started |
| Sitemap discovered pages (pre-rebuild UI) | 143 | GSC Sitemaps table |
| Live sitemap `<url>` count after deploy | **146** | Includes priority Albania + Georgia fee masters (was 144) |

**North-star KPI:** ≥100 organic Google sessions/day by Day 90.

---

## 2. Completed Actions Log (Today — 18 Sept 2026)

| # | Action | Status | Evidence / detail | Timestamp (IST) |
|---|--------|--------|-------------------|-----------------|
| 1 | Integrate `origin/main` apex→www redirects | Done | Pulled `a1b92ea`; `_headers` robots freshness + `_redirects` path-preserving apex→www rules preserved in `sitegen/build.py` | ~20:17 |
| 2 | Rebuild all pages + sitemap | Done | `python3 sitegen/build.py` → **318** page files (174 legacy aliases); sitemap masters + daily guide | ~20:18 |
| 3 | Schema / enrichment ship | Done | Organization, BreadcrumbList, FAQPage, Course JSON-LD via `sitegen/seo_schema.py`; thin “legacy boilerplate” landers replaced with enriched aliases | Deployed |
| 4 | Daily publisher + first guide | Done | `mbbs-fees-in-georgia-2026-guide.htm` live; queue next = `nmc-guidelines-mbbs-abroad-2026` (11 remaining) | Live 200 |
| 5 | Git commit | Done | `68a3ca5` — `feat(seo): deploy rich schema, clean legacy pages, daily publisher and 90-day growth engine` | ~20:19 |
| 6 | Push → Cloudflare Pages (`lpweb`) | Done | `a1b92ea..68a3ca5` on `origin/main`; live URLs return HTTP 200 | ~20:19 |
| 7 | GSC Sitemap submit | Done | Submitted `https://www.launchpadi.com/sitemap.xml` → dialog **“Sitemap submitted successfully”**; table **Submitted: 18 Sept 2026**, Status **Success**, Discovered pages **143** (UI lag vs live 144 expected) | **20:20 IST** |
| 8 | GSC Validate Fix — Alternative canonical | Done | Drilldown → **VALIDATE FIX** → **Validation Started 18/09/2026**; Pending 2 (`/home`, `/index.htm`) | ~20:21 |
| 9 | GSC Validate Fix — Discovered not indexed | Done | Drilldown → **VALIDATE FIX** → **Validation Started 18/09/2026**; Affected **142** | ~20:21 |
| 10 | URL Inspection — Georgia 2026 guide | Done | Live test **18 Sept 2026, 20:22**: **URL is available to Google**; Breadcrumbs **1 valid item**; **Indexing requested** (priority crawl queue) | **20:22 IST** |
| 11 | URL Inspection — Study in Georgia hub | Done | Status: URL unknown to Google → **Indexing requested** (priority crawl queue) | **20:24 IST** |
| 12 | Browser cleanup | Done | Closed Neo local tab opened for this task; chipsilicon GSC tab left untouched | ~20:25 |
| 13 | Verify apex→www HTTP/HTTPS 301 | Done | `curl -I http://launchpadi.com/` → **301** `https://www.launchpadi.com/`; `curl -I https://launchpadi.com/` → **301** same; www **200** | ~20:45 |
| 14 | Origin SSL / Full (strict) check | Done | Valid certs: apex `CN=launchpadi.com` (GTS WE1, to Nov 2026); www `CN=www.launchpadi.com` (to Dec 2026) — no 525 | ~20:45 |
| 15 | Enable HSTS after redirects stable | Done | `_headers` → `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload` live on www responses | Deployed `adf3736` |
| 16 | Shorten homepage title + meta | Done | Title **47 chars**: `LAUNCHPAD — India's Admissions Marketplace` (was ~81); meta **142 chars** | Live |
| 17 | Self-canonical Albania/Georgia fee pages + query metas | Done | Titles `(2026) \| LAUNCHPAD` (59 chars); Albania meta targets affordable/low-cost/how-to-apply; Georgia meta targets Batumi Shota Rustaveli + Akaki Tsereteli tuition/year; unique H1s; added to sitemap as masters | Live |
| 18 | Internal links hub cluster | Done | Homepage fee-guide tiles + `mbbs-abroad.htm` table/chips → Georgia hub, Georgia fees, Albania fees, Georgia 2026 guide | Live |
| 19 | Git commit + push SEO pass | Done | `adf3736` — `perf(seo): optimize homepage title length, high-impression fee metas, and internal links` → `origin/main` (`lpweb`) | ~20:46 |
| 20 | GSC URL Inspection — Home (new title) | Done | Live test: **Page can be indexed**; Breadcrumbs **1 valid**; **Indexing requested** | ~20:47 IST |
| 21 | GSC URL Inspection — Albania fees | Partial | Live test: **Page can be indexed**; Breadcrumbs **1 valid**; **Request indexing = Quota exceeded** (retry next day) | ~20:48 IST |
| 22 | GSC URL Inspection — Georgia fees | Partial | Index status was **URL unknown to Google**; Live test: **Page can be indexed**; Breadcrumbs **1 valid**; **Request indexing = Quota exceeded** (retry next day) | ~20:49 IST |
| 23 | Browser cleanup (pass 2) | Done | Closed Neo GSC tab; left chipsilicon + GitHub user tabs untouched | ~20:50 |

### Git commits referenced

| Commit | Message |
|--------|---------|
| `a1b92ea` | `fix(seo): path-preserving apex→www redirects + fee page titles` (already on origin; integrated locally) |
| `68a3ca5` | `feat(seo): deploy rich schema, clean legacy pages, daily publisher and 90-day growth engine` |
| `3e51d2e` | `docs(seo): add PLAN-LOG with baseline, GSC actions and 90-day roadmap` |
| `adf3736` | `perf(seo): optimize homepage title length, high-impression fee metas, and internal links` |

### Live URLs verified (HTTP 200)

- https://www.launchpadi.com/
- https://www.launchpadi.com/sitemap.xml
- https://www.launchpadi.com/mbbs-fees-in-georgia-2026-guide.htm
- https://www.launchpadi.com/study-in-georgia.htm
- https://www.launchpadi.com/mbbs-fees-in-albania-for-indian-students.htm *(self-canonical)*
- https://www.launchpadi.com/mbbs-fees-in-georgia-for-indian-students.htm *(self-canonical)*
- https://www.launchpadi.com/mbbs-abroad.htm

### Follow-ups (next session)

1. Re-request indexing for Albania + Georgia fee pages when GSC quota resets (live tests already green).
2. Do **not** mass-expand thin content until indexed count rises — index-first policy remains.
3. Continue daily publisher from queue (`nmc-guidelines-mbbs-abroad-2026` next).

---

## 3. 90-Day Execution Roadmap

### Month 1 — Foundation & Indexing Unlock (Days 1–30)

| Week | Deliverable | Status |
|------|-------------|--------|
| **W1** | Rebuild with schema-enhanced `sitegen/build.py` | [x] |
| **W1** | Eliminate thin legacy boilerplate; ship enriched aliases | [x] |
| **W1** | Preserve apex→www redirects in `_redirects` + build writer | [x] |
| **W1** | Resubmit sitemap in GSC | [x] |
| **W1** | Start validation on Alternative canonical + Discovered buckets | [x] |
| **W1** | Publish Day-1 high-intent guide + request indexing | [x] |
| **W1** | Spot-check live schema (BreadcrumbList / FAQPage / Course) | [x] |
| **W1** | Shorten homepage title; query-match Albania/Georgia fee metas; self-canonical fee pages | [x] |
| **W1** | Internal links home → MBBS hub → Georgia/Albania fee pages | [x] |
| **W1** | HSTS after apex→www redirects verified | [x] |
| **W1** | Validate 10 sample URLs in Rich Results Test (batch) | [ ] |
| **W2** | Upgrade `mbbs-abroad.htm` to ≥1,200-word flagship | [ ] |
| **W2** | Deepen Georgia / Russia / Philippines / Kazakhstan hubs | [ ] |
| **W2** | Deepen USA / UK / Canada / Germany hubs | [ ] |
| **W2** | Request indexing on each upgraded master after deploy | [ ] |
| **W3** | Document hub → spoke → supporting cluster map | [ ] |
| **W3** | Add contextual internal links (not chips only) | [ ] |
| **W3** | Daily publish Mon–Sat from keyword queue | [ ] *(Day 1 done)* |
| **W4** | Indexing triage: improve quality before mass re-requests | [ ] |
| **W4** | Month-1 exit target: ≥25 indexed pages | [ ] |

### Month 2 — Topical Authority & Content Engine (Days 31–60)

| Week | Deliverable | Status |
|------|-------------|--------|
| **W5** | Ship Medical / Study-abroad blueprints for every new page | [ ] |
| **W5** | University fee breakdown pages (country × year) | [ ] |
| **W5** | NMC / eligibility explainers with dated callouts | [ ] |
| **W5** | Comparison pages (e.g. Georgia vs Philippines vs Russia) | [ ] |
| **W6** | Non-MBBS: MS Germany/USA CS, IELTS/PTE, loans | [ ] |
| **W6** | Enrich city consultant pages with local proof | [ ] |
| **W7** | Continue 1 new page/day | [ ] |
| **W7** | Refresh top 10 impression pages (titles, H1, FAQ, tables) | [ ] |
| **W8** | GSC query review; double-down on winning clusters | [ ] |
| **W8** | Noindex / consolidate remaining doorway duplicates | [ ] |
| **W8** | Month-2 exit: ≥50 indexed; early daily clicks | [ ] |

### Month 3 — Scale, Conversion & Links (Days 61–90)

| Week | Deliverable | Status |
|------|-------------|--------|
| **W9** | Strengthen WhatsApp CTAs under fee tables / FAQs | [ ] |
| **W9** | Eligibility mini-calculator blocks on fee pages | [ ] |
| **W9** | UTM tracking for counselling starts from organic | [ ] |
| **W10** | Partner listings / earned links | [ ] |
| **W10** | 2 data-led assets (fee PDF + NMC checklist) for outreach | [ ] |
| **W10** | YouTube embeds on matching pages | [ ] |
| **W11** | Clone structures of indexed winners → next 20 keywords | [ ] |
| **W11** | Programmatic only where unique fee/intake data exists | [ ] |
| **W12** | Full GSC coverage + sitemap hygiene + CWV spot-check | [ ] |
| **W12** | Update this log + skill playbook | [ ] |
| **W12** | Month-3 exit: **≥100 Google organic visitors/day** (7-day avg) | [ ] |

---

## 4. Expected Impact & Timeline

| Checkpoint | Indexed pages (target) | Impressions / week (target) | Organic visits / day (target) | What should be true |
|------------|----------------------:|----------------------------:|------------------------------:|---------------------|
| **Day 7** | 3–8 | 200–400 | 0–3 | Sitemap re-read; guide + hub crawled; validation in progress |
| **Day 14** | 8–15 | 300–600 | 1–5 | First spoke pages selected for index; impressions on Georgia/MBBS queries |
| **Day 30** | **25–40** | **500+** | **5–15** | Masters deepened; daily cadence established; Discovery bucket shrinking |
| **Day 60** | **50–70** | **2,000+** | **25–60** | Topical authority in MBBS-abroad + 1–2 adjacent clusters |
| **Day 90** | **80–120** | **5,000+** | **100+** | Sustained traffic + conversion paths + external corroboration |

*Targets are planning ranges, not guarantees. Indexing selection depends on uniqueness and usefulness, not submission volume.*

---

## 5. Daily Publishing Protocol & Operational Guide

### Cadence

- **Mon–Sat:** publish **1** high-intent unique guide (≥800–1,500 words, tables + FAQ schema).  
- **Sunday:** enrich **1** existing master (fees / FAQ / last-reviewed), do not spam new thin URLs.

### Exact commands

```bash
cd /Users/pkmac/website-designing/launchpadi.com

# Publish next keyword from the queue (preferred)
python3 scripts/publish_daily_guide.py --next

# Or explicit slug / keyword
python3 scripts/publish_daily_guide.py --slug nmc-guidelines-mbbs-abroad-2026 \
  --title "NMC Guidelines for MBBS Abroad 2026 — What Indian Students Must Verify" \
  --keyword "nmc guidelines for mbbs abroad 2026"

# Full site rebuild (masters + aliases + sitemap + redirects)
python3 sitegen/build.py

# Deploy (Cloudflare Pages via Git)
git add -A && git status
git commit -m "feat(seo): daily guide <slug>"
git push origin main
```

### Keyword queue status (as of 18 Sept 2026)

| Item | Value |
|------|-------|
| Published today | `mbbs-fees-in-georgia-2026-guide` → https://www.launchpadi.com/mbbs-fees-in-georgia-2026-guide.htm |
| Queue remaining | **11** |
| Next up | `nmc-guidelines-mbbs-abroad-2026` |
| Queue file | `sitegen/data/daily_keyword_queue.json` |
| Publish log | `sitegen/data/publish_log.jsonl` |
| Published registry | `sitegen/data/published_guides.json` |

### How to verify each day

1. **Local / build:** script exits 0; new `.htm` exists; `sitemap.xml` includes the URL with today’s `lastmod`.  
2. **Live:** `curl -sI https://www.launchpadi.com/<slug>.htm` → `200`.  
3. **Schema:** view-source shows `BreadcrumbList` + `FAQPage` (and Course on masters where applicable).  
4. **Internal links:** hub page links to the new spoke; spoke links back to hub.  
5. **GSC:** URL Inspection → Test live URL (new heroes) → **Request indexing** (cap: best URL of the day).  
6. **Log:** append date / URL / keyword / GSC status to `sitegen/data/publish_log.jsonl` and update this file’s weekly checkboxes.

### Do / Don’t

| Do | Don’t |
|----|-------|
| One unique useful page/day | Bulk-submit all 142 Discovered URLs |
| Real `lastmod` on changed content | Fake daily `lastmod` bumps |
| Request indexing for the day’s hero URL | Burn the quota on thin aliases |
| Improve quality when validation fails | Assume VALIDATE FIX alone fixes soft demotion |

---

## 6. Session Notes — GSC (Neo Browser local)

| Step | Result |
|------|--------|
| Browser | `user-browseros-neo-local` (this Mac) |
| Property | `sc-domain:launchpadi.com` (account `pk@bioenabletech.com`) |
| Sitemap dialog | “Sitemap submitted successfully” — Google will periodically process |
| Guide live test | “URL is available to Google”; Breadcrumbs valid |
| Guide + hub indexing | Both: “URL was added to a priority crawl queue” |
| Tabs | Task tab closed after work; pre-existing chipsilicon GSC tab left open |

---

*Last updated: 18 September 2026 (IST) — deploy commit `68a3ca5` + GSC submissions completed same day.*
