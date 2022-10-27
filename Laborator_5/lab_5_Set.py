import random
# /////////////////////////////////multimi/////////////////////////////////////////
# atribuire directa
# user_set_1 = {"Programarea C++", 31, "ianuarie", 1999, 10, 9, 8}
# user_set_2 = {"Programarea C++", 31, "ianuarie", 1999, 7, 5, 6}

# atribuirea de la tastatura
# user_set_1 = set(input("Introduceti valorile multumii 1: ").split())
# print(user_set_1)
# user_set_2 = set(input("Introduceti valorile multumii 2: ").split())
# print(user_set_2)

# atribuirea random
user_set_1 = {"Programarea C++", 31, "ianuarie", 1999, random.randint(5, 10), random.randint(5, 10),
              random.randint(5, 10)}
user_set_2 = {"Programarea C++", 31, "ianuarie", 1999, random.randint(5, 10), random.randint(5, 10),
              random.randint(5, 10)}
print("Multimea initiala 1 : ", user_set_1)
print("Multimea initiala 2 : ", user_set_2)

# reuniunea
print("Reuniunea >>>", user_set_1.union(user_set_2))

# intersecția
print("Intersectia >>>", user_set_1.intersection(user_set_2))

# diferența
print("Diferenta 1 >>>", user_set_1.difference(user_set_2))
print("Diferenta 2 >>>", user_set_2.difference(user_set_1))
