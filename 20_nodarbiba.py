# Uzdevums:
# Ielādēt failu (20_nodarbiba.ini)
# Ielādēt datus vārdnīcā
# Formāta piemērs:
# { 'date': { 'year': 2024, 'date': 25, ...}, ...}
# http://s.ayy.lv/11-4

# 1. Atvērt failu
# 2. Nolasīt katru rindu
# 2.1. Ja rinda [], tad tad ievietot to vārdnīcā
# 2.2. Ja rinda ar =, tad ievietot to vārdnīcā zem []
# 2.3. Ja rinda ir tukša, neko nedarīt
# vardnica = {}
# with open('20_nodarbiba.ini', 'r', encoding='utf-8') as f:
#     nosaukums = ''
#     for line in f:
#         if line.startswith('['):
#             # [date]
#             nosaukums = line[line.index('[') + 1 : line.index(']')]
#             vardnica[nosaukums] = {}
#         if line.find('=') != -1:
#             vertiba = line.split('=')
#             vardnica[nosaukums][vertiba[0].strip()] = vertiba[1].strip()
#         else:
#             continue
# print(vardnica)
# import configparser
# from pathlib import Path
# fails = Path('20_nodarbiba.ini')
# config = configparser.ConfigParser()
# config.read(fails)
# #print(config.sections())
# #print(config['date']['year'])

# new_config = configparser.ConfigParser()
# new_config['kaut_kas'] = {}
# new_config['kaut_kas']['kaut_kas_1'] = '-1'
# new_config['kaut_kas']['kaut_kas_2'] = '0'
# with open('20_nodarbiba_.ini', 'w') as f:
#     new_config.write(f)

class Gens:
    simbols :str
    hgnc :str
    ens :str
    def __init__(self, symb, hgnc, ens) -> None:
        self.simbols = symb
        self.hgnc = hgnc
        self.ens = ens

dati = {} # simbols: Gens
with open('20nodarbiba_uzd\\mart_export_human_filtered.txt', 'r', encoding='utf-8') as f:
    next(f)
    for line in f:
        l = line.split('\t')
        gens = Gens(l[1].strip(), '', l[0].strip())
        dati[gens.simbols] = gens

with open('20nodarbiba_uzd\\genenames_filtered.txt', 'r', encoding='utf-8') as f:
    next(f)
    for line in f:
        l = line.split('\t')
        simbols = l[1].strip()
        if simbols in dati:
            dati[simbols].hgnc = l[0].strip()

for i,j in dati.items():
    print(f'{i}: {j.ens} un {j.hgnc}')

# DBMS: https://www.geeksforgeeks.org/introduction-of-dbms-database-management-system-set-1/
# ACID: https://en.wikipedia.org/wiki/ACID
    
#import sqlite3