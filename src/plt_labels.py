import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
# X-Achse beschriften
plt.xlabel("x")
# Y-Achse beschriften
plt.ylabel("sin(x)")
# Titel des Plots
plt.title("Das ist die Sinusfunktion")


plt.show()
