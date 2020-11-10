# Napiši program koji izračunava površinu trougla za date dužine stranica a,b i c.

from math import sqrt


def zadatak13():
    a = eval(input("Unesite stranicu a: "))
    b = eval(input("Unesite stranicu b: "))
    c = eval(input("Unesite stranicu c: "))
    s = (a + b + c) / 2
    p = sqrt(s * (s-a) * (s-b) * (s-c))
    print("Povrsina trougla je: ", p)


zadatak13()
