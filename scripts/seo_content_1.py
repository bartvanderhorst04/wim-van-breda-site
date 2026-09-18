# -*- coding: utf-8 -*-
"""Inhoud cluster 1-3: maaiarm, klepelmaaier, maaikorf."""
from build_seo_pages import h2, h3, p, ul, a

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related, fact=fact))

# ===========================================================================
# 1. MAAIARM
# ===========================================================================
add(
    "/maaiarm/",
    "Maaiarm kopen: professionele maaiarmen | Wim van Breda",
    "Professionele maaiarm voor berm-, sloot- en terreinonderhoud. Merken als Herder en GreenTec, advies op maat en service vanuit Geldermalsen.",
    "Maaiarm",
    [("Home", HOME), ("Maaiarm", None)],
    "Een maaiarm is een hydraulisch aangedreven, uitschuifbare arm die op een tractor of werktuigdrager wordt gemonteerd om bermen, taluds, sloten en hagen te maaien of te snoeien op plekken waar een gewone maaier niet bij kan.",
    sections=[
        h2("Wat is een maaiarm en waarvoor wordt hij gebruikt",
           p("De arm wordt vanuit de cabine bediend en kan zijwaarts, omhoog en over hindernissen heen werken. Aan het uiteinde zit een verwisselbaar werktuig: een klepelkop voor gras en dun hout, een messenbalk voor nette bermranden, een takkenschaar voor snoeiwerk of een maaikorf voor maaisel dat uit het water moet blijven. Zo is één machine inzetbaar voor meerdere onderhoudstaken door het seizoen heen.")),
        h2("Welke maaiarmen Wim van Breda levert",
           p("Wim van Breda levert maaiarmen van "+a("Herder","/herder/maaiarm/")+", een Nederlands merk met ruim 75 jaar ervaring in berm- en dijkonderhoud, en van "+a("GreenTec","/greentec/maaiarm/")+", bekend om het modulaire systeem waarbij één draagarm zonder gereedschap van werktuig wisselt. Beide merken bouwen machines in uiteenlopende armlengtes en gewichtsklassen, passend bij tractoren vanaf circa 3.000 kg tot zware uitvoeringen voor grootschalig beheer.")),
        h2("Voor wie",
           p("Maaiarmen worden vooral ingezet door loonbedrijven, aannemers in groen- en grondverzet, waterschappen en gemeenten die bermen, sloten, dijken en taluds moeten onderhouden volgens een vast beheerschema.")),
    ],
    faq=[
        ("Wat kost een maaiarm?",
         "De prijs hangt sterk af van armlengte, merk en het gewicht van de tractor waarop de arm gemonteerd wordt. Neem contact op voor een offerte op maat."),
        ("Welke tractor heb ik nodig voor een maaiarm?",
         "Dat verschilt per model: compacte maaiarmen zijn al te combineren met tractoren vanaf circa 3.000 kg, zwaardere uitvoeringen vragen een tractor van 7.000 kg of meer. Zie ook onze pagina over "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+"."),
    ],
    related=[("Maaiarm kopen","/maaiarm/kopen/"),("Maaiarm voor tractor","/maaiarm/voor-tractor/"),
             ("Bermonderhoud","/bermonderhoud/"),("Slootonderhoud","/slootonderhoud/"),
             ("Klepelmaaier","/klepelmaaier/"),("Maaikorf","/maaikorf/")],
)

