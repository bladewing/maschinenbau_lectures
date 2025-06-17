# -*- coding: utf-8 -*-
# beispiel1_wachstum.py

import numpy as np
import matplotlib.pyplot as plt

dt = 1  # Zeitschrittweite 1 sek
tmax = 20  # Simulationszeit 20 sekunden
K = 0.5
S = 2

t = np.arange(0, tmax + dt, dt)
y = np.zeros(len(t))
y[0] = S

for i in range(0, len(t) - 1):
    y[i + 1] = y[i] + K * y[i] * dt

print("t \t y(t)")
for i in range(0, len(t)):
    print(t[i], "\t", round(y[i], 4))
# Ausgabe als Diagramm

plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Exponential Growth Simulation")
plt.xlim(min(t), max(t))
plt.ylim(min(y), max(y))
plt.tight_layout()
plt.show()
