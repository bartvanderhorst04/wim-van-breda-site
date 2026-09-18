#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bouwt alle nieuwe SEO-landingspagina's + /sitemap/ als statische bestanden.
Uitvoeren vanuit de scripts/-map: python3 generate.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_seo_pages import (page_html, write_page, esc, header_html, footer_html,
    breadcrumb_html, FONT_FACE, BASE_CSS, DOMAIN, machine_page_html, contact_page_html)
import machine_data

import seo_content_1, seo_content_2, seo_content_3, seo_content_4, seo_content_5

ALL_PAGES = (seo_content_1.PAGES + seo_content_2.PAGES + seo_content_3.PAGES
             + seo_content_4.PAGES + seo_content_5.PAGES)

# Groepen voor de HTML-sitemap (/sitemap/), in de door de opdracht gevraagde volgorde.
GROUPS = [
    ("Maaiarm", ["/maaiarm/","/maaiarm/kopen/","/maaiarm/voor-tractor/","/maaiarm/bermonderhoud/",
                 "/maaiarm/slootonderhoud/","/maaiarm/herder/","/maaiarm/greentec/"]),
    ("Klepelmaaier", ["/klepelmaaier/","/klepelmaaier/kopen/","/klepelmaaier/voor-tractor/",
                       "/klepelmaaier/bermonderhoud/","/klepelmaaier/ruw-terrein/","/klepelmaaier/omarv/",
                       "/klepelmaaier/votex/","/klepelmaaier/greentec/"]),
    ("Maaikorf", ["/maaikorf/","/maaikorf/kopen/","/maaikorf/slootonderhoud/","/maaikorf/voor-maaiarm/",
                   "/maaikorf/voor-watergangen/","/maaikorf/voor-tractor/","/maaikorf/herder/"]),
    ("Ecologisch maaien", ["/ecologisch-maaien/","/ecologisch-maaien/machines/","/ecologisch-maaien/bermmaaien/",
                            "/ecologisch-maaien/maaien-met-afvoer/","/ecologisch-bermbeheer/"]),
    ("Bermonderhoud", ["/bermonderhoud/","/bermonderhoud/machines/","/bermonderhoud/maaiarm/",
                        "/bermonderhoud/klepelmaaier/","/bermonderhoud/ecologisch/"]),
    ("Slootonderhoud", ["/slootonderhoud/","/slootonderhoud/machines/","/slootonderhoud/maaiarm/",
                         "/slootonderhoud/maaikorf/","/taludmaaien/","/taludonderhoud-machines/"]),
    ("Tuin- en parkmachines", ["/tuin-en-parkmachines/","/tuin-en-parkmachines/kopen/","/tuin-en-parkmachines/professioneel/",
                                "/tuin-en-parkmachines/gemeenten/","/tuin-en-parkmachines/aannemers/",
                                "/tuin-en-parkmachines/terreinonderhoud/"]),
    ("Werktuigdragers", ["/werktuigdrager/","/werktuigdrager/kopen/","/werktuigdrager/professioneel/",
                          "/werktuigdrager/bermonderhoud/","/werktuigdrager/slootonderhoud/"]),
    ("Merken", ["/herder/maaiarm/","/herder/maaikorf/","/greentec/maaiarm/","/greentec/klepelmaaier/",
                "/omarv/klepelmaaier/","/votex/klepelmaaier/"]),
    ("Regio's", ["/regio/geldermalsen/","/regio/betuwe/","/regio/rivierenland/","/regio/zaltbommel/"]),
]

# "Belangrijke websitepagina's": bestaan vandaag alleen als interne SPA-state,
# zonder eigen URL (Component.nav() doet uitsluitend setState, geen
# history.pushState — geverifieerd dat /merken/herder/ en / vandaag
# byte-identieke HTML serveren). Een link naar een specifiek pad zou dus een
# valse/kapotte route zijn; deze rij linkt daarom bewust naar "/", vanwaar de
# bezoeker via het bestaande hoofdmenu bij elke sectie komt. Zie eindrapport.
MAIN_SITE_LINKS = ["Nieuwe machines","Merken","Occasions","Verhuur","Service","Actueel / Nieuws","Over ons"]
# "Contact" heeft nu wél een echte, eigen URL (zie contact_page_html) en
# krijgt daarom een eigen link i.p.v. de generieke "/"-fallback hierboven.

