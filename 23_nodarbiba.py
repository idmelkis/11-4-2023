import sqlite3
db = sqlite3.connect("23_nodarbiba.db")
cur = db.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS atzime (\
#             id INTEGER UNIQUE,\
#             prieksmets STRING,\
#             skolens STRING,\
#             atzime INTEGER,\
#             PRIMARY KEY (id AUTOINCREMENT)\
# )")

# # cur.execute('INSERT INTO atzime (prieksmets, skolens, atzime) VALUES\
# #             ("Matemātika", "Jānis", 6), ("Lat. valoda", "Pēteris", 9),\
# #             ("Matemātika", "Māris", 2), ("Vācu Valoda", "Jana", 4),\
# #             ("Krievu Valoda", "Anna", 9)')

# cur.execute('SELECT prieksmets,skolens,max(atzime) FROM atzime') # min/max
# results = cur.fetchall()
# print(results)
# cur.execute('SELECT prieksmets,skolens,max(atzime) FROM atzime GROUP BY prieksmets') # min/max
# results = cur.fetchall()
# print(results)

cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("CREATE TABLE IF NOT EXISTS supplier (\
            SupplierID INTEGER UNIQUE,\
            SupplierName TEXT,\
            Address TEXT,\
            Phone TEXT,\
            PRIMARY KEY (SupplierID AUTOINCREMENT)\
)")

#cur.execute("DROP TABLE products")
cur.execute("CREATE TABLE IF NOT EXISTS produkts (\
            ProductID INTEGER UNIQUE,\
            ProductName TEXT,\
            SupplierID INTEGER,\
            Price FLOAT,\
            PRIMARY KEY (ProductID AUTOINCREMENT)\
            FOREIGN KEY (SupplierID) REFERENCES supplier(SupplierID)\
)")

cur.execute("INSERT INTO supplier (SupplierName, Address, Phone) \
            VALUES \
            (\"AI loģistika\", \"Nekuriene\", \"+0 0000-000\"),\
            (\"CLV loģistika\", \"LV\", \"+371 00000000\")")
cur.execute("INSERT INTO Products (ProductName, SupplierID, Price)\
            VALUES \
            (\"Telefons\", 1, 1000.0),\
            (\"Dators\", 1, 2000.0),\
            (\"Soma\", 2, 40.0),\
            (\"Burtnīca\", 2, 2.0)")

cur.close()
db.commit()
db.close()