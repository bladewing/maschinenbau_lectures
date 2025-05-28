import numpy as np

Zv = np.array([[1, 2, 3, 4]])
Sv = np.array([[1], [3], [5], [7]])
skalar_prod = np.dot(Zv, Sv)
print(skalar_prod)

kreuz_prod = np.dot(Sv, Zv)
print(kreuz_prod)
