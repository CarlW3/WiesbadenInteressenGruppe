# Aufgabe: Notizen Tool

import os
from datetime import datetime

dateiName="Notizen.txt"

print("Willkommen zum Notizen Tool!")

# Vorhandene Notizen anzeigen
if os.path.exists(dateiName):
    with open(dateiName, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

# Neue Notiz eingeben
print("\nGeben Sie Ihre neue Notiz ein:")
neue_notiz = input("> ")

# Notiz mit Zeitstempel speichern
if neue_notiz.strip():
    zeitstempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notiz_mit_zeitstempel = f"[{zeitstempel}] {neue_notiz}\n"
    if neue_notiz.strip():
        with open(dateiName, 'a', encoding='utf-8') as file:
            file.write(notiz_mit_zeitstempel)
        print(f"\nNotiz wurde erfolgreich zu '{dateiName}' hinzugefügt!")

