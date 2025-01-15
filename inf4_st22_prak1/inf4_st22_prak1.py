class Egzamin:
    """
    /******************************************

     *  nazwa funkcji:  __init__

     *  parametry wejściowe: brak

     *  wartość zwracana: brak

     *  autor:  00000000000000

     * *****************************************
    """
    def __init__(self):
        self.array = []

    """
    /******************************************

     *  nazwa funkcji:  setup_array

     *  parametry wejściowe: brak

     *  wartość zwracana: brak

     *  autor:  00000000000000

     * *****************************************
    """
    def setup_array(self):
        for i in range(10):
            while True:
                try:
                    liczba = int(input(f"Podaj liczbę {i + 1}: "))
                    self.array.append(liczba)
                    break
                except ValueError:
                    print("Podaj liczbe całkowitą.")

    """
    /******************************************

     *  nazwa funkcji:  __find_max_index

     *  parametry wejściowe: start - wartość indeksu od którego zaczynamy

     *  wartość zwracana: max_index - indeks z maksymalna wartością

     *  autor:  00000000000000

     * *****************************************
    """
    def __find_max_index(self, start):
        max_index = start
        for i in range(start + 1, len(self.array)):
            if self.array[i] > self.array[max_index]:
                max_index = i
        return max_index

    """
    /******************************************

     *  nazwa funkcji:  sort

     *  parametry wejściowe: brak

     *  wartość zwracana: brak

     *  autor:  00000000000000

     * *****************************************
    """
    def sort(self):
        for i in range(len(self.array)):
            max_index = self.__find_max_index(i)
            self.array[i], self.array[max_index] = self.array[max_index], self.array[i]

    """
    /******************************************

     *  nazwa funkcji:  display_array

     *  parametry wejściowe: brak

     *  wartość zwracana: brak

     *  autor:  00000000000000

     * *****************************************
    """
    def display_array(self):
        print("Tablica: ", self.array)

def main():
    egzamin = Egzamin()
    egzamin.setup_array()
    egzamin.display_array()
    egzamin.sort()
    egzamin.display_array()

if __name__ == "__main__":
    main()