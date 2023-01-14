import math


# exceptie radical din numar negativ
# try:
#     print(math.sqrt(-7))
# except ValueError as e:
#     print("Radical din numar negativ nu poate fi calculat!")

# exceptie Zero Division Error
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print("Imposibil de impartit la zero!")

# accesarea unui element inexistent in tablou
# custom_list = [10, 20, 30, 40, 50]
# try:
#     print(custom_list[7])
# except IndexError as e:
#     print("Indexare invalida")

# indexare element în afara unui șir de caractere
# custom_str = "ULIM2023"
# try:
#     print(custom_str[9])
# except IndexError as e:
#     print("Indexare invalida")

# eroare în loc de număr utilizatorul introduce litere
# try:
#     custom_input = int(input("Introduceti un numar: "))
#     print(custom_input)
# except ValueError as e:
#     print("Ati introdus litera in loc de cifra!")

# obiect care are referință nulă
# class SomeClass:
#     def __init__(self):
#         self.__class__ = None
#         pass
#
#     @staticmethod
#     def some_func():
#         pass
#
#
# try:
#     example = SomeClass()
#     print(example.some_func())
# except TypeError as e:
#     print("Obiectul are referinta nula!")


# exceptie proprie
class NonPassingNoteException(Exception):
    def __init__(self, message):
        self.message = message


try:
    note = int(input("Introduceti nota : "))
    if 5 > note > 0:
        raise NonPassingNoteException("Nota nu este trecatoare!")
    elif note <= 0:
        raise NonPassingNoteException("Nota nu poate fi negativa sau egala cu zero!")
    elif note > 10:
        raise NonPassingNoteException("Introduceti nota de la 1 la 10!")
    print("Nota : ", note)
except NonPassingNoteException as e:
    print(e.message)
