1. Användaren öppnar appen
            → Flask renderar index.html
            → Läser cookies (om någon tidigare sökning finns)

2️. Användaren fyller i formuläret
            → Trycker på “Sök”
            → Flask tar emot POST-data från formuläret

3️. Flask skickar data till services
            → gutendex_service.py: hämtar bokdata
            → wikipedia_service.py: hämtar biografi

4️. Flask skickar rådata till dataops
            → transforms.py: rensar och strukturerar datan i en DataFrame
            → analysis.py: räknar statistik (t.ex. språkfördelning)
            → viz.py: skapar ett Plotly-diagram (HTML-format)

5️. Flask skickar resultaten till results.html
            → Biografi visas högst upp
            → Boktabell under
            → Diagram längst ned

6️. results.html använder layout.html som mall
            → Header, footer och gemensam stil hämtas automatiskt

7️. När användaren söker igen
            → Flask läser cookien och fyller i tidigare värden i formuläret.


Förklaringar per del
    Frontend (templates/)
                index.html: samlar in sökparametrar.
                results.html: visar data.
                layout.html: gemensam struktur för hela appen.
    Backend (app.py + services/)
                app.py: tar emot formulärdata, anropar tjänster, skickar svar till HTML.
                gutendex_service.py: kontakt med Gutendex API.
                wikipedia_service.py: kontakt med Wikipedia API.
    Datahantering (dataops/)
                transforms.py: omvandlar rå JSON till tabellformat (DataFrame).
                analysis.py: räknar statistik (antal böcker, språk, ämnen).
                viz.py: skapar interaktiv visualisering (Plotly).