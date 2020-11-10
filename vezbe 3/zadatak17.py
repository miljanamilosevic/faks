# Napiši program koji izračunava zbir brojeva koje unosi korisnik. Prvo je potrebno uneti
# broj brojeva koje treba sabrati. Potom treba uneti sve brojeve i na kraju ispisati vrednost

def zadatak17():
    x = 0
    n = eval(input("Unesite n: "))
    for i in range(1, n+1):
        print("Unesite ", i, ". broj:")
        temp = eval(input())
        x += temp
    print("Ukupan zbir iznosi: ", x)


zadatak17()
