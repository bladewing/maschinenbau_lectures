# -*- coding: utf-8 -*-
# beispiel2_fahrt_plot_s_v.py
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

dt = 0.1  # Zeitschrittweite 0.1 sek
tmax = 10  # Simulationszeit 10 sekunden
S = 0
vmax = 30  # 30 m/s

# auf t-Vektor werden alle Zeitwerte erzeugt
t = np.arange(0, tmax + dt, dt)
# für alle Zeitwerte ein Element
s = np.zeros(len(t))
v = np.zeros(len(t))
s[0] = S


def select_v(t, vmax):
    if t <= 2:
        return 0
    elif t > 2 and t < 4:
        return (t - 2) * vmax / 2
    elif t >= 4 and t < 7:
        return vmax
    elif t >= 7:
        return vmax - (t - 7) * vmax / 3
    else:
        return 0  # ausserhalb


for i in range(0, len(t) - 1):
    # v wird aus Vorgabe in Teiltintervallen
    # festegelegt
    v[i] = select_v(t[i], vmax)

    # Schritt-Berechnung
    s[i + 1] = s[i] + v[i] * dt

# Korrektur, da letzter v-Wert nicht in Zyklus berechnet wird
v[len(t) - 1] = v[len(t) - 2]

# Ausgabe als Diagramme mit subplots
plt.style.use(["science", "ieee"])
zweidiagramme = plt.figure(layout="constrained")
d1 = zweidiagramme.add_subplot(2, 1, 1)
d1.plot(t, v)
d1.set_xlabel(r"Zeit $t$ in s")
d1.set_ylabel(r"Geschw. $v$ in $\frac{\mathrm{m}}{\mathrm{s}}$")
d2 = zweidiagramme.add_subplot(2, 1, 2)
d2.plot(t, s)
d2.set_xlabel(r"Zeit $t$ in s")
d2.set_ylabel(r"gefahrene Wegstrecke $s$ in m")
plt.show()
