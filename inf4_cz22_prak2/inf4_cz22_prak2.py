class Osoba:

    liczba_instancji = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    def kopiuj(self, inna_osoba):
        if isinstance(inna_osoba, Osoba):
            self.__id = inna_osoba.__id
            self.__imie = inna_osoba.__imie

    def przywitaj(self, argument):
        if self.__imie:
            print(f"Cześć {argument}, mam na imię {self.__imie}")
        else:
            print("Brak danych")

def main():
    print("Witaj!")

    print(f"Liczba instancji klasy Osoba: {Osoba.liczba_instancji}")

    osoba1 = Osoba()
    osoba1.przywitaj("Jan")

    try:
        id2 = int(input("Podaj ID dla 2 osoby: "))
        imie2 = str(input("Podaj Imię dla 2 osoby: "))
        osoba2 = Osoba(id2, imie2)
    except ValueError:
        print("Nieprawidłowe dane!")

    osoba2.przywitaj("Jan")

    osoba3 = Osoba()
    osoba3.kopiuj(osoba2)
    osoba3.przywitaj("Jan")

    print(f"Liczba instancji klasy Osoba: {Osoba.liczba_instancji}")

if __name__ == "__main__":
    main()