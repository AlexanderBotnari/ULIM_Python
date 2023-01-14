import math


# functie cu parametru implicit
def media_geometrica(a, b=1):
    result = math.sqrt(a * b)
    return round(result, 2)


# functie cu parametri variabili
def media_geometrica_var(**kwargs):
    result = math.sqrt(kwargs.get("a") * kwargs.get("b"))
    return round(result, 2)


try:
    x = 6
    y = 6
    # print("Media geometrica = ", media_geometrica(a=x, b=y))
    # x = int(input("Introduceti primul numar "))
    # y = int(input("Introduceti al doilea numar "))
    # print("Media geometrica = ", media_geometrica(a=x, b=int(y)))
    print("Media geometrica = ", media_geometrica_var(a=x, b=y))
    # print("Media geometrica = ", media_geometrica_var(a=7, b=8))
except ValueError:
    print("Va rugam sa introduceti doar cifre!")
