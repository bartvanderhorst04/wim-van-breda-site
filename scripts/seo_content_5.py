# -*- coding: utf-8 -*-
"""Inhoud cluster 6-9: tuin-en-parkmachines, werktuigdrager, merk×product, regio."""
from build_seo_pages import h2, h3, p, ul, a

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related, fact=fact))

# ===========================================================================
# 6. TUIN- EN PARKMACHINES
# ===========================================================================
add(
    "/tuin-en-parkmachines/",
    "Tuin- en parkmachines | Wim van Breda",
    "Professionele tuin- en parkmachines voor gemeenten en aannemers: maaimachines en handgereedschap voor terreinonderhoud.",
    "Tuin- en parkmachines",
    [("Home", HOME), ("Tuin- en parkmachines", None)],
    "Tuin- en parkmachines zijn de machines en het handgereedschap waarmee openbaar groen, parken en terreinen onderhouden worden: van maaimachines tot kettingzagen en bosmaaiers.",
    sections=[
        h2("Wat hieronder valt",
           p("Denk aan cirkelmaaiers en veegmachines voor gazons en verharding, en professioneel handgereedschap zoals kettingzagen, bosmaaiers en heggenscharen voor kleiner onderhoudswerk.")),
        h2("Merken",
           p("Wim van Breda levert onder meer AS-Motor (maaimachines voor hoog gras en steil terrein), Kersten (veegmachines) en Stihl (handgereedschap en accutechniek) voor tuin- en parkonderhoud.")),
        h2("Voor wie",
           p("Vooral gemeenten, hoveniers en aannemers die openbaar groen, parken en bedrijfsterreinen onderhouden.")),
    ],
    faq=[
        ("Wat zijn tuin- en parkmachines precies?",
         "De verzamelnaam voor machines en gereedschap voor onderhoud van openbaar groen en terreinen: van maai- en veegmachines tot handgereedschap zoals kettingzagen en bosmaaiers."),
    ],
    related=[("Tuin- en parkmachines kopen","/tuin-en-parkmachines/kopen/"),("Professionele tuin- en parkmachines","/tuin-en-parkmachines/professioneel/"),
             ("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/"),("Machines voor aannemers","/tuin-en-parkmachines/aannemers/"),
             ("Terreinonderhoud","/tuin-en-parkmachines/terreinonderhoud/")],
)

