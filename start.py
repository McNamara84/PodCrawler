import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

# Verifikation für die Spotify API
client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
client_secret = "d2f2bd91a62747338b6ef320fc719ce9"
# Variable
suchbegriff = "Museum"
limit = 10

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #Spotify API Objekt erstellen

result = sp.search(suchbegriff)
result['tracks']['items'][0]['artists']

#Test
print(result)