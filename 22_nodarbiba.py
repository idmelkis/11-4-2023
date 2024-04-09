import sqlite3
db = sqlite3.connect('22_nodarbiba.db')
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS test (\
            id INTEGER,\
            value INTEGER,\
            textValue TEXT,\
            PRIMARY KEY(id AUTOINCREMENT)\
)")

# for i in range(0, 20):
#     cur.execute(f"INSERT INTO test (value) VALUES ({i})")

# Izvēlamies noteiktu kolonu
# cur.execute("SELECT (value) FROM test")
# results = cur.fetchall()
# print(results)

# Izvēlamies noteiktu vērtību
# https://www.sqlite.org/lang_expr.html#operators_and_parse_affecting_attributes
# https://www.sqlitetutorial.net/sqlite-where/
# cur.execute("SELECT textvalue FROM test WHERE value = 5")
# results = cur.fetchall()
# print(results)
# cur.execute("SELECT value FROM test WHERE textValue LIKE \"Šī%\"")
# results = cur.fetchall()
# print(results)
# cur.execute("SELECT id FROM test WHERE value > 8 AND value < 11")
# results = cur.fetchall()
# print(results)
# cur.execute("SELECT id FROM test WHERE value BETWEEN 8 AND 11")
# results = cur.fetchall()
# print(results)

# Sakārtot pēc kolonām
# cur.execute("SELECT * FROM test ORDER BY\
#             value DESC, id ASC")
# results = cur.fetchall()
# print(results)

# Iegūt tikai 5 vērtības
# cur.execute("SELECT * FROM test LIMIT 5")
# results = cur.fetchall()
# print(results)

# Funkcijas kolona
# cur.execute("SELECT min(value) FROM test") # count, max, min
# results = cur.fetchall()
# print(results)


# https://www.sqlite.org/foreignkeys.html
cur.execute("CREATE TABLE IF NOT EXISTS test (\
            id INTEGER,\
            value INTEGER,\
            textValue TEXT,\
            PRIMARY KEY(id AUTOINCREMENT)\
)")

# Ieslēgt foreign key atbalstu
cur.execute("PRAGMA foreign_keys = ON;")
# https://www.sqlitetutorial.net/sqlite-update/
#cur.execute("DROP TABLE test2")
cur.execute("CREATE TABLE IF NOT EXISTS test2 (\
            id INTEGER,\
            testId INTEGER,\
            PRIMARY KEY (id AUTOINCREMENT),\
            FOREIGN KEY (testId) REFERENCES test(id) ON DELETE RESTRICT\
)")

# https://www.sqlite.org/lang_delete.html
cur.execute("DELETE FROM test WHERE id = 9")

cur.close()
db.commit()
db.close()