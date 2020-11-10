# Napiši program koji izračunava dužinu merdevina za datu visinu koju treba dostići i ugao
# kojim se meri nagib merdevina.
# previse prosto, popravi kad budes bila bolja

from math import sin


def zadatak14():
    visina = eval(input("Unesite visinu merdevina: "))
    ugao = eval(input("Unesite ugao merdevina: "))
    d = visina / sin(ugao)
    print("Duzina merdevina je: ", d)


zadatak14()
