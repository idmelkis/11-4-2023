#x = input("Vārds: ")
#print(x)

#print(int(x))
#print(float(x))

# Formatēšanas varianti float
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
x = 0.33333
print(f"{str(x)[:4]}")

x = [ "āboli", "banāni", str(3) ]
print(x)
y = [ 123, 456, 789 ]
x[1] = "ķirši"
print(x)
print(x[2])

print("Tests"[1:3])
print(x[:2]) # Izvada sarakstu
print(",".join(x))

x.append("Vērtība")
print(x)

# Ievade: Cilvēka <vārds>
# Izvade: Sveiks <vārd>!
# Piemērs: 
# Ievade: Jānis
# Izvade: Sveiks Jāni!
# x = "vārds"
# ...
#x = input("Cilvēka vārds: ")
#print(f"Sveiks {x[:-1]}!")

x = ( "...", "..." )
x[2] = "123"

#x = "123" == "123" # x = True
x = True
#if x == True:
if not x:
    print("Patiess")
else:
    print("Nepatiess")

# Kalkulators
# Ievade: divi (vai vairāk*) skaitļi (ar input)
# Ievade: Darbība (Saskaitīt, atņemt, dalīt, reizināt...)
# Izvade: Darbības rezultāts