add(
    "/tuin-en-parkmachines/kopen/",
    "Tuin- en parkmachines kopen | Wim van Breda",
    "Tuin- en parkmachines kopen bij Wim van Breda: advies over de juiste machine voor uw terrein en toepassing.",
    "Tuin- en parkmachines kopen",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Kopen", None)],
    "Bij de aanschaf van tuin- en parkmachines is het terrein waarop gewerkt wordt (gazon, ruw terrein, verharding) leidend voor de keuze van het type machine.",
    sections=[
        h2("Advies bij Wim van Breda",
           p("Wim van Breda adviseert over de juiste combinatie van maaimachines, veegtechniek en handgereedschap, en levert alles inclusief onderhoud en onderdelen vanuit Geldermalsen.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Professionele tuin- en parkmachines","/tuin-en-parkmachines/professioneel/")],
)

add(
    "/tuin-en-parkmachines/professioneel/",
    "Professionele tuin- en parkmachines | Wim van Breda",
    "Professionele tuin- en parkmachines voor dagelijks, intensief gebruik door gemeenten en aannemers.",
    "Professionele tuin- en parkmachines",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Professioneel", None)],
    "Professionele tuin- en parkmachines zijn gebouwd voor dagelijks, intensief gebruik, in tegenstelling tot consumentenmachines die voor incidenteel gebruik bedoeld zijn.",
    sections=[
        h2("Het verschil",
           p("Professionele machines hebben zwaardere motoren, robuustere onderdelen en een onderhoudsprogramma dat is afgestemd op continu gebruik door meerdere medewerkers.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/")],
)

add(
    "/tuin-en-parkmachines/gemeenten/",
    "Machines voor gemeenten | Wim van Breda",
    "Tuin- en parkmachines voor gemeenten: onderhoud van openbaar groen, parken en bermen door de eigen buitendienst.",
    "Machines voor gemeenten",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Gemeenten", None)],
    "Gemeenten gebruiken tuin- en parkmachines voor het onderhoud van openbaar groen, parken, bermen en sportvelden door de eigen buitendienst.",
    sections=[
        h2("Breed inzetbaar programma",
           p("Van maaimachines voor gazons tot klepelmaaiers voor bermen — Wim van Breda levert het programma dat past bij het beheerschema van de gemeente, inclusief onderdelen en service.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Bermonderhoud","/bermonderhoud/"),("Machines voor aannemers","/tuin-en-parkmachines/aannemers/")],
)

add(
    "/tuin-en-parkmachines/aannemers/",
    "Machines voor aannemers | Wim van Breda",
    "Tuin- en parkmachines voor aannemers in groenvoorziening en terreinonderhoud, inclusief service en onderdelen.",
    "Machines voor aannemers",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Aannemers", None)],
    "Aannemers in groenvoorziening en terreinonderhoud gebruiken tuin- en parkmachines voor uiteenlopende opdrachten, van kleine tuinen tot grote bedrijfsterreinen.",
    sections=[
        h2("Snel weer aan het werk",
           p("Wim van Breda houdt onderdelen op voorraad en biedt vervangend materieel, zodat een aannemer bij storing snel weer verder kan.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/"),("Terreinonderhoud","/tuin-en-parkmachines/terreinonderhoud/")],
)

add(
    "/tuin-en-parkmachines/terreinonderhoud/",
    "Machines voor terreinonderhoud | Wim van Breda",
    "Tuin- en parkmachines voor terreinonderhoud: van maaien tot vegen en onkruidbestrijding op bedrijfsterreinen en verharding.",
    "Machines voor terreinonderhoud",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Terreinonderhoud", None)],
    "Terreinonderhoud gaat verder dan alleen maaien: ook vegen van verharding en chemievrije onkruidbestrijding horen erbij.",
    sections=[
        h2("Compleet programma",
           p("Naast maaimachines levert Wim van Breda veegmachines en infraroodtechniek voor onkruidbestrijding, geschikt voor bedrijfsterreinen, parkeerplaatsen en verharding.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/")],
)

# ===========================================================================
# 7. WERKTUIGDRAGER
# ===========================================================================
add(
    "/werktuigdrager/",
    "Werktuigdrager | Wim van Breda",
    "Professionele werktuigdrager voor berm-, sloot- en terreinonderhoud: compact platform voor meerdere aanbouwwerktuigen.",
    "Werktuigdrager",
    [("Home", HOME), ("Werktuigdrager", None)],
    "Een werktuigdrager is een compact, wendbaar voertuig dat speciaal is ontworpen om met verschillende aanbouwwerktuigen te werken, in plaats van een tractor met één vaste functie.",
    sections=[
        h2("Waarom een werktuigdrager",
           p("Waar een gewone tractor vooral geschikt is voor trekkracht, is een werktuigdrager gebouwd rond het snel wisselen van werktuigen: maaikop, veegborstel, sneeuwschuif of laadschop, vaak zonder de bestuurdersplek te hoeven verlaten.")),
        h2("Elektrisch en op afstand bestuurd",
           p("Een voorbeeld is de Raymo Torpedo werktuigdrager: een volledig elektrische, radiografisch bestuurbare werktuigdrager voor stil en emissievrij groen- en terreinonderhoud, ontwikkeld door het Nederlandse merk Raymo. Ook compacte werktuigdragers van LM Trac en Reform horen bij het programma van Wim van Breda.")),
    ],
    faq=[
        ("Wat is het verschil tussen een werktuigdrager en een tractor?",
         "Een tractor is vooral gebouwd om trekkracht te leveren, een werktuigdrager is specifiek ontworpen om snel te wisselen tussen uiteenlopende aanbouwwerktuigen, vaak in een compacter en wendbaarder chassis."),
    ],
    related=[("Werktuigdrager kopen","/werktuigdrager/kopen/"),("Professionele werktuigdrager","/werktuigdrager/professioneel/"),
             ("Werktuigdrager bermonderhoud","/werktuigdrager/bermonderhoud/"),("Werktuigdrager slootonderhoud","/werktuigdrager/slootonderhoud/")],
)

add(
    "/werktuigdrager/kopen/",
    "Werktuigdrager kopen | Wim van Breda",
    "Werktuigdrager kopen bij Wim van Breda: advies over het juiste model voor uw werktuigen en toepassing.",
    "Werktuigdrager kopen",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Kopen", None)],
    "Bij de keuze van een werktuigdrager is het bepalend welke werktuigen u wilt combineren en of stil, emissievrij werken een vereiste is.",
    sections=[
        h2("Advies bij Wim van Breda",
           p("Wim van Breda adviseert over de juiste werktuigdrager en levert onder meer elektrische en radiografisch bestuurbare modellen, inclusief onderdelen en service uit Geldermalsen.")),
    ],
    related=[("Werktuigdrager","/werktuigdrager/"),("Professionele werktuigdrager","/werktuigdrager/professioneel/")],
)

add(
    "/werktuigdrager/professioneel/",
    "Professionele werktuigdrager | Wim van Breda",
    "Professionele werktuigdrager voor dagelijks, intensief gebruik door aannemers, gemeenten en waterschappen.",
    "Professionele werktuigdrager",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Professioneel", None)],
    "Een professionele werktuigdrager is gebouwd voor dagelijks gebruik: robuust, goed te onderhouden en met een snel wisselsysteem voor werktuigen.",
    sections=[
        h2("Voor gemeenten, waterschappen en aannemers",
           p("Deze machines worden ingezet voor uiteenlopend beheerwerk waarbij één platform meerdere taken moet kunnen uitvoeren.")),
    ],
    related=[("Werktuigdrager","/werktuigdrager/"),("Werktuigdrager kopen","/werktuigdrager/kopen/")],
)

add(
    "/werktuigdrager/bermonderhoud/",
    "Werktuigdrager voor bermonderhoud | Wim van Breda",
    "Werktuigdrager inzetten voor bermonderhoud: compact platform voor gevarieerd bermwerk met meerdere werktuigen.",
    "Werktuigdrager voor bermonderhoud",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Bermonderhoud", None)],
    "Voor gevarieerd bermwerk op kleinere schaal is een werktuigdrager praktisch: één compact platform waarop verschillende werktuigen gemonteerd kunnen worden.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg over bermonderhoud: "+a("bermonderhoud","/bermonderhoud/")+".")),
    ],
    related=[("Werktuigdrager","/werktuigdrager/"),("Bermonderhoud","/bermonderhoud/"),("Machines voor bermonderhoud","/bermonderhoud/machines/")],
)

add(
    "/werktuigdrager/slootonderhoud/",
    "Werktuigdrager voor slootonderhoud | Wim van Breda",
    "Werktuigdrager inzetten voor slootonderhoud: compact en wendbaar platform voor werk langs de waterkant.",
    "Werktuigdrager voor slootonderhoud",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Slootonderhoud", None)],
    "Langs smalle watergangen is een compacte, wendbare werktuigdrager soms praktischer dan een grote tractor met maaiarm.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg over slootonderhoud: "+a("slootonderhoud","/slootonderhoud/")+".")),
    ],
    related=[("Werktuigdrager","/werktuigdrager/"),("Slootonderhoud","/slootonderhoud/"),("Machines voor slootonderhoud","/slootonderhoud/machines/")],
)

