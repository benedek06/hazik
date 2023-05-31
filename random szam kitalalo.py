import random
print("Szám kitakáló")
y = random.randint(1, 1000)
while True:
    x = int(input("Tipp: "))
    if x==y:
        print("Kitaláltad")
        break
    elif x > y:
        print('Fölötte vagy')
    else:
        print("Alatta vagy")
