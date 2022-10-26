
number = int(input("Introduceti numarul : "))
count = number
factorial = 1

while count > 1:
    factorial *= count
    count -= 1

print("Factorialul numarului ", number, "este", factorial)
