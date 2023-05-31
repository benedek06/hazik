def kiszamolas(ora, perc):
    ora_szog = 0.5*(ora*60+perc)
    perc_szog = 6*perc
    szog = abs(ora_szog-perc_szog)
    if szog > 180:
        szog -= 360
    return szog

ora, perc = input("Óra, Perc: ").split(":")
szog = kiszamolas(ora, perc)
print("Bezárt szög: ", abs(szog),"°")