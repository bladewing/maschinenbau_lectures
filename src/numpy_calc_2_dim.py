import numpy as np

m_mat = np.array([[1000, 1500, 2000], [1000, 1500, 2000], [1000, 1500, 2000]])

v_mat = np.array([[20, 20, 20], [40, 40, 40], [60, 60, 60]])
e = m_mat / 2 * v_mat**2
print(e)
