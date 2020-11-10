# Prodavnica kafe prodaje kafu za 105 dinara za kilogram. Za kućnu dostavu naplaćuje se
# 18 dinara po kilogramu i 15 dinara fiksnih troškova. Napiši program koji izraćunava ukupnu cenu kućne
# porudžbine.

def zadatak9():
    dostava = 18
    fiksni_troskovi = 15
    kafa = eval(input("Unesite koliko kg kafe je naruceno:"))
    cena = kafa * 105 + kafa * (dostava + fiksni_troskovi)
    print("Ukupna cena kucne porudzbine je:", cena)


zadatak9()
