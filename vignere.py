abc = "abcdefghijklmnopqrstuvwxyz "

betu_index = dict(zip(abc, range(len(abc))))
index_betu = dict(zip(range(len(abc)), abc))


def kodolt(uzenet, kulcs):
    kodolt = ""
    split_uzenet = [
        uzenet[i : i + len(kulcs)] for i in range(0, len(uzenet), len(kulcs))
    ]

    for szetszed in split_uzenet:
        i = 0
        for letter in szetszed:
            szam = (betu_index[letter] + betu_index[kulcs[i]]) % len(abc)
            kodolt += index_betu[szam]
            i += 1

    return kodolt

def main():
    uzenet = input("Írd be az üzenetet: ")
    kulcs = "banana"
    kodolt_uzenet = kodolt(uzenet, kulcs)

    print("Üzenet: " + uzenet)
    print("Kódolt üzenet: " + kodolt_uzenet)


main()