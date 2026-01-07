# Install lib: pip install requests

import requests
# Beispiel-URL 
url="https://restcountries.com/v3.1/name/germany"
# GET-Request senden
response = requests.get(url)

# Überprüfen, ob der Request erfolgreich war
if response.status_code == 200:
    # Antwort als JSON ausgeben
    data = response.json()
    print("Erfolg! Daten empfangen:")
    print(data)
else:
    print(f"Fehler: {response.status_code}")
