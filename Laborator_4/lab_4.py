import random


def average(col):
    suma = sum(col)
    result = suma / len(col)
    return result


# /////////////////////////////////Lista/////////////////////
# x = [1, 2, 3, 4]
# print(average(col=x))

# citire de la tastatură
# input_string = input('Introduceti elementele listei : ')
# user_list = input_string.split()
# print('list: ', user_list)
# # Convertam elementele in tipul int
# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])
# print(average(col=user_list))

# atribuire directa
# print(average(col=[1, 2, 3, 4]))

# atribuire random
# user_list = []
# for _ in range(0, 5):
#     n = random.randint(1, 10)
#     user_list.append(n)
# print(user_list)
# print(average(col=user_list))

# //////////////////////Tuple///////////////////////////////
# user_tuple = (1, 2, 3, 4)
# print(user_tuple)
# print(average(col=user_tuple))

# citire de la tastatură
# user_input = input('Introduceti elementele : ')
# user_tuple = tuple(int(el) for el in user_input.split(' '))
# print('tuple: ', user_tuple)
# print(average(col=user_tuple))

# atribuire directa
# print(average(col=(1, 2, 3, 4)))

# atribuire random
user_tuple = ()
for _ in range(0, 5):
    user_tuple += (random.randint(1, 10),)
print(user_tuple)
print(average(col=user_tuple))
