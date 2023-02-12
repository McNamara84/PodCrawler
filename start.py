import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Verifikation für die Spotify API
client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
client_secret = "d2f2bd91a62747338b6ef320fc719ce9"

# Variablen, die der Nutzer festlegen soll
suchbegriff = "Museum"
limit = 10

# Spotify API Objekt erstellen
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# TODO Katja: Funktion, die den Nutzer nach Start des Programms fragt, welcher Suchbegriff 
# gecrawlt werden soll und danach wieviele Treffer angezeigt werden sollen. Beides gerne als 
# Unterfunktionen nach folgendem Muster: def user_ask():

# Funktionsaufruf für Suche
#Aufbau wie? def bla bla eingabe suchbegriff + eingabe anzahl (das wäre aber nervig wenn man das immer 
# eingeben muss)
#oder aufbau def unterdef eingabe suchbegriff rückgabe unterdef eingabe anzahl return (wie gesagt würde 
#ich nicht eingeben wollen)
#die variable mit dem suchbegriff muss wohin? oder nur returnen und dann?
#wie sucht der den String dann in der spotify bibliothek = was ist zu beachten?
#können wir die anzahl standardisieren bzw extra eingeben lassen einmal und nicht jedesmal?
# was meint result =sp.search suchbegriff? ist das der befehl der in der 
#spotifiy bib suchen lässt? dann muss ich auf jeden fall die variable suchbegriff nennen oder?
#was muss in die klammer bei user_ask?
def user_ask():
    suchbegriff=input("Was suchst du?")
    return(suche)
    anzahl=input("Wieviel Treffer willst du haben?")
    return(anzahl)
result = sp.search(suchbegriff)

# TODO Holger: JSON-String formatieren und als Datei abspeichern.

result['tracks']['items'][0]['artists']

# Testbereich
print(result)