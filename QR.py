import qrcode # type: ignore

def QRgen(name, inhalt):
    img = qrcode.make(inhalt)
    img.save(name)
    img.show()

QRgen("QR_Code.png", str(input("Was soll in den QR-Code?")))
