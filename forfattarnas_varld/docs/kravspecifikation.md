
* vad appen gör
* vilka parametrar du valt
* och varför.

# Kravspecifikation – Författarens värld
## Syfte
    Appen låter användaren söka efter en författare och utforska deras verk, språk och teman.
    Den kombinerar **Gutendex API** (böcker) och **Wikipedia API** (biografi) för att ge en helhetsbild av författarens värld.
---
## Våra 9 sökparametrar
    Appen använder nio parametrar från Gutendex för att styra sökningen:
        1. **search** – textfält, sökord (författare/titel).
        2. **languages** – dropdown, språkfilter (ex. en, sv, fr).
        3. **subjects** – textfält, tema eller ämne.
        4. **author_year_start** – tal, filtrerar på födelseår.
        5. **author_year_end** – tal, filtrerar på dödsår.
        6. **sort** – dropdown, sorterar efter popularitet.
        7. **mime_type** – dropdown, filtrerar filformat.
        8. **bookshelves** – dropdown, filtrerar genre.
        9. **page** – tal, sidnummer vid många resultat.
    Dessa parametrar gör sökningen flexibel och ger flera perspektiv på datan.

## Motivering
    Parametrarna valdes för att passa temat: tid, språk, ämne och format.
    Kombinationen gör det möjligt att analysera verk ur olika epoker och språk.
    **search** är kärnan, de övriga filtrerar och sorterar resultatet.

## Dataflöde
    1. Användaren fyller i formuläret (index.html).
    2. Flask tar emot värdena, sparar dem i en cookie.
    3. Gutendex och Wikipedia hämtar data via services.
    4. Data bearbetas med Pandas och visualiseras med Plotly.
    5. Resultat visas i results.html (biografi, tabell, diagram).

## VG-reflektion
    Projektet visar förståelse för hur API:er kan kombineras och data bearbetas.
    Parametrarna är valda med fokus på användarupplevelse och analysmöjligheter.
    Strukturen gör appen testbar, tydlig och pedagogiskt byggd från grunden.


