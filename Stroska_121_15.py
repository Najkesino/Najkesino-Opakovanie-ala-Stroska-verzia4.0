pocet_zam = 0
pocet_m = 0
perc_m = 0
pocet_z = 0
perc_z = 0

subor = open('zamestnanci.csv', 'r', encoding='UTF-8')
for r in subor:
    pocet_zam += 1
    koncovka = r[(len(r))-4::].strip()
    if koncovka=='ová':
        pocet_z += 1
    else:
        pocet_m += 1
perc_z = round((pocet_z/(pocet_zam/100)), 2)
perc_m = round((pocet_m/(pocet_zam/100)), 2)
subor.close()

print('Počet zamestnancov je: '+str(pocet_zam))
print('Počet žien medzi zamestnancami: '+str(pocet_z))
print('Počet žien medzi zamestnancami v %: '+str(perc_z))
print('Počet mužov medzi zamestnancami: '+str(pocet_m))
print('Počet mužov medzi zamestnancami v %: '+str(perc_m))
