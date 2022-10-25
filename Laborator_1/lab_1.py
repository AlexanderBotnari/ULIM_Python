from math import cos

x = int(input("Introduceti cifra x = "))
if x == " ":
    print("y este null")

y = (cos(x) + 7 * x) / ((x * x * x * x) - 3 * (x ** 2))

if y < 0:
    print("y este negativ, y = ", y)
elif y is None:
    print("y este nul")
else:
    print("y este pozitiv, y = ", y)
