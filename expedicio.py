be = open("vetel.txt")
lista = []
sorszam = 1
for sor in be:
    if sorszam % 2 == 1:
        sor = sor.strip().split()
        elem = [int(sor[0]), int(sor[1])]
    else:
        sor = sor.strip()
        elem.append(sor)
        lista.append(elem)
    sorszam += 1
be.close()
print("2. feladat")
print(f"Első üzenet rögzítője:{lista[0][1]} ")
print(f"Utolsó üzenet rögzítője:{lista[-1][1]} ")

print("3. feladat")
for sor in lista:
    if "farkas" in sor[2]:
        print(f"{sor[0]}. nap {sor[2]}. rádióamatőr")

print("4. feladat")
for nap in range(1,12):
    db=0
    for sor in lista:
        if nap == sor[0]:
            db += 1
    print(f"{nap}. nap: {db}. rádióamatőr")

print("5.feladat")
ki = open("adas.txt", "w")
for nap in range(1, 12):
    original = []
    for i in range(90):
        original.append("$")
    for sor in lista:
        if nap == sor[0]:
            for i in range(90):
                if sor[2][i] != "$":
                    original[i] = sor[2][i]
    uzenet = "".join(original)
    print(nap,file=ki)
ki.close()

print("6. feladat")
def sazme(szo:str)->bool:
    valasz = True
    for i in range(len(szo)):
        if szo[i]<"0" or szo[i]>"9":
            valasz = False
    return valasz