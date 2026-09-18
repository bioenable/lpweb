---
name: launchpadi-growth
description: >-
  Webmaster and SEO Growth Lead playbook for launchpadi.com. Use when growing
  organic search traffic, fixing "Discovered – currently not indexed", running
  the daily publishing protocol, rebuilding sitegen pages, validating GSC, or
  executing the 90-day plan from 0 to 100+ Google visitors/day.
---

# LAUNCHPAD (launchpadi.com) — SEO Growth Skill

**Property:** `sc-domain:launchpadi.com`  
**Canonical host:** `https://www.launchpadi.com`  
**Site root:** `/Users/pkmac/website-designing/launchpadi.com`  
**Generator:** `python3 sitegen/build.py`  
**Daily publisher:** `python3 scripts/publish_daily_guide.py`

## Baseline (verified GSC, Sep 2026)

| Metric | Value |
|--------|------:|
| Clicks (16 months) | 2 |
| Impressions | 984 |
| CTR | 0.2% |
| Avg position | 14.7 |
| Indexed pages | **1** (`/`) |
| Not indexed | 149 |
| Discovered – currently not indexed | 142 |
| Page with redirect | 4 |
| Alternative page with proper canonical | 2 |
| Crawled – currently not indexed | 1 |

**Root causes (codebase-confirmed):**
1. Thin programmatic boilerplate on ~179 legacy alias pages.
2. Master destination/course pages too shallow (<400 words), identical templates.
3. Near-zero Schema.org (no BreadcrumbList / FAQPage / Course).
4. No publishing cadence since late July 2026.
5. Flat internal linking — no topic clusters.

**Live URL Inspection fact:** Googlebot Smartphone *can* fetch pages (200, robots allow, indexable, canonical detected) — Google *chooses* not to index the 142 "Discovered" URLs. This is a **quality / usefulness / duplication** problem, not a crawl-block problem.

---

## Strategic answer: Do we need to publish every day and submit URLs?

**Short answer:** Yes — a disciplined **daily high-intent publish cadence** is one of the highest-leverage moves for a near-zero-traffic domain *if and only if* each page is uniquely useful. Blind mass URL submission of thin pages will **not** unlock indexing and can reinforce soft-demotion.

### Exact mechanisms (what actually happens)

#### 1) Crawl budget allocation
- Google allocates **crawl demand** (how often it *wants* to visit) based on perceived popularity, freshness history, and site quality signals.
- New unique URLs in sitemap + internal links + occasional Indexing API / GSC inspection **raise discovery probability**.
- For a small site like launchpadi.com, "budget" is rarely the bottleneck — **selection for indexing** after discovery is. Publishing daily helps *demand*; content quality decides *indexing*.

#### 2) Freshness / QDF (Query Deserves Freshness)
- For queries where recency matters (fee updates, NMC 2026 notices, intake deadlines, exam dates), Google prefers recently updated documents.
- Daily (or weekly) updates to fee tables, guideline callouts, and "last reviewed" dates help pages compete on QDF-eligible queries.
- Evergreen queries ("MBBS in Georgia fees") still need **depth and uniqueness** first; freshness is a tie-breaker, not a substitute for substance.

#### 3) Googlebot crawl-frequency stimulation
- Sites that **reliably** add index-worthy URLs train a higher revisit rate on the sitemap and hub pages.
- Changing `lastmod` in `sitemap.xml` for real content changes (not fake bumps) helps prioritisation.
- Submitting one strong URL/day in GSC URL Inspection → "Request indexing" is a **nudge**, not a guarantee. Cap: Google rate-limits indexing requests; use them for your best new/updated masters, not every legacy alias.

### What "works great" vs what fails

| Works | Fails |
|-------|-------|
| 1 unique, ≥800–1,500 word high-intent page/day with tables + FAQ schema | 50 thin template pages/day |
| Sitemap `lastmod` updated when content changes | Fake daily `lastmod` on unchanged URLs |
| Internal links from hubs + 2–3 related masters | Orphan pages only listed in sitemap |
| GSC inspect + request for the day's hero URL | Bulk-submit 140 discovered-not-indexed URLs hoping for magic |
| Topic cluster (hub → spokes → hub) | Flat nav dump of 143 near-duplicates |

