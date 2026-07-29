#!/usr/bin/env python3
"""Generate LAUNCHPAD admissions marketplace static site (100+ SEO pages)."""

from __future__ import annotations

import html
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "https://www.launchpadi.com"
PHONE = "+91 8855-833-244"
PHONE_TEL = "+918855833244"
WA = "918855833244"
BRAND = "LAUNCHPAD"
TAGLINE = "Admissions Intelligence Marketplace"

DESTINATIONS = [
    ("usa", "USA", "Study in USA for Indian Students", "MS, MBA, BS STEM, and Ivy-path counselling with profile building, Common App, and visa guidance.", "₹25–80L+/yr", "Big 4", ["MS in USA", "MBA in USA", "Study in USA without IELTS", "F1 visa consultants"]),
    ("uk", "UK", "Study in UK for Indian Students", "One-year Master's, CAS support, and post-study work routes with transparent fee planning.", "₹20–55L total", "Big 4", ["Study in UK", "UK student visa", "One year masters UK", "CAS guidance"]),
    ("canada", "Canada", "Study in Canada for Indian Students", "PGWP-focused programs, SDS pathways, and college/university shortlists matched to budget.", "₹18–45L/yr", "Big 4", ["Study in Canada", "Canada SDS visa", "PGWP courses", "Colleges in Canada"]),
    ("australia", "Australia", "Study in Australia for Indian Students", "CRICOS-aware shortlists, GTE guidance, and career-aligned bachelor's and master's options.", "₹20–50L/yr", "Big 4", ["Study in Australia", "GTE statement", "Australia student visa"]),
    ("germany", "Germany", "Study in Germany for Indian Students", "Low/no-tuition public universities, APS guidance, and strong engineering & CS pathways.", "₹9–18L/yr living", "Europe", ["Study in Germany free", "APS certificate", "MS in Germany"]),
    ("ireland", "Ireland", "Study in Ireland for Indian Students", "Tech hub master's programs with stay-back options and EU-facing career paths.", "₹18–40L/yr", "Europe", ["Study in Ireland", "Ireland stay back visa"]),
    ("france", "France", "Study in France for Indian Students", "Business schools, public universities, and Campus France process support.", "₹12–35L/yr", "Europe", ["Study in France", "Campus France"]),
    ("italy", "Italy", "Study in Italy for Indian Students", "Affordable EU degrees in design, architecture, medicine pathways, and management.", "₹10–28L/yr", "Europe", ["Study in Italy", "Italy university fees"]),
    ("netherlands", "Netherlands", "Study in Netherlands for Indian Students", "English-taught programs with strong research and innovation ecosystems.", "₹15–35L/yr", "Europe", ["Study in Netherlands"]),
    ("sweden", "Sweden", "Study in Sweden for Indian Students", "Innovation-led master's with scholarship strategies for Indian applicants.", "₹15–32L/yr", "Europe", ["Study in Sweden"]),
    ("singapore", "Singapore", "Study in Singapore for Indian Students", "Asia's education hub for business, computing, and specialty degrees.", "₹25–55L/yr", "Asia", ["Study in Singapore"]),
    ("uae", "UAE", "Study in UAE for Indian Students", "Dubai/Abu Dhabi campuses, branch universities, and Gulf career proximity.", "₹12–40L/yr", "Gulf", ["Study in Dubai", "Study in UAE"]),
    ("new-zealand", "New Zealand", "Study in New Zealand for Indian Students", "Safe destinations with post-study work and practical learning focus.", "₹18–40L/yr", "Oceania", ["Study in New Zealand"]),
    ("japan", "Japan", "Study in Japan for Indian Students", "MEXT scholarship tracks, engineering, and Japanese university pathways.", "₹8–25L/yr", "Asia", ["Study in Japan", "MEXT scholarship"]),
    ("south-korea", "South Korea", "Study in South Korea for Indian Students", "Tech and design programs with growing English-taught options.", "₹10–28L/yr", "Asia", ["Study in South Korea"]),
    ("russia", "Russia", "MBBS & Higher Studies in Russia", "NMC-aware medical universities and engineering options with fee transparency.", "₹15–35L total MBBS", "MBBS", ["MBBS in Russia", "Medical colleges in Russia"]),
    ("georgia", "Georgia", "MBBS in Georgia for Indian Students", "English-medium medicine with competitive packages and FMGE-aware counselling.", "₹20–35L total", "MBBS", ["MBBS in Georgia", "Georgia medical university fees"]),
    ("philippines", "Philippines", "MBBS in Philippines for Indian Students", "USMLE-oriented curricula and clinical exposure with clear fee tables.", "₹18–32L total", "MBBS", ["MBBS in Philippines"]),
    ("kazakhstan", "Kazakhstan", "MBBS in Kazakhstan for Indian Students", "Affordable NMC-listed pathways with hostel and living cost planning.", "₹18–30L total", "MBBS", ["MBBS in Kazakhstan"]),
    ("uzbekistan", "Uzbekistan", "MBBS in Uzbekistan for Indian Students", "Budget medical seats with English medium and admission calendar support.", "₹15–28L total", "MBBS", ["MBBS in Uzbekistan"]),
    ("kyrgyzstan", "Kyrgyzstan", "MBBS in Kyrgyzstan for Indian Students", "Low-cost packages with transparent hostel and Indian food options.", "₹14–26L total", "MBBS", ["MBBS in Kyrgyzstan"]),
    ("bangladesh", "Bangladesh", "MBBS in Bangladesh for Indian Students", "SAARC proximity, similar syllabus familiarity, and NEET-based eligibility.", "₹25–40L total", "MBBS", ["MBBS in Bangladesh"]),
    ("nepal", "Nepal", "MBBS in Nepal for Indian Students", "Nearby medical colleges with Indian-style academic culture.", "₹30–50L total", "MBBS", ["MBBS in Nepal"]),
    ("egypt", "Egypt", "MBBS in Egypt for Indian Students", "WHO-listed universities with competitive clinical training pathways.", "₹20–35L total", "MBBS", ["MBBS in Egypt"]),
    ("armenia", "Armenia", "MBBS in Armenia for Indian Students", "European-adjacent medicine programs with English instruction.", "₹18–32L total", "MBBS", ["MBBS in Armenia"]),
    ("china", "China", "MBBS in China for Indian Students", "English-medium clinical programs with city and university comparison tools.", "₹20–40L total", "MBBS", ["MBBS in China"]),
    ("poland", "Poland", "Study Medicine & Degrees in Poland", "EU medical and STEM pathways for Indian students.", "₹25–45L total", "Europe", ["MBBS in Poland", "Study in Poland"]),
    ("romania", "Romania", "MBBS in Romania for Indian Students", "EU medicine with English tracks and living-cost clarity.", "₹22–40L total", "MBBS", ["MBBS in Romania"]),
    ("bulgaria", "Bulgaria", "MBBS in Bulgaria for Indian Students", "European medical degrees with structured clinical years.", "₹22–38L total", "MBBS", ["MBBS in Bulgaria"]),
]

