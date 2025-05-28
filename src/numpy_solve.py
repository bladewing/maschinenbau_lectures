import numpy as np

A = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
b = np.transpose(np.array([[-3, 5, -2]]))
x = np.linalg.solve(A, b)
print(x)

# Einsetzen x in A*x
btest = np.dot(A, x)
print(btest)  # ... wenn gleich b, dann wurde Gls genau gelöst
