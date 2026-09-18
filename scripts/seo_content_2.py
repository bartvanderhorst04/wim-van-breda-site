# -*- coding: utf-8 -*-
"""Inhoud cluster 2: klepelmaaier (8 pagina's, uitgebreide versie)."""
from build_seo_pages import h2, h3, p, ul, a
from machine_data import card

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None, machines=None, cta=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related,
                       fact=fact, machines=machines, cta=cta))

# ===========================================================================
add(
    "/klepelmaaier/",
    "Klepelmaaier kopen: professionele klepelmaaiers | Wim van Breda",
    "Professionele klepelmaaier voor berm, ruw terrein en dijkonderhoud. Omarv, Votex en GreenTec, advies en service uit Geldermalsen.",
    "Klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", None)],
    "Een klepelmaaier is een aftakas- of hydraulisch aangedreven maaier met los scharnierende klepelmessen op een draaiende rotor, die gras, onkruid en dunne opslag fijn verkleind achterlaat. Wim van Breda levert klepelmaaiers van Omarv, Votex en GreenTec voor berm-, terrein- en dijkonderhoud, aan loonbedrijven, gemeenten, waterschappen en aannemers.",
    fact="Een klepelmaaier verkleint gras, onkruid en dunne opslag met los scharnierende messen op een draaiende rotor. Omdat de messen bij een obstakel zoals een steen of paal opzij kunnen wijken en verend terugklappen, is een klepelmaaier robuuster in ruig, oneffen terrein dan een klassieke cirkelmaaier met vaste messen.",
    sections=[
        h2("Waarvoor wordt een klepelmaaier gebruikt?",
           ul([
               "Bermen en middenbermen langs wegen",
               "Ruig, oneffen of steenachtig terrein",
               "Dijken en taluds",
               "Terreinen met dunne houtopslag naast gras",
               "Regulier en ecologisch bermbeheer",
           ])),
        h2("Uitvoeringen: front, achter en zijmaaier",
           p("Klepelmaaiers zijn er als vaste of klapbare frontmaaier, als getrokken of opgebouwde achtermaaier, en als zijmaaier of maaiarm-aanbouwdeel voor bermen en taluds. De keuze hangt af van het type werk: een frontmaaier geeft goed zicht op het werktuig, een zijmaaier of klepelarm is de gangbare keuze voor werk langs de kant van de weg.")),
        h2("Welke klepelmaaier past bij uw situatie?",
           ul([
               "Werkbreedte — afgestemd op het te maaien oppervlak en de beschikbare tractorbreedte",
               "Aandrijving — aftakas voor grotere machines, hydraulisch voor compactere toepassingen",
               "Terrein — vlak grasland vraagt iets anders dan ruig, steenachtig bermterrein",
               "Type opslag — dun gras vraagt een lichtere uitvoering dan houtachtige begroeiing",
               "Tractorvermogen — bepaalt welke werkbreedte en rotorzwaarte mogelijk zijn",
           ])),
        h2("Omarv, Votex en GreenTec: de merken die Wim van Breda levert",
           p(a("Omarv","/klepelmaaier/omarv/")+" (Italië) bouwt een breed programma klepelmaaiers van compact tot zwaar, zoals de "+a("Torino","/machine/omarv-torino-klepelmaaier/")+" voor tractoren van 70 tot 140 pk met een uitworp boven de looprol. "+a("Votex","/klepelmaaier/votex/")+" (Nederland) is het bekende merk achter vrijwel elke gemeentetractor, met onder meer de "+a("RoadFlex","/machine/votex-roadflex-klepelmaaier/")+" die zowel als vlakmaaier als zijklepelmaaier werkt. "+a("GreenTec","/klepelmaaier/greentec/")+" levert klepelkoppen als onderdeel van het modulaire maaiarmsysteem.")),
        h2("Service en onderhoud",
           p("Wim van Breda levert klepelmaaiers inclusief montage en houdt onderdelen op voorraad in de eigen werkplaats in Geldermalsen, zodat onderhoud en reparatie snel kunnen plaatsvinden.")),
    ],
    machines=("Voorbeelden van klepelmaaiers bij Wim van Breda", [
        card("omarv-torino-klepelmaaier"),
        card("votex-roadflex-klepelmaaier"),
    ]),
    faq=[
        ("Wat is een klepelmaaier?",
         "Een klepelmaaier is een maaier met los scharnierende klepelmessen op een draaiende rotor, die gras, onkruid en dunne opslag verkleint. De messen kunnen bij een obstakel opzij wijken, wat de machine robuust maakt in ruig terrein."),
        ("Wat is het verschil tussen een klepelmaaier en een cirkelmaaier?",
         "Een klepelmaaier verkleint gras en dunne opslag met los scharnierende klepels en is robuuster tegen obstakels; een cirkelmaaier maait met vaste messen en geeft doorgaans een strakkere snede in schoon gras, maar is gevoeliger voor stenen en obstakels."),
        ("Is een klepelmaaier geschikt voor ruw terrein?",
         "Ja, dat is een van de sterke punten: dankzij de scharnierende messen kunnen klepelmaaiers goed overweg met oneffen, ruig of steenachtig terrein. Zie ook "+a("klepelmaaier voor ruw terrein","/klepelmaaier/ruw-terrein/")+"."),
        ("Welke tractor heb ik nodig voor een klepelmaaier?",
         "Dat hangt af van de werkbreedte: een bredere klepelmaaier vraagt meer aftakasvermogen. Zie "+a("klepelmaaier voor tractor","/klepelmaaier/voor-tractor/")+"."),
        ("Welke merken klepelmaaiers levert Wim van Breda?",
         "Omarv, Votex en GreenTec, elk met een eigen programma en sterke punten."),
        ("Waar kan ik advies krijgen over een klepelmaaier?",
         "Neem contact op met Wim van Breda in Geldermalsen voor advies op basis van uw tractor en terrein."),
    ],
    related=[("Klepelmaaier kopen","/klepelmaaier/kopen/"),("Klepelmaaier voor tractor","/klepelmaaier/voor-tractor/"),
             ("Klepelmaaier bij bermonderhoud","/klepelmaaier/bermonderhoud/"),("Maaiarm","/maaiarm/"),("Ecologisch maaien","/ecologisch-maaien/")],
)

