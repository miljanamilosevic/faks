print(1, 2, 3, sep="")
print("ja","sam","miljana", sep=" .")
print(1, 2, 3, end="") #naredni ispis je u nastavku
print(1, 2, 3, sep=" ")
# ovo je komentar
"""
i ovo
su 
sve
komentari
"""
print(9 % 2) #ostatak pri deljenju
print(9**2) #stepenovanje

print("Rekao je 'Zdravo svima'")
print(len("Zdravo"))#duzina stringa
s = "Miljana"
print(s[-3]) #indeksiranje elementa
print(s + " Milosevic") #konkateniranje
print(s * 10)
print(s[2:5]) #izdvajanje opsega, prvi broj se racuna, drugi ne
def main():
    if 's' in s: #proveravamo da li se neki karakter nalazi u nekom stringu
        print("true")
    else:
        print("false")
main()
#bool
manje = (3 > 8) and (5 < 10)
print(manje)
manje = ((15/8 < 3) or (5 < 10))
print(manje)
isto = not(3 == 5)
print(isto)
isto = (3 == 5)
print(isto)
##
#4(29)
#banana = 0.85
#jabuka = 0.55
#cokolada = 0.18
#torba = banana + jabuka + 3*cokolada
#print(torba, "kg")
##
#dolari = int(input("Unesi vrednost u dolarima: "))
#vrednost_dolara = 106.77
#dinari = dolari * vrednost_dolara
#print("Uneta vrednost u dolarima iznosi", dinari, " dinara")
##
#penzija = 40000
#smanjenje = penzija * (9/10)
#povecanje = smanjenje * (11/10)
#print(povecanje)
##
#def z45():
 #   sekunda = int(input("Unesi vreme u sekundama: "))
 #   dan = sekunda // (24 * 60 * 60)
 #   ostatak = sekunda % (24 * 60 * 60)
 #   sat = ostatak // (60 * 60)
 #   ostatak = ostatak % (60 * 60)
 #   minut = ostatak // (60)
 #   ostatak = ostatak % (60)
 #   sekunda = ostatak
 #   print("Vreme: ", dan, "dana", sat,"sati", minut, "minuta" ,sekunda, "sekundi")
#z45()








