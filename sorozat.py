def igen(a1, n):
    lista=[a1]
    for x in range(n):
        if lista[x]%2==0:
            lista.append(lista[x]+lista[x]/2)
        else:
            lista.append(lista[x]+3)
    return lista

x = int(input("Add meg az első elemét a számsornak: "))
print(igen(7, 8))