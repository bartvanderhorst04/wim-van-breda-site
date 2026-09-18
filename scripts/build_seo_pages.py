#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genereert de nieuwe SEO-landingspagina's + de HTML-sitemap (/sitemap/) als
losse, echte statische .html-bestanden (elk zijn eigen map + index.html),
volledig los van de bestaande SPA (Wim van Breda.dc.html/index.html).

WAAROM STATISCHE BESTANDEN EN GEEN NIEUWE SPA-STATES:
De bestaande site is een single-page app: Component.nav() doet uitsluitend
this.setState(...) — er is nergens history.pushState/replaceState en de
canonical/meta-tags die Component.meta()/applyMeta() zet zijn dus VIRTUEEL:
de browser-URL verandert nooit. vercel.json rewrit alle routes naar
/index.html, dus /merken/herder/ en / serveren vandaag byte-identieke HTML
(geverifieerd). Een nieuwe SPA-state zou dus GEEN eigen crawlbare URL geven.
Vercel serveert een fysiek aanwezig static bestand op een pad wel direct
(geverifieerd voor /robots.txt en /sitemap.xml), vóór de rewrite. Daarom
krijgt elke nieuwe SEO-route hier een eigen, echt statisch bestand met een
eigen <title>/canonical/H1 — dat is de minst ingrijpende manier om dit doel
te bereiken zonder de bestaande SPA-architectuur aan te passen.

