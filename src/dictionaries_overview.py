daten = {
    34554: ("Fritz", "Mayer"),
    34555: ("Robert", "Schulz"),
    34556: ("Lisa", "Mueller"),
}
auswahl = daten[34555]  # ergibt ('Robert', 'Schulz')

if 34556 in daten:
    print(daten[34555])

for mnr in daten:
    print(daten[mnr])

del daten[34555]

daten[34579] = ("Inga", "Krause")  # neu
daten[34554] = ("Friedrich", "Maier")  # ändern
