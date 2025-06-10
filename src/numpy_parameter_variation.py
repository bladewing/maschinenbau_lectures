import numpy as np


# ab 10 in 6er Schritten, 7 Werte
m = np.arange(10, 50, 6)
# ab 8 in 4er Schritten, 4 Werte
v = np.arange(8, 22, 4)

# 4x7 Matrix
m_mat = np.outer(np.ones(len(v)), m)
print(m_mat)

# 4x7 Matrix
v_mat = np.outer(v, np.ones(len(m)))
print(v_mat)

# 4x7 Matrix
e = m_mat / 2 * v_mat**2
print(e)
