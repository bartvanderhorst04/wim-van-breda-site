# -*- coding: utf-8 -*-
"""Inhoud cluster 3: maaikorf (7 pagina's, uitgebreide versie)."""
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
    "/maaikorf/",
    "Maaikorf voor sloot- en watergangonderhoud | Wim van Breda",
    "Maaikorf voor het opvangen van maaisel bij sloot- en watergangonderhoud. Herder maaikorf, montage op maaiarm.",
    "Maaikorf",
    [("Home", HOME), ("Maaikorf", None)],
    "Een maaikorf is een aanbouwdeel dat maaisel tijdens het maaien direct opvangt, zodat het niet in het water of op de kant achterblijft. Wim van Breda levert de Herder maaikorf voor sloot- en watergangonderhoud, als aanbouwdeel op een maaiarm.",
    fact="Een maaikorf maait en vangt vegetatie in één beweging op, in plaats van het materiaal te verkleinen en te laten liggen zoals een klepelkop doet. Dat is nodig zodra maaisel niet in het water of op de kant mag achterblijven, bijvoorbeeld bij sloten en watergangen die vrij moeten blijven voor de waterafvoer.",
    sections=[
        h2("Waarom een maaikorf",
           p("Bij sloten en watergangen mag maaisel vaak niet blijven liggen: het verstopt de waterafvoer en zorgt voor extra voedingsstoffen in het water, wat de waterkwaliteit kan schaden. Een maaikorf vangt het materiaal tijdens het maaien op en voert het apart af, in één werkgang met het maaien zelf.")),
        h2("Hoe een maaikorf werkt",
           p("De maaikorf wordt gemonteerd aan het uiteinde van een "+a("maaiarm","/maaikorf/voor-maaiarm/")+", zodat de bestuurder vanuit de cabine zowel de maaihoogte als de opvang kan regelen. De "+a("Herder maaikorf","/machine/herder-maaikorf/")+" is hiervan een voorbeeld: een korf met messen van gehard staal en een open ontwerp, waardoor overtollig water direct wegstroomt terwijl gemaaide vegetatie wordt opgevangen — geschikt voor maaien boven én onder water.")),
        h2("Waarvoor wordt een maaikorf gebruikt",
           ul([
               "Maaien van riet en grasbegroeiing in en langs het water",
               "Onderhoud van sloten en watergangen",
               "Oeverbeheer",
               "Natuurvriendelijk slootonderhoud",
           ])),
        h2("Merken",
           p(a("Herder","/maaikorf/herder/")+" is het merk dat Wim van Breda levert als aanbouwdeel bij de eigen maaiarmen, veel gebruikt door waterschappen en aannemers in slootonderhoud. De maaikorf is uitwisselbaar tussen verschillende Herder-machines en leverbaar in diverse werkbreedtes, geschikt voor machines van minigraafmachines tot 5 ton tot grotere midi- en graafmachines.")),
        h2("Service en onderhoud",
           p("Wim van Breda levert de maaikorf inclusief montage op de maaiarm en houdt onderdelen op voorraad in de eigen werkplaats in Geldermalsen.")),
    ],
    machines=("Maaikorf bij Wim van Breda", [
        card("herder-maaikorf"),
    ]),
    faq=[
        ("Wat is een maaikorf?",
         "Een maaikorf is een aanbouwdeel dat vegetatie maait en tegelijk opvangt, zodat het niet in het water of op de kant achterblijft."),
        ("Wat is het verschil tussen een maaikorf en een klepelkop?",
         "Een klepelkop verkleint maaisel en laat het liggen; een maaikorf maait en vangt het materiaal tegelijk op, zodat het apart afgevoerd kan worden."),
        ("Past een maaikorf op elke maaiarm?",
         "De maaikorf moet qua bevestiging en gewicht passen bij de maaiarm en het hydraulische systeem van de tractor; Wim van Breda adviseert over de juiste combinatie."),
        ("Kan een maaikorf onder water maaien?",
         "De Herder maaikorf is geschikt voor maaien zowel boven als onder water, dankzij het open korfontwerp dat verstoppingen voorkomt."),
        ("Welke machines kunnen een maaikorf gebruiken?",
         "De Herder maaikorf is geschikt voor minigraafmachines tot 5 ton, midi- en graafmachines en tractormachines."),
    ],
    related=[("Maaikorf kopen","/maaikorf/kopen/"),("Maaikorf bij slootonderhoud","/maaikorf/slootonderhoud/"),
             ("Maaikorf voor watergangen","/maaikorf/voor-watergangen/"),("Maaiarm","/maaiarm/"),("Slootonderhoud","/slootonderhoud/")],
)

