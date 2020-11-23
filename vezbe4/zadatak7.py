#Napisati program koji pita korisnika da unese nekoliko reči odvojenih zarezom, potom program ispisuje
#svaku drugu reč

def zadatak7():
    tekst = input("Unesite reci odvojene zarezom: ")
    reci = tekst.split(",")
    for i in range(0, len(reci), 2):
        print(reci[i])


zadatak7()
