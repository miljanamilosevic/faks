# Napiši program koji izračunava zbir prvih n prirodnih brojeva, gde se n unosi sa tastature

def zadatak15():
    x = 0
    n = eval(input("Unesite n:"))
    for i in range(1, n+1):
        x += i
    print("Ukupan zbir iznosi: ", x)


zadatak15()
