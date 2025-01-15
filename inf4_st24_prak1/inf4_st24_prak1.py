def gender(pesel):
    if int(pesel[9]) % 2:
        return "M"
    else:
        return "K"

def check_checksum(pesel):
    weights = [1,3,7,9,1,3,7,9,1,3]
    S = 0
    for i in range(10):
        S += weights[i] * int(pesel[i])
    M = S % 10
    if M == 0:
        R = 0
    else:
        R = 10 - M
    return R == int(pesel[10])

default_pesel = "55030101193"
pesel = input("Podaj swój pesel (Brak podania automatycznie zostanie przypisany pesel: 55030101193): ")

if not pesel:
    pesel = default_pesel

gender_return = gender(pesel)

if gender_return == "K":
    print("Kobieta")
else:
    print("Mężczyzna")

if check_checksum(pesel):
    print("Podany pesel przeszedł zgodność sumy kontrolnej.")
else:
    print("Podany pesel nie przeszedł zgodność sumy kontrolnej.")
