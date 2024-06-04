import sys
import re
print("Bitte geben Sie eine Zahl zwischen 0 und 9 ein: ")
wert = input()
if wert=="":
  sys.exit('Es wurde kein Zeichen eingegeben!')
if len(wert) != 1:
  sys.exit('Es darf nur ein Zeichen angegeben werden!')
if re.search('\D', wert):
  print ('Ihre Eingabe ist keine Zahl zwischen 0 und 9!')