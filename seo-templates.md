# SEO-templates per paginatype — Wim van Breda

Deze templates beschrijven de logica die momenteel al werkt in
`Wim van Breda.dc.html` (`Component.meta()` / `Component.applyJsonLd()`) en
die bij de migratie naar WordPress moet worden overgenomen (als PHP-template-
logica, ACF-velden met fallback, of een SEO-plugin-integratie). Ze zijn
richtlijnen: unieke, afwijkende pagina's mogen altijd een betere handmatige
title/description krijgen.

Alle titels eindigen op ` | Wim van Breda`, **behalve** wanneer de volledige
titel + suffix langer dan 60 tekens zou worden — dan vervalt de suffix in
plaats van dat de eigenlijke naam wordt ingekort of verzonnen content wordt
toegevoegd (`capTitle()`).

Meta descriptions worden nooit halverwege een zin afgekapt: bij een te lange
description wordt geknipt op het laatste zin-einde (". ") vóór ~162 tekens;
is er geen goed knippunt, dan blijft de tekst liever iets langer dan 175
tekens dan dat er een afgebroken zin of verzonnen inkorting ontstaat
(`capDescription()`).

---

## MACHINE (`/machines/<slug>/`, ook `/machine/<slug>/` — zie opmerking onderaan)

- **H1**: `{merk} {naam}` (merk wordt niet herhaald als de naam al met het
  merk begint)
- **SEO title**: `{weergavenaam}` + ` | Wim van Breda` (dus bv.
  `GreenTec Tiger 725 cirkelmaaier | Wim van Breda`)
- **Meta description**: de bestaande korte productomschrijving (`kort`) als
  die er is; anders `{weergavenaam} — {type, lowercase}.` als fallback.
  Altijd gevolgd door "Bekijk specificaties en toepassingen bij Wim van
  Breda in Geldermalsen."
- **Canonical**: de eigen, unieke detail-URL van de machine
- **OG**: og:title/og:description = seo title/meta description; og:image =
  eerste foto uit de fotogalerij (indien aanwezig)
- **Schema**: `Product` (naam, description, url, brand, category/model
  indien aanwezig — **geen** prijs/voorraad/reviews, die staan niet in de
  brondata) + `BreadcrumbList` (Home → Nieuwe machines → machine, uitsluitend
  bestaande routes)
- **Duplicate-preventie**: twee machines met identieke `kort`-tekst krijgen
  automatisch de eigen naam als voorvoegsel (`DUP_KORTS`)

## OCCASION (`/occasions/<slug>/`, ook `/occasion/<slug>/` — zie opmerking)

Zelfde opbouw als machine, met twee toevoegingen:

- **SEO title**: `{weergavenaam} occasion | Wim van Breda` — **"occasion"
  wordt nooit toegevoegd als de naam daar al op eindigt** (voorkomt
  "... occasion occasion"), zie `occasionTitleBase()`
- **Duplicate-preventie**: twee occasions met exact dezelfde titel (zelfde
  model, twee losse eenheden op voorraad) krijgen een onderscheidend kenmerk
  tussen haakjes toegevoegd — uitsluitend als er een écht verschillende,
  bestaande spec is (bouwjaar, serienummer, afscherming, urenstand of
  voorraadnummer, in die volgorde). Bestaat dat verschil niet, dan blijft de
  titel ongewijzigd (nooit verzonnen).

## MERK (`/merken/<id>/`)

- **H1**: `{merknaam}`
- **SEO title**: `{merknaam} machines | Wim van Breda`
- **Meta description**: "Bekijk het {merk}-programma bij Wim van Breda:
  {bestaande merk-intro}. Advies, onderdelen en service uit Geldermalsen."
- **Canonical**: eigen merk-URL
- **Schema**: geen los Product/Brand-schema; alleen de sitebrede
  `Organization`

## VERHUUR-CATEGORIE (`/verhuur/<slug>/`)

- **H1**: categorienaam (bv. "Maaimachines")
- **SEO title**: `{categorienaam} huren | Wim van Breda`
- **Meta description**: bestaande categorie-intro + "Bekijk het
  verhuuraanbod bij Wim van Breda in Geldermalsen."
