# -*- coding: utf-8 -*-
"""Inhoud cluster 1: maaiarm (7 pagina's, uitgebreide versie)."""
from build_seo_pages import h2, h3, p, ul, a
from machine_data import card

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None, machines=None, cta=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related,
                       fact=fact, machines=machines, cta=cta))

# ===========================================================================
# 1. MAAIARM — hoofdpagina
# ===========================================================================
add(
    "/maaiarm/",
    "Maaiarm kopen: professionele maaiarmen | Wim van Breda",
    "Professionele maaiarm voor berm-, sloot- en terreinonderhoud. Herder en GreenTec maaiarmen, advies op maat en service vanuit Geldermalsen.",
    "Maaiarm",
    [("Home", HOME), ("Maaiarm", None)],
    "Een maaiarm is een hydraulisch aangedreven, uitschuifbare arm die op een tractor of werktuigdrager wordt gemonteerd om bermen, taluds, sloten en hagen te maaien of te snoeien op plekken waar een gewone maaier niet bij kan. Wim van Breda levert maaiarmen van Herder en GreenTec aan loonbedrijven, aannemers, gemeenten en waterschappen, en verzorgt montage, onderdelen en service vanuit de eigen werkplaats in Geldermalsen.",
    fact="Een maaiarm bestaat uit een hydraulische arm op een tractor of werktuigdrager, met aan het uiteinde een verwisselbaar werktuig — meestal een klepelkop, messenbalk, takkenschaar of maaikorf. De arm kan zijwaarts uitschuiven en over hoogteverschil werken, waardoor bermen, taluds en slootkanten vanaf de kant onderhouden kunnen worden zonder dat de bestuurder de tractor hoeft te verplaatsen.",
    sections=[
        h2("Waarvoor wordt een maaiarm gebruikt?",
           p("Een maaiarm wordt professioneel ingezet voor het maaien en snoeien van bermen, taluds, slootkanten, hagen en vegetatie rond obstakels zoals verkeersborden, vangrails en bomen. Doordat de arm vanuit de cabine wordt bediend en over hindernissen heen kan werken, blijft de tractor op de rijbaan of berm terwijl het werktuig het eigenlijke werk doet op plekken die anders lastig of onveilig te bereiken zouden zijn.") +
           ul([
               "Wegbermen en middenbermen",
               "Taluds langs dijken, kanalen en spoorlijnen",
               "Slootkanten en oevers",
               "Vegetatie rond obstakels: borden, palen, bomen",
               "Hagen en opgaande begroeiing langs perceelsranden",
           ])),
        h2("Welke werktuigen kunnen op een maaiarm?",
           p("Het uiteinde van een maaiarm is verwisselbaar, waardoor dezelfde arm voor meerdere taken bruikbaar is:")) +
           ul([
               "Klepelkop — verkleint gras, onkruid en dunne opslag; het materiaal blijft liggen",
               "Messenbalk — geeft een nette, korte snede voor bermranden",
               "Takkenschaar — voor het knippen van dikkere takken en opslag",
               "Maaikorf — maait en vangt maaisel tegelijk op, gebruikt bij sloten en watergangen",
           ]),
        h2("Herder en GreenTec: de twee merken die Wim van Breda levert",
           p("Wim van Breda levert maaiarmen van twee merken met een verschillende aanpak. "+a("Herder","/maaiarm/herder/")+" is een Nederlands merk met ruim 75 jaar ervaring in berm-, dijk- en slootonderhoud; de "+a("Herder Grenadier","/machine/herder-grenadier-maaiarm/")+" is daarvan een voorbeeld — een zware maaiarm met een armlengte van 6,40 tot 8,80 meter, uit te rusten met uiteenlopende werktuigen. "+a("GreenTec","/maaiarm/greentec/")+" is een Deens merk dat werkt met een modulair systeem: één draagarm waarop zonder gereedschap gewisseld kan worden tussen klepelkop en takkenschaar. GreenTec bouwt zowel compacte maaiarmen voor kleinere tractoren als zware uitvoeringen met een horizontaal bereik tot ruim 8 meter voor grootschalig beheer.")),
        h2("Welke maaiarm past bij uw situatie?",
           p("De keuze voor een maaiarm hangt af van een aantal praktische factoren:")) +
           ul([
               "Tractorgewicht en hydraulische capaciteit — bepaalt welke armklasse mogelijk is",
               "Gewenst bereik — hoe ver de arm bij een talud of over water moet reiken",
               "Type werk — regulier bermonderhoud, slootonderhoud of incidenteel snoeiwerk",
               "Werktuig — welk aanbouwdeel het meest gebruikt gaat worden",
               "Gebruiksintensiteit — dagelijkse inzet vraagt om een robuustere uitvoering dan incidenteel gebruik",
           ]) +
           p("Wim van Breda adviseert op basis van deze factoren welk model en welke armklasse passen bij uw tractor en werkzaamheden. Zie ook onze pagina's over "+a("maaiarm kopen","/maaiarm/kopen/")+" en "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+"."),
        h2("Service en onderhoud",
           p("Wim van Breda levert maaiarmen inclusief montage op de tractor, en houdt onderdelen op voorraad in de eigen werkplaats in Geldermalsen. Onderhoud en reparatie kunnen in de werkplaats of, waar dat praktisch is, op locatie plaatsvinden, zodat een machine niet onnodig lang stilstaat.")),
    ],
    machines=("Voorbeelden van maaiarmen bij Wim van Breda", [
        card("herder-grenadier-maaiarm"),
        card("greentec-scorpion-430-s-basisfront-maaiarm"),
        card("greentec-scorpion-830-plus-maaiarm"),
    ]),
    faq=[
        ("Wat is een maaiarm?",
         "Een maaiarm is een hydraulisch aangedreven, uitschuifbare arm op een tractor of werktuigdrager, met aan het uiteinde een verwisselbaar werktuig zoals een klepelkop, messenbalk, takkenschaar of maaikorf. De arm maakt het mogelijk om bermen, taluds en sloten te maaien op plekken die met een gewone maaier moeilijk bereikbaar zijn."),
        ("Waarvoor wordt een maaiarm gebruikt?",
         "Voor het maaien en snoeien van bermen, taluds, slootkanten, hagen en vegetatie rond obstakels — vooral in professioneel berm- en slootonderhoud door loonbedrijven, aannemers, gemeenten en waterschappen."),
        ("Welke maaiarm is geschikt voor mijn tractor?",
         "Dat hangt vooral af van het gewicht en de hydraulische capaciteit van uw tractor. Compacte maaiarmen zijn al te combineren met tractoren vanaf circa 3.000 kg, zwaardere uitvoeringen vragen 7.000 kg of meer. Zie "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+" voor meer uitleg."),
        ("Welke werktuigen kunnen op een maaiarm gemonteerd worden?",
         "Onder meer een klepelkop, messenbalk, takkenschaar en maaikorf, afhankelijk van merk en model. Bij GreenTec kan dit zonder gereedschap gewisseld worden."),
        ("Welke merken maaiarmen levert Wim van Breda?",
         "Wim van Breda levert maaiarmen van Herder en GreenTec, beide met een breed programma van compacte tot zware uitvoeringen."),
        ("Waar kan ik advies krijgen over een maaiarm?",
         "Neem contact op met Wim van Breda in Geldermalsen voor advies op basis van uw tractor, terrein en beheerwerk."),
    ],
    related=[("Maaiarm kopen","/maaiarm/kopen/"),("Maaiarm voor tractor","/maaiarm/voor-tractor/"),
             ("Maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/"),("Maaiarm bij slootonderhoud","/maaiarm/slootonderhoud/"),
             ("Klepelmaaier","/klepelmaaier/"),("Maaikorf","/maaikorf/"),("Bermonderhoud","/bermonderhoud/")],
)

