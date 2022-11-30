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

def kresli_stlpec(x, y, dx, dy, znaky):
    fa, fb = 'yellow', 'lightblue'
    for znak in znaky:
        canvas.create_rectangle(x, y, x+dx, y+dy, fill=fa)
        canvas.create_text(x+dx/2, y+dy/2, text=znak)
        y += dy
        fb, fa = fa, fb
velkost = 300
pocet_casti = 2
x = 10
y = 10
dx = 50
spracovat = []
for i in range(51):
    if i%2==1:
        spracovat.append(zoznam[-1-i])

while len(spracovat) > 0:
    kresli_stlpec(x, y, dx, velkost/pocet_casti, spracovat[:pocet_casti])
    spracovat = spracovat[pocet_casti:]
    x += dx
    pocet_casti *= 2
