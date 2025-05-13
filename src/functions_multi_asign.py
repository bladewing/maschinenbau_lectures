import math

a = 1.0
b = 2.0

a, b = b, a  # tauschen der Werte a,b

# Berechnung eines x- und eines y- Auslenkungswerts
w = 0.5 * math.pi
r = 1.0
x, y = r * math.sin(w), r * math.cos(w)
