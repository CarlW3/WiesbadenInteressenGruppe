# Aufgabe: Zahlenraten
import random

print("Willkommen zum Zahlenraten-Spiel!")

zufallszahl = random.randint(1, 100)
versuche = 0

while True:
    tippText = input("Gib eine Zahl zwischen 1 und 100 ein: ")
    tipp = int(tippText)
    versuche += 1
    if tipp < zufallszahl:
        print("Zu niedrig! Versuch es nochmal.")
    elif tipp > zufallszahl:
        print("Zu hoch! Versuch es nochmal.")
    else:
        print(f"Herzlichen Glückwunsch! Du hast die Zahl {zufallszahl} in {versuche} Versuchen erraten.")
        break