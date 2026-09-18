# -*- coding: utf-8 -*-
"""Inhoud cluster 4-5: ecologisch maaien/bermbeheer + bermonderhoud/slootonderhoud/taludmaaien (16 pagina's, uitgebreide versie)."""
from build_seo_pages import h2, h3, p, ul, a
from machine_data import card

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None, machines=None, cta=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related,
                       fact=fact, machines=machines, cta=cta))

# ===========================================================================
# ECOLOGISCH MAAIEN
# ===========================================================================
add(
    "/ecologisch-maaien/",
    "Ecologisch maaien: machines en advies | Wim van Breda",
    "Ecologisch maaien: gefaseerd maaien en aangepaste maaihoogte voor natuurvriendelijk beheer van bermen en groenstroken.",
    "Ecologisch maaien",
    [("Home", HOME), ("Ecologisch maaien", None)],
    "Ecologisch maaien is een maaimethode die rekening houdt met flora en fauna: gefaseerd maaien, een aangepaste maaihoogte en het afvoeren van maaisel om de bodem te verschralen, in plaats van een terrein in één keer volledig kort te maaien. Steeds meer gemeenten, waterschappen en terreinbeheerders passen deze werkwijze toe binnen hun groenbeleid.",
    fact="Bij ecologisch maaien wordt niet het hele terrein in één beurt gemaaid: een deel van de vegetatie blijft steeds staan als schuil- en voedselplek voor insecten en kleine dieren, de maaihoogte ligt vaak hoger dan bij regulier maaiwerk, en maaisel wordt regelmatig afgevoerd om de bodem te verschralen.",
    sections=[
        h2("Wat ecologisch maaien anders maakt dan regulier maaien",
           p("Bij regulier maaiwerk ligt de nadruk op een strak, kort resultaat, vaak in één of enkele maaibeurten per seizoen. Bij ecologisch maaien is het doel juist het behoud en de versterking van biodiversiteit: door gefaseerd te maaien blijft er altijd een deel van de vegetatie staan, en door de maaihoogte te verhogen krijgen bloeiende planten en insecten meer kans.")),
        h2("Machines voor ecologisch maaien",
           p("De machines die hiervoor gebruikt worden zijn dezelfde als bij regulier beheer — "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("maaiarmen","/maaiarm/")+" — maar worden ingezet volgens een ecologisch maaischema en vaak in combinatie met opvang van maaisel. Zie onze pagina over "+a("machines voor ecologisch maaien","/ecologisch-maaien/machines/")+" voor de precieze uitleg per machinetype.")),
        h2("Ecologisch bermmaaien en maaien met afvoer",
           p("Binnen ecologisch maaien zijn twee specifieke toepassingen te onderscheiden: "+a("ecologisch bermmaaien","/ecologisch-maaien/bermmaaien/")+", gericht op de gefaseerde aanpak van wegbermen, en "+a("maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/")+", waarbij het maaisel bewust wordt afgevoerd om de bodem te verschralen. Zie ook onze bredere pagina over "+a("ecologisch bermbeheer","/ecologisch-bermbeheer/")+" voor de samenhang tussen beleid en uitvoering.")),
        h2("Voor wie ecologisch maaien relevant is",
           p("Gemeenten, waterschappen en terreinbeheerders die natuurvriendelijk bermbeheer voeren, vaak in het kader van biodiversiteitsbeleid, en de loonbedrijven en aannemers die dat beleid in de praktijk uitvoeren.")),
    ],
    faq=[
        ("Wat is het verschil tussen ecologisch maaien en gewoon maaien?",
         "Bij ecologisch maaien wordt gefaseerd gemaaid (niet alles tegelijk), ligt de maaihoogte vaak hoger en wordt maaisel regelmatig afgevoerd om de bodem te verschralen — met als doel meer ruimte voor flora en fauna."),
        ("Is er speciale apparatuur nodig voor ecologisch maaien?",
         "Niet per se: dezelfde klepelmaaiers en maaiarmen die voor regulier bermbeheer worden gebruikt, zijn ook geschikt voor ecologisch maaien; het verschil zit vooral in de werkwijze en planning."),
        ("Wat is het verschil tussen ecologisch maaien en ecologisch bermbeheer?",
         "Ecologisch maaien beschrijft de maaimethode zelf; ecologisch bermbeheer is het bredere beleid en beheer van de berm als geheel, waar ecologisch maaien een onderdeel van is. Zie "+a("ecologisch bermbeheer","/ecologisch-bermbeheer/")+"."),
        ("Wat is maaien met afvoer?",
         "Het bewust afvoeren van maaisel na het maaien, in plaats van het te laten liggen, om de bodem te verschralen en kruidenrijke vegetatie een kans te geven. Zie "+a("maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/")+"."),
    ],
    related=[("Machines voor ecologisch maaien","/ecologisch-maaien/machines/"),("Ecologisch bermmaaien","/ecologisch-maaien/bermmaaien/"),
             ("Maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/"),("Bermonderhoud","/bermonderhoud/")],
)

