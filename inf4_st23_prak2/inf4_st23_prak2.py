"""
************************************************
klasa:      Notatka
opis:       Tworzenie oraz wyświetlanie Notatek
pola:       id - identyfikator notatki, title - Tytuł Notatki, tresc - tresc Notatki, countNotes - licznik Notatek ile aktualnie posiadamy
autor:      00000000000000
************************************************
"""
class Notatka:
    __countNotes = 0

    def __init__(self, title, tresc):
        Notatka.__countNotes += 1

        self.__id = Notatka.__countNotes

        self.__title = title
        self.__tresc = tresc

    def wyswietl_notatke(self):
        print(f"Tytuł: {self.__title}\nTreść: {self.__tresc}")

    def wyswietl_diagnostyke(self):
        print(f"ID: {self.__id}; "
              f"Tytuł: {self.__title}; "
              f"Tresc: {self.__tresc}; "
              f"Licznik Notatek: {self.__countNotes};")

def main():
    print("Witaj w aplikacji do obsługi notatek!")

    tytul1 = input("Podaj tytul pierwszej notatki: ")
    tresc1 = input("Podaj tresc pierwszej notatki: ")
    notatka1 = Notatka(tytul1, tresc1)

    tytul2 = input("Podaj tytul drugiej notatki: ")
    tresc2 = input("Podaj tresc drugiej notatki: ")
    notatka2 = Notatka(tytul2, tresc2)

    print("Wyświetlanie notatek:")
    notatka1.wyswietl_notatke()
    notatka2.wyswietl_notatke()

    print("Diagnostyka notatek:")
    notatka1.wyswietl_diagnostyke()
    notatka2.wyswietl_diagnostyke()

if __name__ == "__main__":
    main()