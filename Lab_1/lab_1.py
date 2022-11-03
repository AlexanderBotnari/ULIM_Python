import math

while True:
    x = input("Introduceti cifra x = ")
    try:
        x = int(x)
    except ValueError:
        print("Va rugam sa introduceti valoarea lui x ")
        continue

    if x != 0:
        y = math.pow(math.e, 2 * x) + x - 2 / math.pow(x, 3) - math.fabs(2 * x)
        if y < 0:
            print("y este negativ, y =", round(y, 2))
            break
        else:
            print("y este pozitiv, y =", round(y, 2))
            break
    else:
        print("y nu poate fi calculat cu valoarea 0")
        break
