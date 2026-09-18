# -*- coding: utf-8 -*-
"""Inhoud cluster 4: ecologisch maaien + ecologisch bermbeheer."""
from build_seo_pages import h2, h3, p, ul, a

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related, fact=fact))

# ===========================================================================
# 4. ECOLOGISCH MAAIEN
# ===========================================================================
add(
    "/ecologisch-maaien/",
    "Ecologisch maaien | Wim van Breda",
    "Ecologisch maaien: machines en methode voor natuurvriendelijk beheer van bermen en groenstroken, met of zonder afvoer van maaisel.",
    "Ecologisch maaien",
    [("Home", HOME), ("Ecologisch maaien", None)],
    "Ecologisch maaien is een maaimethode die rekening houdt met flora en fauna: gefaseerd maaien, aangepaste maaihoogte en het afvoeren van maaisel om de bodem te verschralen, in plaats van alles in één keer kort te maaien.",
    sections=[
        h2("Wat ecologisch maaien anders maakt",
           p("In plaats van een volledig terrein in één beurt kort te maaien, wordt vaak gefaseerd gewerkt: een deel van de vegetatie blijft steeds staan als schuil- en voedselplek voor insecten en kleine dieren. Ook de maaihoogte ligt doorgaans hoger dan bij regulier maaiwerk.")),
        h2("Machines voor ecologisch maaien",
           p("De machines die hiervoor gebruikt worden zijn vergelijkbaar met regulier beheer — "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("maaiarmen","/maaiarm/")+" — maar worden ingezet volgens een ecologisch maaischema en vaak in combinatie met opvang van maaisel. Zie onze pagina over "+a("machines voor ecologisch maaien","/ecologisch-maaien/machines/")+".")),
        h2("Voor wie",
           p("Gemeenten, waterschappen en terreinbeheerders die natuurvriendelijk bermbeheer voeren, vaak in het kader van biodiversiteitsbeleid.")),
    ],
    faq=[
        ("Wat is het verschil tussen ecologisch maaien en gewoon maaien?",
         "Bij ecologisch maaien wordt gefaseerd gemaaid (niet alles tegelijk), ligt de maaihoogte vaak hoger en wordt maaisel regelmatig afgevoerd om de bodem te verschralen — met als doel meer ruimte voor flora en fauna."),
        ("Is er speciale apparatuur nodig voor ecologisch maaien?",
         "Niet per se: dezelfde klepelmaaiers en maaiarmen die voor regulier bermbeheer worden gebruikt, zijn ook geschikt voor ecologisch maaien; het verschil zit vooral in de werkwijze en planning."),
    ],
    related=[("Machines voor ecologisch maaien","/ecologisch-maaien/machines/"),("Ecologisch bermmaaien","/ecologisch-maaien/bermmaaien/"),
             ("Maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/"),("Bermonderhoud","/bermonderhoud/")],
)

add(
    "/ecologisch-maaien/machines/",
    "Machines voor ecologisch maaien | Wim van Breda",
    "Welke machines geschikt zijn voor ecologisch maaien: klepelmaaiers en maaiarmen, ingezet volgens een natuurvriendelijk maaischema.",
    "Machines voor ecologisch maaien",
    [("Home", HOME), ("Ecologisch maaien", "/ecologisch-maaien/"), ("Machines", None)],
    "Voor ecologisch maaien zijn geen aparte machines nodig: het gaat om dezelfde klepelmaaiers en maaiarmen die ook voor regulier bermbeheer worden ingezet, gecombineerd met een ecologisch maaischema.",
    sections=[
        h2("Klepelmaaier of maaiarm",
           p("Een "+a("klepelmaaier","/klepelmaaier/")+" is geschikt voor open, gefaseerd te maaien vlakken; een "+a("maaiarm","/maaiarm/")+" wordt ingezet zodra er hoogteverschil, sloten of obstakels in het traject zitten.")),
        h2("Opvang van maaisel",
           p("Waar maaisel afgevoerd moet worden om de bodem te verschralen, wordt vaak een maaikorf of opvangsysteem toegevoegd — zie "+a("maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/")+".")),
    ],
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Klepelmaaier","/klepelmaaier/"),("Maaiarm","/maaiarm/")],
)