COURSES = [
    ("mbbs-abroad", "MBBS Abroad", "MBBS Abroad for Indian Students — Fees, Countries & Admission", "Compare NMC-aware universities, total packages, NEET eligibility, and FMGE pathways across top destinations.", ["mbbs abroad", "mbbs abroad for indian students", "cheap mbbs abroad", "neet for mbbs abroad"]),
    ("ms-abroad", "MS Abroad", "MS Abroad for Indian Students", "Master of Science shortlists across US, UK, Canada, Germany, and Australia with SOP and funding guidance.", ["ms abroad", "ms in usa", "ms in germany", "masters abroad"]),
    ("mba-abroad", "MBA Abroad", "MBA Abroad for Indian Students", "Global MBA and specialized management degrees with GMAT/GRE strategy and ROI planning.", ["mba abroad", "mba in usa", "mba in uk", "global mba"]),
    ("btech-abroad", "B.Tech / Engineering Abroad", "Engineering Abroad after Class 12", "Undergraduate engineering pathways including US STEM, German TU9, and Canadian co-op degrees.", ["btech abroad", "engineering abroad", "study engineering abroad"]),
    ("bachelors-abroad", "Bachelor's Abroad", "Bachelor's Degree Abroad for Indian Students", "Liberal arts, STEM, business, and design bachelor's with Common App and foundation routes.", ["bachelors abroad", "undergraduate abroad"]),
    ("nursing-abroad", "Nursing Abroad", "Nursing Courses Abroad for Indian Students", "BNSc/MN pathways in UK, Canada, Australia, and Germany with licensing awareness.", ["nursing abroad", "study nursing abroad"]),
    ("pharmacy-abroad", "Pharmacy Abroad", "Pharmacy Degrees Abroad", "B.Pharm/M.Pharm and Pharm.D pathways with destination licensing notes.", ["pharmacy abroad", "pharm d abroad"]),
    ("dentistry-abroad", "Dentistry Abroad", "BDS / Dentistry Abroad", "Dental degrees with clinical hour transparency and return-to-practice guidance.", ["bds abroad", "dentistry abroad"]),
    ("law-abroad", "Law Abroad", "Study Law Abroad for Indian Students", "LLB/LLM pathways including UK GDL/SQE tracks and US LLM options.", ["llm abroad", "study law abroad"]),
    ("design-abroad", "Design Abroad", "Design & Creative Degrees Abroad", "Fashion, UX, product, and graphic design portfolios for global schools.", ["design courses abroad", "fashion design abroad"]),
    ("data-science-abroad", "Data Science Abroad", "Data Science & AI Master's Abroad", "AI/ML and analytics programs with internship-heavy shortlists.", ["data science abroad", "ai masters abroad"]),
    ("cybersecurity-abroad", "Cybersecurity Abroad", "Cybersecurity Courses Abroad", "Security engineering and risk programs aligned to global job markets.", ["cybersecurity courses abroad"]),
    ("medicine-pg-abroad", "Medical PG Abroad", "MD/MS & Medical PG Abroad", "Residency and PG medicine pathways after Indian MBBS with exam mapping.", ["medical pg abroad", "md abroad after mbbs"]),
    ("physiotherapy-abroad", "Physiotherapy Abroad", "Physiotherapy Courses Abroad", "BPT/MPT equivalent pathways and licensing considerations.", ["physiotherapy abroad"]),
    ("hospitality-abroad", "Hospitality Abroad", "Hotel Management Abroad", "Swiss, UAE, and AU hospitality degrees with paid internship culture.", ["hotel management abroad"]),
    ("finance-abroad", "Finance Abroad", "Finance & CFA-Aligned Degrees Abroad", "MFin, quant finance, and accounting master's for Indian graduates.", ["finance masters abroad", "mfin abroad"]),
    ("architecture-abroad", "Architecture Abroad", "Architecture Degrees Abroad", "B.Arch/M.Arch with portfolio coaching and RIBA/NAAB-aware options.", ["architecture abroad"]),
    ("psychology-abroad", "Psychology Abroad", "Psychology Degrees Abroad", "Clinical and organisational psychology pathways with licensing caveats.", ["psychology abroad"]),
    ("public-health-abroad", "Public Health Abroad", "MPH Abroad for Indian Students", "Public health master's for doctors, nurses, and social-science grads.", ["mph abroad"]),
    ("animation-abroad", "Animation & VFX Abroad", "Animation Courses Abroad", "Portfolio-first animation and VFX schools across Canada, UK, and US.", ["animation courses abroad"]),
]

SERVICES = [
    ("admission-counselling", "Admission Counselling", "Personalised shortlists and admit strategy for UG, PG, MBBS, and secondary pathways."),
    ("university-shortlisting", "University Shortlisting", "Data-backed dream/target/safe lists matched to budget, scores, and career goals."),
    ("application-support", "Application Support", "End-to-end filing, portals, transcripts, and deadline control."),
    ("sop-lor-writing", "SOP & LOR Studio", "Human + AI coached statements that sound like you, not a template."),
    ("visa-guidance", "Student Visa Guidance", "Document checklists, mock interviews, and refusal-risk reviews."),
    ("education-loan-abroad", "Education Loans", "Compare bank/NBFC options, collateral vs non-collateral, and disbursal timelines."),
    ("scholarship-guidance", "Scholarships", "Merit, need, and country scholarships with realistic probability framing."),
    ("pre-departure-support", "Pre-Departure", "Forex, insurance, accommodation, packing, and arrival playbooks."),
    ("profile-evaluation", "Free Profile Evaluation", "15-minute diagnostic of admit chances and next actions."),
    ("interview-preparation", "Interview Prep", "University and visa mock interviews with scorecards."),
    ("accommodation-abroad", "Student Housing", "Verified housing partners and city cost baselines."),
    ("forex-and-remittance", "Forex & Remittance", "LRS-aware fee payment and living remittance guidance."),
    ("test-preparation", "Test Prep Partners", "IELTS, TOEFL, PTE, GRE, GMAT, SAT partner pathways."),
    ("neet-counselling", "NEET Counselling", "India seat strategy + abroad MBBS parallel planning."),
    ("jee-counselling", "JEE Counselling", "India engineering seats with overseas Plan-B shortlists."),
    ("find-consultants", "Find Consultants", "Marketplace of verified counsellors by city, country, and specialty."),
    ("ai-admission-agents", "AI Admission Agents", "Always-on agents for shortlisting, SOP drafts, and checklist tracking."),
    ("secondary-abroad", "Secondary / Boarding Abroad", "Post-Class 10 boarding, IB/A-level, and guardianship guidance."),
]

EXAMS = [
    ("ielts", "IELTS", "IELTS for study abroad — bands, booking, and country requirements."),
    ("toefl", "TOEFL", "TOEFL iBT guidance for US and global university applications."),
    ("pte", "PTE Academic", "PTE scores accepted across UK, Australia, Canada pathways."),
    ("gre", "GRE", "GRE strategy for MS/PhD shortlists and waiver scenarios."),
    ("gmat", "GMAT", "GMAT Focus for MBA admits and scholarship positioning."),
    ("sat", "SAT", "SAT for US undergraduate admissions and merit aid."),
    ("duolingo", "Duolingo English Test", "DET as a fast English proof for select universities."),
    ("neet", "NEET", "NEET for India MBBS and eligibility for many abroad medical seats."),
    ("cuet", "CUET", "CUET for central universities with parallel abroad options."),
    ("cat", "CAT", "CAT for Indian MBA with global MBA Plan-B mapping."),
    ("fmge", "FMGE / NExT", "Licensing pathway awareness for foreign medical graduates."),
    ("aps", "APS (Germany)", "APS certificate process for Indian applicants to Germany."),
]

CITIES = [
    ("delhi", "Delhi NCR"),
    ("mumbai", "Mumbai"),
    ("bangalore", "Bengaluru"),
    ("hyderabad", "Hyderabad"),
    ("chennai", "Chennai"),
    ("pune", "Pune"),
    ("kolkata", "Kolkata"),
    ("ahmedabad", "Ahmedabad"),
    ("chandigarh", "Chandigarh"),
    ("jaipur", "Jaipur"),
    ("lucknow", "Lucknow"),
    ("kochi", "Kochi"),
]

