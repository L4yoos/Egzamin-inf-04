import random

def bubble_sort(liczby):
    n = len(liczby)
    for i in range(n):
        for j in range(n - i - 1):
            if liczby[j] > liczby[j + 1]:
                temp = liczby[j]
                liczby[j] = liczby[j + 1]
                liczby[j + 1] = temp


if __name__ == "__main__":
    liczby = [random.randint(1,100) for _ in range(100)]

    print("Tablica liczb pseudolosowych", liczby)
    bubble_sort(liczby)
    print("Liczby posortowane:", ", ".join(map(str, liczby)))
