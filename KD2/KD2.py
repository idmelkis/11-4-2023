# Var pildīt mājās. Termiņš līdz nākošajai nedēļai. Par katru uzdevumu ir līdz 3 punktiem - 3 ir perfekti izpildīts, 2 ir izpildīts bet ar mazām kļūdām, 1 ir 'iesākts', un 0 ir 'neiesākts'.
# Dotos koda piemērus nemainīt - tikai papildināt

# 1. Uzdevums - piekļuve vārdnīcu vērtībām
# Ir dota sekojoša programma. Papildinat to, lai izvadītu atslēgu un vērtību pāri lielākajai un mazākajai dict1 vērtībai.
# piemēram vārdnīcai { 0: 100, 1: 2, 3: 400 } rezultāts būtu - "Lielākā - 3: 400, mazākā 1: 2".
import random
dict1 = {}
for i in range(0,100):
    dict1.update({i: random.randint(0, 1000)})
# ...

# 2. Uzdevums - vārdnīcu apvienošana
# Ir dotas divas vārdnīcas - dict1 un dict2. Izveidot programmu, kas izveido vārdnīcu
# dict3, kas satur atslēgas un tām atbilstošo vērtību summu no dict1 un dict2.
# piemēram
# ja dict1 = {
# "a": 10,
# "b": 20
# }
# un dict2 = {
# "a": 10,
# "b": 80
# },
# tad dict3 = {
# "a" 20,
# "b": 100
# }.
import random
dict1 = {
 "a": 10,
 "b": random.randint(0,100),
 "c": 30,
 random.randint(0,100): random.randint(0,1000),
 random.randint(0,100): random.randint(0,1000),
 random.randint(0,100): random.randint(0,1000),
}
dict2 = {
 "a": 10,
 "b": random.randint(0,100),
 "c": 70,
 random.randint(0,100): random.randint(0,1000),
 random.randint(0,100): random.randint(0,1000),
 random.randint(0,100): random.randint(0,1000),
}
dict3 = {}

# 3. Uzdevums - Vērtību dzēšana
# Ir dota sekojoša programma, kas izveido vārdnīcu dict1. Papildinat šo programmu tā,
# lai šī programma izveidotu _izdzēstu_ vērtības no dict1, kas ir mazākas par 500.
# Nedrīkst veidot atsevišķu vārdnīcu vai papildus mainīgos - visām darbībām jānotiek ar dict1.
import random
dict1 = {}
for i in range(0,100):
    dict1.update({i: random.randint(0, 1000)})

# 4. Uzdevums - Vērtību ielāde un apstrāde
# Ir dots fails 'uzdevums.json'. Šis fails satur vārdnīcu json formātā. Atverat šo failu un izvadat šīs vārdnīcas vērtības formātā 
# "Atslēga: <atslēga>, Vērtība: <vērtība>" (ieskaitot leņķa iekavas - <>).


# 5. Uzdevums - Vērtību glabāšana
# Izveidot programmu, kas nodrošina -
# Vairāku (! - saraksts) cilvēku informācijas ievadi - vārdu, uzvārdu, vecumu. Informāciju par individuālu cilvēku glabāt vārdnīcā ar atslēgām "vards", "uzvards" un "vecums".
# Šīs informācijas izvadi failā ar nosaukumu 'dati.json'.

