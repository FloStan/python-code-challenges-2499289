berechnen = True
while berechnen == True:
  print('Eingabe Geschwindigkeit in km/h:')
  v = int(input())
  situation= ["Trocken", "Nass", "Eis", "Gefahrenbremsung"]
  print('Auswahl Fahrbahnzustand/Situation:')
  for i in range(len(situation)):
    print(i, ': ', situation[i])
  sit = situation[int(input())]
  print('Verzögerung einkalkulieren (Y/N)?')
  delay = input()
  bremsweg=v*v/100
  if sit == "Trocken":
    pass
  elif sit == "Nass":
    bremsweg=bremsweg*1.5
  elif sit == "Eis":
    bremsweg=bremsweg*6.5
  else:
    bremsweg=bremsweg*0.5
  if delay == "Y":
    bremsweg+=0.3*(1/60)*(1/60)*v
  else:
    pass
  print('Der Bremsweg ist ', bremsweg, ' Meter')
  print('Weitere Bremswegberechnungen (Y/N)?')
  entscheidung = input()
  if entscheidung == 'N':
    berechnen = False
  else:
    pass
print('Danke, dass Sie Ihren Bremsweg mit uns berechnet haben.')