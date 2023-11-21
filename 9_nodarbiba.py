# saraksts = [12,34,654] # === masīvs
# print(saraksts[0])
# saraksts.append("123")

# vardnica = {
#     "atslēga": ["vērtība"],
# #   atslēga = ["vērtība"]
#     "word": " A sound or a combination of sounds, or its representation in writing or printing, that symbolizes and communicates a meaning and may consist of a single morpheme or of a combination of morphemes.",
#     123: 423,
#     True: False,
#     4123: "3123",
#     "231": 323
# } # === kartēm (map)
# #print(vardnica)
# #print(vardnica["word"])
# vardnica["vērtība"] = "312"
# print(vardnica["vērtība"])
# vardnica.update({"atslēga2": "vērtība", 766: 111})
# print(vardnica[766])

# Uzdevums: Lietotājs ievada skaitli n, un programma izveido vārdnīcu kura satur
# atslēgas no 1 līdz n, ar vērtībām n^2
# Piemērs:
# {
#  1: 1
#  2: 4
#  3: 9
# }
# Ciklā:
#vardnica[1] = 1
#vardnica[2] = 4
# ...
#vardnica = {}
#inp = int(input("Ievadat skaitli"))
# n=1
# while n <= inp:
#     vardnica[n] = n*n # == n**2
#     #vardnica.update({n: n*n})
#     n += 1
# for n in range(1, inp+1):
#     vardnica[n] = n*n # == n**2
# print(vardnica)

# vardnica = {
#     1: 2,
#     "key": "value",
#     # True: False,
#     "something": "something"
# }
# for i in vardnica.keys():
#     print(i)
# for i in vardnica.values():
#     print(i)
# for i,j in vardnica.items():
#     print(f"atslēga: {i}, vērtība: {j}")

# Uzrakstīt programmu, kas ar ciklu (!neizmantot .replace un līdzīgas palīgfunkc.!)
# Samaina vārda garos patskaņus (ā,ū,ē,ī) uz to īsajiem variantiem (a,u,e,i)
# Piem. Māja -> Maja. Mašīna -> Mašina
def changeLetters(txt):
    y = 0
    dictionary = {
        "ā": "a",
        "ē": "e",
        "ī": "i",
        "ū": "u",
        "š": "s"
    }
    output = ""
    while y < len(txt):
        # Ja vērtība ir iekš saraksta
        #if txt[y] in dictionary.keys():
        if txt[y] in dictionary:
            output += dictionary[txt[y]]
        else:
            output += txt[y]
        y += 1
    return output
print(changeLetters("Māja"))
print(changeLetters("Mašīna"))

# Dota vārdnīca
# Jāņem vērā - izmantojot eksistējošu atslēgu tiks pārrakstīta vērtība
# Nav iespējams, ka vārdnīcā ir divas identiskas atslēgas.
vardnica = {
    1: 2,
    2: 3,
    3: 4,
    4: 5
}
# Pārvieto vērtību
#vardnica[5] = vardnica[1]
#vardnica.pop(1)
# Uzdevums: Pacelt visas vērtības kvadrātā
for i in vardnica.keys():
    # Maina vērtību - paceļ kvadrātā
    vardnica[i] = vardnica[i] * vardnica[i]
for i in vardnica.values():
    # Izvada vērtību kvadrātā
    print(i*i)
for i,j in vardnica.items():
    # Maina vērtību - paceļ kvadrātā
    vardnica[i] = j*j
