# -*- coding: utf-8 -*-
"""
Laadt de echte catalogusdata (machines, occasions, merken, nieuws, verhuur,
vacatures, geleverde machines, magazines) uit catalog_data.json.

Herkomst: 1-op-1 geëxtraheerd uit de Component.MACHINES / Component.OCCASIONS /
Component.BRANDS / Component.BRANDS_EXTRA / Component.NEWS / Component.RENTAL /
Component.VACANCIES / Component.WERK_BLOK / Component.DELIVERIES /
Component.MAGAZINES data-arrays in "Wim van Breda.dc.html" (zie
scripts/extract_catalog.py voor de extractiestap). Niets is verzonnen of
aangevuld — alleen gefilterd op publicatiestatus en gegroepeerd.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalog_data.json"), encoding="utf-8") as f:
    _DATA = json.load(f)

MACHINES_RAW = _DATA["MACHINES"]
OCCASIONS_RAW = _DATA["OCCASIONS"]
BRANDS_CURATED = _DATA["BRANDS"]          # 4 met uitgebreide intro/tekst
BRANDS_EXTRA = _DATA["BRANDS_EXTRA"]      # 16 met kortere intro/tekst
NEWS_RAW = _DATA["NEWS"]
RENTAL = _DATA["RENTAL"]
DELIVERIES_RAW = _DATA["DELIVERIES"]
VACANCIES = _DATA["VACANCIES"]
WERK_BLOK = _DATA["WERK_BLOK"]
MAGAZINES = _DATA["MAGAZINES"]

# Route-slug voor /verhuur/<slug>/ wijkt voor 1 categorie af van het interne id
# (zie Component.resolveRoute, case 'detail', rf-tak: dezelfde mapping).
RENTAL_SLUG = {"maaimachines": "maaimachines", "aanbouwwerktuigen": "aanbouwwerktuigen-maaiarmen-kranen", "bosbouw": "bosbouw"}
RENTAL_SLUG_TO_ID = {v: k for k, v in RENTAL_SLUG.items()}


def slugify(s):
    s = (s or "").strip().lower()
    s = s.replace("ü", "u").replace("ö", "o").replace("ä", "a")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def published_machines():
    return [m for m in MACHINES_RAW if m.get("pubStatus") == "publish" and m.get("url")]


def published_occasions():
    return [o for o in OCCASIONS_RAW if o.get("pubStatus") == "publish" and o.get("url")]


def published_news():
    return list(NEWS_RAW)


def published_deliveries():
    return [d for d in DELIVERIES_RAW if d.get("pubStatus") == "publish"]


# ---------------------------------------------------------------------------
# Merken: elk "/merken/<slug>/"-pad in sitemap.xml komt overeen met een merk
# dat als naam voorkomt bij minstens 1 machine of occasion. Voor 20 van deze
# merken bestaat een los content-record (BRANDS of BRANDS_EXTRA, met intro +
# tekst); voor eventuele overige merken die wel machines/occasions hebben maar
# geen los record, wordt alleen op basis van naam + eigen machines/occasions
# gebouwd (geen intro/tekst verzonnen).
# ---------------------------------------------------------------------------
def _brand_records():
    out = {}
    for b in BRANDS_CURATED:
        out[b["id"]] = dict(b)
    for b in BRANDS_EXTRA:
        out.setdefault(b["id"], dict(b))
    return out


BRAND_RECORDS = _brand_records()


def brand_machines(brand_name):
    return [m for m in published_machines() if (m.get("brand") or "").strip().lower() == brand_name.strip().lower()]


def brand_occasions(brand_name):
    return [o for o in published_occasions() if (o.get("brand") or "").strip().lower() == brand_name.strip().lower()]


def all_brand_slugs_from_catalog():
    """Alle merknamen die als brand voorkomen bij een gepubliceerde machine of
    occasion, met hun slug — gebruikt om te bepalen welke naam bij een
    /merken/<slug>/-URL uit de sitemap hoort, ook als er geen los BRANDS(-
    EXTRA)-record voor is."""
    names = {}
    for m in published_machines():
        b = m.get("brand")
        if b:
            names[slugify(b)] = b
    for o in published_occasions():
        b = o.get("brand")
        if b:
            names[slugify(b)] = b
    return names
