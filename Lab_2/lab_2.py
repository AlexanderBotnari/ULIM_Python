number = int(input("Introduceti lungimea sirului : "))

suma = 0.0
for item in range(1, number + 1):
    suma += 1.0 / item

print("Suma este ", round(suma, 2))
