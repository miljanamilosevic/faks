def zadatak3():

    zbir = 0
    n = eval(input("Unesite n: "))

    for i in range(0, n+1, 2):
        zbir = zbir + i**2

    print("Suma kvadrata prvih n parnih brojeva je: ", zbir)


zadatak3()