# ===========================================================================
# 8. MERK × PRODUCT
# ===========================================================================
add(
    "/herder/maaiarm/",
    "Herder maaiarmen | Wim van Breda",
    "Overzicht van de Herder-maaiarmen die Wim van Breda levert, met een link naar het volledige modellenoverzicht.",
    "Herder maaiarmen",
    [("Home", HOME), ("Herder", "/herder/maaiarm/"), ("Maaiarm", None)],
    "Herder bouwt al ruim 75 jaar maaiarmen voor berm-, dijk- en slootonderhoud, met modellen van compact tot zwaar, zoals de Herder Grenadier maaiarm met een armlengte van 6,40 tot 8,80 meter.",
    sections=[
        h2("Meer over Herder-maaiarmen",
           p("Zie onze uitgebreide pagina over "+a("Herder maaiarm","/maaiarm/herder/")+" voor modellen, armlengtes en toepassingen.")),
    ],
    related=[("Herder maaiarm (detail)","/maaiarm/herder/"),("Herder maaikorven","/herder/maaikorf/"),("Maaiarm","/maaiarm/")],
)

add(
    "/herder/maaikorf/",
    "Herder maaikorven | Wim van Breda",
    "Overzicht van de Herder-maaikorven die Wim van Breda levert, met een link naar de volledige uitleg.",
    "Herder maaikorven",
    [("Home", HOME), ("Herder", "/herder/maaiarm/"), ("Maaikorf", None)],
    "Herder levert naast maaiarmen ook maaikorven, als aanbouwdeel voor sloot- en watergangonderhoud waarbij maaisel direct opgevangen wordt.",
    sections=[
        h2("Meer over Herder-maaikorven",
           p("Zie onze uitgebreide pagina over "+a("Herder maaikorf","/maaikorf/herder/")+".")),
    ],
    related=[("Herder maaikorf (detail)","/maaikorf/herder/"),("Herder maaiarmen","/herder/maaiarm/"),("Maaikorf","/maaikorf/")],
)

