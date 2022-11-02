import math


# exceptie impartire la zero
# a = 8
# b = 0
# try:
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Nu este posibil de impartit la zero!")

# exceptie radical din numar negativ
# try:
#     print(math.sqrt(-2))
# except ValueError as e:
#     print("Nu se poate de calculat radical din numar negativ!")

# exceptie accesarea unui element inexistent in tablou
# user_list = [1, 2, 3, 4, 5]
# try:
#     print(user_list[5])
# except IndexError as e:
#     print("Elementul cu index-ul dat nu exista!")

# exceptie element în afara unui șir de caractere
# user_str = "Python"
# try:
#     print(user_str[7])
# except IndexError as e:
#     print("Litera pe pozitia data nu exista!")

# exceptie în loc de număr utilizatorul introduce litere
# try:
#     user_input = int(input("Introduceti un numar: "))
#     print(user_input)
# except ValueError as e:
#     print("Va rugam sa introduceti doar cifre!")

# exceptie când încercăm să apelăm o metodă a unui obiect care are referință nulă
# None se refera la obiectul NoneType , intotdeuna are cel putin o referinta
# class Person:
#     def __init__(self):
#         self.__class__ = None
#         pass
#
#     @staticmethod
#     def print_info():
#         pass
#
#
# try:
#     person = Person()
#     print(person.print_info())
# except TypeError as e:
#     print("Obiectul are tipul None")


# exceptie proprie
class NegativeAgeException(Exception):
    pass


print("Programul starteaza!")
try:
    age = int(input("Introduceti varsta : "))
    if age < 0:
        raise NegativeAgeException("Exception: Varsta negativa nu exista!")
    print("Varsta : ", age)
except NegativeAgeException as e:
    print(e)
print("Programul a luat sfarsit!")