### Exact daily publishing protocol

**Cadence:** 1 high-intent page per calendar day (Mon–Sat). Sunday = enrich 1 existing master (fees/FAQ refresh).

**Step A — Select keyword (low competition, high intent)**
1. Prefer Indian student commercial-investigational queries:
   - `[country] mbbs fees for indian students 2026`
   - `nmc approved medical colleges in [country]`
   - `study [course] in [country] cost`
   - `[exam] score for [country] student visa`
2. Filters: search volume secondary; **intent + SERP weakness** primary (forums, outdated blogs, thin aggregators on page 1).
3. Maintain queue in `sitegen/data/daily_keyword_queue.json`.

**Step B — Generate page**
```bash
cd /Users/pkmac/website-designing/launchpadi.com
python3 scripts/publish_daily_guide.py --next
# or explicit:
python3 scripts/publish_daily_guide.py --slug mbbs-fees-in-georgia-2026 --title "..." --keyword "..."
```
Script must: write HTML with BreadcrumbList + FAQPage + Organization schema, append to sitemap with today's `lastmod`, link from relevant hub, append to publish log.

**Step C — Deploy**
- Deploy Cloudflare Pages / host sync so the URL returns 200 publicly before GSC inspect.

**Step D — Submit**
1. GSC → URL Inspection → test live URL → **Request indexing** (1 primary URL/day).
2. Confirm sitemap remains submitted (`https://www.launchpadi.com/sitemap.xml`).
3. Log date, URL, keyword, GSC request status in `sitegen/data/publish_log.jsonl`.

**Step E — Internally link (same day)**
- Add 1 contextual link from the cluster hub (e.g. `mbbs-abroad.htm` or `study-in-georgia.htm`).
- Add 1 reciprocal related-chip on 1 sibling page.
- Never leave the new page orphaned.

**Automation stack**
| Tool | Role |
|------|------|
| `sitegen/build.py` | Rebuild masters + enriched aliases + schema |
| `scripts/publish_daily_guide.py` | Daily spoke page + sitemap touch |
| `sitegen/data/daily_keyword_queue.json` | Keyword backlog |
| GSC URL Inspection | Indexing nudge |
| Cloudflare Pages deploy | Make live |

---

## 90-day master plan (0 → 100+ Google visitors/day)

**North-star KPI:** ≥100 organic sessions/day from Google by end of Day 90.  
**Leading indicators:** indexed pages, impressions, avg position for target cluster, CTR.

### Month 1 — Foundation & Technical Indexing Unlock (Days 1–30)

**Goal:** Move from 1 indexed URL → 25–40 quality indexed URLs; kill thin-boilerplate signals.

#### Week 1 — Technical unlock
- [ ] Rebuild site with schema-enhanced `sitegen/build.py` (Organization, BreadcrumbList, FAQPage, Course where relevant).
- [ ] Eliminate "You opened a legacy…" boilerplate; ship rich alias or soft-canonical landers.
- [ ] Validate 10 sample URLs: view-source schema, Rich Results Test, live fetch.
- [ ] Resubmit sitemap in GSC; fix any redirect/canonical mismatches (www).
- [ ] Audit `_redirects` — keep only necessary 301s; do not 301 valuable unique fee URLs.

#### Week 2 — Master page depth (MBBS + Big 4)
- [ ] Upgrade `mbbs-abroad.htm` to flagship (≥1,200 words): fee comparison table, NMC 2026 callout, eligibility, FMGE/NExT, FAQ (≥6) + FAQPage JSON-LD.
- [ ] Upgrade `study-in-georgia.htm`, `study-in-russia.htm`, `study-in-philippines.htm`, `study-in-kazakhstan.htm` with unique fee bands + FAQs.
- [ ] Upgrade `study-in-usa.htm`, `study-in-uk.htm`, `study-in-canada.htm`, `study-in-germany.htm`.
- [ ] Request indexing on each upgraded master after deploy.

