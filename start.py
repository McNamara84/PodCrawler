import requests
import json

# Sollte der Token für die Spotify API abgelaufen sein, bitte mit der verification.py einen neuen Token erzeugen und hier einfügen!
token = "BQA_s7hykAMiA7vIKmN1SXfzX5PpxDK3rXXSl-6LnjhHbWk_bPZKy-JWWwvDCR4JiTwy-pXnvNv42lZwaoIBGvJQyegMI2KH5ErHimmripjgVi4T1OzV"

# Suchbegriff für den Webcrawler
sterm = "Museum"
resultcount = 50
resultcountmax = 50
filename = "ergebnisse.json"


def get_search_string():
    sterm = input("Gebe den Suchbegriff ein:\n")
    if (sterm == ""):
        print("Schreib was du Nuss!")
        get_search_string()
    if (len(sterm) >= 50):
        print("Das ist zu viel! Maximal 50 Zeichen bitte.")
        get_search_string()
    return sterm


def check_integer_input(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False


def get_result_count():
    resultcount = input("Wieviel Ergebnisse möchtest du erhalten?")
    if (check_integer_input(resultcount)):
        int(resultcount)
        return resultcount
    else:
        return resultcountmax


def search_with_string(query, token):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = (
        ('q', query),
        ('type', 'track,album,artist,show'),
    )
    response = requests.get(
        'https://api.spotify.com/v1/search', headers=headers, params=params)
    data = json.loads(response.text)
    return data


def get_result():
    result = search_with_string(sterm, token)
    return result


def clean_dict(input):
    output = json.dumps(input, indent=4)
    return output


def create_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data)
    f.close()


# Programmablauf
sterm = get_search_string()
sterm = sterm + " podcast"
ergebnis = get_result()
bereinigtes_ergebnis = clean_dict(ergebnis)
create_file(bereinigtes_ergebnis, filename)
print("JSON-Datei erfolgreich exporiert!")