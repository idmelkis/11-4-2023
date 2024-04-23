# https://www.sqlitetutorial.net/sqlite-sample-database/
location = "C:\\Users\\idmelkis\\Downloads\\chinook\\chinook.db"
import sqlite3
db = sqlite3.connect(location)
cur = db.cursor()

# 1. Uzdevums
# Iegūt no tabulas "employees" visus cilvēku vārdus, 
# uzvārdus un e-pastus
# (LastName, FirstName, Email)
# cur.execute("SELECT FirstName, LastName, Email\
#             FROM employees")
# results = cur.fetchall()
# for value in results:
#     print(f"{value[0]} {value[1]} {value[2]}")
#print(results)
# cur.execute("SELECT * FROM employees")
# results = cur.fetchall()
# print(results)
# for value in results:
#     print(f"{value[2]} {value[1]} {value[14]}")

# 2. Uzdevums: Iegūt māksliniekus/grupas
# no tabulas "artists" kurām nosaukumā ir vārds "Black"
# Grupu nosaukumi ir kolonā "Name".
# cur.execute("SELECT Name FROM artists WHERE\
#             Name LIKE \"%Black%\"")
# results = cur.fetchall()
# print(results)

# 3. Uzdevums
# Izvadat no tabulas "customers" informāciju par to
# cik klienti ir noteiktam atbalsta personālam
# Personāla ID tiek glabāts kolonā SupportRepId.
# Saskaitīšanai izmantot funkciju COUNT,
# Grupēt ar GROUP BY.
# cur.execute("SELECT SupportRepId, COUNT(*)\
#             FROM customers\
#             GROUP BY SupportRepId")
# results = cur.fetchall()
# print(results)

# 4. Uzdevums
# Iegūt pirmos 3 ierakstus no tabulas "invoice_items"
# Kur invoice_id ir 3.
cur.execute("SELECT * FROM invoice_items\
            WHERE invoiceId = 3 LIMIT 3")
results = cur.fetchall()
# cur.fetchmany(3)
print(results)

cur.close()
db.commit()
db.close()