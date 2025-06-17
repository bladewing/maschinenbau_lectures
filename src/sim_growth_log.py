# -*- coding: utf-8 -*-
# beispiel3_log_wachstum.py

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(["science", "ieee"])

# y(0) = 2;
# y(t+dt) = y(t) + y'(t) * dt
# y'(t) = k * y(t) * (1-y(t)/N)
dt = 1
tmax = 20
S = 2
K = 0.5
N = 150
# alle Zeitwerte erzeugt
t = np.arange(0, tmax + dt, dt)

y = np.zeros(len(t))
y[0] = S

for i in range(0, len(t) - 1):
    y[i + 1] = y[i] + K * y[i] * (1 - y[i] / N) * dt


plt.plot(t, y)
plt.title(r"Logistisches Wachstum $K=0.5$, $N=150$")
plt.xlabel("Zeit")
plt.ylabel("Systemgröße")
plt.savefig("fig/sim_growth_log.pdf")
plt.show()
