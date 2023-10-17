# Uzdevums (i/ni), jāiesniedz e-klasē
# "Uzmini skaitli" spēli
# Tiek uzģenerēts skaitlis no 0 līdz 100 
#import random
#x = int(random.random()*100)
# (Ciklā) - līdz lietotājs uzvar spēli (uzmin skaitli):
# lietotājs ievada skaitli
# Programma saglabā lietotāja ievadi (sarakstā)
# Programma pārbauda vai ievadītais skaitlis ir vienāds ar uzģenerēto
# Ja nav, programma izvada to, vai ģenerētais skaitlis ir lielāks/mazāks
# Ja ir - lietotājs uzvar spēli, programma izvada tekstu 'Uzvara', un
# izvada visus lietotāja minējumus, kopā ar minējumu skaitu (len(...)).

# Funkcijas
# def nosaukums(parametrs, parametrs2 = 4):
#     print(parametrs2)
#     return 0
# print(nosaukums(0))

def nosaukums(parametrs :int, parametrs2: int = 4) -> float:
    """Kaut kāda dokumentācija"""
    print(parametrs2)
    def funkcija2(p1):
        print("ok")
    funkcija2(0)
nosaukums(0, 10)

from stunda4.stunda4_fun2 import sum
print(sum(10, 10))

def vairakiParametri(*parametrs):
    print(parametrs)
    print(type(parametrs))
# def vairakiParametri(parametrs):
#     print(parametrs)
vairakiParametri(10,20,30,40,50)

def rec(param):
    print(param)
    if param == 1:
        return
    else:
        return rec(param-1)
rec(10)

x = 10
while not x == 0:
    print(x)
    x = x - 1
print()

# n! = n * n-1 * n-2 (...)
# 3! = 3 * 2 * 1 == 6
# 4! = 4 * 3 * 2 * 1 == 24
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
print(recur_factorial(4))

# Uzdevums: while..?
sk = 4
reizinajums = 1
while not sk == 0:
    reizinajums *= sk
    sk -= 1
print(reizinajums)