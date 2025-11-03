# Aufgabe: Rechnen Tool

print("Willkommen zum Rechnen Tool!")

# Zoll in cm Umrechner
zahlText=input("Länge in Zoll:")
zahl=int(zahlText)
cm=zahl*2.54
print(f"{zahl} Zoll sind {cm} cm.")

# Rechteck Flächen- und Umfangsrechner
laengeText=input("Länge in cm:")
breiteText=input("Breite in cm:")
# Umwandlung in Zahl
laenge=int(laengeText)
breite=int(breiteText)
flaeche=laenge*breite
print(f"Die Fläche eines Rechtecks mit der Länge {laenge} cm und der Breite {breite} cm ist {flaeche} cm².")
print(f"Der Umfang eines Rechtecks mit der Länge {laenge} cm und der Breite {breite} cm ist {2*(laenge+breite)} cm.")

# Weitere Varianten:
# float für Kommazahlen
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

print(f"Die Summe von {zahl1} und {zahl2} ist {zahl1 + zahl2}.")
print(f"Die Differenz von {zahl1} und {zahl2} ist {zahl1 - zahl2}.")
print(f"Die Produkt von {zahl1} und {zahl2} ist {zahl1 * zahl2}.")
print(f"Die Quotient von {zahl1} und {zahl2} ist {zahl1 / zahl2}.")