"""
**********************************************
nazwa funkcji:          find_nwd
opis funkcji:           Owa funkcja znajduje NWD (Największy wspólny dzielnik) dla dwóch liczb
parametry:              a - pierwsza liczba z klawiatury, b - druga liczba z klawiatury
zwracany typ i opis:    int - zwracamy NWD dla lcizb a i b.
autor:                  0000000000000
***********************************************
"""
def find_nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main():
    while True:
        try:
            a = int(input("Podaj liczbę A: "))
            b = int(input("Podaj liczbę B: "))
            if a > 0 and b > 0:
                break
        except ValueError:
            print("Podaj liczby całkowitą")

    print(f"Największa wartość NWD dla {a} i {b} to {find_nwd(a,b)}")

if __name__ == "__main__":
    main()