add(
    "/maaiarm/kopen/",
    "Maaiarm kopen | Wim van Breda",
    "Maaiarm kopen bij Wim van Breda: advies over merk, armlengte en werktuig, passend bij uw tractor en toepassing. Levering en service uit Geldermalsen.",
    "Maaiarm kopen",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Maaiarm kopen", None)],
    "Bij aanschaf van een maaiarm bepalen drie zaken samen welk model past: het gewicht en vermogen van uw tractor, de gewenste armlengte en reikwijdte, en het werktuig dat u vooral gaat gebruiken.",
    sections=[
        h2("Waar u op let bij aankoop",
           ul([
               "Tractorgewicht en hydraulische capaciteit — bepaalt welke armklasse mogelijk is.",
               "Armlengte en horizontaal bereik — hoe ver moet de arm bij taluds of over water kunnen reiken.",
               "Werktuig — klepelkop, messenbalk, takkenschaar of maaikorf, afhankelijk van het onderhoudstype.",
               "Bediening — moderne armen zijn elektrohydraulisch en proportioneel te besturen vanuit de cabine.",
           ])),
        h2("Advies en service",
           p("Wim van Breda adviseert op basis van uw tractor en het beheerwerk dat u uitvoert, en levert "+a("Herder","/maaiarm/herder/")+"- en "+a("GreenTec","/maaiarm/greentec/")+"-maaiarmen inclusief montage, onderdelen en service vanuit de eigen werkplaats in Geldermalsen.")),
    ],
    related=[("Maaiarm","/maaiarm/"),("Maaiarm voor tractor","/maaiarm/voor-tractor/"),
             ("Maaiarm bermonderhoud","/maaiarm/bermonderhoud/"),("Maaiarm slootonderhoud","/maaiarm/slootonderhoud/")],
)

add(
    "/maaiarm/voor-tractor/",
    "Maaiarm voor tractor | Wim van Breda",
    "Maaiarm gemonteerd op tractor voor berm-, sloot- en taludonderhoud. Advies over de juiste armklasse bij uw tractorgewicht.",
    "Maaiarm voor tractor",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Voor tractor", None)],
    "De meeste maaiarmen worden op een landbouwtractor gemonteerd, via de drie-punts hefinrichting aan de voor- of achterzijde, en aangedreven door de hydrauliek en aftakas van de tractor.",
    sections=[
        h2("Welke tractor past bij welke maaiarm",
           p("Lichtere, compacte maaiarmen zijn al te combineren met tractoren vanaf circa 3.000 kg; middenklasse-armen vragen doorgaans 5.000 tot 7.000 kg, en de zwaarste uitvoeringen met het grootste bereik zijn bedoeld voor tractoren vanaf 7.000 à 8.000 kg. Naast gewicht spelen ook hydraulische capaciteit (oliedebiet) en de beschikbare frontmontage een rol.")),
        h2("Front of achter monteren",
           p("Een maaiarm kan vooraan (voor goed zicht op het werktuig) of achteraan de tractor gemonteerd worden; welke opstelling het beste past, hangt af van het type werk en de voorkeur van de bestuurder.")),
    ],
    related=[("Maaiarm","/maaiarm/"),("Maaiarm kopen","/maaiarm/kopen/"),("Werktuigdrager","/werktuigdrager/")],
)

add(
    "/maaiarm/bermonderhoud/",
    "Maaiarm voor bermonderhoud | Wim van Breda",
    "Maaiarm inzetten voor professioneel bermonderhoud: bereik over taluds en obstakels heen, met klepelkop of messenbalk.",
    "Maaiarm voor bermonderhoud",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Bermonderhoud", None)],
    "In bermonderhoud is de maaiarm het werktuig bij uitstek zodra er hoogteverschil, een sloot of obstakels als verkeersborden en bomen in het maaitraject zitten.",
    sections=[
        h2("Waarom een maaiarm in de berm",
           p("Anders dan een vaste maaier kan de arm zijwaarts uitschuiven, over een talud naar beneden werken en om obstakels heen sturen, zonder dat de bestuurder de tractor hoeft te verplaatsen. Met een klepelkop wordt gras en opslag verkleind achtergelaten; met een messenbalk ontstaat een net, kort gemaaide bermrand.")),
        h2("Merken voor bermwerk",
           p("Zowel "+a("Herder","/maaiarm/herder/")+" als "+a("GreenTec","/maaiarm/greentec/")+" bouwen maaiarmen die specifiek voor intensief bermbeheer worden ingezet door loonbedrijven en gemeenten.")),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Bermonderhoud met maaiarm","/bermonderhoud/maaiarm/"),
             ("Klepelmaaier voor bermonderhoud","/klepelmaaier/bermonderhoud/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/")],
)

