from functools import reduce  # wichtig import notwendig
import math


def rfun(a, b):
    return math.sqrt(a**2 + b**2)


Zahlen = [10.1, 12.6, 9.8, 11.2]

Reduziert = reduce(rfun, Zahlen)
# wirkt wie rfun(rfun(rfun(10.1,12.6),9.8),11.2)

Prod = reduce(lambda a, b: a * b, Zahlen)
# Berechnet Produkt über alle Elemente
