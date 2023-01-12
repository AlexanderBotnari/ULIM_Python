import random
# ########################Prima parte a exercitiului (Multimi)#########################################################
# atribuire directa
# custom_set_1 = {"POO Java", 31, "ianuarie", 1999, 10, 9, 7, 9, 8, 10, 8}
# custom_set_2 = {"Python", 31, "ianuarie", 1999, 7, 8, 10, 8, 9}

# atribuirea de la tastatura
# custom_set_1 = set(input("Introduceti valorile multumii 1: ").split())
# print(custom_set_1)
# custom_set_2 = set(input("Introduceti valorile multumii 2: ").split())
# print(custom_set_2)

# atribuirea random
custom_set_1 = {"Programarea C++", 31, "ianuarie", 1999, random.randint(5, 10), random.randint(5, 10),
                random.randint(5, 10)}
custom_set_2 = {"Programarea C++", 31, "ianuarie", 1999, random.randint(5, 10), random.randint(5, 10),
                random.randint(5, 10)}
print("Multimea initiala 1 : ", custom_set_1)
print("Multimea initiala 2 : ", custom_set_2)

# intersecția
print("Intersectia : ", custom_set_1.intersection(custom_set_2))

# reuniunea
print("Reuniunea : ", custom_set_1.union(custom_set_2))

# diferența
print("Diferenta 1 : ", custom_set_1.difference(custom_set_2))
print("Diferenta 2 : ", custom_set_2.difference(custom_set_1))

# ########################A doua parte a exercitiului (Dictionare)#####################################################
# custom_dict = {"Tema": "POO Java",
#                "Clase": "tipuri de date definite de utilizator sau deja existente în sistem",
#                "Campuri": "un obiect având tipul unei clase sau o variabilă de tip primitiv",
#                "Proprietati": "un câmp (membru) căruia i se atașează două metode ce îi pot expune sau modifica "
#                               "starea",
#                "Specificatori de acces": " al cărui rol este de a restricţiona accesul la entitatea respectivă, din "
#                                          "perspectiva altor clase",
#                "Încapsularea": "se referă la acumularea atributelor şi metodelor caracteristice unei anumite"
#                                "categorii de obiecte într-o clasă. ",
#                "Mostenirea": "posibilitatea de a imprumuta metodele si campurile existenta in clasa (parinte) ",
#                "Polimorfism": "ofera posibilitatea de a folosi metodele mostenite sub mai multe forme",
#                "Abstractizarea": "are legatura cu ascunderea anumitor elemente care compun clasele",
#                "Constructor": "este o metoda speciala folosita la initializarea obiectului"}

# printare
# for key, value in custom_dict.items():
#     print("'", key, "' -", value)

# copie a dictionarului
# user_dict_2 = custom_dict.copy()
# for key, value in user_dict_2.items():
#     print("'", key, "' -", value)

# valoarea cheii
# print(custom_dict.get("Polimorfism"))

# cheile din dictionar
# print(custom_dict.keys())

# valorile perechilor
# print(custom_dict.items())

# sterge continutul dictionarului
# custom_dict.clear()
# print(custom_dict)

# sterge cheia si intoarce valoarea
# print(custom_dict.pop("Mostenirea"))
# print(custom_dict)

# metoda returneaza valoarea cheii dar daca nu  gaseste, nu da exceptie, dar creeaza o cheie cu valoarea none
# print(custom_dict.setdefault("Proprietate"))

# returneaza valorile din dictionar
# print(custom_dict.values())

# sterge si intoarce perechea
# print(custom_dict.popitem())
# print(custom_dict)
