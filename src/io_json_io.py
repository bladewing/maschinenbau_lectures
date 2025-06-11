import json

liste = ["carlsberg", "tuborg", "faxe"]

key_value = {"name": "franz", "age": 24, "occupation": "student"}

waren_dict = {
    471121: ("Cola", 0.5, 0.69),
    452312: ("Wasser", 1.0, 0.45),
    481192: ("O-Saft", 1.5, 2.49),
}

menge = {"kaffee", "tee", "sahne", "milch", "zucker"}
menge.add("softeis")


# ----------------- Schreiben -----------------------

s1 = json.dumps(liste, ensure_ascii="False")
s2 = json.dumps(key_value, ensure_ascii="False")
s3 = json.dumps(waren_dict, ensure_ascii="False")
# s4 = json.dumps(menge,ensure_ascii='False')

f1 = open("bierliste.json", "wt")
f1.write(s1)
f1.close()

f2 = open("personen.json", "wt")
f2.write(s2)
f2.close()

f3 = open("waren.json", "wt")
f3.write(s3)
f3.close()

# f4= open('menge.json','wt')
# f4.write(s4)
# f4.close()
# ------------------ Lesen --------------------------

f1 = open("bierliste.json", "rt")
liste_gelesen = json.load(f1)
f1.close()
print("von bierliste.json gelesenes Objekt:", liste_gelesen)

f2 = open("personen.json", "rt")
personen_gelesen = json.load(f2)
f2.close()
print("von personen.json gelesenes Objekt:", personen_gelesen)

f3 = open("waren.json", "rt")
waren_gelesen = json.load(f3)
f3.close()
print("von waren.json gelesenes Objekt:")
print(waren_gelesen)
print("von waren.json gelesene Daten (key : value):")
for nr in waren_gelesen:
    print(nr, ":", waren_gelesen[nr])

# f4= open('menge.json','rt')
# menge_gelesen = json.load(f4)
# f4.close()