Gebruik: python3 scripts/build_seo_pages.py
Schrijft direct in de projectroot (één map per route, met index.html erin).
"""
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.wimvanbreda.nl"
SITE_NAME = "Wim van Breda"

# ---------------------------------------------------------------------------
# Gedeelde chrome: header + footer, visueel gelijk aan de bestaande site
# (zelfde kleuren/font/logo/adres/telefoon/social-links), maar als kale
# statische HTML (geen React-state, geen dropdowns) — deze pagina's hoeven
# geen volledige SPA-interactiviteit te hebben, alleen dezelfde huisstijl.
# Hoofdnav-items linken naar "/" (de bestaande SPA-home): er bestaat vandaag
# geen eigen URL voor "/nieuwe-machines/", "/merken/" etc. (zie hierboven),
# dus een dieper link zou een kapotte/valse route zijn. Dat is een bewuste,
# transparante keuze — zie eindrapport.
# ---------------------------------------------------------------------------

FONT_FACE = """
@font-face{font-family:'Archivo';font-style:normal;font-weight:100 900;font-display:swap;
  src:url('/assets/fonts/archivo-latin-var.woff2') format('woff2-variations'),url('/assets/fonts/archivo-latin-var.woff2') format('woff2');
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}
"""

BASE_CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#FCFCFB;color:#111214;font:400 17px/1.7 'Archivo',sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}
img{max-width:100%;display:block}
.wrap{max-width:1360px;margin:0 auto;padding:0 40px}
@media (max-width:720px){.wrap{padding:0 20px}}

/* ===== Header (statisch, zelfde huisstijl als bestaande site) ===== */
header.wvb-h{position:sticky;top:0;z-index:800;background:#FBAE00;border-bottom:1px solid #C00020;box-shadow:0 18px 40px -32px rgba(17,18,20,.34)}
.wvb-h__bar{max-width:1360px;margin:0 auto;padding:0 40px;height:84px;display:flex;align-items:center;justify-content:space-between;gap:40px}
@media (max-width:720px){.wvb-h__bar{padding:0 20px;height:72px}}
.wvb-h__logo img{height:52px;width:auto;object-fit:contain}
.wvb-h__nav{display:flex;align-items:center;gap:6px}
.wvb-h__nav a{background:none;border:0;padding:10px 16px;font:500 16px/1 'Archivo',sans-serif;color:#000;text-decoration:none;white-space:nowrap}
.wvb-h__web{display:inline-flex;align-items:center;gap:10px;background:transparent;border:1px solid #000;padding:12px 18px;font:600 14px/1 'Archivo',sans-serif;color:#000;text-decoration:none;margin-left:6px}
@media (max-width:980px){.wvb-h__nav{display:none}}

/* ===== Breadcrumb ===== */
.wvb-crumb{font:400 13px/1 'Archivo',sans-serif;color:#8C867A;display:flex;flex-wrap:wrap;align-items:center;gap:8px;padding:28px 0 0}
.wvb-crumb a{color:#8C867A;text-decoration:none}
.wvb-crumb a:hover{color:#111214;text-decoration:underline}
.wvb-crumb span[aria-current]{color:#111214}

/* ===== Content ===== */
main.wvb-main{max-width:840px;margin:0 auto;padding:0 40px 96px}
@media (max-width:720px){main.wvb-main{padding:0 20px 72px}}
h1.wvb-h1{font:600 clamp(30px,4.6vw,46px)/1.08 'Archivo',sans-serif;letter-spacing:-.026em;margin:22px 0 0}
p.wvb-intro{font:400 18px/1.7 'Archivo',sans-serif;color:#3d3b37;margin:22px 0 0}
h2.wvb-h2{font:600 24px/1.25 'Archivo',sans-serif;letter-spacing:-.01em;margin:52px 0 14px}
h3.wvb-h3{font:600 17px/1.3 'Archivo',sans-serif;margin:28px 0 10px}
.wvb-main p{color:#3d3b37;margin:14px 0}
.wvb-main ul{color:#3d3b37;margin:14px 0;padding-left:22px}
.wvb-main li{margin:6px 0}
.wvb-main a.wvb-link{color:#111214;text-decoration:underline;text-decoration-color:#FBAE00;text-decoration-thickness:2px;text-underline-offset:3px;font-weight:500}
.wvb-fact{background:#F7F5F1;border-left:3px solid #FBAE00;padding:18px 22px;margin:28px 0;font:400 16px/1.6 'Archivo',sans-serif;color:#3d3b37}
.wvb-faq details{border-bottom:1px solid #EFECE6;padding:16px 0}
.wvb-faq summary{cursor:pointer;font:600 16px/1.4 'Archivo',sans-serif;color:#111214;list-style:none}
.wvb-faq summary::-webkit-details-marker{display:none}
.wvb-faq summary:before{content:'+ ';color:#C00020;font-weight:700}
.wvb-faq details[open] summary:before{content:'– '}
.wvb-faq p{margin:10px 0 0}
.wvb-cta{margin:44px 0 0;padding:28px 30px;background:#111214;color:#fff}
.wvb-cta p{color:rgba(255,255,255,.78);margin:0 0 16px}
.wvb-cta a{display:inline-flex;align-items:center;gap:10px;background:#FBAE00;color:#111214;border:0;padding:15px 22px;font:600 15px/1 'Archivo',sans-serif;text-decoration:none}
.wvb-related{margin:48px 0 0;padding-top:24px;border-top:1px solid #EFECE6}
.wvb-related__label{font:500 11px/1 'Archivo',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#8C867A;margin:0 0 12px}
.wvb-related__links{display:flex;flex-wrap:wrap;gap:6px 18px;font:500 15px/1.4 'Archivo',sans-serif}
.wvb-related__links a{color:#111214;text-decoration:none;border-bottom:2px solid #FBAE00}

/* ===== Footer (visueel identiek aan bestaande site) ===== */
footer.wvb-f{position:relative;background:#FBAE00;color:#111214;margin-top:72px}
.wvb-f__wrap{max-width:1420px;margin:0 auto;padding:72px 70px 40px}
@media (max-width:720px){.wvb-f__wrap{padding:52px 20px 32px}}
.wvb-f h2{font:600 clamp(24px,3vw,38px)/1.1 'Archivo',sans-serif;letter-spacing:-.026em;margin:0 0 48px;max-width:22ch}
.wvb-f__cols{display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:40px}
@media (max-width:900px){.wvb-f__cols{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.wvb-f__cols{grid-template-columns:1fr}}
.wvb-f img.wvb-f__logo{height:56px;width:auto}
.wvb-f__addr{font:400 15px/1.8 'Archivo',sans-serif;color:rgba(17,18,20,.72);margin-top:22px}
.wvb-f__tel{display:flex;flex-direction:column;gap:10px;margin-top:20px}
.wvb-f__tel a{color:#111214;font:500 15px/1 'Archivo',sans-serif;text-decoration:none;width:max-content;border-bottom:2px solid rgba(17,18,20,.35);padding-bottom:4px}
.wvb-f__title{font:500 11px/1 'Archivo',sans-serif;letter-spacing:.18em;text-transform:uppercase;color:rgba(17,18,20,.62)}
.wvb-f__links{display:flex;flex-direction:column;gap:2px;margin-top:16px}
.wvb-f__links a{padding:8px 0;color:#111214;font:400 15px/1.5 'Archivo',sans-serif;text-decoration:none}
.wvb-f__rule{height:1px;background:rgba(17,18,20,.26);margin-top:56px}
.wvb-f__bottom{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:center;padding-top:24px;font:400 13px/1 'Archivo',sans-serif;color:rgba(17,18,20,.75)}
.wvb-f__legal{display:flex;gap:22px;flex-wrap:wrap}
.wvb-f__legal a{color:rgba(17,18,20,.75);text-decoration:none;font:400 13px/1 'Archivo',sans-serif}
.wvb-f__credit{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.wvb-f__credit a{display:inline-flex;align-items:center;justify-content:center;height:33px;width:142px;padding:0 14px;background:#0B0C0C;border-radius:999px;overflow:hidden}
.wvb-f__credit img{height:100%;width:100%;object-fit:contain}
"""

