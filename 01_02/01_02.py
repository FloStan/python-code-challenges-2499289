print("Eingabe Datei")
dat = input()
with open(dat,"r") as eingabedatei:
    text=eingabedatei.read()
i = 1
treffer=0
zeichen = {}
while i < 255:
    treffer = text.count(chr(i))
    if treffer > 0:
        zeichen[chr(i)] = treffer
    i += 1
print(zeichen)