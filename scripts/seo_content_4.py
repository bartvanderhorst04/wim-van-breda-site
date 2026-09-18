# -*- coding: utf-8 -*-
"""Inhoud cluster 5: bermonderhoud + slootonderhoud + taludmaaien."""
from build_seo_pages import h2, h3, p, ul, a

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related, fact=fact))

# ===========================================================================
# 5. BERM- EN SLOOTONDERHOUD
# ===========================================================================
add(
    "/bermonderhoud/",
    "Bermonderhoud | Wim van Breda",
    "Professioneel bermonderhoud: machines, methode en advies voor gemeenten, waterschappen en aannemers. Vanuit Geldermalsen.",
    "Bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", None)],
    "Bermonderhoud omvat het periodiek maaien, snoeien en schonen van de berm langs wegen, dijken en watergangen, met als doel verkeersveiligheid, doorstroming van water en (steeds vaker) biodiversiteit.",
    sections=[
        h2("Wat bermonderhoud inhoudt",
           p("Naast maaien hoort hier ook het verwijderen van opslag (jonge bomen en struiken), het schoonhouden van bermsloten en het snoeien van beplanting die het zicht op de weg belemmert bij. De werkzaamheden gebeuren doorgaans meerdere keren per seizoen, volgens een vast beheerschema van de opdrachtgever.")),
        h2("Machines voor bermonderhoud",
           p("Voor rechte, goed bereikbare bermtrajecten wordt vaak een "+a("klepelmaaier","/bermonderhoud/klepelmaaier/")+" ingezet; bij hoogteverschil, sloten of obstakels is een "+a("maaiarm","/bermonderhoud/maaiarm/")+" met groter bereik praktischer.")),
        h2("Ecologisch bermbeheer",
           p("Steeds meer gemeenten en waterschappen voeren een "+a("ecologisch maaibeleid","/bermonderhoud/ecologisch/")+" voor hun bermen, gericht op meer biodiversiteit.")),
    ],
    faq=[
        ("Hoe vaak moet een berm gemaaid worden?",
         "Dat verschilt per beheerschema van de opdrachtgever en het type berm: verkeersveilige bermen worden vaak meerdere keren per seizoen gemaaid, ecologisch beheerde bermen doorgaans minder frequent en gefaseerd."),
        ("Welke machine is geschikt voor bermonderhoud?",
         "Voor rechte, vlakke trajecten volstaat vaak een klepelmaaier; bij hoogteverschil, sloten of obstakels is een maaiarm met groter bereik de gangbare keuze."),
    ],
    related=[("Machines voor bermonderhoud","/bermonderhoud/machines/"),("Maaiarm voor bermonderhoud","/bermonderhoud/maaiarm/"),
             ("Klepelmaaier voor bermonderhoud","/bermonderhoud/klepelmaaier/"),("Ecologisch bermonderhoud","/bermonderhoud/ecologisch/"),
             ("Slootonderhoud","/slootonderhoud/"),("Taludmaaien","/taludmaaien/")],
)

add(
    "/bermonderhoud/machines/",
    "Machines voor bermonderhoud | Wim van Breda",
    "Welke machines voor bermonderhoud geschikt zijn: klepelmaaiers, maaiarmen en werktuigdragers, per situatie toegelicht.",
    "Machines voor bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Machines", None)],
    "Voor bermonderhoud gebruikt Wim van Breda vooral drie type machines: klepelmaaiers voor open, vlakke trajecten, maaiarmen voor bereik over taluds en obstakels, en werktuigdragers als compact platform voor meerdere werktuigen.",
    sections=[
        h2("Klepelmaaier",
           p(a("Klepelmaaiers","/klepelmaaier/")+" verkleinen gras en dunne opslag en zijn robuust tegen obstakels in de berm.")),
        h2("Maaiarm",
           p(a("Maaiarmen","/maaiarm/")+" reiken zijwaarts en over hoogteverschil, praktisch bij sloten, taluds en obstakels als verkeersborden.")),
        h2("Werktuigdrager",
           p("Een "+a("werktuigdrager","/werktuigdrager/bermonderhoud/")+" is een compact platform waarop meerdere werktuigen gemonteerd kunnen worden, handig voor gevarieerd bermwerk op kleinere schaal.")),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Maaiarm","/maaiarm/"),("Klepelmaaier","/klepelmaaier/"),("Werktuigdrager","/werktuigdrager/")],
)