# ===========================================================================
add(
    "/maaiarm/kopen/",
    "Maaiarm kopen voor professioneel gebruik | Wim van Breda",
    "Maaiarm kopen bij Wim van Breda: advies over merk, armlengte en werktuig, passend bij uw tractor en toepassing. Levering en service uit Geldermalsen.",
    "Maaiarm kopen",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Maaiarm kopen", None)],
    "Wie een maaiarm koopt voor professioneel bermen sloot- of taludonderhoud, maakt in feite drie keuzes tegelijk: welk merk en model, welke armlengte en welk werktuig aan het uiteinde. Wim van Breda helpt die keuze te maken op basis van uw tractor en het werk dat u uitvoert, en levert de arm inclusief montage, onderdelen en service.",
    fact="Bij de aanschaf van een maaiarm zijn drie zaken bepalend: het gewicht en de hydraulische capaciteit van de tractor, de gewenste armlengte en het bereik, en het werktuig dat het meest gebruikt gaat worden. Deze drie factoren samen bepalen welk model daadwerkelijk past.",
    sections=[
        h2("Waar u op let bij de aankoop van een maaiarm",
           ul([
               "Tractorgewicht en hydraulische capaciteit — bepaalt welke armklasse mogelijk is; zie "+a("maaiarm voor tractor","/maaiarm/voor-tractor/"),
               "Armlengte en horizontaal bereik — hoe ver de arm bij taluds of over water moet kunnen reiken",
               "Werktuig — klepelkop, messenbalk, takkenschaar of maaikorf, afhankelijk van het onderhoudstype",
               "Bediening — moderne armen zijn elektrohydraulisch en proportioneel vanuit de cabine te besturen",
               "Onderhoudsgemak — toegankelijke servicepunten en beschikbaarheid van onderdelen",
           ])),
        h2("Nieuw of gebruikt?",
           p("Wim van Breda richt zich bij maaiarmen primair op de levering van nieuwe machines van Herder en GreenTec. Voor gebruikte machines, waaronder soms ook maaiarmen, verwijzen wij naar het occasion-aanbod op de website.")),
        h2("Welke merken kunt u kopen bij Wim van Breda?",
           p(a("Herder","/maaiarm/herder/")+" bouwt al ruim 75 jaar maaiarmen voor berm-, dijk- en slootonderhoud, met de "+a("Grenadier","/machine/herder-grenadier-maaiarm/")+" als voorbeeld van een zware uitvoering met een armlengte van 6,40 tot 8,80 meter. "+a("GreenTec","/maaiarm/greentec/")+" werkt met een modulair systeem waarbij dezelfde draagarm zonder gereedschap kan wisselen tussen klepelkop en takkenschaar, en bouwt zowel compacte als zware modellen.")),
        h2("Wat een aankoop bij Wim van Breda inhoudt",
           p("Bij aankoop hoort montage op uw tractor, inrijden van de machine bij aflevering en uitleg aan de machinist over de bediening. Onderdelen worden op voorraad gehouden in de eigen werkplaats in Geldermalsen, zodat onderhoud en reparatie niet hoeven te wachten op een lange levertijd.")),
    ],
    machines=("Voorbeelden van te koop staande maaiarmen", [
        card("herder-grenadier-maaiarm"),
        card("greentec-scorpion-430-s-basisfront-maaiarm"),
    ]),
    faq=[
        ("Wat kost een maaiarm?",
         "De prijs hangt sterk af van armlengte, merk en het gewicht van de tractor waarop de arm gemonteerd wordt. Neem contact op voor een offerte op basis van uw specifieke situatie."),
        ("Kan ik een maaiarm op mijn bestaande tractor monteren?",
         "In veel gevallen wel, mits de tractor voldoende gewicht en hydraulische capaciteit heeft voor de gekozen armklasse. Wim van Breda beoordeelt dit per situatie."),
        ("Levert Wim van Breda ook gebruikte maaiarmen?",
         "Het accent bij maaiarmen ligt op nieuwe machines van Herder en GreenTec; voor gebruikt materieel verwijzen wij naar het occasion-aanbod."),
        ("Wat is het verschil tussen een Herder- en een GreenTec-maaiarm?",
         "Beide merken bouwen een breed programma. Herder is Nederlands en heeft een lange ervaring in berm- en dijkonderhoud; GreenTec is Deens en werkt met een modulair systeem waarbij het werktuig zonder gereedschap gewisseld kan worden."),
    ],
    related=[("Maaiarm","/maaiarm/"),("Maaiarm voor tractor","/maaiarm/voor-tractor/"),
             ("Maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/"),("Maaiarm bij slootonderhoud","/maaiarm/slootonderhoud/")],
)

