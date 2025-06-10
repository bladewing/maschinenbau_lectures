# Funktion ist vektor-geeignet
import numpy as np


def dreh_position(xm, ym, r, winkel_rad):
    xp = np.sin(winkel_rad) * r + xm
    yp = np.cos(winkel_rad) * r + ym
    return xp, yp


xm = 10
ym = 10
r = 5
winkel_grad = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
winkel_rad = winkel_grad / 180 * np.pi  # alle 13 Elemente umrechnen
# ergebnis ist auch numpy.array
xp, yp = dreh_position(xm, ym, r, winkel_rad)

for i in range(0, len(winkel_grad)):
    print((round(xp[i], 2), round(yp[i], 2)))
