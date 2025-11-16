# Wie funktioniert es?
Kopiere alle Dateien auf Raspeberry Pi Pico (W)

Passe Initialize Methode in display.py an:

    # Pin Number - based on GP-Number not physical number!
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

Nutze den Wrapper display.py oder greife direkt auf die Library zu.
