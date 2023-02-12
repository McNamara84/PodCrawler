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

## Wir sind da relativ frei. Wenn du es so nicht haben wollen würdest, wie dann? Wenn du es besser findest,
## können wir auch Suchbegriff und Limit als (optionale) Parameter entgegen nehmen
## (so dass Nutz:innen "start.py suchbegriff limit eingeben müssen beim Programmstart).

#die variable mit dem suchbegriff muss wohin? oder nur returnen und dann?

## Die Variable existiert bereits und ist per default mit "Museum" belegt. Die Funktion sollte diese
## Variable einfach nur überschreiben und stattdessen den neuen Suchbegriff speichern.

#wie sucht der den String dann in der spotify bibliothek = was ist zu beachten?

## Die Suche passiert aktuell in der Zeile 58: result = sp.search(suchbegriff), da ist erstmal nichts
## weiter zu beachten.

#können wir die anzahl standardisieren bzw extra eingeben lassen einmal und nicht jedesmal?

## Ja, klar! Würde als separate Funktion auch sehr gut funktionieren!

# was meint result =sp.search suchbegriff? ist das der befehl der in der 
#spotifiy bib suchen lässt? dann muss ich auf jeden fall die variable suchbegriff nennen oder?

## Ja, die Varibale suchbegriff muss den Suchbegriff enthalten. Die Funktion kommt aus der Spotipy Bib.

#was muss in die klammer bei user_ask?

## Nichts, denn die Funktion erfragt ja nur etwas und braucht dazu keinen Parameter. ;-)

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