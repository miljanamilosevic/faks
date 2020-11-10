# Napiši program koji izračunava cenu pice po kvadratnom centimetru za dati poluprečnik i
# cenu cele pice.

import math


def zadatak6():
    r = eval(input("Unesite r:"))
    cena_pice = eval(input("Unesite cenu cele pice:"))
    s = 4 * r**2 * math.pi
    cena_po_kv_cm = cena_pice / s
    print("Cena pice po kvadratnom centimetru je: ", cena_po_kv_cm)


zadatak6()
