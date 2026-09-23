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

/* ===== Machinekaartjes ("Relevante machines"): compact, geen grote banners ===== */
.wvb-machines{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:18px 0 8px}
@media (max-width:640px){.wvb-machines{grid-template-columns:1fr}}
.wvb-mcard{border:1px solid #E6E3DD;padding:20px 22px;background:#fff}
.wvb-mcard__brand{font:500 11px/1 'Archivo',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8C867A}
.wvb-mcard__name{font:600 18px/1.3 'Archivo',sans-serif;margin:8px 0 0;color:#111214}
.wvb-mcard__desc{font:400 14px/1.6 'Archivo',sans-serif;color:#57544D;margin:8px 0 0}
.wvb-mcard a.wvb-mcard__cta{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font:600 13px/1 'Archivo',sans-serif;color:#111214;text-decoration:none;border-bottom:2px solid #FBAE00;padding-bottom:2px}

/* ===== Machinedetailpagina (subset van Component.MACHINES, echte data) ===== */
.wvb-mspecs{width:100%;border-collapse:collapse;margin:18px 0}
.wvb-mspecs td{padding:10px 0;border-bottom:1px solid #F1EFEA;font:400 15px/1.5 'Archivo',sans-serif;vertical-align:top}
.wvb-mspecs td:first-child{color:#8C867A;width:42%;padding-right:16px}
.wvb-mspecs td:last-child{color:#111214;font-weight:500}

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
      <a href="/machines/">Aanbod</a>
      <a href="/occasions/">Occasions</a>
      <a href="/service/">Service</a>
      <a href="/over-ons/">Over ons</a>
      <a href="/contact/">Contact</a>
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
          <a href="/machines/">Nieuwe machines</a>
          <a href="/occasions/">Occasions</a>
          <a href="/verhuur/">Verhuur</a>
          <a href="/merken/">Merken</a>
        </div>
      </div>
      <div>
        <div class="wvb-f__title">Over ons</div>
        <div class="wvb-f__links">
          <a href="/over-ons/">Over ons</a>
          <a href="/nieuws/">Nieuws</a>
          <a href="/werken-bij/">Werken bij</a>
          <a href="/geleverd/">Geleverd</a>
        </div>
      </div>
      <div>
        <div class="wvb-f__title">Service &amp; contact</div>
        <div class="wvb-f__links">
          <a href="/service/">Service aanvragen</a>
          <a href="/contact/">Contact</a>
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

def machines_html(heading, machines):
    """machines: list of dicts {name, brand, desc, url} — url = het echte
    bestaande m.url-veld (bv. /machine/herder-grenadier-maaiarm/), waar nu
    ook echt een statische paginakopie van dat machinerecord staat (zie
    machine_page_html hieronder). Geen verzonnen machines, geen homepage-
    fallback: de knop gaat altijd naar de specifieke machine."""
    cards = "".join(f"""
    <div class="wvb-mcard">
      <div class="wvb-mcard__brand">{esc(m['brand'])}</div>
      <div class="wvb-mcard__name">{esc(m['name'])}</div>
      <div class="wvb-mcard__desc">{esc(m['desc'])}</div>
      <a class="wvb-mcard__cta" href="{m['url']}">Bekijk machine →</a>
    </div>""" for m in machines)
    return f'<h2 class="wvb-h2">{esc(heading)}</h2><div class="wvb-machines">{cards}</div>'

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
    related (opt list), fact (opt html snippet), machines (opt: (heading,
    [machine dicts])), cta (opt: (tekst, label, href) — anders DEFAULT_CTA
    naar /contact/)."""
    canonical = DOMAIN + page['path']
    sections_html = "".join(page.get('sections', []))
    machines = machines_html(*page['machines']) if page.get('machines') else ""
    faq = faq_html(page.get('faq', []))
    fact = f'<div class="wvb-fact">{page["fact"]}</div>' if page.get('fact') else ""
    related = related_html(page['related']) if page.get('related') else ""
    cta = cta_html(*page['cta']) if page.get('cta') else DEFAULT_CTA
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
  {machines}
  {faq}
  {cta}
  {related}
</main>
{footer_html()}
</body>
</html>
"""

def cta_html(text, label, href):
    return f"""
<div class="wvb-cta">
  <p>{esc(text)}</p>
  <a href="{href}">{esc(label)}</a>
</div>
"""

# Standaard-CTA gaat naar de nu écht bestaande /contact/-pagina (zie
# contact_page_html) — nooit meer naar "/" als contact bedoeld is.
DEFAULT_CTA = cta_html("Advies nodig over de juiste machine voor uw situatie?", "Neem contact op", "/contact/")

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

def machine_page_html(m):
    """Bouwt een echte, statische machinedetailpagina op het bestaande
    m['url']-pad (bv. /machine/herder-grenadier-maaiarm/), met UITSLUITEND
    velden die al in Component.MACHINES staan (name, brand, type, kort,
    kenmerken, specs, tekst, toepassingen) — niets verzonnen. Dit bestaat
    zodat een "Bekijk machine"-knop vanaf een SEO-landingspagina een echte,
    unieke bestemming heeft in plaats van (via de SPA-rewrite) op de
    homepage te landen. Alleen gebouwd voor machines die daadwerkelijk
    vanaf een SEO-pagina worden gelinkt — geen kopie van alle ~264 records."""
    title = f"{m['name']} | {m['brand']} | Wim van Breda"
    desc = m['kort'] if m.get('kort') else f"{m['name']} van {m['brand']} bij Wim van Breda. {m.get('type','')}."
    desc = desc[:300]
    trail = [("Home", "/"), ("Nieuwe machines", "/machines/"), (m['name'], None)]
    kenmerken_html = ul([esc(k) for k in m.get('kenmerken', [])]) if m.get('kenmerken') else ""
    specs_html = ""
    if m.get('specs'):
        rows = "".join(f"<tr><td>{esc(s['k'])}</td><td>{esc(str(s['v']))}</td></tr>" for s in m['specs'])
        specs_html = f'<table class="wvb-mspecs"><tbody>{rows}</tbody></table>'
    toep_html = ul([esc(t) for t in m.get('toepassingen', [])]) if m.get('toepassingen') else ""
    seo_links = related_html(m['seo_links']) if m.get('seo_links') else ""
    canonical = DOMAIN + m['url']
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="product">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<link rel="icon" href="data:,">
<link rel="preload" as="font" href="/assets/fonts/archivo-latin-var.woff2" type="font/woff2" crossorigin="crossorigin">
<style>{FONT_FACE}{BASE_CSS}</style>
</head>
<body>
{header_html()}
<div class="wrap">{breadcrumb_html(trail)}</div>
<main class="wvb-main">
  <div style="font:500 11px/1 'Archivo',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#8C867A;margin-top:22px">{esc(m['brand'])} · {esc(m.get('type',''))}</div>
  <h1 class="wvb-h1" style="margin-top:10px">{esc(m['name'])}</h1>
  <p class="wvb-intro">{esc(m.get('kort') or '')}</p>
  {h2('Over deze machine', p(esc(m.get('tekst') or ''))) if m.get('tekst') else ''}
  {h2('Kenmerken', kenmerken_html) if kenmerken_html else ''}
  {h2('Specificaties', specs_html) if specs_html else ''}
  {h2('Toepassingen', toep_html) if toep_html else ''}
  {DEFAULT_CTA}
  {seo_links}
</main>
{footer_html()}
</body>
</html>
"""

def contact_page_html():
    """Echte, statische /contact/-pagina — dezelfde adres-/telefoon-/
    WhatsApp-/openingstijdengegevens en hetzelfde formulier (velden +
    action) als de bestaande contactpagina in de SPA (Wim van Breda.dc.html,
    isContact-blok). action wijst — exact als in de SPA — naar de
    formspreeEndpoint-prop, die in het project nog op de ontwikkelplaceholder
    staat ('https://formspree.io/f/your-form-id'); dat is een al bestaande,
    losstaande situatie (niet door deze taak veroorzaakt en hier niet
    op te lossen zonder een echte Formspree-ID). Zodra die er is, hoeft
    alleen deze ene constante te worden aangepast."""
    FORM_ENDPOINT = "https://formspree.io/f/your-form-id"
    trail = [("Home", "/"), ("Contact", None)]
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contact, openingstijden en route | Wim van Breda</title>
<meta name="description" content="Bel, WhatsApp of bezoek Wim van Breda aan de Oudenhof 14 in Geldermalsen. Openingstijden, telefoonnummers per afdeling en contactformulier.">
<link rel="canonical" href="{DOMAIN}/contact/">
<meta name="robots" content="index,follow">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="website">
<meta property="og:title" content="Contact, openingstijden en route | Wim van Breda">
<meta property="og:url" content="{DOMAIN}/contact/">
<link rel="icon" href="data:,">
<link rel="preload" as="font" href="/assets/fonts/archivo-latin-var.woff2" type="font/woff2" crossorigin="crossorigin">
<style>{FONT_FACE}{BASE_CSS}
.wvb-cform{{background:#fff;border:1px solid #EFECE6;padding:32px 28px;margin-top:32px}}
.wvb-cform label{{display:flex;flex-direction:column;gap:8px;font:500 13px/1 'Archivo',sans-serif;margin-top:18px}}
.wvb-cform input,.wvb-cform select,.wvb-cform textarea{{background:#fff;border:0;border-bottom:1px solid #D9D5CD;padding:12px 2px;font:400 15px/1.5 'Archivo',sans-serif}}
.wvb-cform button{{margin-top:24px;display:inline-flex;align-items:center;gap:10px;background:#FBAE00;color:#111214;border:1px solid #111214;padding:16px 24px;font:600 15px/1 'Archivo',sans-serif;cursor:pointer}}
.wvb-crow{{display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px solid #F1EFEA;font:400 15px/1 'Archivo',sans-serif}}
main.wvb-main{{max-width:960px}}
</style>
</head>
<body>
{header_html()}
<div class="wrap">{breadcrumb_html(trail)}</div>
<main class="wvb-main">
  <h1 class="wvb-h1">Contact</h1>
  <p class="wvb-intro">Bel, WhatsApp of loop binnen in Geldermalsen. U spreekt direct iemand die de machines kent.</p>

  <h2 class="wvb-h2">Bezoekadres</h2>
  <p>Oudenhof 14, 4191 NW Geldermalsen. <a class="wvb-link" href="https://maps.google.com/?q=Oudenhof+14+Geldermalsen">Route plannen →</a></p>

  <h2 class="wvb-h2">Bel of WhatsApp ons</h2>
  <div class="wvb-crow"><span>Algemeen</span><a class="wvb-link" href="tel:+31345585050">+31(0)345 58 50 50</a></div>
  <div class="wvb-crow"><span>Sales</span><a class="wvb-link" href="tel:+31345585050">+31(0)345 58 50 50</a></div>
  <div class="wvb-crow"><span>Service</span><a class="wvb-link" href="tel:+31345585050">+31(0)345 58 50 50</a></div>
  <div class="wvb-crow"><span>Onderdelen</span><a class="wvb-link" href="tel:+31345585050">+31(0)345 58 50 50</a></div>
  <p><a class="wvb-link" href="https://wa.me/31643070306">WhatsApp klantenservice: +31(0)6 43 07 03 06</a></p>

  <h2 class="wvb-h2">Stuur ons een bericht</h2>
  <p>Wij reageren op werkdagen binnen één werkdag.</p>
  <form class="wvb-cform" action="{FORM_ENDPOINT}" method="POST">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">
    <input type="hidden" name="pagina_url" value="{DOMAIN}/contact/">
    <input type="hidden" name="_subject" value="Nieuwe aanvraag via wimvanbreda.nl/contact/">
    <label>Naam<input name="naam" required="required"></label>
    <label>Bedrijf<input name="bedrijf"></label>
    <label>E-mailadres<input type="email" name="_replyto" required="required"></label>
    <label>Telefoonnummer<input type="tel" name="telefoon"></label>
    <label>Onderwerp<select name="onderwerp"><option>Nieuwe machine</option><option>Occasion</option><option>Verhuur</option><option>Service</option><option>Onderdelen</option><option>Werken bij</option><option selected="selected">Anders</option></select></label>
    <label>Bericht<textarea name="verzoek" rows="5"></textarea></label>
    <button type="submit">Verstuur bericht →</button>
  </form>
</main>
{footer_html()}
</body>
</html>
"""

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