#### Week 3 — Topic clusters & internal links
- [ ] Build cluster map: Hub → Spoke → Supporting.
  - Hub: `mbbs-abroad.htm`
  - Spokes: country study + fee guides
  - Supporting: NEET, FMGE, loans, consultants-by-city
- [ ] Add contextual paragraphs (not just chips) linking hubs ↔ spokes.
- [ ] Start daily publish (6 days/week) from keyword queue — MBBS fees niche first.

#### Week 4 — Indexing triage in GSC
- [ ] For **Discovered – currently not indexed**: do **not** mass-request. Instead improve content quality of the URL or consolidate.
- [ ] For **Crawled – currently not indexed**: strengthen uniqueness, word count, tables, E-E-A-T (author/reviewed date, contact), internal links; then request indexing once.
- [ ] For **Alternative page with proper canonical**: expected if alias → master; ensure master is the strong page.
- [ ] For **Page with redirect**: confirm intentional; else restore unique content.
- [ ] Target Month-1 exit: ≥25 indexed pages, impressions trending up week-over-week.

### Month 2 — Topical Authority & Content Engine (Days 31–60)

**Goal:** Own MBBS-abroad + 2 non-MBBS clusters; 50–70 indexed pages; early clicks.

#### Week 5 — Content templates at scale
- [ ] Ship every new page using **Medical / Study-abroad blueprints** (below).
- [ ] University fee breakdown pages (country × year).
- [ ] NMC / eligibility explainers with dated callouts.
- [ ] Comparison pages (Georgia vs Philippines vs Russia).

#### Week 6 — Non-MBBS expansion
- [ ] MS Germany / USA CS cluster; IELTS/PTE requirement pages; education loan guides.
- [ ] City consultant pages enriched with local proof (not thin location spam).

#### Week 7 — Velocity + refresh
- [ ] Continue 1 new page/day.
- [ ] Refresh top 10 impression pages (even if position 20–40): titles, H1, FAQ, tables.
- [ ] Add `dateModified` visible + in schema.

#### Week 8 — Measurement
- [ ] GSC: queries gaining impressions; double-down on those clusters.
- [ ] Kill or noindex true doorways that still look duplicate after enrichment.
- [ ] Month-2 exit target: ≥50 indexed, measurable CTR on 10+ queries, early clicks daily.

### Month 3 — Scale, Conversion & Backlink Signals (Days 61–90)

**Goal:** 100+ organic visitors/day; conversion paths; external corroboration.

#### Week 9 — Conversion SEO
- [ ] Strengthen CTAs (WhatsApp) below fee tables and FAQs.
- [ ] Add eligibility mini-calculator blocks (static JS) on fee pages.
- [ ] Track counselling starts UTM'd from organic landing pages.

#### Week 10 — Digital PR / backlinks (ethical)
- [ ] Partner listings (universities, consultancies) with do-follow where earned.
- [ ] Publish 2 data-led assets (fee comparison PDF + NMC checklist) for outreach.
- [ ] YouTube `@Launchpadi` video → embed on matching page (watch time + brand).

#### Week 11 — Scale winners
- [ ] Clone structure of pages that got indexed + impressions; expand to next 20 keywords.
- [ ] Programmatic **only** where each row has unique table data (real fees, intakes).

#### Week 12 — Hardening
- [ ] Full GSC coverage review; sitemap hygiene; Core Web Vitals spot-check.
- [ ] Document playbook updates in this skill.
- [ ] Month-3 exit: **≥100 Google organic visitors/day** sustained 7-day average, or clear gap analysis if short.

### Month-by-month KPI table

