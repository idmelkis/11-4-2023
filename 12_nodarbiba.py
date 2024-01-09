# Mainīgajiem
# + Krāsa
# + Marka
# + Dzinēja tips
# + Riteņu izmērs
# + Ātrums
# Funkcijas/Metodes
# - Paātrinājums
# - Bremzēšana
# - Pa labi
# - Pa kreisi
# class nosaukums:
#     0_0
class Auto:
    krasa: str = ""
    marka: str = ""
    tips: str = ""
    izmers: float = 0.0
    atrums: float = 0.0
    virziens: float

    def __init__(self, _krasa :str, _marka :str) -> None:
        self.krasa = _krasa
        self.marka = _marka
        self.virziens = 0.0
    def __str__(self) -> str:
        return f"Marka: {self.marka}, Krasa: {self.krasa}, Atrums: {self.atrums}, Virziens: {self.virziens}"

    def paatrinajums(self) -> None:
        '''Paātrina mašīnu'''
        self.atrums += 0.5
    def bremzesana(self):
        if self.atrums > 0:
            self.atrums -= 0.5
    def pa_labi(self):
        self.virziens = 1.0
    def pa_kreisi(self):
        self.virziens = -1.0
    def taisni(self):
        self.virziens = 0
    def status(auto):
        print(auto)

masina1 = Auto("Sarkana", "Audi")
masina1.paatrinajums()
masina1.bremzesana()
masina1.paatrinajums()
masina1.paatrinajums()
#print(masina1)
Auto.status(masina1)
#masina1.status()

masina2 = Auto()
print(masina2)
#masina2.status()
masina2 = Auto("Zala", "BMW", 123)