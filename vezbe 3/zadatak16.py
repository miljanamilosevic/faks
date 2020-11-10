# Napiši program koji izračunava zbir kvadrata prvih n prirodnih brojeva, gde se n unosi sa tastature

def zadatak16():
    x = 0
    n = eval(input("Unesite n:"))
    for i in range(1, n+1):
        x += i**2
    print("Ukupan zbir iznosi: ", x)


zadatak16()