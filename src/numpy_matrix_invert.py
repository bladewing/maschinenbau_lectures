import numpy as np

m = [
    [1.1, 2.6, 2.0, -1.2],
    [2.6, 5.0, 3.0, -2.0],
    [2.0, 3.0, 4.0, -1.0],
    [-1.2, -2.0, -1.0, 1.0],
]

m_inv = np.linalg.inv(m)
print(m_inv)

p = np.dot(m, m_inv)
print(p)
print(np.round(p, 4))
