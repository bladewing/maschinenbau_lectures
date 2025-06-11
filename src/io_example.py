# -*- coding: utf-8 -*-
# textdateilesen.py

print("Codebeispiel 1")

f = open("testdatei.txt", "rt")

anzahl_zeilen = 0

while True:
    zeile = f.readline()
    if not zeile:
        break
    zeile = zeile.rstrip()
    print(zeile)
    anzahl_zeilen = anzahl_zeilen + 1
f.close()

print("Gelesen wurden ", anzahl_zeilen, "Textzeilen.")

# ----------------------------------------------------

print("Codebeispiel 2")


def verarbeite(s, liste):
    print(s.strip())
    liste.append(s)


L = []

f = open("testdatei.txt", "rt")
for zeile in f:
    verarbeite(zeile, L)

f.close()
# ----------------------------------------------------


print("Codebeispiel 3")

f = open("testdatei.txt", "rt")
lst = f.readlines()
f.close()
print("Liste mit ", len(lst), "Elementen")
print("Gesamte Liste:"), print(lst)

lst = [zeile.strip() for zeile in lst]

print("Entfernung der Zeilenumbrueche")
print("Gesamte Liste:"), print(lst)