# ===========================================================================
add(
    "/ecologisch-maaien/machines/",
    "Machines voor ecologisch maaien | Wim van Breda",
    "Welke machines geschikt zijn voor ecologisch maaien: klepelmaaiers en maaiarmen, ingezet volgens een natuurvriendelijk maaischema.",
    "Machines voor ecologisch maaien",
    [("Home", HOME), ("Ecologisch maaien", "/ecologisch-maaien/"), ("Machines", None)],
    "Voor ecologisch maaien zijn geen aparte machines nodig: het gaat om dezelfde klepelmaaiers en maaiarmen die ook voor regulier bermbeheer worden ingezet, gecombineerd met een ecologisch maaischema en, waar nodig, opvang van maaisel.",
    fact="De machinekeuze bij ecologisch maaien wordt niet bepaald door het ecologische doel zelf, maar door het terrein en de gewenste afvoer: een klepelmaaier voor open, gefaseerd te maaien vlakken, een maaiarm zodra er hoogteverschil of obstakels zijn, en een maai-laadcombinatie waar maaisel direct moet worden afgevoerd.",
    sections=[
        h2("Klepelmaaier of maaiarm",
           p("Een "+a("klepelmaaier","/klepelmaaier/")+" is geschikt voor open, gefaseerd te maaien vlakken zoals bermstroken en graslanden; een "+a("maaiarm","/maaiarm/")+" wordt ingezet zodra er hoogteverschil, sloten of obstakels in het traject zitten. Beide worden bij ecologisch maaien niet anders bediend dan bij regulier werk — het verschil zit in wanneer en hoeveel er gemaaid wordt.")),
        h2("Opvang van maaisel",
           p("Waar maaisel afgevoerd moet worden om de bodem te verschralen, wordt vaak een maaikorf of een maai-laadcombinatie ingezet. Een voorbeeld is de "+a("Omarv Venezia L","/machine/omarv-venezia-l-professionele-maai-laad-combinatie/")+", die maaien, verkleinen en opvangen in één werkgang combineert — zie ook "+a("maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/")+".")),
    ],
    machines=("Relevante machine voor maaien met afvoer", [
        card("omarv-venezia-l-professionele-maai-laad-combinatie"),
    ]),
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Klepelmaaier","/klepelmaaier/"),("Maaiarm","/maaiarm/")],
)

# ===========================================================================
add(
    "/ecologisch-maaien/bermmaaien/",
    "Ecologisch bermmaaien | Wim van Breda",
    "Ecologisch bermmaaien: gefaseerd en natuurvriendelijk onderhoud van wegbermen, met aandacht voor biodiversiteit.",
    "Ecologisch bermmaaien",
    [("Home", HOME), ("Ecologisch maaien", "/ecologisch-maaien/"), ("Bermmaaien", None)],
    "Ecologisch bermmaaien is de toepassing van ecologisch maaien specifiek op wegbermen: gefaseerd maaien, een deel van de berm laten staan en de maaihoogte aanpassen aan de vegetatie, in plaats van de volledige berm in één beurt kort te maaien.",
    fact="Bij ecologisch bermmaaien wordt een bermtraject vaak in stroken of vakken verdeeld, waarbij per maaironde een ander deel wordt gemaaid — zo blijft er altijd bloeiende of hogere vegetatie beschikbaar voor insecten, ongeacht het moment in het seizoen.",
    sections=[
        h2("In de praktijk",
           p("Gemeenten passen dit vaak toe langs wegbermen met kruidenrijke vegetatie, waarbij per seizoen wisselend een deel van het traject gemaaid wordt in plaats van de volledige berm in één beurt. Dat vraagt om nauwkeurige planning, maar geen andere machines dan regulier bermonderhoud.")),
        h2("Verschil met regulier bermonderhoud",
           p("Regulier "+a("bermonderhoud","/bermonderhoud/")+" richt zich primair op verkeersveiligheid en doorstroming en maait doorgaans het hele traject in één keer. Ecologisch bermmaaien voegt daar een gefaseerde, op biodiversiteit gerichte aanpak aan toe, vaak in overleg met de ecoloog van de opdrachtgever.")),
    ],
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/"),("Bermonderhoud ecologisch","/bermonderhoud/ecologisch/")],
)

