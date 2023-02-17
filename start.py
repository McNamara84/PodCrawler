import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

# Verifikation für die Spotify API
#client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
#client_secret = "1d8cc3a1e3104a359046751297c36b28"
#client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
token = "BQBjDfxRtF7930btT-F6cb05a6QjVTdNflDv4FWA4jOPdbsvSKhHy-NSNxqkJjQULNtoayMQ5IOysHmAn2y4MsDsnGC-89W1YOTwIZ3EKz3KDFXuLLDd"


#Suchbegriff für den Webcrawler
sterm = "wissenschaft"
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
    client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
    client_secret = "1d8cc3a1e3104a359046751297c36b28"
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.search(q='arist:' + suchbegriff, limit=anzahl, offset=0, type='episode', market=None)
    return result

def search_spotify(query, token):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = (
        ('q', query),
        ('type', 'track,album,artist,show'),
    )
    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    data = json.loads(response.text)
    return data

#get_search_string()
#resultcount = get_result_count()
#print(search_with_string(sterm, resultcount))

# Suchbegriff = wissenschaft podcast 
sterm = sterm + " podcast"
print(json.dumps(search_spotify(sterm, token), indent=4))