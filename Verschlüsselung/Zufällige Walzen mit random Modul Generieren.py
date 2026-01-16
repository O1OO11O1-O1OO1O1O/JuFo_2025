import random

def Walzengen(zahl):
    Speicherliste1 = []
    Speicherliste2 = []
    storage = 0
    WalzeB = []

    for x in range (0,zahl):
        storage = random.randint(1,zahl)

        if storage == zahl:
            storage = 0

        while storage in Speicherliste1:
            storage = random.randint(1,zahl)

            if storage == zahl:
                storage = 0

        Speicherliste1.append(storage)
    
    for x in range (0,zahl):
        storage = random.randint(1,zahl)

        if storage == zahl:
            storage = 0

        while storage in Speicherliste2:
            storage = random.randint(1,zahl)

            if storage == zahl:
                storage = 0

        Speicherliste2.append(storage)
    
    for x in range (0,zahl):
        WalzeB.append([Speicherliste1[x],Speicherliste2[x]])
    
    return(WalzeB)

laenge = int(input("Wie viele Zeichen soll die Walze enthalten?"))
print(Walzengen(laenge))

