a = 10
def fun():
    global a
    a = 15
    print(a)
fun()
print(a)

# Uzdevums 
import random
a = int(random.random()*100)
b = int(random.random()*100)
def swap():
    global a, b
    print(a, b) # piem 31 51
    # Jāsamaina a un b vietām
    # ...
    c = a
    a = b
    b = c
swap()
print(a, b) # piem 51 31

x = 0
for i in range(0,10):
    x += i
print(x)

x = 0
i = 0
while i < 10:
    x += i
    i += 1
print(x)
