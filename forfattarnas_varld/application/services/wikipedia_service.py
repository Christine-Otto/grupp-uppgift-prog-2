# ============================================================
# Fil: wikipedia_service.py
# Service: Hämtar kort biografi om författare från Wikipedia.
# ============================================================

# ------------------------------------------------------------
# BESKRIVNING
# ------------------------------------------------------------
# Denna modul hämtar en kort biografi för en given författare
# genom att anropa Wikipedias REST API.
#
# Flöde:
#   1. Försök hämta på svenska (sv.wikipedia.org)
#   2. Om ingen data hittas → försök på engelska (en.wikipedia.org)
#   3. Om båda misslyckas → returnera ett standardmeddelande
#
# Returnerar ett dictionary med följande nycklar:
#   - title:   Artikelns titel
#   - summary: Kort text (extract)
#   - image:   Länk till eventuell miniatyrbild
#   - url:     Länk till hela artikeln
#
# Felhantering:
#   - Om API:et inte svarar → returnera standardtext
#   - Om artikel saknas på båda språken → returnera tom biografi
# ------------------------------------------------------------


# ------------------------------------------------------------
# IMPORTER
# ------------------------------------------------------------
import requests


# ------------------------------------------------------------
# FUNKTION: get_bio()
# ------------------------------------------------------------
def get_bio(author_name):
    """
    Hämtar en kort biografi om en författare från Wikipedia API.

    Parametrar:
        author_name (str): Namnet på författaren som ska sökas.

    Returnerar:
        dict: Ett dictionary med nycklarna:
              "title", "summary", "image", "url"

        Om inget hittas returneras:
              {
                  "title": author_name,
                  "summary": "Ingen data hittades för denna författare.",
                  "image": None,
                  "url": None
              }
    """

    # --------------------------------------------------------
    # INRE FUNKTION: fetch(lang)
    # --------------------------------------------------------
    def fetch(lang):
        """
        Försöker hämta biografi från Wikipedia på angivet språk.
        Exempel på URL:
            https://sv.wikipedia.org/api/rest_v1/page/summary/Selma_Lagerlöf
        """

        # Bygger URL med .format() så att rätt språk och namn sätts in
        url = "https://{}.wikipedia.org/api/rest_v1/page/summary/{}".format(lang, author_name)

        try:
            # Skicka GET-anrop till Wikipedia API
            response = requests.get(url, timeout=10)

            # Kontrollera att svaret lyckades
            if response.status_code == 200:
                data = response.json()

                # Returnera relevant information i en strukturerad dict
                return {
                    "title": data.get("title", "Okänd titel"),
                    "summary": data.get("extract", "Ingen text tillgänglig"),
                    "image": data.get("thumbnail", {}).get("source"),
                    "url": data.get("content_urls", {}).get("desktop", {}).get("page")
                }

        except Exception as e:
            # Skriver ut fel om API-anropet misslyckas (t.ex. timeout eller ogiltigt namn)
            print("Fel vid Wikipedia-anrop ({}): {}".format(lang, e))

        # Om anropet inte lyckades, returnera None så nästa språk testas
        return None

    # --------------------------------------------------------
    # 1. Försök först hämta på svenska
    # --------------------------------------------------------
    result = fetch("sv")
    if result:
        return result

    # --------------------------------------------------------
    # 2. Om inget hittas på svenska, försök på engelska
    # --------------------------------------------------------
    result = fetch("en")
    if result:
        return result

    # --------------------------------------------------------
    # 3. Om inget hittas alls, returnera standardmeddelande
    # --------------------------------------------------------
    return {
        "title": author_name,
        "summary": "Ingen data hittades för denna författare.",
        "image": None,
        "url": None
    }


# ------------------------------------------------------------
# FÖRKLARING
# ------------------------------------------------------------
"""
Flöde:
1. get_bio() tar emot ett författarnamn från app.py.
2. fetch("sv") försöker hämta artikeln från svenska Wikipedia.
3. Om den inte finns, kallas fetch("en").
4. Om båda misslyckas, returneras ett standard-dictionary.

- requests.get() används med timeout=10 sekunder för säkerhet.
- .get() används på JSON-fält för att undvika KeyError om data saknas.
- Funktionen är skriven så att appen aldrig kraschar även om Wikipedia
  inte svarar eller om artikeln inte finns.
"""
