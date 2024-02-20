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

with open("fails.txt", 'r') as f:
    for line in f:
        print(line.strip())

# Uzdevums
# Atvērt failu fails.txt
# Veikt katrā rindā attēlotu darbību
# Izvadīt darbības rezultātu
