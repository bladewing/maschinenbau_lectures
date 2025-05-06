menge1 = {"rot", "gruen", "blau"}
print(menge1)
menge1.remove("blau")
print(menge1)
menge1.add("gelb")
print(menge1)
menge1.add("gruen")  # kein Effekt, da schon vorhanden
print(menge1)

if "rot" in menge1 and "gruen" in menge1 and "gelb" in menge1:
    print("alle Ampelfarben vorhanden")
