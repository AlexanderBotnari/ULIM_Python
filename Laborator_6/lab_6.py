from pprint import pprint


class Angajat:
    def __init__(self, nr=None, nume=None, prenume=None, functie=None, adresa=None, telefon=None, salariu=None):
        self.nr = nr
        self.nume = nume
        self.prenume = prenume
        self.functie = functie
        self.adresa = adresa
        self.telefon = telefon
        self.salariu = salariu

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Administratie(Angajat):
    def __init__(self, nr, nume, prenume, functie, adresa, telefon, salariu,
                 categorie_de_manager=None, nr_persoane_conducere=None):
        super().__init__(nr=nr, nume=nume, prenume=prenume, functie=functie, adresa=adresa, telefon=telefon,
                         salariu=salariu)
        self.categorie_de_manager = categorie_de_manager
        self.nr_persoane_conducere = nr_persoane_conducere

    def __str__(self):
        return super().__str__()


class Proprietar(Administratie):
    def __init__(self, nr, nume, prenume, functie, adresa, telefon, salariu, categorie_de_manager,
                 nr_persoane_conducere, tip_proprietar=None, procent_actiuni=None):
        super().__init__(nr, nume, prenume, functie, adresa, telefon, salariu, categorie_de_manager,
                         nr_persoane_conducere)
        self.tip_proprietar = tip_proprietar
        self.procent_actiuni = procent_actiuni

    def __str__(self):
        return super().__str__()


angajat = Angajat(nr=1, nume="Botnari", prenume="Felicia", functie="casier",
                  adresa="Sucevita 36/1", telefon="068735689", salariu=6000)
print(angajat)

administrator = Administratie(nr=2, nume="Botnari", prenume="Giku", functie="administrator",
                              adresa="Straseni,Panasesti", telefon="068567432", salariu=10000,
                              categorie_de_manager="superior", nr_persoane_conducere=4)
print(administrator)

proprietar = Proprietar(nr=3, nume="Botnari", prenume="Alexandru", functie="programator",
                        adresa="Sucevita 36", telefon="068327374", salariu=12000, categorie_de_manager="suprem",
                        nr_persoane_conducere=30, tip_proprietar="Sef Institutie", procent_actiuni=90)
print(proprietar)
