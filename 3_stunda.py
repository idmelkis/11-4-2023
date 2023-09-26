# while, for
#while <nosacījums>:
#    ...
for x in range(0, 11):
    print(x)
x = 0
while x < 11:
    print(x)
    #x += 1
    x = x + 1

x = [ 0, 1, 2, 4, 6, 8 ]
for y in x[0::2]:
    print(y)

# # Uzrakstat while un for ciklus, kurā jūs ievadat 5 vērtības sarakstā
# # x.append(...)
# While...
x = [] # Saraksts kurā glabāsies vērtības
y = 0 # Skaitītājs priekš while cikla
while y < 5:
    x.append(input("Vērtība: "))
    y += 1
print(x)

# For...
x = []
for y in range(0,5):
    x.append(input("Vērtība: "))
print(x)

# break un continue
while True:
    print("Pirmais cikls")
    y = 0
    while True:
        y += 1
        if y == 3:
            continue
        print(y)
        if y >= 5:
            break
    break

# Uzrakstat while ciklu, kas izvada skaitļus no 0 līdz 10 izlaižot skaitļus 4 un 6.
x = 0
while x <= 10:
    #if x != 6 and x != 4:
    #    print(x)
    if x == 6 or x == 4:
        continue
    print(x)
    x += 1

# FizzBuzz
# Ciklā jāizvada skaitļi no 1 līdz 100, BET
# Ja skaitlis dalās ar 3, tad skaitļa vietā izvadam Fizz
# Ja skaitlis dalās ar 5, tad skaitļa vietā izvadam Buzz
# Ja dalās gan ar 3, gan ar 5, tad izvadam FizzBuzz
# Atlikuma pārbaude piem. x % 3 == 0 [modulus operators - izvada dalījuma atlikumu]
# Piemērs izvadei:
# 0
# 1
# 2 
# Fizz
# 4
# Buzz
# Fizz
# 7
# ...
# 14
# FizzBuzz
# 16
# ...

# Izveidojat programmu ar sekojošu izvadi (jāizmanto for cikli)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
