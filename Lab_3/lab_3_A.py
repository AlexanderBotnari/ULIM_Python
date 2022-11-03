# functie cu parametru implicit
def suma_cifrelor(number=0):
    suma = 0
    for digit in str(number):
        suma += int(digit)
    return suma


try:
    # number = 111
    # number = int(input("Introduceti numarul: "))
    # print("Suma cifrelor lui", number, "este", suma_cifrelor(number=number))
    print(suma_cifrelor(45))
except ValueError:
    print("Va rugam sa introduceti doar cifre!")
