# i/ni darba risinājums:
import sqlite3
db = sqlite3.connect("23_nodarbiba.db")
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS autors (\
            id INTEGER UNIQUE,\
            lietotajvards STRING,\
            parole STRING,\
            epasts STRING,\
            PRIMARY KEY (id AUTOINCREMENT)\
)")

cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("CREATE TABLE IF NOT EXISTS ieraksts (\
            id INTEGER UNIQUE,\
            autors STRING,\
            nosaukums STRING,\
            teksts STRING,\
            izveidots STRING,\
            redzams INTEGER,\
            PRIMARY KEY (id AUTOINCREMENT)\
            FOREIGN KEY (autors) REFERENCES autors(id) ON DELETE CASCADE\
)")
cur.execute("CREATE TABLE IF NOT EXISTS komentars (\
            id INTEGER UNIQUE,\
            ieraksts STRING,\
            autors STRING,\
            teksts STRING,\
            redzams INTEGER,\
            PRIMARY KEY (id AUTOINCREMENT)\
            FOREIGN KEY (ieraksts) REFERENCES ieraksts(id) ON DELETE CASCADE\
)")

cur.execute("INSERT INTO autors (lietotajvards, parole, epasts) \
            VALUES\
            (\"admin\", \"parole\", \"....\"),\
            (\"...\", \"...\", \"...\")")
cur.execute("INSERT INTO ieraksts (autors, nosaukums, teksts, redzams) \
            VALUES\
            (1, \"Sveika pasaule\", \":)\", 1),\
            (\"...\", \"...\", \"...\")")

cur.close()
db.commit()
db.close()