# ===========================================================================
add(
    "/ecologisch-maaien/maaien-met-afvoer/",
    "Maaien met afvoer | Wim van Breda",
    "Maaien met afvoer van maaisel: verschraling van de bodem als onderdeel van ecologisch bermbeheer.",
    "Maaien met afvoer",
    [("Home", HOME), ("Ecologisch maaien", "/ecologisch-maaien/"), ("Maaien met afvoer", None)],
    "Bij maaien met afvoer wordt het maaisel na het maaien opgeraapt en afgevoerd in plaats van dat het blijft liggen, met als doel de bodem te verschralen en meer ruimte te geven aan kruidenrijke vegetatie in plaats van snelgroeiend gras.",
    fact="Blijft maaisel liggen, dan verteert het en verrijkt het de bodem, waardoor grassen op termijn de overhand krijgen boven kruiden en bloemen. Maaien met afvoer voorkomt dat door het materiaal direct te verwijderen in plaats van het te laten composteren op het terrein zelf.",
    sections=[
        h2("Waarom afvoeren",
           p("Een voedselrijke bodem bevoordeelt snelgroeiende grassoorten boven bloeiende kruiden. Door maaisel structureel af te voeren, daalt de voedselrijkdom van de bodem geleidelijk, wat op termijn ruimte geeft aan een gevarieerdere, kruidenrijke vegetatie.")),
        h2("Uitvoering",
           p("Dit kan met een maai-laadcombinatie die maait en tegelijk opzuigt, zoals de "+a("Omarv Venezia L","/machine/omarv-venezia-l-professionele-maai-laad-combinatie/")+" met een opvangbak van 10 m³, of met een "+a("maaikorf","/maaikorf/")+" op een maaiarm die het materiaal direct meeneemt bij werk langs water.")),
    ],
    machines=("Relevante machine voor maaien met afvoer", [
        card("omarv-venezia-l-professionele-maai-laad-combinatie"),
    ]),
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Maaikorf","/maaikorf/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/")],
)

# ===========================================================================
add(
    "/ecologisch-bermbeheer/",
    "Ecologisch bermbeheer | Machines & advies | Wim van Breda",
    "Ecologisch bermbeheer: natuurvriendelijk onderhoud van bermen gericht op biodiversiteit, met passende machines en maaimethode.",
    "Ecologisch bermbeheer",
    [("Home", HOME), ("Ecologisch bermbeheer", None)],
    "Ecologisch bermbeheer is het bredere beheer van de berm als geheel met behoud en versterking van de biodiversiteit als uitgangspunt: niet alleen de maaimethode, maar ook planning, maaifrequentie en de omgang met maaisel. Wim van Breda levert de machines waarmee dit beheer in de praktijk wordt uitgevoerd.",
    fact="Ecologisch bermbeheer omvat het volledige beheerproces van een berm met natuurwaarde: van het opstellen van een maaischema en het bepalen van maaifrequentie tot de daadwerkelijke uitvoering met gefaseerd maaien en afvoer van maaisel — ecologisch maaien is daarbinnen de uitvoerende maaimethode.",
    sections=[
        h2("Beleid en uitvoering samen",
           p("Veel gemeenten en waterschappen hebben inmiddels een ecologisch maaibeleid voor hun bermen, waarin is vastgelegd hoe vaak en op welke manier gemaaid wordt. De uitvoering vraagt dezelfde soort machines als regulier bermonderhoud — "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("maaiarmen","/maaiarm/")+" — maar ingezet volgens het ecologische maaischema van de opdrachtgever, met "+a("ecologisch bermmaaien","/ecologisch-maaien/bermmaaien/")+" en "+a("maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/")+" als concrete onderdelen daarvan.")),
        h2("Verschil met ecologisch maaien",
           p("Waar "+a("ecologisch maaien","/ecologisch-maaien/")+" de maaimethode beschrijft, gaat ecologisch bermbeheer over het geheel: welke stukken berm wanneer worden gemaaid, met welke frequentie, en hoe wordt omgegaan met maaisel en opslag door het hele seizoen heen.")),
        h2("Wim van Breda in de praktijk",
           p("Wim van Breda levert en onderhoudt de machines die loonbedrijven en aannemers gebruiken om ecologisch bermbeheer uit te voeren, vanuit Geldermalsen, en adviseert over welke combinatie van machines past bij een specifiek maaischema.")),
    ],
    faq=[
        ("Wat is ecologisch bermbeheer?",
         "Het beheer van een berm met natuurwaarde als uitgangspunt: planning, maaifrequentie en de omgang met maaisel, gericht op behoud en versterking van biodiversiteit."),
        ("Is ecologisch bermbeheer hetzelfde als ecologisch maaien?",
         "Niet precies: ecologisch maaien is de maaimethode, ecologisch bermbeheer is het bredere beheer van de berm als geheel waar die methode onderdeel van is."),
        ("Welke machines zijn nodig voor ecologisch bermbeheer?",
         "Dezelfde klepelmaaiers en maaiarmen als bij regulier bermonderhoud, ingezet volgens het ecologische maaischema van de opdrachtgever."),
    ],
    related=[("Ecologisch maaien","/ecologisch-maaien/"),("Ecologisch bermmaaien","/ecologisch-maaien/bermmaaien/"),
             ("Bermonderhoud ecologisch","/bermonderhoud/ecologisch/"),("Bermonderhoud","/bermonderhoud/")],
)

