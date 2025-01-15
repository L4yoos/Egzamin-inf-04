"""
*************************************
nazwa klasy:    Film
pola:           _title - tytuł filmu
                _rentals - liczbe wypożyczeń
metody:         __init__, None - konstruktor klasy
                get_title, str - zwraca zmienną title
                get_rentals, int - zwraca liczbe wypożyczeń
                set_title, None - ustawia nowa wartość dla title
                set_rentals, None - ustawia nowa wartość dla rentals
                increment_rentals, None - zwiększa wartość zmiennej rentals o 1
informacje:     brak
autor:          00000000000000
*************************************
"""
class Film:
    def __init__(self):
        self._title = ""
        self._rentals = 0

    def get_title(self):
        return self._title

    def get_rentals(self):
        return self._rentals

    def set_title(self, title):
        if len(title) > 20:
            raise ValueError("Tytuł nie może przekraczać 20 znaków.")
        self._title = title

    def set_rentals(self, rentals):
        if not isinstance(rentals, int):
            raise ValueError("Tylko liczby całkowite są akceptowane.")
        self._rentals = rentals

    def increment_rentals(self):
        self._rentals += 1

if __name__ == "__main__":
    film = Film()
    print("Inicjalizacja obiektu...")
    print(f"Tytuł: {film.get_title()}\nLiczba wypożyczeń: {film.get_rentals()}")

    print("\nTest metody set_title i set_rentals...")
    film.set_title("Incepcja")
    film.set_rentals(5)
    print(f"Ustawiono tytuł: {film.get_title()}")
    print(f"Ustawiono liczbę wypożyczeń: {film.get_rentals()}")

    print("\nTest metod get_title i get_rentals...")
    print(f"Tytuł: {film.get_title()}\nLiczba wypożyczeń: {film.get_rentals()}")

    print("\nTest metody increment_rentals...")
    print(f"Liczba wypożyczeń przed inkrementacją: {film.get_rentals()}")
    film.increment_rentals()
    print(f"Liczba wypożyczeń po inkrementacji: {film.get_rentals()}")