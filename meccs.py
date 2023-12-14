be = open("meccs.txt")
lista = []
for sor in be:
    sor = sor.strip().split("\t")
    meccs = [sor[0],sor[1],int(sor[2]),sor[3],int(sor[4]),int(sor[5])]
    lista.append(meccs)
be.close()

print("Meccsek száma: ",len(lista))

lott = 0
for sor in lista:
    lott += sor[4]
print(f"Eddig {lott} gólt lőttünk!")

kapott = 0
for sor in lista:
    kapott += sor[5]
x = round(kapott / len(lista), 2)
print(f"Átlagosan {x} gólt kaptunk meccsenként!")

darab = 0
for sor in lista:
    if sor[5] == 0:
        darab += 1
y = round(darab/len(lista)*100)
print(f"A mérkőzések {y}%-ában nem kaptunk gólt!")

ellenfel = set()
for sor in lista:
    ellenfel.add(sor[3])
z = len(ellenfel)
print(f"Eddig {z} országgal játszottunk!")

ki = open("rangsor.txt", "w")
statisztika = []
for orszag in ellenfel:
    m = 0
    gy = 0
    d = 0
    v = 0
    l = 0
    k = 0
    for sor in lista:
        if orszag == sor[3]:
            m += 1
            l += sor[4]
            k += sor[5]
            if sor[4] > sor[5]:
                gy += 1
        elif sor[4] < sor[5]:
            v += 1
        else: d += 1
    statisztika.append([orszag,m,gy,d,v,l,k])
statisztika.sort(key=lambda elem: (-elem[1],-elem[2]))

for sor in statisztika:
    print(sor,file=ki)

ki.close()
print("Nem kaptunk még ki: ")
for sor in statisztika:
    if sor[4] == 0:
        print(sor[0])