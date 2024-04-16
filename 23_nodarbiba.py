import sqlite3
db = sqlite3.connect("23_nodarbiba.db")
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS atzime (\
            id INTEGER UNIQUE,\
            prieksmets STRING,\
            skolens STRING,\
            atzime INTEGER,\
            PRIMARY KEY (id AUTOINCREMENT)\
)")

# cur.execute('INSERT INTO atzime (prieksmets, skolens, atzime) VALUES\
#             ("Matemātika", "Jānis", 6), ("Lat. valoda", "Pēteris", 9),\
#             ("Matemātika", "Māris", 2), ("Vācu Valoda", "Jana", 4),\
#             ("Krievu Valoda", "Anna", 9)')

cur.execute('SELECT prieksmets,skolens,max(atzime) FROM atzime') # min/max
results = cur.fetchall()
print(results)
cur.execute('SELECT prieksmets,skolens,max(atzime) FROM atzime GROUP BY prieksmets') # min/max
results = cur.fetchall()
print(results)

cur.close()
db.commit()
db.close()