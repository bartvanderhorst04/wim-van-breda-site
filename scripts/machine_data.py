# -*- coding: utf-8 -*-
"""
Echte machinerecords, 1-op-1 overgenomen uit Component.MACHINES in
"Wim van Breda.dc.html" (naam/merk/kort/kenmerken/specs/tekst/toepassingen
letterlijk gekopieerd — niets verzonnen of aangevuld). Alleen deze
machines krijgen een eigen statische /machine/<slug>/-pagina, omdat alleen
deze machines vanaf een SEO-landingspagina worden gelinkt als "Bekijk
machine" — zie build_seo_pages.machine_page_html().

`seo_links`: optionele lijst (label, href) naar de SEO-clusterpagina's die
naar déze machine linken, zodat de machinepagina op zijn beurt weer subtiel
terug- en verderlinkt (geen doodlopende pagina).
"""

MACHINES = {
    "herder-grenadier-maaiarm": {
        "url": "/machine/herder-grenadier-maaiarm/",
        "name": "Grenadier maaiarm", "brand": "Herder", "type": "Maaiarmen",
        "kort": "Veelzijdige maaiarm voor zwaar bermbeheer, uitrusbaar met diverse aanbouwwerktuigen, armlengte 6,40 tot 8,80 meter.",
        "kenmerken": ["Uitrusbaar met diverse aanbouwwerktuigen","Flexibele maaiarm voor moeilijk bereikbare plekken","Zijdelingse montage op de tractor","Ook leverbaar met afzuiging","Toegankelijke servicepunten voor eenvoudig onderhoud"],
        "specs": [{"k":"Armlengte","v":"6,40 m tot 8,80 m"}],
        "tekst": "De Herder Grenadier is een indrukwekkende en veelzijdige maaiarm die speciaal is ontworpen voor het zware werk in het bermbeheer en de groenvoorziening. Met zijn robuuste bouw en krachtige prestaties kan de Herder Grenadier elk landschap aan, van vlakke weilanden tot moeilijk bereikbare hellingen en diepe sloten. De Grenadier kan worden uitgerust met diverse aanbouwwerktuigen zoals klepelmaaier, maaikorf, schijvenmaaier, bosbouwmaaier, stobbenfrees, ecologische maaier en onkruidborstel. De flexibele maaiarm kan verschillende posities innemen, waardoor moeilijk bereikbare plekken zoals diepe sloten, steile taluds en rondom obstakels zoals vangrails en bomen kunnen worden onderhouden. De maaiarm wordt bevestigd aan de zijkant van de tractor en is ook leverbaar met afzuiging.",
        "toepassingen": ["Bermonderhoud","Slootonderhoud","Taludonderhoud"],
        "seo_links": [("Maaiarm","/maaiarm/"),("Herder maaiarmen","/maaiarm/herder/"),("Maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/"),("Bermonderhoud","/bermonderhoud/")],
    },
    "greentec-scorpion-430-s-basisfront-maaiarm": {
        "url": "/machine/greentec-scorpion-430-s-basisfront-maaiarm/",
        "name": "Scorpion 430 S – Basisfront maaiarm", "brand": "GreenTec", "type": "Maaiarmen",
        "kort": "Professionele maaiarm voor gebieden met beperkte ruimte, ontworpen voor kleine tractoren vanaf 3.000 kg.",
        "kenmerken": ["Vier montagepunten voor optimale stabiliteit","Constructie van hoogwaardig Strenx 700 staal","155 graden armbeweging met power control","Hybride armsysteem met of zonder parallelle beweging","Horizontaal bereik 4,3 m, verticaal bereik 4,1 m"],
        "specs": [{"k":"Horizontaal bereik","v":"4,3 m"},{"k":"Verticaal bereik","v":"4,1 m"},{"k":"Transporthoogte","v":"2,2 m"},{"k":"Transportbreedte","v":"1,22 m"},{"k":"Hydrauliek systeem","v":"52 l/min @ 210 bar"},{"k":"Gewicht zonder werktuigen","v":"520 kg"},{"k":"Minimaal gewicht loader","v":"3000 kg"}],
        "tekst": "De GreenTec Scorpion 430 S – Basisfront is een professionele maaiarm die uitstekend geschikt is voor gebieden met een beperkte ruimte, zoals bermen in woonwijken of fietspaden. Daarnaast is het mogelijk om heggen en bomen op smalle bospaden te snoeien. De GreenTec Scorpion 430 S – Basisfront is ontworpen voor kleine tractoren met een minimaal gewicht van 3000 kilogram. De Scorpion modellen van GreenTec bevatten vier montagepunten op het hoofdframe, wat voor een optimale stabiliteit zorgt. Dit maakt deze maaiarm een stuk sneller en betrouwbaarder. De 430 S – Basisfront van GreenTec heeft een horizontaal bereik van 4,3 meter en een verticaal bereik van 4,1 meter. De GreenTec Scorpion 430S – Basisfront is gemaakt van hoogwaardig Strenx 700 staal voor een sterke en duurzame constructie. De hydraulische armdraaiing van de 430 S – Basisfront bedraagt 155 graden en bevat power control. GreenTec biedt de optie tot bediening voor zowel met- als zonder parallelle beweging (hybride armsysteem).",
        "toepassingen": ["Bermen in woonwijken","Fietspaden","Snoeien op smalle bospaden"],
        "seo_links": [("Maaiarm","/maaiarm/"),("GreenTec maaiarmen","/maaiarm/greentec/"),("Maaiarm bij bermonderhoud","/maaiarm/bermonderhoud/")],
    },
    "greentec-scorpion-830-plus-maaiarm": {
        "url": "/machine/greentec-scorpion-830-plus-maaiarm/",
        "name": "Scorpion 830 Plus maaiarm", "brand": "GreenTec", "type": "Maaiarmen",
        "kort": "Krachtige professionele maaiarm met 8,3 meter horizontaal bereik, voor intensief berm-, heg- en slootonderhoud.",
        "kenmerken": ["Horizontaal bereik 8,3 m, verticaal bereik 8,1 m","Robuuste constructie van hoogwaardig staal","155 graden hydraulische armdraaiing met power control","Hybride armsysteem: met of zonder parallelle beweging"],
        "specs": [{"k":"Horizontaal bereik","v":"8,3 m"},{"k":"Verticaal bereik","v":"8,1 m"},{"k":"Geschikt voor tractoren","v":"vanaf 8.000 kg"},{"k":"Armdraaiing","v":"155 graden"}],
        "tekst": "De GreenTec Scorpion 830 Plus is een krachtige professionele maaiarm die speciaal is ontwikkeld voor intensief berm-, heg- en slootonderhoud. Dankzij het horizontale bereik van 8,3 meter en een verticaal bereik van 8,1 meter is deze machine ideaal voor werkzaamheden langs wegen, fietspaden, watergangen en smalle bospaden. De machine is ontworpen voor grote tractoren vanaf 8.000 kg en biedt maximale stabiliteit tijdens werkzaamheden op grotere afstanden. Dankzij de grote reikwijdte kunnen bermen, taluds, heggen en boomrijen worden onderhouden zonder dat het voertuig dicht langs de werkplek hoeft te rijden, wat de veiligheid verhoogt en schade aan de ondergrond beperkt. De Scorpion 830 Plus is gemaakt van hoogwaardig staal en heeft een hydraulische armdraaiing van 155 graden met power control, en biedt een hybride armsysteem met bediening met of zonder parallelle beweging.",
        "toepassingen": ["Bermonderhoud","Heggenonderhoud","Slootonderhoud","Wegen en fietspaden","Watergangen"],
        "seo_links": [("Maaiarm","/maaiarm/"),("GreenTec maaiarmen","/maaiarm/greentec/"),("Slootonderhoud","/slootonderhoud/")],
    },
    "omarv-torino-klepelmaaier": {
        "url": "/machine/omarv-torino-klepelmaaier/",
        "name": "Torino klepelmaaier", "brand": "Omarv", "type": "Klepelmaaiers",
        "kort": "Zware klepelmaaier voor tractoren van 70 tot 140 pk, met uitworp boven de looprol, leverbaar in 6 werkbreedtes van 160 tot 260 cm.",
        "kenmerken": ["Verzwaarde rotoras met sterke hamerklepels","Verwerkt begroeiing tot 6 cm diameter","Uitworp boven de looprol voorkomt blokkades","Leverbaar in 6 werkbreedtes: 160-260 cm","Geschikt voor tractoren van 70 tot 140 pk"],
        "specs": [{"k":"Benodigd tractorvermogen","v":"70-140 pk"},{"k":"Max. diameter begroeiing","v":"ca. 6 cm"},{"k":"Werkbreedtes","v":"160-260 cm (6 uitvoeringen)"}],
        "tekst": "De Omarv Torino is een professionele klepelmaaier voor tractoren van 70 tot 140 pk. Dankzij de verzwaarde rotoras, sterke hamerklepels en robuuste constructie verwerkt deze machine moeiteloos hoog gras, dicht gewas en houtachtige begroeiing tot een diameter van circa 6 cm. De Omarv Torino is ontwikkeld voor intensief gebruik door loonwerkers, waterschappen, aannemers en terreinbeheerders die dagelijks werken onder zware omstandigheden. De combinatie van een hoge capaciteit, betrouwbare techniek en efficiënte materiaalafvoer maakt deze klepelmaaier bijzonder geschikt voor professioneel berm- en slootkantonderhoud. Wat de Omarv Torino onderscheidt van standaard maaiers, is de slimme constructie waarbij de afvoer van het gras boven de looprol plaatsvindt. Dit biedt grote voordelen: minder blokkades, ideaal bij extreem hoog gras of natte omstandigheden; de machine volgt de bodem perfect op oneffen terrein zonder dat het gemaaide materiaal de rol blokkeert; en de machine is multifunctioneel inzetbaar voor zowel regulier bermbeheer als zwaarder snoeiwerk. De Omarv Torino klepelmaaier is verkrijgbaar in 6 verschillende werkbreedtes, variërend van 160 tot 260 cm.",
        "toepassingen": ["Wegbermen","Greppels","Ruige terreinen"],
        "seo_links": [("Klepelmaaier","/klepelmaaier/"),("Omarv klepelmaaiers","/klepelmaaier/omarv/"),("Klepelmaaier voor ruw terrein","/klepelmaaier/ruw-terrein/")],
    },
    "votex-roadflex-klepelmaaier": {
        "url": "/machine/votex-roadflex-klepelmaaier/",
        "name": "Roadflex klepelmaaier", "brand": "Votex", "type": "Klepelmaaiers",
        "kort": "Veelzijdige klepelmaaier met sideshift tot bijna 250 cm: zowel vlakmaaier direct achter de trekker als zijklepelmaaier.",
        "kenmerken": ["Sideshift tot bijna 250 cm: vlakmaaier én zijklepelmaaier","Zwaartepunt blijft altijd dicht tegen de achteras","Hydraulisch veersysteem in de driepuntsbok","Actieve botsbeveiliging bij obstakels","Verhoogd transportcomfort, minder belasting op de hefinrichting"],
        "specs": [{"k":"Sideshift","v":"bijna 250 cm"}],
        "tekst": "De Votex RoadFlex is dé oplossing voor professionals die flexibiliteit eisen zonder in te leveren op stabiliteit. Dankzij de indrukwekkende sideshift van bijna 250 cm verenigt deze machine twee werelden: als vlakmaaier voor compact maaien direct achter de trekker met maximale stabiliteit en wendbaarheid in krappe ruimtes, en als zijklepelmaaier voor volledig uitgeschoven maaien naast de trekker, ideaal voor bermen en taluds. Doordat de maaibak in beide posities kort achter de trekker blijft, ligt het zwaartepunt altijd dicht tegen de achteras. Dit resulteert in een superieur rijgedrag en maximale veiligheid, ook op hellingen. Wat de RoadFlex echt onderscheidt van de concurrentie, is de innovatieve driepuntsbok, uitgerust met een geavanceerd hydraulisch veersysteem dat drie cruciale functies vervult: trillingsreductie, waarbij schokken tijdens het maaien worden geabsorbeerd voor een rustiger wegdekcontact; botsbeveiliging, die werkt als een actieve beveiliging bij het raken van obstakels; en transportcomfort, dat de stabiliteit en het comfort tijdens wegtransport verhoogt, wat de belasting op de hefinrichting van de trekker aanzienlijk verlaagt.",
        "toepassingen": ["Bermen en taluds","Compact vlak maaien","Hellingen"],
        "seo_links": [("Klepelmaaier","/klepelmaaier/"),("Votex klepelmaaiers","/klepelmaaier/votex/"),("Klepelmaaier bij bermonderhoud","/klepelmaaier/bermonderhoud/")],
    },
    "omarv-venezia-l-professionele-maai-laad-combinatie": {
        "url": "/machine/omarv-venezia-l-professionele-maai-laad-combinatie/",
        "name": "Venezia L professionele maai-laad combinatie", "brand": "Omarv", "type": "Maai-laadcombinaties",
        "kort": "De Venezia L is een professionele maai-laad combinatie met opvangbak van 10 m³, geschikt voor tractoren van 90 tot 120 pk.",
        "kenmerken": ["Opvangbak van 10 m³ met hydraulische lossing","Instelbare zijsleden voor aanpassing aan het terrein","Zelfreinigende verstelbare rol met boutbevestiging","Hydraulisch frontsysteem","Elektrisch bedieningssysteem","Elektrohydraulische maaihoogte-instelling","Werkverlichting voor veilig werken"],
        "specs": [{"k":"Rotor diameter","v":"180 mm"},{"k":"Rotor snelheid","v":"1800 rpm"},{"k":"Aftakas","v":"540 / 1000 rpm"},{"k":"Rol diameter","v":"193 mm"},{"k":"Model","v":"190 L"}],
        "tekst": "De Venezia L combineert maaien, verkleinen en opvangen in één werkgang. Deze machine is ontwikkeld voor het maaien en opvangen van gras en snoeimateriaal, zoals wijnstokken en takken tot 9 cm diameter. Dankzij de instelbare maaihoogte van 5 tot 30 cm kan de machine worden afgestemd op verschillende soorten terrein en begroeiing. Hierdoor is de machine geschikt voor professioneel groenonderhoud op grote terreinen, zoals parken, bermen, plantages en landbouwpercelen.",
        "toepassingen": ["Maaien van gras","Onderhoud van grote groenstroken","Verwerken van snoeimateriaal en wijnstokken","Professioneel terreinonderhoud"],
        "seo_links": [("Ecologisch maaien","/ecologisch-maaien/"),("Maaien met afvoer","/ecologisch-maaien/maaien-met-afvoer/")],
    },
    "herder-maaikorf": {
        "url": "/machine/herder-maaikorf/",
        "name": "Maaikorf", "brand": "Herder", "type": "Maaikorven",
        "kort": "Professionele maaikorf voor efficiënt slootonderhoud, geschikt voor maaien boven én onder water.",
        "kenmerken": ["Messen van gehard staal voor een scherpe snede","Open korfontwerp voorkomt verstoppingen","Geschikt voor maaien boven én onder water","Leverbaar in diverse werkbreedtes en uitvoeringen","Uitwisselbaar tussen verschillende Herder-machines"],
        "specs": [{"k":"Toepassing machine","v":"Minigraafmachines tot 5 ton, midi- en graafmachines, tractormachines"}],
        "tekst": "De Herder maaikorf is vervaardigd uit hoogwaardige materialen die bestand zijn tegen intensief gebruik in natte en veeleisende omstandigheden. De messen van gehard staal staan garant voor een scherpe en nauwkeurige snede. Een belangrijk kenmerk is het open korfontwerp: overtollig water stroomt direct uit de korf, terwijl gemaaide vegetatie efficiënt wordt opgevangen, wat verstoppingen voorkomt en de werksnelheid verhoogt. De maaikorf is ontworpen voor uiteenlopende werkzaamheden binnen het waterbeheer en kan zowel boven als onder water worden ingezet. De maaikorf is eenvoudig te monteren aan een maaiarm of giek en is leverbaar in verschillende uitvoeringen en werkbreedtes, van smalle sloten tot brede hoofdwatergangen, geschikt voor machines van minigraafmachines tot grote graafmachines.",
        "toepassingen": ["Maaien van riet en grasbegroeiing","Onderhoud van sloten en watergangen","Oeverbeheer","Natuurvriendelijk slootonderhoud"],
        "seo_links": [("Maaikorf","/maaikorf/"),("Herder maaikorven","/maaikorf/herder/"),("Maaikorf bij slootonderhoud","/maaikorf/slootonderhoud/"),("Slootonderhoud","/slootonderhoud/")],
    },
    "raymo-torpedo-werktuigdrager": {
        "url": "/machine/raymo-torpedo-werktuigdrager/",
        "name": "Torpedo werktuigdrager", "brand": "Raymo", "type": "Werktuigdragers",
        "kort": "Volledig elektrische, radiografisch bestuurbare werktuigdrager voor stil en emissievrij groen- en terreinonderhoud.",
        "kenmerken": ["Volledig elektrisch, geen directe uitstoot","Radiografisch bestuurbaar, veilig werken op afstand","Laag zwaartepunt en compact ontwerp voor hellingen en taluds","Powerswap-accusysteem, accu binnen 1 minuut verwisselbaar","Modulair: compatibel met verschillende maaidekken en werktuigen"],
        "specs": [{"k":"Aandrijving","v":"Volledig elektrisch"},{"k":"Bediening","v":"Radiografisch"},{"k":"Accusysteem","v":"Powerswap (verwisselbaar binnen 1 minuut)"},{"k":"Beschikbare werktuigen","v":"R42FLEX, R52TURF, R14SFINX, R48CRAFT, S46FLORIS, grashark"},{"k":"Wielopties","v":"Gazonbanden, ruwterreinbanden, spikes wielen"}],
        "tekst": "De Raymo Torpedo is een volledig elektrische en radiografisch bestuurbare werktuigdrager voor professioneel groen- en terreinonderhoud. De machine is speciaal ontwikkeld voor locaties waar stil, emissievrij en veilig werken belangrijk is. Dankzij het lage profiel, het lage zwaartepunt en de bediening op afstand is de Raymo Torpedo bijzonder geschikt voor het onderhouden van zonneparken, taluds, bermen, recreatieterreinen en andere moeilijk bereikbare locaties. Het modulaire ontwerp maakt het mogelijk om verschillende maaidekken en aanbouwwerktuigen met dezelfde machine te gebruiken, van de R42FLEX en R52TURF maaidekken tot de R14SFINX obstakelmaaier, het R48CRAFT ruwterreinmaaidek, de S46FLORIS messenbalk en een grashark. Met het Powerswap-accusysteem kan de accu in minder dan één minuut worden verwisseld, waardoor stilstand minimaal blijft en de machine gedurende een volledige werkdag kan worden ingezet. De radiografische bediening zorgt ervoor dat de gebruiker vanaf een veilige positie kan werken, met goed zicht op de machine en de omgeving.",
        "toepassingen": ["Zonneparken","Taluds en hellingen","Bermonderhoud","Sportvelden en parken","Recreatieterreinen en campings","Natuurgebieden"],
        "seo_links": [("Werktuigdrager","/werktuigdrager/"),("Werktuigdrager bij bermonderhoud","/werktuigdrager/bermonderhoud/"),("Werktuigdrager bij slootonderhoud","/werktuigdrager/slootonderhoud/")],
    },
    "herder-cr10-werktuigdrager": {
        "url": "/machine/herder-cr10-werktuigdrager/",
        "name": "CR10 werktuigdrager", "brand": "Herder", "type": "Werktuigdragers",
        "kort": "Radiografisch bestuurbare rups-werktuigdrager voor steile hellingen tot 55°, met 55 of 75 pk dieselmotor.",
        "kenmerken": ["Radiografische bediening voor veilig werken op afstand","Geschikt voor hellingen tot 55°","Variabele spoorbreedte en pendelende rupsen","Keuze uit 55 pk of 75 pk dieselmotor","Zero-turn stuursysteem"],
        "specs": [{"k":"Afmetingen (LxBxH)","v":"2,16 x 1,38 x 1,18 m"},{"k":"Massa zonder werktuig","v":"1.300-1.350 kg"},{"k":"Motor","v":"Hatz 3-cilinder 40 kW/55 pk of 4-cilinder 55 kW/75 pk"},{"k":"Rijsnelheid","v":"max. 14,5 km/u"},{"k":"Beklimbare helling","v":"55 graden"},{"k":"Emissieklasse","v":"Stage 5"}],
        "tekst": "De Herder CR10 is een krachtige radiografisch bestuurbare werktuigdrager die speciaal is ontwikkeld voor professioneel groenbeheer, bermonderhoud, taludbeheer en natuuronderhoud. Dankzij de volledige radiografische bediening kan de machinist veilig op afstand werken, terwijl de machine moeiteloos presteert op steile hellingen en moeilijk bereikbare locaties, tot 55 graden. Dankzij het lage zwaartepunt, de slimme gewichtsverdeling en het geavanceerde rupsonderstel behoudt de machine maximale grip op steile hellingen. De rupsen zijn onafhankelijk verstelbaar in spoorbreedte en pendelend uitgevoerd, waardoor zij de contouren van de ondergrond nauwkeurig volgen. Standaard is de machine uitgerust met een 55 pk watergekoelde driecilinder dieselmotor, optioneel leverbaar met een 75 pk viercilinder dieselmotor. Dankzij een breed aanbod aanbouwwerktuigen (klepelmaaier, stobbenfrees, onkruidborstel, bosbouwmaaier) kan de CR10 het hele jaar door worden ingezet.",
        "toepassingen": ["Bermonderhoud","Taludbeheer","Dijkonderhoud","Bosbeheer","Natuurbeheer"],
        "seo_links": [("Werktuigdrager","/werktuigdrager/"),("Werktuigdrager bij bermonderhoud","/werktuigdrager/bermonderhoud/"),("Taludmaaien","/taludmaaien/")],
    },
}

def card(slug, desc_override=None):
    """Compact dict voor gebruik in machines_html() op de SEO-pagina's."""
    m = MACHINES[slug]
    return {"name": m["name"], "brand": m["brand"], "url": m["url"],
            "desc": desc_override or m["kort"]}