add(
    "/bermonderhoud/maaiarm/",
    "Maaiarm bij bermonderhoud | Wim van Breda",
    "Maaiarm inzetten voor bermonderhoud: bereik over taluds, sloten en obstakels heen, vanuit de tractorcabine bediend.",
    "Maaiarm bij bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Maaiarm", None)],
    "Zodra een bermtraject hoogteverschil, een sloot of veel obstakels bevat, is een maaiarm de praktische keuze: de arm reikt zijwaarts en kan om hindernissen heen sturen zonder dat de tractor hoeft te verplaatsen.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg over maaiarmen, merken en armlengtes: "+a("maaiarm","/maaiarm/")+" en "+a("maaiarm voor bermonderhoud","/maaiarm/bermonderhoud/")+".")),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Maaiarm","/maaiarm/"),("Maaiarm voor bermonderhoud (detail)","/maaiarm/bermonderhoud/")],
)

add(
    "/bermonderhoud/klepelmaaier/",
    "Klepelmaaier bij bermonderhoud | Wim van Breda",
    "Wanneer een klepelmaaier de beste keuze is voor bermonderhoud, en hoe deze zich verhoudt tot een maaiarm.",
    "Klepelmaaier bij bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Klepelmaaier", None)],
    "Voor open, relatief vlakke bermtrajecten is een klepelmaaier vaak de meest efficiënte keuze: de scharnierende messen verkleinen gras en opslag in één werkgang.",
    sections=[
        h2("Zie ook",
           p("Voor merken, uitvoeringen en de volledige uitleg: "+a("klepelmaaier","/klepelmaaier/")+" en "+a("klepelmaaier voor bermonderhoud","/klepelmaaier/bermonderhoud/")+".")),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier voor bermonderhoud (detail)","/klepelmaaier/bermonderhoud/")],
)

add(
    "/bermonderhoud/ecologisch/",
    "Ecologisch bermonderhoud | Wim van Breda",
    "Ecologisch bermonderhoud: gefaseerd maaien en afvoer van maaisel voor meer biodiversiteit in de berm.",
    "Ecologisch bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Ecologisch", None)],
    "Ecologisch bermonderhoud past de reguliere maaimethode aan op biodiversiteit: gefaseerd maaien, hogere maaihoogte en het afvoeren van maaisel om de bodem te verschralen.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg: "+a("ecologisch bermbeheer","/ecologisch-bermbeheer/")+" en "+a("ecologisch maaien","/ecologisch-maaien/")+".")),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/"),("Ecologisch maaien","/ecologisch-maaien/")],
)

add(
    "/slootonderhoud/",
    "Slootonderhoud | Wim van Breda",
    "Professioneel slootonderhoud: talud en waterlijn maaien en schonen, met maaiarm en maaikorf. Advies en machines uit Geldermalsen.",
    "Slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", None)],
    "Slootonderhoud omvat het maaien van het talud en de waterlijn en het schonen van de sloot, met als doel een goede waterafvoer en een begaanbare oever te behouden.",
    sections=[
        h2("Talud en waterlijn",
           p("Het talud wordt gemaaid om begroeiing kort te houden en de oever stabiel te laten; de waterlijn en soms de bodem van de sloot worden geschoond zodat water goed kan afstromen.")),
        h2("Machines voor slootonderhoud",
           p("De meeste sloten worden onderhouden met een "+a("maaiarm","/slootonderhoud/maaiarm/")+" vanaf de kant, eventueel met een "+a("maaikorf","/slootonderhoud/maaikorf/")+" om het maaisel direct op te vangen in plaats van het in het water te laten.")),
    ],
    faq=[
        ("Hoe vaak moet een sloot gemaaid worden?",
         "Dat hangt af van het beheerschema van het waterschap of de eigenaar en de groeisnelheid van de vegetatie; veel sloten worden één tot enkele keren per seizoen gemaaid."),
        ("Moet maaisel uit de sloot verwijderd worden?",
         "Bij veel watergangen wel, om verstopping van de waterafvoer en overmatige voedingsstoffen in het water te voorkomen — daarvoor wordt een maaikorf gebruikt."),
    ],
    related=[("Machines voor slootonderhoud","/slootonderhoud/machines/"),("Maaiarm voor slootonderhoud","/slootonderhoud/maaiarm/"),
             ("Maaikorf voor slootonderhoud","/slootonderhoud/maaikorf/"),("Bermonderhoud","/bermonderhoud/"),("Taludmaaien","/taludmaaien/")],
)

