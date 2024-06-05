t_AB=7 #Minuten
t_AB=t_AB/60 #Stunden
d_AB=10 #km
v_avrg_zul=120 #kmh
#Aufgabe 1
v_avrg_benötigt=round(d_AB/t_AB) #kmh
print('Aufgabe 1: Die benötigte Durchschnittsgeschwindigkeit ist ', v_avrg_benötigt, ' km/h.')
#Aufgabe 2
t_verzögerung = [10/3600, 20/3600, 30/3600] #s in h umgerechnet
v_avrg_benötigt_verzögert = []
for t_v in t_verzögerung:
  v_avrg_benötigt_verzögert.append(round(d_AB/(t_AB-t_v))) #kmh
print('Aufgabe 2: Die benötigten Durchschnittsgeschwindigkeiten sind nun', v_avrg_benötigt_verzögert, ' km/h.')
#Aufgabe 3
t_verzögerung_max = d_AB/v_avrg_zul*3600
print('Aufgabe 3: Die maximal zulässige Verzögerung beträgt: ', t_verzögerung_max, ' s.')
