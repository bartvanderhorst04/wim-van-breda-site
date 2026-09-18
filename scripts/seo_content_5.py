# -*- coding: utf-8 -*-
"""Inhoud cluster 6-9: tuin-en-parkmachines, werktuigdrager, merk×product, regio (21 pagina's, uitgebreide versie)."""
from build_seo_pages import h2, h3, p, ul, a
from machine_data import card

HOME = "/"
PAGES = []

def add(path, title, description, h1, trail, intro, sections=None, faq=None, related=None, fact=None, machines=None, cta=None):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, trail=trail,
                       intro=intro, sections=sections or [], faq=faq or [], related=related,
                       fact=fact, machines=machines, cta=cta))

# ===========================================================================
# TUIN- EN PARKMACHINES
# ===========================================================================
add(
    "/tuin-en-parkmachines/",
    "Tuin- en parkmachines | Wim van Breda",
    "Professionele tuin- en parkmachines voor gemeenten en aannemers: maaimachines, veegtechniek en handgereedschap.",
    "Tuin- en parkmachines",
    [("Home", HOME), ("Tuin- en parkmachines", None)],
    "Tuin- en parkmachines zijn de machines en het handgereedschap waarmee openbaar groen, parken en terreinen onderhouden worden: van maaimachines voor hoog of moeilijk begaanbaar gras tot veegmachines voor verharding en professioneel handgereedschap. Wim van Breda levert dit programma aan gemeenten, hoveniers en aannemers.",
    fact="Onder tuin- en parkmachines vallen bij Wim van Breda onder meer maaimachines voor ruw en steil terrein, veegmachines voor verharding en parkeerterreinen, en handgereedschap zoals kettingzagen, bosmaaiers en heggenscharen.",
    sections=[
        h2("Wat onder tuin- en parkmachines valt",
           ul([
               "Maaimachines voor gazons en hoog of moeilijk begaanbaar gras",
               "Veegmachines voor verharding, parkeerterreinen en bedrijfslocaties",
               "Handgereedschap: kettingzagen, bosmaaiers, heggenscharen",
               "Onkruidbestrijdingstechniek voor verharding",
           ])),
        h2("Merken binnen tuin- en parkmachines",
           p("Wim van Breda levert onder meer AS-Motor, een Duits merk gespecialiseerd in hoogovermaaiers en maaimachines voor ruw en steil terrein zoals hellingen en taluds; Kersten, met veegmachines en werktuigen voor terreinbeheer op verharding en bedrijfslocaties; en Stihl, de standaard in professioneel handgereedschap zoals kettingzagen, bosmaaiers, heggenscharen en accutechniek.")),
        h2("Professioneel versus consumentengebruik",
           p("Het accent bij Wim van Breda ligt op professionele tuin- en parkmachines: gebouwd voor dagelijks, intensief gebruik door meerdere medewerkers, in plaats van incidenteel particulier gebruik. Zie ook "+a("professionele tuin- en parkmachines","/tuin-en-parkmachines/professioneel/")+".")),
        h2("Voor wie",
           p("Vooral "+a("gemeenten","/tuin-en-parkmachines/gemeenten/")+", hoveniers en "+a("aannemers","/tuin-en-parkmachines/aannemers/")+" die openbaar groen, parken en bedrijfsterreinen onderhouden.")),
        h2("Service en onderhoud",
           p("Wim van Breda levert tuin- en parkmachines inclusief onderhoud en onderdelen vanuit de eigen werkplaats in Geldermalsen.")),
    ],
    faq=[
        ("Wat zijn tuin- en parkmachines precies?",
         "De verzamelnaam voor machines en gereedschap voor onderhoud van openbaar groen en terreinen: van maai- en veegmachines tot handgereedschap zoals kettingzagen en bosmaaiers."),
        ("Welke merken tuin- en parkmachines levert Wim van Breda?",
         "Onder meer AS-Motor (maaimachines voor ruw en steil terrein), Kersten (veegmachines) en Stihl (handgereedschap)."),
        ("Zijn tuin- en parkmachines geschikt voor professioneel gebruik?",
         "Ja, het aanbod van Wim van Breda richt zich primair op professionele machines voor dagelijks, intensief gebruik door gemeenten en aannemers."),
    ],
    related=[("Tuin- en parkmachines kopen","/tuin-en-parkmachines/kopen/"),("Professionele tuin- en parkmachines","/tuin-en-parkmachines/professioneel/"),
             ("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/"),("Machines voor aannemers","/tuin-en-parkmachines/aannemers/"),
             ("Terreinonderhoud","/tuin-en-parkmachines/terreinonderhoud/")],
)

