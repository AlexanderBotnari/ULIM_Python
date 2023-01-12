class Telefon:
    # constructor
    def __init__(self, IMEI=None, Marca=None, Model=None, Culoare=None, Tara=None, Pret=None):
        self.IMEI = IMEI
        self.Marca = Marca
        self.Model = Model
        self.Culoare = Culoare
        self.Tara = Tara
        self.Pret = Pret

    # printare obiect
    def __str__(self):
        return " IMEI: " + str(self.IMEI) + ", Marca: " + str(self.Marca) + \
               ", Model: " + str(self.Model) + ", Culoare: " + str(self.Culoare) + ", Tara: " + str(self.Tara) \
               + ", Pret: " + str(self.Pret) + " lei"

    # supraincarcarea operatorului "<"
    def __lt__(self, other):
        return self.Pret < other.Pret

    # functie proprie
    def compare_price(self, obj):
        if self.Pret > obj.Pret:
            print("Pretul lui", self.__class__, "este mai mare ca al lui", obj.__class__)
        elif self.Pret == obj.Pret:
            print("Pretul lui", self.__class__, "este egal cu al lui", obj.__class__)
        else:
            print("Pretul lui", self.__class__, "este mai mic ca al lui", obj.__class__)


class Telefon4G(Telefon):
    def __init__(self, IMEI=None, Marca=None, Model=None, Culoare=None, Tara=None, Pret=None,
                 viteza_internet=None, wifi=None):
        super().__init__(IMEI=IMEI, Marca=Marca, Model=Model, Culoare=Culoare, Tara=Tara, Pret=Pret)
        self.viteza_internet = viteza_internet
        self.wifi = wifi

    def __str__(self):
        return super().__str__() + "\n    , viteza internet: " + str(self.viteza_internet) \
               + ", wifi: " + str(self.wifi)


class Telefoane4G_max(Telefon4G):
    def __init__(self, IMEI=None, Marca=None, Model=None, Culoare=None, Tara=None, Pret=None,
                 viteza_internet=None, wifi=None, tehnologie=None):
        super().__init__(IMEI, Marca, Model, Culoare, Tara, Pret, viteza_internet, wifi)
        self.tehnologie = tehnologie

    def __str__(self):
        return super().__str__() + "\n    , tehnologie: " + str(self.tehnologie)


telefon = Telefon(IMEI=17376782163937, Marca="Xiaomi", Model="12T Pro", Culoare="Gri",
                  Tara="China", Pret="9999")
print(telefon)
# telefon1 = Telefon()
# print(telefon1)
# telefon2 = Telefon(IMEI=39716231, Marca="Realme", Model="9 Pro", Tara="Japonia")
# print(telefon2)

telefon_4g = Telefon4G(IMEI=1380976177, Marca="Iphone", Model="13 Pro", Culoare="Albastru",
                       Tara="USA", Pret="18000", viteza_internet="1 GB/s", wifi=True)
print(telefon_4g)
# telefon_4g_1 = Telefon4G()
# print(telefon_4g_1)
# telefon_4g_2 = Telefon4G(IMEI=7132198989, Marca="Apple", Model="SE 2", Tara="SUA", Pret=8000,
#                          wifi=True)
# print(telefon_4g_2)

telefon_max = Telefoane4G_max(IMEI=3289778232, Marca="Samsung", Model="S23 Ultra", Culoare="Purple",
                                     Tara="Coreea de Sud", Pret="29500", viteza_internet="1 Gb/s", wifi=True,
                                     tehnologie="Wi-Fi 6")
print(telefon_max)
# telefon_max_1 = Telefoane4G_max()
# print(telefon_max_1)
# telefon_max_2 = Telefoane4G_max(IMEI=13279328921, Marca="Nokia", Model="3310", Tara="Finlanda",
#                                        wifi=False, tehnologie="GPRS")
# print(telefon_max_2)

# Verificarea supraincarcarii operatorului "<"
print("Telefonul cu 4g are pretul mai mic decit telefonul cu capacitati maxime?:", telefon_4g < telefon_max)

# Apelarea functiei proprii
telefon_4g.compare_price(telefon_max)