RESOURCES = [
    ("student-journey", "Student Journey Map", "From discovery to departure — the full admissions timeline."),
    ("cost-of-studying-abroad", "Cost of Studying Abroad", "Tuition + living + hidden costs by destination."),
    ("best-country-for-indian-students", "Best Country for Indian Students", "Decision framework by budget, ROI, and visa climate."),
    ("scholarships-abroad", "Scholarships Abroad Guide", "Where real money exists and how to apply early."),
    ("post-study-work-visa", "Post-Study Work Visas", "Stay-back comparisons for Big 4 + Germany/Ireland."),
    ("study-abroad-checklist", "Study Abroad Checklist", "Documents, deadlines, and parent-ready action list."),
    ("compare-countries", "Compare Countries", "Side-by-side destination intelligence."),
    ("compare-courses", "Compare Courses", "MBBS vs engineering vs MS vs MBA trade-offs."),
    ("parents-guide-study-abroad", "Parents' Guide", "How families can evaluate consultants and costs."),
    ("education-loan-guide", "Education Loan Guide", "Collateral, co-applicant, and forex realities."),
    ("sop-examples-guide", "SOP Writing Guide", "Structure, voice, and rejection-proof habits."),
    ("visa-interview-questions", "Visa Interview Questions", "Common questions with strong answer patterns."),
    ("mbbs-abroad-complete-guide", "MBBS Abroad Complete Guide", "Fees, NMC, FMGE, and country shortlists."),
    ("ms-in-cs-guide", "MS in Computer Science Guide", "US/Germany/Canada CS admit playbook."),
    ("secondary-boarding-abroad-guide", "Boarding Schools Abroad", "Post-10th pathways, guardianship, and costs."),
]

INDIA_PAGES = [
    ("study-in-india", "Study in India", "India college admissions intelligence across medical, engineering, and private universities."),
    ("medical-colleges-india", "Medical Colleges in India", "Govt/private MBBS seats, fees ranges, and counselling calendars."),
    ("engineering-colleges-india", "Engineering Colleges in India", "JEE/state counselling with private university alternatives."),
    ("management-colleges-india", "Management Colleges in India", "MBA/PGDM landscape with CAT and profile routes."),
    ("law-colleges-india", "Law Colleges in India", "CLAT and private law school pathways."),
    ("design-colleges-india", "Design Colleges in India", "NID/NIFT and private design school options."),
    ("nursing-colleges-india", "Nursing Colleges in India", "INC-aware nursing admissions guidance."),
    ("private-universities-india", "Private Universities in India", "Compare fees, placements, and accreditation signals."),
    ("scholarship-india", "Scholarships in India", "Central/state and private scholarship routes."),
    ("entrance-exams-india", "Entrance Exams in India", "NEET, JEE, CUET, CLAT, CAT mapped to outcomes."),
]

AI_AGENTS = [
    ("ai-profile-matcher", "Profile Matcher Agent", "Scores your academics, budget, and goals against live destination rules."),
    ("ai-university-finder", "University Finder Agent", "Builds dream/target/safe lists with fee and visa filters."),
    ("ai-visa-assistant", "Visa Assistant Agent", "Checklist builder and mock Q&A for student visas."),
    ("ai-sop-coach", "SOP Coach Agent", "Draft → critique → rewrite loops with plagiarism-safe prompts."),
    ("ai-loan-advisor", "Loan Advisor Agent", "Rough EMI and eligibility framing before bank conversations."),
]

