#!/usr/bin/env python3
"""Lokale ontwikkelserver voor "Wim van Breda" — statische bestanden + SPA-fallback.

Waarom dit bestand bestaat
--------------------------
De website is één client-side gerouteerde pagina ("Wim van Breda.dc.html").
De eerder toegevoegde browserrouter (Component.resolveRoute in dat bestand)
leest de URL pas NADAT de pagina is geladen. Een kale statische server
(zoals `python -m http.server`) probeert een pad als `/occasions/` eerst
als echte map/bestand te openen; omdat die map niet bestaat, geeft de
server zelf al een 404 terug voordat de browser ooit de HTML — en dus de
router — te zien krijgt.

Wat deze server doet
---------------------
- Een aanvraag die overeenkomt met een écht bestand (afbeeldingen, .js,
  .json, alles in /assets/, /uploads/, enz.) wordt gewoon normaal
  geserveerd, met het juiste content-type.
- Een aanvraag die met GEEN enkel bestand overeenkomt (dus elke "virtuele"
  route zoals /occasions/, /merken/herder/, /machine/<slug>/, …, en ook /
  zelf) krijgt de inhoud van "Wim van Breda.dc.html" terug — met
  HTTP-status 200, zónder redirect. De browser-URL in de adresbalk
  verandert dus niet: de client-side router leest die URL bij het laden
  en toont de juiste pagina.
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
SPA_FILE = os.path.join(ROOT, "Wim van Breda.dc.html")

# mimetypes-tabel op sommige systemen/Python-versies onvolledig voor deze
# extensies — expliciet aanvullen zodat content-types altijd klopt.
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("image/svg+xml", ".svg")


class SpaFallbackHandler(http.server.SimpleHTTPRequestHandler):
    """Serveert echte bestanden normaal; valt voor al het overige terug op
    Wim van Breda.dc.html (SPA-fallback), met bescherming tegen directory
    traversal."""

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

    def _serve_spa(self, head_only):
        if not os.path.isfile(SPA_FILE):
            self.send_error(404, "Wim van Breda.dc.html niet gevonden in " + ROOT)
            return
        try:
            with open(SPA_FILE, "rb") as f:
                body = f.read()
        except OSError as exc:
            self.send_error(500, "Kan Wim van Breda.dc.html niet lezen: " + str(exc))
            return
        self.send_response(200)
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
        if os.path.isfile(safe_path):
            # Bestaat als echt bestand: normaal laten serveren (juiste
            # content-type, Content-Length, 304-afhandeling, enz.).
            if head_only:
                super().do_HEAD()
            else:
                super().do_GET()
            return
        # Geen overeenkomend bestand: SPA-fallback. Géén redirect — de
        # browser-URL blijft precies wat de gebruiker heeft geopend.
        self._serve_spa(head_only)

    def do_GET(self):
        self._handle(head_only=False)

    def do_HEAD(self):
        self._handle(head_only=True)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main():
    if not os.path.isfile(SPA_FILE):
        sys.exit('Kan "Wim van Breda.dc.html" niet vinden in ' + ROOT)

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

    print("Wim van Breda — lokale server met SPA-fallback")
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
