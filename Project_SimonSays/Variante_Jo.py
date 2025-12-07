import machine
import utime

for i in range(28):
    machine.Pin(i,machine.Pin.OUT).value(0)
    
led_red = machine.Pin(10,machine.Pin.OUT)
led_yellow = machine.Pin(11,machine.Pin.OUT)
led_green = machine.Pin(12,machine.Pin.OUT)
button_red = machine.Pin(18,machine.Pin.IN)
button_yellow = machine.Pin(17,machine.Pin.IN)
button_green = machine.Pin(16,machine.Pin.IN)
led = machine.Pin(15,machine.Pin.OUT)
        
import random

kombination=[]
punkte=0

def getNextToRemember():
    global kombination
    randomNumber=random.randint(0,2)
    color=['red','yellow','green']
    kombination.append(color[randomNumber])
    print("Ziel"+color[randomNumber])
    
def getPressedKey():
    while True:
        utime.sleep(0.4)
        if button_red.value(): return 'red'
        if button_yellow.value(): return 'yellow'
        if button_green.value(): return 'green'
        
def askForKombination():
    global kombination
    global punkte
    index=0
    for color in kombination:
        print(color)
        if color == 'red':
            led_red.value(1)
            utime.sleep(2)
            led_red.value(0)
        if color == 'yellow':
            led_yellow.value(1)
            utime.sleep(2)
            led_yellow.value(0)
        if color == 'green':
            led_green.value(1)
            utime.sleep(2)
            led_green.value(0)
    print("Now ready Input")
    #while len(kombination) > index:
    for wert in kombination:
        print(wert)
        eingabe=getPressedKey()
        print('Kombination:' +wert)
        print('Eingabe:' + eingabe)
        if wert==eingabe:
            punkte += 1
            index += 1
            print("Korrektx")
            utime.sleep(2)
        else:
            led.value(1)
            kombination=[]
            punkte=0
            return 0
            print("Ende")
    return punkte

while True:
    print("neue Runde")
    getNextToRemember()
    askForKombination()
    