def header_html():
    return """
<header class="wvb-h">
  <div class="wvb-h__bar">
    <a href="/" class="wvb-h__logo" aria-label="Wim van Breda — home">
      <img src="/assets/wvb-logo.svg" alt="Wim van Breda — Bewuste vooruitgang">
    </a>
    <nav class="wvb-h__nav">
      <a href="/">Aanbod</a>
      <a href="/">Occasions</a>
      <a href="/">Service</a>
      <a href="/">Over ons</a>
      <a href="/">Contact</a>
      <a href="https://webshop.wimvanbreda.nl/" target="_blank" rel="noopener noreferrer" class="wvb-h__web">Webshop →</a>
    </nav>
  </div>
</header>
"""

def footer_html():
    return """
<footer class="wvb-f">
  <div class="wvb-f__wrap">
    <h2>Rust, vakmanschap en machines die blijven draaien.</h2>
    <div class="wvb-f__cols">
      <div>
        <img class="wvb-f__logo" src="/assets/wvb-logo.svg" alt="Wim van Breda">
        <div class="wvb-f__addr">Oudenhof 14<br>4191 NW Geldermalsen</div>
        <div class="wvb-f__tel">
          <a href="tel:+31345585050">+31(0)345 58 50 50</a>
          <a href="https://wa.me/31643070306">WhatsApp +31(0)6 43 07 03 06</a>
        </div>
      </div>
      <div>
        <div class="wvb-f__title">Aanbod</div>
        <div class="wvb-f__links">
          <a href="/">Nieuwe machines</a>
          <a href="/">Occasions</a>
          <a href="/">Verhuur</a>
          <a href="/">Merken</a>
        </div>
      </div>
      <div>
        <div class="wvb-f__title">Over ons</div>
        <div class="wvb-f__links">
          <a href="/">Over ons</a>
          <a href="/">Nieuws</a>
          <a href="/">Werken bij</a>
          <a href="/">Geleverd</a>
        </div>
      </div>
      <div>
        <div class="wvb-f__title">Service &amp; contact</div>
        <div class="wvb-f__links">
          <a href="/">Service aanvragen</a>
          <a href="/">Contact</a>
          <a href="/sitemap/">Sitemap</a>
        </div>
      </div>
    </div>
    <div class="wvb-f__rule"></div>
    <div class="wvb-f__bottom">
      <div>Wim van Breda B.V. · Bewuste Vooruitgang</div>
      <div class="wvb-f__legal">
        <a href="/">Privacy</a>
        <a href="/">Voorwaarden</a>
        <a href="/sitemap/">Sitemap</a>
        <a href="https://nl.linkedin.com/company/wim-van-breda-bv" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href="https://www.facebook.com/wimvanbredabv/?locale=nl_NL" target="_blank" rel="noopener noreferrer">Facebook</a>
        <a href="https://www.instagram.com/wimvanbredabv/" target="_blank" rel="noopener noreferrer">Instagram</a>
      </div>
      <div class="wvb-f__credit">
        <span style="font:400 12px/1 'Archivo',sans-serif;color:rgba(17,18,20,.75)">Website gerealiseerd door:</span>
        <a href="https://aichecked.nl/" target="_blank" rel="noopener noreferrer" aria-label="AIChecked.nl">
          <img src="/assets/aichecked-opt.png" alt="AIChecked.nl" width="300" height="100" loading="lazy" decoding="async">
        </a>
      </div>
    </div>
  </div>
</footer>
"""

