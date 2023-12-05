# pop
# saraksts.pop(idx) vardnica.pop(key)
saraksts = [ 123, 421, 63 ]
saraksts.pop(1)
print(saraksts)

vardnica = {
    "atslega1": 231,
    "atslega2": False,
    324: 324
}
print(vardnica.pop("atslega1"))
print(vardnica)

# Uzdevums
# Izņemt no vārdnīcas 'vardnica' katru otro atslēgu (pāra skaitļus)
import random
vardnica = {}
for i in range(0, 100):
    vardnica[i] = random.randint(0, 100)
atslegas = list(vardnica.keys())
for i in atslegas:
    if i % 2 == 0:
        vardnica.pop(i)
print(vardnica)

# JSON
import json
vardnica = {
    "atslega1": 231,
    "atslega2": False,
    324: 324
}
# Darbs ar string
print(json.dumps(vardnica))
vardnica = json.loads('{"atslega1": 231, "atslega2": false, "324": 324}')
print(vardnica['atslega1'])
print(vardnica)

# Darbs ar failiem
# Links uz open definīciju: https://docs.python.org/3/library/functions.html#open
with open('fails.txt', 'a') as f:
    f.writelines('12333\n')

# Uzdevums
# Izvadīt failā 'fails.txt' skaitļus no 1 līdz 100
# katrā rindā jābūt 1 skaitlim.
with open('fails.txt', 'w') as f:
     for i in range(1, 101):
        f.writelines(str(i) + '\n')

# Lasīšana
with open('fails.txt', 'r') as f:
    # Saraksts ar visām rindām
    # print(f.readlines())
    rinda = f.readline()
    while rinda:
        # Kaut kāda apstrāde...
        print(rinda)
        rinda = f.readline()

import json
# Saglabāšana failā
with open('fails.txt', 'w') as f:
    vardnica = {
        "atslega1": 231,
        "atslega2": False,
        324: 324
    }
    json.dump(vardnica, f)

# Ielādēšana no faila
with open('fails.txt', 'r') as f:
    vardnica = json.load(f)
    print(vardnica["atslega1"])

# Uzdevums: 
# Izveidot programmu, kas ļauj ievadīt 5 vārdus
# Šos vārdus glabāt sarakstā
# Kad vārdi ir ievadīti - saglabāt tos json formātā failā 'fails.json'.
saraksts = []
for i in range(0,5):
    saraksts.append(input("Vārds: "))
with open('fails.txt', 'w') as f:
    json.dump(saraksts, f)
