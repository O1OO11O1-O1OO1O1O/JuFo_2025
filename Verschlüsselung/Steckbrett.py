
wdhs = int(input("Wie viele Zeichen sollen auf dem Steckbrett vertauscht werden? (Es können Maximal 13 Zeichen vertauscht werden)"))
abc = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R","S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z" ]
vertauschungen = []
counter = 0

def löschenAusABC(zeichen):
    erfolg = 0
    counter2 = 0
    while erfolg == 0:
        if abc[counter2] == zeichen:
            erfolg = 1
            del(abc[counter2])
        counter2 = counter2 + 1



if wdhs <= 13:

    while counter < wdhs:
        
        storage = str(input("Welches Zeichen soll vertauscht werden? (Es werden nur die 26 Großbuchstaben der Lateinischen Alphabets unterstützt)"))

        if storage in abc:
            storage2 = str(input("Mit welchem Zeichen soll es vertauscht werden? (Es werden nur die 26 Großbuchstaben der Lateinischen Alphabets unterstützt)"))
            
            if storage2 in abc:
                vertauschungen.append([storage,storage2])
                vertauschungen.append([storage2,storage])
                löschenAusABC(storage)
                löschenAusABC(storage2)
                counter = counter + 1
                print(counter, " / ", wdhs)


            else:
                print("Ungültiges Zeichen:" ,storage2 ," wird nicht unterstützt")

        else:
            print("Ungültiges Zeichen:" ,storage ," wird nicht unterstützt")
            
        

else:
    print("Es können nur Maximal 13 Zeichen vertauscht werden")

print(vertauschungen)
print(abc)

abc = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R","S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z" ]

while True:
    storage = str(input("Welches Zeichen soll verschlüsselt weden? (Es werden nur die 26 Großbuchstaben der Lateinischen Alphabets unterstützt)"))
    antwort = storage


    if len(storage) == 1:

        if storage in abc:
            for x in range(0,len(vertauschungen)):
                if storage == vertauschungen [x] [0]:
                    antwort = vertauschungen [x] [1]
                    
            print(storage, " wurde zu ",antwort , " Verschlüsselt")

        else:
            print("Ungültiges Zeichen:" ,storage ," wird nicht unterstützt")

    else:
        print("Es Weden nur einzelnde Zeichen unterstützt")
