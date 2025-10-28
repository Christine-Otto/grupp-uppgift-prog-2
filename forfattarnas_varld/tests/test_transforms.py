# TESTPLAN – DATAOPS: TRANSFORMS
                # Kontrollera att rådata från Gutendex kan rensas och omvandlas till en DataFrame.

# Vad som ska testas:
                # 1. Funktionen returnerar en Pandas DataFrame.
                # 2. DataFrame innehåller kolumner: title, authors, languages, download_count.
                # 3. Tomma värden hanteras korrekt (inga krascher).
                # 4. Felaktig eller ofullständig data (saknad nyckel) ger hanterbart svar.
                # 5. Funktionen kan hantera en liten testfil (sample_data.json).

# Kommentar:
                # Dessa tester säkerställer att data är i rätt format innan analys.



import pandas as pd
from dataops.transforms import clean_data

def test_clean_data_creates_dataframe_with_columns():
    # minimal testdata
    dummy_json = {
        "results": [
            {
                "title": "Testbok",
                "authors": [{"name": "Författare A"}],
                "languages": ["sv"],
                "download_count": 10
            }
        ]
    }

    df = clean_data(dummy_json)

    assert isinstance(df, pd.DataFrame)
    for col in ["title", "authors", "languages", "download_count"]:
        assert col in df.columns
    assert len(df) == 1
