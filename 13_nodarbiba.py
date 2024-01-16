# Vienkārš polimorfisms
class pirma_klase:
    def kautkada_funkcija(self):
        print("Viena klase dara vienu")
class otra_klase:
    def kautkada_funkcija(self):
        print("Otra klase dara ko citu")

viens = pirma_klase()
divi = otra_klase()
for i in (viens, divi):
    i.kautkada_funkcija()

class Transportlidzekli:
    atrums :float = 0.0
    ieslegts :bool = False
    marka :str = "Nedefinets"
    def __init__(self) -> None:
        print("Init transportlīdzekļiem!")
    def paatrinat(self):
        if self.ieslegts:
            self.atrums += 0.5
        # Izmetīs kļūdu
        # self.atrumkarbas_mod = self.atrumkarbas_mod + ""
    def bremzet(self):
        if self.atrums > 0:
            self.atrums -= 0.5
class Auto(Transportlidzekli):
    atrumkarbas_mod :str
    ritenu_skaits :int = 4
    krasa = ""
class Lidmasina(Transportlidzekli):
    sparnu_platums :float = 0.0
    marka = "Airbus"
    def __init__(self) -> None:
        print("Lidmašīna sāk darbu!")
    def paatrinat(self):
        self.atrums += 4
    def bremzet(self):
        print(self.marka)
        print(super().marka)
        super().bremzet()
        self.atrums -= 3.5

automasina = Auto()
automasina.ieslegts = True
automasina.paatrinat()
print(automasina.atrums)

lidmasina = Lidmasina()
lidmasina.paatrinat()
print(lidmasina.atrums)
lidmasina.bremzet()
print(lidmasina.atrums)

# Uzdevums: 1 Bāzes un vismaz 2 apakšklases. Par brīvu tēmu.
# Bāzes klasei vajag būt 2-3 mainīgie un vismaz viena funkcija
# Apakšklasēm jāizmanto polimorfisms lai pārrakstītu bāzes klases funkciju
# Tā, lai tā dara kaut ko citu (pietiek ar primitīvu print() funkc.)
# Pamēģinat izveidot objektus no šīm klasēm un izsaukt funkcijas/mainīgos.

# Uzdevums i/ni: Izveidot programmu un klašu grafiku
# Jāizveido klase "Banka Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50,
#   vai, ja izņemot paliktu zem €30 (piem. ja ir €100, un izņem €71, izņemt neļauj)
# Izveidojat apakšklasi "Krājkonts".
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju, 
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110)
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50,
#   vai, ja izņemot paliktu zem €30 (piem. ja ir €100, un izņem €71, izņemt neļauj)
# Izveidojat objektus no šīm klasēm
# Izsaucat pirmās klases ieskaitīšanas funkciju (€100), 
#   izsaucat izņemšanas funkciju €60.
#   izsaucat izņemšanas funkciju €80.
# Izsaucat otrās klases ieskaitīšanas funkciju (€100), 
#   un izsaucat izņemšanas funkciju €30