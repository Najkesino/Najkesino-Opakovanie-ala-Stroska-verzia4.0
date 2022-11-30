subor = open('osoby.txt', 'r', encoding='UTF-8')
osoby = []
naj_v = 0
meno_v = 0
naj_m = 0
meno_m = 0
for riadok in subor:
    info = riadok.split(';')
    osoba = {}
    osoba['meno'] = info[0]
    osoba['vyska'] = int(info[1])
    osoba['roknarodenia'] = int(info[2])
    osoba['rodisko'] = info[3].strip()
    osoby.append(osoba)
for i in range(len(osoby)):
    vyska = osoby[i]['vyska']
    vek = osoby[i]['roknarodenia']
    if int(vyska)>int(naj_v):
        naj_v = vyska
        meno_v = osoby[i]['meno']
    if int(vek)>int(naj_m):
        naj_m = vek
        meno_m = osoby[i]['meno']
print('Najvyssia osoba je: '+meno_v)
print('Najmladsia osoba je: '+meno_m)
subor.close()