def build_sitemap_page():
    path = "/sitemap/"
    trail = [("Home","/"), ("Sitemap", None)]
    intro = "Overzicht van de website van Wim van Breda: bestaande hoofdpagina's en de nieuwe inhoudelijke pagina's per onderwerp."

    def link_list(items):
        return '<ul>' + "".join(f'<li><a class="wvb-link" href="{href}">{esc(_page_h1(href))}</a></li>' for href in items) + '</ul>'

    def main_link_list(labels):
        return '<ul>' + "".join(f'<li><a class="wvb-link" href="/">{esc(l)}</a></li>' for l in labels) + '</ul>'

    sections_html = []
    main_items_html = '<ul>' + "".join(f'<li><a class="wvb-link" href="/">{esc(l)}</a></li>' for l in MAIN_SITE_LINKS)
    main_items_html += '<li><a class="wvb-link" href="/contact/">Contact</a></li></ul>'
    sections_html.append('<h2 class="wvb-h2">Belangrijke websitepagina’s</h2>' + main_items_html)
    for label, paths in GROUPS:
        sections_html.append(f'<h2 class="wvb-h2">{esc(label)}</h2>' + link_list(paths))
    sections_html.append('<h2 class="wvb-h2">Overig</h2><ul><li><a class="wvb-link" href="/sitemap/">Sitemap</a> (deze pagina)</li></ul>')

    body = f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sitemap | Wim van Breda</title>
<meta name="description" content="Overzicht van alle pagina's van de website van Wim van Breda, gegroepeerd per onderwerp.">
<link rel="canonical" href="{DOMAIN}/sitemap/">
<meta name="robots" content="index,follow">
<link rel="icon" href="data:,">
<link rel="preload" as="font" href="/assets/fonts/archivo-latin-var.woff2" type="font/woff2" crossorigin="crossorigin">
<style>{FONT_FACE}{BASE_CSS}
.wvb-main ul{{list-style:none;padding:0;margin:8px 0 0;columns:2;column-gap:32px}}
@media (max-width:640px){{.wvb-main ul{{columns:1}}}}
.wvb-main li{{break-inside:avoid;margin:0;padding:7px 0;border-bottom:1px solid #F1EFEA}}
main.wvb-main{{max-width:960px}}
</style>
</head>
<body>
{header_html()}
<div class="wrap">{breadcrumb_html(trail)}</div>
<main class="wvb-main">
  <h1 class="wvb-h1">Sitemap</h1>
  <p class="wvb-intro">{intro}</p>
  <p>De pagina's onder “Belangrijke websitepagina’s” zijn onderdeel van de hoofdwebsite en bereikbaar via het menu op de homepage.</p>
  {''.join(sections_html)}
</main>
{footer_html()}
</body>
</html>
"""
    write_page(path, body)
    return path

# Klein label-woordenboek voor de sitemap-links (mooiere labels dan een pad).
_LABELS = {}
def _register_labels():
    for p in ALL_PAGES:
        _LABELS[p['path']] = p['h1']
_register_labels()

def _page_h1(path):
    return _LABELS.get(path, path)

def main():
    written = []
    for pg in ALL_PAGES:
        rel = write_page(pg['path'], page_html(pg))
        written.append(pg['path'])
    sm = build_sitemap_page()
    written.append(sm)
    write_page("/contact/", contact_page_html())
    written.append("/contact/")
    for slug, m in machine_data.MACHINES.items():
        write_page(m['url'], machine_page_html(m))
        written.append(m['url'])
    print(f"Geschreven: {len(written)} pagina's (incl. /sitemap/, /contact/ en {len(machine_data.MACHINES)} machinepagina's)")
    for w in written:
        print(" ", w)
    return written

if __name__ == "__main__":
    main()
