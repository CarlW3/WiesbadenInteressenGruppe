import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd

def Initialize():
    """Scan and Initialze the LCD Screen"""
    # Pin Number - based on GP-Number not physical number!
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
    devices = i2c.scan()

    try:
        if devices != []:
            global lcd
            lcd = I2CLcd(i2c, devices[0], 2, 16)
            lcd.move_to(0, 0)
            lcd.putstr("Display is ready")
            return lcd
        else:
            print("No address found")
            return None
    except:
        pass

def WriteText(text):
    """Writes text to first or second row - based on the last method call"""
    lcd.putstr(text)

def Clear():
    """Clears all content from the screen"""
    lcd.clear()

def FirstRow():
    """Sets cursor to the first row"""
    lcd.move_to(0, 0)

def SecondRow():
    """Sets cursor to the second row"""
    lcd.move_to(0, 1)