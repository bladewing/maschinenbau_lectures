import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)

# erzeugt virtuellen Plot mit zwei Achsen
plt.plot(x, y)

# Zeigt den Plot an
plt.show()
