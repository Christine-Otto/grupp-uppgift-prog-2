# Presentationsanteckningar – Författarens värld

## Projektöversikt
        Appen låter användaren utforska författare genom att kombinera data från **Gutendex** (böcker) och **Wikipedia** (biografier).  
        Syftet är att visa verk, språk, ämnen och tidsperioder på ett tydligt och interaktivt sätt.

## Roller och ansvar
        * Backend och databehandling: [ditt namn]  
        * Frontend och layout: [gruppmedlem]  
        * Tester och API-integrering: [gruppmedlem]  

## Samarbetet:
        skedde i gemensam kodmiljö i VS Code med regelbundna avstämningar och tydlig filstruktur.

## Problem och lösningar
        Vi förberedde anropet till **Gutendex** genom att först undersöka API:ets struktur manuellt.  
        Därefter planerade vi hur datan skulle hämtas, hanteras och testas steg för steg.

## Frontend-strukturen delades upp i tre delar:
        - layout.html – ramverk och gemensam mall  
        - index.html – sökformulär med nio parametrar och cookies för senaste sökning  
        - results.html – visning av biografi, boklista och diagram  

**Vanliga problem och lösningar:**
        - API-svar i fel format: Gutendex saknade ibland data → vi lade in kontroller och fallback-värden.  
        - Fel språk från Wikipedia: API:t gav ofta engelska resultat → vi lade till test för språkprioritet (sv/en).  
        - Plotly visade inget diagram: funktionen returnerade inte HTML → vi justerade `viz.py` för att generera inbäddad HTML.

## Egna lärdomar
        * Förstått hur Flask kopplar ihop frontend, backend och dataflöde.  
        * Lärt mig bearbeta API-data med Pandas och visualisera med Plotly.  
        * Insett vikten av testbara funktioner och tydlig modulstruktur.  
        * Blivit bättre på att felsöka JSON-svar och förstå API-logik.  

## Gruppreflektion
        Samarbetet fungerade bra tack vare tydlig arbetsfördelning och öppen kommunikation.  
        Vi lärde oss att uppdatera varandra ofta och hålla enhetlig kodstruktur, vilket gjorde felsökning och testning enklare.

## Presentationens upplägg
        1. Kort introduktion av idén – *Författarens värld*.  
        2. Visa flödet: sökning → API → analys → resultat.  
        3. Demo: söka på en författare.  
        4. Förklara struktur, testning och datavisualisering.  
        5. Avsluta med reflektion och möjliga förbättringar.

## VG-reflektion
        Projektet visar att vi förstått helheten – från API till användarupplevelse.  
        Vi har arbetat strukturerat, testbart och analyserat data på flera nivåer.  
        Planeringen var den mest utmanande delen, men också den som gav störst lärande.

## Slutsats
        Författarens värld visar hur öppna API:er kan ge nya perspektiv på litteratur.  
        Vi kombinerade teknik, analys och användarvänlighet i en enkel men genomtänkt app.


Absolut — här kommer en **förkortad version av din muntliga presentation**, ungefär 1,5–2 minuter lång.
Den behåller VG-nivå men är mer kondenserad och lättare att säga utan manus.
Perfekt om ni har kort presentationstid eller vill hålla tempot uppe innan demon.





## Kort muntlig version – *Författarens värld*
        Hej!

“Har du någonsin sökt efter en författare och känt att du måste hoppa mellan flera sidor för att få en hel bild?
Vem de var, vad de skrev, på vilket språk och under vilken tid?
Vi ville samla allt det i ett enda fönster – där du kan skriva in ett namn och direkt se både biografin och böckerna, tillsammans med lite statistik.
Det blev grunden till vår app, Författarens värld.”

        Vårt projekt heter Författarens värld.
        Appen låter användaren utforska författare och deras verk genom att kombinera data från två öppna API:er – Gutendex för böcker och Wikipedia för biografier.
        Målet var att visa litteraturen ur flera perspektiv – språk, ämnen och tid – på ett tydligt och interaktivt sätt.
        Användaren söker via ett formulär med nio filter, och appen sparar senaste sökningen i en cookie för att skapa ett mer personligt flöde.
## Vi delade upp arbetet i tre delar:
        Backend – Flask hanterar API-anrop, datarensning med Pandas och diagram med Plotly.
        Här hämtar Flask data,bearbetar den med Pandas och skickar den vidare till Plotly för diagram.
        Frontend – har tre mallar: layout.html, index.html och results.html.
        Tester – kontrollerar att API:er och databehandling fungerar utan fel.
        Det gjorde det lättare att samarbeta och testa varje del separat.
## Några problem vi löste:
        * Saknad data i Gutendex → la in fallback-värden.
        * Wikipedia gav ofta engelska svar → vi prioriterade svenska artiklar.
        * Plotly visade inte diagram → vi justerade funktionen till HTML-format.(ändrade funktionen så att den returnerade HTML direkt till templaten.)

        Jag har lärt mig mycket om hur Flask kopplar ihop frontend och backend,
        hur man bearbetar API-data med Pandas,
        och vikten av att skriva testbara, tydliga funktioner. (hur viktigt det är att bygga funktioner som går att testa och återanvända.)

        Kort sagt visar Författarens värld hur teknik och litteratur kan mötas –
        en enkel men genomtänkt app som kombinerar data, analys och användarvänlighet.

“Så, det var Författarens värld – en liten app som visar hur teknik kan ge nya perspektiv på litteratur.
Vi har kombinerat två öppna API:er, analyserat data med Pandas och visualiserat resultatet med Plotly.

Framför allt har vi lärt oss att planering och testning är lika viktiga som själva koden.
Tack.”