- Let op: de slug in de URL wijkt bij één categorie af van het interne id
  (`aanbouwwerktuigen` → `/verhuur/aanbouwwerktuigen-maaiarmen-kranen/`) —
  dit is bewust een beschrijvendere URL, geen open route-mismatch.

## NIEUWS-ARTIKEL (`/nieuws/<slug>/`)

- **H1**: `{titel}`
- **SEO title**: `{titel} | Wim van Breda` (of kale titel als de suffix de
  60 tekens zou overschrijden)
- **Meta description**: bestaande `intro`, ingekort volgens de standaard
  regel; incidenteel een expliciete `metaDescription`-override op het
  record zelf wanneer twee vergelijkbare artikelen (bv. jaarlijks
  terugkerende beursaankondigingen) anders tot een identieke, afgekapte
  description zouden leiden — zie `groene-sector-2023`/`groene-sector-2024`
  in de brondata voor een voorbeeld.
- **Schema**: `Article` (aanbevolen bij migratie; nu nog niet als los
  JSON-LD-blok aanwezig — zie eindrapport)

## MAGAZINE (`/magazines/<slug>/`)

- **H1**: `{editie}`
- **SEO title**: `{editie} ({jaar}) | Wim van Breda`
- **Meta description**: bestaande samenvattingstekst van de editie

## VACATURE (`/werken-bij/<id>/`)

- **H1**: `{v.titel}` **inclusief** het woord "Vacature" ervoor (bv.
  "Vacature technisch support en garantie") — dit is de tekst zoals hij
  letterlijk op de pagina staat, bewust ongewijzigd.
- **SEO title / og:title**: `Component.capFirst({functietitel zonder
  "Vacature "}) | Wim van Breda` — het voorvoegsel wordt alléén voor de
  metadata weggelaten (niet voor de zichtbare H1), met een hoofdletter aan
  het begin (`capFirst()`) zodat de title niet met een kleine letter begint.
- **Meta description**: bestaande korte functieomschrijving (`kort`) +
  "Solliciteer direct bij Wim van Breda in Geldermalsen."
- **Schema (`applyJsonLd()`)**: `JobPosting` — title (zie boven, zónder
  "Vacature "), description (`v.intro`), `datePosted`, `hiringOrganization`
  (naam/website/logo van Wim van Breda), `jobLocation` (bestaand
  vestigingsadres Oudenhof 14, Geldermalsen). **Uitsluitend** aanwezig
  wanneer het record een echte `v.datePosted` heeft — die datum is per
  vacature **handmatig één keer opgehaald van de live productiesite**
  (`wimvanbreda.nl`, Yoast SEO's `datePublished` in de JSON-LD van de
  betreffende vacaturepagina — nadrukkelijk niet `dateModified`), zie de
  toelichting bij elk record in `Component.VACANCIES` in de HTML-bron en het
  eindrapport van deze taak voor de brontabel. Geen `validThrough` (Wim van
  Breda sluit vacatures zelf af) en geen `employmentType` (staat niet
  expliciet in de vacaturetekst). **Nooit** op "Open sollicitatie" — dat is
  geen specifieke functie.
- **Bij migratie**: geef elke vacature in WordPress een eigen, echt
  publicatiedatumveld (het WP `post_date` van het custom post type volstaat
  al) zodat `datePosted` automatisch meekomt zonder handmatig onderhoud.

## VASTE PAGINA'S (Home, Machines-overzicht, Occasions-overzicht,
Verhuur-overzicht, Service, Merken-overzicht, Nieuws-overzicht,
Werken bij-overzicht, Geleverd, Magazines-overzicht, Over ons, Contact)

Handmatig geschreven, unieke title + description per pagina — geen
sjabloon nodig, er is er maar één van elk. Zie `seo-pages.csv`/`.json` voor
de exacte, huidige teksten.

---

## Belangrijke opmerking over dubbele detail-routes

De brondata gebruikt voor machines het enkelvoud `/machine/<slug>/` en voor
occasions `/occasion/<slug>/` als canonieke URL (`m.url`-veld), terwijl de
overzichtspagina's zelf op het meervoud draaien: `/machines/` en
`/occasions/`. Kies bij de WordPress-migratie **één** consistente vorm
(bij voorkeur het meervoud, gelijk aan de overzichtspagina) voor de
permalink-structuur van het custom post type, en laat de andere vorm
301-redirecten. Zie het eindrapport voor de volledige toelichting.
