subor = open('osoby.txt', 'r', encoding='UTF-8')
osoby = []
pocet = 0
for riadok in subor:
    info = riadok.split(';')
    osoba = {}
    osoba['meno'] = info[0]
    osoba['vyska'] = int(info[1])
    osoba['roknarodenia'] = int(info[2])
    osoba['rodisko'] = info[3].strip()
    osoby.append(osoba)
co = input('Zadaj ci chces vyhladavat podla miesta alebo datumu narodenia: (datum/mesto)')
if co == 'datum':
    datum = input('Zadaj datum kedy sa osoby narodili: ')
    for i in range(len(osoby)):
        datum_os = osoby[i]['roknarodenia']
        meno = osoby[i]['meno']
        if int(datum_os)==int(datum):
            pocet += 1
            print(meno)
    print('Pocet osob: '+str(pocet))
elif co == 'mesto':
    mesto = input('Zadaj mesto z kadial sa osoby narodili: ')
    for i in range(len(osoby)):
        mesto_os = osoby[i]['rodisko']
        meno = osoby[i]['meno']
        if mesto_os==mesto:
            pocet += 1
            print(meno)
    print('Pocet osob: '+str(pocet))
subor.close()
