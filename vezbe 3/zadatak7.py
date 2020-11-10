#  Napiši program koji izračunava molekularnu masu molekula ugljovodonika zavisno od broja
# atoma ugljenika i vodonika koji ga čine.

def zadatak7():
    ugljenik = 12.011
    vodonik = 1.0079
    c = eval(input("Broj atoma ugljenika:"))
    h = eval(input("Broj atoma vodonika:"))
    molekularna_masa = ugljenik * c + vodonik * h
    print("Ukupna masa atoma je: ", molekularna_masa)


zadatak7()