# ===========================================================================
add(
    "/klepelmaaier/kopen/",
    "Klepelmaaier kopen voor professioneel gebruik | Wim van Breda",
    "Klepelmaaier kopen bij Wim van Breda: advies over werkbreedte, aandrijving en uitvoering, passend bij uw tractor en terrein.",
    "Klepelmaaier kopen",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Klepelmaaier kopen", None)],
    "Bij de keuze van een klepelmaaier bepalen werkbreedte, aandrijving (aftakas of hydraulisch) en montagewijze (front, achter of zijkant) samen welk model bij uw werk past. Wim van Breda adviseert op basis van tractor, terrein en beheerdoel en levert klepelmaaiers van Omarv, Votex en GreenTec.",
    fact="De belangrijkste keuzes bij aanschaf zijn: de werkbreedte in verhouding tot het tractorvermogen, de aandrijving (aftakas voor grotere machines, hydraulisch voor compactere toepassingen), en de montagewijze — front, achter of als zijmaaier.",
    sections=[
        h2("Waar u op let",
           ul([
               "Werkbreedte — afgestemd op het te maaien oppervlak en de beschikbare tractorbreedte",
               "Aandrijving — aftakas voor grotere machines, hydraulisch voor compactere of op afstand bediende toepassingen",
               "Montage — front-, achter- of zijmaaier, of als klepelkop op een maaiarm",
               "Terrein — vlak grasland vraagt iets anders dan ruig, steenachtig bermterrein",
               "Type opslag — dun gras versus houtachtige begroeiing bepaalt de benodigde rotorzwaarte",
           ])),
        h2("Nieuw of gebruikt?",
           p("Wim van Breda levert primair nieuwe klepelmaaiers. Voor gebruikt materieel verwijzen wij naar het occasion-aanbod op de website.")),
        h2("Welke merken kunt u kopen",
           p(a("Omarv","/klepelmaaier/omarv/")+" bouwt een breed programma van compact tot zwaar, zoals de "+a("Torino","/machine/omarv-torino-klepelmaaier/")+" voor tractoren van 70 tot 140 pk. "+a("Votex","/klepelmaaier/votex/")+" levert onder meer de "+a("RoadFlex","/machine/votex-roadflex-klepelmaaier/")+", die zowel als vlakmaaier als zijklepelmaaier werkt dankzij een sideshift van bijna 250 cm. "+a("GreenTec","/klepelmaaier/greentec/")+" levert klepelkoppen als onderdeel van het modulaire maaiarmsysteem.")),
        h2("Wat een aankoop bij Wim van Breda inhoudt",
           p("Bij aankoop hoort montage op uw tractor en uitleg over de bediening. Onderdelen worden op voorraad gehouden in de eigen werkplaats in Geldermalsen.")),
    ],
    machines=("Voorbeelden van te koop staande klepelmaaiers", [
        card("omarv-torino-klepelmaaier"),
        card("votex-roadflex-klepelmaaier"),
    ]),
    faq=[
        ("Wat kost een klepelmaaier?",
         "De prijs hangt af van werkbreedte, merk en uitvoering. Neem contact op voor een offerte op maat."),
        ("Wat is het verschil tussen Omarv en Votex klepelmaaiers?",
         "Omarv (Italië) bouwt een breed programma van compact tot zwaar; Votex (Nederland) is vooral bekend van bermmaaiers achter gemeentetractoren, met modellen als de RoadFlex die zowel vlak als zijwaarts kunnen maaien."),
        ("Levert Wim van Breda ook gebruikte klepelmaaiers?",
         "Het accent ligt op nieuwe machines; voor gebruikt materieel verwijzen wij naar het occasion-aanbod."),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier voor tractor","/klepelmaaier/voor-tractor/"),("Klepelmaaier ruw terrein","/klepelmaaier/ruw-terrein/")],
)

# ===========================================================================
add(
    "/klepelmaaier/voor-tractor/",
    "Klepelmaaier voor tractor | Wim van Breda",
    "Klepelmaaier gemonteerd op tractor: front-, achter- of zijmaaier, aangedreven via aftakas of hydrauliek.",
    "Klepelmaaier voor tractor",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Voor tractor", None)],
    "De meeste klepelmaaiers worden op een landbouw- of gemeentetractor gemonteerd en via de aftakas aangedreven, al bestaan er ook hydraulisch aangedreven uitvoeringen voor compactere machines. De werkbreedte van de maaier moet passen bij het vermogen en de hydraulische capaciteit van de tractor.",
    fact="De werkbreedte van een klepelmaaier moet in verhouding staan tot het aftakasvermogen van de tractor: een bredere maaier vraagt meer vermogen om het maaisel goed te verwerken. De meeste klepelmaaiers voor tractoren van 70 tot 140 pk, zoals de Omarv Torino, zijn leverbaar in meerdere werkbreedtes zodat ze op uiteenlopende tractoren passen.",
    sections=[
        h2("Werkbreedte en tractorvermogen",
           p("Een voorbeeld: de "+a("Omarv Torino","/machine/omarv-torino-klepelmaaier/")+" is leverbaar in 6 werkbreedtes van 160 tot 260 cm, voor tractoren van 70 tot 140 pk — hoe breder de maaier, hoe meer vermogen nodig is om de rotor op snelheid te houden.")),
        h2("Front, achter of zijkant",
           p("Frontmontage geeft goed zicht op het werktuig, achtermontage is gangbaar bij getrokken maaiers, en een zijmaaier of klepelarm is de gebruikelijke keuze voor bermwerk langs de kant van de weg. De "+a("Votex RoadFlex","/machine/votex-roadflex-klepelmaaier/")+" is een voorbeeld van een maaier die dankzij een sideshift van bijna 250 cm zowel vlak achter de trekker als volledig zijwaarts kan maaien.")),
        h2("Advies over de juiste combinatie",
           p("Wim van Breda beoordeelt per situatie welke werkbreedte en aandrijving passen bij uw tractor en terrein.")),
    ],
    faq=[
        ("Hoeveel pk heb ik nodig voor een klepelmaaier?",
         "Dat hangt af van de werkbreedte: smallere maaiers (rond 160 cm) zijn al mogelijk vanaf circa 70 pk, bredere uitvoeringen (tot 260 cm) vragen tot 140 pk of meer."),
        ("Kan een klepelmaaier zowel vlak als zijwaarts maaien?",
         "Sommige modellen wel, zoals de Votex RoadFlex met een sideshift van bijna 250 cm die zowel als vlakmaaier als zijklepelmaaier werkt."),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier kopen","/klepelmaaier/kopen/"),("Werktuigdrager","/werktuigdrager/")],
)

# ===========================================================================
add(
    "/klepelmaaier/bermonderhoud/",
    "Klepelmaaier bij bermonderhoud | Wim van Breda",
    "Klepelmaaier inzetten voor bermonderhoud: robuust tegen obstakels, fijn verkleind maaisel dat blijft liggen.",
    "Klepelmaaier voor bermonderhoud",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Bermonderhoud", None)],
    "In de berm is een klepelmaaier vaak de meest praktische keuze: de scharnierende messen verwerken gras, onkruid en dunne opslag tot fijn materiaal dat kan blijven liggen, zonder dat een steen of paal direct schade veroorzaakt. Dat maakt de klepelmaaier tot een van de meest gebruikte werktuigen in regulier bermonderhoud.",
    fact="Een klepelmaaier wordt bij bermonderhoud vooral ingezet op rechte, relatief vlakke trajecten, waar de scharnierende messen gras en dunne opslag in één werkgang verkleinen. Bij hoogteverschil, sloten of veel obstakels wordt de klepelkop vaak gemonteerd op een maaiarm voor meer bereik.",
    sections=[
        h2("Zijmaaier of maaiarm",
           p("Voor rechte bermtrajecten volstaat vaak een zijmaaier met klepelrotor; bij hoogteverschil, sloten of obstakels wordt de klepelkop gemonteerd op een "+a("maaiarm","/maaiarm/bermonderhoud/")+" voor meer bereik en flexibiliteit.")),
        h2("Welke klepelmaaier past bij bermwerk",
           p("Voor dagelijks, intensief bermwerk kiezen loonbedrijven en gemeenten vaak voor bedrijfszekere modellen zoals de "+a("Votex","/klepelmaaier/votex/")+"-maaiers, die bekendstaan als eenvoudig te onderhouden werkpaarden achter gemeentetractoren.")),
        h2("Service en onderhoud",
           p("Bermonderhoud is intensief seizoenswerk. Wim van Breda houdt onderdelen op voorraad en verzorgt onderhoud vanuit de eigen werkplaats in Geldermalsen.")),
    ],
    machines=("Relevante machines voor bermonderhoud", [
        card("votex-roadflex-klepelmaaier"),
        card("omarv-torino-klepelmaaier"),
    ]),
    faq=[
        ("Waarom een klepelmaaier voor bermonderhoud?",
         "Omdat de scharnierende messen gras en dunne opslag verkleinen en tegelijk robuust zijn tegen obstakels zoals stenen en palen, wat veel voorkomt in bermen."),
        ("Wanneer is een maaiarm beter dan een klepelmaaier voor bermwerk?",
         "Zodra er hoogteverschil, een sloot of veel obstakels in het traject zitten, geeft een maaiarm meer bereik en flexibiliteit dan een vaste zijmaaier."),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Bermonderhoud met klepelmaaier","/bermonderhoud/klepelmaaier/"),("Maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/")],
)

# ===========================================================================
add(
    "/klepelmaaier/ruw-terrein/",
    "Klepelmaaier voor ruw terrein | Wim van Breda",
    "Klepelmaaier voor ruw, oneffen en steenachtig terrein: robuuste rotor en scharnierende messen tegen obstakels.",
    "Klepelmaaier voor ruw terrein",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Ruw terrein", None)],
    "Op ruw, oneffen of steenachtig terrein is een klepelmaaier vaak duurzamer in gebruik dan een cirkelmaaier, omdat de klepelmessen bij een obstakel opzij kunnen wijken in plaats van vast te lopen of te breken. Dat maakt de klepelmaaier tot de gangbare keuze voor terreinen waar de ondergrond niet vlak of voorspelbaar is.",
    fact="Op ruw terrein — taluds, natuurterreinen, dijken, braakliggende percelen — is een robuuste klepelmaaier met een steviger rotor en dikkere messen nodig dan bij regulier grasonderhoud, omdat er vaker stenen, takken of houtachtige opslag in het maaipad liggen.",
    sections=[
        h2("Waar dit type terrein voorkomt",
           ul([
               "Taluds langs dijken en waterwegen",
               "Ruwe, onbewerkte bermen",
               "Natuurterreinen",
               "Braakliggende of verwaarloosde percelen",
           ])),
        h2("Zwaardere uitvoeringen voor ruw terrein",
           p("Voor intensief gebruik op ruw terrein bouwt "+a("Omarv","/klepelmaaier/omarv/")+" zwaardere klepelmaaiers met een steviger rotor en dikkere messen. Een voorbeeld is de "+a("Torino","/machine/omarv-torino-klepelmaaier/")+", die begroeiing tot circa 6 cm diameter aankan en dankzij de uitworp boven de looprol minder snel blokkeert bij extreem hoog gras of natte omstandigheden.")),
        h2("Wanneer een klepelmaaier de juiste keuze is",
           p("Een klepelmaaier is met name geschikt wanneer het terrein wisselend gras, onkruid en dunne houtopslag bevat, en wanneer obstakels zoals stenen of takken regelmatig voorkomen. Bij zwaardere, dikkere begroeiing of specifiek boomonderhoud is eerder een bosbouwmaaier of takkenschaar op zijn plaats.")),
    ],
    machines=("Relevante machine voor ruw terrein", [
        card("omarv-torino-klepelmaaier"),
    ]),
    faq=[
        ("Waarom is een klepelmaaier geschikt voor ruw terrein?",
         "Omdat de klepelmessen los scharnieren en bij een obstakel kunnen opzij wijken in plaats van vast te lopen of te breken, wat op oneffen of steenachtig terrein voorkomt."),
        ("Welke begroeiing kan een klepelmaaier voor ruw terrein aan?",
         "Afhankelijk van het model: zwaardere uitvoeringen zoals de Omarv Torino verwerken begroeiing tot circa 6 cm diameter."),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier omarv","/klepelmaaier/omarv/"),("Klepelmaaier voor tractor","/klepelmaaier/voor-tractor/")],
)

# ===========================================================================
add(
    "/klepelmaaier/omarv/",
    "Omarv klepelmaaier | Wim van Breda",
    "Omarv klepelmaaiers bij Wim van Breda: Italiaans merk met een breed programma voor terrein-, berm- en boomgaardonderhoud.",
    "Omarv klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Omarv", None)],
    "Omarv is een Italiaans merk dat een breed programma klepelmaaiers bouwt, van compacte modellen voor tuin- en parkonderhoud tot zware uitvoeringen voor intensief professioneel gebruik. Wim van Breda levert het Omarv-programma inclusief montage, onderdelen en service.",
    fact="Omarv bouwt klepelmaaiers voor uiteenlopend gebruik: van lichte modellen voor regulier grasonderhoud tot zware uitvoeringen voor ruig terrein, boomgaarden en wijngaarden. Ook maai-laadcombinaties zoals de Venezia horen bij het programma.",
    sections=[
        h2("Het Omarv-programma",
           p("Een voorbeeld uit het zwaardere segment is de "+a("Torino","/machine/omarv-torino-klepelmaaier/")+": een klepelmaaier voor tractoren van 70 tot 140 pk, met een verzwaarde rotoras en uitworp boven de looprol, leverbaar in 6 werkbreedtes van 160 tot 260 cm. Daarnaast levert Omarv maai-laadcombinaties zoals de "+a("Venezia L","/machine/omarv-venezia-l-professionele-maai-laad-combinatie/")+", die maaien, verkleinen en opvangen in één werkgang combineert en geschikt is voor tractoren van 90 tot 120 pk.")),
        h2("Voor wie Omarv relevant is",
           p("Omarv-machines worden bij Wim van Breda vooral geleverd aan loonbedrijven en aannemers die met één merk zowel licht als zwaar terreinonderhoud willen uitvoeren, inclusief specifieke toepassingen zoals boomgaard- en wijngaardonderhoud.")),
    ],
    machines=("Omarv-machines bij Wim van Breda", [
        card("omarv-torino-klepelmaaier"),
        card("omarv-venezia-l-professionele-maai-laad-combinatie"),
    ]),
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier voor ruw terrein","/klepelmaaier/ruw-terrein/"),
             ("Omarv (merkpagina)","/omarv/klepelmaaier/"),("Ecologisch maaien","/ecologisch-maaien/")],
)

# ===========================================================================
add(
    "/klepelmaaier/votex/",
    "Votex klepelmaaier | Wim van Breda",
    "Votex klepelmaaiers bij Wim van Breda: het bekende Nederlandse merk voor bermmaaiers achter gemeente- en loonbedrijftractoren.",
    "Votex klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Votex", None)],
    "Votex is een Nederlands merk dat klepelmaaiers bouwt die je terugvindt achter vrijwel elke gemeentetractor: eenvoudig in onderhoud, robuust in de berm en met een onderdelenvoorziening die jarenlang meegaat. Wim van Breda levert en onderhoudt het Votex-programma.",
    fact="Votex-maaiers staan bekend als bedrijfszekere werkpaarden voor dagelijks bermonderhoud. Een voorbeeld is de RoadFlex, die dankzij een sideshift van bijna 250 cm zowel als compacte vlakmaaier direct achter de trekker als volledig uitgeschoven zijklepelmaaier kan werken.",
    sections=[
        h2("De Votex RoadFlex",
           p("De "+a("RoadFlex","/machine/votex-roadflex-klepelmaaier/")+" combineert twee functies in één machine: als vlakmaaier blijft de maaibak dicht bij de trekker voor maximale stabiliteit in krappe ruimtes, en volledig uitgeschoven werkt hij als zijklepelmaaier voor bermen en taluds. Een hydraulisch veersysteem in de driepuntsbok zorgt voor trillingsreductie, botsbeveiliging bij obstakels en meer transportcomfort.")),
        h2("Onderdelen en service",
           p("Wim van Breda houdt Votex-onderdelen op voorraad en verzorgt onderhoud en reparatie vanuit de eigen werkplaats in Geldermalsen, zodat machines die dagelijks worden ingezet niet onnodig lang stilstaan.")),
    ],
    machines=("Votex-machine bij Wim van Breda", [
        card("votex-roadflex-klepelmaaier"),
    ]),
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier bij bermonderhoud","/klepelmaaier/bermonderhoud/"),
             ("Maaiarm","/maaiarm/"),("Votex (merkpagina)","/votex/klepelmaaier/")],
)