# ===========================================================================
add(
    "/maaiarm/voor-tractor/",
    "Maaiarm voor tractor: welke armklasse past bij uw trekker | Wim van Breda",
    "Maaiarm gemonteerd op tractor voor berm-, sloot- en taludonderhoud. Advies over de juiste armklasse bij uw tractorgewicht.",
    "Maaiarm voor tractor",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Voor tractor", None)],
    "De meeste maaiarmen worden op een landbouwtractor gemonteerd, via de drie-punts hefinrichting aan de voor- of achterzijde, en aangedreven door de hydrauliek en aftakas van de tractor. Welke maaiarm mogelijk is, hangt in de eerste plaats af van het gewicht en de hydraulische capaciteit van die tractor.",
    fact="Lichtere, compacte maaiarmen zijn al te combineren met tractoren vanaf circa 3.000 kg; middenklasse-armen vragen doorgaans 5.000 tot 7.000 kg, en de zwaarste uitvoeringen met het grootste bereik zijn bedoeld voor tractoren vanaf 7.000 à 8.000 kg. Naast het gewicht spelen ook de hydraulische capaciteit (oliedebiet) en de beschikbare frontmontage een rol.",
    sections=[
        h2("Welke tractor past bij welke maaiarm",
           p("Het gewicht van de maaiarm zelf, plus het gewicht van het gemonteerde werktuig, moet in verhouding staan tot het gewicht van de tractor om voldoende stabiliteit te houden — zeker bij een volledig uitgeschoven arm. Een voorbeeld: de "+a("GreenTec Scorpion 430 S","/machine/greentec-scorpion-430-s-basisfront-maaiarm/")+" is ontworpen voor tractoren vanaf 3.000 kg, terwijl de grotere "+a("Scorpion 830 Plus","/machine/greentec-scorpion-830-plus-maaiarm/")+" pas past bij tractoren vanaf 8.000 kg.")),
        h2("Front- of achtermontage",
           p("Een maaiarm kan vooraan (voor goed zicht op het werktuig tijdens het werk) of achteraan de tractor gemonteerd worden. Welke opstelling het beste past, hangt af van het type werk, de rijrichting tijdens het maaien en de voorkeur van de bestuurder.")),
        h2("Hydrauliek en bediening",
           p("Naast het gewicht is ook het hydraulische oliedebiet van de tractor van belang: de arm en het werktuig hebben voldoende hydraulische capaciteit nodig om vlot en gelijkmatig te bewegen. Moderne maaiarmen worden elektrohydraulisch en proportioneel bediend vanuit de cabine, waardoor de bestuurder de armbeweging nauwkeurig kan sturen.")),
        h2("Advies over de juiste combinatie",
           p("Wim van Breda beoordeelt per situatie welke armklasse bij uw tractor past, op basis van het gewicht, de hydrauliek en het beoogde werk. Zie ook "+a("maaiarm kopen","/maaiarm/kopen/")+" voor de bredere aankoopoverwegingen.")),
    ],
    faq=[
        ("Welk tractorgewicht heb ik minimaal nodig voor een maaiarm?",
         "Compacte maaiarmen zijn al mogelijk vanaf circa 3.000 kg tractorgewicht; zwaardere uitvoeringen met groter bereik vragen 7.000 tot 8.000 kg of meer."),
        ("Kan een maaiarm zowel voor als achter gemonteerd worden?",
         "Ja, afhankelijk van het model en de tractor kan een maaiarm zowel op de front- als op de achterhefinrichting gemonteerd worden."),
        ("Is elke tractor geschikt voor een maaiarm?",
         "Niet elke tractor: naast het gewicht is ook voldoende hydraulische capaciteit nodig. Wim van Breda beoordeelt dit per tractor en gewenste maaiarm."),
    ],
    related=[("Maaiarm","/maaiarm/"),("Maaiarm kopen","/maaiarm/kopen/"),("Werktuigdrager","/werktuigdrager/")],
)

