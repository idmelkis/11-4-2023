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
# DB Browser: https://sqlitebrowser.org/

import sqlite3

db = sqlite3.connect('21_nodarbiba.db')
cur = db.cursor()

# bool = True/False = int 1/0
# Datu tipi: https://www.sqlite.org/datatype3.html
# CREATE TABLE <nosaukums> (<kolona> <DATU TIPS>, <kolona> <DATU TIPS>)
# AUTOINCREMENT - Automātiski palielina vērtību par 1 katrā ierakstā
# PRIMARY KEY - Speciāla atslēga kuru izmantojam lai paātrinātu datu piekļuvi
create_db = "CREATE TABLE IF NOT EXISTS Lietotajs (id INTEGER NOT NULL UNIQUE,\
vards STRING,\
lietotajvards STRING NOT NULL UNIQUE,\
parole STRING,\
vecums INTEGER,\
PRIMARY KEY(\"id\" AUTOINCREMENT))"
cur.execute(create_db)

# class Prece:
#     id            : int
#     nosaukums     : str
#     cena          : float # REAL
#     def __init__(self, id, nos, cena) -> None:
#         self.id = id
#         self.nosaukums = nos
#         self.cena = cena
create_db = "CREATE TABLE IF NOT EXISTS Prece (id INTEGER NOT NULL UNIQUE,\
nosaukums STRING,\
cena REAL,\
PRIMARY KEY(\"id\" AUTOINCREMENT))"
cur.execute(create_db)

# l1 = Lietotajs(1, "lietotajs", None, "v1", 33)
# ===
# insert_data = "INSERT INTO Lietotajs (vards, lietotajvards, vecums)\
# VALUES (\"lietotajs\", \"lietotajs\", 33)"
# cur.execute(insert_data)

# l2 = Lietotajs(4, "skolens", "hunter2", "Skolēns", 16)
# ===
# insert_data = "INSERT INTO Lietotajs (vards, lietotajvards, parole, vecums)\
# VALUES (\"Skolēns\", \"skolens\", \"hunter2\", 33)"
# cur.execute(insert_data)

#select = "SELECT (id, vards, lietotajvards, parole) FROM "
select = "SELECT * FROM Lietotajs"
cur.execute(select)

results = cur.fetchall()
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
result_objs = []
for result in results:
    result_objs.append(Lietotajs(result[0], result[2], result[1], result[3], result[4]))
print(result_objs[0].lietotajvards)

cur.close()
db.commit()
db.close()

# with sqlite3.connect('21_nodarbiba.db') as db:
#     pass