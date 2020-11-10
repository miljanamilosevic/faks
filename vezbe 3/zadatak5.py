#Napiši program koji izračunava zapreminu i površinu sfere za dati poluprečnik.

def zadatak5():
    r = eval(input("Unesite poluprecnik: "))
    v = (4/3) * 3.14 * r**3
    a = 4 * 3.14 * r**2
    print("Povrsina je:", a)
    print("Zapremina je:", v)


zadatak5()
