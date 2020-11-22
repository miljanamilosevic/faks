def zadatak6():
    string_reci = input("Unesite reci odvojene zarezom: ")
    reci = string_reci.split(" ")
    print(reci)
    reci_sa_dvotackom = ":".join(reci)
    print(reci_sa_dvotackom)


zadatak6()