def esc(s):
    return html.escape(s, quote=True)

def breadcrumb_html(trail):
    # trail: list of (label, href_or_None). Last item = current page (no link).
    parts = []
    for i, (label, href) in enumerate(trail):
        if i:
            parts.append('<span aria-hidden="true">/</span>')
        if href:
            parts.append(f'<a href="{href}">{esc(label)}</a>')
        else:
            parts.append(f'<span aria-current="page">{esc(label)}</span>')
    return '<nav class="wvb-crumb" aria-label="Kruimelpad">' + ''.join(parts) + '</nav>'

def related_html(items):
    # items: list of (label, href)
    links = ' · '.join(f'<a href="{h}">{esc(l)}</a>' for l, h in items)
    return f"""
<div class="wvb-related">
  <div class="wvb-related__label">Meer over dit onderwerp</div>
  <div class="wvb-related__links">{links}</div>
</div>
"""

def faq_html(items):
    if not items:
        return ""
    blocks = "".join(
        f'<details><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in items
    )
    return f'<h2 class="wvb-h2">Veelgestelde vragen</h2><div class="wvb-faq">{blocks}</div>'

def page_html(page):
    """page: dict met keys title, description, path, h1, trail, intro,
    sections (list of html strings, al met h2/h3/p/ul erin), faq (opt),
    related (opt list), fact (opt html snippet)."""
    canonical = DOMAIN + page['path']
    sections_html = "".join(page.get('sections', []))
    faq = faq_html(page.get('faq', []))
    fact = f'<div class="wvb-fact">{page["fact"]}</div>' if page.get('fact') else ""
    related = related_html(page['related']) if page.get('related') else ""
    cta = page.get('cta_html', DEFAULT_CTA)
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page['title'])}</title>
<meta name="description" content="{esc(page['description'])}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['description'])}">
<meta property="og:url" content="{canonical}">
<link rel="icon" href="data:,">
<link rel="preload" as="font" href="/assets/fonts/archivo-latin-var.woff2" type="font/woff2" crossorigin="crossorigin">
<style>{FONT_FACE}{BASE_CSS}</style>
</head>
<body>
{header_html()}
<div class="wrap">{breadcrumb_html(page['trail'])}</div>
<main class="wvb-main">
  <h1 class="wvb-h1">{esc(page['h1'])}</h1>
  <p class="wvb-intro">{page['intro']}</p>
  {fact}
  {sections_html}
  {faq}
  {cta}
  {related}
</main>
{footer_html()}
</body>
</html>
"""

DEFAULT_CTA = """
<div class="wvb-cta">
  <p>Advies nodig over de juiste machine voor uw situatie?</p>
  <a href="/">Neem contact op</a>
</div>
"""

def h2(title, *body):
    return f'<h2 class="wvb-h2">{esc(title)}</h2>' + "".join(body)

def h3(title, *body):
    return f'<h3 class="wvb-h3">{esc(title)}</h3>' + "".join(body)

def p(html_text):
    return f'<p>{html_text}</p>'

def ul(items):
    return '<ul>' + "".join(f'<li>{it}</li>' for it in items) + '</ul>'

def a(label, href):
    return f'<a class="wvb-link" href="{href}">{esc(label)}</a>'

def write_page(path, html_content):
    """path bv. '/maaiarm/kopen/' -> maaiarm/kopen/index.html"""
    rel = path.strip('/')
    if rel == '':
        target_dir = ROOT
    else:
        target_dir = os.path.join(ROOT, rel)
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, 'index.html')
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    return os.path.relpath(target_file, ROOT)
