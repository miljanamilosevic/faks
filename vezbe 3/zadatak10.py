# Dve tačke u ravni date su koordinatama (x1; y1) i (x2; y2). Napiši program koji izračunava
# nagib prave koja prolazi kroz date tačke.

def zadatak10():
    x1 = eval(input("Unesite x koordinatu prve tacke: "))
    y1 = eval(input("Unesite y koordinatu prve tacke: "))
    x2 = eval(input("Unesite x koordinatu druge tacke: "))
    y2 = eval(input("Unesite y koordinatu druge tacke: "))
    m = (y2 - y1) / (x2 - x1)
    print(m)


zadatak10()
