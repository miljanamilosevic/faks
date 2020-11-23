# Napisati program koji pita korisnika da unese nekoliko reči odvojenih razmakom, potom ispisuje iste te
# reči, samo što umesto razmaka ih program spoji dvotačkom. Potrebno je koristiti funkcije split i join.


def zadatak6():
    string_reci = input("Unesite reci odvojene zarezom: ")
    reci = string_reci.split(" ")
    print(reci)
    reci_sa_dvotackom = ":".join(reci)
    print(reci_sa_dvotackom)



zadatak6()
