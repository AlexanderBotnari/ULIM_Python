class Angajat:
    nr = None
    nume = None
    prenume = None
    functie = None
    adresa = None
    telefon = None
    salariu = None

    def __init__(self, nr=None, nume=None, prenume=None, functie=None, adresa=None, telefon=None, salariu=None):
        self.nr = nr
        self.nume = nume
        self.prenume = prenume
        self.functie = functie
        self.adresa = adresa
        self.telefon = telefon
        self.salariu = salariu

    def print_info(self):
        if self.nr is None \
                and self.nume is None \
                and self.prenume is None:
            print("Numele, prenumele si nr de ordine sunt obligatorii!")
        else:
            print(self.nr, self.nume, self.prenume, self.functie, self.adresa, self.telefon, self.salariu)


class Administratie(Angajat):
    categorie_de_manager = None
    nr_persoane_conducere = None

    def __init__(self):
        super().__init__()


class Proprietar(Angajat):
    tip_proprietar = None
    procent_actiuni = None

    def __init__(self):
        super().__init__()


proprietar = Proprietar()
proprietar.print_info()
