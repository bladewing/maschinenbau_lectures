# -*- coding: utf-8 -*-
# beispiel4_beschleunigung.py

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(["science", "ieee"])

tmax = 20
dt = 0.1  # Zeitschrittweite
a = 3.5  # konstante. Beschl.
t = np.arange(0, tmax + dt, dt)
s = np.zeros(len(t))
v = np.zeros(len(t))
s[0] = 0
v[0] = 0

# Schrittweise Berechnung der jeweiligen Folgewerte
for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + v[i] * dt
    v[i + 1] = v[i] + a * dt


# Ausgabe als Diagramme mit subplots
zweidiagramme = plt.figure(layout="constrained")
d1 = zweidiagramme.add_subplot(2, 1, 1)
d1.plot(t, v)
d1.set_xlabel(r"Zeit $t$ in s")
d1.set_ylabel(r"Geschw. $v$ in $\frac{\mathrm{m}}{\mathrm{s}}$")
d2 = zweidiagramme.add_subplot(2, 1, 2)
d2.plot(t, s)
d2.set_xlabel(r"Zeit $t$ in s")
d2.set_ylabel(r"gefahrene Wegstrecke $s$ in $\mathrm{m}$")
plt.savefig("fig/sim_growth_2nd.pdf")
plt.show()