add(
    "/slootonderhoud/machines/",
    "Machines voor slootonderhoud | Wim van Breda",
    "Welke machines voor slootonderhoud geschikt zijn: maaiarm met maaikorf voor talud en waterlijn.",
    "Machines voor slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", "/slootonderhoud/"), ("Machines", None)],
    "Voor slootonderhoud is de combinatie van maaiarm en maaikorf de gangbare oplossing: de arm reikt vanaf de kant tot in de sloot, de korf vangt het maaisel op.",
    sections=[
        h2("Zie ook",
           p(a("Maaiarm","/maaiarm/")+" en "+a("maaikorf","/maaikorf/")+" voor de volledige uitleg over merken en uitvoeringen.")),
    ],
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaiarm","/maaiarm/"),("Maaikorf","/maaikorf/")],
)

add(
    "/slootonderhoud/maaiarm/",
    "Maaiarm bij slootonderhoud | Wim van Breda",
    "Maaiarm voor het maaien van talud en waterlijn bij slootonderhoud, bediend vanaf de kant.",
    "Maaiarm bij slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", "/slootonderhoud/"), ("Maaiarm", None)],
    "De maaiarm maait het talud en de waterlijn van de sloot vanaf de kant, zodat de oever niet betreden hoeft te worden.",
    sections=[
        h2("Zie ook",
           p("Voor merken en armlengtes: "+a("maaiarm","/maaiarm/")+" en "+a("maaiarm voor slootonderhoud","/maaiarm/slootonderhoud/")+".")),
    ],
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaiarm","/maaiarm/"),("Maaiarm voor slootonderhoud (detail)","/maaiarm/slootonderhoud/")],
)

add(
    "/slootonderhoud/maaikorf/",
    "Maaikorf bij slootonderhoud | Wim van Breda",
    "Maaikorf voor slootonderhoud: maaisel direct opvangen tijdens het maaien van de waterlijn.",
    "Maaikorf bij slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", "/slootonderhoud/"), ("Maaikorf", None)],
    "Waar maaisel niet in de sloot mag achterblijven, wordt de maaikorf gebruikt om het materiaal tijdens het maaien direct op te vangen.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg: "+a("maaikorf","/maaikorf/")+" en "+a("maaikorf voor slootonderhoud","/maaikorf/slootonderhoud/")+".")),
    ],
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaikorf","/maaikorf/"),("Maaikorf voor watergangen","/maaikorf/voor-watergangen/")],
)

add(
    "/taludmaaien/",
    "Taludmaaien | Wim van Breda",
    "Taludmaaien: machines voor het maaien van hellingen langs dijken, sloten en wegen, veilig vanaf de kant of op afstand bestuurd.",
    "Taludmaaien",
    [("Home", HOME), ("Taludmaaien", None)],
    "Taludmaaien is het maaien van hellende oevers en dijken, waarbij veiligheid en bereik de belangrijkste aandachtspunten zijn: de bestuurder blijft bovenaan, de machine werkt de helling af.",
    sections=[
        h2("Hoe taluds gemaaid worden",
           p("Voor de meeste taluds volstaat een "+a("maaiarm","/maaiarm/")+" die vanaf de kant naar beneden reikt. Op zeer steile of gevaarlijke taluds levert Wim van Breda ook radiografisch bestuurbare maaimachines van MowHawk, waarbij de bestuurder niet in de machine zit maar de maaier op afstand aanstuurt.")),
        h2("Zie ook",
           p("Voor de bijbehorende machines: "+a("taludonderhoud-machines","/taludonderhoud-machines/")+".")),
    ],
    related=[("Taludonderhoud-machines","/taludonderhoud-machines/"),("Maaiarm","/maaiarm/"),("Bermonderhoud","/bermonderhoud/")],
)

add(
    "/taludonderhoud-machines/",
    "Taludonderhoud machines | Wim van Breda",
    "Machines voor taludonderhoud: maaiarmen en op afstand bestuurde maaimachines voor hellingen en dijken.",
    "Machines voor taludonderhoud",
    [("Home", HOME), ("Taludonderhoud machines", None)],
    "Voor taludonderhoud levert Wim van Breda maaiarmen die vanaf de kant een helling af kunnen maaien, en op afstand bestuurbare maaimachines voor de steilste of minst toegankelijke taluds.",
    sections=[
        h2("Maaiarm vanaf de kant",
           p(a("Maaiarmen","/maaiarm/")+" zijn de gangbare oplossing voor de meeste taluds langs dijken, sloten en wegen.")),
        h2("Op afstand bestuurd voor steile taluds",
           p("Voor taluds die te steil of te gevaarlijk zijn om vanaf de kant te bereiken, levert Wim van Breda radiografisch bestuurbare maaimachines van MowHawk.")),
    ],
    related=[("Taludmaaien","/taludmaaien/"),("Maaiarm","/maaiarm/"),("Bermonderhoud","/bermonderhoud/")],
)
