# Napiši program koji izračunava prosek brojeva koje unosi korisnik. Prosek bi trebalo da bude float

def zadatak18():
    x = 0
    z = type(float)
    n = eval(input("Unesite n:"))
    for i in range(1, n + 1):
        print("Unesite ", i, ". broj:")
        temp = eval(input())
        x += temp
    z = x / n
    print("Prosek iznosi: ", z)


zadatak18()
