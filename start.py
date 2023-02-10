import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Verifikation für die Spotify API
client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
client_secret = "d2f2bd91a62747338b6ef320fc719ce9"

# Variablen, die der Nutzer festlegen soll
suchbegriff = "Museum"
limit = 10
dateiname = "Ergebnisse.json"

# Spotify API Objekt erstellen
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# TODO Katja: Funktion, die den Nutzer nach Start des Programms fragt, welcher Suchbegriff gecrawlt werden soll und danach wieviele Treffer angezeigt werden sollen. Beides gerne als Unterfunktionen nach folgendem Muster:
# def user_ask():

# Funktionsaufruf für Suche
result = sp.search(suchbegriff)

# BUG Holger: Fehlerbehebeung -> Funktion speichert bisher nur Strings und keine Dictionaries.
def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    print("Datei wurde erfolgreich gespeichert.")

result['tracks']['items'][0]['artists']

# Testbereich
print(result)
write_to_file(dateiname, result)