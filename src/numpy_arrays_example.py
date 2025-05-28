import numpy as np

matrix = np.array([[1, -1, 2], [3, 2, 0], [-1, 0, 3]])
print(matrix)

zeilenvektor1d = np.array([1.0, 1.2, 1.3, 1.4])
print(zeilenvektor1d)
zeilenvektor2d = np.array([[1.0, 1.2, 1.3, 1.4]])
print(zeilenvektor2d)

spaltenvektor = np.array([[11], [12], [13]])
print(spaltenvektor)

e = matrix[2, 0]  # 3. Zeile, 1. Spalte

f = zeilenvektor1d[2]  # 3. Element
g = zeilenvektor2d[0, 2]  # 3. Element (1. Zeile, 3. Spalte)

h = spaltenvektor[1, 0]  # 2.Element (2. Zeile, 1. Spalte)

zeile1 = matrix[0, :]  # 1. Zeile, alle Spalten
spalte2 = matrix[:, 1]  # 2. Spalte, alle Zeilen
# Slicing (Auswahl von Bereichen mit start:stop:step)
linksoben = matrix[0:2, 0:2]

sm = matrix.shape  # ergibt Tupel (3,3)
sz1d = zeilenvektor1d.shape  # ergibt Tupel (4)
Sz2d = zeilenvektor2d.shape  # ergibt Tupel (1,4)
ss = spaltenvektor.shape  # ergibt Tupel (3,1)
