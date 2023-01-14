import pickle
# biblioteca de serializare si deserializare a obiectelor pe disc


def introducere_date():
    nr, nume, prenume, localitate, adresa, telefon, nota_medie = input("Introduceti datele prin virgula:").split(",")
    user_dict = {'nr': nr, 'nume': nume, 'prenume': prenume, 'localitatea': localitate,
                 'adresa': adresa, 'telefon': telefon, 'nota medie': nota_medie}
    return user_dict


def creare_fisier():
    file = open("user_file.txt", "wb")
    pickle.dump(introducere_date(), file)
    file.close()
    print("File created succesfull!")


def afisare_continut():
    file = open('user_file.txt', 'rb')
    try:
        while True:
            data = pickle.load(file)
            print(data)
    except EOFError:
        pass
    file.close()


def adaugare_date():
    file = open("user_file.txt", "ab")
    pickle.dump(introducere_date(), file)
    print("Data added succesfull!")
    file.close()


def modificare_date():
    file = open('user_file.txt', 'rb')
    lst = []
    while True:
        try:
            rec = pickle.load(file)
            lst.append(rec)
        except EOFError:
            break
    file.close()

    nr = input("Introduceti nr inregistrarii de modificat: ")
    nume = input("Introduceti numele: ")
    prenume = input("Introduceti prenumele: ")
    localitatea = input("Introduceti localitatea: ")
    adresa = input("Introduceti adresa: ")
    telefon = input("Introduceti telefon: ")
    nota_medie = float(input("Introduceti nota medie: "))
    for i in range(len(lst)):
        if lst[i]['nr'] == nr:
            lst[i]['nume'] = nume
            lst[i]['prenume'] = prenume
            lst[i]['localitatea'] = localitatea
            lst[i]['adresa'] = adresa
            lst[i]['telefon'] = telefon
            lst[i]['nota medie'] = nota_medie
    file = open('user_file.txt', 'wb')
    for i in lst:
        pickle.dump(i, file)
    file.close()


def eliminare_date():
    file = open('user_file.txt', 'rb')
    lst = []
    while True:
        try:
            rec = pickle.load(file)
            lst.append(rec)
        except EOFError:
            break
    file.close()

    nr = input("Introduceti numarul inregistrarii ce doriti sa stergeti: ")
    file = open('user_file.txt', 'wb')
    for i in lst:
        if i['nr'] == nr:
            continue
        pickle.dump(i, file)
    file.close()
    print("Fisierul a fost curatat de inregistrarea nr: ", nr)


def prelucrare_date():
    file = open("user_file.txt", 'rb')
    try:
        while True:
            data = pickle.load(file)
            user_dict = data
            nota_medie = float(user_dict['nota medie'])
            if nota_medie < 5:
                print(user_dict)
            else:
                pass
    except EOFError:
        pass
    file.close()


while True:
    print("###################### Main Menu ######################")
    menu_value = int(input("Alegeti optiunea :\n"
                           "1 - Creare fisier\n"
                           "2 - Afisare continut\n"
                           "3 - Adaugare date (nr, nume, prenume, localitate, adresa, telefon, nota_medie)\n"
                           "4 - Modificare date\n"
                           "5 - Eliminare date\n"
                           "6 - Afisare studenti cu nota mai mica ca 5\n"
                           "7 - Iesire din program\n"
                           "Introduceti optiunea aici >>> "))

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
