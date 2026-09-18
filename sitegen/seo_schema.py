"""Schema.org + SEO helpers for LAUNCHPAD static pages."""

from __future__ import annotations

import json
from typing import Any

CANONICAL = "https://www.launchpadi.com"
PHONE_TEL = "+918855833244"


def dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def organization_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": ["Organization", "EducationalOrganization"],
        "name": "LAUNCHPAD",
        "alternateName": ["LAUNCHPADi", "launchpadi.com"],
        "url": CANONICAL,
        "logo": f"{CANONICAL}/images/logo-launchpad.png",
        "image": f"{CANONICAL}/images/logo-launchpad.png",
        "telephone": PHONE_TEL,
        "email": "hello@launchpadi.com",
        "sameAs": ["https://www.youtube.com/@Launchpadi"],
        "description": (
            "Admissions intelligence marketplace for Indian students — "
            "courses, countries, consultants, and AI agents."
        ),
        "areaServed": {"@type": "Country", "name": "India"},
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": PHONE_TEL,
            "contactType": "admissions counselling",
            "areaServed": "IN",
            "availableLanguage": ["English", "Hindi"],
        },
    }


def breadcrumb_schema(items: list[tuple[str, str]]) -> dict:
    """items: list of (name, absolute_or_site_path). Last item may be current page."""
    elements = []
    for i, (name, path) in enumerate(items, start=1):
        if path in ("", "/"):
            loc = f"{CANONICAL}/"
        elif path.startswith("http"):
            loc = path
        else:
            loc = f"{CANONICAL}/{path.lstrip('/')}"
        elements.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": loc,
            }
        )
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }


def faq_schema(faqs: list[tuple[str, str]]) -> dict | None:
    if not faqs:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def course_schema(
    name: str,
    description: str,
    url: str,
    provider_name: str = "LAUNCHPAD",
) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Course",
        "name": name,
        "description": description,
        "url": url if url.startswith("http") else f"{CANONICAL}/{url.lstrip('/')}",
        "provider": {
            "@type": "Organization",
            "name": provider_name,
            "sameAs": CANONICAL,
        },
        "educationalCredentialAwarded": name,
        "inLanguage": "en",
        "audience": {
            "@type": "EducationalAudience",
            "educationalRole": "student",
            "geographicArea": "India",
        },
    }


def webpage_schema(title: str, description: str, url: str, date_modified: str | None = None) -> dict:
    loc = url if url.startswith("http") else (f"{CANONICAL}/" if url in ("", "/") else f"{CANONICAL}/{url.lstrip('/')}")
    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": description,
        "url": loc,
        "isPartOf": {"@type": "WebSite", "name": "LAUNCHPAD", "url": CANONICAL},
        "inLanguage": "en-IN",
        "about": {"@type": "Thing", "name": "Study abroad admissions for Indian students"},
    }
    if date_modified:
        data["dateModified"] = date_modified
    return data


def json_ld_scripts(*schemas: dict | None) -> str:
    blocks = []
    for s in schemas:
        if not s:
            continue
        blocks.append(f'<script type="application/ld+json">\n{dumps(s)}\n</script>')
    return "\n".join(blocks)


def faq_html(faqs: list[tuple[str, str]]) -> str:
    if not faqs:
        return ""
    parts = ['<h2>Frequently asked questions</h2>', '<div class="faq">']
    for i, (q, a) in enumerate(faqs):
        open_attr = " open" if i == 0 else ""
        parts.append(
            f"<details{open_attr}><summary>{_esc(q)}</summary><p>{_esc(a)}</p></details>"
        )
    parts.append("</div>")
    return "\n".join(parts)


def _esc(s: str) -> str:
    import html

    return html.escape(s, quote=True)