add(
    "/ecologisch-maaien/bermmaaien/",
    "Ecologisch bermmaaien | Wim van Breda",
    "Ecologisch bermmaaien: gefaseerd en natuurvriendelijk onderhoud van bermen, met aandacht voor biodiversiteit.",
    "Ecologisch bermmaaien",
    [("Home", HOME), ("Ecologisch maaien", "/ecologisch-maaien/"), ("Bermmaaien", None)],
    "Ecologisch bermmaaien past de maaimethode van reguliere bermen aan op biodiversiteit: gefaseerd maaien, een deel van de berm laten staan en de maaihoogte aanpassen aan de vegetatie.",
    sections=[
        h2("In de praktijk",
           p("Gemeenten passen dit vaak toe langs wegbermen met kruidenrijke vegetatie, waarbij per seizoen wisselend een deel van het traject gemaaid wordt in plaats van de volledige berm in één beurt.")),
    ],
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/"),("Bermonderhoud ecologisch","/bermonderhoud/ecologisch/")],
)

add(
    "/ecologisch-maaien/maaien-met-afvoer/",
    "Maaien met afvoer | Wim van Breda",
    "Maaien met afvoer van maaisel: verschraling van de bodem als onderdeel van ecologisch bermbeheer.",
    "Maaien met afvoer",
    [("Home", HOME), ("Ecologisch maaien", "/ecologisch-maaien/"), ("Maaien met afvoer", None)],
    "Bij maaien met afvoer wordt het maaisel na het maaien opgeraapt en afgevoerd in plaats van dat het blijft liggen, met als doel de bodem te verschralen en meer ruimte te geven aan kruidenrijke vegetatie.",
    sections=[
        h2("Waarom afvoeren",
           p("Blijft maaisel liggen, dan verteert het en verrijkt het de bodem — waardoor grassen op termijn de overhand krijgen boven kruiden en bloemen. Afvoeren voorkomt dat en ondersteunt zo de biodiversiteit.")),
        h2("Uitvoering",
           p("Dit kan met een maai-laadcombinatie die maait en tegelijk opzuigt, of met een maaikorf op een maaiarm die het materiaal direct meeneemt.")),
    ],
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Maaikorf","/maaikorf/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/")],
)

add(
    "/ecologisch-bermbeheer/",
    "Ecologisch bermbeheer | Wim van Breda",
    "Ecologisch bermbeheer: natuurvriendelijk onderhoud van bermen gericht op biodiversiteit, met passende machines en maaimethode.",
    "Ecologisch bermbeheer",
    [("Home", HOME), ("Ecologisch bermbeheer", None)],
    "Ecologisch bermbeheer richt zich op het onderhouden van bermen met behoud en versterking van de biodiversiteit: gefaseerd maaien, aangepaste maaihoogte en het afvoeren van maaisel.",
    sections=[
        h2("Beleid en uitvoering samen",
           p("Veel gemeenten en waterschappen hebben inmiddels een ecologisch maaibeleid voor hun bermen. De uitvoering vraagt dezelfde soort machines als regulier bermonderhoud — "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("maaiarmen","/maaiarm/")+" — maar ingezet volgens het ecologische maaischema van de opdrachtgever.")),
        h2("Wim van Breda in de praktijk",
           p("Wim van Breda levert en onderhoudt de machines die loonbedrijven en aannemers gebruiken om ecologisch bermbeheer uit te voeren, vanuit Geldermalsen.")),
    ],
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Ecologisch bermmaaien","/ecologisch-maaien/bermmaaien/"),
             ("Bermonderhoud ecologisch","/bermonderhoud/ecologisch/"),("Bermonderhoud","/bermonderhoud/")],
)
