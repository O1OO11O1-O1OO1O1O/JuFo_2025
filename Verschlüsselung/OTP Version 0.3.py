abc = ["A", "Ä", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Ö", "P", "Q", "R", "S", "T", "U", "Ü", "V", "W", "X", "Y", "Z", "a", "ä", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "t", "u", "ü", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", " ", "°"]
Frage = str(input("Soll etwas ver- oder entschlüsselt werden (Bitte v oder e eingeben) "))
verschluesselterSatz = []
falscheZeichen = []
endschlüssel = []
changer = 0

if Frage == "v":

    satz = str(input("Was soll verschlüsselt werden?"))
    changer = 1

if Frage == "e":

    satz = str(input("Was soll entschlüsselt werden?"))
    changer = -1

if changer != 0:
        Frage = str(input("Schlüssel aus Schlüsselspeicher verwenden? (J / n)"))
        if Frage == "J":
            
            with open(r'E:\1_Marten\Jugend Forscht\2025\Code\Python\OTP\Auf Dateien zugreifen\Zahlen.txt', 'r') as Schlüsselspeicher:
                GesSchlüsselspeicher = Schlüsselspeicher.read()

            eingabeschlüssel = GesSchlüsselspeicher[:len(satz)]

            Schlüsselspeicherneu = GesSchlüsselspeicher[len(satz):]

            with open(r'E:\1_Marten\Jugend Forscht\2025\Code\Python\OTP\Auf Dateien zugreifen\Zahlen.txt', 'w') as Schlüsselspeicher:
                Schlüsselspeicher.write(Schlüsselspeicherneu)

        if Frage == "n":
            eingabeschlüssel = str(input("Wie ist der Schlüssel?"))

if len(eingabeschlüssel) < len(satz):
    print("#####-Error-#####")
    print("Schlüssel zu kurz!")
    print("Gib einen längeren Schlüssel ein oder Fülle den Schlüsselspeicher neu auf.")
    print("#################")


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

    print("..........................")

    for durchlauf in range(0,len(satz)):

        print("satz: ", satz)
        print("Index: ", durchlauf +1)
        
        input = satz[durchlauf]
        print("input: ", input, "/", abc.index(input))
        input = abc.index(input)

        Schlüssel = eingabeschlüssel[durchlauf]
        print("Schlüssel: ", Schlüssel, "/", abc.index(Schlüssel))
        Schlüssel = abc.index(Schlüssel)
        
        verschluesselterSatz.append(abc[(input + (Schlüssel*changer))% len(abc)])
        endschlüssel.append(abc[Schlüssel])
        print(verschluesselterSatz)
        print("..........................")
    print("###############################################")
    print("Der eingegebene Satz ")
    print(satz)
    print("wurde mit dem Schlüssel ")
    print("".join(endschlüssel))
    print("zu")
    print("".join(verschluesselterSatz))
    print("vertschlüsselt!")
    print("---------------------------")
    print("------end-of-progress------")
    print("---------------------------")
    print("###############################################")

    #print(satz, " wurde mit ", "".join(endschlüssel), "zu", "".join(verschluesselterSatz), "verschlüsselt")
