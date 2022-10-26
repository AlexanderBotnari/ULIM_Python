import random


def average(lista):
    suma = sum(lista)
    result = suma / len(lista)
    return result


# Lista
# x = [1, 2, 3, 4]
# print(average(lista=x))

# citire de la tastatură
# input_string = input('Introduceti elementele listei : ')
# user_list = input_string.split()
# print('list: ', user_list)
# # Convertam elementele in tipul int
# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])
# print(average(lista=user_list))

# atribuire directa
# print(average(lista=[1, 2, 3, 4]))

# atribuire random
user_list = []
for _ in range(0, 5):
    n = random.randint(1, 10)
    user_list.append(n)

print(user_list)
print(average(lista=user_list))