add(
    "/maaiarm/slootonderhoud/",
    "Maaiarm voor slootonderhoud | Wim van Breda",
    "Maaiarm voor het maaien en schonen van sloten en watergangen, met maaikorf voor opvang van maaisel uit het water.",
    "Maaiarm voor slootonderhoud",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Slootonderhoud", None)],
    "Bij slootonderhoud maait de maaiarm het talud en de waterlijn, vaak in combinatie met een maaikorf die het maaisel direct uit het water opvangt in plaats van het te laten liggen.",
    sections=[
        h2("Talud en waterlijn in één werkgang",
           p("De arm reikt vanaf de kant tot in de sloot, zodat het onderhoud in één keer vanaf de berm kan gebeuren zonder de oever te betreden. Dat is zowel efficiënter als minder belastend voor de bodem.")),
        h2("Combinatie met maaikorf",
           p("Voor watergangen waar maaisel niet in het water mag achterblijven, wordt de klepelkop vervangen door een "+a("maaikorf","/maaikorf/voor-maaiarm/")+" die het gemaaide materiaal direct meeneemt.")),
    ],
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaiarm voor slootonderhoud","/slootonderhoud/maaiarm/"),
             ("Maaikorf voor watergangen","/maaikorf/voor-watergangen/"),("Maaikorf slootonderhoud","/maaikorf/slootonderhoud/")],
)

add(
    "/maaiarm/herder/",
    "Herder maaiarm | Wim van Breda",
    "Herder maaiarmen bij Wim van Breda: Nederlands merk met ruim 75 jaar ervaring in berm-, dijk- en slootonderhoud.",
    "Herder maaiarm",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Herder", None)],
    "Herder is een Nederlands merk dat al ruim 75 jaar maaiarmen, maaikorven en dijkenmaaiers bouwt voor waterschappen, gemeenten en aannemers.",
    sections=[
        h2("Herder-maaiarmen bij Wim van Breda",
           p("Een voorbeeld uit het programma is de "+a("Herder Grenadier maaiarm","/")+", een veelzijdige arm voor zwaar bermbeheer die met diverse aanbouwwerktuigen uitgerust kan worden en een armlengte heeft van 6,40 tot 8,80 meter. Herder bouwt zowel deze zwaardere modellen als compactere uitvoeringen voor kleinere tractoren.")),
        h2("Ook maaikorven van Herder",
           p("Naast maaiarmen levert Herder ook "+a("maaikorven","/maaikorf/herder/")+", vaak gecombineerd ingezet bij sloot- en watergangonderhoud.")),
    ],
    related=[("Maaiarm","/maaiarm/"),("Herder maaikorf","/maaikorf/herder/"),("Maaiarm voor bermonderhoud","/maaiarm/bermonderhoud/")],
)

add(
    "/maaiarm/greentec/",
    "GreenTec maaiarm | Wim van Breda",
    "GreenTec maaiarmen bij Wim van Breda: Deens merk met modulair systeem — één draagarm, meerdere werktuigen zonder gereedschap wisselen.",
    "GreenTec maaiarm",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("GreenTec", None)],
    "GreenTec is een Deens merk dat bekendstaat om zijn modulaire maaiarmsysteem: één draagarm waarop zonder gereedschap gewisseld kan worden tussen klepelkop, takkenschaar en andere werktuigen.",
    sections=[
        h2("Modulair systeem",
           p("Dat maakt een GreenTec-arm geschikt voor meerdere taken door het seizoen: maaien in het voorjaar en de zomer, snoeien en takken verwijderen in het najaar, met dezelfde basisarm.")),
        h2("Scorpion-serie",
           p("De Scorpion-serie is het bekendste voorbeeld: compacte uitvoeringen voor tractoren vanaf circa 3.000 kg tot zware modellen met een horizontaal bereik van 7 à 8,3 meter voor grootschalig beheer.")),
    ],
    related=[("Maaiarm","/maaiarm/"),("GreenTec klepelmaaier","/klepelmaaier/greentec/"),("Maaiarm voor bermonderhoud","/maaiarm/bermonderhoud/")],
)