# ===========================================================================
# BERM- EN SLOOTONDERHOUD
# ===========================================================================
add(
    "/bermonderhoud/",
    "Bermonderhoud: machines en advies | Wim van Breda",
    "Professioneel bermonderhoud: machines, methode en advies voor gemeenten, waterschappen en aannemers. Vanuit Geldermalsen.",
    "Bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", None)],
    "Bermonderhoud omvat het periodiek maaien, snoeien en schonen van de berm langs wegen, dijken en watergangen, met als doel verkeersveiligheid, doorstroming van water en, steeds vaker, biodiversiteit. Wim van Breda levert de maaiarmen, klepelmaaiers en werktuigdragers waarmee dit werk wordt uitgevoerd.",
    fact="Bermonderhoud bestaat uit het maaien van gras en vegetatie, het verwijderen van opslag zoals jonge bomen en struiken, en het schoonhouden van bermsloten, meestal meerdere keren per seizoen volgens een vast beheerschema van de opdrachtgever.",
    sections=[
        h2("Wat bermonderhoud inhoudt",
           p("Naast maaien hoort hier ook het verwijderen van opslag, het schoonhouden van bermsloten en het snoeien van beplanting die het zicht op de weg belemmert bij. De werkzaamheden gebeuren doorgaans meerdere keren per seizoen, volgens een vast beheerschema van de opdrachtgever.")),
        h2("Machines voor bermonderhoud",
           p("Voor rechte, goed bereikbare bermtrajecten wordt vaak een "+a("klepelmaaier","/bermonderhoud/klepelmaaier/")+" ingezet; bij hoogteverschil, sloten of obstakels is een "+a("maaiarm","/bermonderhoud/maaiarm/")+" met groter bereik praktischer. Zie ook de bredere pagina "+a("machines voor bermonderhoud","/bermonderhoud/machines/")+".")),
        h2("Welke machine past bij welk bermtraject?",
           ul([
               "Rechte, vlakke berm zonder obstakels — klepelmaaier als zijmaaier",
               "Berm met hoogteverschil, sloot of obstakels — maaiarm met klepelkop of messenbalk",
               "Berm met vegetatie tot in de watergang — maaiarm met maaikorf",
               "Kleinschalig of moeilijk bereikbaar werk — werktuigdrager",
           ])),
        h2("Ecologisch bermbeheer",
           p("Steeds meer gemeenten en waterschappen voeren een "+a("ecologisch maaibeleid","/bermonderhoud/ecologisch/")+" voor hun bermen, gericht op meer biodiversiteit naast de gebruikelijke verkeersveiligheid.")),
        h2("Wie voert bermonderhoud uit",
           p("Bermonderhoud wordt uitgevoerd door loonbedrijven in opdracht van gemeenten en provincies, door de eigen buitendienst van gemeenten, en door waterschappen en hun aannemers waar bermen grenzen aan watergangen.")),
    ],
    faq=[
        ("Hoe vaak moet een berm gemaaid worden?",
         "Dat verschilt per beheerschema van de opdrachtgever en het type berm: verkeersveilige bermen worden vaak meerdere keren per seizoen gemaaid, ecologisch beheerde bermen doorgaans minder frequent en gefaseerd."),
        ("Welke machine is geschikt voor bermonderhoud?",
         "Voor rechte, vlakke trajecten volstaat vaak een klepelmaaier; bij hoogteverschil, sloten of obstakels is een maaiarm met groter bereik de gangbare keuze."),
        ("Wat is het verschil tussen bermonderhoud en ecologisch bermbeheer?",
         "Regulier bermonderhoud richt zich vooral op verkeersveiligheid en doorstroming; ecologisch bermbeheer voegt daar gefaseerd maaien en aandacht voor biodiversiteit aan toe. Zie "+a("ecologisch bermbeheer","/ecologisch-bermbeheer/")+"."),
        ("Wie voert bermonderhoud uit?",
         "Vooral loonbedrijven in opdracht van gemeenten en provincies, de eigen buitendienst van gemeenten, en waterschappen met hun aannemers."),
    ],
    related=[("Machines voor bermonderhoud","/bermonderhoud/machines/"),("Maaiarm bij bermonderhoud","/bermonderhoud/maaiarm/"),
             ("Klepelmaaier bij bermonderhoud","/bermonderhoud/klepelmaaier/"),("Ecologisch bermonderhoud","/bermonderhoud/ecologisch/"),
             ("Slootonderhoud","/slootonderhoud/"),("Taludmaaien","/taludmaaien/")],
)

