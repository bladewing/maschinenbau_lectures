# -*- coding: utf-8 -*-
# beispiel5_pendel.py

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(["science", "ieee"])

dt = 0.001
tmax = 10
t = np.arange(0, tmax + dt, dt)
alpha = np.zeros(len(t))
omega = np.zeros(len(t))
alpha[0] = np.pi / 4
omega[0] = 0
g = 9.81  # Erdbeschleunigung
l = 1.5  # Länge des Pendels
for i in range(0, len(t) - 1):
    omega[i + 1] = omega[i] - g / l * np.sin(alpha[i]) * dt
    alpha[i + 1] = alpha[i] + omega[i] * dt


# Ausgabe als Diagramme mit subplots
zweidiagramme = plt.figure(layout="constrained")
d1 = zweidiagramme.add_subplot(2, 1, 1)
d1.plot(t, alpha)
d1.set_xlabel(r"Zeit $t$ in s")
d1.set_ylabel(r"Winkel $\alpha$ in rad")
d2 = zweidiagramme.add_subplot(2, 1, 2)
d2.plot(t, omega)
d2.set_xlabel(r"Zeit $t$ in s")
d2.set_ylabel(r"Winkelgeschw. $\omega$ in rad/s")
plt.savefig("fig/sim_growth_2nd.pdf")
plt.show()
