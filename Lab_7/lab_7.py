def create_file():
    with open("studenti.txt", "w") as f:
        f.write("")
        print("Fisier creat!")


def add_student():
    with open("studenti.txt", "a") as f:
        data = input(
            "Introduceti datele studentului (nr., nume, prenume, localitate, adresa, telefon, nota_medie): ")
        f.write(data + "\n")
        print("Student adaugat!")


def print_all():
    with open("studenti.txt", "r") as f:
        print(f.read())


def prelucrare_conditie():
    with open("studenti.txt", "r") as f:
        students = f.readlines()
        for student in students:
            data = student.split(',')
            if int(data[6].strip()) > 9:
                print(student)


def update_student():
    with open("studenti.txt", "r") as f:
        students = f.readlines()
    with open("studenti.txt", "w") as f:
        flag = False
        for student in students:
            data = student.split(',')
            if data[0].strip() == "nr.":
                continue
            if data[0].strip() == input(
                    "Introduceti numarul studentului pe care doriti sa-l actualizati: "):
                flag = True
                new_data = input("Introduceti noile date despre student: ")
                f.write(new_data + "\n")
            else:
                f.write(student)
        if not flag:
            print("Nu s-a gasit studentul cu numarul specificat.")


def delete_student():
    with open("studenti.txt", "r") as f:
        students = f.readlines()
    with open("studenti.txt", "w") as f:
        flag = False
        for student in students:
            data = student.split(',')
            if data[0].strip() == "nr.":
                f.write(student)
                continue
            if data[0].strip() != input(
                    "Introduceti numarul studentului pe care doriti sa-l stergeti: "):
                f.write(student)
            else:
                flag = True
        if not flag:
            print("Nu s-a gasit studentul cu numarul specificat.")


def menu():
    while True:
        print("1 - Creare fisier")
        print("2 - Afisare continut fisier")
        print("3 - Adaugare student")
        print("4 - Actualizare student")
        print("5 - Stergere student")
        print("6 - Afisare studenti cu note mai mari ca 9")
        print("7 - Iesire din program")
        option = input("Alegeti optiunea: ")

        if option == "1":
            create_file()
            continue
        elif option == "2":
            print_all()
            continue
        elif option == "3":
            add_student()
            continue
        elif option == "4":
            update_student()
            continue
        elif option == "5":
            delete_student()
            continue
        elif option == "6":
            prelucrare_conditie()
            continue
        elif option == "7":
            break
        else:
            print("Optiune invalida.")


menu()
