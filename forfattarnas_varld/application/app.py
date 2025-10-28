# ============================================================
# Fil: app.py
# Huvudfil för Flask-applikationen "Författarens värld"
# Ansvar: starta servern, ta emot sökningar, anropa services.
# ============================================================

# FÖRFATTARENS VÄRLD – Flask-applikation
# Hanterar huvudflödet i appen.
# Tar emot formulärdata, sparar cookies,
# skickar data till services och visar resultat.


# ------------------------------------------------------------
# PLANERADE ROUTES:
#   "/"         → Startsidan med sökformulär.
#   "/search"   → Tar emot POST-data och visar resultat.
#
# Flask skickar data vidare till:
#   services/gutendex_service.py  (hämtar bokdata)
#   services/wikipedia_service.py (hämtar biografi)
#   dataops/ (rensning, analys, visualisering)
# ------------------------------------------------------------


# LOGISKT FLÖDE:
# 1. Flask tar emot formulärdata (ex. search="tolstoy").
# 2. Flask skickar data till fetch_gutendex_data().
# 3. Funktionen returnerar JSON med böcker.
# 4. Flask skickar datan vidare till dataops/transforms.py.


# -*- coding: utf-8 -*-
# Säkerställer rätt teckenkodning, särskilt om filer skapats via echo.


# ------------------------------------------------------------
# FLASK–FRONTENDKOPPLING – PLAN
# ------------------------------------------------------------
# 1. "/" (GET):
#       - Renderar index.html.
#       - Läser cookies (tidigare sökning).
#
# 2. "/search" (POST):
#       - Tar emot formulärdata.
#       - Sparar cookies (senaste sökning).
#       - Anropar services:
#             gutendex_service.get_books()
#             wikipedia_service.get_bio()
#       - Skickar resultat till results.html.
#
# Kommentar:
# Dessa två routes utgör hela användarflödet
# från formulär → resultat → ny sökning.


# ------------------------------------------------------------
# COOKIE–HANTERING – PLAN
# ------------------------------------------------------------
# - När användaren söker:
#       Flask skapar en cookie med senaste söktermerna
#       (t.ex. 'search' och 'language').
#
# - När index.html laddas igen:
#       Flask läser cookien och förifyller fälten via Jinja.
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# IMPORTER
# ------------------------------------------------------------
from flask import Flask, render_template, request, make_response
from application.services.gutendex_service import get_books
from application.services.wikipedia_service import get_bio


# ------------------------------------------------------------
# SKAPA FLASK-APP
# ------------------------------------------------------------
app = Flask(__name__)


# ------------------------------------------------------------
# ROUTE: Startsida
# ------------------------------------------------------------
@app.route("/")
def index():
    """
    Renderar startsidan (index.html).
    Läser cookie 'last_search' om den finns
    och skickar värdet till mallen för förifyllning.
    """

    # Hämta cookie med senaste sökning (None om den saknas)
    last_search = request.cookies.get("last_search", "")

    # Skicka värdet till mallen (t.ex. för att förifylla inputfältet)
    return render_template("index.html", last_search=last_search)


# ------------------------------------------------------------
# ROUTE: Sökresultat
# ------------------------------------------------------------
@app.route("/search", methods=["POST"])
def search():
    """
    Tar emot söksträng från formulär (POST), hämtar data via services,
    hanterar API-svar, sparar sökningen i cookie och visar resultat.
    """

    # Hämta söksträng och ta bort överflödiga mellanslag
    query = request.form.get("search", "").strip()

    # Skapa parametrar för API-anropet
    params = {"search": query} if query else {}

    # Hämta bokdata via Gutendex-servicen
    data = get_books(params)

    # Säkerställ att resultat alltid blir en lista
    if isinstance(data, dict):
        results = data.get("results", [])
    else:
        results = data if data else []

    # Hämta biografi (endast om söksträngen finns)
    author_info = get_bio(query) if query else None

    # Placeholder för framtida diagram
    chart_html = ""

    # Skapa svaret (response) för att kunna lägga till cookie
    response = make_response(
        render_template(
            "results.html",
            query=query,
            results=results,
            author_info=author_info,
            chart_html=chart_html
        )
    )

    # Spara senaste sökning i cookie (försvinner när andvändaren stänger webbläsaren.)
    if query:
        response.set_cookie("last_search", query)

    return response


# ------------------------------------------------------------
# TESTFUNKTION: Kontrollera mallar
# ------------------------------------------------------------
@app.route("/test_templates")
def test_templates():
    """
    Testar att Flask kan läsa in mallarna (index.html och results.html)
    utan teckenkodningsfel. Används vid felsökning.
    """
    try:
        render_template("index.html")
        render_template("results.html")
        return "Mallarna hittas och kan läsas utan problem (UTF-8 fungerar)."
    except Exception as e:
        return "Fel vid inläsning av mallar: {}".format(e)


# ------------------------------------------------------------
# STARTA SERVERN
# ------------------------------------------------------------
if __name__ == "__main__":
    """
    Startar Flask-servern i debug-läge.
    Visar fel direkt i webbläsaren och laddar om vid filändringar.
    """
    app.run(debug=True)