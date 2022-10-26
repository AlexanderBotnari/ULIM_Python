from math import cos

while True:
    x = input("Introduceti cifra x = ")
    try:
        x = int(x)
    except ValueError:
        print("Valoarea lui x nu poate fi nula")
        continue

    if x != 0:
        y = (cos(x) + 7 * x) / ((x * x * x * x) - 3 * (x ** 2))
        if y < 0:
            print("y este negativ, y =", round(y, 2))
            break
        else:
            print("y este pozitiv, y =", round(y, 2))
            break
    else:
        print("y nu poate fi calculat cu valoarea x = 0")
        break
