import turtle

# A: Frag den Benutzer nach Farbe, Strichdicke und Größenfaktor
print("Welche Farbe möchten Sie?")
farbe = input("red, green, blue: ").lower()

# Validierung der Farbeingabe
if farbe not in ["red", "green", "blue"]:
    print("Unbekannte Farbe, verwende Schwarz")
    farbe = "black"

dicke = int(input("Wie dick soll der Strich sein? "))
faktor = float(input("Wie groß soll die Zeichnung sein (als Faktor)? "))

# B: Turtle konfigurieren und Form zeichnen
t = turtle.Turtle()
t.speed(8)

# Stift-Eigenschaften setzen
t.color(farbe)
t.pensize(dicke)

# Einen 9-zackigen Stern zeichnen
def zeichne_stern(turtle, groesse):
    for i in range(9):
        turtle.forward(groesse)
        turtle.right(160)

# Stern mit dem Größenfaktor zeichnen
grundgroesse = 100
sterngroesse = grundgroesse * faktor

print(f"Zeichne einen {farbe}en Stern mit Strichdicke {dicke} und Größe {sterngroesse}")
zeichne_stern(t, sterngroesse)

# Turtle-Fenster offen halten
turtle.done()
