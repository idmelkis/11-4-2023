# Uzdevums i/ni: Izveidot programmu un klašu grafiku
# Jāizveido klase "Banka Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50,
#   vai, ja izņemot paliktu zem €30 (piem. ja ir €100, un izņem €71, izņemt neļauj)
class BankasKonts:
    atlikums :float = 0.0
    # kautkas :int = 0
    def __init__(self, sakumaAtlikums) -> None:
        self.atlikums = sakumaAtlikums
    def __str__(self) -> str:
        return f"Kontā ir {self.atlikums}"
    def ieskaitit(self, summa):
        self.atlikums = self.atlikums + summa
    def iznemt(self, summa):
        if self.atlikums >= 50 and self.atlikums - summa >= 30:
            self.atlikums -= summa
        else:
            print("nevar izņemt naudu: nepietiek līdzekļi")
    def funkcijaKautkoAtgriež(self, maingais :int) -> int:
        """ Tekstsxxdd """
        return 100

# Izveidojat apakšklasi "Krājkonts".
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju, 
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110)
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50,
#   vai, ja izņemot paliktu zem €30 (piem. ja ir €100, un izņem €71, izņemt neļauj)
class Krajkonts(BankasKonts):
    def __init__(self, sakumaAtlikums) -> None:
        super().__init__(sakumaAtlikums)
    def iznemt(self, summa):
        if self.atlikums >= 50 and self.atlikums - summa >= 30:
            self.atlikums -= summa + (summa * 0.1)
        else:
            print("nevar izņemt naudu: nepietiek līdzekļi")

# Izveidojat objektus no šīm klasēm
# Izsaucat pirmās klases ieskaitīšanas funkciju (€100), 
#   izsaucat izņemšanas funkciju €60.
#   izsaucat izņemšanas funkciju €80.
# Izsaucat otrās klases ieskaitīšanas funkciju (€100), 
#   un izsaucat izņemšanas funkciju €30

konts = BankasKonts(100)
print(konts)
konts.iznemt(60)
print(konts)
konts.iznemt(80)
print(konts)
konts.funkcijaKautkoAtgriež(0)
# konts2 = BankasKonts(0.0)
# konts2.ieskaitit(600)
# print(konts2)      
krajkonts = Krajkonts(100)
krajkonts.iznemt(30)
print(krajkonts)

# Precēm var izveidot klasi "Prece".
# Šī klase satur preces nosaukumu un 
# cenu (Abas vērtības uzstāda init funkcijā)
# vai izmantot vārdnīcu.
class Prece():
    nosaukums :str = ""
    cena :float = ""
    def __init__(self, _nosaukums, _cena) -> None:
        self.nosaukums = _nosaukums
        self.cena = _cena
# Izveidojat klasi "Grozs". Šī klase satur preces un to daudzumu.
# Klasei jānodrošina funkcijas, kas ļauj
#   pievienot preces, izņemt preces un
#   aprēķināt groza kopējo vērtību.
class Grozs():
    preces :'dict[Prece, int]' = {} # value = daudzums
    def pievienot(self, prece: Prece, daudzums :int):
        self.preces[prece] = daudzums
    def iznemt_preces(self, prece: Prece):
        for iii in self.preces.keys():
            if prece.nosaukums == iii.nosaukums:
                self.preces.pop(iii)
                break
    def aprekinam_vertibu(self) -> float:
        vertiba = 0.0
        for key, value in self.preces.items():
            vertiba += key.cena * value
        return vertiba
    def __str__(self) -> str:
        return f"Kopēja vērtība: {self.aprekinam_vertibu()}"

prece1 = Prece("Piens", 1.0)
prece2 = Prece("Viedtālrunis", 500.0)
grozs = Grozs()
grozs.pievienot(prece1, 3)
grozs.pievienot(prece2, 1)
print(grozs)
grozs.iznemt_preces(prece1)
print(grozs)