# ===========================================================================
add(
    "/maaikorf/kopen/",
    "Maaikorf kopen | Wim van Breda",
    "Maaikorf kopen bij Wim van Breda: advies over de juiste maat en montage, passend bij uw maaiarm en tractor.",
    "Maaikorf kopen",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Maaikorf kopen", None)],
    "Bij de keuze van een maaikorf zijn de afmetingen van de korf, het gewicht en de bevestigingswijze op de maaiarm de belangrijkste aandachtspunten. Wim van Breda adviseert over de combinatie van maaikorf en maaiarm en levert de Herder maaikorf inclusief montage en service.",
    fact="Een maaikorf moet qua bevestiging passen op de maaiarm die u al heeft of gaat aanschaffen, en qua capaciteit en werkbreedte aansluiten bij de watergang of sloot waarin hij wordt ingezet.",
    sections=[
        h2("Waar u op let",
           ul([
               "Bevestiging — de korf moet passen op de maaiarm die u al heeft of gaat aanschaffen",
               "Capaciteit — hoeveel maaisel de korf in één werkgang kan verwerken",
               "Toepassing — sloot, watergang of droge berm stellen elk net andere eisen",
               "Werkbreedte — van smalle sloten tot brede hoofdwatergangen",
           ])),
        h2("Advies bij Wim van Breda",
           p("Wim van Breda adviseert over de combinatie van maaikorf en maaiarm en levert de "+a("Herder maaikorf","/maaikorf/herder/")+" inclusief montage en service. De korf is leverbaar in verschillende uitvoeringen en werkbreedtes, geschikt voor machines van minigraafmachines tot grote graafmachines.")),
    ],
    machines=("Maaikorf bij Wim van Breda", [
        card("herder-maaikorf"),
    ]),
    related=[("Maaikorf","/maaikorf/"),("Maaikorf voor maaiarm","/maaikorf/voor-maaiarm/"),("Maaikorf voor tractor","/maaikorf/voor-tractor/")],
)

# ===========================================================================
add(
    "/maaikorf/slootonderhoud/",
    "Maaikorf voor slootonderhoud | Wim van Breda",
    "Maaikorf inzetten bij slootonderhoud: maaisel direct opvangen tijdens het maaien van talud en waterlijn.",
    "Maaikorf voor slootonderhoud",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Slootonderhoud", None)],
    "Bij professioneel slootonderhoud wordt de maaikorf gebruikt om het talud en de waterlijn te maaien zonder dat het maaisel in de sloot terechtkomt. Dat voorkomt verstopping van de waterafvoer en houdt de watergang schoon in één werkgang met het maaien zelf.",
    fact="Bij slootonderhoud wordt de maaikorf ingezet zodra maaisel niet in het water mag achterblijven. De korf maait en vangt de vegetatie tegelijk op, zodat een aparte werkgang om het maaisel achteraf te verwijderen niet nodig is.",
    sections=[
        h2("Eén werkgang",
           p("Doordat maaien en opvangen tegelijk gebeuren, hoeft het maaisel niet achteraf handmatig uit het water gehaald te worden — dat scheelt een aparte werkgang en voorkomt verstopping van de waterafvoer. Dit is met name relevant voor waterschappen en aannemers die volgens een vast onderhoudsschema werken.")),
        h2("Combinatie met een maaiarm",
           p("De korf wordt gemonteerd aan het uiteinde van een "+a("maaiarm","/maaiarm/slootonderhoud/")+", die vanaf de kant het talud en de waterlijn bereikt zonder dat de oever betreden hoeft te worden.")),
    ],
    machines=("Relevante machine voor slootonderhoud", [
        card("herder-maaikorf"),
    ]),
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaikorf bij slootonderhoud (slootcluster)","/slootonderhoud/maaikorf/"),("Maaikorf voor watergangen","/maaikorf/voor-watergangen/")],
)

# ===========================================================================
add(
    "/maaikorf/voor-maaiarm/",
    "Maaikorf voor maaiarm | Wim van Breda",
    "Maaikorf als aanbouwdeel op een maaiarm: maaien en opvangen van maaisel in één beweging.",
    "Maaikorf voor maaiarm",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Voor maaiarm", None)],
    "De maaikorf wordt gemonteerd aan het uiteinde van een maaiarm, op de plek waar normaal een klepelkop of messenbalk zit, zodat de bestuurder vanuit de cabine kan maaien én tegelijk het maaisel opvangen. Deze combinatie is de gangbare oplossing bij sloot- en watergangonderhoud.",
    fact="Een maaikorf vervangt de klepelkop aan het uiteinde van een maaiarm zodra vegetatie tijdens het maaien direct opgevangen moet worden in plaats van verkleind te blijven liggen — de rest van de bediening (bereik, maaihoogte) verloopt via dezelfde maaiarm.",
    sections=[
        h2("Combinatie met de arm",
           p("Het gewicht en de aansturing van de korf moeten passen bij de hydrauliek van de maaiarm; Wim van Breda adviseert welke combinatie van "+a("maaiarm","/maaiarm/")+" en maaikorf geschikt is voor uw tractor. De "+a("Herder maaikorf","/machine/herder-maaikorf/")+" is bijvoorbeeld ontwikkeld om eenvoudig te monteren te zijn aan een maaiarm of giek.")),
    ],
    machines=("Maaikorf voor op de maaiarm", [
        card("herder-maaikorf"),
    ]),
    related=[("Maaiarm","/maaiarm/"),("Maaikorf","/maaikorf/"),("Maaikorf kopen","/maaikorf/kopen/")],
)

