# Napisati program koji pita korisnika da pogađa broj. Ispravan broj koji korisnik treba da pogodi je broj 42.
# Program pita korisnika da unese broj sve dok ne unese tačan broj. Ukoliko je broj netačan, program kaže
# korisniku da li je pravi broj manji ili veći od unetog.

def zadatak4(broj):
    while True:
        guess = int(input("Pogodi broj: "))
        if guess == broj:
            print("Tacan broj!")
            break
        elif guess > broj:
            print("Pravi broj je manji!")
        else:
            print("Pravi broj je veci!")


zadatak4(59)
