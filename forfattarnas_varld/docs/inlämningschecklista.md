## INLÄMNINGS­CHECKLISTA & SLUTFÖRBEREDELSER
        Att säkerställa att allt i projektet fungerar tekniskt, är dokumenterat och följer kursens krav.

DEL 1: TEKNISK GENOMGÅNG
    Flask-applikationen körs utan fel:
            - Appen startar via terminalen (python app.py).
            - Startsidan (index.html) laddas.
            - Resultatsidan (results.html) visas efter sökning.
            - Inga felmeddelanden i konsolen.

    API-anropen fungerar**
            - Gutendex returnerar bokdata (kontrollerat via print() eller logg).
            - Wikipedia returnerar biografidata.
            - Felhantering vid saknad data fungerar (fallback).

    Datahantering
            - Data omvandlas korrekt till DataFrame.
            - Statistik skapas i `analysis.py`.
            - Diagram genereras med Plotly (HTML returneras).
            - Diagrammet visas på resultatsidan.

    Cookies
            - Senaste sökningen sparas.
            - Formuläret förifylls vid nästa besök.


DEL 2: TESTNING
    Tester
            - test_gutendex.py körs och passerar.
            - test_wikipedia.py körs och passerar.
            - test_transforms.py körs och passerar.
            - Fler tester kan läggas till för analysis.py och viz.py.

Funktioner returnerar testbara värden
            - Alla funktioner i services och dataops returnerar något (dict, DataFrame eller HTML).
            - Undviker “print-only”-lösningar i logiken.


DEL 3: DOKUMENTATION
    README.md
            - Innehåller kort projektbeskrivning, syfte och installationssteg.
            - Har exempel på användning.
            - Förklarar hur man startar appen.

    Kravspecifikation.md
            - Förkortad version av dina 9 parametrar (tydligt och komplett).
            - Motivering till varför de valdes.
            - Koppling till formulär och användning.

    Arkitekturplan.md
            - Beskriver filstruktur, dataflöde och roller.
            - Har en tydlig översikt över hur allt hänger ihop.

Presentation & anteckningar
            - Presentationsanteckningar.md uppdaterad.
            - Kort muntlig version klar.
            - 30-sekunders intro + avslutning förberedda.

DEL 4: SLUTKONTROLL (VG-KRITERIER)
    Tydlig struktur
            - Koden är uppdelad i logiska moduler (app, services, dataops, tests, templates).
            - Namngivning är konsekvent och förklarande.

    Återanvändbarhet och testbarhet
            - Funktioner kan köras separat.
            - Tester använder returvärden, inte bara utskrift.

Reflektion och analys
            - Presentationen beskriver både vad du byggt och vad du lärt dig.
            - Dokumentationen visar förståelse för API-flöden och databehandling.

DEL 5: SLUTSTEG
    När alla punkter är avbockade:
            1. Kör hela appen en sista gång.
            2. Kontrollera att diagrammet visas.
            3. Läs igenom README och presentationsanteckningar en gång till.
            4. Packa allt i en mapp (utan venv/) inför inlämningen.
            5. Ladda upp till lärplattformen.

Avslutande reflektion:
            “Projektet har gett förståelse för hur man bygger en hel applikation – från datainsamling till visuell presentation.
            Jag har lärt mig planera, testa och dokumentera på ett sätt som gör att koden går att förstå även i efterhand.”