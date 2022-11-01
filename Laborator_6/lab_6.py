class Angajat:
    # constructor
    # permite crearea initializarea obiectelor fara parametri,cu toti parametri si doar cu cativa
    def __init__(self, nr=None, nume=None, prenume=None, functie=None, adresa=None, telefon=None, salariu=None):
        self.nr = nr
        self.nume = nume
        self.prenume = prenume
        self.functie = functie
        self.adresa = adresa
        self.telefon = telefon
        self.salariu = salariu

    # printare obiect
    def __str__(self):
        return str(self.nr) + ". Nume: " + str(self.nume) + ", Prenume: " + str(self.prenume) + \
               ", Functie: " + str(self.functie) + ", Adresa: " + str(self.adresa) + ", Telefon: " + str(self.telefon) \
               + ", Salariu: " + str(self.salariu) + " lei"

    # supraincarcarea operatorului "<"
    def __lt__(self, other):
        return self.salariu < other.salariu

    # functie proprie
    def compare_salary(self, obj):
        if self.salariu < obj.salariu:
            print("Salariul lui", self.__class__, "este mai mic ca al lui", obj.__class__)
        elif self.salariu == obj.salariu:
            print("Salariul lui", self.__class__, "este egal cu al lui", obj.__class__)
        else:
            print("Salariul lui", self.__class__, "este mai mare ca al lui", obj.__class__)


class Administratie(Angajat):
    def __init__(self, nr=None, nume=None, prenume=None, functie=None, adresa=None, telefon=None, salariu=None,
                 categorie_de_manager=None, nr_persoane_conducere=None):
        super().__init__(nr=nr, nume=nume, prenume=prenume, functie=functie, adresa=adresa, telefon=telefon,
                         salariu=salariu)
        self.categorie_de_manager = categorie_de_manager
        self.nr_persoane_conducere = nr_persoane_conducere

    def __str__(self):
        return super().__str__() + "\n    , Categorie de Manager: " + str(self.categorie_de_manager) \
               + ", Numar de persoane in conducere: " + str(self.nr_persoane_conducere)


class Proprietar(Administratie):
    def __init__(self, nr=None, nume=None, prenume=None, functie=None, adresa=None, telefon=None, salariu=None,
                 categorie_de_manager=None, nr_persoane_conducere=None, tip_proprietar=None, procent_actiuni=None):
        super().__init__(nr, nume, prenume, functie, adresa, telefon, salariu, categorie_de_manager,
                         nr_persoane_conducere)
        self.tip_proprietar = tip_proprietar
        self.procent_actiuni = procent_actiuni

    def __str__(self):
        return super().__str__() + "\n    , Tip proprietar: " + str(self.tip_proprietar) + ", Procent actiuni: " \
               + str(self.procent_actiuni) + "%"


angajat = Angajat(nr=1, nume="Botnari", prenume="Felicia", functie="casier",
                  adresa="Sucevita 36/1", telefon="068735689", salariu=6000)
print(angajat)
# angajat1 = Angajat()
# print(angajat1)
# angajat2 = Angajat(nr=1, nume="Botnari", prenume="Felicia", functie="casier")
# print(angajat2)

administrator = Administratie(nr=2, nume="Botnari", prenume="Giku", functie="administrator",
                              adresa="Straseni,Panasesti", telefon="068567432", salariu=10000,
                              categorie_de_manager="superior", nr_persoane_conducere=4)
print(administrator)
# administrator1 = Administratie()
# print(administrator1)
# administrator2 = Administratie(nr=2, nume="Botnari", prenume="Giku", functie="administrator", salariu=10000,
#                                categorie_de_manager="superior", nr_persoane_conducere=4)
# print(administrator2)

proprietar = Proprietar(nr=3, nume="Botnari", prenume="Alexandru", functie="programator",
                        adresa="Sucevita 36", telefon="068327374", salariu=12000, categorie_de_manager="suprem",
                        nr_persoane_conducere=30, tip_proprietar="Sef Institutie", procent_actiuni=90)
print(proprietar)
# proprietar1 = Proprietar()
# print(proprietar1)
# proprietar2 = Proprietar(nr=3, nume="Botnari", prenume="Alexandru", functie="programator",salariu=12000,
#                          categorie_de_manager="suprem", nr_persoane_conducere=30, tip_proprietar="Sef Institutie",
#                          procent_actiuni=90)
# print(proprietar2)

print("**********************************************************************************************")
proprietar.compare_salary(administrator)

print("Administratorul are salariu mai mic ca proprietarul?:", administrator < proprietar)