# ===========================================================================
# 2. KLEPELMAAIER
# ===========================================================================
add(
    "/klepelmaaier/",
    "Klepelmaaier kopen: professionele klepelmaaiers | Wim van Breda",
    "Professionele klepelmaaier voor berm, ruw terrein en dijkonderhoud. Merken als Omarv, Votex en GreenTec, advies en service uit Geldermalsen.",
    "Klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", None)],
    "Een klepelmaaier is een aftakas- of hydraulisch aangedreven maaier met los scharnierende klepelmessen op een draaiende rotor, die gras, onkruid en dunne opslag fijn verkleint achterlaat.",
    sections=[
        h2("Wat een klepelmaaier doet",
           p("Doordat de messen los scharnieren, kunnen ze bij een obstakel (steen, paal) opzij wijken en verend terugklappen, wat een klepelmaaier robuuster maakt dan een klassieke cirkelmaaier in ruig, oneffen terrein. Het resultaat is fijn verkleind maaisel dat blijft liggen, zonder dat het hoeft te worden afgevoerd.")),
        h2("Uitvoeringen: front, achter en zijmaaier",
           p("Klepelmaaiers zijn er als vaste of klapbare frontmaaier, als getrokken/opgebouwde achtermaaier, en als zijmaaier of maaiarm-aanbouwdeel voor bermen en taluds.")),
        h2("Merken die Wim van Breda levert",
           p(a("Omarv","/klepelmaaier/omarv/")+" (Italië) bouwt een breed programma klepelmaaiers van compact tot zwaar; "+a("Votex","/klepelmaaier/votex/")+" (Nederland) is het bekende merk achter vrijwel elke gemeentetractor; "+a("GreenTec","/klepelmaaier/greentec/")+" levert klepelkoppen als onderdeel van het modulaire maaiarmsysteem.")),
    ],
    faq=[
        ("Wat is het verschil tussen een klepelmaaier en een cirkelmaaier?",
         "Een klepelmaaier verkleint gras en dunne opslag met los scharnierende klepels en is robuuster tegen obstakels; een cirkelmaaier maait met vaste messen en geeft doorgaans een strakkere snede in schoon gras, maar is gevoeliger voor stenen en obstakels."),
        ("Is een klepelmaaier geschikt voor ruw terrein?",
         "Ja, dat is een van de sterke punten: dankzij de scharnierende messen kunnen klepelmaaiers goed overweg met oneffen, ruig of steenachtig terrein. Zie ook onze pagina over "+a("klepelmaaier voor ruw terrein","/klepelmaaier/ruw-terrein/")+"."),
    ],
    related=[("Klepelmaaier kopen","/klepelmaaier/kopen/"),("Klepelmaaier voor tractor","/klepelmaaier/voor-tractor/"),
             ("Klepelmaaier bermonderhoud","/klepelmaaier/bermonderhoud/"),("Maaiarm","/maaiarm/"),("Ecologisch maaien","/ecologisch-maaien/")],
)

