# -*- coding: utf-8 -*-
"""
Bouwt echte, statische detail- en overzichtspagina's voor het hele
productcatalogus-gedeelte van de site (machines, occasions, merken, nieuws,
verhuur, werken-bij, geleverd, magazines, over-ons) — op dezelfde manier en
met dezelfde chrome (header/footer/CSS) als de bestaande 71 SEO-pagina's in
build_seo_pages.py, met UITSLUITEND data uit catalog_data.json (zie
catalog.py) — geen verzonnen tekst, geen gewijzigd design.

Titles/descriptions voor de overzichtspagina's (machines/occasions/merken/
nieuws/service/geleverd/werken-bij/magazines/over-ons) zijn 1-op-1 overgenomen
uit de bestaande meta-generatiefunctie in de SPA zelf (Component.resolveRoute
/ meta()) — dezelfde tekst die de site altíjd al bedoelde te tonen, nu ook
echt in de ruwe HTML aanwezig.
"""
import re
from build_seo_pages import (esc, header_html, footer_html, breadcrumb_html,
    FONT_FACE, BASE_CSS, DOMAIN, SITE_NAME, write_page, h2, h3, p, ul, a,
    related_html, DEFAULT_CTA, cta_html, machines_html)
import catalog as C

# ---------------------------------------------------------------------------
# Kleine, veilige tekstopmaak-helpers (functioneel gelijk aan de
# capFirst/capDescription-hulpfuncties in de SPA: geen inhoud toevoegen,
# alleen nette hoofdletter/lengte-afhandeling van al bestaande tekst).
# ---------------------------------------------------------------------------
def cap_first(s):
    s = (s or "").strip()
    return s[:1].upper() + s[1:] if s else s