CORE_PAGES = [
    ("about", "About LAUNCHPAD", "We are building India's admissions intelligence marketplace — programs, consultants, AI agents, and transparent guidance in one launchpad."),
    ("how-it-works", "How It Works", "Search opportunities, compare pathways, connect with verified counsellors, or activate AI agents — then apply with confidence."),
    ("admissions-marketplace", "Admissions Marketplace", "Browse countries, courses, consultants, and services the way India actually searches for admissions."),
    ("pricing", "Pricing & Plans", "Free discovery tools, paid counselling packs, and partner marketplace listings."),
    ("offers", "Current Offers", "Limited-time counselling credits, profile evaluations, and partner seat promotions."),
    ("book-counselling", "Book Free Counselling", "Talk to an admissions counsellor on WhatsApp or phone within one business day."),
    ("partner-with-us", "Partner With Us", "Universities, consultancies, and edtechs — list on the LAUNCHPAD marketplace."),
    ("for-consultants", "For Consultants", "Get discovered by high-intent students searching by city and specialty."),
    ("for-universities", "For Universities", "Reach Indian applicants with transparent program pages and lead routing."),
    ("faq", "FAQ", "Answers on fees, visas, MBBS rules, loans, and how our marketplace works."),
    ("privacy-policy", "Privacy Policy", "How we collect and use inquiry data."),
    ("terms", "Terms of Use", "Marketplace terms for students, consultants, and partners."),
    ("careers", "Careers", "Join the team building admissions infrastructure for India."),
    ("resources", "Resources & Guides", "Playbooks for students and parents navigating overseas and India admissions."),
    ("exams", "Entrance & Language Exams", "IELTS to NEET — exam intelligence linked to destinations."),
    ("services", "Admissions Services", "Human counselling + AI agents + marketplace specialists."),
    ("courses", "Courses & Programs", "MBBS, MS, MBA, engineering, nursing, design, and more."),
    ("study-abroad", "Study Abroad Hub", "Country intelligence for Indian students across Big 4, Europe, Gulf, and MBBS destinations."),
    ("ai-agents", "AI Admission Agents", "Always-on helpers for shortlisting, SOP, visa checklists, and loan framing."),
    ("contact-us", "Contact Us", "Phone, WhatsApp, and inquiry form for students, parents, and partners."),
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def head(title: str, description: str, path: str, keywords: str = "") -> str:
    canon = f"{CANONICAL}/{path}" if path not in ("", "/") else f"{CANONICAL}/"
    kw = keywords or "study abroad, admissions consultants, MBBS abroad, education loan, IELTS, university admissions India"
    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="keywords" content="{esc(kw)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#8058A0">
<link rel="canonical" href="{canon}">
<base href="{CANONICAL}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="LAUNCHPAD">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{CANONICAL}/images/logo-launchpad.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
<script type="application/ld+json">
{json.dumps({
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "LAUNCHPAD",
  "alternateName": "LAUNCHPADi",
  "url": CANONICAL,
  "logo": f"{CANONICAL}/images/logo-launchpad.png",
  "telephone": PHONE_TEL,
  "sameAs": ["https://www.youtube.com/@Launchpadi"],
  "description": "Admissions intelligence marketplace for Indian students — courses, countries, consultants, and AI agents."
}, ensure_ascii=False)}
</script>
</head>
<body>
"""


HEADER = f"""
<div class="promo-strip">Free profile evaluation this week · Talk to a counsellor on WhatsApp · <a href="book-counselling.htm">Book now</a> · Call {PHONE}</div>
<header class="site-header">
  <div class="container nav-row">
    <a class="logo" href="index.htm" aria-label="LAUNCHPAD Admissions Intelligence">
      <img src="images/logo-launchpad.png?v=4" alt="LAUNCHPAD" width="140" height="44" decoding="async">
    </a>
    <nav aria-label="Primary">
      <ul class="nav-links">
        <li class="has-mega"><a href="study-abroad.htm">Destinations</a>
          <div class="mega" role="region" aria-label="Destinations">
            <div><h4>Big 4</h4>
              <a href="study-in-usa.htm">USA</a><a href="study-in-uk.htm">UK</a>
              <a href="study-in-canada.htm">Canada</a><a href="study-in-australia.htm">Australia</a>
            </div>
            <div><h4>Europe & Asia</h4>
              <a href="study-in-germany.htm">Germany</a><a href="study-in-ireland.htm">Ireland</a>
              <a href="study-in-singapore.htm">Singapore</a><a href="study-in-uae.htm">UAE</a>
            </div>
            <div><h4>MBBS destinations</h4>
              <a href="study-in-georgia.htm">Georgia</a><a href="study-in-russia.htm">Russia</a>
              <a href="study-in-philippines.htm">Philippines</a><a href="study-in-kazakhstan.htm">Kazakhstan</a>
            </div>
            <div><h4>Explore</h4>
              <a href="study-abroad.htm">All countries</a><a href="compare-countries.htm">Compare</a>
              <a href="mbbs-abroad.htm">MBBS hub</a><a href="best-country-for-indian-students.htm">Best country</a>
            </div>
          </div>
        </li>
        <li class="has-mega"><a href="courses.htm">Courses</a>
          <div class="mega">
            <div><h4>Popular</h4>
              <a href="mbbs-abroad.htm">MBBS Abroad</a><a href="ms-abroad.htm">MS Abroad</a>
              <a href="mba-abroad.htm">MBA Abroad</a><a href="btech-abroad.htm">Engineering</a>
            </div>
            <div><h4>Healthcare</h4>
              <a href="nursing-abroad.htm">Nursing</a><a href="pharmacy-abroad.htm">Pharmacy</a>
              <a href="dentistry-abroad.htm">Dentistry</a><a href="medicine-pg-abroad.htm">Medical PG</a>
            </div>
            <div><h4>Future skills</h4>
              <a href="data-science-abroad.htm">Data Science</a><a href="cybersecurity-abroad.htm">Cybersecurity</a>
              <a href="design-abroad.htm">Design</a><a href="animation-abroad.htm">Animation</a>
            </div>
            <div><h4>India</h4>
              <a href="study-in-india.htm">Study in India</a><a href="neet-counselling.htm">NEET</a>
              <a href="jee-counselling.htm">JEE</a><a href="courses.htm">All courses</a>
            </div>
          </div>
        </li>
        <li><a href="services.htm">Services</a></li>
        <li><a href="find-consultants.htm">Consultants</a></li>
        <li><a href="ai-agents.htm">AI Agents</a></li>
        <li><a href="resources.htm">Resources</a></li>
        <li><a href="offers.htm">Offers</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-primary btn-sm" href="book-counselling.htm">Free counselling</a>
      <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-label="Open menu">☰</button>
    </div>
  </div>
  <div class="container nav-mobile" data-nav-mobile>
    <a href="study-abroad.htm">Destinations</a>
    <a href="courses.htm">Courses</a>
    <a href="services.htm">Services</a>
    <a href="find-consultants.htm">Consultants</a>
    <a href="ai-agents.htm">AI Agents</a>
    <a href="resources.htm">Resources</a>
    <a href="offers.htm">Offers</a>
    <a href="book-counselling.htm">Book free counselling</a>
    <a href="contact-us.htm">Contact</a>
    <a href="https://q.launchpadi.com">LAUNCHPADi-Q Quizzes</a>
  </div>
</header>
"""

FOOTER = f"""
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <div class="footer-brand">LAUNCHPAD</div>
      <p style="margin-top:0.75rem">Admissions intelligence marketplace for Indian students — search courses & countries, connect with consultants, and use AI agents to move faster.</p>
      <p><a href="tel:{PHONE_TEL}">{PHONE}</a></p>
      <p><a href="https://wa.me/{WA}">WhatsApp counselling</a></p>
      <p><a href="https://www.youtube.com/@Launchpadi" target="_blank" rel="noopener">YouTube @Launchpadi</a></p>
    </div>
    <div>
      <h4>Marketplace</h4>
      <a href="admissions-marketplace.htm">Explore</a>
      <a href="study-abroad.htm">Destinations</a>
      <a href="courses.htm">Courses</a>
      <a href="find-consultants.htm">Consultants</a>
      <a href="ai-agents.htm">AI Agents</a>
    </div>
    <div>
      <h4>Services</h4>
      <a href="admission-counselling.htm">Counselling</a>
      <a href="education-loan-abroad.htm">Education loans</a>
      <a href="visa-guidance.htm">Visa guidance</a>
      <a href="sop-lor-writing.htm">SOP & LOR</a>
      <a href="neet-counselling.htm">NEET counselling</a>
    </div>
    <div>
      <h4>Company</h4>
      <a href="about.htm">About</a>
      <a href="how-it-works.htm">How it works</a>
      <a href="pricing.htm">Pricing</a>
      <a href="partner-with-us.htm">Partners</a>
      <a href="careers.htm">Careers</a>
    </div>
    <div>
      <h4>Trust</h4>
      <a href="faq.htm">FAQ</a>
      <a href="contact-us.htm">Contact</a>
      <a href="privacy-policy.htm">Privacy</a>
      <a href="terms.htm">Terms</a>
      <a href="https://q.launchpadi.com">LAUNCHPADi-Q</a>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© 2026 LAUNCHPAD · Admissions Intelligence</span>
    <span>Serving students across India · Marketplace for global admissions</span>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WA}?text={quote('Hi LAUNCHPAD, I want admission guidance')}" aria-label="WhatsApp us" target="_blank" rel="noopener">
  <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M19.11 17.53c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.64.08-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.04-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.08-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.09 3.19 5.06 4.47.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35zM16 3C8.83 3 3 8.83 3 16c0 2.29.6 4.43 1.65 6.29L3 29l6.89-1.61A12.94 12.94 0 0 0 16 29c7.17 0 13-5.83 13-13S23.17 3 16 3zm0 23.67c-2.09 0-4.03-.56-5.71-1.53l-.41-.24-4.09.96.97-3.99-.27-.42A10.63 10.63 0 0 1 5.33 16 10.67 10.67 0 1 1 16 5.33 10.67 10.67 0 0 1 26.67 16 10.67 10.67 0 0 1 16 26.67z"/></svg>
</a>
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


def inquiry_form(title: str = "Get free counselling") -> str:
    dest_opts = "".join(f'<option value="{esc(n)}">{esc(n)}</option>' for _, n, *_ in DESTINATIONS[:16])
    return f"""
<form class="form-card" data-inquiry>
  <h3 style="margin-top:0">{esc(title)}</h3>
  <p class="form-note">Share your details — we open WhatsApp with your inquiry so a counsellor can reply quickly.</p>
  <div class="form-grid two">
    <div class="form-field"><label for="name">Student name</label><input id="name" name="name" required autocomplete="name" placeholder="Full name"></div>
    <div class="form-field"><label for="phone">WhatsApp number</label><input id="phone" name="phone" required inputmode="tel" autocomplete="tel" placeholder="10-digit mobile"></div>
    <div class="form-field"><label for="interest">Looking for</label>
      <select id="interest" name="interest">
        <option value="Study abroad counselling">Study abroad counselling</option>
        <option value="MBBS abroad">MBBS abroad</option>
        <option value="MS / MBA">MS / MBA</option>
        <option value="Education loan">Education loan</option>
        <option value="Find a consultant">Find a consultant</option>
        <option value="India admissions">India admissions</option>
      </select>
    </div>
    <div class="form-field"><label for="destination">Preferred destination</label>
      <select id="destination" name="destination"><option value="">Not sure yet</option>{dest_opts}</select>
    </div>
  </div>
  <div class="form-field" style="margin-top:0.85rem"><label for="message">Message</label><textarea id="message" name="message" rows="3" placeholder="Scores, budget, target year…"></textarea></div>
  <button class="btn btn-primary" type="submit" style="margin-top:1rem;width:100%">Send on WhatsApp</button>
  <p class="form-note" data-form-status>Or call <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
</form>
"""


