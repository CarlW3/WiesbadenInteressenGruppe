import random

kombination=[]
punkte=0

def getNextToRemember():
    global kombination
    randomNumber=random.randint(1,4)
    print(f"##### Neue Zahl: {randomNumber}")
    print("####################################")
    kombination.append(randomNumber)
    return randomNumber

def askForKombination():
    global kombination
    global punkte
    index=0
    while len(kombination) > index:
        eingabe = input(f"{index+1}. Zahl [1|2|3|4]  : ")
        eingabeZahl=int(eingabe)
        if kombination[index]==eingabeZahl:
            punkte += 1
            index += 1
        else:
            print(f"### Falsch - ENDE - Punkte: {punkte}")
            kombination=[]
            punkte=0
            return 0
    print()
    return punkte

while 1==1:
    getNextToRemember()
    askForKombination()
    print()