add(
    "/greentec/maaiarm/",
    "GreenTec maaiarmen | Wim van Breda",
    "GreenTec maaiarmen bij Wim van Breda: Deens merk met modulair systeem — één draagarm, meerdere werktuigen.",
    "GreenTec maaiarmen",
    [("Home", HOME), ("GreenTec", "/greentec/maaiarm/"), ("Maaiarm", None)],
    "GreenTec bouwt maaiarmen volgens een modulair systeem: één draagarm waarop zonder gereedschap gewisseld kan worden tussen klepelkop, takkenschaar en andere werktuigen.",
    sections=[
        h2("Meer over GreenTec-maaiarmen",
           p("Zie onze uitgebreide pagina over "+a("GreenTec maaiarm","/maaiarm/greentec/")+" voor de Scorpion-serie en andere modellen.")),
    ],
    related=[("GreenTec maaiarm (detail)","/maaiarm/greentec/"),("GreenTec klepelmaaiers","/greentec/klepelmaaier/"),("Maaiarm","/maaiarm/")],
)

add(
    "/greentec/klepelmaaier/",
    "GreenTec klepelmaaiers | Wim van Breda",
    "Overzicht van de GreenTec-klepelkoppen die Wim van Breda levert, met een link naar de volledige uitleg.",
    "GreenTec klepelmaaiers",
    [("Home", HOME), ("GreenTec", "/greentec/maaiarm/"), ("Klepelmaaier", None)],
    "Binnen het modulaire GreenTec-systeem is de klepelkop een van de werktuigen die op dezelfde draagarm gemonteerd kan worden als de takkenschaar.",
    sections=[
        h2("Meer over GreenTec-klepelmaaiers",
           p("Zie onze uitgebreide pagina over "+a("GreenTec klepelmaaier","/klepelmaaier/greentec/")+".")),
    ],
    related=[("GreenTec klepelmaaier (detail)","/klepelmaaier/greentec/"),("GreenTec maaiarmen","/greentec/maaiarm/"),("Klepelmaaier","/klepelmaaier/")],
)

