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
vardnica = {}
with open('20_nodarbiba.ini', 'r', encoding='utf-8') as f:
    nosaukums = ''
    for line in f:
        if line.startswith('['):
            # [date]
            nosaukums = line[line.index('[') + 1 : line.index(']')]
            vardnica[nosaukums] = {}
        if line.find('=') != -1:
            vertiba = line.split('=')
            vardnica[nosaukums][vertiba[0].strip()] = vertiba[1].strip()
        else:
            continue
print(vardnica)
