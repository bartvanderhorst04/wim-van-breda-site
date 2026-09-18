# -*- coding: utf-8 -*-
"""Inhoud cluster 3: maaikorf."""
from build_seo_pages import h2, h3, p, ul, a

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related, fact=fact))

# ===========================================================================
# 3. MAAIKORF
# ===========================================================================
add(
    "/maaikorf/",
    "Maaikorf | Wim van Breda",
    "Maaikorf voor het opvangen van maaisel bij sloot- en watergangonderhoud. Merken als Herder, montage op maaiarm of tractor.",
    "Maaikorf",
    [("Home", HOME), ("Maaikorf", None)],
    "Een maaikorf is een rondsel- of trommelvormig aanbouwdeel dat maaisel tijdens het maaien direct opvangt, zodat het niet in het water of op de kant achterblijft.",
    sections=[
        h2("Waarom een maaikorf",
           p("Bij sloten en watergangen mag maaisel vaak niet blijven liggen: het verstopt de waterafvoer en zorgt voor extra voedingsstoffen in het water. Een maaikorf vangt het materiaal tijdens het maaien op en voert het apart af, in één werkgang met het maaien zelf.")),
        h2("Montage",
           p("De maaikorf wordt meestal gemonteerd aan het uiteinde van een "+a("maaiarm","/maaikorf/voor-maaiarm/")+", zodat de bestuurder vanuit de cabine zowel de maaihoogte als de opvang kan regelen.")),
        h2("Merken",
           p(a("Herder","/maaikorf/herder/")+" is een van de merken die maaikorven levert als aanbouwdeel bij hun maaiarmen, veel gebruikt door waterschappen en aannemers in slootonderhoud.")),
    ],
    faq=[
        ("Wat is het verschil tussen een maaikorf en een klepelkop?",
         "Een klepelkop verkleint maaisel en laat het liggen; een maaikorf maait en vangt het materiaal tegelijk op, zodat het apart afgevoerd kan worden — nodig zodra maaisel niet in het water of op de kant mag blijven."),
        ("Past een maaikorf op elke maaiarm?",
         "De maaikorf moet qua bevestiging en gewicht passen bij de maaiarm en het hydraulische systeem van de tractor; vraag advies aan Wim van Breda over de juiste combinatie."),
    ],
    related=[("Maaikorf kopen","/maaikorf/kopen/"),("Maaikorf voor slootonderhoud","/maaikorf/slootonderhoud/"),
             ("Maaikorf voor watergangen","/maaikorf/voor-watergangen/"),("Maaiarm","/maaiarm/"),("Slootonderhoud","/slootonderhoud/")],
)

add(
    "/maaikorf/kopen/",
    "Maaikorf kopen | Wim van Breda",
    "Maaikorf kopen bij Wim van Breda: advies over de juiste maat en montage, passend bij uw maaiarm en tractor.",
    "Maaikorf kopen",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Maaikorf kopen", None)],
    "Bij de keuze van een maaikorf zijn de afmetingen van de korf, het gewicht en de bevestigingswijze op de maaiarm de belangrijkste aandachtspunten.",
    sections=[
        h2("Waar u op let",
           ul([
               "Bevestiging — de korf moet passen op de maaiarm die u al heeft of gaat aanschaffen.",
               "Capaciteit — hoeveel maaisel de korf in één werkgang kan verwerken.",
               "Toepassing — sloot, watergang of droge berm stellen elk net andere eisen.",
           ])),
        h2("Advies bij Wim van Breda",
           p("Wim van Breda adviseert over de combinatie van maaikorf en maaiarm en levert "+a("Herder","/maaikorf/herder/")+"-maaikorven inclusief montage en service.")),
    ],
    related=[("Maaikorf","/maaikorf/"),("Maaikorf voor maaiarm","/maaikorf/voor-maaiarm/"),("Maaikorf voor tractor","/maaikorf/voor-tractor/")],
)

add(
    "/maaikorf/slootonderhoud/",
    "Maaikorf voor slootonderhoud | Wim van Breda",
    "Maaikorf inzetten bij slootonderhoud: maaisel direct opvangen tijdens het maaien van talud en waterlijn.",
    "Maaikorf voor slootonderhoud",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Slootonderhoud", None)],
    "Bij professioneel slootonderhoud wordt de maaikorf gebruikt om het talud en de waterlijn te maaien zonder dat het maaisel in de sloot terechtkomt.",
    sections=[
        h2("Eén werkgang",
           p("Doordat maaien en opvangen tegelijk gebeuren, hoeft het maaisel niet achteraf handmatig uit het water gehaald te worden — dat scheelt een aparte werkgang en voorkomt verstopping van de waterafvoer.")),
    ],
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaikorf voor slootonderhoud (sloot)","/slootonderhoud/maaikorf/"),("Maaikorf voor watergangen","/maaikorf/voor-watergangen/")],
)

