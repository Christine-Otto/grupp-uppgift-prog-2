
# Arkitekturplan – Författarens värld
    Här visar vi hur appen är uppbyggd, hur datan rör sig mellan delarna och hur projektet testas.
    Appen kombinerar Gutendex (böcker) och Wikipedia (biografi) för att presentera författare och deras verk.

## Steg 1 – Miljö och verktyg
    Miljö:
        Python 3.11+, Flask, Pandas, Plotly, Requests, Pytest
        Virtuell miljö: venv/
        IDE: VS Code
    Syfte:
        Alla utvecklar i samma miljö, med samma moduler och kravfil (`requirements.txt`).

## Steg 2 – Dataflöde
    Användare → Formulär → Flask → API → Pandas/Plotly → HTML
    1. Användaren söker i `index.html`.
    2. Flask (`app.py`) tar emot datan, sparar cookie.
    3. `services/` hämtar från Gutendex + Wikipedia.
    4. `dataops/` bearbetar med Pandas och analyserar.
    5. `viz.py` skapar diagram.
    6. Resultat skickas till `results.html` för visning.

## Steg 3 – Datafält
        Gutendex: titel, författare, språk, ämnen, nedladdningar, genre, format
        Wikipedia: namn, bild, biografi, sidlänk
    Kombineras till en helhet:
        Författarprofil (Wikipedia) + Boklista (Gutendex) + Statistik (Pandas + Plotly)

## Steg 4 – Ansvar per fil
        app.py: styr flödet, cookies, routes
        services/:hämtar data från API:erna
        dataops/:rensar, analyserar, visualiserar
        templates/:visar formulär, resultat och layout
        tests/:kontrollerar att alla funktioner fungerar
    Syfte:
        tydlig separation av logik – lätt att felsöka och testa.

## Steg 5 – Backend-flöde
        1. Starta Flask och skapa routes (`/`, `/search`).
        2. Testa API-anrop i `services/`.
        3. Bearbeta data i `dataops/transforms.py`.
        4. Analysera i `analysis.py`.
        5. Visualisera i `viz.py`.
        6. Koppla ihop allt i `app.py`.
        7. Testa funktioner innan frontend kopplas på.

## Steg 6 – Frontend-flöde
        index.html: formulär med 9 parametrar, läser cookie
        results.html: visar biografi, tabell och diagram
        layout.html: gemensam mall för båda sidorna

    Syfte: användaren söker, appen visar, och nästa gång förifylls fälten automatiskt.

## Steg 7 – Tester
    Testa i denna ordning:
        1. API:er – svar och nycklar
        2. transforms – kolumner i DataFrame
        3. analysis – korrekta beräkningar
        4. viz – HTML-resultat
        5. cookies/routes – sökflöde
    Syfte: säkerställa att alla delar fungerar separat och tillsammans.


## Steg 8 – Reflektion och lärdom
    Appen visar förståelse för datainsamling, bearbetning och presentation.
    Strukturen är testbar, enkel och följer uppgiftens krav.
    Vi har lärt oss kombinera API:er, använda Pandas och skapa tydliga visualiseringar i Flask.
