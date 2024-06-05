warenkorb = {}
abbruch = False
print('Willkommen zu Ihrem Shoppingassistenten.')
while abbruch == False:
  print('Geben Sie Ihr gewünschtes Produkt ein: ')
  prod = input()
  print('Geben Sie die gewünschte Anzahl Ihres Produktes an: ')
  anzahl = input()
  warenkorb[prod] = anzahl
  print('Möchten Sie weiter einkaufen? (J/N)')
  entscheidung = input()
  if entscheidung == "J":
    pass
  elif entscheidung == "N":
    abbruch = True
    print('Folgende Bestellung wird abgeschickt: ')
    for prod in warenkorb:
       print(prod, ': ', warenkorb[prod])
  else:
    print('Unerwartete Eingabe, Ihr Einkauf wird abgebrochen...')
    abbruch = True
