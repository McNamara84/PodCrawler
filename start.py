import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Verifikation für die Spotify API
client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
client_secret = "1d8cc3a1e3104a359046751297c36b28"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)


#Suchbegriff für den Webcrawler
sterm = "geschichte"
resultcount = 50
resultcountmax = 50

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
    results=sp.search(q=suchbegriff, limit=anzahl, type="show")
    if results and results["shows"] and results["shows"]["items"]:
        podcasts=results["shows"]["items"]
        print(podcasts)
    else:
        print("Nix GARNIX")

#get_search_string()
#resultcount = get_result_count()
search_with_string(sterm, resultcount)