add(
    "/omarv/klepelmaaier/",
    "Omarv klepelmaaiers | Wim van Breda",
    "Overzicht van de Omarv-klepelmaaiers die Wim van Breda levert, met een link naar het volledige modellenoverzicht.",
    "Omarv klepelmaaiers",
    [("Home", HOME), ("Omarv", "/omarv/klepelmaaier/"), ("Klepelmaaier", None)],
    "Omarv bouwt een breed programma klepelmaaiers, van compacte modellen voor tuin- en parkonderhoud tot zware uitvoeringen voor intensief professioneel gebruik.",
    sections=[
        h2("Meer over Omarv-klepelmaaiers",
           p("Zie onze uitgebreide pagina over "+a("Omarv klepelmaaier","/klepelmaaier/omarv/")+".")),
    ],
    related=[("Omarv klepelmaaier (detail)","/klepelmaaier/omarv/"),("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier voor ruw terrein","/klepelmaaier/ruw-terrein/")],
)

add(
    "/votex/klepelmaaier/",
    "Votex klepelmaaiers | Wim van Breda",
    "Votex klepelmaaiers bij Wim van Breda: het bekende Nederlandse merk voor bermmaaiers achter gemeentetractoren.",
    "Votex klepelmaaiers",
    [("Home", HOME), ("Votex", "/votex/klepelmaaier/"), ("Klepelmaaier", None)],
    "Votex is het merk achter vrijwel elke gemeentetractor: eenvoudig in onderhoud, robuust in de berm, met een onderdelenvoorziening die jarenlang meegaat.",
    sections=[
        h2("Meer over Votex-klepelmaaiers",
           p("Zie onze uitgebreide pagina over "+a("Votex klepelmaaier","/klepelmaaier/votex/")+".")),
    ],
    related=[("Votex klepelmaaier (detail)","/klepelmaaier/votex/"),("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier voor bermonderhoud","/klepelmaaier/bermonderhoud/")],
)

# ===========================================================================
# 9. REGIO
# ===========================================================================
add(
    "/regio/geldermalsen/",
    "Machines voor groenbeheer in Geldermalsen | Wim van Breda",
    "Wim van Breda is gevestigd in Geldermalsen: machines, advies en service voor groen-, berm- en terreinbeheer vanuit onze eigen werkplaats.",
    "Wim van Breda in Geldermalsen",
    [("Home", HOME), ("Regio", None), ("Geldermalsen", None)],
    "Wim van Breda is gevestigd aan de Oudenhof 14 in Geldermalsen, waar sinds 1957 machines voor groen-, berm- en terreinbeheer worden geleverd, onderhouden en verhuurd.",
    sections=[
        h2("Wat wij vanuit Geldermalsen doen",
           p("Vanuit onze vestiging leveren we "+a("maaiarmen","/maaiarm/")+", "+a("klepelmaaiers","/klepelmaaier/")+", "+a("werktuigdragers","/werktuigdrager/")+" en "+a("tuin- en parkmachines","/tuin-en-parkmachines/")+" aan loonbedrijven, aannemers, gemeenten en waterschappen. Onze eigen werkplaats verzorgt onderhoud, reparatie en onderdelen, met vervangend materieel wanneer dat nodig is.")),
        h2("Bermen, sloten en terreinen in de regio",
           p("Klanten in en rond Geldermalsen gebruiken onze machines voor "+a("bermonderhoud","/bermonderhoud/")+" en "+a("slootonderhoud","/slootonderhoud/")+" langs de vele wegen en watergangen die de Betuwe kenmerken.")),
    ],
    related=[("Betuwe","/regio/betuwe/"),("Rivierenland","/regio/rivierenland/"),("Zaltbommel","/regio/zaltbommel/"),("Service","/")],
)