# ===========================================================================
add(
    "/maaiarm/bermonderhoud/",
    "Maaiarm voor bermonderhoud | Wim van Breda",
    "Maaiarm inzetten voor professioneel bermonderhoud: bereik over taluds en obstakels heen, met klepelkop of messenbalk.",
    "Maaiarm voor bermonderhoud",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Bermonderhoud", None)],
    "Een maaiarm wordt bij professioneel bermonderhoud gebruikt om vegetatie langs wegen, sloten en taluds te maaien op plekken die met een vaste maaier moeilijk bereikbaar zijn. Afhankelijk van de uitvoering kan een maaiarm worden gecombineerd met verschillende werktuigen voor berm-, sloot- en vegetatieonderhoud, en dat maakt hem tot het meest gebruikte werktuig in professioneel bermbeheer.",
    fact="In bermonderhoud is de maaiarm het werktuig bij uitstek zodra er hoogteverschil, een sloot of obstakels als verkeersborden en bomen in het maaitraject zitten. Anders dan een vaste maaier kan de arm zijwaarts uitschuiven, over een talud naar beneden werken en om obstakels heen sturen, zonder dat de bestuurder de tractor hoeft te verplaatsen.",
    sections=[
        h2("Waarom een maaiarm bij bermonderhoud",
           p("Met een klepelkop wordt gras en opslag verkleind achtergelaten; met een messenbalk ontstaat een net, kort gemaaide bermrand. Doordat de arm het bereik van de machine vergroot, hoeft de tractor niet van de rijbaan of berm af, wat het werk ook veiliger maakt voor de bestuurder en het overige verkeer.")),
        h2("Waar wordt een maaiarm voor bermonderhoud voor gebruikt",
           ul([
               "Wegbermen langs provinciale en gemeentelijke wegen",
               "Taluds naast de rijbaan",
               "Slootranden aan de bermzijde",
               "Vegetatie rond verkeersborden, lichtmasten en vangrails",
               "Middenbermen en rotondes",
           ])),
        h2("Welke maaiarm past bij bermwerk",
           p("Voor regulier bermonderhoud volstaat vaak een compactere maaiarm met een klepelkop; bij bredere bermen, diepere sloten of zwaardere opslag is een arm met groter bereik en een steviger werktuig praktischer. Zie "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+" voor de gewichtsklassen per tractor.")),
        h2("Herder en GreenTec voor bermwerk",
           p("Zowel "+a("Herder","/maaiarm/herder/")+" als "+a("GreenTec","/maaiarm/greentec/")+" bouwen maaiarmen die specifiek voor intensief bermbeheer worden ingezet door loonbedrijven en gemeenten. De "+a("Herder Grenadier","/machine/herder-grenadier-maaiarm/")+" is daarvan een voorbeeld met een armlengte van 6,40 tot 8,80 meter en de mogelijkheid om te wisselen tussen klepelmaaier, maaikorf en andere werktuigen.")),
        h2("Service en onderhoud",
           p("Bermonderhoud is vaak intensief, seizoensgebonden werk waarbij een machine niet lang mag stilstaan. Wim van Breda houdt onderdelen op voorraad en verzorgt onderhoud vanuit de eigen werkplaats in Geldermalsen.")),
    ],
    machines=("Relevante machines voor bermonderhoud", [
        card("herder-grenadier-maaiarm"),
        card("greentec-scorpion-430-s-basisfront-maaiarm"),
    ]),
    faq=[
        ("Wat is een maaiarm?",
         "Een maaiarm is een hydraulisch aangedreven, uitschuifbare arm op een tractor, met aan het uiteinde een verwisselbaar werktuig zoals een klepelkop of messenbalk."),
        ("Waarvoor wordt een maaiarm bij bermonderhoud gebruikt?",
         "Om vegetatie langs wegen, sloten en taluds te maaien op plekken die met een vaste maaier moeilijk bereikbaar zijn, zoals hellingen, slootkanten en obstakels."),
        ("Welke maaiarm is geschikt voor bermonderhoud?",
         "Dat hangt af van de breedte en het reliëf van de berm en het tractorgewicht; Wim van Breda adviseert op basis van uw specifieke traject."),
        ("Kan een maaiarm aan verschillende tractoren worden gebruikt?",
         "Ja, mits het tractorgewicht en de hydraulische capaciteit passen bij de gekozen armklasse — zie "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+"."),
        ("Welke werktuigen kunnen op een maaiarm voor bermwerk?",
         "Onder meer een klepelkop voor grasverkleining, een messenbalk voor een nette bermrand, en een takkenschaar voor opslag."),
        ("Welke merken maaiarmen levert Wim van Breda voor bermonderhoud?",
         "Herder en GreenTec, beide met modellen die veel voor bermwerk worden ingezet."),
    ],
    related=[("Maaiarm","/maaiarm/"),("Bermonderhoud","/bermonderhoud/"),("Maaiarm bij bermonderhoud (bermcluster)","/bermonderhoud/maaiarm/"),
             ("Klepelmaaier bij bermonderhoud","/klepelmaaier/bermonderhoud/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/")],
)

