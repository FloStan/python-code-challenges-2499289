warenkorb = {}
abbruch = false
print('Willkommen zu Ihrem Shoppingassistenten.')
while abbruch == false:
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
  else:
    print('Unerwartete Eingabe, Ihr EInkauf wird abgebrochen...')
    abbruch = True