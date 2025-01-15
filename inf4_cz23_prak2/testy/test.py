import random

from testy2.inf4_cz23_prak2 import bubble_sort

def test_bubble_sort():
    liczby = [random.randint(0, 1000) for _ in range(50)]

    rezultat = sorted(liczby)

    bubble_sort(liczby)

    assert liczby == rezultat, f"Test nie przeszedł! Otrzymano {liczby}, {rezultat}"

    print(f"Tablica po sortowaniu bąbelkowym: {liczby}")
    print(f"Tablica po sortowaniu sorted(): {rezultat}")
    print("Test przeszedł pomyślnie!")

if __name__ == "__main__":
    test_bubble_sort()