# ===========================================================================
add(
    "/maaiarm/slootonderhoud/",
    "Maaiarm voor slootonderhoud | Wim van Breda",
    "Maaiarm voor het maaien en schonen van sloten en watergangen, met maaikorf voor opvang van maaisel uit het water.",
    "Maaiarm voor slootonderhoud",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Slootonderhoud", None)],
    "Bij slootonderhoud maait de maaiarm het talud en de waterlijn, vaak in combinatie met een maaikorf die het maaisel direct uit het water opvangt in plaats van het te laten liggen. Zo kan het onderhoud in één werkgang vanaf de kant gebeuren, zonder dat de oever betreden hoeft te worden.",
    fact="Een maaiarm reikt vanaf de kant tot in de sloot en kan zowel het talud als de waterlijn maaien. Waar maaisel niet in het water mag achterblijven, wordt de klepelkop vervangen door een maaikorf die het gemaaide materiaal direct meeneemt.",
    sections=[
        h2("Talud en waterlijn in één werkgang",
           p("Doordat de maaiarm vanaf de berm werkt, hoeft de bestuurder de sloot niet in of de oever niet te betreden. Dat is zowel efficiënter als minder belastend voor de bodem en de oeverbeschoeiing.")),
        h2("Waarom een maaikorf bij slootonderhoud",
           p("Voor watergangen waar maaisel niet in het water mag achterblijven — bijvoorbeeld om verstopping van de waterafvoer te voorkomen — wordt de klepelkop vervangen door een "+a("maaikorf","/maaikorf/voor-maaiarm/")+" die het gemaaide materiaal direct opvangt. De "+a("Herder maaikorf","/machine/herder-maaikorf/")+" is daar een voorbeeld van: een korf die zowel boven als onder water kan maaien en verstoppingen voorkomt dankzij het open korfontwerp.")),
        h2("Welke maaiarm past bij slootonderhoud",
           p("Voor de meeste sloten volstaat een maaiarm met voldoende bereik om zowel het talud als de waterlijn te bestrijken. Bij bredere watergangen is een arm met groter horizontaal bereik nodig — zie ook "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+" voor de bijbehorende tractorgewichten.")),
        h2("Wie voert dit werk uit",
           p("Slootonderhoud met een maaiarm wordt vooral uitgevoerd door waterschappen, aannemers die in opdracht van waterschappen werken, en loonbedrijven met vaste onderhoudscontracten voor watergangen.")),
    ],
    machines=("Relevante machines voor slootonderhoud", [
        card("herder-maaikorf"),
        card("herder-grenadier-maaiarm"),
    ]),
    faq=[
        ("Waarom wordt bij slootonderhoud een maaikorf gebruikt in plaats van een klepelkop?",
         "Omdat maaisel bij veel watergangen niet in het water mag achterblijven; een maaikorf maait en vangt het materiaal in één beweging op."),
        ("Kan een maaiarm zowel het talud als de waterlijn maaien?",
         "Ja, de arm reikt vanaf de kant tot in de sloot en kan beide onderdelen in één werkgang bewerken."),
        ("Welke maaiarm is geschikt voor slootonderhoud?",
         "Dat hangt af van de breedte van de sloot en het gewenste bereik; Wim van Breda adviseert op basis van de specifieke watergang."),
    ],
    related=[("Maaiarm","/maaiarm/"),("Slootonderhoud","/slootonderhoud/"),("Maaiarm bij slootonderhoud (slootcluster)","/slootonderhoud/maaiarm/"),
             ("Maaikorf voor watergangen","/maaikorf/voor-watergangen/"),("Maaikorf bij slootonderhoud","/maaikorf/slootonderhoud/")],
)