| Month | Indexed pages | Impressions/week | Organic visits/day | Focus |
|-------|--------------:|-----------------:|-------------------:|-------|
| 1 | 25–40 | 500+ | 5–15 | Index unlock + masters |
| 2 | 50–70 | 2,000+ | 25–60 | Authority + daily engine |
| 3 | 80–120 | 5,000+ | **100+** | Scale + links + CVR |

---

## GSC validation protocols

### After every deploy
1. Open live URL in browser → 200, correct canonical, schema present.
2. Rich Results Test (or Schema Validator) on 1 hub + 1 new spoke.
3. GSC URL Inspection → **View crawled page** / Live test → confirm Google sees updates.
4. Sitemap status: Fetched recently; no spike in "Couldn't fetch".

### Handling indexing states

| State | Meaning | Action |
|-------|---------|--------|
| Discovered – not indexed | Known URL, not crawled/selected | Improve quality, internal links, uniqueness; wait; **don't spam requests** |
| Crawled – not indexed | Fetched but not selected | Major content upgrade; E-E-A-T; reduce duplication; one re-request |
| Alternate with canonical | Soft-canonicalised | Ensure master is excellent; OK for true aliases |
| Page with redirect | 301/meta refresh | Intentional only |
| Indexed | In index | Optimise title/CTR; build links |

### Sitemap submissions
- One sitemap index or single `sitemap.xml` at root.
- Include **self-canonical indexable** URLs only (or include aliases only if they are uniquely valuable *and* self-canonical).
- Update `lastmod` when content materially changes.
- After big rebuild: GSC → Sitemaps → resubmit / wait for recrawl.

### Re-indexing request workflow
1. Deploy → confirm live HTML changed.
2. URL Inspection → Request indexing.
3. Log in `publish_log.jsonl`.
4. Recheck in 3–14 days; if still discovered-not-indexed, upgrade content again before another request.

---

## Content upgrade blueprints

### A) Medical / MBBS country page (target ≥1,000 words)
1. H1: `MBBS in {Country} for Indian Students — Fees, NMC & Admission {Year}`
2. Lead: who it's for + cost band + NEET note.
3. **Fee breakdown table:** tuition / hostel / mess / insurance / total 5–6 yr (INR ranges).
4. **NMC 2026 guidelines callout:** eligibility, duration, internship — with "verify on NMC" disclaimer.
5. Eligibility checklist (NEET, age, PCB, passport).
6. University shortlist table (3–8 rows): name, city, language, indicative fees.
7. FMGE/NExT planning paragraph.
8. Comparison links to 2 peer countries.
9. **FAQ accordion (≥6)** + FAQPage JSON-LD.
10. CTA: WhatsApp counselling + loan + consultants.

### B) Study-abroad destination (non-MBBS)
1. Cost of study table; visa route; post-study work; intake calendar; exams; sample shortlist; FAQ schema; CTAs.

### C) Comparison page
1. Side-by-side table (fees, duration, language, stay-back, NEET).
2. "Choose X if… / Choose Y if…" decision block.
3. FAQ + schema.

### D) FAQ JSON-LD shape
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "…",
      "acceptedAnswer": {"@type": "Answer", "text": "…"}
    }
  ]
}
```

### E) BreadcrumbList
`Home → Destinations → Study in Georgia` (matching visible breadcrumbs).

---

## Repo commands (agent checklist)

```bash
cd /Users/pkmac/website-designing/launchpadi.com
python3 sitegen/build.py
python3 scripts/publish_daily_guide.py --next
python3 -c "import json,re,pathlib; p=pathlib.Path('mbbs-abroad.htm').read_text(); assert 'FAQPage' in p and 'BreadcrumbList' in p; print('schema ok')"
```

Never commit `.env` or GSC credentials. Do not invent fake university fees — use ranges labelled "indicative".

## Related paths
- Project skill copy: `.cursor/skills/launchpadi-growth/SKILL.md`
- Workspace skill: `/Users/pkmac/website-designing/.cursor/skills/launchpadi-growth/SKILL.md`
- GSC exports: `GSC/latest/`
