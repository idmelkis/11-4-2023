# Uzdevums:
# Uzrakstīt programmu, kas izveido vārdnīcu ar atslēgām no 1..n, un šo atslēgu vērtībām - 
# gadījumskaitļiem (random).
# import random
# n = int(input("Skaitlis n:"))
# vardnica = {}
# for i in range(1, n+1):
#     vardnica[i] = random.randint(0, 100)
#     #vardnica[i] = int(random.random()*100)
#     #vardnica.update({ i: random.randint(0, 100) })
# print(vardnica)

# Uzdevums
# Izveidot vārdnīcu 3, kas satur atslēgas un vērtības no vardnica1 un vardnica2
import random
vardnica1 = {
    1: 10,
    "2": 20,
    3: random.randint(0, 100)
}
vardnica2 = {
    4: 40,
    5: "50",
    6: random.randint(0, 100)
}
vardnica3 = {}
# for i,j in vardnica1.items():
#     vardnica3[i] = j
# for i,j in vardnica2.items():
#     vardnica3[i] = j
for i in (vardnica1, vardnica2):
    vardnica3.update(i)
print(vardnica1)
print(vardnica2)
print(vardnica3)

# Uzdevums
# Izveidot vārdnīcu no sarakstiem keys un values, kur keys ir atslēgas, un values ir vērtības
# Ir garantēts, ka keys un values sarakstu garumi ir vienādi.
import random
keys = [ 1, 2, "10", 3, random.randint(0, 100) ]
values = [ "viens", 4, False, [1,3,4], random.randint(0, 100) ]

# vardnica = {}
# for i in range(0, len(keys)):
#     vardnica[keys[i]] = values[i]
# print(vardnica)
print(dict(zip(keys, values)))

# Uzdevums (i/ni)
# Uzrakstīt programmu, kas izveido vārdnīcu, kas satur atslēgas un vērtības no 
# mainīgā "vardnica", kur vērtības ir > 500
# Piemērs, ja vardnica = {0: 713, 1: 175, 2: 829, 3: 742, 4: 185 }
# tad vardnica2 = { 0: 713, 2: 829, 3: 742 }
# (vērtības atslēgām 1 un 4 ir < 500, tādēļ tās netiek pievienotas)
import random
vardnica = {}
for i in range(0, 100):
    vardnica[i] = random.randint(0, 1000)
print(vardnica)
# ...