# ===========================================================================
add(
    "/klepelmaaier/greentec/",
    "GreenTec klepelmaaier | Wim van Breda",
    "GreenTec klepelkoppen bij Wim van Breda: onderdeel van het modulaire maaiarmsysteem voor berm- en terreinonderhoud.",
    "GreenTec klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("GreenTec", None)],
    "Bij GreenTec is de klepelkop een van de verwisselbare werktuigen binnen het modulaire maaiarmsysteem: dezelfde draagarm die met een takkenschaar snoeit, kan zonder gereedschap wisselen naar een klepelkop om te maaien. Wim van Breda levert dit GreenTec-programma als onderdeel van de maaiarmen.",
    fact="Anders dan een losse klepelmaaier is de GreenTec-klepelkop een aanbouwdeel op een modulaire maaiarm: dezelfde arm wisselt zonder gereedschap tussen klepelkop, takkenschaar en andere werktuigen, wat hem geschikt maakt voor beheerders die met één machine meerdere taken willen uitvoeren.",
    sections=[
        h2("Klepelkop op een maaiarm",
           p("Dat maakt GreenTec een logische keuze voor wie met één "+a("maaiarm","/maaiarm/greentec/")+" zowel wil maaien als snoeien, in plaats van twee losse machines aan te schaffen. Modellen als de "+a("Scorpion 430 S","/machine/greentec-scorpion-430-s-basisfront-maaiarm/")+" en de "+a("Scorpion 830 Plus","/machine/greentec-scorpion-830-plus-maaiarm/")+" zijn hier voorbeelden van, met een horizontaal bereik van respectievelijk 4,3 en 8,3 meter.")),
    ],
    machines=("GreenTec-maaiarmen met klepelkop", [
        card("greentec-scorpion-430-s-basisfront-maaiarm"),
        card("greentec-scorpion-830-plus-maaiarm"),
    ]),
    related=[("Klepelmaaier","/klepelmaaier/"),("GreenTec maaiarmen","/maaiarm/greentec/"),("Bermonderhoud","/bermonderhoud/"),
             ("GreenTec (merkpagina)","/greentec/klepelmaaier/")],
)
