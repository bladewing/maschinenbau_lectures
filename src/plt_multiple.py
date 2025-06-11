import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
x2 = np.arange(-1.5 * np.pi, 1.5 * np.pi, 0.1)

y1 = np.sin(x1)
y2 = np.cos(x2)

plt.figure(figsize=(16 / 2.54, 9 / 2.54))
plt.plot(x1, y1, x2, y2)
plt.xlabel("x")
plt.ylabel("y=f(x)")

plt.show()
