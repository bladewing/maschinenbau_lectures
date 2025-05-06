studentin = (87556, "s74331", "Anke", "Hinz", 2.1)
student = (87554, "s75201", "Hannes", "Kunz", 1.7)

paerchen = (studentin, student)  # das ist ein verschachtelter Tupel
print(paerchen)

# studentin[4]='Hinz-Kunz' funktioniert nicht
student = (87554, "s75201", "Hannes", "Kunz-Hinz", 1.7)
print(paerchen)  # bildet aber den Wert ab, als Tupel belegt wurde

paerchen = (studentin, student)  # Neuzuweisung
print(paerchen)
