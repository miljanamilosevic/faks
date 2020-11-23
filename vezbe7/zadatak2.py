# Napisati program za login korisnika na sistem. Program treba da pita korisnika da unese korisničko ime i šifru
# sve dok korisnik ne unese ispravno korisničko ime i šifru - doktorjoca i kartica4.

def zadatak2():

    ime = input("Unesite korisnicko ime: ")
    while ime != 'doktorjoca':
        ime = input("Unesite korisnicko ime: ")

    sifra = input("Unesite sifru: ")
    while sifra != 'kartica4':
        sifra = input("Unesite sifru: ")


zadatak2()