# ===========================================================================
add(
    "/tuin-en-parkmachines/kopen/",
    "Tuin- en parkmachines kopen | Wim van Breda",
    "Tuin- en parkmachines kopen bij Wim van Breda: advies over de juiste machine voor uw terrein en toepassing.",
    "Tuin- en parkmachines kopen",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Kopen", None)],
    "Bij de aanschaf van tuin- en parkmachines is het terrein waarop gewerkt wordt leidend voor de keuze van het type machine: een vlak gazon vraagt iets anders dan een steile berm, en verharding vraagt weer andere techniek dan gras.",
    fact="Bepalend bij de keuze van tuin- en parkmachines zijn: het type ondergrond (gazon, ruw terrein, verharding), de schaal van het werk, en of het gaat om een machine of om handgereedschap.",
    sections=[
        h2("Waar u op let",
           ul([
               "Type ondergrond — gazon, ruw of steil terrein, of verharding",
               "Schaal van het werk — incidenteel onderhoud of dagelijkse, intensieve inzet",
               "Machine of handgereedschap — een maaimachine, veegmachine of bijvoorbeeld een kettingzaag",
           ])),
        h2("Advies bij Wim van Breda",
           p("Wim van Breda adviseert over de juiste combinatie van maaimachines, veegtechniek en handgereedschap, en levert alles inclusief onderhoud en onderdelen vanuit Geldermalsen.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Professionele tuin- en parkmachines","/tuin-en-parkmachines/professioneel/")],
)

# ===========================================================================
add(
    "/tuin-en-parkmachines/professioneel/",
    "Professionele tuin- en parkmachines | Wim van Breda",
    "Professionele tuin- en parkmachines voor dagelijks, intensief gebruik door gemeenten en aannemers.",
    "Professionele tuin- en parkmachines",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Professioneel", None)],
    "Professionele tuin- en parkmachines zijn gebouwd voor dagelijks, intensief gebruik, in tegenstelling tot consumentenmachines die voor incidenteel gebruik bedoeld zijn. Het verschil zit in motorvermogen, materiaalkeuze en onderhoudsgemak.",
    fact="Professionele tuin- en parkmachines onderscheiden zich van consumentenmachines door zwaardere motoren, robuustere onderdelen en een onderhoudsprogramma dat is afgestemd op continu gebruik door meerdere medewerkers per dag.",
    sections=[
        h2("Het verschil met consumentenmachines",
           p("Professionele machines hebben zwaardere motoren, robuustere onderdelen en een onderhoudsprogramma dat is afgestemd op continu gebruik door meerdere medewerkers, in plaats van incidenteel gebruik in een particuliere tuin.")),
        h2("Merken die hierbij passen",
           p("AS-Motor levert bijvoorbeeld hoogovermaaiers en maaimachines specifiek voor ruw en steil terrein, terwijl Stihl de standaard is in professioneel handgereedschap zoals kettingzagen en bosmaaiers.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/")],
)

# ===========================================================================
add(
    "/tuin-en-parkmachines/gemeenten/",
    "Machines voor gemeenten | Wim van Breda",
    "Tuin- en parkmachines voor gemeenten: onderhoud van openbaar groen, parken en bermen door de eigen buitendienst.",
    "Machines voor gemeenten",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Gemeenten", None)],
    "Gemeenten gebruiken tuin- en parkmachines voor het onderhoud van openbaar groen, parken, bermen en sportvelden door de eigen buitendienst, vaak in combinatie met machines voor bermonderhoud zoals maaiarmen en klepelmaaiers.",
    fact="Gemeentelijke buitendiensten combineren doorgaans tuin- en parkmachines voor gazons en parken met zwaarder materieel zoals maaiarmen en klepelmaaiers voor bermen — Wim van Breda levert beide categorieën.",
    sections=[
        h2("Breed inzetbaar programma",
           p("Van maaimachines voor gazons tot klepelmaaiers voor bermen — Wim van Breda levert het programma dat past bij het beheerschema van de gemeente, inclusief onderdelen en service. Zie ook "+a("bermonderhoud","/bermonderhoud/")+" voor het zwaardere materieel dat vaak parallel wordt ingezet.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Bermonderhoud","/bermonderhoud/"),("Machines voor aannemers","/tuin-en-parkmachines/aannemers/")],
)

# ===========================================================================
add(
    "/tuin-en-parkmachines/aannemers/",
    "Machines voor aannemers | Wim van Breda",
    "Tuin- en parkmachines voor aannemers in groenvoorziening en terreinonderhoud, inclusief service en onderdelen.",
    "Machines voor aannemers",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Aannemers", None)],
    "Aannemers in groenvoorziening en terreinonderhoud gebruiken tuin- en parkmachines voor uiteenlopende opdrachten, van kleine tuinen tot grote bedrijfsterreinen, en hebben daarbij vooral behoefte aan betrouwbaarheid en snelle service.",
    fact="Voor aannemers die per opdracht of per dag afrekenen, is stilstand door een kapotte machine kostbaar; Wim van Breda houdt daarom onderdelen op voorraad en biedt vervangend materieel waar dat nodig is.",
    sections=[
        h2("Snel weer aan het werk",
           p("Wim van Breda houdt onderdelen op voorraad en biedt vervangend materieel, zodat een aannemer bij storing snel weer verder kan werken.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/"),("Terreinonderhoud","/tuin-en-parkmachines/terreinonderhoud/")],
)

# ===========================================================================
add(
    "/tuin-en-parkmachines/terreinonderhoud/",
    "Machines voor terreinonderhoud | Wim van Breda",
    "Tuin- en parkmachines voor terreinonderhoud: van maaien tot vegen en onkruidbestrijding op bedrijfsterreinen en verharding.",
    "Machines voor terreinonderhoud",
    [("Home", HOME), ("Tuin- en parkmachines", "/tuin-en-parkmachines/"), ("Terreinonderhoud", None)],
    "Terreinonderhoud gaat verder dan alleen maaien: ook het vegen van verharding en chemievrije onkruidbestrijding horen bij het onderhoud van bedrijfsterreinen, parkeerplaatsen en openbare ruimte.",
    fact="Naast maaimachines levert Wim van Breda veegmachines voor verharding en infraroodtechniek voor chemievrije onkruidbestrijding, beide relevant voor terreinonderhoud op verharde oppervlakken.",
    sections=[
        h2("Compleet programma",
           p("Naast maaimachines levert Wim van Breda veegmachines en infraroodtechniek voor onkruidbestrijding, geschikt voor bedrijfsterreinen, parkeerplaatsen en verharding.")),
    ],
    related=[("Tuin- en parkmachines","/tuin-en-parkmachines/"),("Machines voor gemeenten","/tuin-en-parkmachines/gemeenten/")],
)

# ===========================================================================
# WERKTUIGDRAGER
# ===========================================================================
add(
    "/werktuigdrager/",
    "Werktuigdrager | Wim van Breda",
    "Professionele werktuigdrager voor berm-, sloot- en terreinonderhoud: compact platform voor meerdere aanbouwwerktuigen.",
    "Werktuigdrager",
    [("Home", HOME), ("Werktuigdrager", None)],
    "Een werktuigdrager is een compact, wendbaar voertuig dat speciaal is ontworpen om met verschillende aanbouwwerktuigen te werken, in plaats van een tractor met één vaste functie. Wim van Breda levert onder meer elektrische en radiografisch bestuurbare werktuigdragers van Raymo en Herder.",
    fact="Een werktuigdrager is gebouwd rond het snel wisselen van werktuigen — maaikop, veegborstel of ander aanbouwdeel — vaak zonder de bestuurdersplek te hoeven verlaten, en soms zelfs volledig op afstand bestuurd.",
    sections=[
        h2("Waarom een werktuigdrager",
           p("Waar een gewone tractor vooral geschikt is voor trekkracht, is een werktuigdrager specifiek gebouwd rond het snel wisselen van werktuigen. Dat maakt hem geschikt voor beheerders die met één compact platform meerdere taken willen uitvoeren, vaak op locaties waar een grote tractor lastig of onveilig is.")),
        h2("Elektrisch en radiografisch bestuurd",
           p("Een voorbeeld is de "+a("Raymo Torpedo","/machine/raymo-torpedo-werktuigdrager/")+": een volledig elektrische, radiografisch bestuurbare werktuigdrager voor stil en emissievrij groen- en terreinonderhoud, ontwikkeld door het Nederlandse merk Raymo. Dankzij het lage zwaartepunt en de bediening op afstand is deze machine bijzonder geschikt voor zonneparken, taluds, bermen en recreatieterreinen.")),
        h2("Rups-werktuigdragers voor steile hellingen",
           p("Voor extreem steile of gevaarlijke locaties bouwt Herder de "+a("CR10","/machine/herder-cr10-werktuigdrager/")+": een radiografisch bestuurbare rups-werktuigdrager die hellingen tot 55 graden aankan, met een keuze uit een 55 pk of 75 pk dieselmotor.")),
        h2("Voor wie een werktuigdrager relevant is",
           p("Werktuigdragers worden ingezet door beheerders van zonneparken, waterschappen, gemeenten en aannemers die werken op taluds, bermen en terreinen waar veiligheid en bereikbaarheid een rol spelen.")),
    ],
    machines=("Werktuigdragers bij Wim van Breda", [
        card("raymo-torpedo-werktuigdrager"),
        card("herder-cr10-werktuigdrager"),
    ]),
    faq=[
        ("Wat is het verschil tussen een werktuigdrager en een tractor?",
         "Een tractor is vooral gebouwd om trekkracht te leveren, een werktuigdrager is specifiek ontworpen om snel te wisselen tussen uiteenlopende aanbouwwerktuigen, vaak in een compacter en wendbaarder chassis."),
        ("Is een werktuigdrager altijd op afstand bestuurd?",
         "Niet altijd, maar sommige modellen zoals de Raymo Torpedo en de Herder CR10 zijn wel volledig radiografisch bestuurbaar, wat op steile of gevaarlijke locaties de veiligheid vergroot."),
        ("Welke merken werktuigdragers levert Wim van Breda?",
         "Onder meer Raymo (elektrisch, radiografisch bestuurbaar) en Herder (rups-werktuigdrager voor steile hellingen)."),
    ],
    related=[("Werktuigdrager kopen","/werktuigdrager/kopen/"),("Professionele werktuigdrager","/werktuigdrager/professioneel/"),
             ("Werktuigdrager bij bermonderhoud","/werktuigdrager/bermonderhoud/"),("Werktuigdrager bij slootonderhoud","/werktuigdrager/slootonderhoud/")],
)

# ===========================================================================
add(
    "/werktuigdrager/kopen/",
    "Werktuigdrager kopen | Wim van Breda",
    "Werktuigdrager kopen bij Wim van Breda: advies over het juiste model voor uw werktuigen en toepassing.",
    "Werktuigdrager kopen",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Kopen", None)],
    "Bij de keuze van een werktuigdrager is het bepalend welke werktuigen u wilt combineren en of stil, emissievrij of op afstand bestuurd werken een vereiste is voor de locaties waar u werkt.",
    fact="De keuze tussen bijvoorbeeld een elektrische werktuigdrager en een rups-werktuigdrager hangt af van de toepassing: elektrisch en stil voor gevoelige locaties, rupsen en radiografische bediening voor steile hellingen.",
    sections=[
        h2("Advies bij Wim van Breda",
           p("Wim van Breda adviseert over de juiste werktuigdrager en levert onder meer elektrische en radiografisch bestuurbare modellen, inclusief onderdelen en service uit Geldermalsen.")),
    ],
    machines=("Voorbeelden van werktuigdragers", [
        card("raymo-torpedo-werktuigdrager"),
        card("herder-cr10-werktuigdrager"),
    ]),
    related=[("Werktuigdrager","/werktuigdrager/"),("Professionele werktuigdrager","/werktuigdrager/professioneel/")],
)

# ===========================================================================
add(
    "/werktuigdrager/professioneel/",
    "Professionele werktuigdrager | Wim van Breda",
    "Professionele werktuigdrager voor dagelijks, intensief gebruik door aannemers, gemeenten en waterschappen.",
    "Professionele werktuigdrager",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Professioneel", None)],
    "Een professionele werktuigdrager is gebouwd voor dagelijks gebruik: robuust, goed te onderhouden en met een snel wisselsysteem voor werktuigen, ingezet door beheerders die met één platform meerdere taken willen uitvoeren.",
    fact="Professionele werktuigdragers zoals de Raymo Torpedo en de Herder CR10 zijn ontwikkeld voor dagelijkse inzet door gemeenten, waterschappen en aannemers, met kenmerken als een uitwisselbaar accusysteem of een robuust rupsonderstel voor continu gebruik.",
    sections=[
        h2("Voor gemeenten, waterschappen en aannemers",
           p("Deze machines worden ingezet voor uiteenlopend beheerwerk waarbij één platform meerdere taken moet kunnen uitvoeren, vaak op locaties die met een gewone tractor lastig te bereiken zijn.")),
    ],
    related=[("Werktuigdrager","/werktuigdrager/"),("Werktuigdrager kopen","/werktuigdrager/kopen/")],
)

# ===========================================================================
add(
    "/werktuigdrager/bermonderhoud/",
    "Werktuigdrager bij bermonderhoud | Wim van Breda",
    "Werktuigdrager inzetten voor bermonderhoud: compact platform voor gevarieerd bermwerk met meerdere werktuigen.",
    "Werktuigdrager bij bermonderhoud",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Bermonderhoud", None)],
    "Voor gevarieerd bermwerk op kleinere schaal is een werktuigdrager praktisch: één compact platform waarop verschillende werktuigen gemonteerd kunnen worden, ook op locaties die voor een grote tractor lastig bereikbaar zijn.",
    fact="Werktuigdragers worden bij bermonderhoud vooral ingezet op locaties waar een reguliere tractor met maaiarm minder praktisch is: smalle bermen, taluds of plekken waar stil en emissievrij werken gewenst is.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg over bermonderhoud: "+a("bermonderhoud","/bermonderhoud/")+".")),
    ],
    machines=("Relevante machine", [
        card("herder-cr10-werktuigdrager"),
    ]),
    related=[("Werktuigdrager","/werktuigdrager/"),("Bermonderhoud","/bermonderhoud/"),("Machines voor bermonderhoud","/bermonderhoud/machines/")],
)

# ===========================================================================
add(
    "/werktuigdrager/slootonderhoud/",
    "Werktuigdrager bij slootonderhoud | Wim van Breda",
    "Werktuigdrager inzetten voor slootonderhoud: compact en wendbaar platform voor werk langs de waterkant.",
    "Werktuigdrager bij slootonderhoud",
    [("Home", HOME), ("Werktuigdrager", "/werktuigdrager/"), ("Slootonderhoud", None)],
    "Langs smalle watergangen is een compacte, wendbare werktuigdrager soms praktischer dan een grote tractor met maaiarm, vooral op plekken waar de oever weinig ruimte biedt.",
    fact="Een werktuigdrager biedt bij slootonderhoud vooral voordeel op smalle of moeilijk bereikbare watergangen, waar een compact platform beter past dan een grote tractor met maaiarm.",
    sections=[
        h2("Zie ook",
           p("Voor de volledige uitleg over slootonderhoud: "+a("slootonderhoud","/slootonderhoud/")+".")),
    ],
    related=[("Werktuigdrager","/werktuigdrager/"),("Slootonderhoud","/slootonderhoud/"),("Machines voor slootonderhoud","/slootonderhoud/machines/")],
)

# ===========================================================================
# MERK × PRODUCT
# ===========================================================================
add(
    "/herder/maaiarm/",
    "Herder maaiarmen | Wim van Breda",
    "Herder als merk: 75 jaar ervaring in maaiarmen voor Nederlandse waterschappen, gemeenten en aannemers, met de Grenadier als voorbeeld.",
    "Herder maaiarmen",
    [("Home", HOME), ("Herder", "/herder/maaiarm/"), ("Maaiarm", None)],
    "Herder is een Nederlands merk, opgericht door de gebroeders Den Herder, dat al ruim 75 jaar machines bouwt voor berm-, dijk- en slootonderhoud. Binnen dat programma vormen maaiarmen een van de kernproducten, met de Grenadier als voorbeeld van een zware, veelzijdige uitvoering.",
    fact="Herder bouwt maaiarmen die specifiek zijn ontwikkeld voor Nederlandse omstandigheden: intensief bermbeheer, dijkonderhoud en slootkanten, met een armlengte tot 8,80 meter en de mogelijkheid om te wisselen tussen uiteenlopende aanbouwwerktuigen.",
    sections=[
        h2("Wat Herder als merk kenmerkt",
           p("Waar sommige fabrikanten zich richten op één specifiek marktsegment, bouwt Herder een breed programma dat is afgestemd op de praktijk van Nederlandse waterschappen, gemeenten en aannemers: van compacte maaiarmen tot de zware "+a("Grenadier","/machine/herder-grenadier-maaiarm/")+" met een armlengte van 6,40 tot 8,80 meter.")),
        h2("De Grenadier in detail",
           p("De Grenadier is uit te rusten met onder meer een klepelmaaier, maaikorf, schijvenmaaier, bosbouwmaaier, stobbenfrees, ecologische maaier en onkruidborstel, en wordt zijdelings op de tractor gemonteerd. De flexibele arm kan verschillende posities innemen om moeilijk bereikbare plekken zoals diepe sloten, steile taluds en obstakels als vangrails en bomen te bereiken.")),
        h2("Bekijk ook",
           p("Herder levert naast maaiarmen ook "+a("maaikorven","/herder/maaikorf/")+", vaak in combinatie ingezet bij sloot- en watergangonderhoud. Voor de bredere uitleg over maaiarmen in het algemeen: "+a("maaiarm","/maaiarm/")+" en "+a("Herder maaiarm (uitgebreid)","/maaiarm/herder/")+".")),
    ],
    machines=("Herder-maaiarmen bij Wim van Breda", [
        card("herder-grenadier-maaiarm"),
    ]),
    related=[("Herder maaiarm (detail)","/maaiarm/herder/"),("Herder maaikorven","/herder/maaikorf/"),("Maaiarm","/maaiarm/")],
)

# ===========================================================================
add(
    "/herder/maaikorf/",
    "Herder maaikorven | Wim van Breda",
    "Herder maaikorven bij Wim van Breda: aanbouwdeel op Herder-maaiarmen voor sloot- en watergangonderhoud.",
    "Herder maaikorven",
    [("Home", HOME), ("Herder", "/herder/maaiarm/"), ("Maaikorf", None)],
    "Naast maaiarmen bouwt Herder ook maaikorven: aanbouwdelen die specifiek zijn ontwikkeld voor sloot- en watergangonderhoud, waarbij maaisel tijdens het maaien direct wordt opgevangen in plaats van verkleind te blijven liggen.",
    fact="De Herder maaikorf is gemaakt van materialen die bestand zijn tegen intensief gebruik in natte omstandigheden, met messen van gehard staal en een open korfontwerp dat verstoppingen voorkomt en zowel boven als onder water kan maaien.",
    sections=[
        h2("Waarom Herder deze maaikorf bouwt",
           p("Herder ontwikkelde de maaikorf als logische aanvulling op de eigen maaiarmen, specifiek voor waterschappen en aannemers die sloten en watergangen onderhouden waar maaisel niet mag achterblijven. Zie de volledige productbeschrijving op "+a("Herder maaikorf (uitgebreid)","/maaikorf/herder/")+".")),
        h2("Bekijk ook",
           p("Deze maaikorf wordt vooral gecombineerd met de "+a("Herder maaiarmen","/herder/maaiarm/")+", zoals de Grenadier, voor sloot- en watergangonderhoud.")),
    ],
    machines=("Herder maaikorf", [
        card("herder-maaikorf"),
    ]),
    related=[("Herder maaikorf (detail)","/maaikorf/herder/"),("Herder maaiarmen","/herder/maaiarm/"),("Maaikorf","/maaikorf/")],
)

# ===========================================================================
add(
    "/greentec/maaiarm/",
    "GreenTec maaiarmen | Wim van Breda",
    "GreenTec maaiarmen bij Wim van Breda: Deens merk met modulair systeem — één draagarm, meerdere werktuigen.",
    "GreenTec maaiarmen",
    [("Home", HOME), ("GreenTec", "/greentec/maaiarm/"), ("Maaiarm", None)],
    "GreenTec is een Deens merk dat zich onderscheidt door een modulair maaiarmsysteem: één draagarm waarop zonder gereedschap gewisseld kan worden tussen klepelkop, takkenschaar en andere werktuigen — praktisch voor beheerders die met één machine meerdere taken willen uitvoeren.",
    fact="Het kenmerk van GreenTec is de modulaire opbouw: dezelfde draagarm werkt met verschillende aanbouwdelen, van klepelkop tot takkenschaar, en de Scorpion-serie loopt van compacte modellen voor kleine tractoren tot zware uitvoeringen met een bereik van meer dan 8 meter.",
    sections=[
        h2("Wat GreenTec als merk kenmerkt",
           p("Waar andere merken vaak een vaste combinatie van arm en werktuig bouwen, is bij GreenTec de arm zelf het uitgangspunt: door het werktuig te wisselen kan dezelfde machine in het voorjaar maaien en in het najaar snoeien.")),
        h2("De Scorpion-serie",
           p("De "+a("Scorpion 430 S – Basisfront","/machine/greentec-scorpion-430-s-basisfront-maaiarm/")+" is een compacte uitvoering voor tractoren vanaf 3.000 kg, geschikt voor gebieden met beperkte ruimte. De "+a("Scorpion 830 Plus","/machine/greentec-scorpion-830-plus-maaiarm/")+" is de zwaardere variant met 8,3 meter horizontaal bereik, voor tractoren vanaf 8.000 kg en intensief berm-, heg- en slootonderhoud.")),
        h2("Bekijk ook",
           p("GreenTec levert ook klepelkoppen als onderdeel van dit systeem — zie "+a("GreenTec klepelmaaiers","/greentec/klepelmaaier/")+". Voor de bredere uitleg over maaiarmen: "+a("maaiarm","/maaiarm/")+".")),
    ],
    machines=("GreenTec-maaiarmen bij Wim van Breda", [
        card("greentec-scorpion-430-s-basisfront-maaiarm"),
        card("greentec-scorpion-830-plus-maaiarm"),
    ]),
    related=[("GreenTec maaiarm (detail)","/maaiarm/greentec/"),("GreenTec klepelmaaiers","/greentec/klepelmaaier/"),("Maaiarm","/maaiarm/")],
)

# ===========================================================================
add(
    "/greentec/klepelmaaier/",
    "GreenTec klepelmaaiers | Wim van Breda",
    "GreenTec als merk: het modulaire maaiarmsysteem waarbij de klepelkop één van de verwisselbare werktuigen is.",
    "GreenTec klepelmaaiers",
    [("Home", HOME), ("GreenTec", "/greentec/maaiarm/"), ("Klepelmaaier", None)],
    "Bij GreenTec is de klepelkop niet een losse machine, maar een van de werktuigen binnen het modulaire maaiarmsysteem: dezelfde draagarm die met een takkenschaar snoeit, wisselt zonder gereedschap naar een klepelkop om te maaien.",
    fact="Anders dan bij merken die uitsluitend losse klepelmaaiers bouwen, is de GreenTec-klepelkop altijd gekoppeld aan de eigen maaiarm — de keuze voor GreenTec is dus in de praktijk een keuze voor het hele modulaire armsysteem.",
    sections=[
        h2("Klepelkop als onderdeel van het systeem",
           p("Dat maakt GreenTec een logische keuze voor wie met één "+a("maaiarm","/greentec/maaiarm/")+" zowel wil maaien als snoeien, in plaats van twee losse machines aan te schaffen. Modellen als de "+a("Scorpion 430 S","/machine/greentec-scorpion-430-s-basisfront-maaiarm/")+" en de "+a("Scorpion 830 Plus","/machine/greentec-scorpion-830-plus-maaiarm/")+" zijn hier voorbeelden van.")),
        h2("Bekijk ook",
           p("Voor de bredere uitleg over klepelmaaiers in het algemeen: "+a("klepelmaaier","/klepelmaaier/")+" en "+a("GreenTec klepelmaaier (uitgebreid)","/klepelmaaier/greentec/")+".")),
    ],
    machines=("GreenTec-maaiarmen met klepelkop", [
        card("greentec-scorpion-430-s-basisfront-maaiarm"),
    ]),
    related=[("GreenTec klepelmaaier (detail)","/klepelmaaier/greentec/"),("GreenTec maaiarmen","/greentec/maaiarm/"),("Klepelmaaier","/klepelmaaier/")],
)

# ===========================================================================
add(
    "/omarv/klepelmaaier/",
    "Omarv klepelmaaiers | Wim van Breda",
    "Omarv als merk: een Italiaans programma dat klepelmaaiers combineert met maai-laadcombinaties voor zwaar en specialistisch terreinonderhoud.",
    "Omarv klepelmaaiers",
    [("Home", HOME), ("Omarv", "/omarv/klepelmaaier/"), ("Klepelmaaier", None)],
    "Omarv is een Italiaans merk dat zich onderscheidt door de breedte van het programma: van compacte klepelmaaiers voor regulier onderhoud tot zware uitvoeringen voor ruig terrein, boomgaarden en wijngaarden, en maai-laadcombinaties die maaien en opvangen combineren.",
    fact="Omarv bouwt zowel losse klepelmaaiers, zoals de Torino voor tractoren van 70 tot 140 pk, als maai-laadcombinaties zoals de Venezia L die maaien, verkleinen en opvangen in één werkgang doen.",
    sections=[
        h2("Wat Omarv als merk kenmerkt",
           p("Omarv richt zich met name op professionals die zwaar terreinonderhoud combineren met specifieke toepassingen zoals boomgaard- of wijngaardonderhoud, waar andere merken zich vaker beperken tot regulier bermwerk.")),
        h2("Voorbeelden uit het programma",
           p("De "+a("Torino","/machine/omarv-torino-klepelmaaier/")+" is een zware klepelmaaier met een verzwaarde rotoras en uitworp boven de looprol, leverbaar in 6 werkbreedtes van 160 tot 260 cm. De "+a("Venezia L","/machine/omarv-venezia-l-professionele-maai-laad-combinatie/")+" combineert maaien met opvangen in een bak van 10 m³, geschikt voor tractoren van 90 tot 120 pk.")),
        h2("Bekijk ook",
           p("Voor de bredere uitleg over klepelmaaiers: "+a("klepelmaaier","/klepelmaaier/")+" en "+a("Omarv klepelmaaier (uitgebreid)","/klepelmaaier/omarv/")+".")),
    ],
    machines=("Omarv-machines bij Wim van Breda", [
        card("omarv-torino-klepelmaaier"),
        card("omarv-venezia-l-professionele-maai-laad-combinatie"),
    ]),
    related=[("Omarv klepelmaaier (detail)","/klepelmaaier/omarv/"),("Klepelmaaier","/klepelmaaier/"),("Ecologisch maaien","/ecologisch-maaien/")],
)

# ===========================================================================
add(
    "/votex/klepelmaaier/",
    "Votex klepelmaaiers | Wim van Breda",
    "Votex klepelmaaiers bij Wim van Breda: het bekende Nederlandse merk voor bermmaaiers achter gemeentetractoren.",
    "Votex klepelmaaiers",
    [("Home", HOME), ("Votex", "/votex/klepelmaaier/"), ("Klepelmaaier", None)],
    "Votex is het Nederlandse merk dat je terugvindt achter vrijwel elke gemeentetractor: eenvoudig in onderhoud, robuust in de berm, met een onderdelenvoorziening die jarenlang meegaat. Wim van Breda levert en onderhoudt dit programma vanuit Geldermalsen.",
    fact="Votex onderscheidt zich door de combinatie van eenvoud en bedrijfszekerheid: modellen zoals de RoadFlex zijn gebouwd voor dagelijks, intensief gebruik door gemeenten en loonbedrijven, met een lange onderdelenvoorziening.",
    sections=[
        h2("Wat Votex als merk kenmerkt",
           p("Anders dan merken die zich richten op zware, specialistische toepassingen, is Votex vooral bekend als het bedrijfszekere werkpaard voor dagelijks bermonderhoud — eenvoudig te bedienen en te onderhouden, met een lange levensduur.")),
        h2("De RoadFlex in detail",
           p("De "+a("RoadFlex","/machine/votex-roadflex-klepelmaaier/")+" combineert twee functies: als vlakmaaier direct achter de trekker voor compact werk, en als zijklepelmaaier met een sideshift van bijna 250 cm voor bermen en taluds. Een hydraulisch veersysteem in de driepuntsbok zorgt voor trillingsreductie en botsbeveiliging bij obstakels.")),
        h2("Bekijk ook",
           p("Voor de bredere uitleg over klepelmaaiers: "+a("klepelmaaier","/klepelmaaier/")+" en "+a("Votex klepelmaaier (uitgebreid)","/klepelmaaier/votex/")+".")),
    ],
    machines=("Votex-machine bij Wim van Breda", [
        card("votex-roadflex-klepelmaaier"),
    ]),
    related=[("Votex klepelmaaier (detail)","/klepelmaaier/votex/"),("Klepelmaaier","/klepelmaaier/"),("Klepelmaaier bij bermonderhoud","/klepelmaaier/bermonderhoud/")],
)

# ===========================================================================
# REGIO
# ===========================================================================
add(
    "/regio/geldermalsen/",
    "Machines voor groenbeheer in Geldermalsen | Wim van Breda",
    "Wim van Breda is gevestigd in Geldermalsen: machines, advies en service voor groen-, berm- en terreinbeheer vanuit onze eigen werkplaats.",
    "Wim van Breda in Geldermalsen",
    [("Home", HOME), ("Regio", None), ("Geldermalsen", None)],
    "Wim van Breda is gevestigd aan de Oudenhof 14 in Geldermalsen, waar sinds 1957 machines voor groen-, berm- en terreinbeheer worden geleverd, onderhouden en verhuurd. Vanuit deze ene vestiging bedienen wij klanten in de directe omgeving en daarbuiten.",
    fact="Wim van Breda is een familiebedrijf met eigen werkplaats in Geldermalsen, actief sinds 1957, met 45 collega's en een vast machinepark van meerdere merken voor groen-, berm- en terreinbeheer.",
    sections=[
        h2("Wat wij vanuit Geldermalsen doen",
           p("Vanuit onze vestiging leveren we "+a("maaiarmen","/maaiarm/")+", "+a("klepelmaaiers","/klepelmaaier/")+", "+a("werktuigdragers","/werktuigdrager/")+" en "+a("tuin- en parkmachines","/tuin-en-parkmachines/")+" aan loonbedrijven, aannemers, gemeenten en waterschappen. Onze eigen werkplaats verzorgt onderhoud, reparatie en onderdelen, met vervangend materieel wanneer dat nodig is.")),
        h2("Bereikbaarheid",
           p("Geldermalsen ligt aan de A15, tussen Utrecht en Nijmegen, en is daarmee goed bereikbaar voor klanten in de Betuwe, Rivierenland en de wijdere regio.")),
        h2("Bermen, sloten en terreinen in de regio",
           p("Klanten in en rond Geldermalsen gebruiken onze machines voor "+a("bermonderhoud","/bermonderhoud/")+" en "+a("slootonderhoud","/slootonderhoud/")+" langs de vele wegen en watergangen die de Betuwe kenmerken.")),
    ],
    related=[("Betuwe","/regio/betuwe/"),("Rivierenland","/regio/rivierenland/"),("Zaltbommel","/regio/zaltbommel/")],
)

# ===========================================================================
add(
    "/regio/betuwe/",
    "Machines voor groenbeheer in de Betuwe | Wim van Breda",
    "Wim van Breda levert en onderhoudt machines voor groen-, berm- en terreinbeheer in de Betuwe, vanuit de eigen vestiging in Geldermalsen.",
    "Wim van Breda in de Betuwe",
    [("Home", HOME), ("Regio", None), ("Betuwe", None)],
    "Wim van Breda is gevestigd in Geldermalsen, in het hart van de Betuwe, en levert vanuit deze vestiging machines en service aan bedrijven en overheden in de regio die te maken hebben met fruitteelt, landbouw en een dicht netwerk van watergangen.",
    fact="De Betuwe, waarin Geldermalsen ligt, kent veel fruitteelt, landbouw en een dicht netwerk van kaden, dijken en watergangen — werk waarvoor maaiarmen, klepelmaaiers en maaikorven veel worden ingezet.",
    sections=[
        h2("Fruitteelt, landbouw en waterbeheer",
           p("De Betuwe kent veel fruitteelt, landbouw en een dicht netwerk van kaden, dijken en watergangen — werk waarvoor "+a("maaiarmen","/maaiarm/")+", "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("maaikorven","/maaikorf/")+" veel worden ingezet.")),
        h2("Levering en service",
           p("Loonbedrijven en aannemers in de Betuwe kunnen bij Wim van Breda terecht voor advies, onderhoud en onderdelen vanuit de eigen werkplaats in Geldermalsen.")),
    ],
    related=[("Geldermalsen","/regio/geldermalsen/"),("Rivierenland","/regio/rivierenland/"),("Zaltbommel","/regio/zaltbommel/")],
)

# ===========================================================================
add(
    "/regio/rivierenland/",
    "Machines voor groenbeheer in Rivierenland | Wim van Breda",
    "Wim van Breda levert machines voor groen-, berm- en slootbeheer in Rivierenland, vanuit de eigen vestiging in Geldermalsen.",
    "Wim van Breda in Rivierenland",
    [("Home", HOME), ("Regio", None), ("Rivierenland", None)],
    "Rivierenland, de regio tussen Waal en Linge waarin Geldermalsen ligt, kent veel watergangen, dijken en landelijk gebied dat professioneel onderhoud vraagt van waterschappen, aannemers en loonbedrijven.",
    fact="Rivierenland is de regio tussen Waal en Linge waarin Geldermalsen ligt, gekenmerkt door veel watergangen en dijken die structureel onderhoud vragen.",
    sections=[
        h2("Waterschappen en aannemers",
           p("Waterschappen en aannemers in Rivierenland gebruiken onze "+a("maaiarmen","/maaiarm/")+" en "+a("maaikorven","/maaikorf/")+" voor "+a("slootonderhoud","/slootonderhoud/")+" en dijkbeheer.")),
        h2("Vanuit Geldermalsen",
           p("Wim van Breda levert en onderhoudt deze machines vanuit de eigen werkplaats in Geldermalsen, centraal in de regio.")),
    ],
    related=[("Geldermalsen","/regio/geldermalsen/"),("Betuwe","/regio/betuwe/"),("Zaltbommel","/regio/zaltbommel/")],
)

# ===========================================================================
add(
    "/regio/zaltbommel/",
    "Machines voor groenbeheer in Zaltbommel | Wim van Breda",
    "Wim van Breda levert machines voor groen-, berm- en terreinbeheer in Zaltbommel en de Bommelerwaard, vanuit Geldermalsen.",
    "Wim van Breda in Zaltbommel",
    [("Home", HOME), ("Regio", None), ("Zaltbommel", None)],
    "Zaltbommel en de Bommelerwaard liggen op korte afstand van onze vestiging in Geldermalsen, aan de andere kant van de Waal, in een gebied met vergelijkbare kenmerken als de Betuwe.",
    fact="Zaltbommel en de Bommelerwaard liggen aan de overzijde van de Waal ten opzichte van Geldermalsen en kennen, net als de Betuwe, veel dijken en agrarisch gebied.",
    sections=[
        h2("Dijken en landelijk gebied",
           p("De Bommelerwaard kent, net als de Betuwe, veel dijken, sloten en agrarisch gebied — werk waarvoor "+a("maaiarmen","/maaiarm/")+", "+a("klepelmaaiers","/klepelmaaier/")+" en "+a("werktuigdragers","/werktuigdrager/")+" worden ingezet.")),
        h2("Levering en service",
           p("Ook klanten in Zaltbommel en omgeving kunnen bij Wim van Breda terecht voor advies, onderhoud en onderdelen vanuit Geldermalsen.")),
    ],
    related=[("Geldermalsen","/regio/geldermalsen/"),("Rivierenland","/regio/rivierenland/"),("Betuwe","/regio/betuwe/")],
)