# ===========================================================================
add(
    "/maaiarm/herder/",
    "Herder maaiarm | Wim van Breda",
    "Herder maaiarmen bij Wim van Breda: Nederlands merk met ruim 75 jaar ervaring in berm-, dijk- en slootonderhoud.",
    "Herder maaiarm",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("Herder", None)],
    "Herder is een Nederlands merk dat al ruim 75 jaar maaiarmen, maaikorven en dijkenmaaiers bouwt voor waterschappen, gemeenten en aannemers. Wim van Breda levert het Herder-programma inclusief montage, onderdelen en service.",
    fact="Herder ontwikkelt sinds de oprichting door de gebroeders Den Herder machines voor berm-, sloot- en vegetatieonderhoud. De Herder Grenadier maaiarm is daarvan een voorbeeld: een zware, veelzijdige arm met een armlengte van 6,40 tot 8,80 meter, uit te rusten met uiteenlopende aanbouwwerktuigen.",
    sections=[
        h2("Het Herder-programma bij Wim van Breda",
           p("Herder bouwt zowel zware maaiarmen voor intensief bermbeheer als compactere uitvoeringen voor kleinere tractoren. De "+a("Grenadier","/machine/herder-grenadier-maaiarm/")+" is het bekendste model in het zwaardere segment: een flexibele maaiarm die zijdelings op de tractor wordt gemonteerd en die verschillende posities kan innemen om moeilijk bereikbare plekken zoals diepe sloten, steile taluds en obstakels als vangrails en bomen te bereiken. De arm is uit te rusten met onder meer een klepelmaaier, maaikorf, schijvenmaaier, bosbouwmaaier, stobbenfrees en onkruidborstel, en is ook leverbaar met afzuiging.")),
        h2("Ook maaikorven van Herder",
           p("Naast maaiarmen levert Herder ook "+a("maaikorven","/maaikorf/herder/")+", zoals de "+a("Herder maaikorf","/machine/herder-maaikorf/")+" — een korf met messen van gehard staal en een open ontwerp dat verstoppingen voorkomt, geschikt voor maaien boven én onder water. Deze wordt vaak gecombineerd ingezet met een maaiarm bij sloot- en watergangonderhoud.")),
        h2("Voor wie Herder relevant is",
           p("Herder-machines worden bij Wim van Breda vooral geleverd aan waterschappen, gemeenten en aannemers die structureel bermen, dijken en watergangen onderhouden.")),
    ],
    machines=("Herder-machines bij Wim van Breda", [
        card("herder-grenadier-maaiarm"),
        card("herder-maaikorf"),
    ]),
    related=[("Maaiarm","/maaiarm/"),("Herder maaikorf","/maaikorf/herder/"),("Maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/"),
             ("Herder (merkpagina)","/herder/maaiarm/")],
)

