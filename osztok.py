def nem():
    a1 = int(input("Add meg a számot: "))
    osztok = []
    lista=[]

    for x in range(2, a1,1):
        lista.append(x)
    for x in lista:
        if a1%x==0:
            osztok.append(x)
    return "VAlódi osztók száma: ", osztok
print(nem())