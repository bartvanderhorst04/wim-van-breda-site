#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bouwt alle unieke SEO-landingspagina's + /sitemap/ + /contact/ als
statische bestanden. Uitvoeren vanuit de scripts/-map: python3 generate.py

/sitemap/ en /contact/ hebben allebei een echte, bestaande paginastatus in
de SPA zelf ('sitemap'/'contact') — zie Component.resolveInitialPage() in
"Wim van Breda.dc.html" — en worden daarom, net als alle paden uit
generate_catalog.py, gepubliceerd als een LETTERLIJKE kopie van de SPA-
bundel (write_spa_copy hieronder), niet als eigen hand-opgemaakte HTML.
Zo hergebruiken ze automatisch de echte, interactieve globale header/
footer en het echte template, en blijven ze vanzelf in sync met de SPA
(zie eindrapport "Herstel de volledige HTML-sitemap structureel").

De 59 pagina's in ALL_PAGES (seo_content_1..5.py, bijv. /maaiarm/kopen/,
/klepelmaaier/voor-tractor/) zijn bewust WEL eigen, hand-geschreven
inhoudelijke pagina's zonder overeenkomstige SPA-paginastatus of
productcatalogus-duplicaat — die blijven op de bestaande manier (kale
statische HTML via build_seo_pages.header_html()/footer_html()) gebouwd.

Eerder bouwde dit bestand ook nog losstaand 9 losse /machine/<slug>/-
pagina's (machine_data.py/machine_page_html) — die 9 slugs zitten allemaal
al, met dezelfde brondata, in de veel completere 252-machine-lijst van
build_catalog_pages.py/generate_catalog.py (die ze nu bovendien als
SPA-kopie publiceert). Dat dupliceerde-schrijven is verwijderd: twee
scripts die naar hetzelfde pad schrijven zonder van elkaars extra content
te weten, was de oorzaak van een eerder gevonden, apart bijvangst-bugje
(zie eindrapport "Geleverde machines" — filter/galerij-taak).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_seo_pages import page_html, write_page, ROOT

import seo_content_1, seo_content_2, seo_content_3, seo_content_4, seo_content_5

ALL_PAGES = (seo_content_1.PAGES + seo_content_2.PAGES + seo_content_3.PAGES
             + seo_content_4.PAGES + seo_content_5.PAGES)

def write_spa_copy(path):
    src_path = os.path.join(ROOT, "Wim van Breda.dc.html")
    with open(src_path, encoding="utf-8") as f:
        spa_html = f.read()
    return write_page(path, spa_html)

def main():
    written = []
    for pg in ALL_PAGES:
        write_page(pg['path'], page_html(pg))
        written.append(pg['path'])
    written.append(write_spa_copy("/sitemap/"))
    written.append(write_spa_copy("/contact/"))
    # Aanbod-dropdown, 2 nieuwe categorieoverzichten (zelfde SPA-kopie-
    # mechanisme als /sitemap/ en /contact/ hierboven — geen eigen
    # sub-pagina's per item, dus geen aparte build_catalog_pages.py-functie
    # nodig zoals bij /machine/<slug>/ e.d.). Zie Component.resolveInitialPage()
    # ('elektrisch'/'ecologisch') en Component.MACHINES tags:[] in de bundel.
    written.append(write_spa_copy("/elektrische-machines/"))
    written.append(write_spa_copy("/ecologische-machines/"))
    print(f"Geschreven: {len(written)} pagina's (incl. /sitemap/, /contact/, /elektrische-machines/ en /ecologische-machines/ als SPA-kopie)")
    for w in written:
        print(" ", w)
    return written

if __name__ == "__main__":
    main()
