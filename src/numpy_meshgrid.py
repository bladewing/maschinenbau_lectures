import numpy as np

m = np.arange(10, 50, 6)  # ab 10 in 6er Schritten, 7 Werte
v = np.arange(8, 22, 4)  # ab 8 in 4er Schritten, 4 Werte

m_mat, v_mat = np.meshgrid(m, v)

e = m_mat / 2 * v_mat**2  # 4x7 Matrix

print(e)
