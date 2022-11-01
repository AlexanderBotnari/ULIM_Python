import sys
import fileinput
import ast


def convert_list(list1):
    init = iter(list1)
    res_dct = dict(zip(init, init))
    return res_dct


def introducere_date():
    nr, nume, prenume, localitate, adresa, telefon, nota_medie = input("Introduceti datele prin virgula:").split(",")
    user_list = ['nr, ', nr, ', nume, ', nume, ', prenume, ', prenume, ', localitatea, ', localitate,
                 ', adresa, ', adresa, ', telefon, ', telefon, ', nota medie, ', nota_medie]
    return user_list


def creare_fisier():
    file = open("user_file.txt", 'w')
    for key, value in introducere_date().items():
        file.writelines(" "+key + " : " + value + ", ")
    file.close()
    print("File created succesfull!")


def afisare_continut():
    file = open("user_file.txt", 'r+')
    print(file.read())
    file.close()


def adaugare_date():
    file = open("user_file.txt", 'a+')
    for data in introducere_date():
        file.writelines(data)
    print("Data added succesfull!")
    file.close()


def modificare_date():
    # am folosit biblioteca fileinput si sys
    old_value = input("Introduceti valoarea de modificat: ")
    new_value = input("Introduceti valoarea noua: ")
    for line in fileinput.input("user_file.txt", inplace=True):
        line = line.replace(old_value, new_value)
        sys.stdout.write(line)


def eliminare_date():
    f = open("user_file.txt", "r+")
    f.seek(0)
    f.truncate()
    print("Fisierul a fost curatat complet!")


def prelucrare_date():
    user_list = []
    # file = open("user_file.txt", 'r+')
    with open('user_file.txt', 'rt') as file:
        for line in file:
            user_list.append(line.replace("'", ""))

    user_dict = convert_list(user_list)
    # print(user_list[6])
    print('List>>>', user_list)
    print('Dict>>>', user_dict)
    # De afișat studenții cu nota media mai mică decât 5


    # if nota_medie < 5:
    #     print(file.read())
    #     file.close()
    # else:
    #     print("Nota este trecatoare!")


while True:
    print("###################### Main Menu ######################")
    menu_value = int(input("1 - Creare fisier\n"
                           "2 - Afisare continut\n"
                           "3 - Adaugare date\n"
                           "4 - Modificare date\n"
                           "5 - Eliminare date\n"
                           "6 - Prelucrare date dupa conditie\n"
                           "7 - Iesire din program\n"))
    if menu_value == 1:
        creare_fisier()
        continue
    elif menu_value == 2:
        afisare_continut()
        continue
    elif menu_value == 3:
        adaugare_date()
        continue
    elif menu_value == 4:
        modificare_date()
        continue
    elif menu_value == 5:
        eliminare_date()
        continue
    elif menu_value == 6:
        prelucrare_date()
        continue
    elif menu_value == 7:
        print("Iesire din program !")
        break
    else:
        print("Menu value error!")
        continue
