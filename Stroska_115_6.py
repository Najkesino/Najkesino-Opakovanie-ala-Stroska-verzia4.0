import tkinter
canvas = tkinter.Canvas(width = 500, height = 500, bg='white')
canvas.pack()

zoznam = [0]*52
percenta = [0]*52
neviem = 0
sucet = 0

for i in range(51):
    if i%2==0:
        zoznam[i]=chr(97+neviem)
        neviem += 1
premenna = 0
premenna2 = ''

subor = open('clanky.txt', 'r', encoding='UTF-8')
for riadok in subor:
    riadok = riadok.lower()
    for znak in riadok:
        if 'z'>=znak>='a':
            zoznam[(ord(znak)-97)*2+1] += 1
subor.close()

for i in range(52):
    for y in range(52):
        if i%2==1 and y%2==1:
            if zoznam[y]>zoznam[i]:
                premenna = zoznam[y]
                premenna2 = zoznam[y-1]
                zoznam[y] = zoznam[i]
                zoznam[y-1] = zoznam[i-1]
                zoznam[i] = premenna
                zoznam[i-1] = premenna2

for i in range(len(zoznam)):
    if i%2==1:
        sucet += int(zoznam[i])
percento = round(sucet/100, 2)

for i in range(len(zoznam)):
    if i%2==1:
        percenta[i]=round(int(zoznam[i])/percento, 2)

x = 50
y = 50
canvas.create_text(50, 20, text='Graféma\n(sl.článok)', font='Arial 10 bold')
canvas.create_text(150, 20, text='Výskyt[%]', font='Arial 10 bold')
canvas.create_line(100, 0, 100, 500)
canvas.create_line(0, 35, 500, 35)
for i in range(len(zoznam)):
    if i%2==1:
        canvas.create_text(x, y, text=zoznam[-1-i], font='Arial 10')
        canvas.create_text(x+100, y, text=percenta[-i], font='Arial 10')
        y += 17





zoznam = [0]*52
percenta = [0]*52
neviem = 0
sucet = 0
for i in range(51):
    if i%2==0:
        zoznam[i]=chr(97+neviem)
        neviem += 1
premenna = 0
premenna2 = ''

subor = open('clanky_en.txt', 'r', encoding='UTF-8')
for riadok in subor:
    riadok = riadok.lower()
    for znak in riadok:
        if 'z'>=znak>='a':
            zoznam[(ord(znak)-97)*2+1] += 1
subor.close()

for i in range(52):
    for y in range(52):
        if i%2==1 and y%2==1:
            if zoznam[y]>zoznam[i]:
                premenna = zoznam[y]
                premenna2 = zoznam[y-1]
                zoznam[y] = zoznam[i]
                zoznam[y-1] = zoznam[i-1]
                zoznam[i] = premenna
                zoznam[i-1] = premenna2

for i in range(len(zoznam)):
    if i%2==1:
        sucet += int(zoznam[i])
percento = round(sucet/100, 2)

for i in range(len(zoznam)):
    if i%2==1:
        percenta[i]=round(int(zoznam[i])/percento, 2)

x = 300
y = 50
canvas.create_text(300, 20, text='Graféma\n(eng.článok)', font='Arial 10 bold')
canvas.create_text(400, 20, text='Výskyt[%]', font='Arial 10 bold')
canvas.create_line(350, 0, 350, 500)
for i in range(len(zoznam)):
    if i%2==1:
        canvas.create_text(x, y, text=zoznam[-1-i], font='Arial 10')
        canvas.create_text(x+100, y, text=percenta[-i], font='Arial 10')
        y += 17
