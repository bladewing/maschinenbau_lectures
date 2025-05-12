import math


# isclose() ersetzt ==-Vergleich
def mehrheit(a, b, c):
    if math.isclose(a, b):
        return a
    if math.isclose(b, c):
        return b
    if math.isclose(a, c):
        return a
