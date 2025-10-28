# ============================================================
# Fil: gutendex_service.py
# Service: Hämtar bokdata från Gutendex API baserat på sökparametrar.
# ============================================================

# ------------------------------------------------------------
# BESKRIVNING
# ------------------------------------------------------------
# Denna modul ansvarar för att hämta bokinformation från Gutendex API.
# Viktiga fält i svaret: title, authors, languages, download_count,
# subjects och bookshelves.
#
# Exempel på URL:
#   https://gutendex.com/books?search=tolstoy&languages=en
#
# Används av:
#   app.py  → funktionen get_books() kallas från /search-routen.
#
# Felhantering:
#   - Om API:et inte svarar: returnera {"results": [], "error": True}
#   - Om JSON saknar "results": returnera {"results": []}
#   - Om användaren inte angett sökterm: returnera None (app.py hoppar över anrop)
#
# Testas i test_gutendex.py:
#   - Statuskod = 200
#   - Nycklar i svaret: 'results', 'title', 'authors'
# ------------------------------------------------------------


# ------------------------------------------------------------
# IMPORTER
# ------------------------------------------------------------
import requests


# ------------------------------------------------------------
# FUNKTION: get_books()
# ------------------------------------------------------------
def get_books(parameters):
    """
    Hämtar bokdata från Gutendex baserat på angivna sökparametrar.

    Parametrar:
        parameters (dict): Exempel → {"search": "tolstoy", "languages": "en"}

    Returnerar:
        dict: JSON-svar från API med nyckeln "results" (lista med böcker).
              Om fel uppstår returneras {"results": [], "error": True}.
              Om ingen sökning anges returneras None.
    """

    base_url = "https://gutendex.com/books"

    # Om ingen sökning angetts, avbryt och returnera None
    if not parameters or not parameters.get("search"):
        return None

    try:
        # Skicka GET-anrop till Gutendex API med sökparametrar
        response = requests.get(base_url, params=parameters, timeout=10)

        # Kontrollera om API-anropet lyckades (statuskod 200)
        if response.status_code == 200:
            return response.json()

        # Om statuskod inte är 200, returnera tomt resultat med felmarkör
        print("API-svar misslyckades ({})".format(response.status_code))
        return {"results": [], "error": True}

    except Exception as e:
        # Fångar fel som nätverksproblem, timeout eller ogiltigt svar
        print("Fel vid API-anrop: {}".format(e))
        return {"results": [], "error": True}


# ------------------------------------------------------------
# FÖRKLARING
# ------------------------------------------------------------
"""
Definierar get_books(parameters) som bygger upp URL automatiskt
utifrån de parametrar användaren anger.
Exempel:
    {"search": "tolstoy"} → https://gutendex.com/books?search=tolstoy

- response.status_code kontrollerar att svaret lyckats (200 = OK)
- response.json() omvandlar API-svaret till ett Python-objekt (dict)
- Vid fel returneras alltid en säkert strukturerad dict
  för att undvika krasch i app.py
"""

