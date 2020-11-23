# Napisati program koji traži od korisnika da unese neki broj. Program ponavlja pitanje u krug dok korisnik ne
# unese broj 42.

def zadatak1():
    while True:
        broj = int(input("Unesite broj: "))

        if broj == 42:
            break


zadatak1()
