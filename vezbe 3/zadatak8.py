# Napiši program koji određuje udaljenost posmatrača od munje na bazi vremenske razlike
# trenutka pojavljivanja munje i trenutka kada zvuk stigne do posmatrača.

def zadatak8():
    brzina_zvuka = 340
    vreme = eval(input("Unesite vremensku razlika:"))
    d = brzina_zvuka * vreme
    print("Rastojanje munje i posmatraca je: ", d)


zadatak8()
