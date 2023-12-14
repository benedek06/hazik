be = open("lotto.txt")
lista = []
for sor in be:
    sor=sor.strip().split("\t")
    lista.append([int(x) for x in sor])
be.close()
n = len(lista)
print(n)
print(lista[0])
kozos = []
elso=lista[-1]
for x in elso:
    if x in utolso:
        kozos.append(x)
if kozos:
    print(kozos)
else:
    print("nem")
print(n%52)
het = 122.52+44
het=het-n