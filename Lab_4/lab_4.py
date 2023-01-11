import random


def sum_of_even(collection):
    even_collection = []
    for item in range(len(collection)):
        if collection[item] % 2 == 0:
            even_collection.append(collection[item])
    return sum(even_collection)


# List
# vector = [1, 2, 3, 4]
# print(sum_of_even(collection=vector))

# random
# custom_list = []
# for _ in range(0, 5):
#     x = random.randint(1, 10)
#     custom_list.append(x)
# print(custom_list)
# print(sum_of_even(collection=custom_list))

# from console
# element = input('Introduceti elementele : ')
# custom_list = element.split()
# print('list: ', custom_list)
# # Convert to int
# for i in range(len(custom_list)):
#     custom_list[i] = int(custom_list[i])
# print(sum_of_even(collection=custom_list))

# direct
# print(sum_of_even(collection=[1, 2, 3, 4]))

# Tuple
# custom_tuple = (1, 2, 3, 4)
# print(custom_tuple)
# print(sum_of_even(collection=custom_tuple))

# direct
# print(sum_of_even(collection=(1, 2, 3, 4)))

# random
custom_tuple = ()
for _ in range(0, 5):
    custom_tuple += (random.randint(1, 10),)
print(custom_tuple)
print(sum_of_even(collection=custom_tuple))

# from console
# elements = input('Introduceti elementele : ')
# custom_tuple = tuple(int(element) for element in elements.split(' '))
# print('tuple: ', custom_tuple)
# print(sum_of_even(collection=custom_tuple))

