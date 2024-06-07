import math
import random

x = 0
y = 0
z = 0
op = 0
weg = 0
erg = ""
ausdruck = ["","","","=",""]
fehlenderToken=""
print("Sie sehen nachfolgend einen mathematischen Ausdruck, der entweder eine \n Addition (+),\n Substraktion (-) oder\n Multiplikation (*) zweier einstelliger Zahlen beschreibt.")
print("Es fehlt aber ein Token (Zahl oder Rechenoperator) in dem Ausdruck, den Sie ergänzen sollen.")

while True:
  x = random.randint(1,9) # Bestimmung erste Zahl - zufälliger Wert aus 1 bis 9
  y = random.randint(1,9) # Bestimmung zweite Zahl - zufälliger Wert aus 1 bis 9
  ausdruck[0] = str(x)
  ausdruck[2] = str(y)
  op = random.randint(0,2) # 3 Operationen - zufällige Auswahl
  weg = random.randint(0,3)  # zu eliminierendes Zeichen - zufällige Auswahl
  
  if op == 0:
    ausdruck[1] = "+"
    z = x+y
  elif op == 1:
    ausdruck[1] = "-"
    z = x-y
  else:
    ausdruck[1] = "*"
    z = x*y
  ausdruck[4] = str(z)

  if weg == 3:
    erg=ausdruck[4]
    ausdruck[4]="?"
  else:
    erg=ausdruck[weg]
    ausdruck[weg]="?"
  s = ' '.join(ausdruck)
  print("Wie wird der folgende Ausdruck ergänzt, damit er mathematisch korrekt ist?\n\t",s)#s statt ausdruck
  fehlenderToken=input("An der Position des Fragezeichens fehlt entweder eine Zahl oder ein Operator.\nGeben Sie die fehlende Zahl oder die fehlende Operation (+,-,*) ein.\n")
  if fehlenderToken == erg:
    print("Korrekte Antwort.")
  else:
    print("Leider falsch. Mit '", erg,"' anstelle des Fragezeichens ist der Ausdruck mathematisch korrekt.")
  if input("Weiterer Test (Y/N)?\n").upper()=="N":
    break