# ===========================================================================
add(
    "/maaikorf/voor-watergangen/",
    "Maaikorf voor watergangen | Wim van Breda",
    "Maaikorf voor het onderhoud van watergangen: maaisel opvangen zodat het niet in het water terechtkomt.",
    "Maaikorf voor watergangen",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Voor watergangen", None)],
    "Bij watergangen die vrij van maaisel moeten blijven — bijvoorbeeld voor de waterafvoer of waterkwaliteit — is de maaikorf het aangewezen aanbouwdeel om tijdens het maaien direct op te vangen. Waterschappen en aannemers gebruiken de maaikorf om aan die eis te voldoen.",
    fact="Watergangen waarvan de doorstroming en waterkwaliteit gewaarborgd moeten blijven, mogen doorgaans geen achtergebleven maaisel bevatten; een maaikorf voorkomt dat door vegetatie tijdens het maaien direct op te vangen in plaats van het te laten liggen.",
    sections=[
        h2("Voor waterschappen en aannemers",
           p("Waterschappen en aannemers die in opdracht van waterschappen werken, gebruiken de maaikorf om te voldoen aan de eis dat maaisel uit de watergang wordt gehouden. De "+a("Herder maaikorf","/machine/herder-maaikorf/")+" is hier specifiek voor ontworpen, met een open korfontwerp dat overtollig water direct laat wegstromen.")),
    ],
    machines=("Relevante machine voor watergangen", [
        card("herder-maaikorf"),
    ]),
    related=[("Maaikorf","/maaikorf/"),("Slootonderhoud","/slootonderhoud/"),("Maaikorf bij slootonderhoud","/maaikorf/slootonderhoud/")],
)

# ===========================================================================
add(
    "/maaikorf/voor-tractor/",
    "Maaikorf voor tractor | Wim van Breda",
    "Maaikorf op tractor via maaiarm: opvang van maaisel bij sloot- en bermonderhoud vanaf de tractor.",
    "Maaikorf voor tractor",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Voor tractor", None)],
    "Een maaikorf werkt altijd in combinatie met een maaiarm op de tractor: de tractor levert de hydrauliek en voortbeweging, de arm het bereik, en de korf de opvang van het maaisel. Welke tractor geschikt is, hangt af van de maaiarm waarop de korf gemonteerd wordt.",
    fact="Een maaikorf is nooit een op zichzelf staand aanbouwdeel voor een tractor: hij wordt altijd gecombineerd met een maaiarm, waarvan het gewicht en bereik bepalen welke tractor geschikt is.",
    sections=[
        h2("Geschikte tractoren",
           p("Zie onze pagina over "+a("maaiarm voor tractor","/maaiarm/voor-tractor/")+" voor de gangbare gewichtsklassen: compacte maaiarmen zijn al mogelijk vanaf circa 3.000 kg tractorgewicht, zwaardere uitvoeringen vragen meer.")),
    ],
    related=[("Maaikorf","/maaikorf/"),("Maaiarm voor tractor","/maaiarm/voor-tractor/"),("Maaikorf voor maaiarm","/maaikorf/voor-maaiarm/")],
)

# ===========================================================================
add(
    "/maaikorf/herder/",
    "Herder maaikorf | Wim van Breda",
    "Herder maaikorf bij Wim van Breda: aanbouwdeel op Herder-maaiarmen voor sloot- en watergangonderhoud.",
    "Herder maaikorf",
    [("Home", HOME), ("Maaikorf", "/maaikorf/"), ("Herder", None)],
    "Herder levert naast maaiarmen ook een maaikorf, ontwikkeld om als aanbouwdeel op maaiarmen gemonteerd te worden voor sloot- en watergangonderhoud. Wim van Breda levert deze Herder maaikorf inclusief montage en service.",
    fact="De Herder maaikorf is gemaakt van hoogwaardige materialen die bestand zijn tegen intensief gebruik in natte omstandigheden, met messen van gehard staal voor een scherpe snede en een open korfontwerp dat verstoppingen voorkomt.",
    sections=[
        h2("Eigenschappen van de Herder maaikorf",
           ul([
               "Messen van gehard staal voor een scherpe snede",
               "Open korfontwerp voorkomt verstoppingen",
               "Geschikt voor maaien boven én onder water",
               "Leverbaar in diverse werkbreedtes en uitvoeringen",
               "Uitwisselbaar tussen verschillende Herder-machines",
           ])),
        h2("In combinatie met de Herder-maaiarm",
           p("De maaikorf is ontworpen om te combineren met "+a("Herder-maaiarmen","/maaiarm/herder/")+" zoals de Grenadier, en wordt gebruikt voor het maaien van riet en grasbegroeiing, onderhoud van sloten en watergangen, oeverbeheer en natuurvriendelijk slootonderhoud.")),
    ],
    machines=("Herder maaikorf", [
        card("herder-maaikorf"),
    ]),
    related=[("Maaikorf","/maaikorf/"),("Herder maaiarm","/maaiarm/herder/"),("Maaikorf voor watergangen","/maaikorf/voor-watergangen/"),
             ("Herder (merkpagina)","/herder/maaikorf/")],
)
