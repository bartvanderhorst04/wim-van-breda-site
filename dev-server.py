#!/usr/bin/env python3
"""Lokale ontwikkelserver voor "Wim van Breda" — statische bestanden + echte 404.

Waarom dit bestand bestaat
--------------------------
De website bestaat uit echte, vooraf-gerenderde statische bestanden per URL
(elke map heeft zijn eigen index.html — zie scripts/build_seo_pages.py en
scripts/build_catalog_pages.py) plus, uitsluitend voor "/" zelf, de
client-side gerouteerde SPA-shell ("Wim van Breda.dc.html").

Vóór de Fase 1 crawlability-fix (zie eindrapport) vielen alle URL's zonder
eigen bestand terug op diezelfde SPA-shell met HTTP 200 — ook voor URL's die
helemaal niet bestaan. Dat gaf false-200's / soft-404's voor elke ongeldige
URL. Nu elke geldige route een eigen bestand heeft, betekent "geen bestand
gevonden" ook echt "deze pagina bestaat niet": de server geeft dan een
eigen 404.html terug met een echte HTTP 404-status, precies zoals Vercel dat
in productie doet zodra er geen rewrite meer naar index.html is (zie
vercel.json).

Wat deze server doet
---------------------
- Een aanvraag die overeenkomt met een écht bestand (afbeeldingen, .js,
  .json, alles in /assets/, /uploads/, enz.) of een map met een eigen
  index.html erin, wordt gewoon normaal geserveerd, met het juiste
  content-type.
- Een aanvraag die met GEEN enkel bestand overeenkomt krijgt de inhoud van
  404.html terug — met een echte HTTP-status 404 (geen 200, geen redirect).
- Er wordt nooit buiten deze projectmap gelezen (geen directory traversal),
  ook niet via "../", URL-encodering of symlinks.

Starten
-------
    python3 dev-server.py

Poort 8791 (zelfde poort als voorheen). Stoppen met Ctrl+C.
Als er al een proces op poort 8791 luistert (bijvoorbeeld de oude
`python -m http.server 8791`), stop dat eerst.
"""
import http.server
import mimetypes
import os
import posixpath
import socket
import sys
import urllib.parse

PORT = 8791
ROOT = os.path.dirname(os.path.abspath(__file__))
NOT_FOUND_FILE = os.path.join(ROOT, "404.html")

# mimetypes-tabel op sommige systemen/Python-versies onvolledig voor deze
# extensies — expliciet aanvullen zodat content-types altijd klopt.
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("image/svg+xml", ".svg")


class SpaFallbackHandler(http.server.SimpleHTTPRequestHandler):
    """Serveert echte bestanden (en mappen met een eigen index.html) normaal;
    geeft voor al het overige een echte HTTP 404 (404.html) terug, met
    bescherming tegen directory traversal. Klasse-naam ongewijzigd gelaten
    om de wijziging minimaal te houden — het gedrag is niet meer 'SPA
    fallback' maar 'static files + real 404', zie moduledocstring."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def _resolve_safe_path(self, url_path):
        """Vertaalt een aangevraagd URL-pad naar een absoluut bestandspad
        BINNEN de servermap. Geeft None terug zodra het resultaat buiten
        ROOT zou vallen (ook via "..", url-encodering of symlinks)."""
        raw_path = url_path.split("?", 1)[0].split("#", 1)[0]
        raw_path = urllib.parse.unquote(raw_path)
        normalized = posixpath.normpath(raw_path)
        # ".."-segmenten worden hier al genegeerd, zodat het samengestelde
        # pad nooit boven ROOT kan uitstijgen.
        segments = [seg for seg in normalized.split("/") if seg and seg != ".."]
        candidate = os.path.join(ROOT, *segments) if segments else ROOT
        resolved = os.path.realpath(candidate)
        root_real = os.path.realpath(ROOT)
        if resolved != root_real and not resolved.startswith(root_real + os.sep):
            return None
        return resolved

    def _serve_not_found(self, head_only):
        if not os.path.isfile(NOT_FOUND_FILE):
            self.send_error(404, "Niet gevonden (en 404.html ontbreekt in " + ROOT + ")")
            return
        try:
            with open(NOT_FOUND_FILE, "rb") as f:
                body = f.read()
        except OSError as exc:
            self.send_error(500, "Kan 404.html niet lezen: " + str(exc))
            return
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        if not head_only:
            self.wfile.write(body)

    def _handle(self, head_only):
        safe_path = self._resolve_safe_path(self.path)
        if safe_path is None:
            self.send_error(403, "Ongeldig of niet-toegestaan pad")
            return
        # Browsers vragen deze paden automatisch op, ongeacht wat de pagina
        # zelf aangeeft (bijv. ondanks een <link rel="icon"> tag). Het zijn
        # nooit geldige SPA-routes, dus een echte 404 hier voorkomt dat elke
        # pageload de volledige ~1MB HTML-pagina als "favicon" downloadt.
        if not os.path.isfile(safe_path) and posixpath.basename(
            self.path.split("?", 1)[0].split("#", 1)[0]
        ) in ("favicon.ico", "apple-touch-icon.png", "apple-touch-icon-precomposed.png"):
            self.send_error(404, "Niet gevonden")
            return
        # Een map met een eigen index.html erin (bv. de nieuwe statische
        # SEO-landingspagina's onder /maaiarm/, /klepelmaaier/, /sitemap/,
        # enz.) moet net als op Vercel als een echt bestand tellen — anders
        # valt elk mapverzoek hieronder alsnog terug op de SPA-shell, terwijl
        # Vercel in productie wél gewoon <map>/index.html serveert.
        if os.path.isdir(safe_path) and os.path.isfile(os.path.join(safe_path, "index.html")):
            safe_path = os.path.join(safe_path, "index.html")
        if os.path.isfile(safe_path):
            # Bestaat als echt bestand: normaal laten serveren (juiste
            # content-type, Content-Length, 304-afhandeling, enz.).
            if head_only:
                super().do_HEAD()
            else:
                super().do_GET()
            return
        # Geen overeenkomend bestand: echte 404. Géén redirect — de
        # browser-URL blijft precies wat de gebruiker heeft geopend, maar de
        # HTTP-status klopt nu wel (zie eindrapport, "echte 404" C4-fix).
        self._serve_not_found(head_only)

    def do_GET(self):
        self._handle(head_only=False)

    def do_HEAD(self):
        self._handle(head_only=True)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main():
    if not os.path.isfile(os.path.join(ROOT, "index.html")):
        sys.exit('Kan "index.html" niet vinden in ' + ROOT)
    if not os.path.isfile(NOT_FOUND_FILE):
        sys.exit('Kan "404.html" niet vinden in ' + ROOT)

    handler = lambda *a, **kw: SpaFallbackHandler(*a, **kw)
    try:
        httpd = http.server.ThreadingHTTPServer(("", PORT), handler)
    except OSError as exc:
        sys.exit(
            "Kan niet starten op poort {port}: {err}\n"
            "Draait er al een server op deze poort? Stop die eerst "
            "(bijvoorbeeld de oude 'python -m http.server {port}') en "
            "probeer het opnieuw.".format(port=PORT, err=exc)
        )

    print("Wim van Breda — lokale server (statische bestanden + echte 404)")
    print("  http://localhost:%d/" % PORT)
    print("  Servermap: %s" % ROOT)
    print("  Stoppen met Ctrl+C.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer gestopt.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