add(
    "/regio/betuwe/",
    "Machines voor groenbeheer in de Betuwe | Wim van Breda",
    "Wim van Breda levert en onderhoudt machines voor groen-, berm- en terreinbeheer in de Betuwe, vanuit de eigen vestiging in Geldermalsen.",
    "Wim van Breda in de Betuwe",
    [("Home", HOME), ("Regio", None), ("Betuwe", None)],
    "Wim van Breda is gevestigd in Geldermalsen, in het hart van de Betuwe, en levert vanuit deze vestiging machines en service aan bedrijven en overheden in de regio.",
    sections=[
        h2("Fruitteelt, landbouw en waterbeheer",
           p("De Betuwe kent veel fruitteelt, landbouw en een dicht netwerk van kaden, dijken en watergangen — werk waarvoor "+a("maaiarmen","/maaiarm/")+", "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("maaikorven","/maaikorf/")+" veel worden ingezet.")),
        h2("Levering en service",
           p("Loonbedrijven en aannemers in de Betuwe kunnen bij Wim van Breda terecht voor advies, onderhoud en onderdelen vanuit de eigen werkplaats in Geldermalsen.")),
    ],
    related=[("Geldermalsen","/regio/geldermalsen/"),("Rivierenland","/regio/rivierenland/"),("Zaltbommel","/regio/zaltbommel/")],
)

add(
    "/regio/rivierenland/",
    "Machines voor groenbeheer in Rivierenland | Wim van Breda",
    "Wim van Breda levert machines voor groen-, berm- en slootbeheer in Rivierenland, vanuit de eigen vestiging in Geldermalsen.",
    "Wim van Breda in Rivierenland",
    [("Home", HOME), ("Regio", None), ("Rivierenland", None)],
    "Rivierenland, de regio tussen Waal en Linge waarin Geldermalsen ligt, kent veel watergangen, dijken en landelijk gebied dat professioneel onderhoud vraagt.",
    sections=[
        h2("Waterschappen en aannemers",
           p("Waterschappen en aannemers in Rivierenland gebruiken onze "+a("maaiarmen","/maaiarm/")+" en "+a("maaikorven","/maaikorf/")+" voor "+a("slootonderhoud","/slootonderhoud/")+" en dijkbeheer.")),
        h2("Vanuit Geldermalsen",
           p("Wim van Breda levert en onderhoudt deze machines vanuit de eigen werkplaats in Geldermalsen, centraal in de regio.")),
    ],
    related=[("Geldermalsen","/regio/geldermalsen/"),("Betuwe","/regio/betuwe/"),("Zaltbommel","/regio/zaltbommel/")],
)

add(
    "/regio/zaltbommel/",
    "Machines voor groenbeheer in Zaltbommel | Wim van Breda",
    "Wim van Breda levert machines voor groen-, berm- en terreinbeheer in Zaltbommel en de Bommelerwaard, vanuit Geldermalsen.",
    "Wim van Breda in Zaltbommel",
    [("Home", HOME), ("Regio", None), ("Zaltbommel", None)],
    "Zaltbommel en de Bommelerwaard liggen op korte afstand van onze vestiging in Geldermalsen, aan de andere kant van de Waal.",
    sections=[
        h2("Dijken en landelijk gebied",
           p("De Bommelerwaard kent, net als de Betuwe, veel dijken, sloten en agrarisch gebied — werk waarvoor "+a("maaiarmen","/maaiarm/")+", "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("werktuigdragers","/werktuigdrager/")+" worden ingezet.")),
        h2("Levering en service",
           p("Ook klanten in Zaltbommel en omgeving kunnen bij Wim van Breda terecht voor advies, onderhoud en onderdelen vanuit Geldermalsen.")),
    ],
    related=[("Geldermalsen","/regio/geldermalsen/"),("Rivierenland","/regio/rivierenland/"),("Betuwe","/regio/betuwe/")],
)