# ===========================================================================
add(
    "/maaiarm/greentec/",
    "GreenTec maaiarm | Wim van Breda",
    "GreenTec maaiarmen bij Wim van Breda: Deens merk met modulair systeem — één draagarm, meerdere werktuigen zonder gereedschap wisselen.",
    "GreenTec maaiarm",
    [("Home", HOME), ("Maaiarm", "/maaiarm/"), ("GreenTec", None)],
    "GreenTec is een Deens merk dat bekendstaat om zijn modulaire maaiarmsysteem: één draagarm waarop zonder gereedschap gewisseld kan worden tussen klepelkop, takkenschaar en andere werktuigen. Wim van Breda levert het GreenTec-programma van compacte tot zware uitvoeringen.",
    fact="Het modulaire systeem van GreenTec maakt één maaiarm geschikt voor meerdere taken door het seizoen heen: maaien in het voorjaar en de zomer, snoeien en takken verwijderen in het najaar, met dezelfde basisarm en zonder dat er gereedschap nodig is om van werktuig te wisselen.",
    sections=[
        h2("De Scorpion-serie",
           p("De Scorpion-serie is het bekendste voorbeeld van het GreenTec-programma. De "+a("Scorpion 430 S – Basisfront","/machine/greentec-scorpion-430-s-basisfront-maaiarm/")+" is een compacte uitvoering voor tractoren vanaf 3.000 kg, met een horizontaal bereik van 4,3 meter — geschikt voor gebieden met beperkte ruimte zoals bermen in woonwijken of fietspaden. De "+a("Scorpion 830 Plus","/machine/greentec-scorpion-830-plus-maaiarm/")+" is een zwaardere uitvoering met 8,3 meter horizontaal bereik, bedoeld voor grote tractoren vanaf 8.000 kg en intensief berm-, heg- en slootonderhoud.")),
        h2("Constructie en bediening",
           p("GreenTec-maaiarmen zijn opgebouwd uit hoogwaardig staal (bij de Scorpion-modellen Strenx 700) en hebben vier montagepunten op het hoofdframe voor extra stabiliteit. De hydraulische armdraaiing bedraagt bij veel modellen 155 graden, met power control en de keuze voor een hybride armsysteem — met of zonder parallelle beweging.")),
        h2("Voor wie GreenTec relevant is",
           p("GreenTec wordt bij Wim van Breda geleverd aan loonbedrijven, aannemers en gemeenten die met één maaiarm meerdere werktuigen willen gebruiken, van compact bermwerk tot zwaar berm- en slootonderhoud.")),
    ],
    machines=("GreenTec-maaiarmen bij Wim van Breda", [
        card("greentec-scorpion-430-s-basisfront-maaiarm"),
        card("greentec-scorpion-830-plus-maaiarm"),
    ]),
    related=[("Maaiarm","/maaiarm/"),("GreenTec klepelmaaier","/klepelmaaier/greentec/"),("Maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/"),
             ("GreenTec (merkpagina)","/greentec/maaiarm/")],
)