add(
    "/maaikorf/voor-maaiarm/",
    "Maaikorf voor maaiarm | Wim van Breda",
    "Maaikorf als aanbouwdeel op een maaiarm: maaien en opvangen van maaisel in één beweging.",
    "Maaikorf voor maaiarm",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Voor maaiarm", None)],
    "De maaikorf wordt gemonteerd aan het uiteinde van een maaiarm, op de plek waar normaal een klepelkop of messenbalk zit, zodat de bestuurder vanuit de cabine kan maaien én tegelijk het maaisel opvangen.",
    sections=[
        h2("Combinatie met de arm",
           p("Het gewicht en de aansturing van de korf moeten passen bij de hydrauliek van de maaiarm; Wim van Breda adviseert welke combinatie van "+a("maaiarm","/maaiarm/")+" en maaikorf geschikt is voor uw tractor.")),
    ],
    related=[("Maaiarm","/maaiarm/"),("Maaikorf","/maaikorf/"),("Maaikorf kopen","/maaikorf/kopen/")],
)

add(
    "/maaikorf/voor-watergangen/",
    "Maaikorf voor watergangen | Wim van Breda",
    "Maaikorf voor het onderhoud van watergangen: maaisel opvangen zodat het niet in het water terechtkomt.",
    "Maaikorf voor watergangen",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Voor watergangen", None)],
    "Bij watergangen die vrij van maaisel moeten blijven — bijvoorbeeld voor de waterafvoer of waterkwaliteit — is de maaikorf het aangewezen aanbouwdeel om tijdens het maaien direct op te vangen.",
    sections=[
        h2("Voor waterschappen en aannemers",
           p("Waterschappen en aannemers die in opdracht van waterschappen werken, gebruiken de maaikorf om te voldoen aan de eis dat maaisel uit de watergang wordt gehouden.")),
    ],
    related=[("Maaikorf","/maaikorf/"),("Slootonderhoud","/slootonderhoud/"),("Maaikorf voor slootonderhoud","/maaikorf/slootonderhoud/")],
)

add(
    "/maaikorf/voor-tractor/",
    "Maaikorf voor tractor | Wim van Breda",
    "Maaikorf op tractor via maaiarm: opvang van maaisel bij sloot- en bermonderhoud vanaf de tractor.",
    "Maaikorf voor tractor",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Voor tractor", None)],
    "Een maaikorf werkt altijd in combinatie met een maaiarm op de tractor: de tractor levert de hydrauliek en voortbeweging, de arm het bereik, en de korf de opvang van het maaisel.",
    sections=[
        h2("Geschikte tractoren",
           p("Welke tractor geschikt is, hangt af van de maaiarm waarop de korf gemonteerd wordt — zie onze pagina over "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+" voor de gangbare gewichtsklassen.")),
    ],
    related=[("Maaikorf","/maaikorf/"),("Maaiarm voor tractor","/maaiarm/voor-tractor/"),("Maaikorf voor maaiarm","/maaikorf/voor-maaiarm/")],
)

add(
    "/maaikorf/herder/",
    "Herder maaikorf | Wim van Breda",
    "Herder maaikorven bij Wim van Breda: aanbouwdeel op Herder-maaiarmen voor sloot- en watergangonderhoud.",
    "Herder maaikorf",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Herder", None)],
    "Herder levert naast maaiarmen ook maaikorven, ontwikkeld om als aanbouwdeel op de eigen maaiarmen gemonteerd te worden voor sloot- en watergangonderhoud.",
    sections=[
        h2("In combinatie met de Herder-maaiarm",
           p("Zie ook onze pagina over de "+a("Herder maaiarm","/maaiarm/herder/")+" voor de armmodellen waarop deze maaikorven passen.")),
    ],
    related=[("Maaikorf","/maaikorf/"),("Herder maaiarm","/maaiarm/herder/"),("Maaikorf voor watergangen","/maaikorf/voor-watergangen/")],
)
