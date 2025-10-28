
IMPLEMENTERINGSPLAN
        Att planera exakt vilken fil du ska börja i, vad du lägger till där,
        och hur du stegvis testar att allt fungerar längs vägen.
        Det gör att du kan utveckla lugnt, med full kontroll och VG-struktur.

Översikt
    Appen byggs i fem etapper:
            1. Flask-grunden
            2. API-kopplingar
            3. Datahantering (Pandas + analys)
            4. Visualisering (Plotly)
            5. Integration & testning

Flask-grunden (app/application/app.py)
    Startar servern och får fram första sidan i webbläsaren.
        Steg:
            - Skapa Flask-appinstansen.
            - Lägg till route för "/" → returnerar "index.html".
            - Testa att sidan laddas utan fel (ännu utan formulär).
            - Lägg till route "/search" som tar emot POST-data (kommer användas sen).
    Testa appen tidigt – se att servern körs och HTML-sidan laddas korrekt.

API-kopplingar (services/)
        Filer:
            - gutendex_service.py
            - wikipedia_service.py
        Mål:
            Få kontakt med båda API:erna och kunna returnera data till Flask.
        Steg:
            - Implementera funktion för att hämta bokdata från Gutendex (requests + URL-parametrar).
            - Implementera funktion för att hämta biografi från Wikipedia (fallback till engelska).
            - Kontrollera att JSON-data skrivs ut korrekt i terminalen.
    Kör enkla testanrop i terminalen med "print()" innan du går vidare.

Datahantering (dataops/)
        Filer:
            - transforms.py
            - analysis.py
        Mål:
            Göra rådata läsbar och användbar.
        Steg:
            - transforms.py: omvandla JSON till Pandas DataFrame.
            - analysis.py: räkna ut enklare statistik (t.ex. antal böcker per språk).
            - Testa med sampledata innan du kopplar in API:erna.
    Här är det extra viktigt att varje funktion returnerar något testbart (lista, dict, DataFrame).

Visualisering (dataops/viz.py)
        Mål:
            Skapa en enkel, fungerande visualisering.
        Steg:
            - Skapa en funktion som tar emot DataFrame och returnerar HTML från Plotly.
            - Testa att rendera en liten tabell eller stapeldiagram.
            - Förbered för att skicka diagrammet till results.html via Flask.
    Börja med något litet – ett stapeldiagram över språk räcker för första versionen.

Integration och testning
        Mål:
            Knyt ihop allt och säkerställ att flödet fungerar.
        Steg:
            - Koppla API-funktionerna till Flask-routes.
            - Skicka data till templates via render_template().
            - Testa hela flödet: sök → API → analys → resultat.
            - Kör pytest på de testfiler du redan planerat (börja med services).
            - Fyll i cookie-hanteringen sist när allt fungerar.
    Testa ofta. Det är lättare att hitta fel när du tar ett steg i taget.
