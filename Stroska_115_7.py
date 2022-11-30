import tkinter
canvas = tkinter.Canvas(width = 500, height = 500, bg='white')
canvas.pack()

zoznam = [0]*52
neviem = 0
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

x = 80
y = 200
canvas.create_text(250, 100, text='Frekvencia výskytu písmem v slov. článku.')
for i in range(52):
    if i%2==1:
        canvas.create_rectangle(x, y, x+10, y-zoznam[i], fill='lime')
        canvas.create_text(x+5, y+10, text=zoznam[i-1])
        x += 15

zoznam = [0]*52
neviem = 0
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

x = 80
y = 400
canvas.create_text(250, 300, text='Frekvencia výskytu písmem v angl. článku.')
for i in range(52):
    if i%2==1:
        canvas.create_rectangle(x, y, x+10, y-zoznam[i], fill='red')
        canvas.create_text(x+5, y+10, text=zoznam[i-1])
        x += 15


