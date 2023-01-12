import random


def average(matrix):
    matrix_sum = 0
    count = 0

    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            matrix_sum += matrix[i][k]
            count += 1

    matrix_average = matrix_sum / count
    return matrix_average


# /////////////////////////////////Lista/////////////////////
# x = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(average(matrix=x))

# citire de la tastatură
# matrix = []
# matrix_length = input('Introduceti lungimea matricei : ')
# for length in range(int(matrix_length)):
#     user_text = 'Introduceti rindul ' + str(length+1) + ' : '
#     input_string = input(user_text)
#     user_list = input_string.split()
#     # Convertam elementele in tipul int
#     for i in range(len(user_list)):
#         user_list[i] = int(user_list[i])
#
#     matrix.append(user_list)
#
# print('Matrice : ', matrix)
# print('Media aritmetica : ', average(matrix=matrix))

# atribuire directa
# print(average(matrix=[[1, 2, 3, 4], [5, 6, 7, 8]]))

# atribuire random
# user_matrix = []
#
# for j in range(random.randint(2, 5)):
#     user_list = []
#     for _ in range(random.randint(2, 5)):
#         number = random.randint(1, 10)
#         user_list.append(number)
#
#     if user_list:
#         user_matrix.append(user_list)
#
# print(user_matrix)
# print(average(matrix=user_matrix))

# //////////////////////Tuple///////////////////////////////
# user_tuple = ((1, 2, 3, 4), (5, 6, 7, 8))
# print(user_tuple)
# print(average(matrix=user_tuple))

# citire de la tastatură
# matrix_tuple = []
# matrix_length = input('Introduceti lungimea matricei : ')
# for length in range(int(matrix_length)):
#     user_text = 'Introduceti rindul ' + str(length+1) + ' : '
#     input_string = input(user_text)
#     user_tuple = tuple(int(el) for el in input_string.split(' '))
#
#     matrix_tuple.append(user_tuple)
#
# # convertam lista in tuple
# user_tuple = tuple(matrix_tuple)
# print('Matrice : ', user_tuple)
# print('Media aritmetica : ', average(matrix=user_tuple))

# atribuire directa
# print(average(matrix=((1, 2, 3, 4), (5, 6, 7, 8))))

# atribuire random
user_list = []
for j in range(random.randint(2, 5)):
    custom_list = []
    for _ in range(random.randint(2, 5)):
        number = random.randint(1, 10)
        custom_list.append(number)

    if custom_list:
        # convertam in tuple
        custom_tuple = tuple(custom_list)
        user_list.append(custom_tuple)
# convertam in tuple
user_tuple = tuple(user_list)
print(user_tuple)
print(average(matrix=user_tuple))
