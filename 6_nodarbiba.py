# 1. Uzdevums
# Ir dots kāds vārds, piem. 'Siers'.
# Jāuzraksta programma, kas ar cikla palīdzību atrod un izvada visas burta 'S'
# Pozīcijas. Piemēram vāram 'Siers' burts atrodas 1 un 5 poz.
# Jāatceras, ka piekļūt teksta daļām var tā pat, kā sarakstiem, piem
# ja txt == "Siers", tad txt[1] == "i", txt[2] == "e".
def findLetter(txt):
    y = 0
    while y < len(txt):
        if txt[y] == "s" or txt[y] == "S":
            print(y+1, end=" ")
        y += 1
    
findLetter("Siers") # 1, 5
print()
findLetter("skurstenis") # 1, 5, 10
print()
findLetter("lielas saulesbrilles") # 6, 8, 13, 20
print()

# 2. Uzdevums
# Uzrakstīt programmu, kas ar ciklu (!neizmantot .replace un līdzīgas palīgfunkc.!)
# Samaina vārda garos patskaņus (ā,ū,ē,ī) uz to īsajiem variantiem (a,u,e,i)
# Piem. Māja -> Maja. Mašīna -> Mašina

# def changeLetters(txt):
#     y = 0
#     while y < len(txt):
#         if txt[y] == "ā":
#             print("a", end = "")
#         elif txt[y] == "ē":
#             print("e", end = "")
#         elif txt[y] == "ī":
#             print("i", end = "")
#         elif txt[y] == "ū":
#             print("u", end = "")
#         else:
#             print(txt[y], end = "")
#         y += 1
#     print()
# def changeLetters(txt):
#     y = 0
#     output = ""
#     while y < len(txt):
#         if txt[y] == "ā":
#             output += "a"
#         elif txt[y] == "ē":
#             output += "e"
#         elif txt[y] == "ī":
#             output += "i"
#         elif txt[y] == "ū":
#             output += "u"
#         else:
#             output += txt[y]
#         y += 1
#     return output
def changeLetters(txt):
    y = 0
    while y < len(txt):
        if txt[y] == "ā":
            txt = txt[:y] + "a" + txt[y+1:]
        elif txt[y] == "ē":
            txt = txt[:y] + "e" + txt[y+1:]
        elif txt[y] == "ī":
            txt = txt[:y] + "i" + txt[y+1:]
        elif txt[y] == "ū":
            txt = txt[:y] + "u" + txt[y+1:]
        y += 1
    #for i in range(0, len(txt)):
    #    0_0
    return txt

print(changeLetters("Māja"))
print(changeLetters("Mašīna"))

# 3. Uzdevums
# Mājas pamēģinat - Sarakstu apvienošana izmantojot ciklu
# Piezīme - nav pievienošana galā (.append(), +)
# Piemērs - x1 = [ 10, 20, 30 ], x2 = [ 50, 60, 70 ]
# Rezultāts - [ 10, 50, 20, 60, 30, 70 ]
# Vienkāršākais variants - var pieņemt, ka ievades ir vienāda garuma

# 4. Uzdevums
# Blokshēma un diagramma Spēlei "uzmini skaitli" (2. i/ni darbs)
# Bet ar uzlabojumu - spēlētājam ir 5 dzīvības
# Blokshēmu var veidot vietnē: draw.io
import random
skaitlis = int(random.random()*100)
dzivibas = 5
while dzivibas > 0:
    minejums = int(input("Minējums: "))
    if minejums==skaitlis:
        break
    elif minejums > skaitlis:
        print("Skaitlis ir mazaks")
    else:
        print("Skaitlis ir lielaks")
    dzivibas = dzivibas - 1
if dzivibas > 0:
	print("Uzvara")
else:
	print("Zaudejat")