def page_shell(title: str, description: str, path: str, body: str, keywords: str = "") -> str:
    return head(title, description, path, keywords) + HEADER + body + FOOTER


def homepage() -> str:
    dest_tiles = "".join(
        f'<a class="tile reveal" href="study-in-{slug}.htm"><div class="icon">✈</div><h3>Study in {esc(name)}</h3><p>{esc(blurb[:110])}…</p><div class="meta">{esc(cost)}</div></a>'
        for slug, name, _, blurb, cost, *_ in DESTINATIONS[:8]
    )
    course_tiles = "".join(
        f'<a class="tile reveal" href="{slug}.htm"><h3>{esc(name)}</h3><p>{esc(desc[:100])}…</p><div class="meta">Explore</div></a>'
        for slug, name, _, desc, _ in COURSES[:8]
    )
    body = f"""
<section class="hero">
  <div class="hero-orbit" aria-hidden="true"><img src="assets/svg/orbit.svg" alt="" style="width:100%;height:100%;object-fit:cover"></div>
  <div class="container hero-grid">
    <div>
      <div class="hero-brand">LAUNCHPAD</div>
      <h1>India’s admissions intelligence marketplace</h1>
      <p class="lead">Search courses and countries, compare real fee bands, connect with verified consultants, and use AI agents — for MBBS, MS, MBA, engineering, nursing, and secondary pathways.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="book-counselling.htm">Start free counselling</a>
        <a class="btn btn-ghost" href="admissions-marketplace.htm">Explore marketplace</a>
        <a class="btn btn-ghost" href="ai-agents.htm">Try AI agents</a>
      </div>
      <div class="stats">
        <div class="stat"><b>18.8L+</b><span>Indians studying abroad (MEA)</span></div>
        <div class="stat"><b>30+</b><span>Destination guides</span></div>
        <div class="stat"><b>20+</b><span>Program pathways</span></div>
        <div class="stat"><b>AI + Human</b><span>Guidance that ships</span></div>
      </div>
    </div>
    <div class="hero-panel" data-quick-search>
      <h2>Find your next admit path</h2>
      <div class="quick-search">
        <div><label>Destination</label>
          <select name="destination">
            <option value="">Any country</option>
            {''.join(f'<option value="study-in-{s}.htm">{esc(n)}</option>' for s,n,*_ in DESTINATIONS)}
          </select>
        </div>
        <div><label>Course</label>
          <select name="course">
            <option value="">Any program</option>
            {''.join(f'<option value="{s}.htm">{esc(n)}</option>' for s,n,*_ in COURSES)}
          </select>
        </div>
        <button class="btn btn-primary" type="button" data-quick-go>Search opportunities</button>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Why LAUNCHPAD</div>
      <h2>Not another brochure site — a marketplace for admissions</h2>
      <p class="lead">Students in India don’t just need articles. They need shortlists, fee honesty, counsellor access, loan options, and AI that removes busywork.</p>
    </div>
    <div class="grid-4">
      <a class="tile reveal" href="admissions-marketplace.htm"><div class="icon">◎</div><h3>Opportunity search</h3><p>Countries, courses, and fee bands organised the way families actually decide.</p></a>
      <a class="tile reveal" href="find-consultants.htm"><div class="icon">◈</div><h3>Consultant network</h3><p>Connect with specialists by city, destination, and program — not cold calls.</p></a>
      <a class="tile reveal" href="ai-agents.htm"><div class="icon">✦</div><h3>AI admission agents</h3><p>Profile matching, university finder, SOP coach, visa checklists — on demand.</p></a>
      <a class="tile reveal" href="resources.htm"><div class="icon">▣</div><h3>Knowledge base</h3><p>Guides for NEET, FMGE, loans, visas, and parent decision frameworks.</p></a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Offers live now</div><h2>Promotions that convert — because families need a reason to act</h2></div>
    <div class="offer-row">
      <div class="offer reveal"><div class="tag">Limited</div><h3>Free profile evaluation</h3><p>15-minute admit diagnostic on WhatsApp — scores, budget, and destination fit.</p><a class="btn btn-ghost btn-sm" href="book-counselling.htm">Claim free slot</a></div>
      <div class="offer reveal"><div class="tag">MBBS</div><h3>Country fee comparison</h3><p>Georgia, Russia, Philippines, Kazakhstan packages explained without seat-pressure tactics.</p><a class="btn btn-ghost btn-sm" href="mbbs-abroad.htm">Compare MBBS</a></div>
      <div class="offer reveal"><div class="tag">PG</div><h3>MS/MBA shortlist pack</h3><p>Dream/target/safe list + SOP outline for your next intake.</p><a class="btn btn-ghost btn-sm" href="ms-abroad.htm">Get shortlist</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Destinations</div><h2>Study abroad intelligence for Indian students</h2></div>
    <div class="grid-4">{dest_tiles}</div>
    <p style="margin-top:1.25rem"><a class="btn btn-secondary" href="study-abroad.htm">View all destinations</a></p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Programs</div><h2>From MBBS to data science — one marketplace</h2></div>
    <div class="grid-4">{course_tiles}</div>
    <p style="margin-top:1.25rem"><a class="btn btn-secondary" href="courses.htm">Browse all courses</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">How it works</div><h2>Four steps from confusion to application</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Discover</h3><p>Search by country, course, exam, or budget using our marketplace.</p></div>
      <div class="step reveal"><h3>Decide</h3><p>Compare fees, visas, and ROI with guides built for Indian families.</p></div>
      <div class="step reveal"><h3>Get help</h3><p>Book counselling, hire a consultant, or run AI agents for drafts and checklists.</p></div>
      <div class="step reveal"><h3>Apply</h3><p>File applications, loans, and visas with deadline discipline.</p></div>
    </div>
  </div>
</section>

<section class="section section-ink">
  <div class="container inquiry">
    <div class="reveal">
      <div class="eyebrow" style="color:var(--brand-glow)">Talk to us</div>
      <h2>Ready for a clear next step?</h2>
      <p class="lead">Whether you are planning MBBS abroad, an MS in Germany, or India NEET counselling — start with a human conversation.</p>
      <ul class="trust-list">
        <li>WhatsApp-first counselling for Indian students & parents</li>
        <li>Transparent fee bands — not surprise “packages”</li>
        <li>MBBS + UG + PG + secondary pathways covered</li>
        <li>Marketplace option if you prefer a local consultant</li>
      </ul>
    </div>
    {inquiry_form()}
  </div>
</section>
"""
    return page_shell(
        "LAUNCHPAD — Admissions Intelligence Marketplace | Study Abroad & India Admissions",
        "India’s admissions marketplace: search countries & courses, connect with consultants, use AI agents, and get counselling for MBBS, MS, MBA, and more.",
        "",
        body,
        "study abroad consultants India, MBBS abroad, admissions marketplace, education counselling, study in USA UK Canada Germany",
    )


def content_page(
    slug: str,
    h1: str,
    description: str,
    intro: str,
    bullets: list[str],
    related: list[tuple[str, str]],
    keywords: str,
    extra_html: str = "",
    crumb: str = "Explore",
) -> str:
    rel = "".join(f'<a class="chip" href="{esc(u)}">{esc(t)}</a>' for u, t in related)
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.htm">Home</a> / {esc(crumb)} / {esc(h1)}</div>
    <h1>{esc(h1)}</h1>
    <p class="lead">{esc(description)}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="book-counselling.htm">Free counselling</a>
      <a class="btn btn-secondary" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp now</a>
    </div>
  </div>
