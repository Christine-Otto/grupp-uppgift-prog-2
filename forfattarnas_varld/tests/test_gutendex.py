# TESTPLAN – GUTENDEX SERVICE
                # Kontrollera att appen kan hämta bokdata från Gutendex API.

# Vad som ska testas:
                # 1. API-anropet till "https://gutendex.com/books?search=dickens" ger statuskod 200.
                # 2. Svaret innehåller nyckeln 'results'.
                # 3. Varje bok innehåller 'title' och 'authors'.
                # 4. Vid tom sökning ska funktionen returnera None eller tom lista.
                # 5. Felhantering: API-fel (t.ex. 404) ska inte krascha appen.
                # 6. (Valfritt) Skriv ut antal böcker i svaret för loggning.

# Kommentar:
                # Dessa tester säkerställer att kommunikationen med Gutendex fungerar korrekt.



from services.gutendex_service import get_books

def test_get_books_returns_results():
    params = {"search": "tolstoy"}
    data = get_books(params)

    assert isinstance(data, dict)
    assert "results" in data
    assert isinstance(data["results"], list)
