# Epakt predstavlja starost meseca u danima na dan 1. januara. Koristi se za izračunavanje
# termina Uskrsa.Napiši program koji od korisnika traži godinu kao 4-cifreni broj i izračunava epakt po gregorijanskom
# kalendaru

def zadatak12():
    year = eval(input("Unesite cetvorocifreni broj: "))
    c = year / 100
    epakt = (8 + c / 4 - c + ((8 * c + 13) / 25) + 11 * (year % 19)) % 30
    print("Epakt po Gregorijanskom kalendaru je:", epakt)


zadatak12()