# ===========================================================================
add(
    "/bermonderhoud/machines/",
    "Machines voor bermonderhoud | Wim van Breda",
    "Welke machines voor bermonderhoud geschikt zijn: klepelmaaiers, maaiarmen en werktuigdragers, per situatie toegelicht.",
    "Machines voor bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Machines", None)],
    "Voor bermonderhoud gebruikt Wim van Breda vooral drie soorten machines: klepelmaaiers voor open, vlakke trajecten, maaiarmen voor bereik over taluds en obstakels, en werktuigdragers als compact platform voor meerdere werktuigen.",
    fact="De keuze tussen een klepelmaaier, maaiarm of werktuigdrager voor bermonderhoud hangt vooral af van het reliëf van de berm: vlak en open werkt met een klepelmaaier, hoogteverschil of obstakels vragen om een maaiarm, en kleinschalig of gevarieerd werk leent zich voor een werktuigdrager.",
    sections=[
        h2("Klepelmaaier",
           p(a("Klepelmaaiers","/klepelmaaier/")+" verkleinen gras en dunne opslag en zijn robuust tegen obstakels in de berm; ze worden vooral op rechte, relatief vlakke trajecten ingezet.")),
        h2("Maaiarm",
           p(a("Maaiarmen","/maaiarm/")+" reiken zijwaarts en over hoogteverschil, praktisch bij sloten, taluds en obstakels als verkeersborden. De "+a("Herder Grenadier","/machine/herder-grenadier-maaiarm/")+" is hiervan een voorbeeld met een armlengte tot 8,80 meter.")),
        h2("Werktuigdrager",
           p("Een "+a("werktuigdrager","/werktuigdrager/bermonderhoud/")+" is een compact platform waarop meerdere werktuigen gemonteerd kunnen worden, handig voor gevarieerd bermwerk op kleinere schaal of op locaties die moeilijk bereikbaar zijn voor een grote tractor.")),
    ],
    machines=("Relevante machines voor bermonderhoud", [
        card("herder-grenadier-maaiarm"),
        card("votex-roadflex-klepelmaaier"),
    ]),
    related=[("Bermonderhoud","/bermonderhoud/"),("Maaiarm","/maaiarm/"),("Klepelmaaier","/klepelmaaier/"),("Werktuigdrager","/werktuigdrager/")],
)

# ===========================================================================
add(
    "/bermonderhoud/maaiarm/",
    "Maaiarm bij bermonderhoud | Wim van Breda",
    "Maaiarm inzetten voor bermonderhoud: bereik over taluds, sloten en obstakels heen, vanuit de tractorcabine bediend.",
    "Maaiarm bij bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Maaiarm", None)],
    "Zodra een bermtraject hoogteverschil, een sloot of veel obstakels bevat, is een maaiarm de praktische keuze voor bermonderhoud: de arm reikt zijwaarts en kan om hindernissen heen sturen zonder dat de tractor hoeft te verplaatsen, wat het werk zowel efficiënter als veiliger maakt.",
    fact="Een maaiarm wordt binnen bermonderhoud specifiek ingezet daar waar een vaste zijmaaier tekortschiet: bij taluds, slootkanten en obstakels zoals verkeersborden, lichtmasten en vangrails.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg over maaiarmen, merken en armlengtes: "+a("maaiarm","/maaiarm/")+" en "+a("maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/")+".")),
    ],
    machines=("Relevante machine", [
        card("herder-grenadier-maaiarm"),
    ]),
    related=[("Bermonderhoud","/bermonderhoud/"),("Maaiarm","/maaiarm/"),("Maaiarm bij bermonderhoud (detail)","/maaiarm/bermonderhoud/")],
)

