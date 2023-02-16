import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Verifikation für die Spotify API
client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
client_secret = "d2f2bd91a62747338b6ef320fc719ce9"

#Suchbegriff für den Webcrawler
sterm = ""
resultcount = 20
resultcountmax = 100

def get_search_string():
    sterm = input("Gebe den Suchbegriff ein:\n")
    if (sterm==""):
        print("Schreib was du Nuss!")
        get_search_string()
    if (len(sterm)>=50):
        print("Das ist zu viel! Maximal 50 Zeichen bitte.")
        get_search_string()

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
        print(resultcount)
        return resultcount
    else:
        return resultcountmax

#get_search_string()
resultcount = get_result_count()
print(resultcount)