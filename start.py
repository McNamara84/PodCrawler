import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Verifikation für die Spotify API
client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
client_secret = "d2f2bd91a62747338b6ef320fc719ce9"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)


#Suchbegriff für den Webcrawler
sterm = "geschichte"
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
        return resultcount
    else:
        return resultcountmax

def search_with_string(suchbegriff, anzahl):
    sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results=sp.search(q=suchbegriff, limit=anzahl, type="podcasts")
    podcasts=results["shows"]["items"]
    print(podcasts)

#get_search_string()
#resultcount = get_result_count()
search_with_string(sterm, resultcount)
