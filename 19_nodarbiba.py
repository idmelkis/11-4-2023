# # Izveidojat mapi "faili". 
# import os

# # Vajadzētu arī pārbaudīt vai mape eksistē pirms izveides
# os.mkdir('faili')

# # Izveidojat mapē failus ar nosaukumiem no 0 līdz 100. 
# import random
# for i in range (0, 101):
#     with open(f"faili/{i}", 'w') as f:
#         # Katrā failā noglabājat gadījumskaitli.
#         f.write(str(random.randint(0, 10000)))
# # Prasat lietotājam atvērt kādu no šiem failiem, un ievadīt vērtību, kas ir failā. 
# # Alt: os.listdir(f"{path}\\mape"), un izvēlās vienu failu no saraksta
# file = random.randint(0, 100)
# inp = input(f"Kas atrodās failā {file}? :")

# # Atkarībā no tā vai ievadīts pareizi, izvadīt "pareizi", vai "nepareizi".
# with open(f"faili/{file}", 'r') as f:
#     saturs = f.readline()
#     if saturs == inp:
#         print("Pareizi")
#     else:
#         print("Nepareizi")

# # Kad programma beidz darbu, izdzēšat šo mapi.
# import shutil
# shutil.rmtree("faili")

# 2. uzdevums
# with open('fails.txt', 'r') as f:
#     line = f.readline().strip()
#     splitLine = line.split(" ")
#     print(f"Failā ir {len(splitLine)} vārdi")

# 3. uzdevums
# * atver šo failu
with open('fails.txt', 'r') as f:
  import os
  # from pathlib import Path
  # upperFilename = Path("fails.txt").stem+"_uppercase.txt"
  # upperFilename = "fails.txt".split(".")[0]+"_uppercase.txt"
  upperFilename = 'fails_uppercase.txt'
  if not os.path.exists(upperFilename):
    with open(upperFilename, 'w') as uf:
        for line in f:
          uf.write(line.upper())
  else:
    print("Fails jau eksistē!")
    #raise Exception("Fails jau eksistē!")