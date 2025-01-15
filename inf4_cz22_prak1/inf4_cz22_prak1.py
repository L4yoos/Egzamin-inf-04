import random

class Egzamin:
    """
    *******************************************
    nazwa funkcji:  __init__
    argumenty:      brak
    typ zwracany:   brak
    informacje:     Konstruktor klasy Egzamin, tworzy pusta tablice
    autor:          000000000000000
    *******************************************
    """
    def __init__(self):
        self.array = []

    """
    *******************************************
    nazwa funkcji:  setup_array
    argumenty:      brak
    typ zwracany:   brak
    informacje:     Ta funkcja wypełnia tablicę liczbami pseudolosowymi od 1 do 100, w ilości sztuk 50.
    autor:          000000000000000
    *******************************************
    """
    def setup_array(self):
        self.array = [random.randint(1, 100) for _ in range(50)]

    """
    *******************************************
    nazwa funkcji:  display_array
    argumenty:      brak
    typ zwracany:   brak
    informacje:     Ta funkcja wyświetla zawartość tablicy, odzielone seperatorem (przecinkiem)
    autor:          000000000000000
    *******************************************
    """
    def display_array(self):
        print("Zawartość tablicy:")
        print(", ".join(map(str, self.array)))

    """
    *******************************************
    nazwa funkcji:  search
    argumenty:      value - wartość z klawiatury (liczba której szukamy)
    typ zwracany:   int - indeks na którym liczba sie znajduje, bądź jeżeli nie znajdzie to zwraca nam -1.
    informacje:     Funkcja ta polega na odnalezieniu indeksu liczby której szukamy. Jest to algorytm przeszukiwania tablicy z wartownikiem.
    autor:          000000000000000
    *******************************************
    """
    def search(self, value):
        self.array.append(value)
        index = 0
        while self.array[index] != value:
            index += 1
        self.array.pop()

        if index == len(self.array):
            return -1
        return index


def main():
    print("Witaj w programie!")

    try:
        liczba = int(input("Podaj liczbe z zakresu (1-100): "))
    except ValueError:
        print("Błędne dane. Podaj liczbę całkowitą")

    egzamin = Egzamin()
    egzamin.setup_array()
    index = egzamin.search(liczba)

    if index == -1:
        print("Nie znaleziono takiej liczby w tablicy.")
    else:
        print(f"Twoja liczba została znaleziona na indeksie: {index}")
    egzamin.display_array()

if __name__ == "__main__":
    main()