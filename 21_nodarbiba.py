# class Lietotajs:
#     id            : int
#     lietotajvards : str
#     parole        : str
#     vards         : str
#     vecums        : int
#     def __init__(self, id, lvards, parole, vards, vecums) -> None:
#         self.id = id
#         self.lietotajvards = lvards
#         self.parole = parole
#         self.vards = vards
#         self.vecums = vecums
# l1 = Lietotajs(1, "lietotajs", "****", "v1", 20)
# l1 = Lietotajs(2, "lietotajs2", "****", "v2", 20)

# class Prece:
#     id            : int
#     nosaukums     : str
#     cena          : float

# class Pirkumi:
#     id            : int
#     prece_id      : int
#     lietotajs_id  : int

# Indeksi: https://www.geeksforgeeks.org/indexing-in-databases-set-1/

class Lietotajs:
    id            : int
    lietotajvards : str
    parole        : str
    vards         : str
    vecums        : int
    def __init__(self, id, lvards, parole, vards, vecums) -> None:
        self.id = id
        self.lietotajvards = lvards
        self.parole = parole
        self.vards = vards
        self.vecums = vecums

import sqlite3

db = sqlite3.connect('21_nodarbiba.db')
# bool = True/False = int 1/0
# Datu tipi: https://www.sqlite.org/datatype3.html
# CREATE TABLE <nosaukums> (<kolona> <DATU TIPS>, <kolona> <DATU TIPS>)
# AUTOINCREMENT - Automātiski palielina vērtību par 1 katrā ierakstā
# PRIMARY KEY - Speciāla atslēga kuru izmantojam lai paātrinātu datu piekļuvi
create_db = "CREATE TABLE Lietotajs (id INTEGER AUTOINCREMENT PRIMARY KEY,\
vards STRING,\
lietotajvards STRING,\
parole STRING,\
vecums INTEGER)"
cur = db.cursor()

db.commit()
db.close()

# with sqlite3.connect('21_nodarbiba.db') as db:
#     pass