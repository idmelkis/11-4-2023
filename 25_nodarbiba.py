# Izveidot datu bāzi kas glabās informāciju par CSN pārkāpumu sodiem
# 1. Tabula - Pārkāpējs [ ID, Vecums, Vārds, Uzvārds, PersonasKods ]
# 2. Tabula - Sods [ ID, SodaPunkti, Pants, NaudasSods, ApmaksasTermiņš, MašīnasNr, Laiks, Vieta ]

# ----
# 1. Tabula - Pārkāpējs [ ID, Vārds, 
#                         Uzvārds, PersonasKods ]
# 2. Tabula - Sods [ ID, SodaPunkti, Pants, 
#                   MašīnasNr, Laiks, Vieta, Pārkāpējs(ID) ]
# 1 : N attiecība
# ----
# 

# import sqlite3
# db = sqlite3.connect("25_nodarbiba.db")
# cur = db.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS parkapejs (\
#             id INTEGER UNIQUE,\
#             vards STRING,\
#             uzvards STRING,\
#             PK INTEGER,\
#             PRIMARY KEY (id AUTOINCREMENT)\
# )")

# cur.execute("PRAGMA foreign_keys = ON;")
# cur.execute("CREATE TABLE IF NOT EXISTS sods (\
#             id INTEGER UNIQUE,\
#             SodaPunkti INTEGER,\
#             Pants STRING,\
#             MasinasNR STRING,\
#             Laiks STRING,\
#             Vieta STRING,\
#             parkapejsID INTEGER,\
#             PRIMARY KEY (id AUTOINCREMENT)\
#             FOREIGN KEY (parkapejsID) REFERENCES parkapejs(id)\
# )")

# # Datuma formatēšana 
# # 2024. gada 30. aprīlis 08:32:00
# # 202430083200
# # 1714455120

# # INSERT INTO ... VALUES ...

# cur.close()
# db.commit()
# db.close()

# Uzdevums: Izveidot mapi output, saglabāt failu ar lietotāja dotu nosaukumu,
# kurš satur pašreizējo laiku
# Pašreizējais laiks UNIX formātā:
# import time
# str(int(time.time()))
import os

if not os.path.exists("output"):
    os.mkdir("output")

nosaukums = input("Lūdzu ievadat faila nosaukumu: ")
with open(f'output\\{nosaukums}', 'w') as f:
    import time
    f.write(str(int(time.time())))