add(
    "/klepelmaaier/kopen/",
    "Klepelmaaier kopen | Wim van Breda",
    "Klepelmaaier kopen bij Wim van Breda: advies over werkbreedte, aandrijving en uitvoering, passend bij uw tractor en terrein.",
    "Klepelmaaier kopen",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Klepelmaaier kopen", None)],
    "Bij de keuze van een klepelmaaier bepalen werkbreedte, aandrijving (aftakas of hydraulisch) en montagewijze (front, achter of zijkant) samen welk model bij uw werk past.",
    sections=[
        h2("Waar u op let",
           ul([
               "Werkbreedte — afgestemd op het te maaien oppervlak en de beschikbare tractorbreedte.",
               "Aandrijving — aftakas voor grotere machines, hydraulisch voor compactere of op afstand bediende toepassingen.",
               "Montage — front-, achter- of zijmaaier, of als klepelkop op een maaiarm.",
               "Terrein — vlak grasland vraagt iets anders dan ruig, steenachtig bermterrein.",
           ])),
        h2("Advies bij Wim van Breda",
           p("Wim van Breda adviseert op basis van tractor, terrein en beheerdoel, en levert "+a("Omarv","/klepelmaaier/omarv/")+"-, "+a("Votex","/klepelmaaier/votex/")+"- en "+a("GreenTec","/klepelmaaier/greentec/")+"-klepelmaaiers inclusief onderdelen en service uit Geldermalsen.")),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier voor tractor","/klepelmaaier/voor-tractor/"),("Klepelmaaier ruw terrein","/klepelmaaier/ruw-terrein/")],
)

add(
    "/klepelmaaier/voor-tractor/",
    "Klepelmaaier voor tractor | Wim van Breda",
    "Klepelmaaier gemonteerd op tractor: front-, achter- of zijmaaier, aangedreven via aftakas of hydrauliek.",
    "Klepelmaaier voor tractor",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Voor tractor", None)],
    "De meeste klepelmaaiers worden op een landbouw- of gemeentetractor gemonteerd en via de aftakas aangedreven, al bestaan er ook hydraulisch aangedreven uitvoeringen voor compactere machines.",
    sections=[
        h2("Werkbreedte en tractorvermogen",
           p("De werkbreedte van de maaier moet passen bij het vermogen en de hydraulische capaciteit van de tractor: een bredere klepelmaaier vraagt meer aftakasvermogen om het maaisel goed te verwerken.")),
        h2("Front, achter of zijkant",
           p("Frontmontage geeft goed zicht op het werktuig, achtermontage is gangbaar bij getrokken maaiers, en een zijmaaier of klepelarm is de gebruikelijke keuze voor bermwerk langs de kant van de weg.")),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier kopen","/klepelmaaier/kopen/"),("Werktuigdrager","/werktuigdrager/")],
)

add(
    "/klepelmaaier/bermonderhoud/",
    "Klepelmaaier voor bermonderhoud | Wim van Breda",
    "Klepelmaaier inzetten voor bermonderhoud: robuust tegen obstakels, fijn verkleind maaisel dat blijft liggen.",
    "Klepelmaaier voor bermonderhoud",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Bermonderhoud", None)],
    "In de berm is een klepelmaaier vaak de meest praktische keuze: de scharnierende messen verwerken gras, onkruid en dunne opslag tot fijn materiaal dat kan blijven liggen, zonder dat een steen of paal direct schade veroorzaakt.",
    sections=[
        h2("Zijmaaier of maaiarm",
           p("Voor rechte bermtrajecten volstaat vaak een zijmaaier met klepelrotor; bij hoogteverschil, sloten of obstakels wordt de klepelkop gemonteerd op een "+a("maaiarm","/maaiarm/bermonderhoud/")+" voor meer bereik en flexibiliteit.")),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Bermonderhoud met klepelmaaier","/bermonderhoud/klepelmaaier/"),("Maaiarm voor bermonderhoud","/maaiarm/bermonderhoud/")],
)

add(
    "/klepelmaaier/ruw-terrein/",
    "Klepelmaaier voor ruw terrein | Wim van Breda",
    "Klepelmaaier voor ruw, oneffen en steenachtig terrein: robuuste rotor en scharnierende messen tegen obstakels.",
    "Klepelmaaier voor ruw terrein",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Ruw terrein", None)],
    "Op ruw, oneffen of steenachtig terrein is een klepelmaaier vaak duurzamer in gebruik dan een cirkelmaaier, omdat de klepelmessen bij een obstakel opzij kunnen wijken in plaats van vast te lopen of te breken.",
    sections=[
        h2("Waar dit type terrein voorkomt",
           p("Denk aan taluds, ruwe bermen, natuurterreinen, dijken en braakliggende percelen — plekken waar de ondergrond niet vlak is en waar stenen, takken of opslag in het maaipad kunnen liggen.")),
        h2("Zwaardere uitvoeringen",
           p("Voor intensief gebruik op ruw terrein bouwt "+a("Omarv","/klepelmaaier/omarv/")+" zwaardere klepelmaaiers met een steviger rotor en dikkere messen, geschikt voor grovere opslag dan een lichte grasmaaier aankan.")),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier omarv","/klepelmaaier/omarv/"),("Ruwterreinmaaiers","/")],
)

add(
    "/klepelmaaier/omarv/",
    "Omarv klepelmaaier | Wim van Breda",
    "Omarv klepelmaaiers bij Wim van Breda: Italiaans merk met een breed programma voor terrein-, berm- en boomgaardonderhoud.",
    "Omarv klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Omarv", None)],
    "Omarv is een Italiaans merk dat een breed programma klepelmaaiers bouwt, van compacte modellen voor tuin- en parkonderhoud tot zware uitvoeringen voor intensief professioneel gebruik.",
    sections=[
        h2("Programma",
           p("Het assortiment loopt uiteen van klepelmaaiers voor regulier grasonderhoud tot zwaardere modellen voor ruig terrein, boomgaarden en wijngaarden. Ook maai-laadcombinaties zoals de Omarv Venezia horen bij het programma: deze verkleinen en zuigen maaisel en snoeimateriaal in één werkgang op, met een opvangbak tot 10 m³.")),
        h2("Voor wie",
           p("Omarv-machines worden bij Wim van Breda vooral geleverd aan loonbedrijven en aannemers die met één merk zowel licht als zwaar terreinonderhoud willen uitvoeren.")),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier voor ruw terrein","/klepelmaaier/ruw-terrein/"),("Klepelmaaier voor tractor","/klepelmaaier/voor-tractor/")],
)

add(
    "/klepelmaaier/votex/",
    "Votex klepelmaaier | Wim van Breda",
    "Votex klepelmaaiers bij Wim van Breda: het bekende Nederlandse merk voor bermmaaiers achter gemeente- en loonbedrijftractoren.",
    "Votex klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("Votex", None)],
    "Votex is een Nederlands merk dat klepelmaaiers bouwt die je terugvindt achter vrijwel elke gemeentetractor: eenvoudig in onderhoud, robuust in de berm en met een onderdelenvoorziening die jarenlang meegaat.",
    sections=[
        h2("Bekend en bewezen",
           p("Votex-maaiers staan bekend als bedrijfszekere werkpaarden voor dagelijks bermonderhoud, met een eenvoudige, goed te onderhouden constructie.")),
        h2("Onderdelen en service",
           p("Wim van Breda houdt Votex-onderdelen op voorraad en verzorgt onderhoud en reparatie vanuit de eigen werkplaats in Geldermalsen.")),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier bermonderhoud","/klepelmaaier/bermonderhoud/"),("Maaiarm","/maaiarm/")],
)

add(
    "/klepelmaaier/greentec/",
    "GreenTec klepelmaaier | Wim van Breda",
    "GreenTec klepelkoppen bij Wim van Breda: onderdeel van het modulaire maaiarmsysteem voor berm- en terreinonderhoud.",
    "GreenTec klepelmaaier",
    [("Home", HOME), ("Klepelmaaier", "/klepelmaaier/"), ("GreenTec", None)],
    "Bij GreenTec is de klepelkop een van de verwisselbare werktuigen binnen het modulaire maaiarmsysteem: dezelfde draagarm die met een takkenschaar snoeit, kan zonder gereedschap wisselen naar een klepelkop om te maaien.",
    sections=[
        h2("Klepelkop op een maaiarm",
           p("Dat maakt GreenTec een logische keuze voor wie met één "+a("maaiarm","/maaiarm/greentec/")+" zowel wil maaien als snoeien, in plaats van twee losse machines aan te schaffen.")),
    ],
    related=[("Klepelmaaier","/klepelmaaier/"),("GreenTec maaiarm","/maaiarm/greentec/"),("Bermonderhoud","/bermonderhoud/")],
)