</section>
<div class="container layout-split">
  <article class="prose reveal">
    <p>{esc(intro)}</p>
    <h2>What you get on LAUNCHPAD</h2>
    <ul>{''.join(f'<li>{esc(b)}</li>' for b in bullets)}</ul>
    {extra_html}
    <h2>Related pathways</h2>
    <div class="chips">{rel}</div>
    <h2>Ask an admissions counsellor</h2>
    <p>Share your scores, budget, and target year. We’ll map destinations and services that fit — including AI agents for speed and human experts for judgement calls.</p>
  </article>
  <aside>
    <div class="side-cta reveal">
      <h3 style="margin-top:0;color:#fff">Need a decision this week?</h3>
      <p>Book a free profile evaluation. We reply on WhatsApp.</p>
      <a class="btn btn-primary" href="book-counselling.htm" style="width:100%;margin:0.5rem 0">Book now</a>
      <a class="btn btn-ghost btn-sm" href="tel:{PHONE_TEL}" style="width:100%">{PHONE}</a>
    </div>
    <div style="margin-top:1rem">{inquiry_form("Quick inquiry")}</div>
  </aside>
</div>
"""
    return page_shell(f"{h1} | LAUNCHPAD", description, f"{slug}.htm", body, keywords)


def hub_page(slug: str, h1: str, description: str, tiles: list[tuple[str, str, str]], crumb: str) -> str:
    grid = "".join(
        f'<a class="tile reveal" href="{esc(href)}"><h3>{esc(title)}</h3><p>{esc(blurb)}</p><div class="meta">Open</div></a>'
        for href, title, blurb in tiles
    )
    body = f"""
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.htm">Home</a> / {esc(crumb)}</div>
  <h1>{esc(h1)}</h1>
  <p class="lead">{esc(description)}</p>
