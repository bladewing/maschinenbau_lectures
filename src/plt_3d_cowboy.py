import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

plt.rcParams["text.usetex"] = True

fig = plt.figure(layout="constrained")
ax = fig.add_subplot(projection="3d")
X, Y = np.meshgrid(X=np.arange(-5, 5, 0.25), Y=np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False
)
ax.set_zlim(-1.01, 1.01)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("$\sin (\sqrt{x^2 + y^2})$")
fig.colorbar(surf, shrink=0.5, aspect=10, location="left")
plt.show()