# ===========================================================================
add(
    "/bermonderhoud/klepelmaaier/",
    "Klepelmaaier binnen bermonderhoud | Wim van Breda",
    "Wanneer een klepelmaaier de beste keuze is voor bermonderhoud, en hoe deze zich verhoudt tot een maaiarm.",
    "Klepelmaaier bij bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Klepelmaaier", None)],
    "Voor open, relatief vlakke bermtrajecten is een klepelmaaier vaak de meest efficiënte keuze binnen bermonderhoud: de scharnierende messen verkleinen gras en opslag in één werkgang en zijn robuust tegen obstakels zoals stenen.",
    fact="Een klepelmaaier is binnen bermonderhoud de eerste keus zolang het traject relatief vlak en goed bereikbaar is; zodra er sloten, hoogteverschil of veel obstakels bijkomen, is een maaiarm praktischer.",
    sections=[
        h2("Zie ook",
           p("Voor merken, uitvoeringen en de volledige uitleg: "+a("klepelmaaier","/klepelmaaier/")+" en "+a("klepelmaaier bij bermonderhoud","/klepelmaaier/bermonderhoud/")+".")),
    ],
    machines=("Relevante machine", [
        card("votex-roadflex-klepelmaaier"),
    ]),
    related=[("Bermonderhoud","/bermonderhoud/"),("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier bij bermonderhoud (detail)","/klepelmaaier/bermonderhoud/")],
)

# ===========================================================================
add(
    "/bermonderhoud/ecologisch/",
    "Ecologisch bermonderhoud | Wim van Breda",
    "Ecologisch bermonderhoud: gefaseerd maaien en afvoer van maaisel voor meer biodiversiteit in de berm.",
    "Ecologisch bermonderhoud",
    [("Home", HOME), ("Bermonderhoud", "/bermonderhoud/"), ("Ecologisch", None)],
    "Ecologisch bermonderhoud past de reguliere maaimethode aan op biodiversiteit: gefaseerd maaien, hogere maaihoogte en het afvoeren van maaisel om de bodem te verschralen, als aanvulling op de gebruikelijke aandacht voor verkeersveiligheid.",
    fact="Waar regulier bermonderhoud een traject in één keer maait, verdeelt ecologisch bermonderhoud het werk over meerdere fasen, zodat er altijd vegetatie beschikbaar blijft voor insecten en kleine dieren.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg: "+a("ecologisch bermbeheer","/ecologisch-bermbeheer/")+" en "+a("ecologisch maaien","/ecologisch-maaien/")+".")),
    ],
    related=[("Bermonderhoud","/bermonderhoud/"),("Ecologisch bermbeheer","/ecologisch-bermbeheer/"),("Ecologisch maaien","/ecologisch-maaien/")],
)

# ===========================================================================
add(
    "/slootonderhoud/",
    "Slootonderhoud: machines en advies | Wim van Breda",
    "Professioneel slootonderhoud: talud en waterlijn maaien en schonen, met maaiarm en maaikorf. Advies en machines uit Geldermalsen.",
    "Slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", None)],
    "Slootonderhoud omvat het maaien van het talud en de waterlijn en het schonen van de sloot, met als doel een goede waterafvoer en een begaanbare, stabiele oever te behouden. Wim van Breda levert de maaiarmen en maaikorven waarmee waterschappen en aannemers dit werk uitvoeren.",
    fact="Slootonderhoud bestaat uit het maaien van het talud om begroeiing kort te houden, het schonen van de waterlijn en soms de bodem zodat water goed kan afstromen, en waar nodig het afvoeren van maaisel met een maaikorf.",
    sections=[
        h2("Talud en waterlijn",
           p("Het talud wordt gemaaid om begroeiing kort te houden en de oever stabiel te laten; de waterlijn en soms de bodem van de sloot worden geschoond zodat water goed kan afstromen. Dit gebeurt doorgaans vanaf de kant, zonder de oever te betreden.")),
        h2("Machines voor slootonderhoud",
           p("De meeste sloten worden onderhouden met een "+a("maaiarm","/slootonderhoud/maaiarm/")+" vanaf de kant, eventueel met een "+a("maaikorf","/slootonderhoud/maaikorf/")+" om het maaisel direct op te vangen in plaats van het in het water te laten. Zie ook de bredere pagina "+a("machines voor slootonderhoud","/slootonderhoud/machines/")+".")),
        h2("Wanneer een maaikorf nodig is",
           p("Bij watergangen waar maaisel niet in het water mag achterblijven — om verstopping van de waterafvoer of extra voedingsstoffen in het water te voorkomen — wordt in plaats van een klepelkop een maaikorf gemonteerd, zoals de "+a("Herder maaikorf","/machine/herder-maaikorf/")+".")),
        h2("Wie voert slootonderhoud uit",
           p("Slootonderhoud wordt vooral uitgevoerd door waterschappen zelf en door aannemers en loonbedrijven die in opdracht van waterschappen werken volgens een vast onderhoudsschema.")),
    ],
    machines=("Relevante machines voor slootonderhoud", [
        card("herder-maaikorf"),
        card("herder-grenadier-maaiarm"),
    ]),
    faq=[
        ("Hoe vaak moet een sloot gemaaid worden?",
         "Dat hangt af van het beheerschema van het waterschap of de eigenaar en de groeisnelheid van de vegetatie; veel sloten worden één tot enkele keren per seizoen gemaaid."),
        ("Moet maaisel uit de sloot verwijderd worden?",
         "Bij veel watergangen wel, om verstopping van de waterafvoer en overmatige voedingsstoffen in het water te voorkomen — daarvoor wordt een maaikorf gebruikt."),
        ("Welke machine wordt gebruikt voor slootonderhoud?",
         "Meestal een maaiarm vanaf de kant, eventueel met een maaikorf aan het uiteinde in plaats van een klepelkop."),
    ],
    related=[("Machines voor slootonderhoud","/slootonderhoud/machines/"),("Maaiarm bij slootonderhoud","/slootonderhoud/maaiarm/"),
             ("Maaikorf bij slootonderhoud","/slootonderhoud/maaikorf/"),("Bermonderhoud","/bermonderhoud/"),("Taludmaaien","/taludmaaien/")],
)