</div></section>
<section class="section"><div class="container"><div class="grid-3">{grid}</div></div></section>
<section class="section section-alt"><div class="container inquiry"><div><h2>Not sure where to start?</h2><p class="lead">Tell us your goal — we’ll route you to the right destination, course, or consultant.</p></div>{inquiry_form()}</div></section>
"""
    return page_shell(f"{h1} | LAUNCHPAD", description, f"{slug}.htm", body)


def build() -> None:
    pages: dict[str, str] = {}
    pages["index.htm"] = homepage()
    pages["index.html"] = homepage().replace('href="https://www.launchpadi.com/"', 'href="https://www.launchpadi.com/"')

    # Core
    for slug, title, desc in CORE_PAGES:
        if slug in ("resources", "exams", "services", "courses", "study-abroad", "ai-agents", "admissions-marketplace"):
            continue
        bullets = [
            "Clear next steps instead of generic brochures",
            "WhatsApp-first counselling for Indian families",
            "Marketplace access to consultants and partner services",
            "AI agents for shortlists, SOP drafts, and checklists",
        ]
        related = [("admissions-marketplace.htm", "Marketplace"), ("book-counselling.htm", "Counselling"), ("ai-agents.htm", "AI Agents")]
        extra = ""
        if slug == "faq":
            extra = """
            <div class="faq">
              <details open><summary>Is counselling really free?</summary><p>Profile evaluation and first WhatsApp consult are free. Premium application packs are optional and quoted upfront.</p></details>
              <details><summary>Do you only do MBBS abroad?</summary><p>No. LAUNCHPAD covers MBBS, UG, PG, secondary/boarding, India admissions, loans, and visas.</p></details>
              <details><summary>How do consultants on the marketplace work?</summary><p>You can book LAUNCHPAD counselling or choose a listed specialist by city/destination. We focus on transparent scope.</p></details>
              <details><summary>Are AI agents a replacement for counsellors?</summary><p>No. Agents accelerate research and drafts; humans handle judgement, negotiations, and high-stakes visa calls.</p></details>
            </div>"""
        if slug == "pricing":
            extra = """
            <div class="table-wrap"><table class="data">
              <thead><tr><th>Plan</th><th>Best for</th><th>Includes</th><th>Indicative</th></tr></thead>
              <tbody>
                <tr><td>Discover</td><td>Early research</td><td>Guides + AI lite + free evaluation</td><td>₹0</td></tr>
                <tr><td>Counsel</td><td>Families deciding</td><td>1:1 counselling + shortlist</td><td>Quoted</td></tr>
                <tr><td>Apply</td><td>Ready to file</td><td>Applications + SOP studio + tracking</td><td>Quoted</td></tr>
                <tr><td>Partner listing</td><td>Consultants/universities</td><td>Marketplace presence + lead routing</td><td>Partner pricing</td></tr>
              </tbody>
            </table></div>"""
        if slug == "offers":
            extra = """
            <div class="offer-row" style="margin:1.5rem 0">
              <div class="offer"><div class="tag">This week</div><h3>Free profile evaluation</h3><p>WhatsApp diagnostic for 2026/27 intakes.</p></div>
              <div class="offer"><div class="tag">Bundle</div><h3>SOP + shortlist</h3><p>Discounted combo for MS/MBA applicants.</p></div>
              <div class="offer"><div class="tag">Referral</div><h3>Bring a friend</h3><p>Extra counselling credit on successful referral.</p></div>
            </div>"""
        pages[f"{slug}.htm"] = content_page(slug, title, desc, desc, bullets, related, title.lower(), extra, "Company")

    # Destinations hub + pages
    dest_tiles = [(f"study-in-{s}.htm", f"Study in {n}", b) for s, n, _, b, *_ in DESTINATIONS]
    pages["study-abroad.htm"] = hub_page(
        "study-abroad",
        "Study Abroad for Indian Students",
        "Destination intelligence across Big 4, Europe, Gulf, Asia, and MBBS countries — fees, visas, and next actions.",
        dest_tiles,
        "Destinations",
    )
    for slug, name, title, blurb, cost, cluster, kws in DESTINATIONS:
        mbbs_note = ""
        if cluster == "MBBS":
            mbbs_note = f"""
            <h2>MBBS notes for {esc(name)}</h2>
            <p>Indian families comparing MBBS in {esc(name)} should verify current NMC/eligibility notices, English-medium instruction, internship structure, and FMGE/NExT preparation plans. Total packages commonly marketed in India often differ from university tuition alone — always separate tuition, hostel, mess, insurance, and agent fees.</p>
            <ul>
              <li>Ask for a line-item fee sheet, not only a “package” number</li>
              <li>Confirm intake months, NEET documentation, and medium of instruction</li>
              <li>Plan FMGE/NExT prep early if you intend to practise in India</li>
              <li>Use <a href="mbbs-abroad.htm">MBBS Abroad hub</a> to compare destinations</li>
            </ul>"""
        elif cluster == "Big 4":
            mbbs_note = f"""
            <h2>Why Indians shortlist {esc(name)}</h2>
            <p>{esc(name)} remains a core destination for master’s and bachelor’s aspirants. Competition is high, so profile building, English scores, and funding proof matter as much as college brand. Post-study work rules change — treat stay-back as a planning input, not a guarantee.</p>"""
        elif cluster == "Europe":
            mbbs_note = f"""
            <h2>Europe pathway tips — {esc(name)}</h2>
            <p>European options often trade lower tuition for language, blocked-account, or APS-style documentation. Build timelines 9–12 months out and keep a parallel shortlist if one visa corridor tightens.</p>"""
        table = f"""
        <h2>At a glance — {esc(name)}</h2>
        <div class="table-wrap"><table class="data">
          <tr><th>Typical cost band</th><td>{esc(cost)}</td></tr>
          <tr><th>Cluster</th><td>{esc(cluster)}</td></tr>
          <tr><th>Popular searches</th><td>{esc(', '.join(kws[:3]))}</td></tr>
          <tr><th>Who it fits</th><td>Indian students comparing ROI, visa climate, and English-taught options</td></tr>
        </table></div>
        <h2>How Indian students usually evaluate {esc(name)}</h2>
        <p>Families weigh tuition, living costs, post-study work, safety, climate, and whether a consultant or DIY application makes sense. On LAUNCHPAD you can open a destination shortlist, message a counsellor on WhatsApp, or browse consultants who specialise in {esc(name)}.</p>
        {mbbs_note}
        <h2>Popular keywords we optimise for</h2>
        <div class="chips">{''.join(f'<span class="chip">{esc(k)}</span>' for k in kws)}</div>
        <h2>Services for {esc(name)}</h2>
        <div class="chips">
          <a class="chip" href="admission-counselling.htm">Counselling</a>
          <a class="chip" href="visa-guidance.htm">Visa</a>
          <a class="chip" href="education-loan-abroad.htm">Loans</a>
          <a class="chip" href="sop-lor-writing.htm">SOP</a>
          <a class="chip" href="find-consultants.htm">Consultants</a>
          <a class="chip" href="ai-university-finder.htm">AI University Finder</a>
        </div>"""
        pages[f"study-in-{slug}.htm"] = content_page(
            f"study-in-{slug}",
            title,
            blurb,
            f"{blurb} Typical marketed cost band: {cost}. Use LAUNCHPAD to shortlist universities, talk to consultants, and activate AI agents for checklists.",
            [
                f"Country guide for “study in {name} for Indian students” and related queries",
                f"INR-oriented fee framing ({cost}) with counselling for line-item clarity",
                "Visa and post-study work notes for family planning conversations",
                "Connect to counselling, loans, AI agents, and marketplace consultants",
            ],
            [
                ("study-abroad.htm", "All destinations"),
                ("compare-countries.htm", "Compare countries"),
                ("book-counselling.htm", "Book counselling"),
                ("education-loan-abroad.htm", "Loans"),
            ],
            ", ".join(kws + [f"study in {name}", f"{name} for indian students", f"admission consultants for {name}"]),
            table,
            "Destinations",
        )

    # Courses
    course_tiles = [(f"{s}.htm", n, d) for s, n, _, d, _ in COURSES]
    pages["courses.htm"] = hub_page("courses", "Courses & Programs", "Browse MBBS, MS, MBA, engineering, nursing, design, and more — India and abroad.", course_tiles, "Courses")
    for slug, name, title, desc, kws in COURSES:
        pages[f"{slug}.htm"] = content_page(
            slug,
            title,
            desc,
            desc + " LAUNCHPAD combines destination pages, counsellor access, and AI tools so you can decide faster.",
            [
                f"SEO-focused guidance for “{kws[0]}” and related searches",
                "Fee bands and eligibility checkpoints",
                "Link-outs to destinations and exams that unlock admits",
                "Optional human counselling and consultant marketplace",
            ],
            [("courses.htm", "All courses"), ("study-abroad.htm", "Destinations"), ("book-counselling.htm", "Counselling")],
            ", ".join(kws),
            f"<h2>Next actions for {esc(name)}</h2><ol><li>Run a free profile evaluation</li><li>Shortlist 6–10 programs</li><li>Align exams (IELTS/GRE/NEET)</li><li>Plan funding early</li></ol>",
            "Courses",
        )

    # Services
    service_tiles = [(f"{s}.htm", n, d) for s, n, d in SERVICES]
    pages["services.htm"] = hub_page("services", "Admissions Services", "Human counselling, documentation, visas, loans, and AI agents — pick what you need.", service_tiles, "Services")
    for slug, name, desc in SERVICES:
        pages[f"{slug}.htm"] = content_page(
            slug,
            f"{name} | Admissions Service",
            desc,
            desc + " Available as LAUNCHPAD-delivered service or via marketplace specialists.",
            [
                "Clear scope before you pay",
                "WhatsApp coordination for Indian students & parents",
                "Works alongside AI agents for speed",
                "Optional bundling with applications and visas",
            ],
            [("services.htm", "All services"), ("pricing.htm", "Pricing"), ("book-counselling.htm", "Book")],
            f"{name.lower()}, study abroad {name.lower()}, admission consultants",
            "",
            "Services",
        )

    # Exams
    exam_tiles = [(f"{s}-preparation.htm" if s not in ("fmge", "aps", "neet", "cuet", "cat") else (f"{s}.htm" if s in ("fmge", "aps") else f"{s}-counselling.htm" if s in ("neet",) else f"{s}-exam.htm"), n, d) for s, n, d in EXAMS]
    # normalize exam filenames
    exam_files = []
    for slug, name, desc in EXAMS:
        if slug == "neet":
            fname = "neet-exam.htm"
        elif slug in ("cuet", "cat"):
            fname = f"{slug}-exam.htm"
        elif slug in ("fmge", "aps"):
            fname = f"{slug}.htm"
        else:
            fname = f"{slug}-preparation.htm"
        exam_files.append((fname, slug, name, desc))
    pages["exams.htm"] = hub_page(
        "exams",
        "Entrance & Language Exams",
        "Map exams to destinations — IELTS, TOEFL, GRE, GMAT, NEET, CUET, APS, and more.",
        [(f, n, d) for f, _, n, d in exam_files],
        "Exams",
    )
    for fname, slug, name, desc in exam_files:
        pages[fname] = content_page(
            fname.replace(".htm", ""),
            f"{name} Guide for Indian Students",
            desc,
            desc + " Use this page to understand whether the exam is required, optional, or waivable for your shortlist.",
            [
                "Who needs this exam",
                "How scores affect shortlists",
                "Prep partner options on LAUNCHPAD",
                "When to book relative to applications",
            ],
            [("exams.htm", "All exams"), ("test-preparation.htm", "Test prep"), ("book-counselling.htm", "Counselling")],
            f"{name}, {name} for study abroad, {name} Indian students",
            "",
            "Exams",
        )

    # India
    for slug, title, desc in INDIA_PAGES:
        pages[f"{slug}.htm"] = content_page(
            slug,
            title,
            desc,
            desc + " Pair India options with an overseas Plan-B when seats or budgets are uncertain.",
            [
                "India admissions mapped in plain language",
                "Fee and counselling calendar awareness",
                "Parallel overseas options when useful",
                "Counsellor + AI support",
            ],
            [("study-in-india.htm", "Study in India"), ("neet-counselling.htm", "NEET"), ("jee-counselling.htm", "JEE")],
            f"{title}, admissions India, college counselling",
            "",
            "India",
        )

    # Cities
    for slug, name in CITIES:
        pages[f"admission-consultants-{slug}.htm"] = content_page(
            f"admission-consultants-{slug}",
            f"Admission Consultants in {name}",
            f"Find study abroad and MBBS admission consultants serving {name}. Book LAUNCHPAD counselling or browse marketplace specialists.",
            f"Students in {name} search for trusted admission consultants for study abroad, MBBS, MS, and MBA. LAUNCHPAD gives you a national marketplace with local intent pages for faster discovery.",
            [
                f"Local landing page for “admission consultants in {name}”",
                "Study abroad + MBBS + India admissions coverage",
                "WhatsApp counselling from LAUNCHPAD",
                "Option to list as a consultant partner",
            ],
            [("find-consultants.htm", "All consultants"), ("book-counselling.htm", "Book"), ("partner-with-us.htm", "List your firm")],
            f"admission consultants in {name}, study abroad consultants {name}, MBBS consultants {name}",
            "",
            "Consultants",
        )

    # Resources
    pages["resources.htm"] = hub_page(
        "resources",
        "Resources & Guides",
        "Practical playbooks for students and parents — costs, visas, scholarships, MBBS, and more.",
        [(f"{s}.htm", t, d) for s, t, d in RESOURCES],
        "Resources",
    )
    for slug, title, desc in RESOURCES:
        pages[f"{slug}.htm"] = content_page(
            slug,
            title,
            desc,
            desc + " Written for Indian search behaviour and family decision meetings.",
            [
                "Actionable frameworks, not fluff",
                "Links to destination and service pages",
                "Counsellor CTA when you need judgement",
                "Shareable with parents",
            ],
            [("resources.htm", "All guides"), ("compare-countries.htm", "Compare"), ("book-counselling.htm", "Talk to us")],
            f"{title}, study abroad guide, {slug.replace('-', ' ')}",
            "",
            "Resources",
        )

    # AI agents
    pages["ai-agents.htm"] = hub_page(
        "ai-agents",
        "AI Admission Agents",
        "Always-on agents for profile matching, university finding, SOP coaching, visa checklists, and loan framing.",
        [(f"{s}.htm", t, d) for s, t, d in AI_AGENTS],
        "AI Agents",
    )
    for slug, title, desc in AI_AGENTS:
        pages[f"{slug}.htm"] = content_page(
            slug,
            title,
            desc,
            desc + " Pair with human counselling for high-stakes decisions.",
            [
                "Faster research loops",
                "Structured outputs you can share with parents",
                "Escalation path to human experts",
                "Works across MBBS, UG, and PG journeys",
            ],
            [("ai-agents.htm", "All agents"), ("book-counselling.htm", "Human counselling"), ("sop-lor-writing.htm", "SOP studio")],
            f"{title}, AI admissions, study abroad AI",
            f'<p><a class="btn btn-primary" href="book-counselling.htm">Activate with counsellor onboarding</a></p>',
            "AI Agents",
        )

    # Marketplace hub
    pages["admissions-marketplace.htm"] = hub_page(
        "admissions-marketplace",
        "Admissions Marketplace",
        "One launchpad to search programs, destinations, consultants, services, and AI agents.",
        [
            ("study-abroad.htm", "Destinations", "Country intelligence"),
            ("courses.htm", "Courses", "Program pathways"),
            ("find-consultants.htm", "Consultants", "People who can help"),
            ("services.htm", "Services", "Loans, visas, SOPs"),
            ("ai-agents.htm", "AI Agents", "Automation layer"),
            ("offers.htm", "Offers", "Live promotions"),
        ],
        "Marketplace",
    )

    # LAUNCHPADi-Q bridge page
    pages["LAUNCHPADi-Q-MCQ-quiz-web-application.htm"] = content_page(
        "LAUNCHPADi-Q-MCQ-quiz-web-application",
        "LAUNCHPADi-Q — Practice Quizzes for Aspirants",
        "MCQ practice product for entrance and aptitude preparation — part of the LAUNCHPAD ecosystem.",
        "LAUNCHPADi-Q helps aspirants practise with structured quizzes while LAUNCHPAD handles admissions marketplace, counselling, and AI agents.",
        [
            "Quiz practice at q.launchpadi.com",
            "Complements NEET/JEE and aptitude journeys",
            "Pathway into counselling when you’re ready to apply",
        ],
        [("https://q.launchpadi.com", "Open LAUNCHPADi-Q"), ("exams.htm", "Exams"), ("book-counselling.htm", "Counselling")],
        "LAUNCHPADi-Q, MCQ quiz, entrance exam practice",
        '<p><a class="btn btn-primary" href="https://q.launchpadi.com" target="_blank" rel="noopener">Launch quizzes</a></p>',
        "Products",
    )

    # Write pages
    for name, content in pages.items():
        (ROOT / name).write_text(content, encoding="utf-8")

    # Sitemap
    urls = sorted({n for n in pages if n.endswith(".htm")})
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm.append(f"  <url><loc>{CANONICAL}/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>")
    for u in urls:
        if u == "index.htm":
            continue
        pri = "0.9" if u in ("study-abroad.htm", "courses.htm", "admissions-marketplace.htm", "mbbs-abroad.htm") else "0.7"
        sm.append(f"  <url><loc>{CANONICAL}/{u}</loc><changefreq>weekly</changefreq><priority>{pri}</priority></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    (ROOT / "robots.txt").write_text(
        f"""User-agent: *
