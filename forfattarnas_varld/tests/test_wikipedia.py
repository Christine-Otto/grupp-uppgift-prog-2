# TESTPLAN – WIKIPEDIA SERVICE          
                # Testa att appen kan hämta biografidata från Wikipedia API.

# Vad som ska testas:
                # 1. API-anropet ger statuskod 200 för kända författare (t.ex. Tolstoy).
                # 2. Svaret innehåller 'extract' (biografitext) och 'title'.
                # 3. Om artikeln saknas på svenska, ska funktionen försöka på engelska ('en').
                # 4. Vid ogiltigt namn (t.ex. “asdfghjkl”) ska funktionen inte krascha.
                # 5. Bild och länk returneras korrekt om de finns.

# Kommentar:
                # Dessa tester säkerställer att appen klarar både normala och ovanliga API-svar.



from services.wikipedia_service import get_bio

def test_get_bio_returns_text_and_title():
    author = "Leo Tolstoy"
    bio = get_bio(author)

    assert isinstance(bio, dict)
    assert "title" in bio
    assert "summary" in bio
    assert isinstance(bio["title"], str)
    assert isinstance(bio["summary"], str)
