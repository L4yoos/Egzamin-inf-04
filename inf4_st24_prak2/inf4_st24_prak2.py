"""
************************************************
 klasa:     StringTools
 opis:      Klasa to narzędzie do tekst'ów, posiada 2 funkcje: do liczenia samogłosków oraz usuwania powtórzenia tych samych znaków.
 metody:    count_vowels - int, liczbe samogłosków
            remove_consecutive_duplicates - str, tekst bez powtórek
 autor:     0000000000000000
************************************************
"""
class StringTools:

    @staticmethod
    def count_vowels(input_string):

        if not input_string:
            return 0

        vowels = "aąeęiouóyAĄEĘIOUÓY"
        count = sum(1 for char in input_string if char in vowels)
        return count

    @staticmethod
    def remove_consecutive_duplicates(input_string):
        if not input_string:
            return ""

        result = [input_string[0]]
        for char in input_string[1:]:
            if char != result[-1]:
                result.append(char)

        return ''.join(result)

def main():
    tekst = input("Podaj tekst do analizy: ")

    vowels_count = StringTools.count_vowels(tekst)
    print(f"Liczba samogłosek w podanym tekście: {vowels_count}")

    cleaned_text = StringTools.remove_consecutive_duplicates(tekst)
    print(f"Tekst po usunięciu powtórzeń: {cleaned_text}")

if __name__ == "__main__":
    main()