# ===========================================================================
add(
    "/slootonderhoud/machines/",
    "Machines voor slootonderhoud | Wim van Breda",
    "Welke machines voor slootonderhoud geschikt zijn: maaiarm met maaikorf voor talud en waterlijn.",
    "Machines voor slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", "/slootonderhoud/"), ("Machines", None)],
    "Voor slootonderhoud is de combinatie van maaiarm en maaikorf de gangbare oplossing: de arm reikt vanaf de kant tot in de sloot, de korf vangt het maaisel op zodat het niet in het water achterblijft.",
    fact="Bij slootonderhoud is de maaiarm het werktuig dat het bereik levert, en de maaikorf (in plaats van een klepelkop) het onderdeel dat zorgt voor opvang van het maaisel — samen vormen ze de gangbare combinatie voor watergangen.",
    sections=[
        h2("Zie ook",
           p(a("Maaiarm","/maaiarm/")+" en "+a("maaikorf","/maaikorf/")+" voor de volledige uitleg over merken en uitvoeringen.")),
    ],
    machines=("Relevante machines", [
        card("herder-grenadier-maaiarm"),
        card("herder-maaikorf"),
    ]),
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaiarm","/maaiarm/"),("Maaikorf","/maaikorf/")],
)

# ===========================================================================
add(
    "/slootonderhoud/maaiarm/",
    "Maaiarm bij slootonderhoud | Wim van Breda",
    "Maaiarm voor het maaien van talud en waterlijn bij slootonderhoud, bediend vanaf de kant.",
    "Maaiarm bij slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", "/slootonderhoud/"), ("Maaiarm", None)],
    "De maaiarm maait het talud en de waterlijn van de sloot vanaf de kant, zodat de oever niet betreden hoeft te worden. Dit is de gangbare werkwijze bij professioneel slootonderhoud door waterschappen en hun aannemers.",
    fact="Een maaiarm bij slootonderhoud werkt uitsluitend vanaf de berm of oeverkant: de arm reikt naar het talud en de waterlijn, zodat de tractor niet in de sloot hoeft te rijden en de oever niet wordt belast.",
    sections=[
        h2("Zie ook",
           p("Voor merken en armlengtes: "+a("maaiarm","/maaiarm/")+" en "+a("maaiarm bij slootonderhoud","/maaiarm/slootonderhoud/")+".")),
    ],
    machines=("Relevante machine", [
        card("herder-grenadier-maaiarm"),
    ]),
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaiarm","/maaiarm/"),("Maaiarm bij slootonderhoud (detail)","/maaiarm/slootonderhoud/")],
)

