# Prevedi sledeće matematičke izraze u Python izraze. Možeš podrazumevati da je importovana math biblioteka.


def zadatak2():
    from math import sqrt, sin, cos
    a = (3+4) * 5
    print(a)
    n = eval(input("Unesite n:"))
    b = (n * (n-1)) / 2
    print(b)
    r = eval(input("r "))
    print(4 != r*r)
    a = eval(input("Unesite a:"))
    r = eval(input("Unesite r:"))
    c = sqrt(r * (cos(a)*cos(a)) + r * (sin(a)*sin(a)))
    print(c)
    x1 = eval(input("Unesite x1:"))
    x2 = eval(input("Unesite x2:"))
    y1 = eval(input("Unesite y1:"))
    y2 = eval(input("Unesite y2:"))
    p = (y2 - y1) / (x2 - x1)
    print(p)


zadatak2()
