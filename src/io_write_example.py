z = [3, 16, 21, 30, 31, 36]
string = "Lottozahlen Tippvorschlag:"
for i in range(0, 6):
    string = string + str(z[i]) + " "
string = string + "\n"

f = open("ausgabedatei.txt", "wt")
f.write(string)
f.close()

# ------------------------------------------------


#          Datum,   Tmax,  Tmin, Tdurchschn
daten = [
    ((2023, 5, 25), 24.4, 10.3, 13.5),
    ((2023, 5, 26), 25.8, 11.4, 15.0),
    ((2023, 5, 27), 27.6, 13.8, 18.6),
]

f = open("temperaturen.txt", "wt")

for element in daten:
    f.write(str(element) + "\n")

f.close()

# ------------------------------------------------
# wieder einlesen ...

f = open("temperaturen.txt", "rt")

daten_gelesen = []
for zeile in f:
    daten_gelesen.append(eval(zeile.strip()))

f.close()

# Testausgabe
print(daten_gelesen)
