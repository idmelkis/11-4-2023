# Izveidojat klasi Restorāns. Šai klasei vajag saturēt informāciju par 
# * pieejamajiem ēdieniem un to cenu (ēdienkarte). ({'nosaukums': cena})
# * pieejamajiem galdiņiem, un vai tie ir aizņemti. (Numurs, Aizņemts, Pirkumi)
#   * Galdiņa pirkumiem
# Izveidojat funkcijas, kas
# * Ļauj pievienot ēdienus pie ēdienkartes
# * Izvada ēdienkarti
# * Ļauj norezervēt galdiņu (atzīmē to kā aizņemtu)
# * Reģistrēt galdiņa pirkumus (ja galdiņš ir aizņemts)
class Galdins:
    numurs: int
    aiznemts: bool = False
    pirkumi = []

class Restorans:
    edienkarte :'dict[str, float]' = {}
    galdini: 'list[Galdins]'= []
    def pievienotEdienu(self, ediens: 'dict[str, float]'):
        ediens.update(ediens)
    def izvaditEdienkarti(self):
        print(self.edienkarte)
    def rezervetGaldinu(self, galdinaNr):
        for iii in self.galdini:
            if iii.numurs == galdinaNr:
                iii.aiznemts = True
    def registretPirkumu(self, galdinaNr :int, pirkums: str):
        for iii in self.galdini:
            if iii.numurs == galdinaNr and iii.aiznemts:
                iii.pirkumi.append(pirkums)
            else:
                print('Galdins nav atrasts vai nav aiznemts')



