import random

"""
************************************************
nazwa:                  random_numbers
opis:                   losuje wyniki z kostek
parametry:              ile_razy - ilość rzutów kostkami wartość z klawiatury
zwracany typ i opis:    zwraca tablice liczb z zakresu (1-6)
autor:                  000000000
************************************************
"""
def random_numbers(ile_razy):
    return [random.randint(1,6) for _ in range(ile_razy)]

"""
************************************************
nazwa:                  count_points
opis:                   zlicza punkty według wymagań
parametry:              rolls - liczby które wypadły podczas rzutów kostkami
zwracany typ i opis:    zwraca liczbę uzyskanych punktów
autor:                  000000000
************************************************
"""
def count_points(rolls):
    points = 0
    for i in range(1,7):
        count = rolls.count(i)
        if count >= 2:
            points += count * i
    return points

while True:
    while True:
        try:
            ile_razy = int(input("Ile kostek chcesz rzucić?(3-10): "))
            if 3 <= ile_razy <= 10:
                break
        except ValueError:
            print("Podaj liczbe całkowitą.")

    rolls = random_numbers(ile_razy)

    for i, wynik in enumerate(rolls, start=1):
        print(f"Kostka {i}: {wynik}")

    points = count_points(rolls)
    print(f"Liczba uzyskanych punktów: {points}")

    answer = input("Jeszcze raz? (t/n): ").lower()
    while True:
        if answer not in ['t', 'n']:
            print("Błędna odpowiedź t/n")
        else:
            break

    if answer == 'n':
        print("Dziękujemy za gre!")
        break

