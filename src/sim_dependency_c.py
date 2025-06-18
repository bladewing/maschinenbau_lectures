import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(["science", "ieee"])

tmax = 160
dt = 1 / 12
t = np.arange(0, tmax + dt, dt)
b = np.zeros(len(t))
w = np.zeros(len(t))
b[0] = 2000
Kb = 0.6
Nb = 4000
w[0] = 20
Kw = 0.1
Nw = 1000

kr = 1.1

wolf_t = 0
for i in range(0, len(t) - 1):
    wolf_t = wolf_t + dt
    if wolf_t >= 10:
        ew = w[i] * 0.4
        wolf_t = 0
    else:
        ew = 0
    b[i + 1] = max(0, b[i] + (Kb * b[i] * (1 - b[i] / Nb) - kr * w[i]) * dt)
    w[i + 1] = w[i] + (Kw * w[i] * (1 - w[i] / Nw)) * dt - ew


plt.plot(t, b, t, w)
plt.xlabel("$t$ in a")
plt.ylabel("Population")
plt.legend(("Wildschweine", "Wölfe"))
plt.xlim([0, tmax])
plt.savefig("fig/sim_dependency_c.pdf")
plt.show()
