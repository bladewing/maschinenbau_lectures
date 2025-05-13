# Funktion erzeugt große Anfangsbuchstaben
def GB_fun(s):
    return s.capitalize()


L = ["otto", "berta", "emil"]

L1 = list(map(GB_fun, L))
# neu = GB_fun(alt) wird auf jedes Element angewendet

L2 = [(1, 2), (4, 5), (10, 11)]

L3 = list(map(lambda t: (t[1], t[0]), L2))
# lambda-Funktion dreht tupel-Elemente um
# L3 ergibt [(2, 1), (5, 4), (11, 10)]