def cap_description(s, limit=165):
    s = re.sub(r"\s+", " ", (s or "").strip())
    if not s:
        return s
    if not s.endswith((".", "!", "?")):
        s += "."
    if len(s) <= limit:
        return s
    cut = s[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(".,;: ") + "…"

def title_suffix(t):
    t = (t or "").strip()
    return t if t.endswith(SITE_NAME) else f"{t} | {SITE_NAME}"

# ---------------------------------------------------------------------------
# Generieke paginaromp (zelfde chrome als build_seo_pages.page_html, maar
# met vrije body-HTML in plaats van het vaste secties-formaat — nodig omdat
# deze pagina's een andere inhoudelijke structuur hebben per type).
# ---------------------------------------------------------------------------
def shell(path, title, description, h1, trail, body_html, og_type="website", extra_css=""):
    canonical = DOMAIN + path
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<link rel="icon" href="data:,">
<link rel="preload" as="font" href="/assets/fonts/archivo-latin-var.woff2" type="font/woff2" crossorigin="crossorigin">
<style>{FONT_FACE}{BASE_CSS}
.wvb-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:18px 0 8px}}
@media (max-width:640px){{.wvb-grid{{grid-template-columns:1fr}}}}
.wvb-card{{border:1px solid #E6E3DD;padding:20px 22px;background:#fff}}
.wvb-card__eyebrow{{font:500 11px/1 'Archivo',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8C867A}}
.wvb-card__name{{font:600 18px/1.3 'Archivo',sans-serif;margin:8px 0 0;color:#111214}}
.wvb-card__desc{{font:400 14px/1.6 'Archivo',sans-serif;color:#57544D;margin:8px 0 0}}
.wvb-card a.wvb-card__cta{{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font:600 13px/1 'Archivo',sans-serif;color:#111214;text-decoration:none;border-bottom:2px solid #FBAE00;padding-bottom:2px}}
.wvb-type-group{{margin-top:44px}}
main.wvb-main{{max-width:1040px}}
{extra_css}
</style>
</head>
<body>
{header_html()}
<div class="wrap">{breadcrumb_html(trail)}</div>
<main class="wvb-main">
  <h1 class="wvb-h1">{esc(h1)}</h1>
  {body_html}
</main>
{footer_html()}
</body>
</html>
"""

def card(eyebrow, name, desc, href, cta="Bekijk →"):
    return f"""
    <div class="wvb-card">
      <div class="wvb-card__eyebrow">{esc(eyebrow)}</div>
      <div class="wvb-card__name">{esc(name)}</div>
      <div class="wvb-card__desc">{esc(desc or "")}</div>
      <a class="wvb-card__cta" href="{href}">{esc(cta)}</a>
    </div>"""

def grid(cards_html):
    return f'<div class="wvb-grid">{"".join(cards_html)}</div>'


# ===========================================================================
# MACHINES: alle gepubliceerde machines als eigen /machine/<slug>/-pagina
# (zelfde template als de bestaande 9, nu voor de volledige catalogus) + de
# /machines/-overzichtspagina, gegroepeerd per machinetype.
# ===========================================================================
def _machine_for_template(m):
    """Vertaalt een catalog_data.json-record naar de vorm die
    build_seo_pages.machine_page_html() verwacht (zelfde velden als de 9
    handmatige machine_data.MACHINES-records)."""
    seo_links = None
    return {
        "url": m["url"], "name": m["name"], "brand": m.get("brand") or "",
        "type": m.get("type") or "", "kort": m.get("kort") or "",
        "kenmerken": m.get("kenmerken") or [], "specs": m.get("specs") or [],
        "tekst": m.get("tekst") or "", "toepassingen": m.get("toepassingen") or [],
        "seo_links": seo_links,
    }

def build_all_machines():
    from build_seo_pages import machine_page_html
    written = []
    for m in C.published_machines():
        mt = _machine_for_template(m)
        write_page(m["url"], machine_page_html(mt))
        written.append(m["url"])
    return written

def build_machines_hub():
    machines = C.published_machines()
    by_type = {}
    for m in machines:
        by_type.setdefault(m.get("type") or "Overig", []).append(m)
    sections = []
    for t in sorted(by_type):
        items = by_type[t]
        cards = [card(m.get("brand") or "", m["name"], m.get("kort"), m["url"]) for m in items]
        sections.append(f'<div class="wvb-type-group">{h2(f"{t} ({len(items)})")}{grid(cards)}</div>')
    title = "Nieuwe machines voor groenbeheer | Wim van Breda"
    desc = "Bekijk het actuele aanbod nieuwe machines voor groen-, berm- en terreinbeheer. Filter op machinetype en merk en vraag deskundig advies aan."
    body = f'<p class="wvb-intro">{esc(desc)}</p>' + "".join(sections) + DEFAULT_CTA
    trail = [("Home", "/"), ("Nieuwe machines", None)]
    write_page("/machines/", shell("/machines/", title, desc, "Nieuwe machines voor groenbeheer", trail, body))
    return "/machines/"


# ===========================================================================
# OCCASIONS
# ===========================================================================
def occasion_page_html(o):
    name = o["name"]
    brand = o.get("brand") or ""
    kort = o.get("kort") or (f"{brand} {name} — occasion bij Wim van Breda." if brand else f"{name} — occasion bij Wim van Breda.")
    title = title_suffix(f"{brand} {name}".strip() if brand else name)
    desc = cap_description(kort)
    trail = [("Home", "/"), ("Occasions", "/occasions/"), (name, None)]
    meta_bits = []
    if o.get("bouwjaar"):
        meta_bits.append(("Bouwjaar", o["bouwjaar"]))
    if o.get("uren"):
        meta_bits.append(("Draaiuren", o["uren"]))
    specs_html = ""
    rows = list(meta_bits)
    if o.get("specs"):
        rows += [(s["k"], str(s["v"])) for s in o["specs"]]
    if rows:
        trs = "".join(f"<tr><td>{esc(k)}</td><td>{esc(v)}</td></tr>" for k, v in rows)
        specs_html = f'<table class="wvb-mspecs"><tbody>{trs}</tbody></table>'
    kenmerken_html = ul([esc(k) for k in o.get("kenmerken") or []]) if o.get("kenmerken") else ""
    toep_html = ul([esc(t) for t in o.get("toepassingen") or []]) if o.get("toepassingen") else ""
    tekst = o.get("tekst") or ""
    eyebrow = " · ".join(x for x in [brand, o.get("type")] if x)
    body = f"""
  <div style="font:500 11px/1 'Archivo',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#8C867A;margin-top:-14px">{esc(eyebrow)}</div>
  <p class="wvb-intro">{esc(kort)}</p>
  {h2('Over deze occasion', p(esc(tekst))) if tekst else ''}
  {h2('Kenmerken', kenmerken_html) if kenmerken_html else ''}
  {h2('Specificaties', specs_html) if specs_html else ''}
  {h2('Toepassingen', toep_html) if toep_html else ''}
  {DEFAULT_CTA}
"""
    return shell(o["url"], title, desc, name, trail, body, og_type="product")

def build_all_occasions():
    written = []
    for o in C.published_occasions():
        write_page(o["url"], occasion_page_html(o))
        written.append(o["url"])
    return written

def build_occasions_hub():
    occasions = C.published_occasions()
    by_type = {}
    for o in occasions:
        by_type.setdefault(o.get("type") or "Overig", []).append(o)
    sections = []
    for t in sorted(by_type):
        items = by_type[t]
        cards = [card(o.get("brand") or "", o["name"], o.get("kort") or (o.get("bouwjaar") and f"Bouwjaar {o['bouwjaar']}") or "", o["url"]) for o in items]
        sections.append(f'<div class="wvb-type-group">{h2(f"{t} ({len(items)})")}{grid(cards)}</div>')
    title = "Occasions: gebruikte machines | Wim van Breda"
    desc = "Gebruikte machines voor groen- en terreinbeheer, technisch nagekeken in onze eigen werkplaats. Filter op merk en type."
    body = f'<p class="wvb-intro">{esc(desc)}</p>' + "".join(sections) + DEFAULT_CTA
    trail = [("Home", "/"), ("Occasions", None)]
    write_page("/occasions/", shell("/occasions/", title, desc, "Occasions: gebruikte machines", trail, body))
    return "/occasions/"


# ===========================================================================
# MERKEN — 20 merken uit sitemap.xml; voor elk merk: eigen machines +
# occasions (uit de catalogus, dus altijd actueel/echt) plus de korte
# intro/tekst uit BRANDS of BRANDS_EXTRA waar die bestaat.
# ===========================================================================
def brand_page_html(slug, name, record, machines, occasions):
    intro = (record or {}).get("intro") or ""
    tekst = (record or {}).get("tekst") or ""
    land = (record or {}).get("land") or ""
    if intro:
        desc = cap_description(f"Bekijk het {name}-programma bij Wim van Breda: {intro.rstrip('.')}. Advies, onderdelen en service uit Geldermalsen.")
    else:
        desc = cap_description(f"Het {name}-aanbod bij Wim van Breda: {len(machines)} machines en {len(occasions)} occasions. Advies, onderdelen en service uit Geldermalsen.")
    title = title_suffix(f"{name} machines")
    trail = [("Home", "/"), ("Merken", "/merken/"), (name, None)]
    lead = intro or tekst or f"Het {name}-programma bij Wim van Breda."
    parts = [f'<p class="wvb-intro">{esc(lead)}</p>']
    if tekst and tekst != intro:
        parts.append(p(esc(tekst)))
    if land:
        parts.append(f'<div class="wvb-fact">Land van herkomst: {esc(land)}</div>')
    if machines:
        cards = [card(m.get("type") or "", m["name"], m.get("kort"), m["url"]) for m in machines]
        parts.append(f'<div class="wvb-type-group">{h2(f"{name} machines ({len(machines)})")}{grid(cards)}</div>')
    if occasions:
        cards = [card(o.get("type") or "", o["name"], o.get("kort") or "", o["url"]) for o in occasions]
        parts.append(f'<div class="wvb-type-group">{h2(f"{name} occasions ({len(occasions)})")}{grid(cards)}</div>')
    parts.append(DEFAULT_CTA)
    body = "".join(parts)
    return shell(f"/merken/{slug}/", title, desc, f"{name} machines", trail, body)

def build_all_brands():
    written = []
    brand_names = C.all_brand_slugs_from_catalog()  # slug -> name (from catalog)
    for slug, record in C.BRAND_RECORDS.items():
        name = record.get("name") or brand_names.get(slug) or slug
        machines = C.brand_machines(name)
        occasions = C.brand_occasions(name)
        path = f"/merken/{slug}/"
        write_page(path, brand_page_html(slug, name, record, machines, occasions))
        written.append(path)
    return written

def build_merken_hub():
    items = []
    brand_names = C.all_brand_slugs_from_catalog()
    for slug, record in sorted(C.BRAND_RECORDS.items(), key=lambda kv: (kv[1].get("name") or kv[0]).lower()):
        name = record.get("name") or brand_names.get(slug) or slug
        items.append((slug, name, record))
    cards = [card(r.get("land") or "", name, r.get("intro") or "", f"/merken/{slug}/") for slug, name, r in items]
    title = "Merken machines groenbeheer | Wim van Breda"
    desc = "De merken waarmee Wim van Breda samenwerkt: Herder, Votex, GreenTec en meer. Zoek op merk of filter op machinetype."
    body = f'<p class="wvb-intro">{esc(desc)}</p>{grid(cards)}{DEFAULT_CTA}'
    trail = [("Home", "/"), ("Merken", None)]
    write_page("/merken/", shell("/merken/", title, desc, "Merken machines groenbeheer", trail, body))
    return "/merken/"


# ===========================================================================
# NIEUWS
# ===========================================================================
def news_page_html(n):
    title = title_suffix(n["title"])
    intro = n.get("intro") or ""
    body_paras = n.get("body") or []
    desc = cap_description(intro or (body_paras[0] if body_paras else n["title"]))
    trail = [("Home", "/"), ("Nieuws", "/nieuws/"), (n["title"], None)]
    date_html = f'<div style="font:400 13px/1 \'Archivo\',sans-serif;color:#8C867A;margin-top:14px">{esc(n.get("date") or "")}</div>' if n.get("date") else ""
    intro_html = f'<p class="wvb-intro">{esc(intro)}</p>' if intro else ""
    body_html = "".join(p(esc(par)) for par in body_paras)
    body = date_html + intro_html + body_html + DEFAULT_CTA
    return shell(f"/nieuws/{n['slug']}/", title, desc, n["title"], trail, body, og_type="article")

def build_all_news():
    written = []
    for n in C.published_news():
        path = f"/nieuws/{n['slug']}/"
        write_page(path, news_page_html(n))
        written.append(path)
    return written

def build_nieuws_hub():
    items = sorted(C.published_news(), key=lambda n: n.get("publishedAt") or "", reverse=True)
    cards = [card(n.get("date") or "", n["title"], n.get("intro") or "", f"/nieuws/{n['slug']}/", "Lees artikel →") for n in items]
    title = "Nieuws over machines en het bedrijf | Wim van Breda"
    desc = "Nieuwe machines in het programma, leveringen, beurzen en ontwikkelingen bij Wim van Breda in Geldermalsen."
    body = f'<p class="wvb-intro">{esc(desc)}</p>{grid(cards)}{DEFAULT_CTA}'
    trail = [("Home", "/"), ("Nieuws", None)]
    write_page("/nieuws/", shell("/nieuws/", title, desc, "Nieuws over machines en het bedrijf", trail, body))
    return "/nieuws/"


# ===========================================================================
# VERHUUR — hub + 3 categorieën (met de echte voorwaarden-tekst per
# categorie). Geen automatische machine-selectie per categorie: welke
# machines exact verhuurbaar zijn per categorie staat nergens expliciet in de
# data (alleen rentalPool() = alle gepubliceerde machines), dus om niets te
# verzinnen wordt hier gelinkt naar het volledige machine-aanbod i.p.v. een
# geraden subset.
# ===========================================================================
def build_verhuur():
    written = []
    cards = []
    for r in C.RENTAL:
        slug = C.RENTAL_SLUG.get(r["id"], r["id"])
        cards.append(card("Verhuur", r["name"], r.get("intro") or "", f"/verhuur/{slug}/"))
    title = "Verhuur van machines | Wim van Breda"
    desc = "Machines voor groen-, berm- en terreinbeheer huren bij Wim van Breda in Geldermalsen: kort of langer, met instructie bij aflevering."
    body = f'<p class="wvb-intro">{esc(desc)}</p>{grid(cards)}{DEFAULT_CTA}'
    trail = [("Home", "/"), ("Verhuur", None)]
    write_page("/verhuur/", shell("/verhuur/", title, desc, "Verhuur van machines", trail, body))
    written.append("/verhuur/")

    for r in C.RENTAL:
        slug = C.RENTAL_SLUG.get(r["id"], r["id"])
        path = f"/verhuur/{slug}/"
        title_r = title_suffix(f"{r['name']} huren")
        desc_r = cap_description(f"{r.get('intro','')} Bekijk het verhuuraanbod bij Wim van Breda in Geldermalsen.")
        trail_r = [("Home", "/"), ("Verhuur", "/verhuur/"), (r["name"], None)]
        voorwaarden = r.get("voorwaarden") or []
        vw_html = "".join(p(esc(v)) for v in voorwaarden)
        vw_title = r.get("voorwaardenTitel") or "Voorwaarden"
        body_r = f'<p class="wvb-intro">{esc(r.get("intro") or "")}</p>' + (h2(vw_title, vw_html) if vw_html else "") + DEFAULT_CTA
        write_page(path, shell(path, title_r, desc_r, f"{r['name']} huren", trail_r, body_r))
        written.append(path)
    return written


# ===========================================================================
# SERVICE — geen losse data-array beschikbaar; pagina bouwt uitsluitend op de
# al bestaande, echte omschrijving uit de SPA zelf (geen nieuwe claims).
# ===========================================================================
def build_service():
    title = "Service, reparatie en onderhoud | Wim van Breda"
    desc = "Reparatie en onderhoud van machines in onze werkplaats in Geldermalsen of bij u op locatie. Servicemonteurs, vervangend materieel en duizenden onderdelen op voorraad."
    items = ["Eigen werkplaats in Geldermalsen", "Onderhoud en reparatie op locatie", "Servicemonteurs", "Vervangend materieel", "Duizenden onderdelen op voorraad"]
    body = f'<p class="wvb-intro">{esc(desc)}</p>{h2("Wat wij bieden", ul([esc(i) for i in items]))}{DEFAULT_CTA}'
    trail = [("Home", "/"), ("Service", None)]
    write_page("/service/", shell("/service/", title, desc, "Service, reparatie en onderhoud", trail, body))
    return "/service/"


# ===========================================================================
# GELEVERD — 1 overzichtspagina met de gepubliceerde leveringen (geen losse
# URL's per item in de sitemap).
# ===========================================================================
def build_geleverd():
    items = C.published_deliveries()
    items = sorted(items, key=lambda d: d.get("order") or 0)
    cards = [card(d.get("merk") or "", d.get("machine") or "", d.get("categorie") or "", "/geleverd/", "Zie /geleverd/") for d in items]
    # geen eigen detailpagina per item -> cta linkt naar het contactformulier i.p.v. naar zichzelf
    cards = []
    for d in items:
        cards.append(f"""
    <div class="wvb-card">
      <div class="wvb-card__eyebrow">{esc(d.get('merk') or '')}</div>
      <div class="wvb-card__name">{esc(d.get('machine') or '')}</div>
      <div class="wvb-card__desc">{esc(d.get('categorie') or '')}</div>
    </div>""")
    title = "Geleverde machines en projecten | Wim van Breda"
    desc = "Machines die recent hun weg naar onze klanten vonden: maaiarmen, klepelmaaiers, veegmachines en meer, geleverd door Wim van Breda."
    body = f'<p class="wvb-intro">{esc(desc)}</p>{grid(cards)}{DEFAULT_CTA}'
    trail = [("Home", "/"), ("Geleverd", None)]
    write_page("/geleverd/", shell("/geleverd/", title, desc, "Geleverde machines en projecten", trail, body))
    return "/geleverd/"


# ===========================================================================
# WERKEN BIJ — hub (met de echte WERK_BLOK-introtekst) + 4 vacaturepagina's
# ===========================================================================
def _blokken_html(blokken):
    out = []
    for b in blokken or []:
        kop = b.get("kop")
        items = b.get("items") or []
        if b.get("isList"):
            inner = ul([esc(i) for i in items])
        else:
            inner = "".join(p(esc(i)) for i in items)
        out.append(h3(kop, inner) if kop else inner)
    return "".join(out)

def vacature_page_html(v):
    titel = cap_first(re.sub(r"^Vacature\s+", "", v["titel"]))
    title = title_suffix(titel)
    desc = cap_description(f"{v.get('kort','')} Solliciteer direct bij Wim van Breda in Geldermalsen.")
    trail = [("Home", "/"), ("Werken bij", "/werken-bij/"), (v["titel"], None)]
    meta_bits = [x for x in [("Afdeling", v.get("afdeling")), ("Locatie", v.get("locatie")), ("Uren", v.get("uren"))] if x[1]]
    meta_html = "".join(f'<div class="wvb-crow"><span>{esc(k)}</span><span>{esc(val)}</span></div>' for k, val in meta_bits)
    body = f"""
  <p class="wvb-intro">{esc(v.get('intro') or '')}</p>
  {meta_html}
  {_blokken_html(v.get('blokken'))}
  {cta_html('Interesse in deze functie?', v.get('cta') or 'Solliciteer', '/contact/')}
"""
    return shell(f"/werken-bij/{v['id']}/", title, desc, v["titel"], trail, body, extra_css=".wvb-crow{display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px solid #F1EFEA;font:400 15px/1 'Archivo',sans-serif}")

def build_werken_bij():
    written = []
    intro_paras = (C.WERK_BLOK or {}).get("waar") or []
    intro_html = "".join(p(esc(t)) for t in intro_paras)
    cards = [card(v.get("afdeling") or "", v["titel"], v.get("kort") or "", f"/werken-bij/{v['id']}/", v.get("cta") or "Bekijk vacature →") for v in C.VACANCIES]
    title = "Werken bij Wim van Breda: vacatures | Wim van Breda"
    desc = "Echte vakmensen met passie voor deze sector. Bekijk de actuele vacatures bij Wim van Breda in Geldermalsen of stuur een open sollicitatie."
    body = intro_html + grid(cards)
    trail = [("Home", "/"), ("Werken bij", None)]
    write_page("/werken-bij/", shell("/werken-bij/", title, desc, "Werken bij Wim van Breda", trail, body))
    written.append("/werken-bij/")
    for v in C.VACANCIES:
        path = f"/werken-bij/{v['id']}/"
        write_page(path, vacature_page_html(v))
        written.append(path)
    return written


# ===========================================================================
# MAGAZINES — hub + 6 edities
# ===========================================================================
def build_magazines():
    written = []
    cards = [card(m.get("jaar") or "", m.get("editie") or "", m.get("tekst") or "", f"/magazines/{m['slug']}/") for m in C.MAGAZINES]
    title = "Wim van Breda Magazine | Wim van Breda"
    desc = "Onze magazines met machinenieuws, klantverhalen uit de praktijk en achtergronden over het werk in weg, berm en sloot."
    body = f'<p class="wvb-intro">{esc(desc)}</p>{grid(cards)}{DEFAULT_CTA}'
    trail = [("Home", "/"), ("Magazines", None)]
    write_page("/magazines/", shell("/magazines/", title, desc, "Wim van Breda Magazine", trail, body))
    written.append("/magazines/")
    for m in C.MAGAZINES:
        path = f"/magazines/{m['slug']}/"
        title_m = title_suffix(f"{m.get('editie','')} ({m.get('jaar','')})")
        desc_m = cap_description(m.get("tekst") or desc)
        trail_m = [("Home", "/"), ("Magazines", "/magazines/"), (m.get("editie") or m["slug"], None)]
        body_m = f'<p class="wvb-intro">{esc(m.get("tekst") or "")}</p>{DEFAULT_CTA}'
        write_page(path, shell(path, title_m, desc_m, m.get("editie") or m["slug"], trail_m, body_m))
        written.append(path)
    return written


# ===========================================================================
# OVER ONS — geen los data-array; korte, echte pagina met de bestaande
# meta-omschrijving als basis (geen bedrijfsgeschiedenis-feiten verzonnen
# buiten wat de SPA zelf al claimt).
# ===========================================================================
def build_over_ons():
    title = "Over ons: bewuste vooruitgang sinds 1957 | Wim van Breda"
    desc = "Wim van Breda is een familiebedrijf met 45 collega’s, eigen werkplaats en ruim zestig jaar historie. Lees ons verhaal en bekijk de tijdlijn vanaf 1957."
    body = f'<p class="wvb-intro">{esc(desc)}</p>{DEFAULT_CTA}'
    trail = [("Home", "/"), ("Over ons", None)]
    write_page("/over-ons/", shell("/over-ons/", title, desc, "Over ons: bewuste vooruitgang sinds 1957", trail, body))
    return "/over-ons/"
