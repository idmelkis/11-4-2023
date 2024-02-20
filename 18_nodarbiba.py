# import os
# with open("fails.txt", 'w'):
#     pass
# os.path.exists()
# if os.path.isfile("fails.txt"): #os.path.isdir()
#     print("Eksistē")
# else:
#     print("Neeksistē")
import os
path = os.path.dirname(__file__)
# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# ./ - Pašreizējā mape
# .. - Iepriekšējā mape
# ../.. - Divas mapes augstāk == ..\\..
# with open(f"{path}\\..\\fails.txt", 'w'):
#     pass
# if not os.path.isdir(f"{path}\\mape"):
#     os.mkdir(f"{path}\\mape")
#     with open(f"{path}\\mape\\fails.txt", 'w'):
#         pass
#os.rmdir(f"{path}\\mape")
# Dzēšana 1. variants
#import shutil
#shutil.rmtree(f"{path}\\mape")
# Dzēšana 2. variants
# for file in os.listdir(f"{path}\\mape"):
#     print(f"Dzēšam {file}")
#     os.remove(f"{path}\\mape\\{file}")
# os.rmdir(f"{path}\\mape")

# Šādi labāk neizdarīt - var aizmirst aizvērt
# fails = open("fails.txt", 'w')
# fails.close()

#with open("fails.txt", 'w') as f:
    #f.write("asdasd")
    #f.seek(0,0)
    #f.writelines(["asd", "asd"])

# with open("fails.txt", 'r') as f:
#     for line in f:
#         darbiba = line.strip()
#         #for letter in darbiba:
#         #...
#         darbiba = darbiba.split(" ")
#         if darbiba[1] == "*":
#             rez = int(darbiba[0]) * int(darbiba[2])
#             print(rez)

# Uzdevums
# Atvērt failu fails.txt
# faila saturs
# 10 * 8
# 10 / 2
# 4 - 3
# Veikt katrā rindā attēlotu darbību
# Izvadīt darbības rezultātu

import csv
# with open("fails.txt", 'r') as f:
#     csv_read = csv.reader(f, delimiter=" ")
#     next(csv_read)
#     for line in csv_read:
#         print(line)
with open("fails.txt", 'w') as f:
    #print(end="\n")
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(["col1","col2"])
    writer.writerow(["val1","val2"])
    writer.writerow(["val3","val4"])
