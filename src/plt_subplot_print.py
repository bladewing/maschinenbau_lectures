# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

m_2022_05 = np.array(
    [
        40.10,
        41.36,
        43.26,
        45.27,
        47.48,
        48.27,
        50.35,
        52.84,
        54.56,
        56.54,
        58.54,
        60.11,
        66.70,
        67.35,
        68.41,
        69.74,
        71.23,
        71.47,
        71.72,
        68.60,
        61.27,
        61.03,
        61.24,
        61.56,
        62.07,
        62.28,
        62.43,
        62.25,
    ]
)
m_2023_05 = np.array(
    [
        48.21,
        48.69,
        49.93,
        51.80,
        58.16,
        63.06,
        63.38,
        63.04,
        66.40,
        69.42,
        73.90,
        82.42,
        69.30,
        71.38,
        74.47,
        76.46,
        76.06,
        76.15,
        77.52,
        79.16,
        81.48,
        88.07,
        90.16,
        90.35,
        89.67,
        90.07,
        70.95,
        71.31,
    ]
)

tage = np.arange(1, 29, 1)

beideplots = plt.figure(layout="constrained", figsize=(16 / 2.54, 9 / 2.54))
verlauf1 = beideplots.add_subplot(2, 1, 1)
verlauf1.set_title("2022")
verlauf1.plot(tage, m_2022_05, "+")
verlauf1.set_xlabel("Tage (Monat Mai)")
verlauf1.set_ylabel("Gewicht (kg)")
verlauf2 = beideplots.add_subplot(2, 1, 2)
verlauf2.set_title("2023")
verlauf2.plot(tage, m_2023_05, "+")
verlauf2.set_xlabel("Tage (Monat Mai)")
verlauf2.set_ylabel("Gewicht (kg)")


plt.show()
