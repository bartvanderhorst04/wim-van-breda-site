#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bouwt alle nieuwe SEO-landingspagina's + /sitemap/ als statische bestanden.
Uitvoeren vanuit de scripts/-map: python3 generate.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_seo_pages import (page_html, write_page, ROOT, machine_page_html, contact_page_html)
import machine_data

import seo_content_1, seo_content_2, seo_content_3, seo_content_4, seo_content_5

ALL_PAGES = (seo_content_1.PAGES + seo_content_2.PAGES + seo_content_3.PAGES
             + seo_content_4.PAGES + seo_content_5.PAGES)

# /sitemap/ was tot voor kort een losse, statisch hand-opgemaakte pagina
# (met zijn eigen "look-alike" header/footer i.p.v. de echte globale
# componenten van de site — precies het probleem dat later expliciet is
# gemeld en hersteld, zie eindrapport "Herstel header/footer sitemap").
# De inhoud (groepen + links, ooit hier gedefinieerd als GROUPS/
# MAIN_SITE_LINKS) leeft nu, 1-op-1 overgenomen, in de SPA zelf als
# Component.SITEMAP_GROUPS ("Wim van Breda.dc.html") — dat is voortaan de
# enige bron van waarheid voor de sitemap-inhoud. write_sitemap_shell()
# hieronder publiceert /sitemap/ simpelweg als een letterlijke kopie van
# de SPA-bundel zelf (zelfde bestand als index.html): de SPA herkent bij
# het opstarten window.location.pathname === '/sitemap/' en rendert dan
# automatisch zijn 'sitemap'-paginastatus, met exact dezelfde globale
# header/footer als iedere andere pagina. Toekomstige header/footer- of
# sitemap-inhoudswijzigingen in de SPA werken hierdoor vanzelf door.
def write_sitemap_shell():
    src_path = os.path.join(ROOT, "Wim van Breda.dc.html")
    with open(src_path, encoding="utf-8") as f:
        spa_html = f.read()
    return write_page("/sitemap/", spa_html)

def main():
    written = []
    for pg in ALL_PAGES:
        rel = write_page(pg['path'], page_html(pg))
        written.append(pg['path'])
    sm = write_sitemap_shell()
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
