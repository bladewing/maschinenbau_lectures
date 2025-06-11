import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

plt.rcParams["text.usetex"] = True

m = np.array([10, 15, 20, 25, 30])
v = np.array([5, 10, 15, 20, 25])
mm, vv = np.meshgrid(m, v)
EE = mm / 2 * vv**2
fig = plt.figure(layout="constrained")
ax = fig.add_subplot(projection="3d")
ax.plot_surface(
    mm, vv, EE, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False
)
ax.set_xlabel(r"$m \mbox{ in } \mbox{kg}$")
ax.set_ylabel(r"$v \mbox{ in } \frac{\mbox{m}}{\mbox{s}}$")
ax.set_zlabel(r"$E_{kin} \mbox{ in } \mbox{Nm}$")
plt.show()
