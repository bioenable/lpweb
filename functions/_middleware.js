/**
 * Apex launchpadi.com /robots.txt must be a real robots body.
 * Cloudflare treats a 301 as "no robots.txt" and serves Content Signals as 200.
 *
 * This middleware is a catch-all Function, so _redirects may be skipped.
 * Retired thin pages 301 in one hop to https://www.launchpadi.com{hub}.
 * Remaining HTML traffic 301s apex → www.
 */
import { RETIRED_REDIRECTS } from "./_lib/retired-redirects.js";

const CANONICAL_ORIGIN = "https://www.launchpadi.com";

const ROBOTS_BODY = [
  "User-agent: *",
  "Allow: /",
  "",
  "Sitemap: https://www.launchpadi.com/sitemap.xml",
  "",
].join("\n");

function resolveRetired(pathname) {
  if (RETIRED_REDIRECTS[pathname]) return RETIRED_REDIRECTS[pathname];
  if (pathname.length > 1 && pathname.endsWith("/")) {
    const trimmed = pathname.slice(0, -1);
    if (RETIRED_REDIRECTS[trimmed]) return RETIRED_REDIRECTS[trimmed];
  }
  return null;
}

function canonicalRedirectUrl(dest) {
  if (dest.startsWith("http://") || dest.startsWith("https://")) return dest;
  return `${CANONICAL_ORIGIN}${dest}`;
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.pathname === "/robots.txt") {
    return new Response(ROBOTS_BODY, {
      status: 200,
      headers: {
        "content-type": "text/plain; charset=utf-8",
        "cache-control": "public, max-age=0, must-revalidate",
      },
    });
  }

  const mapped = resolveRetired(url.pathname);
  if (mapped) {
    return Response.redirect(canonicalRedirectUrl(mapped), 301);
  }

  if (url.hostname === "launchpadi.com") {
    url.hostname = "www.launchpadi.com";
    url.protocol = "https:";
    return Response.redirect(url.toString(), 301);
  }
  return context.next();
}
