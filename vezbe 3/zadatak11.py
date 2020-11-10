# Za dve tačke u ravni izračunati rastojanje između njih.

from math import sqrt

def zadatak11():
    x1 = eval(input("Unesite x koordinatu prve tacke: "))
    y1 = eval(input("Unesite y koordinatu prve tacke: "))
    x2 = eval(input("Unesite x koordinatu druge tacke: "))
    y2 = eval(input("Unesite y koordinatu druge tacke: "))
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Rastojanje izmedju dve tacke je: ", d)


zadatak11()
