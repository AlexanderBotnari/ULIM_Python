# menu
import sys
import fileinput

nr, nume, prenume, localitate, adresa, telefon, nota_medie = input("Introduceti datele prin virgula:").split(",")
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
        file = open("user_file.txt", 'w')
        file.writelines([nr, nume, prenume, localitate, adresa, telefon, nota_medie])
        file.close()
        print("File created succesfull!")
        break
    elif menu_value == 2:
        file = open("user_file.txt", 'r+')
        print(file.read())
        file.close()
        break
    elif menu_value == 3:
        file = open("user_file.txt", 'a+')
        file.writelines([nr, nume, prenume, localitate, adresa, telefon, nota_medie])
        file.close()
        break
    elif menu_value == 4:
        old_value = input("Introduceti valoarea de modificat")
        new_value = input("Introduceti valoarea noua: ")
        for line in fileinput.input("user_file.txt", inplace=True):
            line = line.replace(old_value, new_value)
            sys.stdout.write(line)
        break
    elif menu_value == 5:
        f = open("user_file.txt", "r+")
        f.seek(0)
        f.truncate()
        break
    elif menu_value == 6:
        file = open("user_file.txt", 'r+')
        nota_medie = float(nota_medie)
        # De afișat studenții cu nota media mai mică decât 5
        if nota_medie < 5:
            print(file.read())
            file.close()
        else:
            print("Nota este trecatoare!")
        break
    elif menu_value == 7:
        print("Iesire din program !")
        break
    else:
        print("Menu value error!")