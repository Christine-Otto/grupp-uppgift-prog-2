*Ytterligare planeringsdokument finns i /docs för att visa utvecklingsprocessen (flödesplan, implementeringsplan, inlämningschecklista).*

## Författarens värld
        En webbaserad applikation som låter användaren utforska författare, deras verk och litterära epoker.
        Appen kombinerar data från två öppna API:er: **Gutendex** (böcker) och **Wikipedia** (biografier).

Syfte och mål:
        Syftet med projektet är att visa hur man kan kombinera flera externa API:er i en Flask-applikation
        och presentera resultaten på ett strukturerat och interaktivt sätt.

Användaren kan:
        - Söka på författare.
        - Filtrera efter språk, ämne, årtal och format.
        - Se författarens biografi, verk och nedladdningsstatistik.
        - Få resultaten visualiserade i ett interaktivt diagram.

Projektgrupp:
        Backend & databehandling:  [Christine]  
        Frontend & layout:         [Markus] 
        Tester & API-integrering:  [Christine och Markus] 

Funktioner
        - Sökformulär med 9 parametrar (t.ex. språk, år, ämne, format).
        - Data hämtas från Gutendex API och Wikipedia API.
        - Cookies sparar senaste sökning.
        - Datan bearbetas med Pandas och visualiseras med Plotly.
        - Strukturerad visning i tabell och diagram.
        - Tester i pytest för att säkerställa stabilitet.

Projektstruktur
        app/
        ├── application/
        │   ├── app.py                # Flask-appens kärna
        │   ├── services/             # API-anrop (Gutendex + Wikipedia)
        │   ├── dataops/              # Datahantering (Pandas, Plotly)
        │   └── templates/            # HTML-sidor (index, results, layout)
        │
        ├── tests/                    # Testfiler för services och dataops
        └── docs/                     # Planering, specifikation, presentation


Installation och körning
        Kopiera projektet
                cd forfattarens_varld

        Skapa virtuell miljö
            python -m venv venv

        Aktivera miljön:
            - Windows:
                venv\Scripts\activate
            - macOS/Linux:
                source venv/bin/activate

        Installera beroenden:
            pip install -r requirements.txt

        Starta appen:
            python app.py 

        Öppna i webbläsaren
            http://127.0.0.1:5000

Tester:
        Kör alla tester:
            pytest

Exempel på testfiler:
            - test_gutendex.py → kontrollerar API-anrop till Gutendex.
            - test_wikipedia.py → kontrollerar biografidata.
            - test_transforms.py → säkerställer att data konverteras korrekt.

Dataflöde (översikt):
        index.html (formulär)
        ↓
        Flask (app.py)
        ↓
        services/
        ├─ gutendex_service.py  → boklista
        └─ wikipedia_service.py → biografi
        ↓
        dataops/
        ├─ transforms.py → DataFrame
        ├─ analysis.py   → statistik
        └─ viz.py        → diagram (Plotly)
        ↓
        results.html → visar tabell + diagram

Exempel på användning:
        1. Skriv t.ex. Tolstoy i sökfältet.
        2. Välj språk “en” och genre “Philosophy”.
        3. Klicka på *Sök*.
        4. Appen visar:
                - Kort biografi från Wikipedia.
                - Lista med böcker från Gutendex.
                - Ett diagram över språkfördelningen i hans verk.

Lärdomar:
        - Förståelse för hur Flask kopplar ihop frontend, backend och data.
        - Hantering av externa API:er och JSON-data.
        - Dataanalys med Pandas och visualisering med Plotly.
        - Vikten av testbarhet, struktur och dokumentation.

Slutsats
        Författarens värld visar hur man kan förena litteratur och teknik i ett konkret projekt.
        Genom att kombinera öppna datakällor med tydlig struktur och testning skapade vi en app som både informerar och inspirerar.