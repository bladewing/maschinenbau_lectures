def filter_fun(x):
    return abs(x) >= 0.5


WERTE = [1.2, 3.0, 0.1, -0.05, 2.8, -3.8]

WERTE1 = list(filter(filter_fun, WERTE))
# nur Werte >=0.5 werden in WERTE1 übernommen

NAMEN = ["Fritz", "Peter", "Inga", "Robert", "Michael", "Jan"]

NAMEN1 = list(filter(lambda s: len(s) < 6, NAMEN))
# nur Namen mit weniger als 6 Buchstaben werden übernommen
