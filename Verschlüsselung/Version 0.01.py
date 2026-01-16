abc = ["A", "Ä", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Ö", "P", "Q", "R", "S", "T", "U", "Ü", "V", "W", "X", "Y", "Z", "a", "ä", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "t", "u", "ü", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", " ", "°"]
Frage = str(input("Soll etwas ver- oder entschlüsseltwerden (Bitte v oder e eingeben) "))
verschluesselterSatz = []
falscheZeichen = []
endschlüssel = []

if Frage == "v":

    satz = str(input("Was soll verschlüsselt werden?"))
    eingabeschlüssel = str(input("Wie ist der Schlüssel?"))
    changer = 1

if Frage == "e":

    satz = str(input("Was soll entschlüsselt werden?"))
    eingabeschlüssel = str(input("Wie ist der Schlüssel?"))
    changer = -1

for scan in range(0,len(satz)):

    if not satz[scan] in abc:
        falscheZeichen.append(satz[scan])
    
    if not eingabeschlüssel[scan] in abc:
        falscheZeichen.append(eingabeschlüssel[scan]) 
        
if len(falscheZeichen) > 0:
    print("Fehler:")
    print(len(falscheZeichen), "nicht unterstützte Zeichen wurden benutzt:")
    print(" ".join(falscheZeichen))

else:

    print("##########################")

    for durchlauf in range(0,len(satz)):

        print("satz: ", satz)
        print("Index: ", durchlauf +1)
        
        input = satz[durchlauf]  # zeichen zum verschlüsseln wird ermittelt
        print("input: ", input, abc.index(input))  # 
        input = abc.index(input) # Zeichen wird in Zahl umgewandelt

        Schlüssel = eingabeschlüssel[durchlauf] # Schlüssel Zeichen wird ermittelt
        print("Schlüssel: ", Schlüssel, abc.index(Schlüssel))
        Schlüssel = abc.index(Schlüssel) # Zeichen wird in Zahl umgewandelt
        
        verschluesselterSatz.append(abc[(input + (Schlüssel*changer))% len(abc)]) # Zeichen-Nachricht + Zeichen-Schlüssel mod länge Alphabet
        endschlüssel.append(abc[Schlüssel])
        print(verschluesselterSatz)
        print("##########################")

    print(satz, " wurde mit ", "".join(endschlüssel), "zu", "".join(verschluesselterSatz), "verschlüsselt")
