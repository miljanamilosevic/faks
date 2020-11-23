# Napisati program koji traži od korisnika da unese broj n. Program potom sabira prirodne brojeve redom od
# 1 pa na dalje, sve dok zbir ne postane veći od broja n. Kada zbir postane veći od n, program ispiše koliko je
# brojeva sabrao, i koliki je zbir.

def zadatak3():
    n = eval(input("Unesite broj n: "))
    i = 1
    sum = 0
    while True:
        sum += i
        if sum > n:
            print(sum)
            print(i)
            break
        i = i + 1


zadatak3()
