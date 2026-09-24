#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bouwt alle statische catalogus-/hubpagina's (Fase 1 crawlability-fix).
Uitvoeren vanuit de scripts/-map: python3 generate_catalog.py

BELANGRIJK — sinds "Herstel de volledige HTML-sitemap structureel":
Elke pagina die build_catalog_pages.py hieronder aanmaakt (alle
/machine/<slug>/, /occasion/<slug>/, /merken/<slug>/ + hub, /nieuws/<slug>/
+ hub, /verhuur/ + categorieën, /service/, /geleverd/, /werken-bij/ + hub,
/magazines/<slug>/ + hub, /over-ons/) wordt NIET meer als eigen,
losstaande "look-alike" HTML/CSS gepubliceerd. In plaats daarvan wordt elk
van deze paden achteraf overschreven met een LETTERLIJKE kopie van
"Wim van Breda.dc.html" zelf (dezelfde bundel als index.html) — zie
write_all_as_spa_copies() hieronder. De SPA herkent bij het opstarten,
via Component.resolveInitialPage()/INITIAL_ROUTE (in de bundel zelf),
aan welk van deze paden hij geladen is en start meteen in de bijbehorende
paginastatus — inclusief de echte, interactieve globale header/footer
(dropdowns, mobiel menu, sticky gedrag) en het echte detail-/hub-template,
i.p.v. een vereenvoudigde statische nabootsing. <base href="/"> in de
bundel zorgt dat alle relatieve foto-URL's (machine-images.js, m.img/
m.gallery e.d. — bewust zonder voorloopslash) ook vanaf deze geneste
paden correct blijven oplossen.

build_catalog_pages.py's eigen page_html()-functies draaien nog gewoon
mee: ze bepalen nog altijd de JUISTE, volledige lijst van paden (nodig
voor sitemap.xml/robots.txt en om exact hetzelfde aantal/dezelfde paden
te blijven schrijven als voorheen) — alleen de UITEINDELIJKE bestandsinhoud
op die paden verandert.

De 59 losse SEO-landingspagina's uit generate.py (seo_content_1..5.py,
bijv. /maaiarm/kopen/, /klepelmaaier/voor-tractor/) hebben GEEN
overeenkomstige SPA-paginastatus — dat zijn bewust unieke, hand-geschreven
inhoudelijke pagina's zonder productcatalogus-duplicaat (zie sitemap-audit
in het eindrapport) en worden hier dus NIET aangeraakt.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_catalog_pages as B
from build_seo_pages import ROOT, write_page

def write_all_as_spa_copies(paths):
    src_path = os.path.join(ROOT, "Wim van Breda.dc.html")
    with open(src_path, encoding="utf-8") as f:
        spa_html = f.read()
    for path in paths:
        write_page(path, spa_html)
    return paths

def main():
    written = []
    written += B.build_all_machines()
    written.append(B.build_machines_hub())
    written += B.build_all_occasions()
    written.append(B.build_occasions_hub())
    written += B.build_all_brands()
    written.append(B.build_merken_hub())
    written += B.build_all_news()
    written.append(B.build_nieuws_hub())
    written += B.build_verhuur()
    written.append(B.build_service())
    written.append(B.build_geleverd())
    written += B.build_werken_bij()
    written += B.build_magazines()
    written.append(B.build_over_ons())
    write_all_as_spa_copies(written)
    print(f"Geschreven: {len(written)} catalogus-/hubpagina's (elk als SPA-kopie, zie moduledocstring)")
    return written

if __name__ == "__main__":
    main()