Allow: /

Sitemap: {CANONICAL}/sitemap.xml
""",
        encoding="utf-8",
    )

    # Redirects: map popular legacy MBBS URLs to new study-in / course pages
    legacy_map = {
        "/mbbs-abroad.htm": "/mbbs-abroad.htm",
        "/mbbs-in-georgia.htm": "/study-in-georgia.htm",
        "/mbbs-in-russia.htm": "/study-in-russia.htm",
        "/mbbs-in-philippines.htm": "/study-in-philippines.htm",
        "/mbbs-in-kazakhstan.htm": "/study-in-kazakhstan.htm",
        "/mbbs-in-uzbekistan.htm": "/study-in-uzbekistan.htm",
        "/mbbs-in-bangladesh.htm": "/study-in-bangladesh.htm",
        "/mbbs-in-nepal.htm": "/study-in-nepal.htm",
        "/mbbs-in-china.htm": "/study-in-china.htm",
        "/mbbs-in-egypt.htm": "/study-in-egypt.htm",
        "/mbbs-in-armenia.htm": "/study-in-armenia.htm",
        "/mbbs-in-romania.htm": "/study-in-romania.htm",
        "/mbbs-in-bulgaria.htm": "/study-in-bulgaria.htm",
        "/mbbs-in-usa.htm": "/study-in-usa.htm",
        "/mbbs-admission-consultants.htm": "/find-consultants.htm",
        "/mbbs-career-counseling.htm": "/admission-counselling.htm",
        "/contact-us.htm": "/contact-us.htm",
        "/neet-counselling.htm": "/neet-counselling.htm",
        "/foreign-medical-graduate-exam.htm": "/fmge.htm",
        "/education-loan-for-mbbs.htm": "/education-loan-abroad.htm",
    }
    redir_lines = [
        "# Cloudflare Pages redirects — LAUNCHPAD redesign 2026",
        "/index.html / 301",
    ]
    # Redirect remaining archived filenames that aren't regenerated
    archived = list((ROOT / "_archive_legacy").glob("*.htm")) if (ROOT / "_archive_legacy").exists() else []
    generated = set(pages.keys())
    for p in archived:
        old = f"/{p.name}"
        if p.name in generated:
            continue
        # smart fallbacks
        target = "/mbbs-abroad.htm" if "mbbs" in p.name else "/study-abroad.htm"
        for k, v in legacy_map.items():
            if k == old:
                target = v
                break
        if "fees" in p.name and "georgia" in p.name:
            target = "/study-in-georgia.htm"
        elif "fees" in p.name and "russia" in p.name:
            target = "/study-in-russia.htm"
        redir_lines.append(f"{old} {target} 301")
    for k, v in legacy_map.items():
        line = f"{k} {v} 301"
        if line not in redir_lines and k.split("/")[-1] not in generated:
            redir_lines.append(line)
    (ROOT / "_redirects").write_text("\n".join(redir_lines) + "\n", encoding="utf-8")

    print(f"Generated {len(pages)} page files")
    print(f"Sitemap URLs: {len(urls)}")
    print(f"Redirect rules: {len(redir_lines)}")


if __name__ == "__main__":
    build()