# ===========================================================================
add(
    "/slootonderhoud/maaikorf/",
    "Maaikorf bij slootonderhoud | Wim van Breda",
    "Maaikorf voor slootonderhoud: maaisel direct opvangen tijdens het maaien van de waterlijn.",
    "Maaikorf bij slootonderhoud",
    [("Home", HOME), ("Slootonderhoud", "/slootonderhoud/"), ("Maaikorf", None)],
    "Waar maaisel niet in de sloot mag achterblijven, wordt de maaikorf gebruikt om het materiaal tijdens het maaien direct op te vangen, in plaats van het te verkleinen en te laten liggen zoals een klepelkop doet.",
    fact="Een maaikorf wordt bij slootonderhoud ingezet als vervanging van de klepelkop aan het uiteinde van de maaiarm, specifiek wanneer de watergang vrij van maaisel moet blijven.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg: "+a("maaikorf","/maaikorf/")+" en "+a("maaikorf bij slootonderhoud","/maaikorf/slootonderhoud/")+".")),
    ],
    machines=("Relevante machine", [
        card("herder-maaikorf"),
    ]),
    related=[("Slootonderhoud","/slootonderhoud/"),("Maaikorf","/maaikorf/"),("Maaikorf voor watergangen","/maaikorf/voor-watergangen/")],
)

# ===========================================================================
add(
    "/taludmaaien/",
    "Taludmaaien | Wim van Breda",
    "Taludmaaien: machines voor het maaien van hellingen langs dijken, sloten en wegen, veilig vanaf de kant of op afstand bestuurd.",
    "Taludmaaien",
    [("Home", HOME), ("Taludmaaien", None)],
    "Taludmaaien is het maaien van hellende oevers en dijken, waarbij veiligheid en bereik de belangrijkste aandachtspunten zijn: de bestuurder blijft bovenaan of op afstand, terwijl de machine de helling zelf afwerkt.",
    fact="Voor de meeste taluds volstaat een maaiarm die vanaf de kant naar beneden reikt; op zeer steile of gevaarlijke taluds worden radiografisch bestuurbare maaimachines ingezet, waarbij de bestuurder niet in de machine zit.",
    sections=[
        h2("Hoe taluds gemaaid worden",
           p("Voor de meeste taluds volstaat een "+a("maaiarm","/maaiarm/")+" die vanaf de kant naar beneden reikt. Op zeer steile of gevaarlijke taluds levert Wim van Breda radiografisch bestuurbare rups-werktuigdragers zoals de "+a("Herder CR10","/machine/herder-cr10-werktuigdrager/")+", die hellingen tot 55 graden aankan en de machinist op veilige afstand laat werken.")),
        h2("Zie ook",
           p("Voor de bijbehorende machines: "+a("taludonderhoud-machines","/taludonderhoud-machines/")+".")),
    ],
    machines=("Relevante machine voor steile taluds", [
        card("herder-cr10-werktuigdrager"),
    ]),
    related=[("Taludonderhoud-machines","/taludonderhoud-machines/"),("Maaiarm","/maaiarm/"),("Bermonderhoud","/bermonderhoud/")],
)

# ===========================================================================
add(
    "/taludonderhoud-machines/",
    "Taludonderhoud machines | Wim van Breda",
    "Machines voor taludonderhoud: maaiarmen en radiografisch bestuurbare werktuigdragers voor hellingen en dijken.",
    "Machines voor taludonderhoud",
    [("Home", HOME), ("Taludonderhoud machines", None)],
    "Voor taludonderhoud levert Wim van Breda maaiarmen die vanaf de kant een helling af kunnen maaien, en radiografisch bestuurbare werktuigdragers voor de steilste of minst toegankelijke taluds.",
    fact="De keuze tussen een maaiarm en een radiografisch bestuurbare werktuigdrager voor taludonderhoud hangt af van de steilheid van het talud: tot een bepaalde hellingshoek volstaat een arm vanaf de kant, bij extreme hellingen is een machine die zelf op het talud rijdt en op afstand wordt bestuurd veiliger.",
    sections=[
        h2("Maaiarm vanaf de kant",
           p(a("Maaiarmen","/maaiarm/")+" zijn de gangbare oplossing voor de meeste taluds langs dijken, sloten en wegen, zonder dat de machine het talud zelf op hoeft.")),
        h2("Radiografisch bestuurd voor steile taluds",
           p("Voor taluds die te steil of te gevaarlijk zijn om vanaf de kant te bereiken, levert Wim van Breda de "+a("Herder CR10","/machine/herder-cr10-werktuigdrager/")+": een rups-werktuigdrager die hellingen tot 55 graden aankan en volledig op afstand wordt bestuurd, met een keuze uit een 55 pk of 75 pk dieselmotor.")),
    ],
    machines=("Relevante machine voor taludonderhoud", [
        card("herder-cr10-werktuigdrager"),
    ]),
    related=[("Taludmaaien","/taludmaaien/"),("Maaiarm","/maaiarm/"),("Bermonderhoud","/bermonderhoud/"),("Werktuigdrager","/werktuigdrager/")],
)
