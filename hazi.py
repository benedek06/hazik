lista = list(map(lambda x: list(map(int, x.split(","))),open("input.txt").read().split("\n"))) 
# 2. feladat 
lista1 = list(map(lambda x: x,sorted(lista[0])[-10:])) 
print("1. ", sum(lista1)) 
# 3. feladata 
from functools import reduce 
lista2 = reduce(lambda x, y: x * y, filter(lambda x: x%3, lista[1])) 
print(f'2. 10^', len(str(lista2))) 
# 4. feladat 
print("4. ",sum(lista[2])) 
# 5. feladat 
lista4 = list(map(lambda x: x**2,sorted(lista[3])[-21:])) 
print("5. ", sum(lista4)) 
# 6. feladat 
lista5 = list(map(lambda x: x,sorted(lista[4])[10:])) 
print("6. ", sum(lista5)) 
# 7. feladat 
print("7. ", max(sorted(sum(lista, []))[12:]))