#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bouwt alle statische catalogus-/hubpagina's (Fase 1 crawlability-fix).
Uitvoeren vanuit de scripts/-map: python3 generate_catalog.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_catalog_pages as B

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
    print(f"Geschreven: {len(written)} catalogus-/hubpagina's")
    return written

if __name__ == "__main__":
    main()
