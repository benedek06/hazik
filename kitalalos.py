import random
szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc",
          "dervis", "bagoly", "ecetes", "angyal", "boglya"]

szo = random.choice(szavak)
# print(f'{szo=}')

tipp = input('Kérem a tippet! ')
tippek_szama = 1
stop = False
while tipp != szo:
    if tipp == 'stop':
        stop = True
        break
    print('Az eredmény: ', end='')
    for index in range(6):
        if tipp[index] == szo[index]:
            print(tipp[index], end='')
        else:
            print('.', end='')
    tipp = input('\nKérem a tippet! ')
    tippek_szama += 1
if not stop:
    print(f'{tippek_szama} tippeléssel sikerült kitalálni!')    